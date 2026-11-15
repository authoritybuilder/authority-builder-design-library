#!/usr/bin/env node
/* Optional: measure every sample with Lighthouse and write src/data/speed.json, which the build reads for each audit table.

     npm install lighthouse          (once, anywhere on your machine; point NODE_PATH at it if it is not local)
     node src/speed.mjs              all samples
     node src/speed.mjs 007 012      only these

   Each sample is tested as a visitor's phone would load it: Lighthouse's default mobile profile (a mid-range phone on slow 4G).
   1 thing is changed for the test copy, and it is stated in the audit table: the Google Fonts request is removed, so the test also
   runs offline. Install the fonts locally to match the real look.
   The same run also measures page width and tap-target height at 390px wide. */
import { createServer } from 'node:http';
import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync } from 'node:fs';
import { dirname, join, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(process.env.LH_HOME ? join(process.env.LH_HOME, 'x.js') : import.meta.url);
const lighthouse = (await import(require.resolve('lighthouse'))).default;
const chromeLauncher = await import(require.resolve('chrome-launcher'));
const puppeteer = (await import(require.resolve('puppeteer-core'))).default;

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const TYPES = { '.html': 'text/html; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.webp': 'image/webp', '.xml': 'application/xml', '.txt': 'text/plain' };
const only = process.argv.slice(2);

/* Each sample is served from its own site folder, exactly as it would be on its own domain, so its own robots.txt is the one that applies. */
let site = ROOT;
const server = createServer((req, res) => {
  const p = decodeURIComponent(req.url.split('?')[0]);
  const file = join(site, p.endsWith('/') ? p + 'index.html' : p);
  if (!existsSync(file)) { res.writeHead(404); return res.end('not found'); }
  let body = readFileSync(file);
  if (file.endsWith('.html')) {
    body = body.toString()
      .replace(/<link rel="preconnect"[^>]+>\n/g, '')
      .replace(/<link href="https:\/\/fonts\.googleapis\.com[^>]+>\n/, '');
  }
  res.writeHead(200, { 'content-type': TYPES[extname(file)] || 'application/octet-stream' });
  res.end(body);
});
await new Promise(r => server.listen(0, r));
const port = server.address().port;

const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless=new', '--no-sandbox', '--disable-gpu'] });
const browser = await puppeteer.connect({ browserURL: `http://127.0.0.1:${chrome.port}` });
const out = existsSync(join(ROOT, 'src/data/speed.json')) ? JSON.parse(readFileSync(join(ROOT, 'src/data/speed.json'))) : {};

for (const dir of readdirSync(ROOT).filter(d => /^\d{3}-/.test(d) && existsSync(join(ROOT, d, 'site'))).sort()) {
  const num = dir.slice(0, 3);
  if (only.length && !only.includes(num)) continue;
  site = join(ROOT, dir, 'site');
  const url = `http://127.0.0.1:${port}/`;
  const { lhr } = await lighthouse(url, { port: chrome.port, output: 'json', logLevel: 'error', onlyCategories: ['performance', 'accessibility', 'best-practices', 'seo'] });
  const scores = Object.fromEntries(Object.entries(lhr.categories).map(([k, v]) => [k, Math.round(v.score * 100)]));
  const failed = [];
  for (const cat of ['accessibility', 'best-practices', 'seo']) {
    for (const ref of lhr.categories[cat].auditRefs) {
      const a = lhr.audits[ref.id];
      if (a.score !== null && a.score < 1 && ref.weight > 0) failed.push(a.title);
    }
  }
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  await page.goto(url, { waitUntil: 'load' });
  const m = await page.evaluate(() => {
    const els = [...document.querySelectorAll('main a.btn, main button, main input:not([type=radio]):not([type=hidden]), main select, main textarea, main summary, .sticky a, .lb-l a')]
      .filter(el => !el.closest('.hp'))   // the spam trap is hidden from people, so it is not a tap target
      .map(el => el.getBoundingClientRect()).filter(r => r.width > 0 && r.height > 0);
    // where the first way to act sits on a phone screen, and whether any form field is small enough to make the phone zoom in
    const first = document.querySelector('main section .btn, main section button[type=submit], main section form button, .lb-f .btn');
    const fields = [...document.querySelectorAll('main input:not([type=radio]):not([type=hidden]), main select, main textarea')].filter(el => !el.closest('.hp'));
    return { scroll_w: document.documentElement.scrollWidth, min_tap: Math.round(Math.min(...els.map(r => r.height))), taps: els.length,
      pinned: !!document.querySelector('.sticky a') && getComputedStyle(document.querySelector('.sticky')).display !== 'none',
      cta_y: first ? Math.round(first.getBoundingClientRect().bottom + scrollY) : null, cta: first ? first.textContent.trim().slice(0, 40) : '',
      field_px: fields.length ? Math.min(...fields.map(el => parseFloat(getComputedStyle(el).fontSize))) : null, fields: fields.length };
  });
  await page.close();
  out[num] = { scores, failed, lcp: Math.round(lhr.audits['largest-contentful-paint'].numericValue), cls: +lhr.audits['cumulative-layout-shift'].numericValue.toFixed(4),
    tbt: Math.round(lhr.audits['total-blocking-time'].numericValue), ...m, lighthouse: lhr.lighthouseVersion };
  console.log(num, JSON.stringify(out[num]));
}
mkdirSync(join(ROOT, 'src/data'), { recursive: true });
writeFileSync(join(ROOT, 'src/data/speed.json'), JSON.stringify(out, null, 1) + '\n');
await browser.disconnect();
await chrome.kill();
server.close();
