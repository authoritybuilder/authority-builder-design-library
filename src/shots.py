#!/usr/bin/env python3
"""Optional: regenerate preview.jpg for every entry, and full-page check sheets.

    python3 src/shots.py            # previews only
    python3 src/shots.py --check    # also writes desktop and phone check sheets to /tmp/ab-check

Needs Google Chrome and Pillow. The library itself needs neither.
"""
import pathlib
import subprocess
import sys

from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).parent.parent
CHROME = "google-chrome"


def still(page, tmp):
    """A copy with entrance animations and the web-font request removed, so captures are steady and use installed fonts."""
    import re
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


def main():
    check = "--check" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    tmp = pathlib.Path("/tmp/ab-check")
    tmp.mkdir(exist_ok=True)
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:3].isdigit()):
        if only and not any(d.name.startswith(o) for o in only):
            continue
        page = d / "sample.html" if (d / "sample.html").exists() else d / "index.html"
        raw = tmp / f"{d.name}.png"
        page = still(page, tmp)
        grab(page, raw, 1280, 800)
        Image.open(raw).convert("RGB").resize((960, 600), Image.LANCZOS).save(d / "preview.jpg", quality=80, optimize=True)
        if check:
            for tag, w, hgt in (("desk", 1280, 12000), ("phone", 390, 16000)):
                f = tmp / f"{d.name}-{tag}.png"
                grab(page, f, w, hgt)
                trim(Image.open(f).convert("RGB")).save(f)
        page.unlink()
        print("shot", d.name)


if __name__ == "__main__":
    main()
