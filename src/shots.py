#!/usr/bin/env python3
"""Optional: regenerate each entry's preview.jpg, site icons and share image.

    python3 src/shots.py            # previews, icons and share images
    python3 src/shots.py 007 012    # only these entries

For full-page desktop and phone pictures of every sample, use: node src/legible.mjs --sheets

Needs Google Chrome and Pillow. The library itself needs neither: the files this writes are committed.
"""
import pathlib
import re
import subprocess
import sys

from PIL import Image

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
CHROME = next((p for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome") if pathlib.Path(p).exists()), "google-chrome")

import art  # noqa: E402
import build  # noqa: E402
from kit import h  # noqa: E402
from polish import THEME_POLISH  # noqa: E402
from themes import THEMES  # noqa: E402,F401
import variants  # noqa: E402


# With --web-fonts the captures load the real fonts from Google. Use it on a computer that does not have them installed.
WEB_FONTS = "--web-fonts" in sys.argv


def still(page):
    """A copy with entrance animations and the web-font request removed, so captures are steady and use installed fonts."""
    t = page.read_text()
    if not WEB_FONTS:
        t = re.sub(r'<link href="https://fonts.googleapis.com[^>]+>', "", t)
    t = t.replace("</head>", "<style>*:not(.hd){animation:none!important}</style></head>").replace('decoding="async"', 'decoding="sync"').replace('loading="lazy"', 'loading="eager"')
    f = page.parent / "_shot.html"
    f.write_text(t)
    return f


def grab(html, out, w, hgt):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{hgt}",
                    "--virtual-time-budget=8000", "--force-device-scale-factor=1", f"--screenshot={out}", pathlib.Path(html).resolve().as_uri()],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def tokens(P):
    t = variants.theme(P)
    link = f'</style><link href="{t["fonts"]}" rel="stylesheet"><style>' if WEB_FONTS else ""
    return link + ":root{" + ";".join(f"--{k}:{v}" for k, v in t["v"].items()) + "}" + t["css"] + THEME_POLISH.get(P["theme"], "") + t["vcss"]


def brand_assets(P, site, tmp):
    """The site icon (192px and 512px PNG) and the 1200 by 630 share image, drawn from the sample's own tokens."""
    b = P["brand"]
    mono = b.get("mono", b["name"][0])
    f = site / "_asset.html"
    f.write_text(f"<!doctype html><meta charset=utf-8><style>{tokens(P)}html,body{{margin:0}}body{{width:512px;height:512px;display:grid;place-items:center;"
                 f"background:var(--accent);color:var(--accent-ink);font:var(--hw) 300px/1 var(--fd);letter-spacing:var(--hls);text-transform:var(--htt)}}"
                 f"span{{translate:0 -3%}}</style><span>{mono}</span>")
    raw = tmp / "icon.png"
    grab(f, raw, 512, 512)
    im = Image.open(raw).convert("RGB").crop((0, 0, 512, 512))
    im.save(site / "icon-512.png", optimize=True)
    im.resize((192, 192), Image.LANCZOS).save(site / "icon-192.png", optimize=True)
    head = next((d.get("h") or (d.get("tiles") or [{}])[0].get("h") for n, d in P["sections"] if n.startswith("hero") or n in ("bento", "linkbio")), P["name"])
    light = P["art"]["tone"] == "light"
    veil = "linear-gradient(90deg,rgba(6,10,22,.78),rgba(6,10,22,.42) 62%,rgba(6,10,22,.1))" if light else "linear-gradient(90deg,rgba(255,255,255,.9),rgba(255,255,255,.6) 62%,rgba(255,255,255,.1))"
    f.write_text(f"""<!doctype html><meta charset=utf-8><style>{tokens(P)}
html,body{{margin:0}}body{{width:1200px;height:630px;box-sizing:border-box;padding:64px 72px;color:{"#fff" if light else "var(--ink)"};font-family:var(--fb);display:grid;align-content:center;
position:relative;overflow:hidden;background:url(images/hero-1920.webp) center 80%/cover}}body::before{{content:"";position:absolute;inset:0;background:{veil}}}
div{{position:relative;max-width:820px}}p{{font:600 22px/1.2 var(--fa);letter-spacing:.14em;text-transform:uppercase;margin:0 0 26px}}
h1{{font-family:var(--fd);font-weight:var(--hw);letter-spacing:var(--hls);line-height:var(--hlh);text-transform:var(--htt);font-size:calc(68px*var(--hs));margin:0;text-wrap:balance}}
h1 em{{background:none!important;color:{"#FFE6BF" if light else "var(--accent-t)"}}}small{{display:block;margin-top:34px;font-size:24px;opacity:.9}}
</style><div><p>{h(b["name"])}</p><h1>{h(head)}</h1><small>{b["domain"]}</small></div>""")
    raw = tmp / "share.png"
    grab(f, raw, 1200, 630)
    Image.open(raw).convert("RGB").crop((0, 0, 1200, 630)).save(site / "share.jpg", quality=82, optimize=True)
    f.unlink()


def main():
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    import tempfile
    tmp = pathlib.Path(tempfile.gettempdir()) / "ab-shots"
    tmp.mkdir(exist_ok=True)
    pages = {P["dir"]: P for P in build.load_pages()}
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:3].isdigit()):
        if only and not any(d.name.startswith(o) for o in only):
            continue
        site = d / "site"
        if d.name in pages and "--no-assets" not in sys.argv:
            brand_assets(pages[d.name], site, tmp)
        page = still(site / "index.html" if site.exists() else d / "index.html")
        raw = tmp / f"{d.name}.png"
        grab(page, raw, 1280, 800)
        Image.open(raw).convert("RGB").resize((960, 600), Image.LANCZOS).save(d / "preview.jpg", quality=80, optimize=True)
        page.unlink()
        print("shot", d.name)
    if not only:  # the picture at the top of the README
        page = still(ROOT / "index.html")
        raw = tmp / "library.png"
        grab(page, raw, 1280, 800)
        Image.open(raw).convert("RGB").crop((0, 0, 1280, 800)).save(ROOT / "preview.jpg", quality=84, optimize=True)
        page.unlink()
        print("shot library")


if __name__ == "__main__":
    main()
