"""Section components. Each takes a dict of content and returns HTML. Mix and reorder them to make a page."""
import re

from kit import S, e, h, eyebrow, btn, acts, sh, ul, paras, sec, vis


def form(f, cls="card formcard"):
    """A visual-only form. Connect it to your email or booking tool when you make the page yours."""
    fields = ""
    for i, (label, typ, hint) in enumerate(f.get("fields", [])):
        fid = "f-" + re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-") + f"-{i}"
        if typ == "area":
            ctl = f'<textarea id="{fid}" name="{fid}" placeholder="{e(hint)}"></textarea>'
        elif typ == "select":
            ctl = f'<select id="{fid}" name="{fid}">' + "".join(f"<option>{e(o)}</option>" for o in hint) + "</select>"
        else:
            ctl = f'<input id="{fid}" name="{fid}" type="{typ}" placeholder="{e(hint)}" autocomplete="off">'
        fields += f'<div class="field"><label for="{fid}">{e(label)}</label>{ctl}</div>'
    title = f'<h3>{h(f["title"])}</h3>' if f.get("title") else ""
    text = f'<p class="fine" style="text-align:left;margin-top:.4rem">{h(f["text"])}</p>' if f.get("text") else ""
    note = f'<p class="fine">{h(f["note"])}</p>' if f.get("note") else ""
    return (f'<form class="{cls}" action="#" method="get" onsubmit="return false"><!-- Visual only: connect to your own tool -->{title}{text}{fields}'
            f'<button class="btn" type="submit">{e(f.get("button", "Send"))}</button>{note}</form>')


# ---------- HEROES ----------

@S("hero_split", """
.hs-g{display:grid;grid-template-columns:1.08fr .92fr;gap:clamp(28px,5vw,76px);align-items:center}
.hero{padding-block:clamp(40px,6vw,88px) clamp(56px,8vw,104px)}
.hero .lead{margin-top:1.4rem}.hero .ticks{margin-top:1.2rem}
.hs-v{position:relative}.float{position:absolute;left:-9%;bottom:26%;max-width:230px;padding:16px 18px;font-size:.9rem;line-height:1.4;z-index:3}
.float b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:1.7rem;line-height:1;letter-spacing:var(--hls)}
@media(max-width:860px){.hs-g{grid-template-columns:1fr}.hs-v{max-width:430px}.float{left:auto;right:-4px}}
""")
def hero_split(d, P):
    fl = d.get("float")
    flo = f'<div class="card float"><b>{e(fl[0])}</b>{e(fl[1])}</div>' if fl else ""
    proof = f'<p class="proof" data-in style="--i:4">{h(d["proof"])}</p>' if d.get("proof") else ""
    flip = ' style="order:-1"' if d.get("flip") else ""
    inner = (f'<div class="hs-g"><div class="hs-c">{eyebrow(d.get("eyebrow"))}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{ul(d.get("bullets"))}{acts(d)}{proof}</div>'
             f'<div class="hs-v" data-in style="--i:2"{flip}>{vis(d.get("visual"))}{flo}</div></div>')
    return sec("hero hsplit", d, inner)


@S("hero_center", """
.hero{padding-block:clamp(40px,6vw,88px) clamp(56px,8vw,104px)}
.hcenter .wrap{text-align:center}.hcenter h1{max-width:17ch;margin-inline:auto}.hcenter .lead{margin:1.4rem auto 0}
.hcenter .acts{justify-content:center}.hc-u{margin-top:clamp(36px,5vw,64px)}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.6rem}
.chips li{border:max(1px,var(--bw)) solid var(--line);border-radius:999px;padding:.35em .9em;font-size:.86rem;background:var(--card)}
""")
def hero_center(d, P):
    chips = ('<ul class="chips">' + "".join(f"<li>{e(c)}</li>" for c in d["chips"]) + "</ul>") if d.get("chips") else ""
    proof = f'<p class="proof" data-in style="--i:4">{h(d["proof"])}</p>' if d.get("proof") else ""
    under = f'<div class="hc-u" data-in style="--i:4">{vis(d["under"])}</div>' if d.get("under") else ""
    inner = (f'{eyebrow(d.get("eyebrow"))}<h1 data-in style="--i:1">{h(d["h"])}</h1><p class="lead" data-in style="--i:2">{h(d["sub"])}</p>'
             f'{acts(d)}{chips}{proof}{under}')
    return sec("hero hcenter", d, inner)


@S("hero_form", """
.hero{padding-block:clamp(40px,6vw,88px) clamp(56px,8vw,104px)}
.hf-g{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);align-items:center}
.hero .lead{margin-top:1.4rem}.hero .ticks{margin-top:1.4rem}
.meta{display:flex;flex-wrap:wrap;gap:.6rem 2rem;margin-top:1.6rem;padding-top:1.2rem;border-top:max(1px,var(--bw)) solid var(--line)}
.meta dt{font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}.meta dd{font-weight:700}
.hf-v{display:grid;gap:1.4rem}
.cal-m{font-weight:700;margin-bottom:.7rem}.cal-g{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:1.2rem}
.cal-g span{aspect-ratio:1;display:grid;place-items:center;border-radius:50%;font-size:.86rem;color:var(--ink2)}
.cal-g .on{background:var(--bg2);color:var(--ink);font-weight:700}.cal-g .pick,.cal-s .pick{background:var(--accent);color:var(--accent-ink)}
.cal-s{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:1rem}.cal-s .slot{border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),12px);text-align:center;padding:.65rem .3rem;font-weight:600;font-size:.92rem}
@media(max-width:860px){.hf-g{grid-template-columns:1fr}}
""")
def hero_form(d, P):
    meta = ""
    if d.get("meta"):
        meta = '<dl class="meta">' + "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in d["meta"]) + "</dl>"
    inner = (f'<div class="hf-g"><div>{eyebrow(d.get("eyebrow"))}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{ul(d.get("bullets"))}{meta}'
             f'{("<p class=proof>" + h(d["proof"]) + "</p>") if d.get("proof") else ""}</div>'
             f'<div class="hf-v" data-in style="--i:3">{vis(d.get("visual"))}{form(d["form"]) if d.get("form") else ""}</div></div>')
    return sec("hero hform", d, inner)


@S("hero_stage", """
.hero{padding-block:clamp(40px,6vw,88px) clamp(56px,8vw,104px)}
.hstage h1{font-size:clamp(3.2rem,calc(9.5vw*var(--hs)),calc(7.4rem*var(--hs)));max-width:13ch}
.hstage .lead{margin-top:1.6rem}
.hst-g{display:grid;grid-template-columns:1.25fr .75fr;gap:clamp(28px,5vw,64px);align-items:end}
.hstats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1.4rem 2.4rem;margin-top:clamp(40px,6vw,72px);padding-top:1.6rem;border-top:max(1px,var(--bw)) solid var(--line)}
.hstats b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.2rem,4.5vw,3.4rem);line-height:1;color:var(--accent-t);letter-spacing:var(--hls)}
.hstats span{font-size:.9rem;color:var(--ink2)}
@media(max-width:860px){.hst-g{grid-template-columns:1fr}.hst-g>div:last-child{max-width:360px}}
""")
def hero_stage(d, P):
    stats = ""
    if d.get("stats"):
        stats = '<div class="hstats">' + "".join(f"<div><b>{e(n)}</b><span>{e(l)}</span></div>" for n, l in d["stats"]) + "</div>"
    v = f'<div data-in style="--i:3">{vis(d["visual"])}</div>' if d.get("visual") else "<div></div>"
    inner = (f'<div class="hst-g"><div>{eyebrow(d.get("eyebrow"))}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["sub"])}</p>{acts(d)}</div>{v}</div>{stats}')
    return sec("hero hstage", d, inner)


@S("hero_article", """
.hart{padding-block:clamp(36px,5vw,72px) 0}
.hart .wrap{max-width:900px}.hart h1{font-size:clamp(2.2rem,calc(5vw*var(--hs)),calc(3.9rem*var(--hs)))}
.hart .lead{margin-top:1.3rem;max-width:none}
.byline{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1.2rem;margin-top:1.8rem;padding-block:1rem;border-block:max(1px,var(--bw)) solid var(--line);font-size:.9rem}
.byline b{font-weight:700}.byline .dot{width:44px;height:44px;border-radius:50%;background:radial-gradient(circle at 30% 30%,var(--ph1),var(--ph2))}
.hart .ph{margin-top:clamp(28px,4vw,48px)}
""")
def hero_article(d, P):
    by = (f'<div class="byline"><span class="dot" aria-hidden="true"></span><span>By <b>{e(d["author"])}</b>, {e(d["role"])}</span>'
          f'<span>Published <time datetime="{e(d["iso"])}">{e(d["date"])}</time></span><span>{e(d["read"])}</span></div>')
    v = vis(d["visual"]) if d.get("visual") else ""
    inner = (f'{eyebrow(d.get("kicker"))}<h1 data-in style="--i:1">{h(d["h"])}</h1>'
             f'<p class="lead" data-in style="--i:2">{h(d["standfirst"])}</p>{by}{v}')
    return sec("hart", d, inner)


@S("bento", """
.bento{padding-block:clamp(24px,3vw,40px) clamp(48px,6vw,80px)}
.bn{display:grid;grid-template-columns:repeat(6,1fr);gap:clamp(12px,1.6vw,18px)}
.tile{border-radius:var(--r);background:var(--card);padding:clamp(20px,2.6vw,32px);border:var(--bw) solid var(--line);box-shadow:var(--shadow);display:flex;flex-direction:column;gap:.7rem;min-height:190px}
.tile.w6{grid-column:span 6}.tile.w4{grid-column:span 4}.tile.w3{grid-column:span 3}.tile.w2{grid-column:span 2}
.tile.t1{background:var(--t1,var(--bg2))}.tile.t2{background:var(--t2,var(--bg2))}.tile.t3{background:var(--t3,var(--bg2))}
.tile.dk{background:var(--dark);color:var(--dark-ink);--ink:var(--dark-ink);--ink2:color-mix(in srgb,var(--dark-ink) 76%,var(--dark));--accent-t:var(--dark-accent);--line:color-mix(in srgb,var(--dark-ink) 22%,var(--dark))}
.tile h1{font-size:clamp(2.2rem,5.2vw,4.2rem)}.tile .big{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.6rem,5vw,4rem);line-height:.95;letter-spacing:var(--hls)}
.tile .eyebrow{margin-bottom:0}.tile .btn{align-self:flex-start;margin-top:auto}.tile .ph{flex:1;min-height:200px;aspect-ratio:auto}
.tile li{display:flex;justify-content:space-between;gap:1rem;padding:.65rem 0;border-top:1px solid var(--line);font-size:.96rem}.tile li span{color:var(--ink2);white-space:nowrap;font-size:.85rem}
.tile .q{font-family:var(--fd);font-weight:var(--hw);font-size:1.35rem;line-height:1.2;letter-spacing:var(--hls)}
.tile .inl{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto}.tile .inl input{flex:1;min-width:150px;min-height:50px;border-radius:var(--rb);border:1px solid var(--line);padding:0 1.1rem;font:inherit;background:var(--bg)}
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
                f'<li><a href="#" class="link" style="text-decoration:none">{e(a)}</a><span>{e(b)}</span></li>' for a, b in t["items"]) + "</ul>"
        elif k == "form":
            body += (f'<h2 style="font-size:1.7rem">{h(t["h"])}</h2><p>{h(t["text"])}</p>'
                     f'<form class="inl" action="#" method="get" onsubmit="return false"><label class="skip" for="bn{i}">Email</label>'
                     f'<input id="bn{i}" type="email" placeholder="you@email.com"><button class="btn" type="submit">{e(t["button"])}</button></form>'
                     f'<p class="fine">{h(t.get("note", ""))}</p>')
        elif k == "quote":
            body += f'<p class="q">{h(t["q"])}</p><p class="fine">{e(t["by"])}</p>'
        elif k == "ph":
            body += vis(t["visual"])
        else:
            body += f'<h2 style="font-size:1.5rem">{h(t["h"])}</h2><p>{h(t["text"])}</p>{btn(t.get("cta"), "ghost")}'
        out += f'<div class="{cls}" data-in style="--i:{i}">{body}</div>'
    return sec("bento", d, f'<div class="bn">{out}</div>')


@S("linkbio", """
.lb{padding-block:clamp(28px,5vw,56px)}.lb .wrap{max-width:520px;text-align:center}
.lb .ph{width:112px;margin:0 auto 1rem;border-radius:50%;--ar:1/1}.lb .ph span{display:none}
.lb h1{font-size:clamp(1.9rem,6vw,2.5rem)}.lb .lead{margin:.7rem auto 0;font-size:1.05rem}
.lb-f{margin-top:1.8rem;text-align:left}.lb-f h2{font-size:1.45rem;margin:.3rem 0 .5rem}.lb-f .btn{width:100%;margin-top:1rem}
.lb-l{margin-top:1.1rem;display:grid;gap:.75rem}
.lb-l a{display:flex;align-items:center;justify-content:space-between;gap:1rem;text-align:left;text-decoration:none;min-height:64px;padding:.8rem 1.2rem;border-radius:var(--r);background:var(--card);border:var(--bw) solid var(--line);box-shadow:var(--shadow);font-weight:700}
.lb-l small{display:block;font-weight:400;color:var(--ink2);font-size:.84rem}.lb-l i{font-style:normal;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:var(--bg2);border-radius:999px;padding:.3em .7em;white-space:nowrap}
.lb-s{display:flex;justify-content:center;flex-wrap:wrap;gap:.4rem 1.2rem;margin-top:1.8rem;font-size:.9rem}
""")
def linkbio(d, P):
    f = d["feature"]
    links = "".join(
        f'<a href="#"><span>{e(a)}<small>{e(b)}</small></span>{("<i>" + e(t) + "</i>") if t else ""}</a>' for a, b, t in d["links"])
    soc = "".join(f'<a href="#">{e(s)}</a>' for s in d["socials"])
    inner = (f'{vis({"kind": "person", "label": d["photo"], "ar": "1/1"})}<h1>{h(d["h"])}</h1><p class="lead">{h(d["sub"])}</p>'
             f'<div class="card lb-f">{eyebrow(f["eyebrow"])}<h2>{h(f["h"])}</h2><p>{h(f["text"])}</p>{btn(f["cta"])}</div>'
             f'<nav class="lb-l" aria-label="Main links">{links}</nav><nav class="lb-s" aria-label="Social profiles">{soc}</nav>')
    return sec("lb", d, inner)


# ---------- PROOF ----------

@S("logos", """
.logos{padding-block:clamp(26px,3.5vw,44px);border-block:max(1px,var(--bw)) solid var(--line)}
.logos .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:1rem 2.6rem;justify-content:center}
.logos p{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink2)}
.logos ul{display:flex;flex-wrap:wrap;gap:.8rem 2.4rem;justify-content:center}
.logos li{font-family:var(--fd);font-weight:var(--hw);font-size:1.25rem;letter-spacing:var(--hls);text-transform:var(--htt);opacity:.72}
.logos li:nth-child(even){font-family:var(--fb);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.95rem}
""")
def logos(d, P):
    return sec("logos", d, f'<p>{e(d["label"])}</p><ul>' + "".join(f"<li>{e(x)}</li>" for x in d["items"]) + "</ul>")


@S("stats", """
.st-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:2rem 3rem}
.st-g b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.6rem,5.4vw,4.2rem);line-height:1;letter-spacing:var(--hls);color:var(--accent-t)}
.st-g span{display:block;margin-top:.5rem;color:var(--ink2);max-width:24ch}
""")
def stats(d, P):
    g = '<div class="st-g">' + "".join(f"<div><b>{e(n)}</b><span>{h(l)}</span></div>" for n, l in d["items"]) + "</div>"
    note = f'<p class="fine" style="margin-top:2rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("stats", d, sh(d) + g + note)


@S("quotes", """
.qt blockquote{font-size:1.06rem;line-height:1.55}.qt .feature blockquote{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.5rem,3vw,2.3rem);line-height:1.18;letter-spacing:var(--hls);text-transform:var(--htt);max-width:26ch}
.qt figcaption{margin-top:1.1rem;font-size:.9rem;color:var(--ink2)}.qt figcaption b{color:var(--ink);display:block}
.res{display:inline-block;margin-bottom:.9rem;font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-t);border:max(1px,var(--bw)) solid currentColor;border-radius:999px;padding:.3em .8em}
.qt .wall{columns:3 260px;column-gap:clamp(16px,2.4vw,28px)}.qt .wall figure{break-inside:avoid;margin-bottom:clamp(16px,2.4vw,28px)}
.qt .feature{display:grid;grid-template-columns:.8fr 1.2fr;gap:clamp(28px,5vw,64px);align-items:center}
@media(max-width:760px){.qt .feature{grid-template-columns:1fr}.qt .feature .ph{max-width:300px}}
""")
def quotes(d, P):
    def fig(q, cls="card"):
        res = f'<span class="res">{e(q["result"])}</span>' if q.get("result") else ""
        return (f'<figure class="{cls}">{res}<blockquote><p>{h(q["q"])}</p></blockquote>'
                f'<figcaption><b>{e(q["name"])}</b>{e(q["role"])}</figcaption></figure>')
    v = d.get("variant", "grid")
    if v == "feature":
        q = d["items"][0]
        body = f'<div class="feature">{vis(d.get("visual"))}{fig(q, "")}</div>'
    elif v == "wall":
        body = '<div class="wall">' + "".join(fig(q) for q in d["items"]) + "</div>"
    else:
        body = f'<div class="grid" style="--cols:{d.get("cols", 3)}">' + "".join(fig(q) for q in d["items"]) + "</div>"
    note = f'<p class="fine" style="margin-top:1.8rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("qt", d, sh(d) + body + note)


@S("metrics", """
.mt{width:100%;border-collapse:collapse;font-size:1rem}
.mt th,.mt td{text-align:left;padding:1rem .8rem;border-bottom:max(1px,var(--bw)) solid var(--line)}
.mt thead th{font:600 .76rem/1.3 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}
.mt td:last-child{font-family:var(--fd);font-weight:var(--hw);font-size:1.5rem;color:var(--accent-t);letter-spacing:var(--hls)}
@media(max-width:600px){.mt thead{display:none}.mt tr{display:block;padding:.8rem 0;border-bottom:max(1px,var(--bw)) solid var(--line)}.mt th,.mt td{display:block;border:0;padding:.15rem 0}.mt td::before{content:attr(data-l) ": ";font-size:.78rem;color:var(--ink2);font-family:var(--fb)}}
""")
def metrics(d, P):
    rows = "".join(f'<tr><th scope="row">{e(a)}</th><td data-l="Before">{e(b)}</td><td data-l="After">{e(c)}</td></tr>' for a, b, c in d["items"])
    t = (f'<table class="mt"><thead><tr><th scope="col">Measure</th><th scope="col">{e(d.get("before", "Before"))}</th>'
         f'<th scope="col">{e(d.get("after", "After"))}</th></tr></thead><tbody>{rows}</tbody></table>')
    note = f'<p class="fine" style="margin-top:1.4rem">{h(d["note"])}</p>' if d.get("note") else ""
    return sec("metrics", d, sh(d) + t + note)


# ---------- CONTENT ----------

@S("doors", """
.door{display:flex;flex-direction:column;gap:.8rem;text-decoration:none;min-height:240px}
.door .tag{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.door h3{font-size:1.6rem}.door .go{margin-top:auto;font-weight:700;text-decoration:underline;text-underline-offset:.3em}
.door:hover{translate:0 -3px}
""")
def doors(d, P):
    it = "".join(
        f'<a class="card door" href="{e(x.get("href", "#"))}"><span class="tag">{e(x["tag"])}</span><h3>{h(x["h"])}</h3>'
        f'<p>{h(x["text"])}</p><span class="go">{e(x["go"])}</span></a>' for x in d["items"])
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
.cards .card h3{margin-bottom:.6rem}.cards .n{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:2.2rem;line-height:1;color:var(--accent-t);margin-bottom:1rem;letter-spacing:var(--hls)}
.cards .card p{color:var(--ink2)}
""")
def cards(d, P):
    it = "".join(
        f'<div class="card">{("<span class=n>" + str(i + 1).zfill(2) + "</span>") if d.get("num") else ""}<h3>{h(a)}</h3><p>{h(b)}</p></div>'
        for i, (a, b) in enumerate(d["items"]))
    return sec("cards", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 3)}">{it}</div>' + acts(d).replace(" data-in", ""))


@S("steps", """
.stp{counter-reset:s;display:grid;gap:0}
.stp li{counter-increment:s;display:grid;grid-template-columns:auto 1fr;gap:clamp(16px,3vw,40px);padding:clamp(20px,3vw,34px) 0;border-top:max(1px,var(--bw)) solid var(--line)}
.stp li::before{content:counter(s,decimal-leading-zero);font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2rem,4.5vw,3.4rem);line-height:.95;color:var(--accent-t);min-width:1.6em;letter-spacing:var(--hls)}
.stp h3{font-size:1.5rem;margin-bottom:.4rem}.stp p{color:var(--ink2);max-width:60ch}
""")
def steps(d, P):
    it = "".join(f"<li><div><h3>{h(a)}</h3><p>{h(b)}</p></div></li>" for a, b in d["items"])
    return sec("steps", d, sh(d) + f'<ol class="stp">{it}</ol>')


@S("split", """
.sp-g{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(28px,6vw,84px);align-items:center}
.sp-g h2{margin-bottom:1.2rem}.sp-g .ticks{margin-top:1.2rem}
.split.flip .sp-v{order:2}
@media(max-width:860px){.sp-g{grid-template-columns:1fr}.sp-v{max-width:420px}.split.flip .sp-v{order:0}}
""")
def split(d, P):
    inner = (f'<div class="sp-g"><div class="sp-v">{vis(d.get("visual"))}</div><div>{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2>'
             f'{paras(d.get("paras"))}{ul(d.get("bullets"))}{acts(d).replace(" data-in", "")}</div></div>')
    return sec("split", d, inner, "flip" if d.get("flip") else "")


@S("compare", """
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:clamp(16px,2.4vw,28px)}
.cmp h3{margin-bottom:.8rem;font-size:1.45rem}.cmp .no li::before{border:0;content:"\\00d7";top:-.1em;rotate:0deg;font-weight:700;color:var(--ink2);width:auto;height:auto;font-size:1.2em}
.cmp .no{background:transparent;box-shadow:none}
@media(max-width:700px){.cmp{grid-template-columns:1fr}}
""")
def compare(d, P):
    l, r = d["left"], d["right"]
    inner = (f'<div class="cmp"><div class="card no"><h3>{h(l[0])}</h3>{ul(l[1])}</div>'
             f'<div class="card"><h3>{h(r[0])}</h3>{ul(r[1])}</div></div>')
    return sec("compare", d, sh(d) + inner)


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
    return sec("mod", d, sh(d) + it + note)


@S("pricing", """
.pr-a{margin-bottom:2rem;font-size:1.05rem;max-width:62ch}
.tier{display:flex;flex-direction:column;position:relative}.tier .nm{font-size:.82rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2)}
.tier .pc{font-family:var(--fd);font-weight:var(--hw);font-size:clamp(2.4rem,4.4vw,3.3rem);line-height:1;margin:.8rem 0 .2rem;letter-spacing:var(--hls)}
.tier .pc small{font:400 .95rem var(--fb);color:var(--ink2);letter-spacing:0}
.tier .ticks{margin:1rem 0 1.6rem;font-size:.97rem}.tier .btn{margin-top:auto;width:100%}
.tier.hot{border-color:var(--accent-t);outline:2px solid var(--accent-t);outline-offset:-1px}
.tier .bdg{position:absolute;top:-.85rem;left:1.4rem;background:var(--accent);color:var(--accent-ink);font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.35em .9em;border-radius:999px}
""")
def pricing(d, P):
    it = ""
    for t in d["tiers"]:
        bd = f'<span class="bdg">{e(t["badge"])}</span>' if t.get("badge") else ""
        it += (f'<div class="card tier{" hot" if t.get("hot") else ""}">{bd}<p class="nm">{e(t["name"])}</p>'
               f'<p class="pc">{e(t["price"])} <small>{e(t.get("per", ""))}</small></p><p class="fine">{h(t["desc"])}</p>'
               f'{ul(t["feats"])}{btn(t["cta"], "" if t.get("hot") or len(d["tiers"]) == 1 else "ghost")}</div>')
    anchor = f'<p class="pr-a">{h(d["anchor"])}</p>' if d.get("anchor") else ""
    note = f'<p class="fine" style="margin-top:1.6rem">{h(d["note"])}</p>' if d.get("note") else ""
    cols = len(d["tiers"])
    style = f'--cols:{cols}' + (';max-width:560px' if cols == 1 else '')
    return sec("pricing", d, sh(d) + anchor + f'<div class="grid" style="{style}">{it}</div>' + note)


@S("guarantee", """
.gu .card{display:grid;grid-template-columns:auto 1fr;gap:clamp(18px,3vw,40px);align-items:center;max-width:900px;margin:auto}
.seal{width:clamp(84px,12vw,128px);aspect-ratio:1;border-radius:50%;border:3px double var(--accent-t);display:grid;place-items:center;text-align:center;font:700 .74rem/1.25 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--accent-t);padding:.6rem}
.gu h2{font-size:clamp(1.5rem,2.8vw,2.1rem);margin-bottom:.6rem}
@media(max-width:600px){.gu .card{grid-template-columns:1fr}}
""")
def guarantee(d, P):
    return sec("gu", d, f'<div class="card"><div class="seal" aria-hidden="true">{e(d["seal"])}</div><div><h2>{h(d["h"])}</h2>{paras(d["paras"])}</div></div>')


@S("faq", """
.faq .wrap{max-width:860px}.faq details{border-top:max(1px,var(--bw)) solid var(--line)}.faq details:last-of-type{border-bottom:max(1px,var(--bw)) solid var(--line)}
.faq summary{cursor:pointer;list-style:none;padding:1.2rem 2.2rem 1.2rem 0;position:relative;font-weight:700;font-size:1.08rem}
.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";position:absolute;right:.2rem;top:.9rem;font-size:1.5rem;font-weight:400}
.faq details[open] summary::after{content:"\\2212"}.faq .a{padding:0 0 1.4rem;color:var(--ink2);max-width:66ch}
""")
def faq(d, P):
    it = "".join(f'<details><summary>{h(q)}</summary><div class="a"><p>{h(a)}</p></div></details>' for q, a in d["items"])
    return sec("faq", d, sh(d) + it)


@S("cta", """
.cta .wrap{text-align:center;max-width:880px}.cta h2{font-size:clamp(2.1rem,calc(5vw*var(--hs)),calc(3.8rem*var(--hs)))}
.cta .lead{margin:1.2rem auto 0}.cta .acts{justify-content:center}.cta .fine{margin-top:1.2rem}
""")
def cta(d, P):
    d.setdefault("tone", "dark")
    note = f'<p class="fine">{h(d["note"])}</p>' if d.get("note") else ""
    lead = f'<p class="lead">{h(d["text"])}</p>' if d.get("text") else ""
    return sec("cta", d, f'{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2>{lead}{acts(d).replace(" data-in", "")}{note}')


@S("feed", """
.fd-l li{display:grid;grid-template-columns:minmax(90px,130px) 1fr auto;gap:.6rem 2rem;align-items:baseline;padding:1.25rem 0;border-top:max(1px,var(--bw)) solid var(--line)}
.fd-l li:last-child{border-bottom:max(1px,var(--bw)) solid var(--line)}
.fd-l .k{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.fd-l h3{font-size:clamp(1.15rem,2.2vw,1.5rem)}.fd-l h3 a{text-decoration:none}.fd-l h3 a:hover{text-decoration:underline;text-underline-offset:.2em}
.fd-l p{color:var(--ink2);font-size:.96rem;margin-top:.3rem;max-width:64ch}.fd-l .m{font-size:.85rem;color:var(--ink2);white-space:nowrap}
.fd-g .ph{margin-bottom:1rem;--ar:16/10}.fd-g .k{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.fd-g h3{margin:.4rem 0 .5rem;font-size:1.35rem}.fd-g h3 a{text-decoration:none}.fd-g p{color:var(--ink2);font-size:.96rem}.fd-g .m{margin-top:.7rem;font-size:.84rem}
.fd-more{margin-top:2rem}
@media(max-width:700px){.fd-l li{grid-template-columns:1fr}}
""")
def feed(d, P):
    if d.get("variant") == "grid":
        it = "".join(
            f'<article>{vis({"kind": "scene", "label": x.get("img", "Article image"), "ar": "16/10"})}<span class="k">{e(x["kind"])}</span>'
            f'<h3><a href="#">{h(x["title"])}</a></h3><p>{h(x.get("text", ""))}</p><p class="m fine">{e(x["meta"])}</p></article>'
            for x in d["items"])
        body = f'<div class="grid fd-g" style="--cols:{d.get("cols", 3)}">{it}</div>'
    else:
        it = "".join(
            f'<li><span class="k">{e(x["kind"])}</span><div><h3><a href="#">{h(x["title"])}</a></h3>'
            f'{("<p>" + h(x["text"]) + "</p>") if x.get("text") else ""}</div><span class="m">{e(x["meta"])}</span></li>' for x in d["items"])
        body = f'<ul class="fd-l">{it}</ul>'
    more = f'<p class="fd-more"><a class="link" href="#">{e(d["more"])}</a></p>' if d.get("more") else ""
    return sec("feed", d, sh(d) + body + more)


@S("capture", """
.cap .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,5vw,64px);align-items:center}
.cap h2{font-size:clamp(1.8rem,3.4vw,2.6rem)}.cap p{margin-top:.8rem;color:var(--ink2)}
.cap form{display:flex;flex-wrap:wrap;gap:.6rem}.cap input{flex:1;min-width:200px;min-height:54px;padding:0 1.1rem;border-radius:var(--rb);border:max(1px,var(--bw)) solid var(--line);background:var(--card);color:var(--ink);font:inherit}
.cap .fine{flex-basis:100%}
@media(max-width:800px){.cap .wrap{grid-template-columns:1fr}}
""")
def capture(d, P):
    inner = (f'<div>{eyebrow(d.get("eyebrow"))}<h2>{h(d["h"])}</h2><p>{h(d["text"])}</p></div>'
             f'<form action="#" method="get" onsubmit="return false"><label class="skip" for="cap-e">Email address</label>'
             f'<input id="cap-e" type="email" placeholder="you@email.com"><button class="btn" type="submit">{e(d["button"])}</button>'
             f'<p class="fine">{h(d.get("note", ""))}</p></form>')
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
    return sec("schedule", d, sh(d) + f'<ol class="sch">{it}</ol>')


@S("article", """
.art .wrap{max-width:760px}.art{padding-block:clamp(36px,5vw,64px)}
.art p{font-size:1.16rem;line-height:1.75}.art h2{font-size:clamp(1.6rem,3vw,2.1rem);margin:2.6rem 0 1rem}
.art .ticks{margin:1.2rem 0;font-size:1.1rem}.art>.wrap>p:first-of-type::first-letter{font-family:var(--fd);font-weight:var(--hw);float:left;font-size:4.4em;line-height:.82;padding:.06em .1em 0 0;color:var(--accent-t)}
.pull{margin-block:2.2rem;padding-left:1.4rem;border-left:4px solid var(--accent-t);font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.4rem,2.6vw,1.9rem);line-height:1.22;letter-spacing:var(--hls);text-transform:var(--htt)}
.box{margin:2.4rem 0;background:var(--bg2);box-shadow:none}.box h2{margin:0 0 .6rem;font-size:1.3rem}
.auth{display:grid;grid-template-columns:96px 1fr;gap:1.4rem;align-items:center;margin-top:3rem}.auth .ph{--ar:1/1;border-radius:50%}.auth .ph span{display:none}
.auth h2{margin:0 0 .3rem;font-size:1.3rem}.auth p{font-size:1rem;line-height:1.55}
""")
def article(d, P):
    out = ""
    for b in d["blocks"]:
        k = b[0]
        if k == "p":
            out += f"<p>{h(b[1])}</p>"
        elif k == "h2":
            out += f"<h2>{h(b[1])}</h2>"
        elif k == "quote":
            out += f'<p class="pull">{h(b[1])}</p>'
        elif k == "list":
            out += ul(b[1])
        elif k == "box":
            out += f'<aside class="card box"><h2>{h(b[1])}</h2>{ul(b[2])}</aside>'
    a = d.get("author")
    if a:
        out += (f'<aside class="card auth">{vis({"kind": "person", "label": "Author photo", "ar": "1/1"})}<div><h2>About {e(a["name"])}</h2>'
                f'<p>{h(a["bio"])}</p><p><a class="link" href="#">{e(a["link"])}</a></p></div></aside>')
    return sec("art", d, out)


@S("player", """
.pl{display:grid;grid-template-columns:auto 1fr;gap:clamp(18px,3vw,36px);align-items:center}
.pl .art-c{width:clamp(110px,18vw,190px);aspect-ratio:1;border-radius:var(--r);background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;text-align:center;font-family:var(--fd);font-weight:var(--hw);font-size:clamp(1.1rem,2.4vw,1.8rem);line-height:1;padding:.6rem;text-transform:var(--htt);letter-spacing:var(--hls)}
.pl h2{font-size:clamp(1.5rem,3vw,2.3rem);margin:.3rem 0 .8rem}
.bar{display:flex;align-items:center;gap:1rem;margin-top:.6rem}.bar .pb{width:54px;height:54px;border-radius:50%;background:var(--accent);position:relative;flex:none}
.bar .pb::after{content:"";position:absolute;left:54%;top:50%;translate:-50% -50%;border-left:15px solid var(--accent-ink);border-block:10px solid transparent}
.bar .tr{flex:1;height:6px;border-radius:9px;background:var(--line);position:relative}.bar .tr::after{content:"";position:absolute;inset:0 64% 0 0;border-radius:9px;background:var(--accent-t)}
.pl-n{margin-top:1.6rem;display:flex;flex-wrap:wrap;gap:.6rem}.pl-n a{font-size:.86rem;font-weight:700;border:max(1px,var(--bw)) solid var(--line);border-radius:999px;padding:.5em 1em;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
@media(max-width:600px){.pl{grid-template-columns:1fr}}
""")
def player(d, P):
    apps = "".join(f'<a href="#">{e(a)}</a>' for a in d["apps"])
    inner = (f'<div class="card pl"><div class="art-c" aria-hidden="true">{h(d["art"])}</div><div>{eyebrow(d["eyebrow"])}'
             f'<h2>{h(d["h"])}</h2><p class="fine">{e(d["meta"])}</p>'
             f'<div class="bar" role="img" aria-label="Audio player mock-up"><span class="pb"></span><span class="tr"></span><span class="fine">{e(d["time"])}</span></div>'
             f'<div class="pl-n">{apps}</div></div></div>')
    return sec("player", d, inner)


@S("products", """
.prd{display:flex;flex-direction:column;gap:.5rem}.prd .ph{--ar:4/3;margin-bottom:.8rem}
.prd .k{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t)}
.prd h3{font-size:1.4rem}.prd p{color:var(--ink2);font-size:.96rem}
.prd .row{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:auto;padding-top:1rem}
.prd .pc{font-family:var(--fd);font-weight:var(--hw);font-size:1.7rem;letter-spacing:var(--hls)}.prd .btn{min-height:46px;padding:.6em 1.2em;font-size:.92rem}
""")
def products(d, P):
    it = "".join(
        f'<article class="card prd">{vis({"kind": "scene", "label": x["img"], "ar": "4/3"})}<span class="k">{e(x["kind"])}</span>'
        f'<h3>{h(x["name"])}</h3><p>{h(x["text"])}</p><div class="row"><span class="pc">{e(x["price"])}</span>'
        f'<a class="btn" href="#">{e(x.get("go", "Get it"))}</a></div></article>' for x in d["items"])
    return sec("products", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 3)}">{it}</div>')


@S("contact", """
.ct-g{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(28px,5vw,72px);align-items:start}
.ct-d dt{font-size:.76rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);margin-top:1.4rem}
.ct-d dd{font-size:1.1rem;margin-top:.2rem}.ct-d .ph{margin-top:1.8rem;--ar:16/10}
.hrs{width:100%;border-collapse:collapse;margin-top:.5rem}.hrs th,.hrs td{text-align:left;padding:.4rem 0;border-bottom:1px solid var(--line);font-weight:400;font-size:1rem}.hrs td{text-align:right}
@media(max-width:860px){.ct-g{grid-template-columns:1fr}}
""")
def contact(d, P):
    det = "".join(f"<dt>{e(a)}</dt><dd>{h(b)}</dd>" for a, b in d["details"])
    hrs = ""
    if d.get("hours"):
        hrs = '<dt>Opening hours</dt><dd><table class="hrs"><tbody>' + "".join(
            f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in d["hours"]) + "</tbody></table></dd>"
    mp = vis({"kind": "scene", "label": d["map"], "ar": "16/10"}) if d.get("map") else ""
    left = form(d["form"]) if d.get("form") else f'<div>{paras(d.get("paras"))}{ul(d.get("bullets"))}{acts(d).replace(" data-in", "")}</div>'
    inner = f'<div class="ct-g">{left}<dl class="ct-d">{det}{hrs}{mp}</dl></div>'
    return sec("contact", d, sh(d) + inner)


@S("quiz", """
.qz-g{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,4vw,48px);align-items:start}
.qz .pg{height:8px;border-radius:9px;background:var(--line);margin:.6rem 0 1.4rem;position:relative}.qz .pg::after{content:"";position:absolute;inset:0 62% 0 0;border-radius:9px;background:var(--accent)}
.qz fieldset{border:0}.qz legend{font-family:var(--fd);font-weight:var(--hw);font-size:1.5rem;line-height:1.15;letter-spacing:var(--hls);text-transform:var(--htt);margin-bottom:1rem}
.qz label{display:flex;gap:.8rem;align-items:center;min-height:54px;padding:.7rem 1rem;border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),14px);margin-top:.6rem;cursor:pointer;background:var(--bg)}
.qz input{width:20px;height:20px;accent-color:var(--accent)}.qz label:has(input:checked){border-color:var(--accent-t);outline:2px solid var(--accent-t)}
.qz .btn{margin-top:1.2rem}
.rs h3{font-size:1.6rem;margin:.4rem 0 .6rem}.rs .b{margin-top:1rem}.rs .b span{display:flex;justify-content:space-between;font-size:.88rem;font-weight:600}
.rs .b i{display:block;height:10px;border-radius:9px;background:var(--line);margin-top:.3rem;position:relative;overflow:hidden}.rs .b i::after{content:"";position:absolute;inset:0;width:var(--p);background:var(--accent-t);border-radius:9px}
@media(max-width:800px){.qz-g{grid-template-columns:1fr}}
""")
def quiz(d, P):
    opts = "".join(
        f'<label><input type="radio" name="q"{" checked" if i == 1 else ""}> {e(o)}</label>' for i, o in enumerate(d["options"]))
    r = d["result"]
    bars = "".join(f'<div class="b"><span>{e(a)}<b>{p}%</b></span><i style="--p:{p}%"></i></div>' for a, p in r["bars"])
    inner = (f'<div class="qz-g"><form class="card qz" action="#" method="get" onsubmit="return false"><p class="fine">{e(d["progress"])}</p><div class="pg" aria-hidden="true"></div>'
             f'<fieldset><legend>{h(d["q"])}</legend>{opts}</fieldset><button class="btn" type="submit">{e(d["button"])}</button></form>'
             f'<div class="card rs">{eyebrow(r["eyebrow"])}<h3>{h(r["h"])}</h3><p>{h(r["text"])}</p>{bars}</div></div>')
    return sec("quiz", d, sh(d) + inner)


@S("thanks", """
.thx .wrap{max-width:780px;text-align:center}.thx h1{font-size:clamp(2.2rem,5.4vw,3.8rem)}.thx .lead{margin:1.2rem auto 0}
.thx ol{counter-reset:t;text-align:left;margin-top:2.4rem;display:grid;gap:1rem}
.thx li{counter-increment:t;display:grid;grid-template-columns:auto 1fr;gap:1.1rem;align-items:start}
.thx li::before{content:counter(t);width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;font-weight:700}
.thx .acts{justify-content:center}
""")
def thanks(d, P):
    it = "".join(f'<li class="card" style="padding:1.2rem 1.4rem"><div><h3>{h(a)}</h3><p>{h(b)}</p></div></li>' for a, b in d["steps"])
    return sec("thx", d, f'{eyebrow(d.get("eyebrow"))}<h1>{h(d["h"])}</h1><p class="lead">{h(d["text"])}</p><ol>{it}</ol>{acts(d).replace(" data-in", "")}')


@S("bios", """
.bio{position:relative}.bio .tag{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--accent-t);display:block;margin-bottom:.7rem}
.bio p{font-size:1.02rem}
""")
def bios(d, P):
    it = "".join(f'<div class="card bio"><span class="tag">{e(a)}</span><p>{h(b)}</p></div>' for a, b in d["items"])
    return sec("bios", d, sh(d) + f'<div class="grid" style="--cols:{d.get("cols", 2)}">{it}</div>')
