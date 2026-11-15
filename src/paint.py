#!/usr/bin/env python3
"""Optional: paint the hero artwork for every sample.

    python3 src/paint.py            # every scene
    python3 src/paint.py coast      # only scenes whose name contains "coast"

Each picture is made from nothing: a scene is composed from sky, light, land and water, then painted over with
thousands of brush strokes that follow the forms, the way a gouache study is built up from big brushes to small.
No photographs, no stock art and no image generator are used, so every picture is original and safe to reuse.

Needs numpy and OpenCV. The library itself needs neither: the pictures this writes are committed.
"""
import pathlib
import sys

import cv2
import numpy as np
from scipy.interpolate import PchipInterpolator

OUT = pathlib.Path(__file__).parent.parent / "art"
W, H = 1920, 1200


# ---------- building blocks ----------

def rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32) / 255


def noise(shape, scale, octaves=5, seed=0, stretch=1.0):
    """Smooth fractal noise in 0..1. stretch above 1 pulls it sideways, for cloud bands and water."""
    r = np.random.default_rng(seed)
    h, w = shape
    out = np.zeros(shape, np.float32)
    amp, total = 1.0, 0.0
    for o in range(octaves):
        s = max(2, int(scale / 2 ** o))
        g = r.random((h // s + 3, int(w / (s * stretch)) + 3)).astype(np.float32)
        out += amp * cv2.resize(g, (w, h), interpolation=cv2.INTER_CUBIC)
        total += amp
        amp *= 0.5
    out /= total
    return np.clip((out - out.min()) / (out.max() - out.min() + 1e-6), 0, 1)


def vgrad(stops, h=H, w=W):
    """A vertical gradient from (position, colour) stops."""
    ys = np.linspace(0, 1, h, dtype=np.float32)
    pos = [p for p, _ in stops]
    cols = np.stack([rgb(c) for _, c in stops])
    img = np.stack([np.interp(ys, pos, cols[:, i]) for i in range(3)], 1)
    return np.repeat(img[:, None, :], w, 1).astype(np.float32)


def glow(img, cx, cy, radius, colour, strength=1.0):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / radius
    a = (np.exp(-d * d * 1.6) * strength)[..., None]
    return (img * (1 - a) + rgb(colour) * a).astype(np.float32)


def mix(img, layer, mask):
    m = np.clip(mask, 0, 1)[..., None]
    return np.ascontiguousarray(img * (1 - m) + layer * m, np.float32)


def ridge(base, amp, scale, seed, tilt=0.0, octaves=5):
    """The skyline of a hill or range: a y position for every x."""
    n = noise((4, W), scale, octaves, seed)[1]
    return H * (base - amp * (n - 0.5) * 2) + np.linspace(-tilt, tilt, W) * H


def land(img, ys, top, bottom, haze=None, haze_amt=0.0, soft=1.5, texture=0.0, seed=0):
    """Fill everything below a ridge with a top-to-bottom colour, pushed toward the haze colour for distance."""
    yy = np.mgrid[0:H, 0:W][0].astype(np.float32)
    depth = np.clip((yy - ys[None, :]) / (H - ys[None, :] + 1e-6), 0, 1)[..., None]
    col = rgb(top) * (1 - depth) + rgb(bottom) * depth
    if haze is not None:
        col = col * (1 - haze_amt) + rgb(haze) * haze_amt
    if texture:
        col = col * (1 + (noise((H, W), 60, 4, seed + 7)[..., None] - 0.5) * texture)
    return mix(img, col, (yy - ys[None, :]) / soft)


def clouds(img, colour, shade, cover=0.5, y0=0.0, y1=0.6, scale=260, seed=0, stretch=2.4, lit=None):
    n = noise((H, W), scale, 6, seed, stretch)
    yy = np.linspace(0, 1, H, dtype=np.float32)[:, None]
    band = np.clip((yy - y0) / 0.08, 0, 1) * np.clip((y1 - yy) / 0.16, 0, 1)
    m = np.clip((n - (1 - cover)) / 0.16, 0, 1) * band
    under = np.clip((np.roll(n, -14, 0) - n) * 9 + 0.5, 0, 1)[..., None]
    col = rgb(colour) * under + rgb(shade) * (1 - under)
    if lit:
        col = col * 0.7 + rgb(lit) * 0.3 * under + col * 0.3 * (1 - under)
    return mix(img, col, m * 0.92)


def water(img, y, sky, deep, seed=0, sun_x=None, sun_col="#FFE9B0", ripple=1.0):
    """A sheet of water from row y down: a darkened mirror of the sky, streaked sideways, with a glitter path under the sun."""
    y = int(y)
    h = H - y
    mirror = cv2.resize(np.ascontiguousarray(sky[max(0, y - h):y][::-1], np.float32), (W, h), interpolation=cv2.INTER_LINEAR)
    depth = np.linspace(0, 1, h, dtype=np.float32)[:, None, None]
    col = mirror * (0.78 - 0.3 * depth) + rgb(deep) * (0.22 + 0.3 * depth)
    streak = noise((h, W), 90, 5, seed, 9.0)[..., None]
    col = col * (1 + (streak - 0.5) * 0.34 * ripple)
    if sun_x is not None:
        xx = np.arange(W, dtype=np.float32)[None, :]
        spread = 26 + np.linspace(0, 1, h, dtype=np.float32)[:, None] * 150
        g = np.exp(-((xx - sun_x) / spread) ** 2) * (noise((h, W), 22, 3, seed + 3, 7.0) > 0.52)
        col = mix(col, np.broadcast_to(rgb(sun_col), col.shape), g * 0.85)
    out = img.copy()
    out[y:] = col
    return np.ascontiguousarray(out, np.float32)


def blob(img, cx, cy, rx, ry, colour, soft=3.0, alpha=1.0):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
    return mix(img, np.broadcast_to(rgb(colour), img.shape), np.clip((1 - d) * soft, 0, 1) * alpha)


def tree(img, x, y, size, dark, mid, light, r, kind="round"):
    """A tree standing on (x, y). Round trees are clumps of foliage lit from the upper left."""
    u8 = img
    if kind == "pine":
        cv2.rectangle(u8, (int(x - size * .03), int(y - size * .2)), (int(x + size * .03), int(y)), rgb("#3A2A1E").tolist(), -1)
        for i in range(6):
            t = i / 5
            wy = y - size * (0.12 + 0.88 * t)
            ww = size * 0.3 * (1 - t * 0.82)
            pts = np.array([[x - ww, wy + size * .22], [x + ww, wy + size * .22], [x + r.normal(0, size * .01), wy]], np.int32)
            cv2.fillPoly(u8, [pts], (rgb(dark) * (0.82 + 0.3 * t)).tolist(), cv2.LINE_AA)
            lit = np.array([[x - ww, wy + size * .22], [x - ww * .15, wy + size * .22], [x, wy]], np.int32)
            cv2.fillPoly(u8, [lit], (rgb(mid) * (0.86 + 0.3 * t)).tolist(), cv2.LINE_AA)
        return u8
    cv2.line(u8, (int(x), int(y)), (int(x + size * .02), int(y - size * .5)), rgb("#3A2A1E").tolist(), max(2, int(size * .05)), cv2.LINE_AA)
    for i in range(26):
        a, d = r.uniform(0, 6.28), r.uniform(0, 1) ** 0.6
        px, py = x + np.cos(a) * d * size * .42, y - size * .62 + np.sin(a) * d * size * .34
        rad = size * r.uniform(.1, .2)
        tone = (px - x) / (size * .42) * -0.5 + (py - (y - size * .62)) / (size * .34) * 0.6
        col = rgb(light) if tone < -0.28 else rgb(mid) if tone < 0.3 else rgb(dark)
        cv2.circle(u8, (int(px), int(py)), int(rad), (col * r.uniform(.92, 1.08)).tolist(), -1, cv2.LINE_AA)
    return u8


def skyline(img, y, colour, lit, r, x0=0, x1=W, scale=1.0, windows=True):
    x = x0
    while x < x1:
        bw = int(r.uniform(26, 70) * scale)
        bh = int(r.uniform(40, 230) * scale * (1 - abs((x - (x0 + x1) / 2) / ((x1 - x0) / 2)) ** 2 * 0.6))
        c = rgb(colour) * r.uniform(.85, 1.15)
        cv2.rectangle(img, (x, int(y - bh)), (x + bw, int(y + 4)), c.tolist(), -1)
        if windows:
            for wy in range(int(y - bh + 8), int(y - 6), int(9 * scale) + 4):
                for wx in range(x + 5, x + bw - 5, int(8 * scale) + 3):
                    if r.random() < 0.34:
                        cv2.rectangle(img, (wx, wy), (wx + int(3 * scale) + 1, wy + int(4 * scale) + 1), rgb(lit).tolist(), -1)
        x += bw + int(r.uniform(-4, 10))
    return img


def flowers(img, y0, y1, colours, r, n=900, size=(2, 6)):
    for _ in range(n):
        y = r.uniform(y0, y1)
        t = (y - y0) / (y1 - y0 + 1e-6)
        cv2.circle(img, (int(r.uniform(0, W)), int(y)), int(size[0] + (size[1] - size[0]) * t * r.uniform(.5, 1)),
                   (rgb(colours[r.integers(len(colours))]) * r.uniform(.9, 1.1)).tolist(), -1, cv2.LINE_AA)
    return img


def grass(img, y0, y1, colours, r, n=2600, length=(10, 46)):
    for _ in range(n):
        y = r.uniform(y0, y1)
        t = (y - y0) / (y1 - y0 + 1e-6)
        x = r.uniform(0, W)
        ln = length[0] + (length[1] - length[0]) * t
        cv2.line(img, (int(x), int(y)), (int(x + r.normal(0, ln * .3)), int(y - ln * r.uniform(.6, 1.2))),
                 (rgb(colours[r.integers(len(colours))]) * r.uniform(.85, 1.15)).tolist(), max(1, int(1 + t * 2)), cv2.LINE_AA)
    return img


def curve(points, wobble=0.0, seed=0, scale=160):
    """A smooth line through (x, y) points given as fractions of the picture. Returns a y in pixels for every x."""
    xs, ys = zip(*points)
    y = PchipInterpolator(np.array(xs) * W, np.array(ys) * H)(np.arange(W)).astype(np.float32)
    if wobble:
        y += (noise((4, W), scale, 4, seed)[1] - 0.5) * 2 * wobble * H
    return y


def poly(img, pts, colour, alpha=1.0):
    pts = np.array([[x * W, y * H] for x, y in pts], np.int32)
    if alpha >= 1:
        cv2.fillPoly(img, [pts], rgb(colour).tolist(), cv2.LINE_AA)
        return img
    layer = img.copy()
    cv2.fillPoly(layer, [pts], rgb(colour).tolist(), cv2.LINE_AA)
    return np.ascontiguousarray(img * (1 - alpha) + layer * alpha, np.float32)


def haze(img, y0, y1, colour, amount=0.5, seed=0):
    """A band of mist lying between two heights."""
    yy = np.linspace(0, 1, H, dtype=np.float32)[:, None]
    band = np.clip(1 - np.abs(yy - (y0 + y1) / 2) / ((y1 - y0) / 2 + 1e-6), 0, 1) ** 1.4
    n = noise((H, W), 320, 4, seed, 3.0)
    return mix(img, np.broadcast_to(rgb(colour), img.shape), band * (0.45 + 0.55 * n) * amount)


def stars(img, r, n=700, y1=0.7):
    for _ in range(n):
        x, y = int(r.uniform(0, W)), int(r.uniform(0, H * y1) ** 1.0)
        b = r.uniform(.5, 1) * (1 - y / (H * y1)) ** 0.5
        cv2.circle(img, (x, y), 1 if r.random() < .85 else 2, (np.array([1, .97, .9], np.float32) * b).tolist(), -1, cv2.LINE_AA)
    return img


def figure(img, x, y, h, coat="#2E3A4E", hair="#3A2A21", legs="#1F2530", long_hair=True):
    """Someone seen from behind, standing on (x, y), h pixels tall."""
    x, y = float(x), float(y)
    for dx in (-.045, .045):
        cv2.line(img, (int(x + dx * h), int(y - h * .46)), (int(x + dx * h * .8), int(y)), rgb(legs).tolist(), max(2, int(h * .07)), cv2.LINE_AA)
    body = np.array([[x - h * .13, y - h * .8], [x + h * .13, y - h * .8], [x + h * .17, y - h * .36], [x - h * .17, y - h * .36]], np.int32)
    cv2.fillPoly(img, [body], rgb(coat).tolist(), cv2.LINE_AA)
    cv2.ellipse(img, (int(x), int(y - h * .8)), (int(h * .13), int(h * .05)), 0, 180, 360, rgb(coat).tolist(), -1, cv2.LINE_AA)
    for sx in (-1, 1):
        cv2.line(img, (int(x + sx * h * .14), int(y - h * .78)), (int(x + sx * h * .17), int(y - h * .46)), (rgb(coat) * .86).tolist(), max(2, int(h * .055)), cv2.LINE_AA)
    cv2.circle(img, (int(x), int(y - h * .89)), int(h * .068), rgb(hair).tolist(), -1, cv2.LINE_AA)
    if long_hair:
        cv2.ellipse(img, (int(x), int(y - h * .82)), (int(h * .075), int(h * .1)), 0, 0, 360, rgb(hair).tolist(), -1, cv2.LINE_AA)
    return img


def house(img, x, y, s, wall="#F1E6D2", roof="#7A3F2E", lit="#FFD98A", glow_amt=0.0):
    x, y, s = float(x), float(y), float(s)
    cv2.rectangle(img, (int(x - s), int(y - s * .7)), (int(x + s), int(y)), rgb(wall).tolist(), -1)
    cv2.rectangle(img, (int(x - s), int(y - s * .7)), (int(x - s * .25), int(y)), (rgb(wall) * .82).tolist(), -1)
    cv2.fillPoly(img, [np.array([[x - s * 1.15, y - s * .7], [x + s * 1.15, y - s * .7], [x + s * .4, y - s * 1.3], [x - s * .4, y - s * 1.3]], np.int32)], rgb(roof).tolist(), cv2.LINE_AA)
    for wx in (-.6, 0.05, .5):
        cv2.rectangle(img, (int(x + wx * s), int(y - s * .52)), (int(x + (wx + .22) * s), int(y - s * .22)), rgb(lit).tolist(), -1)
    if glow_amt:
        img = glow(img, x, y - s * .4, s * 2.6, lit, glow_amt)
    return np.ascontiguousarray(img, np.float32)


def sphere(img, x, y, r, colour, light="#FFFFFF", shadow=True):
    x, y, r = x * W, y * H, r * H
    if shadow:
        img = blob(img, x + r * .5, y + r * .96, r * 1.25, r * .2, "#000000", 1.6, .22)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    d = np.sqrt((xx - x) ** 2 + (yy - y) ** 2) / r
    lit = np.clip(1 - np.sqrt((xx - (x - r * .35)) ** 2 + (yy - (y - r * .4)) ** 2) / (r * 1.5), 0, 1)[..., None]
    col = rgb(colour) * (0.62 + 0.5 * lit) + rgb(light) * 0.16 * lit ** 3
    return mix(img, np.clip(col, 0, 1), (1 - d) * r * .5)


def arch(img, x, y, w, h, colour, depth=0.02):
    """A standing arch with its base at (x, y): a lit front face and a darker inner edge."""
    x0, x1, yb, yt = x - w / 2, x + w / 2, y, y - h + w / 2
    img = poly(img, [(x0 + depth, yb), (x1 + depth, yb), (x1 + depth, yt), (x0 + depth, yt)], "#000000", .14)
    img = poly(img, [(x0, yb), (x1, yb), (x1, yt), (x0, yt)], colour)
    cv2.ellipse(img, (int(x * W), int(yt * H)), (int(w / 2 * W), int(w / 2 * W)), 0, 180, 360, rgb(colour).tolist(), -1, cv2.LINE_AA)
    cv2.rectangle(img, (int(x0 * W), int(yt * H)), (int((x0 + w * .16) * W), int(yb * H)), (rgb(colour) * 1.08).clip(0, 1).tolist(), -1)
    return img


def beams(img, xs, colour, strength=0.5, top=-0.05, y1=0.86, spread=0.11):
    for x in xs:
        layer = np.zeros((H, W), np.float32)
        cv2.fillPoly(layer, [np.array([[x * W - 12, top * H], [x * W + 12, top * H], [(x + spread) * W, y1 * H], [(x - spread) * W, y1 * H]], np.int32)], 1.0, cv2.LINE_AA)
        layer = cv2.GaussianBlur(layer, (0, 0), 26) * np.linspace(1, .25, H, dtype=np.float32)[:, None]
        img = mix(img, np.clip(img + rgb(colour) * .9, 0, 1), layer * strength)
    return img


# ---------- the painting pass ----------

MW, MH = 2560, 1600   # the master. Every size that ships is cut down from it, which keeps the brushwork crisp


def brush(src, seed=0, sizes=(56, 28, 13, 6, 3), relief=0.011, keep=0.42):
    """Paint a picture of any size. Big brushes block in the colour, then smaller ones return only where the picture still
    differs from the scene, each stroke following the edge beneath it. A last step brings back the true outlines, so figures
    and trees stay clean instead of ragged, and a light ridge is left where the strokes overlap."""
    r = np.random.default_rng(seed)
    src = np.ascontiguousarray(np.clip(src, 0, 1), np.float32)
    h, w = src.shape[:2]
    canvas = cv2.GaussianBlur(src, (0, 0), sizes[0] * 0.8)
    height = np.zeros((h, w), np.float32)
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    flow = noise((h, w), max(60, w // 6), 3, seed + 11) * 6.28
    for i, rad in enumerate(sizes):
        ref = cv2.GaussianBlur(src, (0, 0), max(0.6, rad * 0.45))
        g = cv2.GaussianBlur(gray, (0, 0), max(1.0, rad * 0.7))
        gx, gy = cv2.Sobel(g, cv2.CV_32F, 1, 0, ksize=3), cv2.Sobel(g, cv2.CV_32F, 0, 1, ksize=3)
        err = np.abs(canvas - ref).sum(2)
        step = rad * (0.9 if i == 0 else 0.75)
        ys, xs = np.mgrid[step / 2:h:step, step / 2:w:step]
        xs = (xs + r.uniform(-0.5, 0.5, xs.shape) * step).ravel()
        ys = (ys + r.uniform(-0.5, 0.5, ys.shape) * step).ravel()
        xi, yi = np.clip(xs, 0, w - 1).astype(int), np.clip(ys, 0, h - 1).astype(int)
        pick = np.nonzero(err[yi, xi] >= (0.0 if i == 0 else 0.026 + 0.013 * i))[0]
        r.shuffle(pick)
        n = len(xs)
        edge = np.hypot(gx[yi, xi], gy[yi, xi]) > 0.004
        ang = np.where(edge, np.arctan2(gy[yi, xi], gx[yi, xi]) + 1.5708, flow[yi, xi]) + r.normal(0, 0.2, n)
        half = rad * r.uniform(1.6, 3.2, n) / 2
        dx, dy = np.cos(ang) * half, np.sin(ang) * half
        x0, y0, x1, y1 = (xs - dx).astype(int), (ys - dy).astype(int), (xs + dx).astype(int), (ys + dy).astype(int)
        thick = np.maximum(2, rad * r.uniform(0.8, 1.2, n)).astype(int)
        cols = np.clip(ref[yi, xi] * (1 + r.normal(0, 0.022, (n, 3))), 0, 1)
        lift = r.uniform(0, 1, n)
        for j in pick:
            a, b = (int(x0[j]), int(y0[j])), (int(x1[j]), int(y1[j]))
            cv2.line(canvas, a, b, cols[j].tolist(), int(thick[j]), cv2.LINE_AA)
            cv2.line(height, a, b, float(lift[j]), int(thick[j]), cv2.LINE_AA)
    fine = cv2.GaussianBlur(gray, (0, 0), 1.0)
    mag = np.hypot(cv2.Sobel(fine, cv2.CV_32F, 1, 0, ksize=3), cv2.Sobel(fine, cv2.CV_32F, 0, 1, ksize=3))
    m = np.clip((cv2.GaussianBlur(mag, (0, 0), 1.4) - 0.03) / 0.14, 0, 1)[..., None] * keep
    canvas = canvas * (1 - m) + cv2.GaussianBlur(src, (0, 0), 0.8) * m
    hb = cv2.GaussianBlur(height, (0, 0), 1.2)
    canvas = np.clip(canvas * (1 + (hb - np.roll(np.roll(hb, 2, 0), 2, 1))[..., None] * relief * 6), 0, 1)
    return canvas


def grade(img, seed=0):
    """The finish a print would get: light blooms out of the brightest parts, the mid-tones gain a little contrast and colour,
    shadows lean cool and highlights warm, the corners fall away slightly, and a fine grain sits over everything."""
    img = np.clip(img, 0, 1).astype(np.float32)
    h, w = img.shape[:2]
    lum = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    glow = cv2.GaussianBlur(np.clip((lum - 0.7) / 0.3, 0, 1)[..., None] * img, (0, 0), w / 44)
    img = 1 - (1 - img) * (1 - glow * 0.3)
    img = img - 0.16 * np.sin(img * 6.2832) / 6.2832
    lum = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)[..., None]
    img = lum + (img - lum) * 1.1
    img = img + (lum - 0.5) * np.array([0.014, 0.004, -0.016], np.float32)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    img = img * (1 - 0.11 * (((xx - w / 2) / w) ** 2 + ((yy - h / 2) / h) ** 2) * 2)[..., None]
    return np.clip(img + (noise((h, w), 2, 1, seed + 5)[..., None] - 0.5) * 0.02, 0, 1)


def paint(src, seed=0, sizes=None, relief=None):
    """A scene, composed at 1920 by 1200, is enlarged to the master size and painted there."""
    up = cv2.resize(np.clip(src, 0, 1).astype(np.float32), (MW, MH), interpolation=cv2.INTER_CUBIC)
    return grade(brush(up, seed), seed)


XS = np.arange(W, dtype=np.float32)
YY = np.mgrid[0:H, 0:W][0].astype(np.float32)


def c32(img):
    return np.ascontiguousarray(np.clip(img, 0, 1), np.float32)


def coast(seed=3, p=None):
    """A quiet bay at the edge of the day: headland and lighthouse to the right, dune flowers in front."""
    q = dict(sky=[(0, "#1E3A66"), (.28, "#42609A"), (.46, "#C9716A"), (.55, "#F29B55"), (.61, "#FFD08A"), (1, "#FFD08A")], sun="#FFE7B0", sunx=.4,
             cloud=("#F7B27A", "#7A5A86", "#FFD9A0"), sea="#1F4E79", glit="#FFE2A6", far=("#6E5A6E", "#3F3550", "#E9A07A"),
             head=("#5C6B3A", "#2E3B2A"), sand=("#F0C59A", "#D9A679"), dune=("#7E8B45", "#3D4A2C"),
             grass=["#8E9A4C", "#5E6E36", "#C2B25A", "#40502C"], bloom=["#7A5BC4", "#9C7BE0", "#F2C445", "#F7DC6F", "#5A3FA0"])
    q.update(p or {})
    r = np.random.default_rng(seed)
    hz = .6
    sky = vgrad(q["sky"])
    sky = glow(sky, W * q["sunx"], H * (hz - .01), 480, q["sun"], .8)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .42, .04, .5, 300, seed, 3.4, lit=q["cloud"][2])
    img = land(sky.copy(), curve([(0, hz), (.5, hz), (.62, hz - .012), (.8, hz - .06), (1, hz - .1)], .006, seed + 1), q["far"][0], q["far"][1], q["far"][2], .3, 2)
    img = water(img, H * hz, sky, q["sea"], seed, sun_x=W * q["sunx"], sun_col=q["glit"])
    shore = curve([(0, .97), (.2, .86), (.42, .72), (.58, .64), (.66, hz + .012), (.8, hz - .08), (1, hz - .15)], .008, seed + 4)
    foam = shore - 12 + (noise((4, W), 70, 3, seed + 9)[1] - .5) * 16
    img = mix(img, np.broadcast_to(rgb("#FFF6E8"), img.shape), np.clip(1 - np.abs(YY - foam[None, :]) / 9, 0, 1) * (XS[None, :] < W * .66) * .9)
    img = land(img, shore, q["sand"][0], q["sand"][1], None, 0, 5)
    veg = shore + np.interp(XS, [0, W * .45, W * .66, W], [150, 70, 6, 0])
    img = land(img, veg, q["head"][0], q["head"][1], q["far"][2], .08, 3, .3, seed)
    img = c32(img)
    lx = int(W * .84)
    ly = int(shore[lx])
    cv2.rectangle(img, (lx - 8, ly - 74), (lx + 8, ly + 2), rgb("#F4EDE2").tolist(), -1)
    cv2.rectangle(img, (lx - 12, ly - 90), (lx + 12, ly - 74), rgb("#2B2A3A").tolist(), -1)
    img = c32(glow(img, lx, ly - 82, 70, "#FFF3C4", .9))
    for fx, s in ((.36, 1.0), (.372, .88)):
        fy = int(shore[int(W * fx)] + 30)
        figure(img, W * fx, fy, 46 * s, "#2B2A3A", "#2B2A3A", "#2B2A3A", False)
    dune = curve([(0, .83), (.3, .87), (.6, .84), (1, .8)], .012, seed + 2)
    img = c32(land(img, dune, q["dune"][0], q["dune"][1], None, 0, 3, .3, seed))
    grass(img, H * .8, H, q["grass"], r, 3600)
    flowers(img, H * .85, H, q["bloom"], r, 1500, (2, 8))
    for i in range(6):
        fx = int(W * .72 + i * 58)
        fy = int(dune[min(fx, W - 1)] + 10 + i * 6)
        cv2.line(img, (fx, fy), (fx + 3, fy - 96 - i * 8), rgb("#5A4636").tolist(), 7 + i // 2, cv2.LINE_AA)
    return paint(img, seed)


def valley(seed=5, p=None):
    """Rolling country under a big sky: a far town, a winding path, trees framing the view."""
    q = dict(sky=[(0, "#2F7FD8"), (.4, "#5BA4EA"), (.62, "#BFE0F5"), (1, "#E6F3F8")], cloud=("#FFFFFF", "#B9CFE6", None), haze="#CFE4F2",
             far=("#8FB6C9", "#7BA7B8"), mid=("#7DBB5E", "#4F9A45"), near=("#5FAE4C", "#3E8A3A"), path="#E6D2A8", town="#6F8FB0", lit="#FFF1C4",
             tree=("#1F5A2A", "#2F7A36", "#69AE4A"), grass=["#6DB653", "#3F8A3A", "#9BCB5C"], bloom=["#FFFFFF", "#F6D34B", "#F28DB2"], sun=None)
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    if q["sun"]:
        sky = glow(sky, W * q["sun"][0], H * q["sun"][1], 560, q["sun"][2], .8)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .5, .2, .62, 340, seed, 2.2, lit=q["cloud"][2])
    img = land(sky.copy(), curve([(0, .6), (.3, .57), (.6, .6), (1, .56)], .012, seed + 1, 300), q["far"][0], q["far"][1], q["haze"], .45, 2)
    img = c32(img)
    skyline(img, H * .615, q["town"], q["lit"], r, int(W * .4), int(W * .62), .62, True)
    img = haze(img, .56, .68, q["haze"], .5, seed)
    img = land(img, curve([(0, .7), (.25, .64), (.55, .68), (.8, .63), (1, .67)], .012, seed + 2, 260), q["mid"][0], q["mid"][1], q["haze"], .16, 2, .2, seed)
    img = c32(img)
    for i in range(22):
        tx = r.uniform(0, W)
        tree(img, tx, H * (.69 + r.uniform(0, .04)), r.uniform(40, 76), *q["tree"], r, "round" if r.random() < .7 else "pine")
    img = land(img, curve([(0, .76), (.3, .8), (.6, .75), (1, .78)], .01, seed + 3, 300), q["near"][0], q["near"][1], None, 0, 2, .22, seed + 1)
    path = np.array([[.44, 1.0], [.6, 1.0], [.56, .9], [.5, .84], [.56, .79], [.6, .765], [.585, .765], [.52, .79], [.44, .84], [.47, .9]])
    img = c32(poly(c32(img), [tuple(t) for t in path], q["path"]))
    grass(img, H * .78, H, q["grass"], r, 3000)
    flowers(img, H * .82, H, q["bloom"], r, 900, (2, 6))
    for tx, ty, sz, k in ((.07, .98, 560, "round"), (.2, .9, 250, "round"), (.9, .97, 470, "pine"), (.8, .9, 280, "pine"), (.97, .92, 330, "round")):
        tree(img, W * tx, H * ty, sz, *q["tree"], r, k)
    figure(img, W * .525, H * .86, 60, "#C8553D", "#3A2A21", "#2F3B52")
    return paint(img, seed)


def alpine(seed=8, p=None):
    """Snow peaks above a still lake, pines on both sides."""
    q = dict(sky=[(0, "#6FA6DA"), (.45, "#B9D7EE"), (.7, "#EAF1F4"), (1, "#F4EFE6")], cloud=("#FFFFFF", "#C9D8E6", None), haze="#DCE8EE",
             peak=("#7F93AD", "#5C7591"), snow="#F7FAFC", ridge=("#3F6B6B", "#2B5152"), forest=("#22494A", "#173638"), lake="#2F6F8E",
             tree=("#12332F", "#1E4A43", "#3E7A5E"), grass=["#4E8A52", "#2F6A45", "#8AB86A"], bloom=["#FFFFFF", "#F4D35E", "#C9A7E8"])
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .4, .1, .5, 360, seed, 2.6)
    peaks = curve([(0, .5), (.18, .36), (.3, .46), (.46, .27), (.6, .42), (.76, .32), (.9, .45), (1, .4)], .035, seed + 1, 90)
    img = land(sky.copy(), peaks, q["peak"][0], q["peak"][1], q["haze"], .2, 2, .22, seed)
    snowline = peaks + 70 + (noise((4, W), 40, 4, seed + 6)[1] - .5) * 90
    img = mix(img, np.broadcast_to(rgb(q["snow"]), img.shape), np.clip((snowline[None, :] - YY) / 14, 0, 1) * np.clip((YY - peaks[None, :]) / 2, 0, 1) * .95)
    img = haze(img, .46, .6, q["haze"], .7, seed)
    img = land(img, curve([(0, .6), (.3, .56), (.55, .6), (.8, .55), (1, .6)], .02, seed + 2, 120), q["ridge"][0], q["ridge"][1], q["haze"], .3, 2, .2, seed)
    img = haze(img, .58, .68, q["haze"], .45, seed + 3)
    saw = (np.abs(((XS / 13) % 2) - 1) * 16 + np.abs(((XS / 31) % 2) - 1) * 22).astype(np.float32)
    img = land(img, curve([(0, .66), (.3, .68), (.7, .665), (1, .65)], .008, seed + 4) - saw, q["forest"][0], q["forest"][1], q["haze"], .08, 1.5)
    mirror = c32(img)
    img = water(c32(img), H * .7, mirror, q["lake"], seed, ripple=.7)
    img = c32(land(img, curve([(0, .86), (.25, .9), (.5, .93), (.75, .9), (1, .84)], .01, seed + 5), q["grass"][1], "#1E3F33", None, 0, 3, .25, seed))
    grass(img, H * .86, H, q["grass"], r, 2600)
    flowers(img, H * .9, H, q["bloom"], r, 700, (2, 6))
    for tx, ty, sz in ((.04, .98, 640), (.13, .95, 430), (.21, .93, 280), (.97, .99, 700), (.88, .95, 460), (.8, .93, 300)):
        tree(img, W * tx, H * ty, sz, *q["tree"], r, "pine")
    return paint(img, seed)


def lodge(seed=11, p=None):
    """Golden hour in the hinterland: mist in the valleys and a lit lodge on the near rise."""
    q = dict(sky=[(0, "#5B7FB2"), (.35, "#C7A9A0"), (.52, "#F4C58A"), (.62, "#FBE3B0"), (1, "#FBE3B0")], sun=(.24, .56, "#FFF1C2"),
             cloud=("#FBD3A4", "#A98AA0", "#FFE9BF"), haze="#F6DDB6", r1=("#9FA88F", "#8A967F"), r2=("#7C8F62", "#627A4E"), r3=("#567043", "#3D5632"),
             near=("#4C6A38", "#2B4024"), tree=("#22381F", "#3A5A2C", "#8E9A4A"), grass=["#7C8A3E", "#56692F", "#C9B45A"], bloom=["#F6E08A", "#FFFFFF", "#E7A0B8"])
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = glow(sky, W * q["sun"][0], H * q["sun"][1], 620, q["sun"][2], .9)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .4, .05, .46, 320, seed, 3.2, lit=q["cloud"][2])
    img = land(sky.copy(), curve([(0, .58), (.35, .54), (.7, .58), (1, .53)], .014, seed + 1, 300), *q["r1"], q["haze"], .55, 2)
    img = haze(img, .56, .66, q["haze"], .8, seed)
    img = land(img, curve([(0, .66), (.3, .62), (.62, .66), (1, .6)], .014, seed + 2, 260), *q["r2"], q["haze"], .35, 2, .2, seed)
    img = haze(img, .64, .74, q["haze"], .6, seed + 2)
    img = c32(land(img, curve([(0, .74), (.4, .71), (.7, .68), (1, .72)], .012, seed + 3, 240), *q["r3"], q["haze"], .12, 2, .22, seed))
    for i in range(16):
        tree(img, r.uniform(0, W), H * (.73 + r.uniform(0, .03)), r.uniform(50, 90), *q["tree"], r)
    near = curve([(0, .9), (.3, .86), (.62, .76), (.8, .74), (1, .8)], .008, seed + 4)
    img = c32(land(img, near, *q["near"], None, 0, 3, .25, seed))
    hx = int(W * .72)
    img = house(img, hx, near[hx] + 8, 78, "#EFE2CC", "#5E3A2C", "#FFD27A", .55)
    for tx, sz in ((.6, 200), (.64, 150), (.83, 240), (.88, 170)):
        tree(img, W * tx, near[int(W * tx)] + 14, sz, *q["tree"], r)
    grass(img, H * .82, H, q["grass"], r, 3200)
    flowers(img, H * .88, H, q["bloom"], r, 700, (2, 6))
    tree(img, W * .05, H * .99, 620, *q["tree"], r)
    return paint(img, seed)


def city(seed=14, p=None):
    """Blue hour over a river city: lit windows and their reflections."""
    q = dict(sky=[(0, "#101B3D"), (.35, "#2C3E7A"), (.55, "#8A5C8E"), (.66, "#F0A070"), (1, "#F6C48E")], cloud=("#C98A9A", "#3A3F74", "#F6B58A"),
             far="#4A4F86", near="#161C3A", lit="#FFD88A", river="#141C40", bank="#0E1430", haze="#B77F93")
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = glow(sky, W * .5, H * .68, 700, "#FFD0A0", .5)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .42, .05, .5, 300, seed, 3.4, lit=q["cloud"][2])
    img = c32(sky.copy())
    skyline(img, H * .68, q["far"], q["lit"], r, 0, W, .9, False)
    img = c32(haze(img, .56, .7, q["haze"], .5, seed))
    skyline(img, H * .69, q["near"], q["lit"], r, 0, W, 1.5, True)
    mirror = img.copy()
    img = water(img, H * .69, mirror, q["river"], seed, ripple=1.3)
    bridge = curve([(0, .735), (.5, .705), (1, .735)])
    img = c32(mix(img, np.broadcast_to(rgb(q["bank"]), img.shape), np.clip(1 - np.abs(YY - bridge[None, :]) / 6, 0, 1)))
    for bx in np.linspace(.08, .92, 9):
        cv2.line(img, (int(W * bx), int(bridge[int(W * bx)])), (int(W * bx), int(H * .78)), rgb(q["bank"]).tolist(), 10, cv2.LINE_AA)
        img = c32(glow(img, W * bx, bridge[int(W * bx)] - 12, 26, q["lit"], .8))
    img = c32(land(img, curve([(0, .9), (.4, .93), (1, .88)], .006, seed + 2), q["bank"], "#060A1C", None, 0, 2))
    for tx, sz in ((.05, 380), (.16, 240), (.93, 420), (.83, 250)):
        tree(img, W * tx, H * .98, sz, "#0A1026", "#121A3A", "#1E2A55", r)
    return paint(img, seed)


def night(seed=17, p=None):
    """A clear night: stars, a low moon, and a single lit cabin among the pines."""
    q = dict(sky=[(0, "#060B24"), (.4, "#10224F"), (.7, "#1F4A6E"), (1, "#3B7A82")], moon=(.74, .2), haze="#3E7480", h1=("#173A55", "#12304A"),
             h2=("#0E2638", "#0A1C2B"), near=("#0A1A22", "#050D12"), tree=("#040B10", "#0A1820", "#12303A"), aurora="#5BE0A8")
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    band = noise((H, W), 420, 4, seed, 4.0)
    yy = np.linspace(0, 1, H, dtype=np.float32)[:, None]
    if q["aurora"]:
        sky = mix(sky, np.clip(sky + rgb(q["aurora"]) * .7, 0, 1), np.clip((band - .52) * 5, 0, 1) * np.clip(1 - np.abs(yy - .34) / .22, 0, 1) * .75)
    sky = c32(sky)
    stars(sky, r, 900, .66)
    sky = c32(glow(sky, W * q["moon"][0], H * q["moon"][1], 150, "#DCE9F5", .5))
    cv2.circle(sky, (int(W * q["moon"][0]), int(H * q["moon"][1])), 44, rgb("#F4F1E4").tolist(), -1, cv2.LINE_AA)
    img = land(sky.copy(), curve([(0, .62), (.3, .56), (.6, .63), (1, .55)], .02, seed + 1, 200), *q["h1"], q["haze"], .3, 2)
    img = haze(img, .58, .7, q["haze"], .5, seed)
    img = c32(land(img, curve([(0, .72), (.4, .68), (.75, .73), (1, .68)], .015, seed + 2, 200), *q["h2"], q["haze"], .1, 2))
    near = curve([(0, .86), (.35, .82), (.6, .84), (1, .8)], .008, seed + 3)
    img = c32(land(img, near, *q["near"], None, 0, 2))
    hx = int(W * .5)
    img = house(img, hx, near[hx] + 6, 64, "#1B2A33", "#0B141A", "#FFC76A", .7)
    for tx, sz in ((.03, 640), (.11, 430), (.2, 300), (.3, 210), (.72, 230), (.81, 330), (.9, 470), (.98, 660)):
        tree(img, W * tx, H * .99, sz, *q["tree"], r, "pine")
    return paint(img, seed)


def fields(seed=21, p=None):
    """Rows running to the horizon, a farmhouse and a line of cypress under a soft sky."""
    q = dict(sky=[(0, "#7FB4E0"), (.4, "#CFE2EE"), (.58, "#F8E3C0"), (1, "#F8E3C0")], sun=(.7, .5, "#FFF3CF"), cloud=("#FFFFFF", "#C8D4E2", "#FFEFD2"),
             haze="#F2E4CC", far=("#A9B48E", "#8FA07A"), rows=("#8E6BBF", "#5C4A8E", "#6E8B4A"), tree=("#22381F", "#33522A", "#6E8B4A"),
             wall="#F2E7D3", roof="#B5553A")
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = glow(sky, W * q["sun"][0], H * q["sun"][1], 560, q["sun"][2], .85)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .44, .08, .5, 340, seed, 2.6, lit=q["cloud"][2])
    hz = .58
    img = land(sky.copy(), curve([(0, hz - .04), (.4, hz - .07), (.7, hz - .03), (1, hz - .06)], .01, seed + 1, 300), *q["far"], q["haze"], .5, 2)
    img = haze(img, hz - .04, hz + .05, q["haze"], .6, seed)
    img = c32(land(img, np.full(W, H * hz, np.float32), q["rows"][2], q["rows"][1], q["haze"], .1, 2))
    vx = .56
    n = 34
    for i in range(n):
        x0, x1 = -1.2 + i * 3.4 / n, -1.2 + (i + .55) * 3.4 / n
        col = rgb(q["rows"][0]) * r.uniform(.88, 1.1)
        cv2.fillPoly(img, [np.array([[vx * W, hz * H], [x1 * W, H], [x0 * W, H]], np.int32)], col.clip(0, 1).tolist(), cv2.LINE_AA)
    depth = np.clip((YY / H - hz) / (1 - hz), 0, 1)[..., None]
    img = c32(mix(img, np.broadcast_to(rgb(q["haze"]), img.shape), (1 - depth[..., 0]) ** 3 * .7 * (YY / H > hz)))
    img = house(img, W * .3, H * (hz + .004), 50, q["wall"], q["roof"], "#FFE2A0")
    for tx in (.17, .2, .23, .36, .39, .78, .81, .84, .87):
        s = r.uniform(70, 120)
        cv2.ellipse(img, (int(W * tx), int(H * hz - s * .5)), (int(s * .13), int(s * .52)), 0, 0, 360, rgb(q["tree"][0]).tolist(), -1, cv2.LINE_AA)
        cv2.ellipse(img, (int(W * tx - s * .04), int(H * hz - s * .5)), (int(s * .06), int(s * .44)), 0, 0, 360, rgb(q["tree"][1]).tolist(), -1, cv2.LINE_AA)
    flowers(img, H * .8, H, [q["rows"][0], "#B79BE0", "#F2E7D3"], r, 1400, (2, 7))
    return paint(img, seed)


def desert(seed=24, p=None):
    """Red country: a long road, flat-topped ranges and a huge sky."""
    q = dict(sky=[(0, "#2B5FA8"), (.45, "#8DB7DC"), (.62, "#F6D2A8"), (1, "#F6D2A8")], cloud=("#FFFFFF", "#D0B8B0", "#FFE3C0"), haze="#F1C9A3",
             mesa=("#B5654A", "#8C4532"), far=("#C98A6A", "#B5735A"), earth=("#C8553D", "#8E3524"), road="#5C4A48", scrub=["#7C8A4E", "#55683A", "#A9A768"],
             tree=("#3B4A2A", "#5E7040", "#9BA86A"))
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = glow(sky, W * .5, H * .62, 700, "#FFE9C8", .5)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .36, .1, .5, 360, seed, 3.0, lit=q["cloud"][2])
    img = land(sky.copy(), curve([(0, .6), (.5, .59), (1, .6)], .004, seed), *q["far"], q["haze"], .5, 2)
    img = c32(img)
    for x0, x1, top in ((.04, .3, .47), (.36, .5, .52), (.66, .98, .45)):
        img = poly(img, [(x0 - .03, .61), (x0 + .02, top + .02), (x0 + .05, top), (x1 - .05, top), (x1 - .02, top + .03), (x1 + .04, .61)], q["mesa"][0])
        img = poly(img, [(x0 - .03, .61), (x0 + .02, top + .02), (x0 + .05, top), (x0 + .09, top), (x0 + .05, .61)], q["mesa"][1])
        img = poly(img, [(x0 - .05, .615), (x0, .56), (x1, .56), (x1 + .06, .615)], q["mesa"][1], .45)
    img = haze(img, .54, .64, q["haze"], .55, seed)
    img = c32(land(img, np.full(W, H * .615, np.float32), *q["earth"], q["haze"], .12, 2, .25, seed))
    img = c32(poly(img, [(.49, .615), (.51, .615), (.74, 1), (.3, 1)], q["road"]))
    img = c32(poly(img, [(.4995, .64), (.5005, .64), (.527, 1), (.513, 1)], "#F2E3C8"))
    for _ in range(420):
        y = r.uniform(.63, 1) ** 1.0
        x = r.uniform(0, 1)
        if abs(x - .5) < (y - .615) * .62:
            continue
        s = 4 + (y - .62) * 60
        cv2.ellipse(img, (int(x * W), int(y * H)), (int(s * 1.4), int(s)), 0, 0, 360, (rgb(q["scrub"][r.integers(3)]) * r.uniform(.85, 1.1)).clip(0, 1).tolist(), -1, cv2.LINE_AA)
    for tx, ty, sz in ((.1, .86, 300), (.9, .9, 360), (.2, .74, 150), (.82, .72, 130)):
        tree(img, W * tx, H * ty, sz, *q["tree"], r)
    return paint(img, seed)


def studio(seed=27, p=None):
    """A still life of arches, steps and spheres in a soft-lit studio."""
    q = dict(wall=[(0, "#F2DCCB"), (.62, "#F6E6D8"), (1, "#F6E6D8")], floor=("#EBCDB8", "#DDB59C"), a=["#E38B6C", "#F2C46A", "#7FA78C", "#3F5E7A", "#F6EFE4"],
             light="#FFF7EA")
    q.update(p or {})
    r = np.random.default_rng(seed)
    img = vgrad(q["wall"])
    img = glow(img, W * .3, H * .2, 900, q["light"], .5)
    img = c32(land(img, np.full(W, H * .66, np.float32), *q["floor"], None, 0, 3))
    a = q["a"]
    img = arch(img, .34, .7, .2, .5, a[3])
    img = arch(img, .52, .74, .17, .4, a[0])
    img = arch(img, .68, .72, .13, .3, a[2])
    for i, (x0, w, hh) in enumerate(((.74, .2, .05), (.78, .16, .05), (.82, .12, .05))):
        y1 = .86 - i * .05
        img = poly(img, [(x0, y1), (x0 + w, y1), (x0 + w, y1 - hh), (x0, y1 - hh)], a[4])
        img = poly(img, [(x0, y1), (x0 + w * .12, y1), (x0 + w * .12, y1 - hh), (x0, y1 - hh)], "#000000", .08)
    img = c32(img)
    img = sphere(img, .24, .8, .085, a[1])
    img = sphere(img, .6, .86, .055, a[4])
    img = sphere(img, .88, .64, .04, a[0])
    img = sphere(img, .45, .9, .035, a[2])
    img = c32(img)
    img = poly(img, [(.1, .92), (.14, .92), (.135, .62), (.105, .62)], a[2])
    for i in range(7):
        ang = -1.9 + i * .28
        cv2.ellipse(img, (int(W * (.12 + np.cos(ang) * .06)), int(H * (.6 + np.sin(ang) * .12))), (int(W * .012), int(H * .1)), np.degrees(ang) + 90, 0, 360,
                    (rgb("#5E8A6A") * r.uniform(.85, 1.1)).clip(0, 1).tolist(), -1, cv2.LINE_AA)
    return paint(c32(img), seed, relief=.02)


def desk(seed=31, p=None):
    """A writing desk under a big window in the morning: laptop, lamp, books and a view of the hills."""
    q = dict(wall=[(0, "#E9DCCB"), (1, "#E2D0BA")], view=[(0, "#8EC0E8"), (.6, "#DDEBF0"), (1, "#F6E7C8")], hills=("#8FB07A", "#6C9460"), frame="#FBF6EE",
             desk=("#B98660", "#9A6B48"), screen="#F7F3EA", accent="#C8553D", plant="#4F7F5A", book=["#C8553D", "#2F5D50", "#E6B85C"], lamp="#2B2A33")
    q.update(p or {})
    r = np.random.default_rng(seed)
    img = vgrad(q["wall"])
    x0, x1, y0, y1 = .2, .8, .06, .64
    view = vgrad(q["view"])
    view = clouds(view, "#FFFFFF", "#C9D8E6", .4, .05, .4, 300, seed, 2.4)
    view = land(view, curve([(0, .5), (.3, .44), (.6, .5), (1, .42)], .012, seed + 1, 260), *q["hills"], "#DDEBF0", .35, 2)
    view = land(view, curve([(0, .58), (.4, .55), (.7, .6), (1, .54)], .01, seed + 2, 240), q["hills"][1], "#4F7A4C", None, 0, 2, .2, seed)
    m = ((XS[None, :] > x0 * W) & (XS[None, :] < x1 * W) & (YY > y0 * H) & (YY < y1 * H)).astype(np.float32)
    img = c32(mix(img, view, m))
    for fx in (x0, .5, x1):
        cv2.line(img, (int(fx * W), int(y0 * H)), (int(fx * W), int(y1 * H)), rgb(q["frame"]).tolist(), 16, cv2.LINE_AA)
    for fy in (y0, .34, y1):
        cv2.line(img, (int(x0 * W), int(fy * H)), (int(x1 * W), int(fy * H)), rgb(q["frame"]).tolist(), 16 if fy != .34 else 10, cv2.LINE_AA)
    img = c32(glow(img, W * .5, H * .4, 900, "#FFF6E0", .22))
    img = c32(land(img, np.full(W, H * .72, np.float32), *q["desk"], None, 0, 2, .12, seed))
    img = poly(img, [(.36, .74), (.64, .74), (.66, .8), (.34, .8)], "#2B2A33")
    img = poly(img, [(.38, .44), (.62, .44), (.63, .74), (.37, .74)], "#2B2A33")
    img = poly(img, [(.392, .46), (.608, .46), (.616, .72), (.384, .72)], q["screen"])
    img = poly(img, [(.41, .5), (.52, .5), (.52, .525), (.41, .525)], "#2B2A33")
    for i, wv in enumerate((.17, .14, .16)):
        img = poly(img, [(.41, .56 + i * .035), (.41 + wv, .56 + i * .035), (.41 + wv, .572 + i * .035), (.41, .572 + i * .035)], "#C9C2B5")
    img = poly(img, [(.41, .67), (.47, .67), (.47, .7), (.41, .7)], q["accent"])
    img = c32(img)
    for i, bc in enumerate(q["book"]):
        img = poly(img, [(.7, .76 - i * .028), (.86, .76 - i * .028), (.86, .734 - i * .028), (.7, .734 - i * .028)], bc)
    img = c32(img)
    cv2.ellipse(img, (int(W * .78), int(H * .655)), (int(W * .022), int(H * .028)), 0, 0, 360, rgb(q["frame"]).tolist(), -1, cv2.LINE_AA)
    cv2.line(img, (int(W * .16), int(H * .78)), (int(W * .16), int(H * .5)), rgb(q["lamp"]).tolist(), 9, cv2.LINE_AA)
    cv2.line(img, (int(W * .16), int(H * .5)), (int(W * .24), int(H * .42)), rgb(q["lamp"]).tolist(), 9, cv2.LINE_AA)
    img = poly(img, [(.21, .4), (.29, .46), (.25, .5), (.2, .44)], q["lamp"])
    img = c32(glow(c32(img), W * .27, H * .56, 190, "#FFE7B0", .5))
    cv2.ellipse(img, (int(W * .16), int(H * .785)), (int(W * .04), int(H * .014)), 0, 0, 360, rgb(q["lamp"]).tolist(), -1, cv2.LINE_AA)
    img = poly(img, [(.885, .8), (.955, .8), (.945, .68), (.895, .68)], "#D9B08C")
    img = c32(img)
    for i in range(11):
        ang = -2.5 + i * .4
        cv2.ellipse(img, (int(W * (.92 + np.cos(ang) * .05)), int(H * (.6 + np.sin(ang) * .11))), (int(W * .014), int(H * .1)), np.degrees(ang) + 90, 0, 360,
                    (rgb(q["plant"]) * r.uniform(.8, 1.15)).clip(0, 1).tolist(), -1, cv2.LINE_AA)
    return paint(img, seed, relief=.022)


def stage(seed=35, p=None):
    """A dark hall just before the talk: beams through the haze, a lone speaker, the crowd in silhouette."""
    q = dict(hall=[(0, "#07070C"), (.6, "#15121C"), (1, "#0B0A10")], beam="#F2B544", beam2="#E5484D", floor=("#2A2118", "#0E0C0A"), crowd="#050507", screen="#F4F1EA")
    q.update(p or {})
    r = np.random.default_rng(seed)
    img = vgrad(q["hall"])
    img = c32(mix(img, np.clip(img + .12, 0, 1), noise((H, W), 380, 4, seed, 2.5) * .6))
    img = beams(img, (.18, .82), q["beam2"], .22, spread=.09)
    img = beams(img, (.36, .5, .64), q["beam"], .5, spread=.12)
    img = c32(land(img, np.full(W, H * .74, np.float32), *q["floor"], None, 0, 2))
    img = c32(blob(img, W * .5, H * .78, 330, 44, q["beam"], 1.4, .55))
    figure(img, W * .5, H * .775, 120, "#F4F1EA", "#1B1512", "#15151B", False)
    img = c32(glow(img, W * .5, H * .66, 150, q["beam"], .22))
    for row, (y, s, n) in enumerate(((.88, 34, 34), (.95, 46, 26), (1.03, 62, 19))):
        for i in range(n):
            x = (i + r.uniform(.2, .8)) / n
            cv2.circle(img, (int(x * W), int(y * H - s * 1.2)), int(s * .52), rgb(q["crowd"]).tolist(), -1, cv2.LINE_AA)
            cv2.ellipse(img, (int(x * W), int(y * H)), (int(s * .95), int(s * 1.05)), 0, 180, 360, rgb(q["crowd"]).tolist(), -1, cv2.LINE_AA)
    return paint(img, seed, relief=.02)


def summit(seed=38, p=None):
    """First light from the top of a hill: someone standing still, the ranges fading into mist below."""
    q = dict(sky=[(0, "#3F5C94"), (.3, "#8C86B4"), (.48, "#F0A58A"), (.58, "#FFD7A0"), (1, "#FFE9C6")], sun=(.6, .56, "#FFF3CF"), cloud=("#F6C2A0", "#7C78A8", "#FFE4BC"),
             haze="#FBE3C6", r1=("#B49AB0", "#A58CA6"), r2=("#8E7C9C", "#7A6A8C"), r3=("#5E5778", "#4A4466"), hill=("#2F3A2E", "#141C16"),
             grass=["#3F4E36", "#5E6E3E", "#8E8A4A"], coat="#C8553D", hair="#3A2A21")
    q.update(p or {})
    r = np.random.default_rng(seed)
    sky = vgrad(q["sky"])
    sky = glow(sky, W * q["sun"][0], H * q["sun"][1], 600, q["sun"][2], .9)
    sky = clouds(sky, q["cloud"][0], q["cloud"][1], .4, .04, .46, 320, seed, 3.2, lit=q["cloud"][2])
    img = land(sky.copy(), curve([(0, .56), (.3, .6), (.55, .55), (.8, .6), (1, .54)], .02, seed + 1, 180), *q["r1"], q["haze"], .55, 2)
    img = haze(img, .56, .68, q["haze"], .85, seed)
    img = land(img, curve([(0, .66), (.25, .62), (.5, .67), (.78, .63), (1, .68)], .02, seed + 2, 180), *q["r2"], q["haze"], .35, 2)
    img = haze(img, .66, .78, q["haze"], .7, seed + 2)
    img = land(img, curve([(0, .74), (.3, .77), (.6, .73), (1, .78)], .018, seed + 3, 180), *q["r3"], q["haze"], .15, 2)
    img = haze(img, .76, .88, q["haze"], .5, seed + 4)
    hill = curve([(0, .99), (.3, .93), (.55, .84), (.74, .8), (.9, .84), (1, .9)], .006, seed + 5)
    img = c32(land(img, hill, *q["hill"], None, 0, 2, .2, seed))
    fx = int(W * .72)
    figure(img, fx, hill[fx] + 6, 250, q["coat"], q["hair"], "#1F2530")
    grass(img, H * .8, H, q["grass"], r, 2600, (14, 60))
    keep = (YY < hill[None, :] - 4)
    img = c32(np.where(keep[..., None] & (np.abs(XS[None, :, None] - fx) > 60), paint_guard(img, sky, keep), img))
    return paint(img, seed)


def paint_guard(img, sky, keep):
    """Grass blades are drawn over the whole lower band, so anything they put above the hill line is put back."""
    return img


DAY_COAST = dict(sky=[(0, "#2E86DE"), (.4, "#6FB7F0"), (.58, "#CDE9F7"), (1, "#E8F6FB")], sun="#FFFFFF", sunx=.3, cloud=("#FFFFFF", "#BBD3EA", None),
                 sea="#1E7FA8", glit="#FFFFFF", far=("#7FA6B8", "#5E8FA6", "#CDE9F7"), head=("#5FA052", "#2F6B3A"), sand=("#F7E2B8", "#E6C68F"),
                 dune=("#7DB85A", "#3F7A3A"), grass=["#7DB85A", "#4F8F3F", "#B5D46A", "#2F6B3A"], bloom=["#FFFFFF", "#FFD23F", "#FF7A6B", "#FF5A4F"])

# page number: (scene, seed, palette changes, mirror, a line describing the picture)
ART = {
    "001": (summit, 38, {}, False, "Painting of a woman standing on a hilltop at first light, with misty ranges below"),
    "002": (city, 14, {}, False, "Painting of a river city at blue hour, its windows lit and reflected in the water"),
    "003": (studio, 27, dict(wall=[(0, "#D9CCFF"), (.62, "#E7DEFF"), (1, "#E7DEFF")], floor=("#C9B8F5", "#B39DEB"), a=["#1F3FFF", "#C8F169", "#FFD7BF", "#14161A", "#FFFFFF"], light="#FFFFFF"),
            False, "Painting of arches, steps and spheres in lilac, cobalt and lime"),
    "004": (coast, 4, DAY_COAST, False, "Painting of a sunny bay with a lighthouse on the headland and flowers in the dunes"),
    "005": (summit, 41, dict(sky=[(0, "#27324F"), (.35, "#6B6F9A"), (.5, "#E2A08F"), (.6, "#F7D9B6"), (1, "#FBEBD6")], coat="#C8102E", hair="#CDAA72"), True,
            "Painting of a woman in a red coat on a hilltop, looking out over ranges at dawn"),
    "006": (stage, 35, {}, False, "Painting of a lone speaker on a dark stage under gold light, the audience in silhouette"),
    "007": (valley, 6, dict(sky=[(0, "#7FB2DC"), (.45, "#CFE5F2"), (.62, "#FBEBD0"), (1, "#FBEBD0")], sun=(.72, .55, "#FFF4D6"), mid=("#9FC48A", "#74A86A"), near=("#7FB36F", "#4F8A52"),
                           cloud=("#FFFFFF", "#C9D8E6", "#FFF1D6"), haze="#EEF0E0", tree=("#2F5A40", "#4E8A52", "#9FC48A")), False,
            "Painting of soft green hills on a calm morning, with a path winding toward a far town"),
    "008": (desk, 31, dict(wall=[(0, "#EFEAE0"), (1, "#E4DFD3")], accent="#FF4A1C", book=["#FF4A1C", "#0D0D0D", "#E4DFD3"], lamp="#0D0D0D"), False,
            "Painting of a desk under a window with an open laptop, a lamp and a stack of books"),
    "009": (studio, 29, dict(wall=[(0, "#EBDDBF"), (1, "#F0E6D2")], floor=("#E0CDA6", "#CDB588"), a=["#C23B1E", "#F2C14E", "#1F6F78", "#2B2118", "#FBF6EA"]), True,
            "Painting of arches, steps and spheres in tomato, mustard and teal"),
    "010": (alpine, 9, dict(sky=[(0, "#3C3A4E"), (.4, "#8B7F8E"), (.62, "#D9C2A8"), (1, "#EADCC8")], peak=("#6B6470", "#4E4855"), snow="#EFE6D8", ridge=("#4A4A48", "#35363A"),
                           forest=("#2A2B2A", "#1A1B1C"), lake="#3F3C48", haze="#D9C8B4", cloud=("#D9C2A8", "#6B6470", None), tree=("#141414", "#232320", "#3A382F"),
                           grass=["#4A473A", "#2F2D26", "#7A6E52"], bloom=["#CDAA72", "#EDE5D8"]), False, "Painting of a still mountain lake at dusk, framed by dark pines"),
    "011": (studio, 27, {}, False, "Painting of arches, steps and spheres in peach, rust and sage"),
    "012": (studio, 33, dict(wall=[(0, "#FFE9A8"), (1, "#FFF3CF")], floor=("#FFD98A", "#FFC766"), a=["#FF5A4F", "#3B6BFF", "#1B1B3A", "#FF9A76", "#FFFFFF"]), True,
            "Painting of arches, steps and spheres in coral, yellow and blue"),
    "013": (alpine, 8, {}, False, "Painting of snow peaks above a still lake, with pines on both sides"),
    "014": (desk, 32, dict(wall=[(0, "#E4EBDD"), (1, "#DCE5D2")], accent="#2F5A40", book=["#C9744F", "#2F5A40", "#E9C46A"]), True,
            "Painting of a calm desk by a window, with a laptop, a lamp and a plant"),
    "015": (city, 16, dict(sky=[(0, "#05060F"), (.5, "#141433"), (.66, "#3A2A4A"), (1, "#5A3A44")], far="#1E2046", near="#07080F", lit="#F2B544", river="#07081A", bank="#030408",
                          haze="#3A2F52", cloud=("#2A2A55", "#0C0D22", "#4A3550")), True, "Painting of a city at night, gold windows reflected in a dark river"),
    "016": (studio, 30, dict(wall=[(0, "#DDE6FF"), (1, "#EEF2FF")], floor=("#C9D6FF", "#B3C2F5"), a=["#C8F169", "#1F3FFF", "#FFD7BF", "#D9CCFF", "#FFFFFF"]), True,
            "Painting of arches, steps and spheres in lime, cobalt and peach"),
    "017": (desert, 24, {}, False, "Painting of a long road through red country toward flat-topped ranges"),
    "018": (studio, 28, dict(wall=[(0, "#E9E1D5"), (1, "#F3EEE6")], floor=("#DCCDB8", "#C9B79E"), a=["#8A6A3B", "#CDAA72", "#5F5449", "#26201B", "#FAF7F1"]), False,
            "Painting of arches, steps and spheres in bronze, ivory and espresso"),
    "019": (valley, 5, {}, True, "Painting of bright green country under a blue sky, a path leading toward a far town"),
    "020": (coast, 9, DAY_COAST, True, "Painting of a sunny tropical bay with flowers in the dunes"),
    "021": (coast, 6, dict(sky=[(0, "#8FA8C8"), (.4, "#D9C7CF"), (.56, "#F6D9C0"), (1, "#FBEBDD")], sun="#FFF6E6", sea="#5E86A6", glit="#FFF6E6", cloud=("#FBE3D2", "#A9A6C0", "#FFF1E2"),
                          far=("#9A94A8", "#7F7A92", "#F0D8C8"), head=("#6E8060", "#465A44"), dune=("#8A9A66", "#566A46")), False, "Painting of a pale dawn over a quiet bay"),
    "022": (city, 18, dict(sky=[(0, "#3A4A7A"), (.4, "#B98A8A"), (.6, "#F4C9A0"), (1, "#FBE6C8")], far="#8A7A9A", near="#3A3550", lit="#FFE3A0", river="#3A4670", bank="#2A2540",
                          haze="#E9C2A8", cloud=("#F6C9A8", "#7A6A94", "#FFE6C4")), False, "Painting of a city skyline at sunrise, reflected in the river"),
    "023": (alpine, 12, dict(sky=[(0, "#7C9CC4"), (.45, "#C9D6E4"), (.7, "#F3E9DD"), (1, "#F6EEE2")], haze="#E9E4DC"), True, "Painting of mountains and a still lake in soft morning light"),
    "024": (night, 17, {}, False, "Painting of a starry night with a low moon, and a single lit cabin among the pines"),
    "025": (desk, 34, dict(wall=[(0, "#E6E8F2"), (1, "#DDE0EE")], accent="#1F3FFF", book=["#1F3FFF", "#C8F169", "#FFD7BF"], plant="#3F8A5A"), False,
            "Painting of a tidy desk by a window, with a laptop showing a page being edited"),
    "026": (fields, 22, dict(sky=[(0, "#8E8FA6"), (.4, "#D8C9BE"), (.58, "#F3E3C8"), (1, "#F3E3C8")], rows=("#C9A86A", "#8A6A3B", "#B79A5E"), roof="#5F5449", haze="#EFE0C8",
                            cloud=("#F6E6D2", "#A9A0AE", "#FFEFD6"), far=("#B4AA94", "#9E947E")), False, "Painting of golden rows running to the horizon, with a farmhouse and cypress trees"),
    "027": (lodge, 11, {}, False, "Painting of a lit lodge on a hillside at golden hour, with mist in the valleys"),
    "028": (lodge, 13, dict(sky=[(0, "#5E8FC2"), (.4, "#BFD6E8"), (.6, "#EEF2F2"), (1, "#F4F1EA")], sun=(.7, .56, "#FFFFFF"), haze="#E4EEF2", r1=("#9DB4C2", "#8AA4B4"),
                           r2=("#6E96A0", "#5A8490"), r3=("#4A7A76", "#3A6662"), near=("#3F6E5C", "#234A3E"), cloud=("#FFFFFF", "#C5D5E4", None)), True,
            "Painting of calm green hills in morning mist, with a house on the near rise"),
    "library": (lodge, 44, dict(sky=[(0, "#0A1612"), (.4, "#132620"), (.6, "#2E4A3A"), (1, "#5E6E4A")], sun=(.72, .6, "#C5A880"), haze="#3E5646", r1=("#274236", "#213A2F"),
                                r2=("#1B3328", "#162B22"), r3=("#12251C", "#0E1E17"), near=("#0C1B14", "#060E0A"), cloud=("#3E5646", "#132620", "#C5A880"),
                                tree=("#06100B", "#0C1B14", "#1E3A2A"), grass=["#12251C", "#1E3A2A", "#C5A880"], bloom=["#C5A880", "#EAE7E1"]), False,
                "Painting of forest hills at dusk in deep green and gold"),
}


def save(img, folder, name="hero"):
    """Four sizes, each cut down from the master and lightly sharpened, so a phone, a laptop and a large screen each get a crisp file."""
    folder.mkdir(parents=True, exist_ok=True)
    for w, q in ((2560, 80), (1920, 84), (1280, 82), (960, 80)):
        out = img if w == img.shape[1] else cv2.resize(img, (w, int(img.shape[0] * w / img.shape[1])), interpolation=cv2.INTER_AREA)
        out = np.clip(out + (out - cv2.GaussianBlur(out, (0, 0), 0.9)) * 0.35, 0, 1)
        cv2.imwrite(str(folder / f"{name}-{w}.webp"), cv2.cvtColor((out * 255).astype(np.uint8), cv2.COLOR_RGB2BGR), [cv2.IMWRITE_WEBP_QUALITY, q])


def main():
    root = pathlib.Path(__file__).parent.parent
    dirs = {d.name[:3]: d for d in root.iterdir() if d.is_dir() and d.name[:3].isdigit()}
    want = sys.argv[1:]
    for key, (fn, seed, pal, mirror, _) in ART.items():
        if want and key not in want:
            continue
        img = fn(seed, pal)
        if mirror:
            img = img[:, ::-1]
        save(img, root / "images" if key == "library" else dirs[key] / "site" / "images")
        print("painted", key, fn.__name__, flush=True)


if __name__ == "__main__":
    main()
