"""Section components. Each takes a dict of content and returns HTML. Mix and reorder them to make a page."""
import re

import art
import kit
from kit import S, e, h, eyebrow, btn, acts, sh, ul, paras, sec, vis, crowd, reassure, backdrop, detail

CARDS = ("book", "cover", "lesson", "email")


def tone():
    return "bleed t-" + kit.CTX["art"]["tone"]


def brief(v):
    """The hero is a painting. The brief for the photograph that could replace it is kept as a comment and listed in the notes."""
    if not v or not v.get("label") or v.get("kind", "person") in CARDS:
        return ""
    if "briefs" in kit.CTX:
        kit.CTX["briefs"].append(kit._brief(v["label"]))
    return f'<!-- {e(v["label"])} -->'

AUTO = {"email": "email", "tel": "tel"}


def field_name(label, typ):
    low = label.lower()
    if typ == "email":
        return "email"
    if typ == "tel":
        return "phone"
    if typ == "area":
        return "message"
    if "name" in low and "business" not in low and "agency" not in low:
        return "name"
    return re.sub(r"[^a-z0-9]+", "-", low).strip("-")[:40]


def form_open(name, cls=""):
    """Every form posts for real. On Netlify it is collected with no extra code once form detection is on; on any other host,
    point the action at your email or form tool. The hidden field is a spam trap that people never see."""
    klass = f' class="{cls}"' if cls else ""
    return (f'<form{klass} name="{name}" method="post" action="thank-you.html" data-netlify="true" data-netlify-honeypot="website">'
            f'<input type="hidden" name="form-name" value="{name}"><p class="hp"><label>Leave this empty <input name="website" tabindex="-1" autocomplete="off"></label></p>')


def form(f, cls="card formcard"):
    fields = ""
    for i, (label, typ, hint) in enumerate(f.get("fields", [])):
        fid = "f-" + re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-") + f"-{i}"
        nm = field_name(label, typ)
        req = "" if "optional" in label.lower() else " required"
        if typ == "area":
            ctl = f'<textarea id="{fid}" name="{nm}" placeholder="{e(hint)}"{req}></textarea>'
        elif typ == "select":
            ctl = f'<select id="{fid}" name="{nm}"{req}>' + "".join(f"<option>{e(o)}</option>" for o in hint) + "</select>"
        else:
            auto = AUTO.get(typ) or ("name" if nm == "name" else "on")
            ctl = f'<input id="{fid}" name="{nm}" type="{typ}" placeholder="{e(hint)}" autocomplete="{auto}" enterkeyhint="next"{req}>'
        fields += f'<div class="field"><label for="{fid}">{e(label)}</label>{ctl}</div>'
    title = f'<h2 class="ft-t">{h(f["title"])}</h2>' if f.get("title") else ""
    text = f'<p class="fine" style="text-align:left;margin-top:.4rem">{h(f["text"])}</p>' if f.get("text") else ""
    note = f'<p class="fine">{art.icon("lock")}<span>{h(f["note"])}</span></p>' if f.get("note") else ""
    proof = crowd(f["proof"], 3).replace(" data-in", "") if f.get("proof") else ""
    cals = ""
    if f.get("cals"):
        cals = '<p class="cals"><span>Add to calendar:</span>' + "".join(f'<a href="{e(hr)}"{dl}>{e(c)}</a>' for c, hr, dl in f["cals"]) + "</p>"
    return (f'{form_open(f.get("name", "enquiry"), cls)}{title}{text}{fields}'
            f'<button class="btn" type="submit">{e(f.get("button", "Send"))}</button>{note}{proof}{cals}</form>')


def under(d):
    """What sits directly under a hero's buttons: the reassurance line, then the proof."""
    return reassure(d.get("reassure")) + crowd(d.get("proof"))


# ---------- HEROES ----------

@S("hero_split", """
.hs-g{display:grid;grid-template-columns:1.08fr .92fr;gap:clamp(28px,5vw,76px);align-items:center}
.hero{padding-block:clamp(36px,5vw,72px) clamp(56px,8vw,104px)}
.hero .lead{margin-top:1.1rem}.hero .ticks{margin-top:1.2rem}
.hs-v{position:relative;min-height:clamp(240px,34vw,440px)}.hs-v.has-card{min-height:0}
.float{position:absolute;left:6%;bottom:12%;max-width:230px;padding:16px 18px;font-size:.9rem;line-height:1.4;z-index:3}.has-card .float{left:-8%;bottom:-6%}
.float b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:1.9rem;line-height:1;letter-spacing:var(--hls);color:var(--accent-t)}
@media(max-width:860px){.hs-g{grid-template-columns:1fr}.hs-v{min-height:0;display:flex;flex-wrap:wrap;gap:.8rem;align-items:flex-start}
.hs-v .float,.hs-v .float.f2{position:static;max-width:none;flex:1 1 150px;animation:none}.hs-v.has-card{display:block;max-width:430px}.has-card .float{display:none}}
""")
def hero_split(d, P):
    fl, f2 = d.get("float"), d.get("float2")
    v = d.get("visual") or {}
    flo = f'<div class="card float"><b>{e(fl[0])}</b>{e(fl[1])}</div>' if fl else ""
    flo += f'<div class="card float f2">{art.icon(f2[0])}<div><b>{e(f2[1])}</b><span>{e(f2[2])}</span></div></div>' if f2 else ""
    card = vis(v, main=True) if v else ""
    cls = "" if not card else " has-card" if v.get("kind") in CARDS else " has-pic"
    person = bool(v) and v.get("kind", "person") == "person"
    inner = (f'<div class="hs-g"><div class="hs-c">{eyebrow(d.get("eyebrow"), who=not person)}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{ul(d.get("bullets"))}{acts(d)}{under(d)}</div>'
             f'<div class="hs-v{cls}" data-in style="--i:2">{card}{flo}</div></div>')
    return sec("hero hsplit " + tone(), d, inner, pre=backdrop(True))


@S("hero_center", """
.hero{padding-block:clamp(36px,5vw,72px) clamp(56px,8vw,104px)}
.hcenter .wrap{text-align:center}.hcenter h1{max-width:17ch;margin-inline:auto}.hcenter .lead{margin:1.4rem auto 0}
.hcenter .acts{justify-content:center}.hc-u{margin-top:clamp(26px,3.4vw,44px);max-width:680px;margin-inline:auto}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.6rem}
.chips li{border:max(1px,var(--bw)) solid var(--line);border-radius:999px;padding:.4em 1em;font-size:.86rem;font-weight:500;background:var(--card)}
""")
def hero_center(d, P):
    chips = ('<ul class="chips">' + "".join(f"<li>{e(c)}</li>" for c in d["chips"]) + "</ul>") if d.get("chips") else ""
    below = f'<div class="hc-u" data-in style="--i:4">{vis(d["under"])}</div>' if d.get("under") else ""
    inner = (f'{eyebrow(d.get("eyebrow"), who=True)}<h1 data-in style="--i:1">{h(d["h"])}</h1><p class="lead" data-in style="--i:2">{h(d["sub"])}</p>'
             f'{chips}{acts(d)}{under(d)}{below}')
    return sec("hero hcenter " + tone(), d, inner, pre=backdrop(True))


@S("hero_form", """
.hero{padding-block:clamp(36px,5vw,72px) clamp(56px,8vw,104px)}
.hf-g{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);align-items:center}
.hero .lead{margin-top:1.1rem}.hero .ticks{margin-top:1.4rem}
.meta{display:flex;flex-wrap:wrap;gap:.6rem 2rem;margin-top:1.6rem;padding-top:1.2rem;border-top:max(1px,var(--bw)) solid var(--line)}
.meta dt{font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}.meta dd{font-weight:700}
.hf-v{display:grid;gap:1.4rem}.hf-v .bookwrap{padding:clamp(12px,2vw,24px)}.hf-v .book{width:min(210px,56%)}
.ft-t{font-size:1.5rem;margin-bottom:.2rem}
.cal-m{font-weight:700;margin-bottom:.7rem}.cal-g{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:1.2rem}
.cal-g span{aspect-ratio:1;display:grid;place-items:center;border-radius:50%;font-size:.86rem;color:var(--ink2)}
.cal-g .on{background:var(--bg2);color:var(--ink);font-weight:700}.cal-g .pick,.cal-s .pick{background:var(--accent);color:var(--accent-ink)}
.cal-s{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1rem}.cal-s .slot{border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),12px);text-align:center;padding:.65rem .3rem;font-weight:600;font-size:.92rem}
@media(max-width:860px){.hf-g{grid-template-columns:1fr}.hf-v .bookwrap{order:2}}
""")
def hero_form(d, P):
    meta = ""
    if d.get("meta"):
        meta = '<dl class="meta">' + "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in d["meta"]) + "</dl>"
    inner = (f'<div class="hf-g"><div>{eyebrow(d.get("eyebrow"), who=True)}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{ul(d.get("bullets"))}{meta}{under(d)}</div>'
             f'<div class="hf-v" id="{d.get("fid", "signup")}" data-in style="--i:3">{vis(d.get("visual"))}{form(d["form"]) if d.get("form") else ""}'
             f'{reassure(d.get("after"), "check")}</div></div>')
    long = " long" if len((d.get("form") or {}).get("fields", [])) >= 3 else ""
    return sec("hero hform" + long + " " + tone(), d, inner, pre=backdrop(True))


@S("hero_stage", """
.hero{padding-block:clamp(36px,5vw,72px) clamp(56px,8vw,104px)}
.hstage h1{font-size:clamp(2.4rem,calc(5vw*var(--hs)),calc(4rem*var(--hs)));max-width:16ch}
.hstage .lead{margin-top:1.6rem}
.hst-g{display:grid;grid-template-columns:1.2fr .8fr;gap:clamp(28px,5vw,64px);align-items:end}
.hstats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1.4rem 2.4rem;margin-top:clamp(26px,3.6vw,44px);padding-top:1.3rem;border-top:max(1px,var(--bw)) solid var(--line)}
.hstats b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2rem,4vw,3.1rem);line-height:1;color:var(--accent-t);letter-spacing:var(--hls)}
.hstats span{font-size:.9rem;color:var(--ink2)}
@media(max-width:860px){.hst-g{grid-template-columns:1fr}.hst-g>div:last-child{max-width:420px}}
""")
def hero_stage(d, P):
    stats = ""
    if d.get("stats"):
        stats = '<div class="hstats">' + "".join(f"<div><b>{e(n)}</b><span>{e(l)}</span></div>" for n, l in d["stats"]) + "</div>"
    v = d.get("visual") or {}
    person = bool(v) and v.get("kind", "person") == "person"
    pic = f'<div class="hst-v" data-in style="--i:2">{vis(v, main=True)}</div>' if v else ""
    inner = (f'<div class="hst-g"><div>{eyebrow(d.get("eyebrow"), who=not person)}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{acts(d)}{under(d)}</div>{pic}</div>{stats}')
    return sec("hero hstage " + tone(), d, inner, pre=backdrop(True))


@S("hero_article", """
.hart{padding-block:clamp(36px,5vw,72px) 0}
.hart .wrap{max-width:900px}.hart h1{font-size:clamp(2rem,calc(4vw*var(--hs)),calc(3.2rem*var(--hs)))}
.hart .lead{margin-top:1.3rem;max-width:none}
.byline{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.2rem;margin-top:1.8rem;padding-block:1rem;border-block:max(1px,var(--bw)) solid var(--line);font-size:.9rem}
.byline b{font-weight:700}
.short{margin-top:1.8rem;background:var(--bg2);box-shadow:none}.short h2{font:700 .8rem/1.3 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t);margin-bottom:.4rem}
.short .ticks{font-size:1.05rem}
.toc{display:flex;flex-wrap:wrap;gap:.4rem 1.4rem;margin-top:1.2rem;font-size:.92rem}.toc span{color:var(--ink2)}
.hart .ph{margin-top:clamp(28px,4vw,48px)}
""")
def hero_article(d, P):
    upd = f'<span>Updated <time datetime="{e(d["updated_iso"])}">{e(d["updated"])}</time></span>' if d.get("updated") else ""
    by = (f'<div class="byline">{kit.face(d["author"])}<span>By <a class="link" href="about.html"><b>{e(d["author"])}</b></a>, {e(d["role"])}</span>'
          f'<span>Published <time datetime="{e(d["iso"])}">{e(d["date"])}</time></span>{upd}<span>{e(d["read"])}</span></div>')
    short = ""
    if d.get("short"):
        short = f'<aside class="card short"><h2>{e(d.get("short_h", "The Short Version"))}</h2>{ul(d["short"])}</aside>'
    toc = ""
    if d.get("toc"):
        toc = '<nav class="toc" aria-label="On this page"><span>On this page:</span>' + "".join(f'<a class="link" href="#{i}">{e(t)}</a>' for t, i in d["toc"]) + "</nav>"
    v = vis(dict(d.get("visual") or {}, kind="scene", ar="16/7"))
    inner = (f'{eyebrow(d.get("kicker"))}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["standfirst"])}</p>{by}{short}{toc}{v}')
    return sec("hart", d, inner)


@S("bento", """
.bento{padding-block:clamp(24px,3vw,40px) clamp(48px,6vw,80px)}
.bn{display:grid;grid-template-columns:repeat(6,1fr);gap:clamp(12px,1.6vw,18px)}
.tile{border-radius:var(--r);background:var(--card);padding:clamp(20px,2.6vw,32px);border:var(--bw) solid var(--line);box-shadow:var(--shadow);display:flex;flex-direction:column;gap:.7rem;min-height:190px}
.tile.w6{grid-column:span 6}.tile.w4{grid-column:span 4}.tile.w3{grid-column:span 3}.tile.w2{grid-column:span 2}
.tile.t1{background:var(--t1,var(--bg2))}.tile.t2{background:var(--t2,var(--bg2))}.tile.t3{background:var(--t3,var(--bg2))}
.tile.dk{background:var(--dark);color:var(--dark-ink);--ink:var(--dark-ink);--ink2:color-mix(in srgb,var(--dark-ink) 76%,var(--dark));--accent-t:var(--dark-accent);--line:color-mix(in srgb,var(--dark-ink) 22%,var(--dark))}
.tile h1{font-size:clamp(2rem,4.2vw,3.3rem)}.tile .big{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.6rem,5vw,4rem);line-height:.95;letter-spacing:var(--hls)}
.tile .eyebrow{margin-bottom:0}.tile .btn{align-self:flex-start;margin-top:auto}.tile .ph{flex:1;min-height:220px;aspect-ratio:auto;margin:calc(clamp(20px,2.6vw,32px)*-1);border-radius:0}
.tile:has(>.ph){overflow:hidden}
.tile li{display:flex;justify-content:space-between;gap:1rem;padding:.65rem 0;border-top:1px solid var(--line);font-size:.96rem}.tile li span{color:var(--ink2);white-space:nowrap;font-size:.85rem}
.tile .q{font-family:var(--fd);font-weight:var(--hw);font-size:1.35rem;line-height:1.2;letter-spacing:var(--hls)}
.tile .by{display:flex;align-items:center;gap:.7rem;margin-top:auto}
.tile .inl{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto}.tile .inl input{flex:1;min-width:150px;min-height:50px;border-radius:var(--rb);border:1px solid var(--line);padding:0 1.1rem;font:inherit;background:var(--bg)}
.tile .crowd{margin-top:.4rem}
@media(max-width:860px){.tile.w4,.tile.w3,.tile.w2{grid-column:span 6}}
""")
def bento(d, P):
    out = ""
    for i, t in enumerate(d["tiles"]):
        k = t["kind"]
        cls = f'tile w{t.get("w", 2)} {t.get("tone", "")}'
        body = eyebrow(t.get("eyebrow"))
        if k == "intro":
            body += f'<h1>{h(t["h"])}</h1><p class="lead">{h(t["text"])}</p>{btn(t.get("cta"))}'
        elif k == "stat":
            body += f'<p class="big">{e(t["num"])}</p><p>{h(t["text"])}</p>'
        elif k == "list":
            body += f'<h2 style="font-size:1.5rem">{h(t["h"])}</h2><ul>' + "".join(
                f'<li><a href="{kit.connect("article")}" class="link" style="text-decoration:none">{e(a)}</a><span>{e(b)}</span></li>' for a, b in t["items"]) + "</ul>"
        elif k == "form":
            body += (f'<h2 style="font-size:1.7rem">{h(t["h"])}</h2><p>{h(t["text"])}</p>'
                     f'{form_open("newsletter", "inl")}<label class="skip" for="bn{i}">Email</label>'
                     f'<input id="bn{i}" name="email" type="email" placeholder="you@email.com" autocomplete="email" required><button class="btn" type="submit">{e(t["button"])}</button></form>'
                     f'{crowd(t.get("proof"), 3).replace(" data-in", "")}<p class="fine">{h(t.get("note", ""))}</p>')
        elif k == "quote":
            name = t["by"].split(",")[0]
            body += f'<p class="q">{h(t["q"])}</p><p class="by fine">{kit.face(name)}<span>{e(t["by"])}</span></p>'
        elif k == "ph":
            body += vis(t["visual"], main=True)
        else:
            body += f'<h2 style="font-size:1.5rem">{h(t["h"])}</h2><p>{h(t["text"])}</p>{btn(t.get("cta"), "ghost")}'
        out += f'<div class="{cls}" data-in style="--i:{i}">{body}</div>'
    return sec("bento", d, f'<div class="bn">{out}</div>')


@S("linkbio", """
.lb{padding-block:clamp(28px,5vw,56px)}.lb .wrap{max-width:520px;text-align:center}
.lb>.wrap>.ph{width:124px;margin:0 auto 1rem;border-radius:50%;--ar:1/1;box-shadow:0 0 0 5px var(--card),0 0 0 7px var(--accent)}
.lb h1{font-size:clamp(1.9rem,6vw,2.5rem)}.lb .lead{margin:.7rem auto 0;font-size:1.05rem}
.lb .crowd{justify-content:center;margin-top:1.1rem}
.lb-f{margin-top:1.8rem;text-align:left}.lb-f h2{font-size:1.45rem;margin:.3rem 0 .5rem}.lb-f .btn{width:100%;margin-top:1rem}
.lb-l{margin-top:1.1rem;display:grid;gap:.75rem}
.lb-l a{display:flex;align-items:center;justify-content:space-between;gap:1rem;text-align:left;text-decoration:none;min-height:64px;padding:.8rem 1.2rem;border-radius:var(--r);background:var(--card);border:var(--bw) solid var(--line);box-shadow:var(--shadow);font-weight:700;transition:translate .2s}
.lb-l a:hover{translate:0 -3px}
.lb-l small{display:block;font-weight:400;color:var(--ink2);font-size:.84rem}.lb-l i{font-style:normal;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:var(--bg2);border-radius:999px;padding:.3em .7em;white-space:nowrap}
.lb-s{display:flex;justify-content:center;flex-wrap:wrap;gap:.4rem 1.2rem;margin-top:1.8rem;font-size:.9rem}
.lb-s a{min-height:44px;display:inline-flex;align-items:center}
""")
def linkbio(d, P):
    f = d["feature"]
    links = "".join(
        f'<a href="{e(hr)}"><span>{e(a)}<small>{e(b)}</small></span>{("<i>" + e(t) + "</i>") if t else ""}</a>' for a, b, t, hr in d["links"])
    soc = "".join(f'<a href="{kit.connect(s)}">{e(s)}</a>' for s in d["socials"])
    inner = (f'{vis({"kind": "person", "label": d["photo"], "ar": "1/1"}, main=True)}<h1>{h(d["h"])}</h1><p class="lead">{h(d["sub"])}</p>{crowd(d.get("proof"), 3)}'
             f'<div class="card lb-f">{eyebrow(f["eyebrow"])}<h2>{h(f["h"])}</h2><p>{h(f["text"])}</p>{btn(f["cta"])}{reassure(f.get("reassure"))}</div>'
             f'<nav class="lb-l" aria-label="Main links">{links}</nav><nav class="lb-s" aria-label="Social profiles">{soc}</nav>')
    return sec("lb", d, inner)


# ---------- PROOF ----------

@S("logos", """
.logos{padding-block:clamp(26px,3.5vw,44px);border-block:max(1px,var(--bw)) solid var(--line)}
.logos .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:1rem 2.6rem;justify-content:center}
.logos p{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink2)}
.logos ul{display:flex;flex-wrap:wrap;gap:.8rem 2.6rem;justify-content:center}
.logos li{display:flex;align-items:center;gap:.55rem;font-family:var(--fd);font-weight:var(--hw);font-size:1.25rem;letter-spacing:var(--hls);text-transform:var(--htt);opacity:.74}
.logos li:nth-child(even){font-family:var(--fb);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.95rem}
.logos li::before{content:"";width:16px;height:16px;border-radius:50%;background:currentColor;opacity:.6}
.logos li:nth-child(3n+2)::before{border-radius:3px;rotate:45deg}.logos li:nth-child(3n)::before{background:none;border:4px solid currentColor}
@media(max-width:600px){.logos ul{gap:.7rem 1.4rem}.logos li{font-size:1.02rem}.logos li:nth-child(even){font-size:.78rem}.logos li::before{width:12px;height:12px}}
""")
def logos(d, P):
    return sec("logos", d, f'<p>{e(d["label"])}</p><ul>' + "".join(f"<li>{e(x)}</li>" for x in d["items"]) + "</ul>")


@S("stats", """
.st-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:2rem 2.4rem}
.st-g>div{padding-left:1.3rem;border-left:max(2px,var(--bw)) solid var(--accent-t)}
.st-g b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.4rem,5vw,3.9rem);line-height:1;letter-spacing:var(--hls);color:var(--accent-t)}
.st-g span{display:block;margin-top:.5rem;color:var(--ink2);max-width:24ch}
""")
def stats(d, P):
    g = '<div class="st-g">' + "".join(f"<div><b>{e(n)}</b><span>{h(l)}</span></div>" for n, l in d["items"]) + "</div>"
    note = f'<p class="fine" style="margin-top:2rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("stats", d, sh(d) + g + note)


def figure(q, cls="card"):
    res = f'<span class="res">{e(q["result"])}</span>' if q.get("result") else ""
    return (f'<figure class="{cls}">{res}<blockquote><p>{h(q["q"])}</p></blockquote>'
            f'<figcaption>{kit.face(q["name"])}<span><b>{e(q["name"])}</b>{e(q["role"])}</span></figcaption></figure>')


@S("quotes", """
.qt blockquote{font-size:1.06rem;line-height:1.55}.qt .feature blockquote{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.5rem,3vw,2.3rem);line-height:1.18;letter-spacing:var(--hls);text-transform:var(--htt);max-width:26ch}
.qt figure.card{display:flex;flex-direction:column;transition:translate .25s}.qt figure.card:hover{translate:0 -4px}
.qt figure.card>blockquote::before{content:"\\201C";display:block;font-family:Georgia,serif;font-size:3.4rem;line-height:.7;height:1.4rem;color:color-mix(in srgb,var(--accent) 45%,transparent)}
.qt figcaption{display:flex;align-items:center;gap:.8rem;margin-top:auto;padding-top:1.2rem;font-size:.9rem;color:var(--ink2)}.qt figcaption b{color:var(--ink);display:block}
.res{display:inline-block;align-self:flex-start;margin-bottom:1rem;font-size:.76rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-t);background:color-mix(in srgb,var(--accent) 12%,transparent);border-radius:999px;padding:.4em .9em}
.qt .wall{columns:3 260px;column-gap:clamp(16px,2.4vw,28px)}.qt .wall figure{break-inside:avoid;margin-bottom:clamp(16px,2.4vw,28px)}
.qt .feature{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(28px,5vw,64px);align-items:center}
@media(max-width:760px){.qt .feature{grid-template-columns:1fr}.qt .feature .ph{max-width:300px}}
""")
def quotes(d, P):
    v = d.get("variant", "grid")
    if v == "feature":
        q = d["items"][0]
        pic = dict(d.get("visual") or {}, who=q["name"]) if d.get("visual") else None
        body = f'<div class="feature">{vis(pic)}{figure(q, "")}</div>'
    elif v == "wall":
        body = '<div class="wall">' + "".join(figure(q) for q in d["items"]) + "</div>"
    else:
        body = f'<div class="grid" style="--cols:{d.get("cols", 3)}">' + "".join(figure(q) for q in d["items"]) + "</div>"
    note = f'<p class="fine" style="margin-top:1.8rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("qt", d, sh(d) + body + note + acts(d).replace(" data-in", ""))


@S("metrics", """
.mt{width:100%;border-collapse:collapse;font-size:1rem}
.mt th,.mt td{text-align:left;padding:1rem .8rem;border-bottom:max(1px,var(--bw)) solid var(--line)}
.mt thead th{font:600 .76rem/1.3 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}
.mt td:last-child{font-family:var(--fd);font-weight:var(--hw);font-size:1.5rem;color:var(--accent-t);letter-spacing:var(--hls)}
.mt-g{display:grid;grid-template-columns:1.25fr .75fr;gap:clamp(20px,4vw,56px);align-items:center}
.chartc{padding:22px 24px}.chartc h3{font:700 .78rem/1.3 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);margin-bottom:1rem}
.chartc svg{width:100%;height:auto;display:block}.chartc .ct{font:600 12px var(--fb);fill:var(--ink2)}.chartc .cv{font:700 12px var(--fb);fill:var(--ink2)}.chartc .cb{fill:var(--accent-t)}
.chartc .key{display:flex;gap:1.2rem;margin-top:.8rem;font-size:.8rem;color:var(--ink2)}.chartc .key i{display:inline-block;width:12px;height:12px;border-radius:3px;background:var(--line);margin-right:.4em;vertical-align:-1px}.chartc .key i.a{background:var(--accent)}
@media(max-width:860px){.mt-g{grid-template-columns:1fr}}
@media(max-width:600px){.mt thead{display:none}.mt tr{display:block;padding:.8rem 0;border-bottom:max(1px,var(--bw)) solid var(--line)}.mt th,.mt td{display:block;border:0;padding:.15rem 0}.mt td::before{content:attr(data-l) ": ";font-size:.78rem;color:var(--ink2);font-family:var(--fb)}}
""")
def metrics(d, P):
    b4, af = e(d.get("before", "Before")), e(d.get("after", "After"))
    rows = "".join(f'<tr><th scope="row">{e(a)}</th><td data-l="{b4}">{e(b)}</td><td data-l="{af}">{e(c)}</td></tr>' for a, b, c in d["items"])
    t = (f'<table class="mt"><thead><tr><th scope="col">Measure</th><th scope="col">{b4}</th>'
         f'<th scope="col">{af}</th></tr></thead><tbody>{rows}</tbody></table>')
    if d.get("chart"):
        c = d["chart"]
        t = (f'<div class="mt-g">{t}<figure class="card chartc"><h3>{e(c["title"])}</h3>{art.bars(c["rows"], c.get("unit", ""))}'
             f'<p class="key"><span><i></i>{b4}</span><span><i class="a"></i>{af}</span></p></figure></div>')
    note = f'<p class="fine" style="margin-top:1.4rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("metrics", d, sh(d) + t + note + acts(d).replace(" data-in", ""))


@S("trust", """
.trust{padding-block:clamp(26px,3.5vw,44px)}.trust ul{display:flex;flex-wrap:wrap;gap:1rem 2.6rem;justify-content:center}
.trust li{display:flex;align-items:center;gap:.6rem;font-weight:600;font-size:.96rem}.trust .ic{color:var(--accent-t)}
""")
def trust(d, P):
    return sec("trust", d, "<ul>" + "".join(f"<li>{art.icon(i)}<span>{h(t)}</span></li>" for i, t in d["items"]) + "</ul>")


# ---------- CONTENT ----------

@S("doors", """
.door{display:flex;flex-direction:column;gap:.8rem;text-decoration:none;min-height:240px;transition:translate .25s,border-color .25s}
.door .tag{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.door h3{font-size:1.6rem}.door .go{margin-top:auto;font-weight:700;display:flex;align-items:center;gap:.5rem}
.door .go .ic{transition:translate .2s}.door:hover{translate:0 -5px;border-color:var(--accent-t)}.door:hover .go .ic{translate:5px 0}
""")
def doors(d, P):
    it = "".join(
        f'<a class="card door" href="{e(x.get("href") or P["action_file"])}"><span class="tag">{e(x["tag"])}</span><h3>{h(x["h"])}</h3>'
        f'<p>{h(x["text"])}</p><span class="go">{e(x["go"])}{art.icon("arrow")}</span></a>' for x in d["items"])
    return sec("doors", d, sh(d) + f'<div class="grid" style="--cols:{len(d["items"])}">{it}</div>')


@S("prose", """
.prose .wrap{max-width:820px}.prose p{font-size:1.14rem;line-height:1.7}.prose .ticks{margin-top:1.4rem;font-size:1.08rem}
.pull{margin-block:2.2rem;padding-left:1.4rem;border-left:4px solid var(--accent-t);font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.4rem,2.6vw,1.9rem);line-height:1.22;letter-spacing:var(--hls);text-transform:var(--htt)}
.sign{margin-top:1.8rem;font-family:var(--fd);font-size:1.5rem;font-style:italic}
""")
def prose(d, P):
    pull = f'<p class="pull">{h(d["pull"])}</p>' if d.get("pull") else ""
    sign = f'<p class="sign">{e(d["sign"])}</p>' if d.get("sign") else ""
    return sec("prose", d, sh(d) + paras(d.get("paras")) + ul(d.get("list")) + pull + paras(d.get("after")) + sign + acts(d).replace(" data-in", ""))


@S("cards", """
.cards .card{transition:translate .25s,border-color .25s}.cards .card:hover{translate:0 -5px;border-color:var(--accent-t)}
.cards .card h3{margin-bottom:.6rem}.cards .n{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:2.4rem;line-height:1;color:var(--accent-t);margin-bottom:1rem;letter-spacing:var(--hls)}
.cards .card p{color:var(--ink2)}
.chip-ic{display:grid;place-items:center;width:48px;height:48px;border-radius:min(var(--r),14px);background:color-mix(in srgb,var(--accent) 13%,var(--card));color:var(--accent-t);margin-bottom:1.1rem}
""")
def cards(d, P):
    def top(i, a):
        if d.get("num"):
            return f'<span class="n">{str(i + 1).zfill(2)}</span>'
        if d.get("plain"):
            return ""
        name = d["icons"][i] if d.get("icons") else art.icon_for(a, i)
        return f'<span class="chip-ic">{art.icon(name)}</span>'
    it = "".join(f'<div class="card">{top(i, a)}<h3>{h(a)}</h3><p>{h(b)}</p></div>' for i, (a, b) in enumerate(d["items"]))
    return sec("cards", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 3)}">{it}</div>' + acts(d).replace(" data-in", ""))


@S("steps", """
.stp{counter-reset:s;display:grid;gap:0}
.stp li{counter-increment:s;display:grid;grid-template-columns:auto 1fr;gap:clamp(16px,3vw,40px);padding:clamp(20px,3vw,34px) 0;border-top:max(1px,var(--bw)) solid var(--line)}
.stp li::before{content:counter(s,decimal-leading-zero);font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2rem,4.5vw,3.4rem);line-height:.95;color:var(--accent-t);min-width:1.6em;letter-spacing:var(--hls)}
.stp h3{font-size:1.5rem;margin-bottom:.4rem}.stp p{color:var(--ink2);max-width:60ch}
""")
def steps(d, P):
    it = "".join(f"<li><div><h3>{h(a)}</h3><p>{h(b)}</p></div></li>" for a, b in d["items"])
    return sec("steps", d, sh(d) + f'<ol class="stp">{it}</ol>' + acts(d).replace(" data-in", ""))


@S("split", """
.sp-g{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(28px,6vw,84px);align-items:center}
.sp-g h2{margin-bottom:1.2rem}.sp-g .ticks{margin-top:1.2rem}
.split.flip .sp-v{order:2}
@media(max-width:860px){.sp-g{grid-template-columns:1fr}.sp-v{max-width:420px}.split.flip .sp-v{order:0}}
""")
def split(d, P):
    v = d.get("visual") or {}
    b = P["brand"]
    name = f'<p class="signed"><b>{e(b["person"])}</b>{e(b["role"])}</p>' if v.get("kind", "person") == "person" and b.get("role") and not v.get("who") else ""
    inner = (f'<div class="sp-g"><div class="sp-v">{vis(d.get("visual"))}{name}</div><div>{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2>'
             f'{paras(d.get("paras"))}{ul(d.get("bullets"))}{acts(d).replace(" data-in", "")}{reassure(d.get("reassure"))}</div></div>')
    return sec("split", d, inner, "flip" if d.get("flip") else "")


@S("compare", """
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,2.4vw,28px)}
.cmp h3{margin-bottom:.8rem;font-size:1.45rem}.cmp .no li::before{border:0;content:"\\00d7";top:-.1em;rotate:0deg;font-weight:700;color:var(--ink2);width:auto;height:auto;font-size:1.2em}
.cmp .no{background:transparent;box-shadow:none}.cmp .yes{border-color:var(--accent-t)}
@media(max-width:700px){.cmp{grid-template-columns:1fr}}
""")
def compare(d, P):
    l, r = d["left"], d["right"]
    inner = (f'<div class="cmp"><div class="card no"><h3>{h(l[0])}</h3>{ul(l[1])}</div>'
             f'<div class="card yes"><h3>{h(r[0])}</h3>{ul(r[1])}</div></div>')
    return sec("compare", d, sh(d) + inner + acts(d).replace(" data-in", ""))


@S("matrix", """
.mxw{overflow-x:auto}.mx{width:100%;border-collapse:collapse;min-width:560px}.mx th,.mx td{padding:1rem .9rem;border-bottom:max(1px,var(--bw)) solid var(--line);text-align:center}
.mx th:first-child,.mx td:first-child{text-align:left;font-weight:600}.mx thead th{font-family:var(--fd);font-weight:var(--hw);font-size:1.15rem;letter-spacing:var(--hls);text-transform:var(--htt);vertical-align:bottom}
.mx .hot{background:color-mix(in srgb,var(--accent) 9%,transparent)}.mx .ic{color:var(--accent-t);margin:auto;display:block}.mx .no{color:var(--ink2)}
""")
def matrix(d, P):
    return sec("matrix", d, sh(d) + table(d["cols"], d["rows"], d.get("hot")) + (f'<p class="fine" style="margin-top:1.2rem">{h(d["note"])}</p>' if d.get("note") else ""))


def table(cols, rows, hot=None):
    def cell(v, i):
        c = ' class="hot"' if i == hot else ""
        if v is True:
            return f'<td{c}>{art.icon("check")}<span class="skip">Included</span></td>'
        if v is False:
            return f'<td{c}><span class="no" aria-hidden="true">·</span><span class="skip">Not included</span></td>'
        return f"<td{c}>{h(v)}</td>"
    head = "".join(f'<th scope="col"{" class=hot" if i == hot else ""}>{h(c)}</th>' for i, c in enumerate(cols))
    body = "".join(f'<tr><th scope="row">{h(r[0])}</th>' + "".join(cell(v, i + 1) for i, v in enumerate(r[1:])) + "</tr>" for r in rows)
    return f'<div class="mxw"><table class="mx"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


@S("modules", """
.mod details{border-top:max(1px,var(--bw)) solid var(--line)}.mod details:last-of-type{border-bottom:max(1px,var(--bw)) solid var(--line)}
.mod summary{display:grid;grid-template-columns:minmax(90px,auto) 1fr auto;gap:1rem 2rem;align-items:baseline;padding:1.3rem 0;cursor:pointer;list-style:none}
.mod summary::-webkit-details-marker{display:none}
.mod summary .tag{font-size:.78rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.mod summary h3{font-size:clamp(1.2rem,2.4vw,1.6rem)}.mod summary::after{content:"+";font-size:1.6rem;line-height:1}
.mod details[open] summary::after{content:"\\2212"}
.mod .in{padding:0 0 1.6rem;max-width:68ch;color:var(--ink2)}
@media(max-width:600px){.mod summary{grid-template-columns:1fr auto}.mod summary .tag{grid-column:1/-1}}
""")
def modules(d, P):
    it = "".join(
        f'<details{" open" if i == 0 else ""}><summary><span class="tag">{e(m["tag"])}</span><h3>{h(m["h"])}</h3></summary>'
        f'<div class="in"><p>{h(m["text"])}</p>{ul(m.get("points"))}</div></details>' for i, m in enumerate(d["items"]))
    note = f'<p class="fine" style="margin-top:1.4rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("mod", d, sh(d) + it + note + acts(d).replace(" data-in", ""))


@S("pricing", """
.pr-a{margin-bottom:2.4rem;font-size:1.05rem;max-width:62ch}
.tier{display:flex;flex-direction:column;position:relative;transition:translate .25s}.tier .nm{font-size:.82rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}
.tier .pc{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.4rem,4.4vw,3.3rem);line-height:1;margin:.8rem 0 .2rem;letter-spacing:var(--hls)}
.tier .pc small{font:400 .95rem var(--fb);color:var(--ink2);letter-spacing:0}
.tier .eq{font-weight:700;color:var(--accent-t);margin-bottom:.3rem}
.tier .ticks{margin:1rem 0 1.6rem;font-size:.97rem}.tier .btn{margin-top:auto;width:100%}
.tier .ticks li::before{width:1.15em;height:1.15em;border:0;rotate:0deg;top:.2em;border-radius:50%;background:color-mix(in srgb,var(--accent) 18%,transparent)}
.tier .ticks li::after{content:"";position:absolute;left:.32em;top:.5em;width:.5em;height:.26em;border-left:2px solid var(--accent-t);border-bottom:2px solid var(--accent-t);rotate:-45deg}
.tier.hot{border-color:var(--accent-t);outline:2px solid var(--accent-t);outline-offset:-1px;translate:0 -10px;box-shadow:0 34px 64px -30px color-mix(in srgb,var(--accent) 70%,transparent)}
.tier .bdg{position:absolute;top:-.85rem;left:1.4rem;background:var(--accent);color:var(--accent-ink);font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.35em .9em;border-radius:999px}
.tier .und{margin-top:.8rem;font-size:.82rem;color:var(--ink2);display:flex;gap:.4rem;align-items:flex-start}.tier .und .ic{width:16px;height:16px;color:var(--accent-t);margin-top:.15em}
.pr-q{margin-top:clamp(20px,3vw,32px);display:grid;grid-template-columns:auto 1fr;gap:.4rem 1.2rem;align-items:center;background:transparent;box-shadow:none;border-style:dashed}
.pr-q .av{width:60px;height:60px;grid-row:span 2}.pr-q blockquote{font-size:1.08rem;line-height:1.5}.pr-q figcaption{font-size:.88rem;color:var(--ink2)}.pr-q figcaption b{color:var(--ink)}
.pr-1{display:grid;grid-template-columns:minmax(0,560px) 1fr;gap:clamp(20px,4vw,48px);align-items:center}.pr-1 .pr-q{margin-top:0;grid-template-columns:1fr;border:0;padding:0}.pr-1 .pr-q .av{grid-row:auto}
.pr-1 .pr-q blockquote{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.3rem,2.4vw,1.8rem);line-height:1.25;letter-spacing:var(--hls)}
@media(max-width:900px){.tier.hot{translate:none}.pr-1{grid-template-columns:1fr}}
""")
def pricing(d, P):
    it = ""
    for t in d["tiers"]:
        bd = f'<span class="bdg">{e(t["badge"])}</span>' if t.get("badge") else ""
        eq = f'<p class="eq">{h(t["eq"])}</p>' if t.get("eq") else ""
        u = t.get("under") or d.get("under")
        und = f'<p class="und">{art.icon("shield")}<span>{h(u)}</span></p>' if u else ""
        it += (f'<div class="card tier{" hot" if t.get("hot") else ""}">{bd}<p class="nm">{e(t["name"])}</p>'
               f'<p class="pc">{e(t["price"])} <small>{e(t.get("per", ""))}</small></p>{eq}<p class="fine">{h(t["desc"])}</p>'
               f'{ul(t["feats"])}{btn(t["cta"], "" if t.get("hot") or len(d["tiers"]) == 1 else "ghost")}{und}</div>')
    anchor = f'<p class="pr-a">{h(d["anchor"])}</p>' if d.get("anchor") else ""
    note = f'<p class="fine" style="margin-top:1.6rem">{h(d["note"])}</p>' if d.get("note") else ""
    q = d.get("quote")
    qh = ""
    if q:
        qh = (f'<figure class="card pr-q">{kit.face(q["name"])}<blockquote><p>{h(q["q"])}</p></blockquote>'
              f'<figcaption><b>{e(q["name"])}</b> · {e(q["role"])}</figcaption></figure>')
    cols = len(d["tiers"])
    if cols == 1:
        body = f'<div class="pr-1">{it}{qh}</div>'
    else:
        body = f'<div class="grid" style="--cols:{cols}">{it}</div>{qh}'
    return sec("pricing", d, sh(d) + anchor + body + note)


@S("guarantee", """
.gu .card{display:grid;grid-template-columns:auto 1fr;gap:clamp(18px,3vw,40px);align-items:center;max-width:900px;margin:auto;border-color:var(--accent-t)}
.seal{width:clamp(96px,12vw,132px);aspect-ratio:1;border-radius:50%;border:3px double var(--accent-t);display:grid;place-items:center;align-content:center;gap:.3rem;text-align:center;font:700 .72rem/1.25 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--accent-t);padding:.6rem}
.seal .ic{width:28px;height:28px}
.gu h2{font-size:clamp(1.5rem,2.8vw,2.1rem);margin-bottom:.6rem}
@media(max-width:600px){.gu .card{grid-template-columns:1fr}}
""")
def guarantee(d, P):
    return sec("gu", d, f'<div class="card"><div class="seal" aria-hidden="true">{art.icon("shield")}{e(d["seal"])}</div><div><h2>{h(d["h"])}</h2>{paras(d["paras"])}</div></div>')


@S("faq", """
.faq .wrap{max-width:860px}.faq details{border-top:max(1px,var(--bw)) solid var(--line);transition:background .2s}.faq details:last-of-type{border-bottom:max(1px,var(--bw)) solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:1.2rem 2.6rem 1.2rem .4rem;position:relative;font-weight:700;font-size:1.08rem}
.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";position:absolute;right:.6rem;top:.9rem;font-size:1.5rem;font-weight:400}
.faq details[open]{background:color-mix(in srgb,var(--accent) 5%,transparent)}
.faq details[open] summary::after{content:"\\2212"}.faq .a{padding:0 .4rem 1.4rem;color:var(--ink2);max-width:66ch}
.faq .ask{margin-top:1.6rem}
""")
def faq(d, P):
    it = "".join(f'<details><summary>{h(q)}</summary><div class="a"><p>{h(a)}</p></div></details>' for q, a in d["items"])
    ask = ""
    if d.get("ask"):
        links = "".join(f' <a class="link" href="{e(hr)}"{dl}>{e(c)}</a>' for c, hr, dl in d.get("cals", []))
        ask = f'<p class="ask">{h(d["ask"])}{links}</p>'
    return sec("faq", d, sh(d) + it + ask)


@S("cta", """
.cta .wrap{text-align:center;max-width:880px}.cta h2{font-size:clamp(2.1rem,calc(5vw*var(--hs)),calc(3.8rem*var(--hs)))}
.cta .lead{margin:1.2rem auto 0}.cta .acts{justify-content:center}.cta .reassure{justify-content:center}
""")
def cta(d, P):
    d.setdefault("tone", "dark")
    lead = f'<p class="lead">{h(d["text"])}</p>' if d.get("text") else ""
    # the last decision on the page is made with a person in view: their face, name and role sit under the button
    inner = (f'{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2>{lead}{acts(d).replace(" data-in", "")}{reassure(d.get("note"), d.get("icon", "shield"))}'
             f'{kit.host()}')
    if d["tone"] == "dark":
        return sec("cta bleed t-light deep", d, inner, pre=backdrop())
    return sec("cta", d, inner)


@S("feed", """
.fd-l li{display:grid;grid-template-columns:minmax(90px,130px) 1fr auto;gap:.6rem 2rem;align-items:baseline;padding:1.25rem 0;border-top:max(1px,var(--bw)) solid var(--line)}
.fd-l li:last-child{border-bottom:max(1px,var(--bw)) solid var(--line)}
.fd-l .k{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.fd-l h3{font-size:clamp(1.15rem,2.2vw,1.5rem)}.fd-l h3 a{text-decoration:none}.fd-l h3 a:hover{text-decoration:underline;text-underline-offset:.2em}
.fd-l p{color:var(--ink2);font-size:.96rem;margin-top:.3rem;max-width:64ch}.fd-l .m{font-size:.85rem;color:var(--ink2);white-space:nowrap}
.fd-g .ph{margin-bottom:1rem;--ar:16/10;box-shadow:none}.fd-g .k{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.fd-g h3{margin:.4rem 0 .5rem;font-size:1.35rem}.fd-g h3 a{text-decoration:none}.fd-g p{color:var(--ink2);font-size:.96rem}.fd-g .m{margin-top:.7rem;font-size:.84rem}
.fd-more{margin-top:2rem}
@media(max-width:700px){.fd-l li{grid-template-columns:1fr}}
""")
def feed(d, P):
    if d.get("variant") == "grid":
        it = "".join(
            f'<article>{vis({"kind": "sketch", "label": x.get("img", "Article image"), "ar": "16/10"})}<span class="k">{e(x["kind"])}</span>'
            f'<h3><a href="{e(x.get("href") or kit.connect(d.get("link", "article")))}">{h(x["title"])}</a></h3><p>{h(x.get("text", ""))}</p><p class="m fine">{e(x["meta"])}</p></article>'
            for x in d["items"])
        body = f'<div class="grid fd-g" style="--cols:{d.get("cols", 3)}">{it}</div>'
    else:
        it = "".join(
            f'<li><span class="k">{e(x["kind"])}</span><div><h3><a href="{e(x.get("href") or kit.connect(d.get("link", "article")))}">{h(x["title"])}</a></h3>'
            f'{("<p>" + h(x["text"]) + "</p>") if x.get("text") else ""}</div><span class="m">{e(x["meta"])}</span></li>' for x in d["items"])
        body = f'<ul class="fd-l">{it}</ul>'
    more = f'<p class="fd-more"><a class="link" href="{kit.connect(d.get("link", "article") + " index")}">{e(d["more"])}</a></p>' if d.get("more") else ""
    return sec("feed", d, sh(d) + body + more)


@S("capture", """
.cap .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,5vw,64px);align-items:center}
.cap h2{font-size:clamp(1.8rem,3.4vw,2.6rem)}.cap p{margin-top:.8rem;color:var(--ink2)}
.cap form{display:flex;flex-wrap:wrap;gap:.6rem}.cap input{flex:1;min-width:200px;min-height:54px;padding:0 1.1rem;border-radius:var(--rb);border:max(1px,var(--bw)) solid var(--line);background:var(--card);color:var(--ink);font:inherit}
.cap .fine{flex-basis:100%;margin-top:.2rem}.cap .crowd{flex-basis:100%;margin-top:.4rem}.cap .crowd p{margin-top:0}
@media(max-width:800px){.cap .wrap{grid-template-columns:1fr}}
""")
def capture(d, P):
    inner = (f'<div>{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2><p>{h(d["text"])}</p></div>'
             f'{form_open(d.get("name", "newsletter"))}<label class="skip" for="cap-e">Email address</label>'
             f'<input id="cap-e" name="email" type="email" placeholder="you@email.com" autocomplete="email" required><button class="btn" type="submit">{e(d["button"])}</button>'
             f'<p class="fine">{h(d.get("note", ""))}</p>{crowd(d.get("proof"), 3).replace(" data-in", "")}</form>')
    return sec("cap", d, inner)


@S("schedule", """
.sch li{display:grid;grid-template-columns:minmax(110px,170px) 1fr;gap:.4rem 2rem;padding:1.3rem 0;border-top:max(1px,var(--bw)) solid var(--line)}
.sch li:last-child{border-bottom:max(1px,var(--bw)) solid var(--line)}
.sch .t{font-family:var(--fd);font-weight:var(--hw);font-size:1.35rem;color:var(--accent-t);letter-spacing:var(--hls);text-transform:var(--htt);line-height:1.1}
.sch h3{font-size:1.3rem;margin-bottom:.3rem}.sch p{color:var(--ink2);max-width:62ch}
@media(max-width:600px){.sch li{grid-template-columns:1fr}}
""")
def schedule(d, P):
    it = "".join(f'<li><span class="t">{e(t)}</span><div><h3>{h(a)}</h3><p>{h(b)}</p></div></li>' for t, a, b in d["items"])
    return sec("schedule", d, sh(d) + f'<ol class="sch">{it}</ol>' + acts(d).replace(" data-in", ""))


@S("article", """
.art .wrap{max-width:760px}.art{padding-block:clamp(36px,5vw,64px)}
.art p{font-size:1.16rem;line-height:1.75}.art h2{font-size:clamp(1.6rem,3vw,2.1rem);margin:2.6rem 0 1rem;scroll-margin-top:90px}
.art .ticks{margin:1.2rem 0;font-size:1.1rem}.art>.wrap>p:first-of-type::first-letter{font-family:var(--fd);font-weight:var(--hw);float:left;font-size:4.4em;line-height:.82;padding:.06em .1em 0 0;color:var(--accent-t)}
.pull{margin-block:2.2rem;padding-left:1.4rem;border-left:4px solid var(--accent-t);font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.4rem,2.6vw,1.9rem);line-height:1.22;letter-spacing:var(--hls);text-transform:var(--htt)}
.box{margin:2.4rem 0;background:var(--bg2);box-shadow:none}.box h2{margin:0 0 .6rem;font-size:1.3rem}
.art .mxw{margin:1.8rem 0}.art .mx{min-width:520px;font-size:1rem}.art .mx thead th{font-size:1rem}.art figcaption{font-size:.86rem;color:var(--ink2);margin-top:.6rem}
.art .chartc{margin:2rem 0}
.srcs{margin-top:2.6rem;padding-top:1.4rem;border-top:max(1px,var(--bw)) solid var(--line)}.srcs h2{margin:0 0 .8rem;font-size:1.2rem}
.srcs ol{list-style:decimal;padding-left:1.3rem;font-size:.96rem;color:var(--ink2)}.srcs li{margin-top:.5rem}.srcs a{color:var(--ink)}
.auth{display:grid;grid-template-columns:auto 1fr;gap:1.4rem;align-items:center;margin-top:3rem}.auth .av{width:84px;height:84px;font-size:1.5rem}
.auth h2{margin:0 0 .3rem;font-size:1.3rem}.auth p{font-size:1rem;line-height:1.55}
.mxw{overflow-x:auto}.mx{width:100%;border-collapse:collapse}.mx th,.mx td{padding:.9rem .8rem;border-bottom:max(1px,var(--bw)) solid var(--line);text-align:left;vertical-align:top}
.mx thead th{font-family:var(--fb);font-weight:700;letter-spacing:.04em}.mx .hot{background:color-mix(in srgb,var(--accent) 9%,transparent)}
.chartc{padding:22px 24px}.chartc h3{font:700 .78rem/1.3 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);margin-bottom:1rem}
.chartc svg{width:100%;height:auto;display:block;max-width:520px}.chartc .ct{font:600 12px var(--fb);fill:var(--ink2)}.chartc .cv{font:700 12px var(--fb);fill:var(--ink2)}.chartc .cb{fill:var(--accent-t)}
""")
def article(d, P):
    out = ""
    for b in d["blocks"]:
        k = b[0]
        if k == "p":
            out += f"<p>{h(b[1])}</p>"
        elif k == "h2":
            hid = f' id="{b[2]}"' if len(b) > 2 else ""
            out += f"<h2{hid}>{h(b[1])}</h2>"
        elif k == "quote":
            out += f'<p class="pull">{h(b[1])}</p>'
        elif k == "list":
            out += ul(b[1])
        elif k == "box":
            out += f'<aside class="card box"><h2>{h(b[1])}</h2>{ul(b[2])}</aside>'
        elif k == "table":
            out += f'<figure>{table(b[1], b[2], b[3] if len(b) > 3 else None)}<figcaption>{h(b[4]) if len(b) > 4 else ""}</figcaption></figure>'
        elif k == "chart":
            out += f'<figure class="card chartc"><h3>{e(b[1])}</h3>{art.bars(b[2], b[3] if len(b) > 3 else "")}</figure>'
        elif k == "sources":
            out += ('<section class="srcs"><h2>Sources</h2><ol>' + "".join(
                f'<li><a href="{e(u)}" rel="noopener">{e(t)}</a>. {e(pub)}</li>' for t, u, pub in b[1]) + "</ol></section>")
    a = d.get("author")
    if a:
        out += (f'<aside class="card auth">{kit.face(a["name"])}<div><h2>About {e(a["name"])}</h2>'
                f'<p>{h(a["bio"])}</p><p><a class="link" href="about.html">{e(a["link"])}</a></p></div></aside>')
    return sec("art", d, out)


@S("player", """
.pl{display:grid;grid-template-columns:auto 1fr;gap:clamp(18px,3vw,36px);align-items:center}
.pl .art-c{width:clamp(110px,18vw,190px);aspect-ratio:1;border-radius:var(--r);background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;text-align:center;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.1rem,2.4vw,1.8rem);line-height:1;padding:.6rem;text-transform:var(--htt);letter-spacing:var(--hls);box-shadow:0 24px 44px -20px color-mix(in srgb,var(--accent) 80%,transparent)}
.pl h2{font-size:clamp(1.5rem,3vw,2.3rem);margin:.3rem 0 .8rem}
.bar{display:flex;align-items:center;gap:1rem;margin-top:.6rem}.bar .pb{width:54px;height:54px;border-radius:50%;background:var(--accent);position:relative;flex:none}
.bar .pb::after{content:"";position:absolute;left:54%;top:50%;translate:-50% -50%;border-left:15px solid var(--accent-ink);border-block:10px solid transparent}
.bar .tr{flex:1;height:6px;border-radius:9px;background:var(--line);position:relative}.bar .tr::after{content:"";position:absolute;inset:0 64% 0 0;border-radius:9px;background:var(--accent-t)}
.pl-n{margin-top:1.6rem;display:flex;flex-wrap:wrap;gap:.6rem}.pl-n a{font-size:.86rem;font-weight:700;border:max(1px,var(--bw)) solid var(--line);border-radius:999px;padding:.5em 1em;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
@media(max-width:600px){.pl{grid-template-columns:1fr}}
""")
def player(d, P):
    apps = "".join(f'<a href="{"#notes" if a in ("Full transcript", "Show notes") else kit.connect(a)}">{e(a)}</a>' for a in d["apps"])
    inner = (f'<div class="card pl"><div class="art-c" aria-hidden="true">{h(d["art"])}</div><div>{eyebrow(d["eyebrow"])}'
             f'<h2>{h(d["h"])}</h2><p class="fine">{e(d["meta"])}</p>'
             f'<div class="bar" role="img" aria-label="Audio player mock-up"><span class="pb"></span><span class="tr"></span><span class="fine">{e(d["time"])}</span></div>'
             f'<div class="pl-n">{apps}</div></div></div>')
    return sec("player", d, inner)


@S("shownotes", """
.sn-g{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(24px,5vw,64px);align-items:start}
.sn-g h3{font:700 .8rem/1.3 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t);margin-bottom:1rem}
.sn-t li{display:grid;grid-template-columns:4.2rem 1fr;gap:.8rem;padding:.75rem 0;border-top:1px solid var(--line)}.sn-t b{font-variant-numeric:tabular-nums;color:var(--accent-t)}
.sn-x p{font-size:1.05rem;line-height:1.65}.sn-x p b{display:block;font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2);margin-bottom:.15rem}
.sn-x .link{display:inline-block;margin-top:1.2rem}
@media(max-width:800px){.sn-g{grid-template-columns:1fr}}
""")
def shownotes(d, P):
    stamps = "".join(f"<li><b>{e(t)}</b><span>{h(x)}</span></li>" for t, x in d["stamps"])
    lines = "".join(f"<p><b>{e(who)}</b>{h(x)}</p>" for who, x in d["transcript"])
    inner = (f'<div class="sn-g"><div><h3>In This Episode</h3><ul class="sn-t">{stamps}</ul></div>'
             f'<div class="sn-x"><h3>From The Transcript</h3>{lines}<a class="link" href="{kit.connect("full transcript")}">{e(d["more"])}</a></div></div>')
    return sec("shownotes", d, sh(d) + inner)


@S("products", """
.prd{display:flex;flex-direction:column;gap:.5rem;transition:translate .25s}.prd:hover{translate:0 -5px}
.prd .pv{position:relative;margin-bottom:.8rem}.prd .ph{--ar:4/3;box-shadow:none}
.prd .tagi{position:absolute;left:10px;bottom:10px;z-index:2;font:700 .72rem/1.2 var(--fb);background:var(--card);color:var(--ink);padding:.5em .8em;border-radius:999px;box-shadow:0 4px 12px rgba(0,0,0,.14)}
.prd .k{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.prd h3{font-size:1.4rem}.prd p{color:var(--ink2);font-size:.96rem}
.prd .row{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:auto;padding-top:1rem}
.prd .pc{font-family:var(--fd);font-weight:var(--hw);font-size:1.7rem;letter-spacing:var(--hls)}.prd .btn{min-height:48px;padding:.6em 1.2em;font-size:.92rem}
.prd .und{font-size:.8rem;color:var(--ink2);display:flex;gap:.4rem;align-items:center;margin-top:.3rem}.prd .und .ic{width:15px;height:15px;color:var(--accent-t)}
""")
def products(d, P):
    und = f'<p class="und">{art.icon("shield")}<span>{h(d["under"])}</span></p>' if d.get("under") else ""
    it = "".join(
        f'<article class="card prd"><div class="pv">{vis({"kind": "sketch", "label": x["img"], "ar": "4/3"})}'
        f'{("<span class=tagi>" + e(x["tag"]) + "</span>") if x.get("tag") else ""}</div><span class="k">{e(x["kind"])}</span>'
        f'<h3>{h(x["name"])}</h3><p>{h(x["text"])}</p><div class="row"><span class="pc">{e(x["price"])}</span>'
        f'<a class="btn" href="{e(x.get("href") or kit.connect("checkout " + x["name"]))}">{e(x.get("go", "Get it"))}<span class="skip"> {e(x["name"])}</span></a></div>{und}</article>' for x in d["items"])
    return sec("products", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 3)}">{it}</div>')


@S("contact", """
.ct-g{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);align-items:start}
.ct-d dt{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);margin-top:1.4rem}
.ct-d dd{font-size:1.1rem;margin-top:.2rem}.ct-d .ph{margin-top:1.8rem;--ar:16/10;box-shadow:none}
.ct-call{display:flex;align-items:center;gap:.8rem;text-decoration:none;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.7rem,3.4vw,2.4rem);letter-spacing:var(--hls);line-height:1.1;color:var(--accent-t)}
.ct-call .ic{width:34px;height:34px}.ct-call+p{margin-top:.3rem}
.hrs{width:100%;border-collapse:collapse;margin-top:.5rem}.hrs th,.hrs td{text-align:left;padding:.4rem 0;border-bottom:1px solid var(--line);font-weight:400;font-size:1rem}.hrs td{text-align:right}
.ft-t{font-size:1.5rem;margin-bottom:.2rem}
@media(max-width:860px){.ct-g{grid-template-columns:1fr}}
""")
def contact(d, P):
    det = "".join(f"<dt>{e(a)}</dt><dd>{h(b)}</dd>" for a, b in d["details"])
    hrs = ""
    if d.get("hours"):
        hrs = '<dt>Opening hours</dt><dd><table class="hrs"><tbody>' + "".join(
            f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in d["hours"]) + "</tbody></table></dd>"
    call = ""
    if d.get("call"):
        c = d["call"]
        call = f'<a class="ct-call" href="{e(c[1])}">{art.icon("phone")}{e(c[0])}</a><p class="fine">{h(c[2])}</p>'
    mp = vis({"kind": "sketch", "label": d["map"], "ar": "16/10"}) if d.get("map") else ""
    left = form(d["form"]) if d.get("form") else f'<div>{paras(d.get("paras"))}{ul(d.get("bullets"))}{acts(d).replace(" data-in", "")}</div>'
    inner = f'<div class="ct-g">{left}<div>{kit.host()}{call}<dl class="ct-d">{det}{hrs}</dl>{mp}</div></div>'
    return sec("contact", d, sh(d) + inner)


QUIZ_JS = """<script>
/* The quiz. Every question is already in the HTML, so it reads without this script. The script shows 1 question at a time and adds up the result. */
(function(){var f=document.querySelector('[data-quiz]');if(!f)return;var qs=[].slice.call(f.querySelectorAll('[data-q]')),i=0,
prog=f.querySelector('[data-progress]'),bar=f.querySelector('[data-bar]'),btn=f.querySelector('[data-next]'),warn=f.querySelector('[data-warn]'),
res=document.querySelector('[data-result]'),R=JSON.parse(f.getAttribute('data-styles'));f.classList.add('live');
function show(){qs.forEach(function(q,n){q.hidden=n!==i});prog.textContent='Question '+(i+1)+' of '+qs.length;bar.style.width=(i/qs.length*100)+'%';
btn.textContent=i===qs.length-1?'See My Result':'Next Question'}
btn.addEventListener('click',function(){if(i>=qs.length){qs.forEach(function(q){q.querySelectorAll('input').forEach(function(x){x.checked=false})});i=0;show();return}
var c=qs[i].querySelector('input:checked');if(!c){warn.hidden=false;qs[i].querySelector('input').focus();return}warn.hidden=true;
if(i<qs.length-1){i++;show();qs[i].querySelector('input').focus();return}
var t={};Object.keys(R).forEach(function(k){t[k]=0});qs.forEach(function(q){t[q.querySelector('input:checked').value]++});
var top=Object.keys(t).sort(function(a,b){return t[b]-t[a]})[0];
res.querySelector('[data-eyebrow]').textContent='Your result';res.querySelector('[data-title]').textContent=R[top][1];res.querySelector('[data-text]').textContent=R[top][2];
Object.keys(t).forEach(function(k){var p=Math.round(t[k]/qs.length*100),row=res.querySelector('[data-k="'+k+'"]');row.querySelector('b').textContent=p+'%';row.querySelector('i').style.setProperty('--p',p+'%')});
var s=res.querySelector('[data-style]');if(s)s.value=R[top][1];qs.forEach(function(q){q.hidden=true});i=qs.length;bar.style.width='100%';
prog.textContent='Done. Your result is ready.';btn.textContent='Start Again';res.setAttribute('tabindex','-1');res.focus()});show()})();
</script>"""


@S("quiz", """
.qz-g{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,4vw,48px);align-items:start}
.qz .pg{height:8px;border-radius:9px;background:var(--line);margin:.6rem 0 1.4rem;overflow:hidden}.qz .pg i{display:block;height:100%;width:0;border-radius:9px;background:var(--accent);transition:width .3s}
.qz fieldset{border:0;margin-bottom:1.6rem}.qz.live fieldset{margin-bottom:0}.qz:not(.live) [data-next]{display:none}.qz legend{font-family:var(--fd);font-weight:var(--hw);font-size:1.5rem;line-height:1.15;letter-spacing:var(--hls);text-transform:var(--htt);margin-bottom:1rem}
.qz label{display:flex;gap:.8rem;align-items:center;min-height:54px;padding:.7rem 1rem;border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),14px);margin-top:.6rem;cursor:pointer;background:var(--bg)}
.qz input{width:20px;height:20px;accent-color:var(--accent)}.qz label:has(input:checked){border-color:var(--accent-t);outline:2px solid var(--accent-t)}
.qz .btn{margin-top:1.2rem}
.rs h3{font-size:1.6rem;margin:.4rem 0 .6rem}.rs .b{margin-top:1rem}.rs .b span{display:flex;justify-content:space-between;font-size:.88rem;font-weight:600}
.rs .b i{display:block;height:10px;border-radius:9px;background:var(--line);margin-top:.3rem;position:relative;overflow:hidden}.rs .b i::after{content:"";position:absolute;inset:0;width:var(--p);background:var(--accent-t);border-radius:9px}
.gate{margin-top:1.6rem;padding-top:1.3rem;border-top:1px dashed var(--line)}.gate label{display:block;font-weight:700;font-size:.95rem;margin-bottom:.5rem}
.gate div{display:flex;flex-wrap:wrap;gap:.5rem}.gate input{flex:1;min-width:170px;min-height:50px;padding:0 1rem;border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),12px);background:var(--bg);color:var(--ink);font:inherit}
.gate .btn{min-height:50px;padding:.6em 1.2em}.gate .fine{margin-top:.7rem}
@media(max-width:800px){.qz-g{grid-template-columns:1fr}}
""")
def quiz(d, P):
    r = d["result"]
    styles = d["styles"]
    qs = ""
    for n, (text, opts) in enumerate(d["questions"]):
        o = "".join(f'<label><input type="radio" name="q{n + 1}" value="{k}"> {e(t)}</label>' for k, t in opts)
        qs += f'<fieldset data-q><legend>{h(text)}</legend>{o}</fieldset>'
    top = max(r["bars"], key=lambda x: x[1])[0]
    bars = "".join(f'<div class="b" data-k="{k}"><span>{e(lab)}<b>{dict(r["bars"])[lab]}%</b></span><i style="--p:{dict(r["bars"])[lab]}%"></i></div>' for k, (lab, _, _) in styles.items())
    gate = ""
    if r.get("gate"):
        g = r["gate"]
        gate = (f'{form_open("quiz-plan", "gate")}<input type="hidden" name="style" value="{e(r["h"])}" data-style><label for="qz-e">{e(g["label"])}</label>'
                f'<div><input id="qz-e" name="email" type="email" placeholder="you@email.com" autocomplete="email" required><button class="btn" type="submit">{e(g["button"])}</button></div>'
                f'<p class="fine">{h(g["skip"])}</p></form>')
    import json
    data = e(json.dumps(styles))
    inner = (f'<div class="qz-g"><div class="card qz formcard" data-quiz data-styles="{data}"><p class="fine" data-progress>{len(d["questions"])} questions. Answer them in order.</p>'
             f'<div class="pg" aria-hidden="true"><i data-bar></i></div>{qs}<p class="fine" data-warn hidden>Pick 1 answer to continue.</p>'
             f'<button class="btn" type="button" data-next>See The 4 Styles Below</button></div>'
             f'<div class="card rs" data-result>{eyebrow(r["eyebrow"]).replace("<p ", "<p data-eyebrow ")}<h3 data-title>{h(r["h"])}</h3><p data-text>{h(r["text"])}</p>{bars}{gate}</div></div>')
    return sec("quiz", d, sh(d) + inner + QUIZ_JS)


@S("thanks", """
.thx .wrap{max-width:780px;text-align:center}.thx h1{font-size:clamp(2.2rem,5.4vw,3.8rem)}.thx .lead{margin:1.2rem auto 0}
.thx ol{counter-reset:t;text-align:left;margin-top:2.4rem;display:grid;gap:1rem}
.thx li{counter-increment:t;display:grid;grid-template-columns:auto 1fr;gap:1.1rem;align-items:start}
.thx li::before{content:counter(t);width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;font-weight:700}
.thx li h2{font-size:1.28rem;line-height:1.2}.thx .acts{justify-content:center}
""")
def thanks(d, P):
    it = "".join(f'<li class="card" style="padding:1.2rem 1.4rem"><div><h2>{h(a)}</h2><p>{h(b)}</p></div></li>' for a, b in d["steps"])
    steps = f"<ol>{it}</ol>" if it else ""
    return sec("thx", d, f'{eyebrow(d.get("eyebrow"))}<h1>{h(d["h"])}</h1><p class="lead">{h(d["text"])}</p>{kit.host()}{steps}{acts(d).replace(" data-in", "")}')


@S("bios", """
.bio{position:relative}.bio .tag{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t);display:block;margin-bottom:.7rem}
.bio p{font-size:1.02rem}
""")
def bios(d, P):
    it = "".join(f'<div class="card bio"><span class="tag">{e(a)}</span><p>{h(b)}</p></div>' for a, b in d["items"])
    return sec("bios", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 2)}">{it}</div>' + acts(d).replace(" data-in", ""))


@S("legal", """
.legal .wrap{max-width:780px}.legal .lh{font-size:clamp(2.1rem,5vw,3.4rem);margin:0}.legal .lead{margin-top:1rem}
.legal h2{font-size:1.4rem;margin:2.2rem 0 .6rem}.legal p,.legal li{font-size:1.06rem;line-height:1.7}
.legal .ticks{margin-top:.6rem}
.tpl{margin:1.8rem 0;background:var(--bg2);box-shadow:none;border-left:4px solid var(--accent-t);font-size:.96rem}
.facts{width:100%;border-collapse:collapse;margin-top:1rem}.facts th,.facts td{text-align:left;padding:.8rem .2rem;border-bottom:max(1px,var(--bw)) solid var(--line);vertical-align:top}
.facts th{width:34%;font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink2)}
""")
def legal(d, P):
    tag = "h2" if d.get("sub") else "h1"
    out = f'{eyebrow(d.get("eyebrow"))}<{tag} class="lh">{h(d["h"])}</{tag}>'
    if d.get("lead"):
        out += f'<p class="lead">{h(d["lead"])}</p>'
    if d.get("tpl"):
        out += f'<aside class="card tpl"><p>{h(d["tpl"])}</p></aside>'
    for b in d["blocks"]:
        if b[0] == "h2":
            out += f"<h2>{h(b[1])}</h2>"
        elif b[0] == "p":
            out += f"<p>{h(b[1])}</p>"
        elif b[0] == "list":
            out += ul(b[1])
        elif b[0] == "facts":
            out += '<table class="facts"><tbody>' + "".join(f'<tr><th scope="row">{e(a)}</th><td>{h(v)}</td></tr>' for a, v in b[1]) + "</tbody></table>"
    return sec("legal", d, out + acts(d).replace(" data-in", ""))


# ---------- PICTURE BAND ----------

SPOTS = [("18% 42%", 2.3), ("50% 30%", 2.7), ("82% 46%", 2.3), ("34% 82%", 2.5), ("68% 78%", 2.5), ("50% 62%", 1.7)]


def crop(i, ar):
    """A piece of the site's painting, by number. Decoration, so it carries no alt text."""
    pos, zoom = SPOTS[i % len(SPOTS)]
    return f'<div class="ph art" style="--ar:{ar};--pos:{pos};--zoom:{zoom}"><img {kit.SRCSET} alt="" loading="lazy" decoding="async"></div>'


@S("band", """
.band{position:relative;isolation:isolate;overflow:clip}
.bd-h{font-size:clamp(1.9rem,calc(4.2vw*var(--hs)),calc(3.5rem*var(--hs)));max-width:19ch}.band .eyebrow{margin-bottom:1.1rem}
.band.wide{padding-block:clamp(84px,11vw,160px)}.band.wide::before{background:linear-gradient(90deg,rgba(6,10,22,.84),rgba(6,10,22,.62) 52%,rgba(6,10,22,.2))}
.band.wide picture.art img,.band.frame picture.art img{object-position:50% 46%}
.band.frame{margin:clamp(12px,2.2vw,30px);border-radius:clamp(22px,3vw,44px);padding-block:clamp(72px,9vw,128px);text-align:center}
.band.frame::before{background:linear-gradient(180deg,rgba(6,10,22,.7),rgba(6,10,22,.62))}.band.frame .bd-h{margin-inline:auto}.band.frame .acts{justify-content:center}
.band.frame .eyebrow::before{display:none}
.band.mosaic .wrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(28px,6vw,84px);align-items:center}
.mos{display:grid;grid-template-columns:1.15fr .85fr;grid-template-rows:1fr 1fr;gap:clamp(10px,1.4vw,18px);aspect-ratio:5/4}
.mos .ph{aspect-ratio:auto;height:100%;box-shadow:0 30px 56px -34px color-mix(in srgb,var(--ink) 60%,transparent)}.mos .ph:first-child{grid-row:span 2}
.mos .ph:nth-child(2){translate:0 clamp(-26px,-2vw,-10px)}.mos .ph:nth-child(3){translate:clamp(10px,2vw,26px) 0}
.band.strip{padding-bottom:0}.band.strip .bd-c{text-align:center;display:grid;justify-items:center}.band.strip .eyebrow::before{display:none}
.strip-w{margin-top:clamp(36px,5vw,64px);overflow:hidden;display:flex;justify-content:center;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.strip-t{display:flex;gap:clamp(10px,1.4vw,18px);width:max-content;padding-bottom:clamp(40px,5vw,72px)}
.strip-t .ph{width:clamp(180px,22vw,300px);flex:none}.strip-t .ph:nth-child(even){margin-top:clamp(16px,2.4vw,36px)}
@media(max-width:860px){.band.mosaic .wrap{grid-template-columns:1fr}.mos{aspect-ratio:4/3}.mos .ph:nth-child(n){translate:none}}
""")
def band(d, P):
    k = d["kind"]
    inner = f'<div class="bd-c">{eyebrow(d.get("eyebrow"))}<h2 class="bd-h">{h(d["h"])}</h2>{acts(d).replace(" data-in", "")}</div>'
    if k in ("wide", "frame"):
        return sec(f"band {k} bleed t-light", d, inner, pre=backdrop())
    if k == "mosaic":
        pics = crop(0, "3/4") + crop(2, "4/3") + crop(4, "4/3")
        return sec("band mosaic alt", d, f'{inner}<div class="mos" aria-hidden="true">{pics}</div>')
    row = "".join(crop(i, "4/5" if i % 2 else "1/1") for i in range(6))
    return f'<section class="sec band strip"><div class="wrap">{inner}</div><div class="strip-w" aria-hidden="true"><div class="strip-t">{row}</div></div></section>'
