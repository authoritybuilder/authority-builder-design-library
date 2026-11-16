#!/usr/bin/env python3
"""Hero photographs. Each site's large picture is a photograph from Pexels, listed in src/data/heroes.json.

    python3 src/photos.py          # fetch every photograph and cut its 4 sizes
    python3 src/photos.py 007 012  # only these sites

Each photograph is cropped to 16:10 and written as hero-2560, hero-1920, hero-1280 and hero-960 (WebP) in the site's images folder,
the same files the paintings used, so nothing else in a site changes. The downloads are kept in src/.photo-cache, which is not committed.

To change a site's photograph, change its id and alt text in src/data/heroes.json, run this, then people.py --scenes, shots.py and build.py.
Pexels photographs are free to use (https://www.pexels.com/license/). They may not be sold or passed on as stand-alone files.

Needs Pillow. The build needs neither this nor Pillow: the files this writes are committed.
"""
import json
import pathlib
import sys
import urllib.request

from PIL import Image

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
CACHE = SRC / ".photo-cache"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"}
SIZES = (2560, 1920, 1280, 960)


def fetch(pid):
    CACHE.mkdir(exist_ok=True)
    f = CACHE / f"{pid}.jpg"
    if not f.exists():
        url = f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=2560"
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
            f.write_bytes(r.read())
    return f


def main():
    plan = json.loads((SRC / "data" / "heroes.json").read_text(encoding="utf-8"))
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    dirs = {d.name[:3]: d for d in ROOT.iterdir() if d.is_dir() and d.name[:3].isdigit() and (d / "site").exists()}
    for num, p in sorted(plan.items()):
        if want and num not in want:
            continue
        im = Image.open(fetch(p["id"])).convert("RGB")
        w, h = im.size
        ch = round(w * 10 / 16)                       # crop to 16:10, keeping the part of the picture named by "focus" (0 top, 1 bottom)
        if ch <= h:
            top = round((h - ch) * p.get("focus", 0.5))
            im = im.crop((0, top, w, top + ch))
        else:
            cw = round(h * 16 / 10)
            im = im.crop(((w - cw) // 2, 0, (w - cw) // 2 + cw, h))
        out = dirs[num] / "site" / "images"
        for s in SIZES:
            im.resize((s, round(s * 10 / 16)), Image.LANCZOS).save(out / f"hero-{s}.webp", quality=80 if s <= 1280 else 76, method=6)
        print("photo", num, p["id"], f"{w}x{h}", flush=True)


if __name__ == "__main__":
    main()
