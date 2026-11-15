"""Shared helpers and the base stylesheet every sample starts from."""
import re
from html import escape

import art

REG, CSS = {}, {}
CTX = {"person": "", "faces": []}  # set per page by the build: whose portrait to draw, whose faces to stack


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


def eyebrow(t):
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


def sec(name, d, inner, cls=""):
    tone = d.get("tone", "")
    idattr = f' id="{d["id"]}"' if d.get("id") else ""
    note = f"<!-- {e(d['_'])} -->\n" if d.get("_") else ""
    return f'{note}<section class="sec {name} {tone} {cls}"{idattr}><div class="wrap">{inner}</div></section>'


def crowd(text, n=4, i=4):
    """Proof beside the button: a stack of client faces and 1 line of evidence."""
    if not text:
        return ""
    avs = "".join(art.avatar(x) for x in CTX.get("faces", [])[:n])
    stack = f'<span class="avs" aria-hidden="true">{avs}</span>' if avs else ""
    return f'<div class="crowd" data-in style="--i:{i}">{stack}<p>{h(text)}</p></div>'


def reassure(text, ic="shield"):
    """The line that answers the last worry, placed right at the button."""
    return f'<p class="reassure">{art.icon(ic)}<span>{h(text)}</span></p>' if text else ""


def _brief(raw):
    return re.sub(r"^(Photo|Image|Video) brief:\s*", "", raw)


def vis(v):
    """Visuals. Samples ship no stock photos: each frame is an illustration, and the brief for the real shot sits in an HTML comment beside it."""
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
    if k == "person":
        seen = CTX.setdefault("drawn", {})
        seen[who] = seen.get(who, 0) + 1
        pose = 0 if v.get("ar") == "1/1" else (seen[who] - 1) % 2
        return (f'{note}<div class="ph person" style="--ar:{ar}" role="img" aria-label="Illustrated portrait standing in for a photo of {e(who)}">'
                f'{art.portrait(who, pose=pose)}</div>')
    if k == "scene":
        ar = v.get("ar", "1/1")
        return (f'{note}<div class="ph scene" style="--ar:{ar}" role="img" aria-label="Illustration standing in for a photo: {e(_brief(raw))}">'
                f'{art.scene(raw, ar)}</div>')
    if k == "video":
        pic = art.scene(raw) if art.kind_of(raw) in ("stage", "mic") or "lesson" in raw else art.portrait(who, wide=True)
        cap = f'<span class="cap">{e(v["cap"])}</span>' if v.get("cap") else ""
        return (f'{note}<div class="ph scene vid" style="--ar:16/9" role="img" aria-label="Video frame: {e(_brief(raw))}">'
                f'{pic}<i class="play" aria-hidden="true"></i>{cap}</div>')
    if k == "book":
        return (f'<div class="bookwrap"><div class="book" role="img" aria-label="Book cover: {e(v["title"])}">'
                f'<small>{e(v.get("kicker", ""))}</small><strong>{h(v["title"])}</strong><em>{e(v.get("author", ""))}</em></div></div>')
    if k == "cover":
        return (f'<div class="bookwrap"><div class="book guide" role="img" aria-label="Guide cover: {e(v["title"])}">'
                f'<small>{e(v.get("kicker", "Free guide"))}</small><strong>{h(v["title"])}</strong><em>{e(v.get("author", ""))}</em></div></div>')
    if k == "cal":
        days = "".join(
            f'<span class="{"on" if n in v.get("open", []) else ""}{" pick" if n == v.get("pick") else ""}">{n}</span>'
            for n in range(1, 29))
        slots = "".join(f'<span class="slot{" pick" if i == 1 else ""}">{e(s)}</span>' for i, s in enumerate(v.get("slots", [])))
        return (f'<div class="card cal formcard" role="img" aria-label="Booking calendar mock-up"><p class="cal-m">{e(v.get("month", "March"))}</p>'
                f'<div class="cal-g">{days}</div><p class="cal-m">{e(v.get("day", "Thursday 12"))}</p><div class="cal-s">{slots}</div>'
                f'<p class="fine">{lab}</p></div>')
    if k == "email":
        lines = "".join(f"<p>{h(x)}</p>" for x in v["lines"])
        return (f'<div class="card mk mk-email" role="img" aria-label="Preview of a sample email"><div class="mk-top">{art.avatar(who)}'
                f'<div><b>{e(v["sender"])}</b><span>{e(v["when"])}</span></div><i>{e(v.get("tag", "Inbox"))}</i></div>'
                f'<h3>{h(v["subject"])}</h3>{lines}<div class="mk-fade" aria-hidden="true"></div></div>')
    if k == "lesson":
        items = "".join(f'<li class="{c}"><i aria-hidden="true"></i><span>{e(t)}</span><small>{e(m)}</small></li>' for c, t, m in v["items"])
        return (f'{note}<div class="card mk mk-lesson" role="img" aria-label="Preview of the course player">'
                f'<div class="ph scene vid" style="--ar:16/9">{art.scene("laptop lesson")}<i class="play" aria-hidden="true"></i>'
                f'<span class="cap">{e(v["cap"])}</span></div><ul>{items}</ul></div>')
    return ""


BASE_CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
body{font:400 1.0625rem/1.6 var(--fb);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;overflow-x:clip}
a{color:inherit}
h1,h2,h3,h4{font-family:var(--fd);font-weight:var(--hw);letter-spacing:var(--hls);line-height:var(--hlh);text-transform:var(--htt);text-wrap:balance}
h1{font-size:clamp(2.5rem,calc(6.3vw*var(--hs)),calc(5rem*var(--hs)))}
h2{font-size:clamp(1.85rem,calc(3.9vw*var(--hs)),calc(3.05rem*var(--hs)))}
h3{font-size:1.28rem;line-height:1.2}
p{text-wrap:pretty}
p+p{margin-top:1em}
.wrap{max-width:1160px;margin-inline:auto;padding-inline:clamp(20px,5vw,48px)}
.sec{padding-block:clamp(64px,9vw,120px)}
.alt{background:var(--bg2)}
.dark{background:var(--dark);color:var(--dark-ink);--ink:var(--dark-ink);--ink2:color-mix(in srgb,var(--dark-ink) 76%,var(--dark));--line:color-mix(in srgb,var(--dark-ink) 22%,var(--dark));--card:color-mix(in srgb,var(--dark-ink) 7%,var(--dark));--accent-t:var(--dark-accent)}
.center{text-align:center}.center .lead,.center p{margin-inline:auto}
.lead{font-size:clamp(1.1rem,1.55vw,1.28rem);color:var(--ink2);max-width:58ch;line-height:1.55}
.eyebrow{font-family:var(--fa);font-size:.8rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent-t);margin-bottom:1rem}
.sh{margin-bottom:clamp(32px,4.5vw,56px);max-width:780px}.sh.center{margin-inline:auto}.sh .lead{margin-top:1.1rem}
.fine{font-size:.84rem;color:var(--ink2)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5em;min-height:50px;padding:.82em 1.6em;border-radius:var(--rb);background:var(--accent);color:var(--accent-ink);border:var(--bw) solid var(--accent);font-weight:600;font-size:1rem;line-height:1.2;text-decoration:none;transition:transform .15s ease}
.btn:hover{transform:translateY(-2px)}
.btn.ghost{background:transparent;color:var(--ink);border:max(1px,var(--bw)) solid currentColor;box-shadow:none}
.acts{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:2rem}.center .acts{justify-content:center}
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
.ph.vid{border-radius:var(--r)}
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
/* Sections lift into place as they scroll in. They never fade, so nothing sits half-visible at the edge of the screen */
@keyframes lift{from{transform:translateY(28px)}}
@supports(animation-timeline:view()){.sec>.wrap>*{animation:lift linear both;animation-timeline:view();animation-range:entry 0% entry 40%}}
}
@media print{.libbar{display:none}.sec{padding-block:28px}}
"""
