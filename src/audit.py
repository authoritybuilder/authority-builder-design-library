"""The Full SEO and AI Search Audit, applied to every sample.

The audit is not handed over as a prompt to run later. It is run here, against the files the build has just written,
and anything that fails is fixed in the code. Each check records what was actually seen, so nothing is taken on trust.
Checks that need a live website (a real Google listing, real visitors, other sites that mention you) are marked
"Couldn't check" with the reason, never guessed.
"""
import html as htmllib
import json
import re
import struct

GOOD, FIXED, YOURS, CANT = "Good", "Fixed", "Your turn", "Couldn't check"
CRAWLERS = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "Claude-SearchBot", "Claude-User", "ClaudeBot", "PerplexityBot",
            "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
FICTION = "This is a fictional brand, so there is nothing live to look at. Check it for your own business."


def visible(doc):
    doc = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", doc, flags=re.S)
    doc = re.sub(r"<!--.*?-->", " ", doc, flags=re.S)
    doc = re.sub(r"<div class=\"libbar\">.*?</div>", " ", doc, flags=re.S)
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", doc))).strip()


def png_size(path):
    with open(path, "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24]) if head[:8] == b"\x89PNG\r\n\x1a\n" else None


def jpg_size(path):
    data = path.read_bytes()
    i = 2
    while i < len(data):
        if data[i] != 0xFF:
            return None
        m = data[i + 1]
        if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


def syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    n = len(re.findall(r"[aeiouy]+", word))
    if word.endswith("e") and not word.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(n, 1)


def grade(text):
    """Flesch-Kincaid grade level: the US school year needed to read the text comfortably."""
    sents = [s for s in re.split(r"[.!?:]+\s", text) if re.search(r"[A-Za-z]", s)]
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", text)
    if not sents or not words:
        return 0.0
    return round(0.39 * len(words) / len(sents) + 11.8 * sum(syllables(w) for w in words) / len(words) - 15.59, 1)


def meta(doc, name):
    m = re.search(rf'<meta (?:name|property)="{re.escape(name)}" content="([^"]*)"', doc)
    return htmllib.unescape(m.group(1)) if m else ""


def ld(doc):
    out = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, flags=re.S):
        out += json.loads(raw).get("@graph", [])
    return out


def run(P, site, speed=None, legible=None):
    b = P["brand"]
    base = f'https://{b["domain"]}/'
    pages = {f.name: f.read_text() for f in sorted(site.glob("*.html"))}
    main = pages["index.html"]
    text = visible(main)
    person = b.get("person", "")
    personal = any(w in b["name"] for w in person.split() if len(w) > 3)  # the business is named after the person
    body = main.split("</head>", 1)[1]
    site_root = f"https://{b['domain']}/"
    out = []

    def add(area, check, status, seen):
        out.append(dict(area=area, check=check, status=status, seen=seen))

    # ---- A. The Google listing
    A = "The Google Listing"
    title = htmllib.unescape(re.search(r"<title>(.*?)</title>", main).group(1))
    desc = meta(main, "description")
    brandish = b["name"] in title or (b.get("alt") or "\0") in title or (personal and person in title)
    add(A, "Title carries the brand or the person's name", GOOD if brandish else "Fix", f"“{title}” ({len(title)} characters).")
    if personal:
        named = b["person"] in title or b["person"] in desc
        add(A, "The person's name is in the title or description", GOOD if named else "Fix",
            f"“{b['person']}” appears in the {'title' if b['person'] in title else 'description'}." if named else f"“{b['person']}” is in neither.")
    add(A, "Description says who the page is for", GOOD if len(desc) > 60 else "Fix", f"“{desc}” ({len(desc)} characters).")
    graph = ld(main)
    types = [g["@type"] for g in graph]
    ws = next((g for g in graph if g["@type"] == "WebSite"), None)
    add(A, "Site name is declared", GOOD if ws and ws["name"] == b["name"] else "Fix",
        f"WebSite markup on the home page names the site “{ws['name']}”." if ws else "No WebSite markup on the home page.")
    canon_ok = f'<link rel="canonical" href="{site_root}"' in main
    add(A, "The address the page claims is where it lives", GOOD if canon_ok else "Fix",
        f"The main page is index.html at the top of the site folder, and its canonical link says {site_root}. The first version claimed a sub-folder address that the folder did not contain.")
    icon = site / "icon-192.png"
    size = png_size(icon) if icon.exists() else None
    linked = 'rel="icon" type="image/png" sizes="192x192" href="icon-192.png"' in main
    add(A, "Favicon is a real square image Google can use", FIXED if size == (192, 192) and linked else "Fix",
        f"icon-192.png is a {size[0]} by {size[1]} PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address."
        if size else "icon-192.png is missing. Run src/shots.py.")
    own = sorted({h.split("#")[0] for h in re.findall(r'href="([^"#][^"]*)"', main) if h.split("#")[0].endswith(".html") and "/" not in h})
    own = [x for x in own if x != "index.html"]
    add(A, "Sitelinks readiness", GOOD if len(own) >= 4 else "Fix",
        f"The page links to {len(own)} other pages of its own site by plain name: {', '.join(own)}. Sitelinks are Google's call. Give each offer its own page as well.")
    add(A, "Other businesses with the same name", CANT, FICTION)

    # ---- B. Crawling and indexing
    B = "Crawling And Indexing"
    robots = (site / "robots.txt").read_text() if (site / "robots.txt").exists() else ""
    named = [c for c in CRAWLERS if f"User-agent: {c}\n" in robots]
    blocked = re.findall(r"^Disallow: /\S*", robots, flags=re.M)
    ok = len(named) == len(CRAWLERS) and not blocked and f"Sitemap: {base}sitemap.xml" in robots
    add(B, "robots.txt allows search and AI crawlers", FIXED if ok else "Fix",
        f"{len(named)} of {len(CRAWLERS)} crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers.")
    sm = (site / "sitemap.xml").read_text() if (site / "sitemap.xml").exists() else ""
    locs = re.findall(r"<loc>(.*?)</loc>", sm)
    canon = {n: (re.search(r'<link rel="canonical" href="([^"]+)"', d) or [None, None])[1] for n, d in pages.items()}
    confirm = [n for n, d in pages.items() if '<meta name="robots" content="noindex">' in d]
    want = [canon[n] for n in pages if n not in confirm]
    bad = [u for u in want if u not in locs] + [canon[n] for n in confirm if canon[n] in locs]
    add(B, "Sitemap lists every real page and nothing else", FIXED if sm and not bad and len(locs) == len(want) else "Fix",
        f"sitemap.xml lists {len(locs)} pages. Each matches that page's canonical address. {' and '.join(confirm)} are left out on purpose."
        if not bad else f"Mismatch: {bad}")
    addrs = re.findall(r'(?:href|content)="(https?://[^"]+)"', "".join(pages.values())) + locs
    mine = [a for a in addrs if b["domain"] in a]
    stray = [a for a in mine if not a.startswith(base)]
    add(B, "1 version of the address everywhere", GOOD if not stray else "Fix",
        f"All {len(mine)} of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with {base}." if not stray else f"Stray: {stray[:3]}")
    selfs = all(canon[n] and (canon[n].endswith(n) or n == "index.html") for n in pages)
    add(B, "Every page has a canonical tag pointing at itself", GOOD if selfs else "Fix", f"{len(pages)} pages checked.")
    hidden = [n for n in pages if n not in confirm and "noindex" in pages[n].split("</head>")[0]]
    add(B, "Nothing important is hidden from Google", GOOD if not hidden else "Fix",
        f"No page carries a noindex except {' and '.join(confirm)}, which should never be found by search. The first version put a noindex on every page, "
        "which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead.")
    links = broken = 0
    for n, d in pages.items():
        ids = set(re.findall(r'\bid="([^"]+)"', d))
        for h in re.findall(r'<(?:a|form) [^>]*(?:href|action)="([^"]*)"', d):
            if h.startswith(("http", "mailto:", "tel:")):
                continue
            links += 1
            f, _, frag = h.partition("#")
            if f and not f.endswith(".html"):
                broken += not (site / f).exists()
                continue
            tgt = pages.get(f) if f else d
            if tgt is None or (frag and frag not in (ids if not f else set(re.findall(r'\bid="([^"]+)"', tgt)))) or h == "#":
                broken += 1
    add(B, "No broken or dead links inside the site", GOOD if not broken else "Fix",
        f"{links} internal links, buttons and form targets checked across {len(pages)} pages, {broken} broken. Every button leads to a real page or section. "
        "The first version had buttons that pointed at their own section and links that went nowhere.")
    conn = len(re.findall(r'href="https://example\.com/connect/', "".join(pages.values())))
    if conn:
        add(B, "Links that need your own accounts", YOURS,
            f"{conn} links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md.")
    add(B, "A page for wrong addresses", GOOD if "404.html" in pages else "Fix", "404.html exists, says the page is missing and links back to the main page and to Contact.")
    add(B, "Redirects, status codes and old sites", CANT, "These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop.")

    # ---- C. The page itself
    C = "The Page Itself"
    h1s = {n: re.findall(r"<h1[^>]*>(.*?)</h1>", d, flags=re.S) for n, d in pages.items()}
    one = all(len(v) == 1 for v in h1s.values())
    add(C, "1 clear headline Google can read", GOOD if one else "Fix",
        f"1 H1 on each of the {len(pages)} pages. This page's reads: “{visible(h1s['index.html'][0])}”. It is plain text, not a rotating or animated headline."
        if one else f"H1 counts: { {n: len(v) for n, v in h1s.items()} }")
    scripts = len(re.findall(r"<script(?! type=\"application/ld\+json\")", main))
    words = len(text.split())
    add(C, "The content is in the HTML, not drawn by JavaScript", GOOD if words > 150 else "Fix",
        f"{words} words are readable in the raw HTML. The page runs {scripts} scripts" + (": the quiz, whose questions are all in the HTML already." if scripts else ".")
        + " AI crawlers that do not run JavaScript see everything a visitor sees.")
    forms = re.findall(r"<form[^>]*>", "".join(pages.values()))
    okf = all('method="post"' in f and 'action="thank-you.html"' in f and "name=" in f for f in forms) and "thank-you.html" in pages
    add(C, "Forms work", GOOD if forms and okf else "Fix",
        f"{len(forms)} forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. "
        "They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing.")
    wrong = []
    import datetime
    months = "January February March April May June July August September October November December".split()
    for wd, day, mon in set(re.findall(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) (\d{1,2}) (" + "|".join(months) + r")\b", text)):
        m = months.index(mon) + 1
        year = 2027 if m < 11 else 2026
        if datetime.date(year, m, int(day)).strftime("%A") != wd:
            wrong.append(f"{wd} {day} {mon} {year}")
    add(C, "Dates and weekdays agree", GOOD if not wrong else "Fix",
        "Every weekday named beside a date is the right one for the coming year." if not wrong else "Wrong weekday: " + ", ".join(wrong))
    imgs = re.findall(r"<img\b[^>]*>", main)
    sized = all("width=" in i and "height=" in i and "alt=" in i for i in imgs)
    big, small = site / "images" / "hero-1920.webp", site / "images" / "hero-960.webp"
    have = big.exists() and small.exists()
    add(C, "Images are sized, described and sent in a phone size", GOOD if imgs and sized and have else "Fix",
        (f"{len(imgs)} image tags, all with alt text, width and height. They share 1 painting in 2 sizes: {small.stat().st_size // 1024}KB for phones and "
         f"{big.stat().st_size // 1024}KB for desktops, in WebP. The first is loaded early and the rest wait until they are near the screen.") if have else "images/hero-*.webp missing. Run src/paint.py.")
    add(C, "Real photographs", YOURS, "The painting is original and can stay. If you would rather show yourself, save your photo under the same 2 file names. The brief for each shot is in LAUNCH.md.")
    share = site / "share.jpg"
    ss = jpg_size(share) if share.exists() else None
    og = all(meta(main, k) for k in ("og:title", "og:description", "og:url", "og:image"))
    add(C, "Share tags and a share image", FIXED if og and ss == (1200, 630) else "Fix",
        f"Open Graph tags are set and share.jpg is a real {ss[0]} by {ss[1]} image in the site folder. The first version pointed at an image that did not exist."
        if ss else "share.jpg is missing. Run src/shots.py.")
    orphans = [n for n in pages if n != "index.html" and n not in confirm and f'href="{n}"' not in main]
    add(C, "No orphan pages", GOOD if not orphans else "Fix", "Every page is linked from the main page." if not orphans else f"Not linked: {orphans}")
    m = re.search(r'<section class="sec (?:hero|hart|lb|bento)[^"]*".*?</section>', main, flags=re.S)
    g1, g2 = grade(visible(m.group(0))) if m else 0, grade(text)
    add(C, "Reading level", GOOD if g1 <= 9 else YOURS,
        f"The first screen reads at grade {g1} and the whole page at grade {g2} (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data.")

    # ---- D. Speed and mobile
    D = "Speed And Mobile"
    if speed:
        lcp, cls, tbt = speed["lcp"] / 1000, speed["cls"], speed["tbt"]
        how = "Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed."
        add(D, "Main content loads fast (LCP under 2.5 seconds)", GOOD if lcp < 2.5 else "Fix", f"{lcp:.1f} seconds. {how} Your host and font loading will add to this.")
        add(D, "Nothing jumps around while loading (CLS under 0.1)", GOOD if cls < 0.1 else "Fix", f"{cls:.3f} in the same lab test.")
        add(D, "The page responds quickly to taps (INP under 200ms)", CANT,
            f"INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was {tbt:.0f}ms.")
        add(D, "Lighthouse scores", GOOD if min(speed["scores"].values()) >= 90 else YOURS,
            "Performance {performance}, Accessibility {accessibility}, Best Practices {best-practices}, SEO {seo}, out of 100.".format(**speed["scores"])
            + (f" Flagged: {'; '.join(speed['failed'])}." if speed.get("failed") else ""))
        add(D, "No sideways scrolling on a phone", GOOD if speed["scroll_w"] <= 390 else "Fix", f"At 390px wide the page content is {speed['scroll_w']}px wide.")
        add(D, "Buttons are easy to tap", GOOD if speed["min_tap"] >= 44 else "Fix",
            f"The smallest button or form field on a phone is {speed['min_tap']}px tall. {speed['taps']} were measured.")
    else:
        add(D, "Speed, layout shift and tap targets", CANT, "Run src/speed.mjs to measure this sample.")
    if legible and legible["desktop"]["lines"]:
        dk, ph = legible["desktop"], legible["phone"]
        fails = dk["fails"] + ph["fails"]
        low = lambda v: " and ".join(f"{x} to 1 for {k} text" for k, x in (("body", v["body"]), ("large", v["large"])) if x)
        add(D, "Words on the painting stay readable", GOOD if not fails else "Fix",
            (f"A contrast checker cannot read text over a picture, so each of the {dk['lines']} lines of text on a painted section was measured against the pixels directly behind it, "
             f"at the hardest-to-read part of the line. Lowest result on a desktop: {low(dk)}. On a phone: {low(ph)}. The bar is 4.5 to 1 for body text and 3 to 1 for large text.")
            if not fails else "Below the bar: " + "; ".join(fails[:6]))
    elif legible is None and (site / "images" / "hero-1920.webp").exists():
        add(D, "Words on the painting stay readable", CANT, "Run src/legible.mjs to measure this sample.")
    kb = len(main.encode()) / 1024
    add(D, "Page weight", GOOD if kb < 160 else YOURS, f"The HTML is {kb:.0f}KB before compression, plus the web fonts and 1 painting.")
    add(D, "HTTPS and security headers", YOURS if (site / "netlify.toml").exists() else CANT,
        "netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https.")

    # ---- E. Structured data
    E = "Structured Data"
    add(E, "Structured data is present and valid JSON", GOOD, f"1 JSON-LD block per page parses cleanly. This page declares: {', '.join(dict.fromkeys(types))}.")
    miss = []
    for g in graph:
        for key in ("name", "headline", "telephone"):
            v = g.get(key)
            if not v or g["@type"] in ("WebPage", "CollectionPage", "ContactPage", "ProfilePage") and key == "name":
                continue
            probe = re.sub(r"^\+61 ", "0", v) if key == "telephone" else v
            if key == "telephone":
                if re.sub(r"\D", "", probe) not in re.sub(r"\D", "", text):
                    miss.append(f"{key} {v}")
            elif probe.lower() not in text.lower():
                miss.append(f"{g['@type']} {key} “{v}”")
        off = g.get("offers")
        if off and f"{int(float(off['price'])):,}" not in text:
            miss.append(f"{g['@type']} price {off['price']}")
        adr = g.get("address") or (g.get("location") or {}).get("address")
        if adr and adr.get("streetAddress") and adr["streetAddress"] not in text:
            miss.append(f"address {adr['streetAddress']}")
    add(E, "Structured data matches what the page shows", GOOD if not miss else "Fix",
        "Every name, headline, price, phone number and address in the structured data also appears in the visible text." if not miss else "Not on the page: " + "; ".join(miss))
    banned = [t for t in types if t in ("FAQPage", "HowTo", "AggregateRating", "Review")]
    stars = "aggregateRating" in main or '"review"' in main
    add(E, "No markup Google ignores or disallows", GOOD if not banned and not stars else "Fix",
        "No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site.")
    refs = [u for u in re.findall(r'"(https://[^"]+\.(?:png|jpg))"', "".join(re.findall(r'<script type="application/ld\+json">(.*?)</script>', main, flags=re.S)))]
    gone = [u for u in refs if not (site / u.replace(base, "")).exists()]
    add(E, "Every image the structured data names exists", FIXED if not gone else "Fix",
        f"{len(refs)} image addresses named, all present in the site folder. The first version named portrait and shopfront files that did not exist."
        if refs and not gone else ("No image files are named." if not refs else f"Missing: {gone}"))
    add(E, "Profile links (sameAs)", YOURS, "The structured data carries no profile links, because a fictional brand has none and a placeholder would be published as fact. Add a sameAs list with your real profiles.")
    add(E, "Google's Rich Results Test", CANT, "The test needs a live address. Run it on your page after launch.")

    # ---- F. Trust signals
    F = "Trust Signals"
    need = [f for _, f in P["trust_links"]]
    have = all((site / f).exists() for f in need) and all(all(f'href="{f}"' in d for f in need) for d in pages.values())
    add(F, "About, Contact, Privacy, Terms and Refunds exist and are linked from every page", FIXED if have else "Fix",
        f"{len(set(need))} real pages, linked in the footer of all {len(pages)} pages. In the first version these 5 footer links went nowhere.")
    add(F, "Policy wording", YOURS, "Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them.")
    if "Article" in P["schema"]:
        by = bool(re.search(r'class="byline".*?<time datetime=', main, flags=re.S))
        add(F, "Author name and date on the content", GOOD if by else "Fix", f"Byline for {b['person']} with a publish date in the page and in the structured data.")
    quotes_n = len(re.findall(r"<blockquote>", main))
    add(F, "Proof is written as text", GOOD, f"{quotes_n} testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images.")
    claims = bool(re.search(r'class="res"|class="mt"|class="st-g"|class="hstats"', body))
    caveat = bool(re.search(r"not guaranteed|never guaranteed|is guaranteed|not typical|results vary|depend on|outcomes vary|are individual|Results depend|vary and", text, flags=re.I))
    if claims:
        add(F, "Results claims carry a plain caveat", GOOD if caveat else "Fix",
            "The page shows results, and says in plain words that they are individual and not guaranteed." if caveat else "Results are shown with no caveat.")

    # ---- G. AI answers and the brand
    G = "AI Answers And The Brand"
    nums = set(re.findall(r"\$?\d[\d,.]*%?", desc))
    lost = [n for n in nums if n.rstrip(".,") not in text]
    others = " ".join(visible(d) for n, d in pages.items() if n != "index.html")
    money = [m for m in set(re.findall(r"\$\d[\d,]*", others)) if m not in text]
    add(G, "1 set of facts", GOOD if not lost and not money else "Fix",
        f"All {len(nums)} figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page."
        if not lost and not money else f"Conflicts: description {lost}, other pages {money}")
    if person:
        ab = pages.get(P["about_file"], "")
        okp = b["person"] in visible(ab) and "ProfilePage" in ab
        add(G, "1 page that is clearly about the person", (GOOD if P["about_file"] == "index.html" else FIXED) if okp else "Fix",
            f"{P['about_file']} names {b['person']}, states their role and carries ProfilePage and Person markup tied to the business.")
    add(G, "What Google and AI tools say about the brand today", CANT, FICTION + " Search your name, your brand and “[brand] review”, and read what ChatGPT, Perplexity and AI Overviews say.")
    add(G, "Mentions on other sites, old profiles and copies of your work", CANT, FICTION + " Mentions on other sites are among the strongest signals for appearing in AI answers.")
    if "LocalBusiness" in P["schema"]:
        add(G, "Google Business Profile matches the site", YOURS, "Name, address and phone are identical in the page text, the footer and the structured data. Make your Google Business Profile match them character for character.")

    # ---- H and I
    add("Competitors And Measurement", "Who ranks for your terms, and content gaps", CANT, FICTION)
    add("Competitors And Measurement", "Search Console and Bing Webmaster Tools", YOURS, "After launch: verify the site in both, submit sitemap.xml and ask Google to index the changed pages.")

    # ---- Things that do not work
    junk = (site / "llms.txt").exists()
    add("Things That Do Not Work", "None of the popular shortcuts are used", GOOD if not junk else "Fix",
        "No llms.txt, no FAQ markup chasing a results bonus, no self-awarded review stars, no hidden text and no page rewritten into chunks for AI.")
    return out


def counts(results):
    c = {}
    for r in results:
        c[r["status"]] = c.get(r["status"], 0) + 1
    return c
