"""Shared helpers and the base stylesheet every sample starts from."""
import re
from html import escape

import art

REG, CSS = {}, {}
CTX = {"person": "", "faces": [], "art": None}  # set per page by the build: the page's painting and whose initials to stack
SRCSET = 'src="images/hero-960.webp" srcset="images/hero-960.webp 960w, images/hero-1280.webp 1280w, images/hero-1920.webp 1920w, images/hero-2560.webp 2560w" sizes="100vw" width="1920" height="1200"'


def S(name, css=""):
    """Register a section renderer with the CSS it needs. Only CSS for sections a page uses is shipped."""
    def deco(fn):
        REG[name] = fn
        CSS[name] = css
        return fn
    return deco


def e(s):
    return escape(str(s), quote=True)


def h(s):
    """Headline markup: *word* becomes <em>, | becomes a line break."""
    s = e(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s.replace("|", "<br>")


def eyebrow(t, who=False):
    """The small line above a headline. With who=True it carries the owner's face, so a real person is on the first screen."""
    if t and who and CTX.get("brand"):
        return f'<p class="eyebrow who">{face(CTX["brand"]["person"])}<span>{e(t)}</span></p>'
    return f'<p class="eyebrow">{e(t)}</p>' if t else ""


def btn(c, cls=""):
    if not c:
        return ""
    k = f"btn {cls}".strip()
    return f'<a class="{k}" href="{e(c[1])}">{e(c[0])}</a>'


def acts(d, i=3):
    a = btn(d.get("cta")) + btn(d.get("cta2"), "ghost")
    return f'<div class="acts" data-in style="--i:{i}">{a}</div>' if a else ""


def sh(d, center=False):
    if not d.get("h"):
        return ""
    lead = f'<p class="lead">{h(d["lead"])}</p>' if d.get("lead") else ""
    c = " center" if center or d.get("center") else ""
    return f'<header class="sh{c}">{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2>{lead}</header>'


def ul(items, cls="ticks"):
    if not items:
        return ""
    return f'<ul class="{cls}">' + "".join(f"<li>{h(i)}</li>" for i in items) + "</ul>"


def paras(ps):
    return "".join(f"<p>{h(p)}</p>" for p in (ps or []))


def sec(name, d, inner, cls="", pre=""):
    tone = d.get("tone", "")
    idattr = f' id="{d["id"]}"' if d.get("id") else ""
    note = f"<!-- {e(d['_'])} -->\n" if d.get("_") else ""
    return f'{note}<section class="sec {name} {tone} {cls}"{idattr}>{pre}<div class="wrap">{inner}</div></section>'


def backdrop(eager=False):
    """The page's painting as a full-bleed background. The first one on a page loads first; the rest wait until they are near the screen."""
    a = CTX["art"]
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    alt = e(a["alt"]) if eager else ""
    return f'<picture class="art"><img {SRCSET} alt="{alt}" {load} decoding="async"></picture>'


def detail(ar="4/5", whole=False):
    """A close crop of the page's painting, used wherever a second picture is needed. Each call moves to a different part of the picture."""
    a = CTX["art"]
    if whole:
        pos, zoom = "50% 72%", 1
    else:
        i = CTX["crops"] = CTX.get("crops", 0) + 1
        pos, zoom = a["crops"][(i - 1) % len(a["crops"])]
    return (f'<div class="ph art" style="--ar:{ar};--pos:{pos};--zoom:{zoom}"><img {SRCSET} alt="" loading="lazy" decoding="async"></div>')


SIZES = {"you": (900, 1125), "guest": (900, 1125), "me": (240, 240), "face": (200, 200), "scene": (1200, 900), "video": (1280, 720),
         "mock": (1600, 1000), "phone": (780, 1560), "slide": (1600, 900), "post": (1080, 1350)}


def slot(kind, key, brief="", who=""):
    """Every photograph on a site is a named file in its images folder, so the owner swaps a photo by saving their own under the
    same name. This hands out the file names and remembers where each is used, for the launch checklist."""
    book = CTX.setdefault("photos", {})
    if (kind, key) not in book:
        n = sum(1 for kk, _ in book if kk == kind) + 1
        w, h = SIZES[kind]
        rec = dict(file="you-headshot.jpg" if kind == "me" else f"{kind}-{n}.jpg", kind=kind, w=w, h=h, brief=brief, who=who, where=[])
        if kind in ("scene", "video"):
            crops = CTX["art"]["cropn"]
            rec["crop"] = list(crops[(n - 1) % len(crops)])
        book[(kind, key)] = rec
    rec = book[(kind, key)]
    rec["brief"] = rec["brief"] or brief
    if CTX.get("file", "index.html") not in rec["where"]:
        rec["where"].append(CTX.get("file", "index.html"))
    return rec


def photo(kind, key, brief="", ar="4/5", who="", alt="", cls=""):
    p = slot(kind, key, brief, who)
    return (f'<div class="{("ph photo " + cls).strip()}" style="--ar:{ar}"><img src="images/{p["file"]}" width="{p["w"]}" height="{p["h"]}" alt="{e(alt)}" '
            f'loading="lazy" decoding="async"></div>')


def face(name):
    """A small round photo. The owner's own face is 1 file used everywhere; every other person gets a file of their own."""
    p = slot("me", "me", "Your headshot, cropped square. It appears small wherever your name does") if name == CTX.get("person") else slot("face", name, who=name)
    return f'<span class="av"><img src="images/{p["file"]}" width="{p["w"]}" height="{p["h"]}" alt="" loading="lazy" decoding="async"></span>'


def host(line=""):
    """The person behind the page, shown where a visitor decides: their face, their name and what they do."""
    b = CTX.get("brand")
    if not b:
        return ""
    return f'<p class="host">{face(b["person"])}<span><b>{e(b["person"])}</b>{e(line or b["role"])}</span></p>'


def connect(what):
    """A link that can only be finished with the owner's own account: a checkout, a profile, a podcast app.
    It points at example.com so it never breaks, and every one is listed in the site's launch checklist."""
    return "https://example.com/connect/" + re.sub(r"[^a-z0-9]+", "-", what.lower()).strip("-")


def crowd(text, n=4, i=4):
    """Proof beside the button: a stack of client faces and 1 line of evidence."""
    if not text:
        return ""
    avs = "".join(face(x) for x in CTX.get("faces", [])[:n])
    stack = f'<span class="avs" aria-hidden="true">{avs}</span>' if avs else ""
    return f'<div class="crowd" data-in style="--i:{i}">{stack}<p>{h(text)}</p></div>'


def reassure(text, ic="shield"):
    """The line that answers the last worry, placed right at the button."""
    return f'<p class="reassure">{art.icon(ic)}<span>{h(text)}</span></p>' if text else ""


def _brief(raw):
    return re.sub(r"^(Photo|Image|Video) brief:\s*", "", raw)


def vis(v, main=False):
    """Pictures. A person, a place or a video still is a photo file in the images folder, with the brief for the real photograph
    in a comment beside it. Small product and map thumbnails stay as line illustrations."""
    if not v:
        return ""
    k = v.get("kind", "person")
    ar = v.get("ar", "4/5")
    raw = v.get("label", "")
    lab = e(raw)
    note = f"<!-- {lab} -->" if raw else ""
    if raw and k in ("person", "scene", "video", "lesson") and "briefs" in CTX:
        CTX["briefs"].append(_brief(raw))
    who = v.get("who") or CTX.get("person") or "Guest"
    said = re.split(r"[.:]", _brief(raw))[0].strip()
    if k == "person":
        if v.get("who") and v["who"] != CTX.get("person"):
            return note + photo("guest", v["who"], _brief(raw), ar, who=v["who"], alt=v["who"])
        return note + photo("you", "main" if main else raw, _brief(raw), ar, alt=CTX.get("person", ""))
    if k == "scene":
        return note + photo("scene", raw, _brief(raw), ar, alt=said[:1].upper() + said[1:], cls="wide")
    if k == "sketch":
        return (f'{note}<div class="ph scene" style="--ar:{ar}" role="img" aria-label="Illustration: {e(_brief(raw))}">{art.scene(raw, ar)}</div>')
    if k == "video":
        cap = f'<span class="cap">{e(v["cap"])}</span>' if v.get("cap") else ""
        # A video slot plays a real file as soon as there is one: save video-1.mp4 in the site's media folder, beside images, and rebuild.
        # Until then the slot shows its still with a play mark.
        p = slot("video", raw, _brief(raw))
        clip = CTX.get("site") and CTX["site"] / "media" / (p["file"][:-4] + ".mp4")
        if clip and clip.exists():
            return (f'{note}<div class="ph photo wide vid has-clip" style="--ar:16/9"><video controls preload="none" playsinline poster="images/{p["file"]}" '
                    f'width="{p["w"]}" height="{p["h"]}" aria-label="{e(said)}"><source src="media/{clip.name}" type="video/mp4"></video></div>')
        return note + photo("video", raw, _brief(raw), "16/9", cls="wide vid").replace("</div>", f'<i class="play" aria-hidden="true"></i>{cap}</div>')
    if k == "book":
        return (f'<div class="bookwrap"><div class="book" role="img" aria-label="Book cover: {e(v["title"])}">'
                f'<small>{e(v.get("kicker", ""))}</small><strong>{h(v["title"])}</strong><em>{e(v.get("author", ""))}</em></div></div>')
    if k == "cover":
        return (f'<div class="bookwrap"><div class="book guide" role="img" aria-label="Guide cover: {e(v["title"])}">'
                f'<small>{e(v.get("kicker", "Free guide"))}</small><strong>{h(v["title"])}</strong><em>{e(v.get("author", ""))}</em></div></div>')
    if k == "email":
        lines = "".join(f"<p>{h(x)}</p>" for x in v["lines"])
        return (f'<div class="card mk mk-email" role="img" aria-label="Preview of a sample email"><div class="mk-top">{face(who)}'
                f'<div><b>{e(v["sender"])}</b><span>{e(v["when"])}</span></div><i>{e(v.get("tag", "Inbox"))}</i></div>'
                f'<h3>{h(v["subject"])}</h3>{lines}<div class="mk-fade" aria-hidden="true"></div></div>')
    if k == "lesson":
        items = "".join(f'<li class="{c}"><i aria-hidden="true"></i><span>{e(t)}</span><small>{e(m)}</small></li>' for c, t, m in v["items"])
        poster = photo("video", raw, _brief(raw), "16/9", cls="wide vid").replace("</div>", f'<i class="play" aria-hidden="true"></i><span class="cap">{e(v["cap"])}</span></div>')
        return f'{note}<div class="card mk mk-lesson">{poster}<ul>{items}</ul></div>'
    return ""


BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
body{font:400 1.0625rem/1.6 var(--fb);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;font-optical-sizing:auto;font-kerning:normal;overflow-x:clip}
p,li{text-wrap:pretty}
a{color:inherit}
h1,h2,h3,h4{font-family:var(--fd);font-weight:var(--hw);letter-spacing:var(--hls);line-height:var(--hlh);text-transform:var(--htt);text-wrap:balance}
h1{font-size:clamp(2.15rem,calc(4.5vw*var(--hs)),calc(3.9rem*var(--hs)))}
h2{font-size:clamp(1.75rem,calc(3.3vw*var(--hs)),calc(2.8rem*var(--hs)))}
h3{font-size:1.28rem;line-height:1.2}
p{text-wrap:pretty}
p+p{margin-top:1em}
.wrap{max-width:1160px;margin-inline:auto;padding-inline:clamp(20px,5vw,48px)}
.sec{padding-block:clamp(60px,8vw,112px)}
.alt{background:var(--bg2)}
.dark{background:var(--dark);color:var(--dark-ink);--ink:var(--dark-ink);--ink2:color-mix(in srgb,var(--dark-ink) 76%,var(--dark));--line:color-mix(in srgb,var(--dark-ink) 22%,var(--dark));--card:color-mix(in srgb,var(--dark-ink) 7%,var(--dark));--accent-t:var(--dark-accent)}
.center{text-align:center}.center .lead,.center p{margin-inline:auto}
.lead{font-size:clamp(1.12rem,1.6vw,1.32rem);color:var(--ink2);max-width:56ch;line-height:1.52;text-wrap:pretty}
.eyebrow{font-family:var(--fa);font-size:.78rem;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-t);margin-bottom:1rem}
.sh{margin-bottom:clamp(32px,4.5vw,56px);max-width:780px}.sh.center{margin-inline:auto}.sh .lead{margin-top:1.1rem}
.fine{font-size:.84rem;color:var(--ink2)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;min-height:50px;padding:.82em 1.6em;border-radius:var(--rb);background:var(--accent);color:var(--accent-ink);border:var(--bw) solid var(--accent);font-weight:600;font-size:1rem;line-height:1.2;text-decoration:none;transition:transform .15s ease}
.btn:hover{transform:translateY(-2px)}
.btn.ghost{background:transparent;color:var(--ink);border:max(1px,var(--bw)) solid currentColor;box-shadow:none}
.acts{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.7rem}.center .acts{justify-content:center}
.link{font-weight:600;text-underline-offset:.25em}
.card{background:var(--card);border:var(--bw) solid var(--line);border-radius:var(--r);padding:clamp(22px,3vw,34px);box-shadow:var(--shadow)}
.grid{display:grid;gap:clamp(16px,2.4vw,28px);grid-template-columns:repeat(var(--cols,3),minmax(0,1fr))}
@media(max-width:900px){.grid{grid-template-columns:repeat(min(var(--cols,3),2),minmax(0,1fr))}}
@media(max-width:600px){.grid{grid-template-columns:1fr}}
ul{list-style:none}
.ticks li{position:relative;padding-left:1.7em;margin-top:.6em}
.ticks li::before{content:"";position:absolute;left:0;top:.42em;width:.95em;height:.5em;border-left:2.5px solid var(--accent-t);border-bottom:2.5px solid var(--accent-t);rotate:-45deg}
.proof{margin-top:1.6rem;font-size:.92rem;color:var(--ink2)}.proof b{color:var(--ink)}
.ph{position:relative;aspect-ratio:var(--ar,4/5);border-radius:var(--phr);background:radial-gradient(90% 70% at 30% 18%,var(--ph1),var(--ph2));overflow:hidden;isolation:isolate}
.ph>svg{position:absolute;inset:0;width:100%;height:100%}
.ph.photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 16%}.ph.photo.wide img{object-position:50% 50%}
.ph.art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:var(--pos,50% 70%);transform:scale(var(--zoom,1));transform-origin:var(--pos,50% 70%)}
picture.art{position:absolute;inset:0;z-index:-3;display:block;overflow:hidden}picture.art img{width:100%;height:100%;object-fit:cover;object-position:var(--apos,50% 100%);display:block}
.ph.vid{border-radius:var(--r)}.ph.vid video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;background:#000}
.ph.vid .play{position:absolute;left:50%;top:50%;translate:-50% -50%;width:74px;height:74px;border-radius:50%;background:var(--card);z-index:2}
.ph.vid .play::after{content:"";position:absolute;left:54%;top:50%;translate:-50% -50%;border-left:20px solid var(--ink);border-block:13px solid transparent}
.bookwrap{display:grid;place-items:center;padding:clamp(16px,4vw,48px);background:var(--bg2);border-radius:var(--r)}
.dark .bookwrap{background:color-mix(in srgb,var(--dark-ink) 8%,var(--dark))}
.book{width:min(300px,78%);aspect-ratio:2/3;background:var(--accent);color:var(--accent-ink);padding:10% 9%;display:flex;flex-direction:column;justify-content:space-between;border-radius:3px 8px 8px 3px;box-shadow:inset 9px 0 0 rgba(0,0,0,.16),18px 22px 40px rgba(0,0,0,.28);rotate:-3deg}
.book small{font:600 .68rem/1.3 var(--fb);letter-spacing:.16em;text-transform:uppercase}
.book strong{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.5rem,3.2vw,2.3rem);line-height:1.02;letter-spacing:var(--hls);text-transform:var(--htt)}
.book strong em{font-style:italic;color:inherit;background:none}.book>em{font:500 .82rem/1.3 var(--fb);font-style:normal}
.book.guide{aspect-ratio:3/4;background:var(--card);color:var(--ink);border:var(--bw) solid var(--line);box-shadow:10px 10px 0 var(--accent),22px 26px 40px rgba(0,0,0,.14)}
.field{margin-top:1rem}.field label{display:block;font-size:.86rem;font-weight:600;margin-bottom:.35rem}
.field input,.field select,.field textarea{width:100%;min-height:50px;padding:.72rem .95rem;border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),12px);background:var(--bg);color:var(--ink);font:inherit}
.field textarea{min-height:120px;resize:vertical}
.formcard .btn{width:100%;margin-top:1.2rem}.formcard .fine{margin-top:.8rem;text-align:center}
.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;z-index:99;background:var(--card);color:var(--ink);padding:.6rem 1rem;border-radius:6px}
:focus-visible{outline:3px solid var(--accent-t);outline-offset:3px}
.libbar{background:#132620;color:#EAE7E1;font:500 .78rem/1.35 system-ui,-apple-system,'Segoe UI',sans-serif;padding:.6rem clamp(20px,5vw,48px);display:flex;gap:.4rem 1.2rem;justify-content:space-between;flex-wrap:wrap}
.libbar a{color:#C5A880;text-underline-offset:.2em}
.hd{display:flex;align-items:center;justify-content:space-between;gap:1.5rem;max-width:1160px;margin:auto;padding:1.15rem clamp(20px,5vw,48px)}
.logo{font-family:var(--fd);font-weight:var(--hw);font-size:1.4rem;letter-spacing:var(--hls);text-transform:var(--htt);text-decoration:none;line-height:1.1}
.hd nav ul{display:flex;gap:1.7rem;font-size:.95rem}.hd nav a{text-decoration:none}.hd nav a:hover{text-decoration:underline;text-underline-offset:.3em}
.hd .btn{min-height:44px;padding:.55em 1.15em;font-size:.92rem;box-shadow:none}
@media(max-width:860px){.hd nav{display:none}}
@media(max-width:520px){.logo{font-size:1.15rem}.hd .btn{font-size:.82rem;padding:.5em .95em;white-space:nowrap}}
.ft{background:var(--dark);color:var(--dark-ink);--ink:var(--dark-ink);--ink2:color-mix(in srgb,var(--dark-ink) 74%,var(--dark));padding:clamp(48px,6vw,80px) 0 28px;font-size:.95rem}
.ft-g{display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:2.4rem}
@media(max-width:760px){.ft-g{grid-template-columns:1fr}}
.ft .logo{display:inline-block;margin-bottom:.8rem}.ft h2{font:600 .78rem/1.3 var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--ink2);margin-bottom:.9rem}
.ft li{margin-top:.5rem}.ft a{text-underline-offset:.25em}.ft p{color:var(--ink2);max-width:42ch}
.ft-s{margin-top:2.6rem;padding-top:1.3rem;border-top:1px solid color-mix(in srgb,var(--dark-ink) 22%,var(--dark));font-size:.8rem;color:var(--ink2)}
.ft-s p{max-width:none}.ft-s p+p{margin-top:.5em}
@media(prefers-reduced-motion:no-preference){
[data-in]{animation:rise .7s cubic-bezier(.2,.7,.2,1) both;animation-delay:calc(var(--i,0)*90ms)}
@keyframes rise{from{opacity:0;transform:translateY(16px)}}
/* The headline slides but never starts hidden, so the largest element paints straight away */
h1[data-in]{animation-name:slide}
@keyframes slide{from{transform:translateY(16px)}}
/* Sections below the first screen reveal as they scroll in: see src/motion.py */
}
@media print{.libbar{display:none}.sec{padding-block:28px}}
"""
