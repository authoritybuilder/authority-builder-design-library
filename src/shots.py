#!/usr/bin/env python3
"""Optional: regenerate each entry's preview.jpg, site icons and share image, and full-page check sheets.

    python3 src/shots.py            # previews, icons and share images
    python3 src/shots.py --check    # also writes desktop and phone check sheets to /tmp/ab-check
    python3 src/shots.py 007 012    # only these entries

Needs Google Chrome and Pillow. The library itself needs neither: the files this writes are committed.
"""
import pathlib
import re
import subprocess
import sys

from PIL import Image, ImageChops

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
CHROME = "google-chrome"

import art  # noqa: E402
import build  # noqa: E402
from kit import h  # noqa: E402
from polish import POLISH_CSS, THEME_POLISH  # noqa: E402
from themes import THEMES  # noqa: E402


def still(page):
    """A copy with entrance animations and the web-font request removed, so captures are steady and use installed fonts."""
    t = page.read_text()
    t = re.sub(r'<link href="https://fonts.googleapis.com[^>]+>', "", t)
    t = t.replace("</head>", "<style>*{animation:none!important}</style></head>")
    f = page.parent / "_shot.html"
    f.write_text(t)
    return f


def grab(html, out, w, hgt):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{hgt}",
                    "--virtual-time-budget=8000", "--force-device-scale-factor=1", f"--screenshot={out}", f"file://{html}"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)


def trim(im):
    """Cut the empty space below the end of the page."""
    bg = Image.new(im.mode, im.size, im.getpixel((im.width - 1, im.height - 1)))
    box = ImageChops.difference(im, bg).getbbox()
    return im.crop((0, 0, im.width, min(im.height, box[3] + 4))) if box else im


def tokens(P):
    t = THEMES[P["theme"]]
    return ":root{" + ";".join(f"--{k}:{v}" for k, v in t["v"].items()) + "}" + t["css"] + THEME_POLISH.get(P["theme"], "")


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
    who = b.get("person") or b["name"]
    f.write_text(f"""<!doctype html><meta charset=utf-8><style>{tokens(P)}{POLISH_CSS}
html,body{{margin:0}}body{{width:1200px;height:630px;box-sizing:border-box;padding:64px 72px;background:var(--bg);color:var(--ink);font-family:var(--fb);display:grid;
grid-template-columns:1fr 330px;gap:56px;align-items:center;position:relative;overflow:hidden}}body::before{{content:"";position:absolute;inset:0;background:var(--atmo,none)}}
div{{position:relative}}p{{font:600 22px/1.2 var(--fa);letter-spacing:.14em;text-transform:uppercase;color:var(--accent-t);margin:0 0 26px}}
h1{{font-family:var(--fd);font-weight:var(--hw);letter-spacing:var(--hls);line-height:var(--hlh);text-transform:var(--htt);font-size:calc(66px*var(--hs));margin:0;text-wrap:balance}}
small{{display:block;margin-top:34px;font-size:24px;color:var(--ink2)}}
.ph{{position:relative;aspect-ratio:4/5;border-radius:var(--phr);overflow:hidden;background:radial-gradient(90% 70% at 30% 18%,var(--ph1),var(--ph2))}}.ph svg{{position:absolute;inset:0;width:100%;height:100%}}
</style><div><p>{h(b["name"])}</p><h1>{h(head)}</h1><small>{b["domain"]}</small></div><div class="ph person">{art.portrait(who)}</div>""")
    raw = tmp / "share.png"
    grab(f, raw, 1200, 630)
    Image.open(raw).convert("RGB").crop((0, 0, 1200, 630)).save(site / "share.jpg", quality=82, optimize=True)
    f.unlink()


def main():
    check = "--check" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    tmp = pathlib.Path("/tmp/ab-check")
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
        if check:
            for tag, w, hgt in (("desk", 1280, 14000), ("phone", 390, 20000)):
                f = tmp / f"{d.name}-{tag}.png"
                grab(page, f, w, hgt)
                trim(Image.open(f).convert("RGB")).save(f)
        page.unlink()
        print("shot", d.name)


if __name__ == "__main__":
    main()
