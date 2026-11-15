#!/usr/bin/env python3
"""Build the Authority Builder Design Library.

    python3 src/build.py

Reads every page definition in src/pages, then writes one self-contained sample.html per entry,
a notes page, a notes.md, the gallery index, the research canon page and the README index.
No dependencies beyond Python 3. The files it writes need no build step: open index.html.
"""
import importlib.util
import json
import pathlib
import re
import sys
from urllib.parse import quote

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))

import canon  # noqa: E402
import sections  # noqa: E402,F401  (registers the section renderers)
import shell  # noqa: E402
from kit import BASE_CSS, CSS, REG, e, h  # noqa: E402
from themes import THEMES  # noqa: E402

GROUPS = [
    ("Home Bases", "The pages that say who you are and send each visitor the right way."),
    ("Offer Pages", "The pages that sell. One offer, one action, objections answered in order."),
    ("List Builders And Launches", "The pages that turn attention into an email address, a seat or a booked call."),
    ("Trust And Content", "The pages that prove it, and give Google and AI tools something to quote."),
]

SECTION_NAMES = {
    "hero_split": "Hero: promise beside a portrait", "hero_center": "Hero: centred promise", "hero_form": "Hero: promise beside the form",
    "hero_stage": "Hero: oversized headline with numbers", "hero_article": "Article header with byline and date", "bento": "Bento grid of content tiles",
    "linkbio": "Link-in-bio stack", "logos": "Proof strip", "stats": "Numbers row", "quotes": "Testimonials", "metrics": "Before and after table",
    "doors": "Routing cards", "prose": "Story or letter block", "cards": "Card grid", "steps": "Numbered method", "split": "Image beside text",
    "compare": "Two-column comparison", "modules": "Curriculum accordion", "pricing": "Pricing", "guarantee": "Guarantee", "faq": "Questions and answers",
    "cta": "Closing call to action", "feed": "Content list", "capture": "Email capture band", "schedule": "Agenda or timeline", "article": "Long-form article body",
    "player": "Podcast player", "products": "Product cards", "contact": "Contact form and details", "quiz": "Quiz question and result preview",
    "thanks": "Thank-you confirmation", "bios": "Copy-ready bios",
}

SCHEMA_WHY = {
    "WebSite": "Names the site, so Google can show your brand name above the result instead of a bare web address.",
    "Organization": "States who the business is: name, logo, address and every real profile, tied together in one place.",
    "Person": "States who the founder is and links them to the business. Essential for a personal brand.",
    "ProfilePage": "Marks this as the page that is about a person, which helps Google and AI tools answer \"who is\" questions.",
    "Course": "Describes the course and who provides it. Google retired its course info rich result in June 2025, so this is for clarity, not a visual bonus.",
    "LocalBusiness": "Address, phone, hours and service area in a form Google can read. Must match your Google Business Profile exactly.",
    "Article": "Headline, author and dates. First-hand, bylined content is what gets cited.",
    "BreadcrumbList": "Shows where this page sits in the site, so the result displays a tidy path.",
    "Event": "Name, date and a real location for an in-person event. Check Google's current rules before marking up online-only events.",
    "Product": "Name, price and availability for each thing you sell, matching what the page shows.",
    "PodcastSeries": "Names the show and its host so the podcast is tied to the person and the brand.",
    "Book": "Title, author and format, tying the book to the author's name.",
    "Service": "What you provide, who provides it and where.",
    "ContactPage": "Marks the page as the place to get in touch.",
    "CollectionPage": "Marks the page as a collection of proof, articles or products.",
    "WebPage": "A plain description of the page. Enough when no richer type fits.",
}

SEO_BUILT_IN = [
    "A title that carries the brand name and a description that says who the page is for",
    "1 clear headline (H1) in the HTML itself, with every word of the page readable without JavaScript",
    "Canonical address, Open Graph tags and a share image slot, all pointing at 1 version of the address",
    "Structured data (JSON-LD) that matches the visible text",
    "A trust footer on every page: About, Contact, Privacy, Terms and Refunds",
    "Proof written as real text, so Google and AI tools can read and quote it",
    "Mobile-first layout, tap targets of 48px or more, visible focus states and reduced-motion support",
    "No image weight above the fold, so the main content can load inside Google's 2.5 second target",
]

SEO_SKIP = [
    "No llms.txt file: Google says its Search and AI features do not use it",
    "No FAQ markup chasing a results-page bonus: FAQ rich results stopped appearing on 7 May 2026",
    "No review stars on your own business: Google excludes self-serving reviews",
    "No hidden text, keyword stuffing or pages rewritten into chunks \"for AI\"",
]


# ---------- helpers ----------

def lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


PAIRS = [("ink", "bg"), ("ink2", "bg"), ("ink", "bg2"), ("ink2", "bg2"), ("accent-t", "bg"), ("accent-t", "bg2"), ("accent-t", "card"),
         ("accent-ink", "accent"), ("dark-ink", "dark"), ("dark-accent", "dark"), ("ink", "card"), ("ink2", "card")]


def check_contrast():
    bad = []
    for k, t in THEMES.items():
        for a, b in PAIRS:
            r = ratio(t["v"][a], t["v"][b])
            if r < 4.5:
                bad.append(f"{k}: {a} on {b} = {r:.2f}")
    return bad


def favicon(mono, bg, fg):
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'><rect width='48' height='48' rx='10' fill='{bg}'/>"
           f"<text x='24' y='33' text-anchor='middle' font-family='Georgia,serif' font-size='26' font-weight='700' fill='{fg}'>{mono}</text></svg>")
    return "data:image/svg+xml," + quote(svg, safe="/:=' ")


def jsonld(P):
    b = P["brand"]
    x = P.get("ld", {})
    url = f'https://{b["domain"]}/'
    page = url + P.get("path", "")
    same = [f"https://www.linkedin.com/in/YOUR-HANDLE", "https://www.instagram.com/YOUR-HANDLE", "https://www.youtube.com/@YOUR-HANDLE"]
    g = []
    for t in P["schema"]:
        if t == "WebSite":
            o = {"@type": "WebSite", "@id": url + "#site", "name": b["name"], "url": url}
            if b.get("alt"):
                o["alternateName"] = b["alt"]
        elif t == "Organization":
            o = {"@type": "Organization", "@id": url + "#org", "name": b["name"], "url": url, "logo": url + "icon-512.png", "sameAs": same}
            if b.get("person"):
                o["founder"] = {"@id": url + "#person"}
        elif t == "Person":
            o = {"@type": "Person", "@id": url + "#person", "name": b["person"], "jobTitle": b["role"], "url": url + "about/",
                 "image": url + "images/portrait.jpg", "worksFor": {"@id": url + "#org"}, "sameAs": same}
        elif t == "ProfilePage":
            o = {"@type": "ProfilePage", "url": page, "dateCreated": "2024-03-04", "dateModified": "2026-11-02", "mainEntity": {"@id": url + "#person"}}
        elif t == "Course":
            o = {"@type": "Course", "name": x["course"], "description": P["desc"], "provider": {"@type": "Organization", "name": b["name"], "sameAs": url}}
        elif t == "LocalBusiness":
            o = {"@type": x.get("subtype", "LocalBusiness"), "@id": url + "#business", "name": b["name"], "url": url, "telephone": x["phone"],
                 "priceRange": x.get("price", "$$"), "image": url + "images/shopfront.jpg",
                 "address": {"@type": "PostalAddress", "streetAddress": x["street"], "addressLocality": x["suburb"], "addressRegion": x["state"],
                             "postalCode": x["postcode"], "addressCountry": "AU"},
                 "areaServed": x["area"],
                 "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o1, "closes": c1} for d, o1, c1 in x["hours"]]}
        elif t == "Article":
            o = {"@type": "BlogPosting", "headline": x["headline"], "description": P["desc"], "datePublished": x["published"], "dateModified": x["modified"],
                 "author": {"@type": "Person", "name": b["person"], "url": url + "about/"}, "publisher": {"@type": "Organization", "name": b["name"], "url": url},
                 "image": url + "images/" + P["slug"] + ".jpg", "mainEntityOfPage": page}
        elif t == "BreadcrumbList":
            o = {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": n, "item": url + p} for i, (n, p) in enumerate(x["crumbs"])]}
        elif t == "Event":
            o = {"@type": "Event", "name": x["event"], "startDate": x["start"], "endDate": x["end"], "eventStatus": "https://schema.org/EventScheduled",
                 "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode", "description": P["desc"],
                 "location": {"@type": "Place", "name": x["venue"], "address": {"@type": "PostalAddress", "addressLocality": x["suburb"],
                                                                               "addressRegion": x["state"], "addressCountry": "AU"}},
                 "organizer": {"@type": "Organization", "name": b["name"], "url": url},
                 "offers": {"@type": "Offer", "price": x["price"], "priceCurrency": "AUD", "availability": "https://schema.org/InStock", "url": page}}
        elif t == "Product":
            for n, pr in x["products"]:
                g.append({"@type": "Product", "name": n, "brand": {"@type": "Brand", "name": b["name"]},
                          "offers": {"@type": "Offer", "price": pr, "priceCurrency": "AUD", "availability": "https://schema.org/InStock", "url": page}})
            continue
        elif t == "PodcastSeries":
            o = {"@type": "PodcastSeries", "name": x["show"], "description": P["desc"], "url": page, "author": {"@type": "Person", "name": b["person"]}}
        elif t == "Book":
            o = {"@type": "Book", "name": x["book"], "author": {"@type": "Person", "name": b["person"], "url": url + "about/"},
                 "bookFormat": "https://schema.org/Paperback", "datePublished": x["published"], "url": page}
        elif t == "Service":
            o = {"@type": "Service", "name": x["service"], "provider": {"@type": "Organization", "name": b["name"], "url": url}, "areaServed": x.get("area", "Australia")}
        else:
            o = {"@type": t, "name": P["title"], "url": page, "description": P["desc"]}
        g.append(o)
    return json.dumps({"@context": "https://schema.org", "@graph": g}, indent=1, ensure_ascii=False)


def css_for(P, secs):
    t = THEMES[P["theme"]]
    vars_ = ":root{" + ";".join(f"--{k}:{v}" for k, v in t["v"].items()) + "}"
    used = []
    for name, _ in secs:
        if name not in used:
            used.append(name)
    return vars_ + BASE_CSS + "".join(CSS[n] for n in used) + "\n" + t["css"] + "\n" + P.get("css", "")


def render_sections(P, secs):
    return "\n".join(REG[name](dict(d), P) for name, d in secs)


def sample_html(P, secs=None, title=None, desc=None, path=None, noindex_note=None, back="index.html"):
    secs = secs or P["sections"]
    t = THEMES[P["theme"]]
    v = t["v"]
    b = P["brand"]
    title = title or P["title"]
    desc = desc or P["desc"]
    path = P.get("path", "") if path is None else path
    url = f'https://{b["domain"]}/{path}'
    nav = P.get("nav")
    navhtml = ""
    if nav:
        navhtml = '<nav aria-label="Main"><ul>' + "".join(f'<li><a href="{e(hr)}">{e(l)}</a></li>' for l, hr in nav) + "</ul></nav>"
    hcta = f'<a class="btn" href="{e(P["cta"][1])}">{e(P["cta"][0])}</a>' if P.get("cta") else ""
    flinks = nav or P.get("foot", [("Home", "#top")])
    disc = f'<p>{h(P["disclaimer"])}</p>' if P.get("disclaimer") else ""
    robots = ('<!-- This page is a confirmation step, so it stays out of Google on purpose. Keep this line. -->\n<meta name="robots" content="noindex">'
              if noindex_note else
              '<!-- LIBRARY ONLY: this line keeps the fictional sample out of Google. Delete it when the page is yours. -->\n<meta name="robots" content="noindex">')
    return f"""<!doctype html>
<html lang="en-AU" id="top">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{robots}
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<!-- Swap every {b["domain"]} address below for your real one. Use 1 version of your address everywhere. -->
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(b["name"])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://{b["domain"]}/share/{P["slug"]}.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{v["bg"]}">
<!-- On your site, link a real square PNG icon that is a multiple of 48px, at an address that never changes. -->
<link rel="icon" href="{favicon(b.get("mono", b["name"][0]), v["accent"], v["accent-ink"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{t["fonts"]}" rel="stylesheet">
<script type="application/ld+json">
{jsonld(P)}
</script>
<style>{css_for(P, secs)}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<!-- LIBRARY BAR: delete this block when you make the page yours -->
<div class="libbar"><span><a href="../index.html">&larr; Design Library</a> &nbsp;·&nbsp; Sample {P["num"]}: {e(P["name"])}</span><span>Fictional brand, sample copy &nbsp;·&nbsp; <a href="{back}">Why this page works</a></span></div>
<header class="hd"><a class="logo" href="#top">{e(b["name"])}</a>{navhtml}{hcta}</header>
<main id="main">
{render_sections(P, secs)}
</main>
<footer class="ft"><div class="wrap"><div class="ft-g">
<div><a class="logo" href="#top">{e(b["name"])}</a><p>{h(b.get("line", ""))}</p></div>
<div><h3>Explore</h3><ul>{"".join(f'<li><a href="{e(hr)}">{e(l)}</a></li>' for l, hr in flinks)}</ul></div>
<div><h3>The Fine Print</h3><ul><li><a href="#">About</a></li><li><a href="#">Contact</a></li><li><a href="#">Privacy Policy</a></li><li><a href="#">Terms</a></li><li><a href="#">Refund Policy</a></li></ul></div>
</div><div class="ft-s"><p>{e(b.get("contact", "hello@" + b["domain"]))} &nbsp;·&nbsp; {e(b.get("where", "Australia"))} &nbsp;·&nbsp; ABN 00 000 000 000</p>{disc}
<p>Sample page from the Authority Builder Design Library. {e(b["name"])} is a fictional brand. Every name, price and result here is invented for teaching.</p></div></div></footer>
</body>
</html>
"""


def purposes(P):
    out = []
    for name, d in P["sections"]:
        out.append(d.get("_") or SECTION_NAMES.get(name, name))
    return out


def prompt_for(P):
    t = THEMES[P["theme"]]
    steps = "\n".join(f"{i + 1}. {p}" for i, p in enumerate(purposes(P)))
    rules = "\n".join(f"- {canon.C[k][2]}, {canon.C[k][1]}: {how}" for k, how in P["principles"])
    return f"""Build me a {P["name"].lower()} for my business, modelled on sample {P["num"]} in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
{steps}

DESIGN DIRECTION
{t["label"]}. {t["mood"]}
Fonts: {t["pair"]} from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
{rules}

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data ({", ".join(P["schema"])}) that matches the visible text.
- Canonical tag, Open Graph tags and a share image, all on 1 version of my address.
- A footer linking About, Contact, Privacy, Terms and Refunds.
- No llms.txt, no FAQ rich-result markup, no review stars on my own business, no hidden text.
- No images above the fold heavier than they need to be. Aim for the main content to load in under 2.5 seconds.

HONESTY RULES
- Use only the proof I gave you. Do not invent testimonials, client names, numbers or press.
- Where I have not given you something, leave a clearly marked placeholder.
- No fake countdown timers and no invented scarcity. If I make an income or results claim, add a line that results are not typical.

OUTPUT
1 self-contained HTML file with inline CSS. Australian spelling. No em dashes."""


def notes_md(P):
    t = THEMES[P["theme"]]
    L = [f"# {P['num']} · {P['name']}", "", f"**Group:** {P['group']}  ", f"**For:** {', '.join(P['aud'])}  ",
         f"**Style:** {t['label']} ({t['pair']})  ", f"**Sample brand:** {P['brand']['name']} (fictional)", "", P["blurb"], "",
         "## Why This Page Works", ""]
    L += [f"- {w}" for w in P["why"]]
    L += ["", "## The Psychology At Work", "", "| Principle | Where you can see it |", "|---|---|"]
    L += [f"| **{canon.C[k][1]}** ({canon.C[k][2]}, {canon.C[k][3]}) | {how} |" for k, how in P["principles"]]
    L += ["", "## Page Structure", ""]
    L += [f"{i + 1}. {p}" for i, p in enumerate(purposes(P))]
    L += ["", "## Search Card", "", f"- **Title:** {P['title']}", f"- **Description:** {P['desc']}",
          f"- **Structured data:** {', '.join(P['schema'])}"]
    L += [f"- {s}" for s in P.get("seo", [])]
    L += ["", "## Borrow This", ""] + [f"- {x}" for x in P["borrow"]]
    if P.get("study"):
        L += ["", "## Study The Real Thing", ""] + [f"- **{n}**: {w}" for n, w in P["study"]]
    L += ["", "## Build Your Own", "", "```text", prompt_for(P), "```", ""]
    return "\n".join(L)


def notes_html(P):
    t = THEMES[P["theme"]]
    v = t["v"]
    why = "".join(f"<li>{e(w)}</li>" for w in P["why"])
    psy = "".join(
        f'<tr><th scope="row">{e(canon.C[k][1])}<small>{e(canon.C[k][2])}</small></th><td>{e(how)}</td></tr>' for k, how in P["principles"])
    struct = "".join(f"<li>{e(p)}</li>" for p in purposes(P))
    sch = "".join(f"<li><b>{e(s)}.</b> {e(SCHEMA_WHY.get(s, SCHEMA_WHY['WebPage']))}</li>" for s in P["schema"])
    extra = "".join(f"<li>{e(s)}</li>" for s in P.get("seo", []))
    built = "".join(f"<li>{e(s)}</li>" for s in SEO_BUILT_IN)
    skip = "".join(f"<li>{e(s)}</li>" for s in SEO_SKIP)
    borrow = "".join(f"<li>{e(x)}</li>" for x in P["borrow"])
    study = ""
    if P.get("study"):
        study = '<div class="blk"><h2>Study The Real Thing</h2><ul>' + "".join(f"<li><b>{e(n)}.</b> {e(w)}</li>" for n, w in P["study"]) + \
                '</ul><p class="note">Read for structure and messaging. Borrow the technique, never the words, images or layout.</p></div>'
    sw = "".join(f'<span style="background:{v[k]}" title="{k} {v[k]}"></span>' for k in ("bg", "bg2", "card", "ink", "accent", "accent2", "dark"))
    extra_files = "".join(f' <a class="btn ghost" href="{x["file"]}">{e(x["label"])}</a>' for x in P.get("extra", []))
    sl_note = ' The extra links under the listing are sitelinks. They are Google\'s call, so treat them as likely, never guaranteed.' if P.get("sitelinks") else ""
    body = f"""<div class="banner"><div class="wrap">{shell.top("../")}
<div class="eh"><p class="crumbs"><a href="../index.html#library">Design Library</a> › {e(P["group"])}</p>
<h1>{P["num"]} · {e(P["name"])}</h1><p class="lead">{e(P["blurb"])}</p>
<div class="acts"><a class="btn" href="sample.html">Open The Live Sample</a>{extra_files}<a class="btn ghost" href="#prompt">Copy The Build Prompt</a></div></div></div></div>
<main id="main"><div class="wrap">
<a class="pv" href="sample.html" style="display:block"><img src="preview.jpg" alt="Preview of the {e(P["name"])} sample for the fictional brand {e(P["brand"]["name"])}" width="1280" height="800"></a>
<div class="cols">
<div>
<div class="blk"><h2>Why This Page Works</h2><ul>{why}</ul></div>
<div class="blk"><h2>The Psychology At Work</h2><table class="ptab"><tbody>{psy}</tbody></table>
<p class="note">Every principle is explained, with its source, on <a href="../canon/index.html">the research page</a>.</p></div>
<div class="blk"><h2>Page Structure</h2><ol style="list-style:decimal;padding-left:1.3rem">{struct}</ol></div>
<div class="blk"><h2>Search Card</h2><p class="lead" style="font-size:1rem;margin-bottom:1rem">How this page is set up to appear in Google, and what is built into its code.</p>
{shell.serp(P, v)}<p class="note">A mock-up drawn from this sample's real title, description and site name.{sl_note}</p>
<h3 style="margin-top:1.6rem">Structured Data On This Page</h3><ul>{sch}{extra}</ul>
<h3 style="margin-top:1.6rem">Built Into Every Sample</h3><ul>{built}</ul>
<h3 style="margin-top:1.6rem">Left Out On Purpose</h3><ul>{skip}</ul></div>
<div class="blk"><h2>Borrow This</h2><ul>{borrow}</ul></div>
{study}
<div class="blk" id="prompt"><h2>Build Your Own</h2><p>Paste this into Claude, fill in the brackets and attach your real proof. When your page is live, run <a href="../audit/index.html">the audit prompt</a> on it.</p>
<div class="prompt"><button type="button" onclick="var b=this;navigator.clipboard.writeText(document.getElementById('pt').textContent).then(function(){{b.textContent='Copied'}}).catch(function(){{b.textContent='Select the text to copy'}})">Copy Prompt</button><pre id="pt">{e(prompt_for(P))}</pre></div></div>
</div>
<aside class="side blk"><div class="panel"><h2>At A Glance</h2><dl>
<dt>Best for</dt><dd>{e(", ".join(P["aud"]))}</dd><dt>Group</dt><dd>{e(P["group"])}</dd>
<dt>Style direction</dt><dd>{e(t["label"])}. {e(t["mood"])}</dd><dt>Fonts</dt><dd>{e(t["pair"])}</dd>
<dt>Palette</dt><dd><div class="sw">{sw}</div></dd><dt>Sample brand</dt><dd>{e(P["brand"]["name"])} (fictional)</dd></dl></div>
<div class="panel"><h2>Files In This Entry</h2><dl><dt>sample.html</dt><dd>The live page. 1 file, no build step.</dd><dt>notes.md</dt><dd>These notes as plain text, ready to hand to an AI assistant.</dd><dt>preview.jpg</dt><dd>A screenshot of the sample.</dd></dl></div></aside>
</div></div><div style="height:clamp(56px,8vw,104px)"></div></main>"""
    return shell.page(f'{P["num"]} {P["name"]} | Authority Builder Design Library', P["blurb"], body, root="../")


# ---------- building blocks (generated from the themes and sections) ----------

def block_fonts(num):
    cards = ""
    links = ""
    for k, t in THEMES.items():
        v = t["v"]
        links += f'<link href="{t["fonts"]}" rel="stylesheet">\n'
        cards += f"""<article class="panel" style="padding:clamp(22px,3vw,36px)"><p class="kick">{e(t["label"])}</p>
<p style="font-family:{v["fd"]};font-weight:{v["hw"]};letter-spacing:{v["hls"]};text-transform:{v["htt"]};font-size:clamp(2rem,4.6vw,3.2rem);line-height:1.02;margin-bottom:.8rem">Clients first, then the calendar</p>
<p style="font-family:{v["fb"]};font-size:1.08rem;line-height:1.6;max-width:56ch">A display face sets the mood in 1 line. A body face has to stay readable for 600 words on a phone. This pairing does both.</p>
<dl><dt>Pairing</dt><dd>{e(t["pair"])}</dd><dt>Feels like</dt><dd>{e(t["mood"])}</dd><dt>Paste into your page head</dt>
<dd><code style="font-size:.74rem;word-break:break-all;color:var(--ink2)">&lt;link href="{e(t["fonts"])}" rel="stylesheet"&gt;</code></dd></dl></article>"""
    body = f"""<div class="banner"><div class="wrap">{shell.top("../")}<div class="eh"><p class="crumbs"><a href="../index.html#blocks">Design Library</a> › Building Blocks</p>
<h1>{num} · Font Pairings For Personal Brands</h1><p class="lead">10 pairings, every one free on Google Fonts. Each is used in at least 2 samples, so you can see it working on a real page before you commit.</p></div></div></div>
<main id="main"><div class="wrap sec"><div class="blk" style="margin-top:0"><h2>How To Choose</h2><ul>
<li>Pick the display font for the feeling you want in the first second. Pick the body font for how it reads on a phone.</li>
<li>2 families is plenty. A third only earns its place as a small accent, like a handwritten note or a mono label.</li>
<li>If the real font you love is paid, use the nearest free match and say so. Never pretend a substitute is the original.</li>
<li>Then stop changing it. A look you repeat is how people come to recognise you (Byron Sharp, How Brands Grow).</li></ul></div>
<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(340px,1fr));margin-top:2.4rem">{cards}</div></div></main>"""
    return shell.page(f"{num} Font Pairings | Authority Builder Design Library", "10 free Google Font pairings for coaches, creators and consultants.", body, "../", links)


def block_palettes(num):
    cards = ""
    for k, t in THEMES.items():
        v = t["v"]
        roles = [("bg", "Page"), ("bg2", "Alternate band"), ("card", "Cards"), ("ink", "Text"), ("ink2", "Quiet text"), ("accent", "The 1 action"),
                 ("accent2", "Support"), ("dark", "Contrast band")]
        sw = "".join(f'<div><span style="display:block;height:54px;border-radius:10px;border:1px solid rgba(0,0,0,.12);background:{v[r]}"></span>'
                     f'<small style="display:block;margin-top:.3rem;font-size:.72rem;line-height:1.3"><b>{n}</b><br>{v[r]}</small></div>' for r, n in roles)
        rows = "".join(f"<tr><td>{a} on {b}</td><td><b>{ratio(v[a], v[b]):.1f}:1</b></td></tr>" for a, b in
                       [("ink", "bg"), ("ink2", "bg"), ("accent-ink", "accent"), ("accent-t", "bg"), ("dark-ink", "dark")])
        cssvars = "; ".join(f"--{r}:{v[r]}" for r, _ in roles)
        cards += f"""<article class="panel" style="padding:clamp(22px,3vw,32px)"><p class="kick">{e(t["label"])}</p><p style="color:var(--ink2);margin-bottom:1rem">{e(t["mood"])}</p>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem">{sw}</div>
<table class="ptab" style="margin-top:1.2rem"><tbody>{rows}</tbody></table>
<p class="note"><code style="font-size:.72rem;word-break:break-all">{e(cssvars)}</code></p></article>"""
    body = f"""<div class="banner"><div class="wrap">{shell.top("../")}<div class="eh"><p class="crumbs"><a href="../index.html#blocks">Design Library</a> › Building Blocks</p>
<h1>{num} · Colour Palettes, Contrast-Checked</h1><p class="lead">10 palettes with every text and button pairing measured against the WCAG AA line of 4.5 to 1. If it is in here, it is readable.</p></div></div></div>
<main id="main"><div class="wrap sec"><div class="blk" style="margin-top:0"><h2>How To Use A Palette</h2><ul>
<li>1 accent colour, kept for the 1 action you want. The thing that looks different is the thing that gets noticed (the Von Restorff effect).</li>
<li>Most of the page is the page colour and the text colour. The alternate band and the contrast band give the scroll its rhythm.</li>
<li>Check contrast before you fall in love. Body text needs 4.5 to 1 against its background.</li>
<li>Pull your accent from something you already own: your logo, your book cover, the jacket in your headshot.</li></ul></div>
<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(340px,1fr));margin-top:2.4rem">{cards}</div></div></main>"""
    return shell.page(f"{num} Colour Palettes | Authority Builder Design Library", "10 contrast-checked colour palettes for personal brand websites.", body, "../")


def block_patterns(num, pages):
    first, used = {}, {}
    for P in pages:
        for name, d in P["sections"]:
            used.setdefault(name, []).append(P["num"])
            first.setdefault(name, (d, P))
    secs, labels = [], ""
    order = [n for n in SECTION_NAMES if n in first]
    host = dict(pages[0])
    host.update(num=num, name="Section Patterns", slug="section-patterns", theme="corporate_calm", nav=None, cta=None, schema=["CollectionPage"],
                title="Section Patterns | Authority Builder Design Library", desc="Every section pattern used across the library, on 1 page.",
                brand=dict(name="Pattern Shelf", domain="patternshelf.example", mono="P", line="Every section pattern in the library, shown once."),
                css=".pat{background:#132620;color:#EAE7E1;font:600 .8rem/1.4 system-ui,sans-serif;padding:.7rem clamp(20px,5vw,48px);letter-spacing:.04em}.pat b{color:#C5A880}")
    html = ""
    for i, n in enumerate(order):
        d, P0 = first[n]
        us = ", ".join(sorted(set(used[n])))
        html += f'<div class="pat"><b>Pattern {i + 1:02d} · {e(SECTION_NAMES[n])}</b> &nbsp;·&nbsp; used in {us}</div>\n' + REG[n](dict(d), host) + "\n"
        secs.append((n, d))
    full = sample_html(host, secs=secs, back="../index.html#blocks")
    full = re.sub(r"<main id=\"main\">.*?</main>", lambda m: f'<main id="main">\n{html}</main>', full, flags=re.S)
    md = "# " + num + " · Section Patterns\n\nEvery section pattern used across the library, shown once on 1 page.\n\n| Pattern | Used in |\n|---|---|\n" + \
         "\n".join(f"| {SECTION_NAMES[n]} | {', '.join(sorted(set(used[n])))} |" for n in order) + "\n"
    return full, md


# ---------- gallery, canon, readme ----------

def card(P):
    t = THEMES[P["theme"]]
    tags = "".join(f"<span>{e(a)}</span>" for a in P["aud"]) + f"<span>{e(t['label'])}</span>"
    return (f'<a class="card" href="{P["dir"]}/index.html" data-g="{e(P["group"])}" data-a="{e("|".join(P["aud"]))}" data-s="{e(t["label"])}">'
            f'<div class="th"><img src="{P["dir"]}/preview.jpg" alt="{e(P["name"])} sample preview" loading="lazy" width="640" height="400"></div>'
            f'<div class="bd"><span class="no">{P["num"]} · {e(P["group"])}</span><h3>{e(P["name"])}</h3><p>{e(P["blurb"])}</p><div class="tags">{tags}</div></div></a>')


def gallery(pages, blocks):
    groups = ""
    for g, gd in GROUPS:
        cs = "".join(card(P) for P in pages if P["group"] == g)
        groups += f'<section class="group" data-group="{e(g)}"><header><h2>{e(g)}</h2><p>{e(gd)}</p></header><div class="grid">{cs}</div></section>'
    auds = ["Coach", "Creator", "Consultant", "Business Owner"]
    styles = [t["label"] for t in THEMES.values()]
    chips = lambda key, vals: "".join(f'<button class="chip" type="button" data-k="{key}" data-v="{e(x)}" aria-pressed="false">{e(x)}</button>' for x in vals)
    bl = "".join(f'<a class="card" href="{d}/{f}"><div class="bd"><span class="no">{n} · Building Blocks</span><h3>{e(t)}</h3><p>{e(b)}</p></div></a>'
                 for n, d, f, t, b in blocks)
    nprin = len(canon.C)
    body = f"""<div class="banner"><div class="wrap">{shell.top()}
<div class="hero"><p class="kick">Authority Builder™ · Design Library</p>
<h1>Steal The Structure. <em>Keep Your Own Voice.</em></h1>
<p class="lead">{len(pages)} website pages a coach, creator, consultant or business owner actually needs. Each one is a live sample built on proven psychology, search-ready code and a look worth borrowing. Open a page, read why it works, copy the prompt and make it yours.</p>
<div class="acts"><a class="btn" href="#library">Browse The Library</a><a class="btn ghost" href="canon/index.html">Read The Research</a></div>
<div class="nums"><div><b>{len(pages)}</b><span>page samples, each a single file</span></div><div><b>{len(THEMES)}</b><span>style directions, not 1 template</span></div>
<div><b>{nprin}</b><span>principles in the research, each with its source</span></div><div><b>0</b><span>stock photos, fake timers or invented scarcity</span></div></div></div></div></div>
<main id="main">
<section class="sec cream light"><div class="wrap"><p class="kick">How To Use It</p><h2>Three Steps From Blank Page To <em>Live Page</em></h2>
<ol class="how"><li><h3>Pick The Page You Need</h3><p>Filter by who you are and the job the page has to do. Open the live sample and scroll it on your phone.</p></li>
<li><h3>Read Why It Works</h3><p>Every sample comes with notes: the psychology behind each section, the search card and what to borrow.</p></li>
<li><h3>Copy The Prompt, Then Audit</h3><p>Paste the build prompt into Claude with your real proof. Once it is live, run the audit prompt over it.</p></li></ol></div></section>
<div class="filters" id="library"><div class="wrap">
<div class="fg"><span>I am a</span>{chips("a", auds)}</div><div class="fg"><span>Style</span>{chips("s", styles)}</div>
<button class="chip" type="button" id="clear" style="border-style:dashed">Show all</button></div></div>
<div class="wrap" style="padding-bottom:clamp(56px,8vw,104px)">{groups}
<section class="group" id="blocks"><header><h2>Building Blocks</h2><p>The parts every page is made from: type, colour and section patterns.</p></header><div class="grid">{bl}</div></section></div>
<section class="sec strip"><div class="wrap two"><div><p class="kick">The Research</p><h2>Built On The <em>Legends</em>, Checked Against This Month's Rules</h2>
<p class="lead" style="margin-top:1rem">Kahneman, Cialdini, Fogg, Schwartz, Ogilvy, Dunford and more, each mapped to the exact pages that use them. Search rules are checked against Google's current guidance, including the May 2026 changes.</p>
<div class="acts"><a class="btn" href="canon/index.html">Open The Research Page</a></div></div>
<div><p class="kick">After You Build</p><h2>Then Run The <em>Audit</em></h2><p class="lead" style="margin-top:1rem">The Full SEO and AI Search Audit checks how your finished site shows up in Google and in AI answers, then hands you a ranked fix list.</p>
<div class="acts"><a class="btn ghost" href="audit/index.html">Get The Audit Prompt</a></div></div></div></section>
</main>
<script>
(function(){{var on={{a:null,s:null}},chips=document.querySelectorAll('.chip[data-k]'),cards=document.querySelectorAll('.card[data-g]');
function run(){{cards.forEach(function(c){{var ok=(!on.a||c.dataset.a.split('|').indexOf(on.a)>-1)&&(!on.s||c.dataset.s===on.s);c.hidden=!ok}});
document.querySelectorAll('.group[data-group]').forEach(function(g){{g.hidden=!g.querySelector('.card:not([hidden])')}})}}
chips.forEach(function(b){{b.addEventListener('click',function(){{var k=b.dataset.k,v=b.dataset.v;on[k]=on[k]===v?null:v;
chips.forEach(function(x){{x.setAttribute('aria-pressed',on[x.dataset.k]===x.dataset.v)}});run()}})}});
document.getElementById('clear').addEventListener('click',function(){{on={{a:null,s:null}};chips.forEach(function(x){{x.setAttribute('aria-pressed','false')}});run()}})}})();
</script>"""
    return shell.page("Authority Builder Design Library | Website Design Inspiration For Coaches, Creators And Consultants",
                      f"{len(pages)} live website page samples for coaches, creators, consultants and business owners, each with the psychology, search set-up and build prompt behind it.", body)


EVERY = {"site_name", "title_desc", "favicon", "cwv", "ai_is_seo", "no_faq_rich"}  # built into every sample


def canon_page(pages):
    uses = {}
    for P in pages:
        for k, _ in P["principles"]:
            uses.setdefault(k, []).append(P)
    secs = ""
    for gid, gname, gdesc in canon.GROUPS:
        rows = ""
        for k, (g, name, who, src, mean) in canon.C.items():
            if g != gid:
                continue
            links = "".join(f'<a href="../{P["dir"]}/index.html" title="{e(P["name"])}">{P["num"]}</a>' for P in uses.get(k, []))
            fallback = "<small>Every sample</small>" if k in EVERY else "<small>Reference</small>"
            rows += f'<tr id="{k}"><td><b>{e(name)}</b><small>{e(who)}</small></td><td>{e(mean)}</td><td><small>{e(src)}</small></td><td class="use">{links or fallback}</td></tr>'
        secs += (f'<section class="blk"><p class="kick">{e(gname)}</p><h2>{e(gdesc)}</h2><table class="ctab"><thead><tr><th>Principle</th><th>In Plain English</th>'
                 f'<th>Source</th><th>Samples</th></tr></thead><tbody>{rows}</tbody></table></section>')
    sites = "".join(f'<li><b><a href="{u}" rel="noopener">{e(n)}</a></b> <small>{e(k)}</small>{e(w)}</li>' for n, u, k, w in canon.SITES)
    shelf = "".join(f'<li><b><a href="{u}" rel="noopener">{e(n)}</a></b> {e(w)}</li>' for n, u, w in canon.SHELF)
    srcs = "".join(f'<li><a href="{u}" rel="noopener">{e(t)}</a><small>{e(p)}</small></li>' for p, t, u in canon.SOURCES)
    docs = "".join(f'<li><a href="{u}" rel="noopener">{e(t)}</a></li>' for t, u in canon.GOOGLE_DOCS)
    body = f"""<div class="banner"><div class="wrap">{shell.top("../")}<div class="eh"><p class="crumbs"><a href="../index.html">Design Library</a> › The Research</p>
<h1>The Canon Behind <em>Every Page</em></h1><p class="lead">{len(canon.C)} principles from behavioural science, interface research, the copywriting legends and current search guidance. Each links to the samples that use it, so you can see the idea working on a real page. A few apply to every sample and are marked that way.</p></div></div></div>
<main id="main"><div class="wrap" style="padding-bottom:clamp(56px,8vw,104px)">
<section class="blk"><h2>The Ethics Test</h2><p class="lead">Use these to help a person make a decision they will be glad they made. If a tactic only works because the person did not see it clearly, it is not in this library. That is why you will find no fake countdown timers, no invented scarcity and no made-up proof in any sample.</p></section>
{secs}
<section class="blk"><p class="kick">Sites Studied</p><h2>Successful Sites In The Niche, Read For Structure</h2>
<p class="lead">Read from each site's live page text in November 2026. These notes cover structure and messaging only. Borrow the technique, never the words, images or layout.</p><ul class="src">{sites}</ul>
<h3 style="margin-top:2rem">Also On The Authority Builder Reference Shelf</h3><ul class="src">{shelf}</ul></section>
<section class="blk"><p class="kick">Sources</p><h2>What Was Read, And When</h2><p class="lead">Web sources were read in November 2026. Books are cited beside each principle above.</p><ul class="src">{srcs}</ul>
<h3 style="margin-top:2rem">Google's Own Documentation</h3><p class="note">Search rules change often. These are the primary pages to re-check before you rely on any rule. If anything in this library disagrees with them, Google's page wins.</p><ul class="src">{docs}</ul></section>
</div></main>"""
    return shell.page("The Research | Authority Builder Design Library", "The psychology, copywriting and search principles behind every sample in the Authority Builder Design Library.", body, "../")


def audit_page(md):
    body = f"""<div class="banner"><div class="wrap">{shell.top("../")}<div class="eh"><p class="crumbs"><a href="../index.html">Design Library</a> › After You Build</p>
<h1>The Full SEO And <em>AI Search Audit</em></h1><p class="lead">Built your page? This prompt checks how your whole site shows up in Google and in AI answers, then gives you a ranked, plain-English fix list you approve by number.</p></div></div></div>
<main id="main"><div class="wrap narrow sec"><div class="blk" style="margin-top:0"><h2>How To Use It</h2><ol style="list-style:decimal;padding-left:1.3rem">
<li>Open a new chat in Claude and turn on web search.</li><li>Copy the whole prompt below and send it.</li>
<li>Answer the questions about your business. Skip any you like.</li><li>Read the report, then reply with the numbers of the fixes you want.</li></ol>
<p class="note">Nothing on your site changes until you say which fixes to make. The same prompt is in this folder as a plain file: full-seo-and-ai-search-audit.md.</p></div>
<div class="prompt"><button type="button" onclick="var b=this;navigator.clipboard.writeText(document.getElementById('pt').textContent).then(function(){{b.textContent='Copied'}}).catch(function(){{b.textContent='Select the text to copy'}})">Copy Prompt</button><pre id="pt" style="max-height:none">{e(md)}</pre></div></div></main>"""
    return shell.page("The Full SEO And AI Search Audit | Authority Builder Design Library", "A prompt that audits how your site shows up in Google and in AI answers, then gives you a ranked fix list.", body, "../")


def load_pages():
    pages = []
    for f in sorted((SRC / "pages").glob("p*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        for P in getattr(m, "PAGES", None) or [m.P]:
            P["num"] = f"{P['n']:03d}"
            P["dir"] = f"{P['num']}-{P['slug']}"
            pages.append(P)
    return sorted(pages, key=lambda P: P["n"])


def main():
    bad = check_contrast()
    if bad:
        print("CONTRAST FAILURES:\n  " + "\n  ".join(bad))
    pages = load_pages()
    import shutil
    n0 = len(pages)
    keep = {P["dir"] for P in pages} | {f"{n0 + 1:03d}-font-pairings", f"{n0 + 2:03d}-colour-palettes", f"{n0 + 3:03d}-section-patterns"}
    for old in ROOT.iterdir():  # remove entry folders left over from an earlier numbering
        if old.is_dir() and re.match(r"\d{3}-", old.name) and old.name not in keep:
            shutil.rmtree(old)
    for P in pages:
        d = ROOT / P["dir"]
        d.mkdir(exist_ok=True)
        for k, _ in P["principles"]:
            assert k in canon.C, f"{P['num']}: unknown principle {k}"
        (d / "sample.html").write_text(sample_html(P))
        for x in P.get("extra", []):
            (d / x["file"]).write_text(sample_html(P, secs=x["sections"], title=x["title"], desc=x["desc"], path=x["path"], noindex_note=True))
        (d / "index.html").write_text(notes_html(P))
        (d / "notes.md").write_text(notes_md(P))
    n = len(pages)
    blocks = [(f"{n + 1:03d}", f"{n + 1:03d}-font-pairings", "index.html", "Font Pairings For Personal Brands", "10 pairings, all free on Google Fonts, each shown working on real samples."),
              (f"{n + 2:03d}", f"{n + 2:03d}-colour-palettes", "index.html", "Colour Palettes, Contrast-Checked", "10 palettes with every text and button pairing measured against WCAG AA."),
              (f"{n + 3:03d}", f"{n + 3:03d}-section-patterns", "index.html", "Section Patterns", "Every section used across the library on 1 page: heroes, proof, pricing, footers.")]
    for (num, d, f, t, b), fn in zip(blocks, (block_fonts, block_palettes, None)):
        (ROOT / d).mkdir(exist_ok=True)
        if fn:
            (ROOT / d / f).write_text(fn(num))
            (ROOT / d / "notes.md").write_text(f"# {num} · {t}\n\n{b}\n\nGenerated from `src/themes.py`. Change a token there and rebuild.\n")
        else:
            html, md = block_patterns(num, pages)
            (ROOT / d / f).write_text(html)
            (ROOT / d / "notes.md").write_text(md)
    (ROOT / "index.html").write_text(gallery(pages, blocks))
    audit_md = ROOT / "audit" / "full-seo-and-ai-search-audit.md"
    if audit_md.exists():
        (ROOT / "audit" / "index.html").write_text(audit_page(audit_md.read_text()))
    (ROOT / "canon").mkdir(exist_ok=True)
    (ROOT / "canon" / "index.html").write_text(canon_page(pages))
    rows = "\n".join(f"| {P['num']} | [{P['name']}]({P['dir']}/index.html) | {P['group']} | {', '.join(P['aud'])} | {THEMES[P['theme']]['label']} |" for P in pages)
    rows += "\n" + "\n".join(f"| {num} | [{t}]({d}/{f}) | Building Blocks | Everyone | All 10 |" for num, d, f, t, b in blocks)
    table = "| # | Page | Group | For | Style |\n|---|---|---|---|---|\n" + rows + "\n"
    (ROOT / "INDEX.md").write_text("# Library Index\n\n" + table)
    readme = ROOT / "README.md"
    if readme.exists():  # keep the index in the README in step with the build
        readme.write_text(re.sub(r"<!-- INDEX:START -->.*?<!-- INDEX:END -->", lambda m: "<!-- INDEX:START -->\n" + table + "<!-- INDEX:END -->",
                                 readme.read_text(), flags=re.S))
    print(f"Built {n} samples, {len(blocks)} building blocks, gallery and canon.")


if __name__ == "__main__":
    main()
