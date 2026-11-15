#!/usr/bin/env node
/* Optional: measure how readable the words are where they sit on a painting, and write src/data/legible.json for the audit tables.

     npm install lighthouse            (once; it brings the browser driver this uses. Point LH_HOME at it if it is not local)
     node src/legible.mjs              all samples
     node src/legible.mjs 007 012      only these
     node src/legible.mjs --sheets     also save full-page desktop and phone pictures of every sample to /tmp/ab-check

   A contrast checker cannot read text over a picture, so this does it the slow way. For every line of text on a painted section it
   takes the pixels directly behind that line (with the words hidden), works out the contrast of each pixel against the text colour,
   and keeps the tenth-lowest percentile: the hardest-to-read part of the line, ignoring single stray pixels.
   The bar is WCAG's: 4.5 to 1 for body text, 3 to 1 for large text (24px and up, or 18.66px and up in bold). */
import { createServer } from 'node:http';
import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(process.env.LH_HOME ? join(process.env.LH_HOME, 'x.js') : import.meta.url);
const chromeLauncher = await import(require.resolve('chrome-launcher'));
const puppeteer = (await import(require.resolve('puppeteer-core'))).default;

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const TYPES = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.xml': 'application/xml', '.txt': 'text/plain' };
const args = process.argv.slice(2);
const sheets = args.includes('--sheets');
const only = args.filter(a => !a.startsWith('--'));
const VIEWS = [['desktop', 1280, 800], ['phone', 390, 844]];

const server = createServer((req, res) => {
  const file = join(ROOT, decodeURIComponent(req.url.split('?')[0]));
  if (!existsSync(file)) { res.writeHead(404); return res.end('not found'); }
  let body = readFileSync(file);
  // the web-font request is dropped so this runs offline (install the fonts to match), and pictures are decoded before the capture, not after
  if (file.endsWith('.html')) body = body.toString().replace(/<link rel="preconnect"[^>]+>\n/g, '').replace(/<link href="https:\/\/fonts\.googleapis\.com[^>]+>\n/, '')
    .replaceAll('decoding="async"', 'decoding="sync"').replaceAll('loading="lazy"', 'loading="eager"');
  res.writeHead(200, { 'content-type': TYPES[extname(file)] || 'application/octet-stream' });
  res.end(body);
});
await new Promise(r => server.listen(0, r));
const port = server.address().port;
const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars'] });
const browser = await puppeteer.connect({ browserURL: `http://127.0.0.1:${chrome.port}` });
const bench = await browser.newPage();   // a blank page used only to read pixels back out of each picture
const file = join(ROOT, 'src/data/legible.json');
const out = existsSync(file) ? JSON.parse(readFileSync(file)) : {};
if (sheets) mkdirSync('/tmp/ab-check', { recursive: true });

/* Runs in the page: every line of text that sits on a painting, with its colour and size. Text on a solid button or card is skipped,
   because the build already checks those colour pairs. */
function lines() {
  const found = [];
  const zones = [...document.querySelectorAll('.bleed, .over .hdw')];
  const onSolid = (el, zone) => {
    for (let n = el; n && n !== zone; n = n.parentElement) {
      const s = getComputedStyle(n);
      const c = s.backgroundColor.match(/[\d.]+/g) || [];
      if ((c.length === 3 || +c[3] > 0.9) && s.backgroundColor !== 'transparent') return true;
      if (s.backgroundImage !== 'none') return true;
    }
    return false;
  };
  zones.forEach((zone, z) => {
    const box = zone.getBoundingClientRect();
    const walk = document.createTreeWalker(zone, NodeFilter.SHOW_TEXT);
    for (let t = walk.nextNode(); t; t = walk.nextNode()) {
      const el = t.parentElement;
      if (t.textContent.trim().length < 2 || el.closest('svg, .hp, select, script, style') || onSolid(el, zone)) continue;
      const s = getComputedStyle(el);
      if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) continue;
      const r = document.createRange();
      r.selectNodeContents(t);
      for (const q of r.getClientRects()) {
        if (q.width < 6 || q.height < 6) continue;
        found.push({ z, x: q.left - box.left, y: q.top - box.top, w: q.width, h: q.height, color: s.color, px: parseFloat(s.fontSize), bold: +s.fontWeight >= 700,
          text: t.textContent.trim().slice(0, 48) });
      }
    }
  });
  return { zones: zones.map(z => { const b = z.getBoundingClientRect(); return { x: b.left + scrollX, y: b.top + scrollY, w: b.width, h: b.height }; }), found };
}

/* Runs in the blank page: the tenth-percentile contrast of each line against the pixels behind it. */
async function measure(b64, rows) {
  const img = new Image();
  img.src = 'data:image/png;base64,' + b64;
  await img.decode();
  const g = new OffscreenCanvas(img.width, img.height).getContext('2d', { willReadFrequently: true });
  g.drawImage(img, 0, 0);
  const lin = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  const lum = (r, gr, b) => 0.2126 * lin(r) + 0.7152 * lin(gr) + 0.0722 * lin(b);
  return rows.map(row => {
    const c = row.color.match(/[\d.]+/g).map(Number);
    const a = c.length > 3 ? c[3] : 1;
    const x = Math.max(0, Math.floor(row.x)), y = Math.max(0, Math.floor(row.y));
    const w = Math.min(img.width - x, Math.ceil(row.w)), h = Math.min(img.height - y, Math.ceil(row.h));
    if (w < 2 || h < 2) return null;
    const d = g.getImageData(x, y, w, h).data;
    const ratios = [];
    for (let i = 0; i < d.length; i += 8) {
      const t = lum(c[0] * a + d[i] * (1 - a), c[1] * a + d[i + 1] * (1 - a), c[2] * a + d[i + 2] * (1 - a));
      const b = lum(d[i], d[i + 1], d[i + 2]);
      ratios.push((Math.max(t, b) + 0.05) / (Math.min(t, b) + 0.05));
    }
    ratios.sort((p, q) => p - q);
    return ratios[Math.floor(ratios.length * 0.1)];
  });
}

for (const dir of readdirSync(ROOT).filter(d => /^\d{3}-/.test(d) && existsSync(join(ROOT, d, 'site'))).sort()) {
  const num = dir.slice(0, 3);
  if (only.length && !only.includes(num)) continue;
  const result = {};
  for (const [name, w, h] of VIEWS) {
    const page = await browser.newPage();
    await page.setViewport({ width: w, height: h, deviceScaleFactor: 1 });
    await page.goto(`http://127.0.0.1:${port}/${dir}/site/index.html`, { waitUntil: 'load' });
    // entrance animation is switched off, and the phone bar that stays pinned to the screen is hidden so it does not cover a long capture
    await page.addStyleTag({ content: '*:not(.hdw){animation:none!important;transition:none!important}.sticky{display:none!important}' });
    await page.evaluate(async () => {
      document.querySelectorAll('img').forEach(i => { i.loading = 'eager'; });
      await Promise.all([...document.images].map(i => i.decode().catch(() => 0)));
      await document.fonts.ready;
    });
    if (sheets) await page.screenshot({ path: `/tmp/ab-check/${dir}-${name === 'desktop' ? 'desk' : 'phone'}.png`, fullPage: true });
    const { zones, found } = await page.evaluate(lines);
    await page.addStyleTag({ content: '*,*::placeholder{color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important}' });
    let body = [], large = [], fails = [];
    for (let z = 0; z < zones.length; z++) {
      const rows = found.filter(f => f.z === z);
      if (!rows.length) continue;
      const b64 = await page.screenshot({ encoding: 'base64', captureBeyondViewport: true, clip: { x: zones[z].x, y: zones[z].y, width: zones[z].w, height: zones[z].h } });
      const ratios = await bench.evaluate(measure, b64, rows);
      rows.forEach((row, i) => {
        if (ratios[i] == null) return;
        const big = row.px >= 24 || (row.px >= 18.66 && row.bold);
        (big ? large : body).push(ratios[i]);
        if (ratios[i] < (big ? 3 : 4.5)) fails.push(`${row.text} (${ratios[i].toFixed(1)}, ${Math.round(row.px)}px)`);
      });
    }
    const low = a => a.length ? +Math.min(...a).toFixed(1) : null;
    result[name] = { lines: body.length + large.length, body: low(body), large: low(large), fails: [...new Set(fails)] };
    await page.close();
  }
  out[num] = result;
  const f = result.desktop.fails.length + result.phone.fails.length;
  console.log(num, `desktop ${result.desktop.body}/${result.desktop.large}`, `phone ${result.phone.body}/${result.phone.large}`, f ? `${f} below the bar` : 'ok');
  for (const v of ['desktop', 'phone']) for (const x of result[v].fails.slice(0, 8)) console.log('   ', v, x);
}
mkdirSync(join(ROOT, 'src/data'), { recursive: true });
writeFileSync(file, JSON.stringify(out, null, 1) + '\n');
await browser.disconnect();
await chrome.kill();
server.close();
