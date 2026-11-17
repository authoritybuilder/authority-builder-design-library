"""The launch checklist for each site, and the settings for hosting the library itself."""
import re

LIBRARY_NETLIFY = """# Hosting the library on Netlify: publish the repository root. No build command is needed.
[build]
  publish = "."

# The sample sites are fictional brands, so the library asks search engines not to index them.
# This lives here, not in the pages, so a site you copy out of the library is ready to be found.
[[headers]]
  for = "/*/site/*"
  [headers.values]
    X-Robots-Tag = "noindex"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
"""


def scan(P, site):
    """Count, from the files that were actually written, everything a new owner has to replace or connect."""
    b = P["brand"]
    pages = {f.name: f.read_text() for f in sorted(site.glob("*.html"))}
    text = {**pages, "sitemap.xml": (site / "sitemap.xml").read_text(), "robots.txt": (site / "robots.txt").read_text()}
    conn = {}
    for name, t in pages.items():
        for label, what in re.findall(r'<a [^>]*href="https://example\.com/connect/([a-z0-9-]+)"[^>]*>(.*?)</a>', t, flags=re.S):
            words = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", what)).strip()
            entry = conn.setdefault(label, [set(), 0, words[:60]])
            entry[0].add(name)
            entry[1] += 1
    forms = sorted({(m, name) for name, t in pages.items() for m in re.findall(r'<form[^>]* name="([^"]+)"', t)})
    return dict(pages=len(pages), domain=sum(t.count(b["domain"]) for t in text.values()), conn=conn, links=sum(v[1] for v in conn.values()), forms=forms)


def launch_md(P, site):
    b = P["brand"]
    s = P["launch"] = scan(P, site)
    contact = b.get("contact", "hello@" + b["domain"])
    L = [f"# Launch Checklist · {P['num']} {P['name']}", "",
         "The `site` folder is a complete website. Upload it to Netlify, or any static host, and every page, link and form works.",
         "What it cannot contain is you. Work through this list, then run the pre-launch check at the end.", "",
         "## 1. Make It Yours", "",
         f"- [ ] Replace the demo brand ({b['name']}), the copy, the prices and the proof with your own. The comments in the HTML say what each section is for.",
         f"- [ ] Delete the demo note in the footer of all {s['pages']} pages. Search for `DEMO NOTE`.",
         f"- [ ] Replace `{b['domain']}` with your real address. It appears {s['domain']} times across the pages, `sitemap.xml` and `robots.txt`.",
         f"- [ ] Replace the contact details: {contact}, {b.get('where', 'Australia')} and the placeholder ABN 00 000 000 000.", "",
         "## 2. Your Photos", "",
         "Every picture is a file in `site/images/`. To use your own, save it under the same file name, at about the size shown. Nothing in the code needs to change.",
         "The files that ship are painted stand-ins, each labelled with its file name. The pre-launch check tells you which are still in place.", ""]
    names = {"you": "You", "me": "You", "guest": "A client", "face": "A client or reader", "scene": "A place or moment", "video": "A video still",
             "mock": "Your product or work, on a laptop", "phone": "The same, on a phone", "slide": "A slide or page", "post": "A social post"}
    L += ["| File | Size | Who Or What | On | The Photo To Take |", "|---|---|---|---|---|"]
    L += ["| `hero-2560.webp`, `hero-1920.webp`, `hero-1280.webp`, `hero-960.webp` | 2560, 1920, 1280 and 960 wide, all 16:10 | The background photograph, from Pexels | every section with a picture behind it | It can stay: Pexels photographs are free to use. Your own wide photo with a quiet area for the words is better |"]
    for ph in P.get("photos", []):
        who = ph["who"] if ph["kind"] in ("guest", "face") and ph["who"] and "reader" not in ph["who"] else names[ph["kind"]]
        brief = ph["brief"] or ("A square headshot, used with their permission" if ph["kind"] == "face" else "")
        L.append(f"| `{ph['file']}` | {ph['w']} × {ph['h']} | {who} | {', '.join(ph['where'])} | {brief} |")
    L += ["",
         "- [ ] Replace every photo of you. Use the same headshot on your social profiles so people recognise you.",
         "- [ ] Replace client photos only with their permission. If you have none yet, delete that `<img>` tag and the quote stands on the name alone.",
         "- [ ] After swapping a photo, read its `alt` text in the HTML and make it describe your picture.",
         "- [ ] Replace `icon-192.png`, `icon-512.png` and `share.jpg` with your own mark and share image, keeping the file names."]
    L += ["", f"## 3. Connect Your Accounts ({s['links']} Links)", ""]
    if s["conn"]:
        L += ["These can only be finished with your own accounts. Each points at example.com until you give it a real destination, so nothing breaks in the meantime.",
              "Search the folder for `example.com/connect` to find them all.", "", "| Replace this | Shown on the page as | In | Times |", "|---|---|---|---|"]
        L += [f"| `example.com/connect/{k}` | {v[2]} | {', '.join(sorted(v[0]))} | {v[1]} |" for k, v in sorted(s["conn"].items())]
    else:
        L += ["None. Every link on this site already goes to a real page."]
    L += ["", f"## 4. Forms ({len(s['forms'])})", ""]
    L += [f"- `{n}` on {f}" for n, f in s["forms"]]
    L += ["", "Every form posts to the thank-you page, names its fields, marks what is required and carries a hidden spam trap. They follow Netlify's own pattern for plain HTML forms.", "",
          "- [ ] **On Netlify:** open Forms for your site, select Enable form detection, then deploy again. Netlify scans for forms from the next deploy. Entries appear under Forms, and you can have them emailed to you.",
          "- [ ] **On another host, or to send entries straight to your email tool:** change each form's `action` to the address your tool gives you. On a host with no form handling, a form will show an error until you do.",
          "- [ ] Netlify writes the thank-you path with a leading slash. With your site at the top of your domain, `thank-you.html` and `/thank-you.html` are the same page. Use the second if you move a form into a subfolder.",
          "- [ ] Send a test entry through every form, then check that the thank-you page appears and the entry arrived."]
    if P.get("action"):
        L += ["", "## 5. Bookings And Payments", "",
              f"- [ ] The main buttons lead to `{P['action']['file']}`, a short request form that works with no calendar or checkout tool: you reply with times or an invoice. "
              "When you have a booking or payment link, point those buttons at it."]
    L += ["", "## 6. Policies", "",
          "- [ ] Rewrite `privacy.html`, `terms.html` and `refunds.html` in your own words and have a lawyer check them. They are marked as template wording on the page.",
          "- [ ] Never publish a guarantee you do not actually offer.", "",
          "## 7. Structured Data", "",
          "- [ ] In the `application/ld+json` block near the top of each page, check every fact against the visible page after your edits.",
          "- [ ] Add a `sameAs` list with your real profile links (LinkedIn, Instagram, YouTube) to the Organization and Person entries.",
          "- [ ] Adding this page to a site you already have, at an address like `/masterclass/`? Update its canonical link, its `og:url` and its line in `sitemap.xml` to that address, and add breadcrumb markup.", "",
          "## 8. After Launch", "",
          "- [ ] Check that http, https, www and non-www all land on 1 address.",
          "- [ ] Verify the site in Google Search Console and Bing Webmaster Tools, and submit `sitemap.xml`.",
          "- [ ] Run Google's Rich Results Test and PageSpeed Insights on the live address.", "",
          "## Pre-Launch Check", "",
          "From the library folder, run:", "", "```bash", "python3 src/prelaunch.py path/to/your/site", "```", "",
          "It lists anything from this checklist that is still in the files. Launch when it reports nothing left from the demo.", ""]
    return "\n".join(L)


def library_host(root, pages):
    """The sample sites carry no noindex of their own, so the library keeps its fictional brands out of search with host settings."""
    rules = "\n".join(f"Disallow: /{P['dir']}/site/" for P in pages)
    (root / "robots.txt").write_text(f"# The gallery and notes can be indexed. The fictional sample sites are kept out of search.\nUser-agent: *\nAllow: /\n{rules}\n")
    (root / "netlify.toml").write_text(LIBRARY_NETLIFY)
    (root / ".nojekyll").write_text("")
