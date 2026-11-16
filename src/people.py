#!/usr/bin/env python3
"""Photo placeholders. Every picture of a person or a place on a site is a named file in its images folder, so the owner
swaps a photo by saving their own under the same name. This script paints the stand-ins that ship in those files.

    python3 src/build.py           # first: it decides which photo files each site needs and lists them in src/data/photos.json
    python3 src/people.py          # paints every placeholder
    python3 src/people.py 007 012  # only these sites
    python3 src/people.py --missing # only files that are not there yet
    python3 src/people.py --owner   # only the pictures of the site owner
    python3 src/people.py --scenes  # only the pictures of places and the video stills

A portrait placeholder is a back-lit figure with no face, painted over a soft-focus piece of that site's own painting, so it
belongs to the page without pretending to be anyone. A place placeholder is a crop of the site's painting. Each large one carries
a small label with its file name and size, which disappears the moment the file is replaced.

Needs numpy, OpenCV and Pillow. The build needs none of them: the files this writes are committed.
"""
import hashlib
import json
import pathlib
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
from paint import brush, rgb  # noqa: E402

FONTS = [["/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", "C:/Windows/Fonts/seguisb.ttf", "C:/Windows/Fonts/arialbd.ttf", "/System/Library/Fonts/Helvetica.ttc"],
         ["/usr/share/fonts/opentype/inter/Inter-Medium.otf", "C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf", "/System/Library/Fonts/Helvetica.ttc"]]


def font(i, size):
    """The first label font this computer has."""
    for p in FONTS[i]:
        if pathlib.Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)
STYLES = ["crop", "bob", "long", "bun", "curly", "crop", "long", "bob"]


def seed_of(text):
    return int(hashlib.sha256(text.encode()).hexdigest()[:8], 16)


def crop_of(hero, cx, cy, zoom, w, h):
    """A w by h piece of the painting centred near cx, cy (0 to 1)."""
    H, W = hero.shape[:2]
    cw = min(W, max(w * 0.9, W / zoom))
    ch = cw * h / w
    if ch > H:
        ch, cw = H, H * w / h
    x0 = int(min(max(cx * W - cw / 2, 0), W - cw))
    y0 = int(min(max(cy * H - ch / 2, 0), H - ch))
    return cv2.resize(hero[y0:y0 + int(ch), x0:x0 + int(cw)], (w, h), interpolation=cv2.INTER_CUBIC)


def outline(points, n=400):
    """A smooth closed-ish path through a few points, for shoulders that slope like shoulders."""
    from scipy.interpolate import PchipInterpolator
    pts = np.array(points, np.float32)
    t = np.linspace(0, 1, len(pts))
    tt = np.linspace(0, 1, n)
    return np.stack([PchipInterpolator(t, pts[:, 0])(tt), PchipInterpolator(t, pts[:, 1])(tt)], 1).astype(np.int32)


def figure(w, h, who, pose, close, incog=False):
    """Masks for a head-and-shoulders figure seen against the light: the garment, and the head with its hair as 1 shape.
    `who` fixes the person, `pose` varies the shot."""
    rw, rp = np.random.default_rng(who), np.random.default_rng(pose)
    S = 2
    W2, H2 = w * S, h * S
    style = STYLES[who % len(STYLES)]
    k = 1.32 if close else 1.0
    ry = H2 * 0.118 * k * rw.uniform(0.96, 1.05)
    rx = ry * rw.uniform(0.74, 0.79)
    cx = W2 * (0.5 + rp.uniform(-0.06, 0.06))
    hy = H2 * ((0.43 if close else 0.34) + rp.uniform(-0.015, 0.015))
    hx = cx + rx * rp.uniform(-0.22, 0.22)
    sy = hy + ry * 1.2                                    # where the neck meets the shoulders
    sw = rx * rw.uniform(2.3, 2.6)                        # half the shoulder width
    drop = ry * rw.uniform(0.62, 0.8)                     # how far the shoulders slope
    lift = ry * rp.uniform(-0.14, 0.14)                   # 1 shoulder a touch higher, as people stand
    z = lambda: np.zeros((H2, W2), np.float32)
    P = lambda x, y: (int(x), int(y))
    body, head = z(), z()
    nw = rx * 0.47
    side_ = lambda d, up: outline([(cx + d * nw, sy - ry * 0.12), (cx + d * nw * 2.0, sy + ry * 0.26), (cx + d * sw * 0.8, sy + drop * 0.9 + up), (cx + d * sw, sy + drop * 2.1 + up), (cx + d * sw * 1.04, sy + drop * 4.2 + up), (cx + d * sw * 1.02, H2 * 1.25)])
    left, right = side_(-1, lift), side_(1, -lift)
    cv2.fillPoly(body, [np.concatenate([left, right[::-1]])], 1, cv2.LINE_AA)
    cv2.rectangle(head, P(cx - nw, hy), P(cx + nw, sy + ry * 0.2), 1, -1)                      # neck
    cv2.ellipse(head, P(hx, hy), P(rx, ry), 0, 0, 360, 1, -1, cv2.LINE_AA)
    cv2.ellipse(head, P(hx, hy + ry * 0.22), P(rx * 0.86, ry * 0.9), 0, 0, 360, 1, -1, cv2.LINE_AA)  # a narrower jaw
    specs = z()
    if incog:
        # Guy Incognito, the library's sample owner: a hat with a brim and round glasses, still with no face.
        # The moment a real photo is saved over the file, he is gone.
        style = "hat"
        by = hy - ry * 0.46
        cv2.ellipse(head, P(hx, by), P(rx * 1.86, ry * 0.17), 0, 0, 360, 1, -1, cv2.LINE_AA)                 # brim
        crown = np.array([P(hx - rx * 1.02, by), P(hx - rx * 0.9, by - ry * 0.92), P(hx - rx * 0.3, by - ry * 1.08), P(hx, by - ry * 0.96),
                          P(hx + rx * 0.3, by - ry * 1.08), P(hx + rx * 0.9, by - ry * 0.92), P(hx + rx * 1.02, by)], np.int32)
        cv2.fillPoly(head, [crown], 1, cv2.LINE_AA)
        gy, gr, th = hy + ry * 0.1, rx * 0.34, max(2, int(rx * 0.085))
        for d in (-1, 1):
            cv2.circle(specs, P(hx + d * rx * 0.44, gy), int(gr), 1, th, cv2.LINE_AA)
            cv2.line(specs, P(hx + d * (rx * 0.44 + gr), gy - gr * 0.2), P(hx + d * rx * 1.0, gy - gr * 0.5), 1, th, cv2.LINE_AA)
        cv2.line(specs, P(hx - rx * 0.1, gy - gr * 0.25), P(hx + rx * 0.1, gy - gr * 0.25), 1, th, cv2.LINE_AA)
        band = np.array([P(hx - rx * 1.0, by - ry * 0.3), P(hx + rx * 1.0, by - ry * 0.3), P(hx + rx * 1.02, by - ry * 0.1), P(hx - rx * 1.02, by - ry * 0.1)], np.int32)
        cv2.fillPoly(specs, [band], 0.55, cv2.LINE_AA)                                                     # the hat band catches a little light
    if style == "hat":
        pass
    elif style == "crop":
        cv2.ellipse(head, P(hx, hy - ry * 0.12), P(rx * 1.07, ry * 1.0), 0, 180, 360, 1, -1, cv2.LINE_AA)
    elif style == "bob":
        cv2.ellipse(head, P(hx, hy + ry * 0.05), P(rx * 1.3, ry * 1.18), 0, 150, 390, 1, -1, cv2.LINE_AA)
    elif style == "long":
        cv2.ellipse(head, P(hx, hy - ry * 0.05), P(rx * 1.22, ry * 1.12), 0, 0, 360, 1, -1, cv2.LINE_AA)
        cv2.ellipse(head, P(hx, hy + ry * 1.3), P(rx * 1.4, ry * 1.75), 0, 0, 360, 1, -1, cv2.LINE_AA)
    elif style == "bun":
        cv2.ellipse(head, P(hx, hy - ry * 0.12), P(rx * 1.08, ry * 1.02), 0, 180, 360, 1, -1, cv2.LINE_AA)
        cv2.circle(head, P(hx + rx * 0.12, hy - ry * 1.16), int(rx * 0.42), 1, -1, cv2.LINE_AA)
    else:   # curly
        for a in np.linspace(-3.6, 0.5, 14):
            cv2.circle(head, P(hx + np.cos(a) * rx * 1.02, hy - ry * 0.1 + np.sin(a) * ry * 1.0), int(rx * rw.uniform(0.34, 0.46)), 1, -1, cv2.LINE_AA)
    lean = cv2.getRotationMatrix2D((float(cx), float(H2)), float(rp.uniform(-3.5, 3.5)), 1.0)
    soft = lambda m: cv2.resize(cv2.GaussianBlur(cv2.warpAffine(m, lean, (W2, H2)), (0, 0), 1.4 * S), (w, h), interpolation=cv2.INTER_AREA)
    return soft(body), soft(head), np.clip(soft(specs) * 1.25, 0, 1)


def portrait(hero, accent, who, pose, w, h, close=False, incog=False):
    r = np.random.default_rng(pose)
    back = crop_of(hero, r.uniform(0.25, 0.75), r.uniform(0.2, 0.55), 2.2, w, h)
    back = cv2.GaussianBlur(back, (0, 0), w * 0.07)
    lum = cv2.cvtColor(hero, cv2.COLOR_RGB2GRAY)
    light = hero[lum > np.quantile(lum, 0.92)].mean(0)
    dark = hero[lum < np.quantile(lum, 0.15)].mean(0)
    back = back * 0.84 + light * 0.16                                            # lift it a little, like a bright wall behind a sitter
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    side = 1 if who % 2 else -1
    halo = np.exp(-(((xx - w * (0.5 + 0.14 * side)) / (w * 0.55)) ** 2 + ((yy - h * 0.32) / (h * 0.46)) ** 2))[..., None]
    back = np.clip(back + (light * 1.04 - back) * halo * 0.55, 0, 1)
    back *= (1 - 0.24 * (((xx - w / 2) / w) ** 2 + ((yy - h / 2) / h) ** 2))[..., None]
    body, head, specs = figure(w, h, who, pose, close, incog)
    ink = dark * 0.45 + np.array(rgb("#161922")) * 0.55                          # a shadow tone taken from the painting, never a skin colour
    tint = (0.26, 0.36, 0.46)[who % 3]
    garment = ink * (1 - tint) + np.array(rgb(accent)) * tint
    whole = np.clip(body + head, 0, 1)
    img = back * (1 - body[..., None]) + garment * body[..., None]
    img = img * (1 - head[..., None]) + ink * head[..., None]
    wrap = cv2.GaussianBlur(back, (0, 0), w * 0.03)                              # light spilling round the edges of the figure
    edge = np.clip(cv2.GaussianBlur(whole, (0, 0), w / 70) * 2 - 1, 0, 1)
    img = img * (0.72 + 0.28 * edge[..., None]) + wrap * (0.28 * (1 - edge[..., None])) * whole[..., None] + img * 0 
    img = np.where(whole[..., None] > 0.02, img, back)
    inner = cv2.erode(whole, np.ones((3, 3), np.uint8), iterations=max(3, w // 120))
    rim = cv2.GaussianBlur(np.clip(whole - inner, 0, 1), (0, 0), w / 300)
    lit = np.clip(0.42 + side * (xx - w / 2) / (w * 0.45), 0, 1) * np.clip(1.3 - yy / h, 0.2, 1)
    img = np.clip(img + (light * 1.08 - img) * (rim * lit)[..., None] * 0.85, 0, 1)
    img = brush(img, pose, sizes=(max(12, w // 40), max(6, w // 80), max(4, w // 170), max(2, w // 340)), relief=0.009)
    if incog:   # drawn after the brushwork so the rims stay fine
        tone = np.clip(light * 0.55 + np.array(rgb(accent)) * 0.45, 0, 1)
        img = np.clip(img + (tone - img) * specs[..., None] * 0.9, 0, 1)
    return img


def label(img, lines, y=0.66):
    """A small plate naming the file and its size, centred and kept away from the edges so it survives any crop.
    Text is drawn after the paint so it stays crisp."""
    im = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8)).convert("RGBA")
    w = im.width
    fs = max(15, w // 40)
    f1, f2 = font(0, fs), font(1, int(fs * 0.9))
    pad, gap = int(fs * 0.9), int(fs * 0.4)
    w1, w2 = f1.getlength(lines[0]), f2.getlength(lines[1])
    bw, bh = int(max(w1, w2) + pad * 2), int(fs + fs * 0.9 + gap + pad * 1.9)
    x0, y0 = (w - bw) // 2, int(im.height * y - bh / 2)
    plate = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(plate)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=int(fs * 0.75), fill=(12, 15, 24, 140), outline=(255, 255, 255, 90), width=1)
    d.text((x0 + (bw - w1) / 2, y0 + pad * 0.8), lines[0], font=f1, fill=(255, 255, 255, 255))
    d.text((x0 + (bw - w2) / 2, y0 + pad * 0.8 + fs + gap), lines[1], font=f2, fill=(255, 255, 255, 210))
    return np.asarray(Image.alpha_composite(im, plate).convert("RGB")).astype(np.float32) / 255


def write(img, path, q):
    path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), cv2.cvtColor((np.clip(img, 0, 1) * 255).astype(np.uint8), cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, q, cv2.IMWRITE_JPEG_PROGRESSIVE, 1])


def main():
    plan = json.loads((SRC / "data" / "photos.json").read_text())
    want = [a for a in sys.argv[1:] if not a.startswith("--")]
    marks_file = SRC / "data" / "placeholders.json"
    marks = json.loads(marks_file.read_text()) if marks_file.exists() else {}
    for num, site in sorted(plan.items()):
        if want and num not in want:
            continue
        folder = ROOT / site["folder"]
        hero = cv2.cvtColor(cv2.imread(str(ROOT / site["hero"])), cv2.COLOR_BGR2RGB).astype(np.float32) / 255
        for p in site["photos"]:
            w, h, kind, name = p["w"], p["h"], p["kind"], p["file"]
            if "--missing" in sys.argv and (folder / name).exists():
                continue
            if "--owner" in sys.argv and kind not in ("you", "me"):
                continue
            if "--scenes" in sys.argv and kind not in ("scene", "video"):
                continue
            if kind in ("you", "me", "guest", "face"):
                who = seed_of(site["dir"] + (site["person"] if kind in ("you", "me") else p["who"]))
                small = w <= 320
                k = 3 if small else 1.5                       # painted larger, then cut down, so the brushwork is fine and the edges clean
                img = portrait(hero, site["accent"], who, seed_of(site["dir"] + name), int(w * k), int(h * k), close=small or p.get("close", False),
                               incog=kind in ("you", "me") and site["person"] == "Guy Incognito")
                img = cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)
                if not small:
                    img = label(img, ["YOUR PHOTO" if kind == "guest" or site["person"] != "Guy Incognito" else "GUY INCOGNITO · YOUR PHOTO", f"{name} · {w} × {h}"])
            else:
                cx, cy, zoom = p["crop"]
                img = crop_of(hero, cx, cy, zoom, w, h)   # a piece of the site's own photograph, with no label, so the page reads as a real site
            write(img, folder / name, 80)
            marks[f"{site['folder']}/{name}"] = hashlib.sha256((folder / name).read_bytes()).hexdigest()
        print("photos", num, len(site["photos"]), flush=True)
    marks_file.write_text(json.dumps(marks, indent=1, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
