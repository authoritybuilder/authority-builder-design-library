"""The trust pages every site needs: About, Contact, Privacy, Terms and Refunds.

Google's quality guidelines expect clear contact details and policies on any site that takes money, and they need to be
linked from every page. Each sample gets real, linked pages built from its own brand details. The policy wording is a
plain-English starting template: replace it with your own terms and have a lawyer check it.
"""

TPL = ("**Template wording for a fictional brand.** Replace every line with your real policy, in your own words, and have a lawyer check it. "
       "Never publish a guarantee or policy you do not actually offer.")


def a_an(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


def role_line(P):
    b = P["brand"]
    role = b["role"][0].lower() + b["role"][1:]
    own = "" if b["name"].startswith(b["person"]) else f" and the founder of {b['name']}"
    return f"{b['person']} is {a_an(role)} {role}{own}."


def email(P):
    return P["brand"].get("contact", "hello@" + P["brand"]["domain"]).split(" · ")[0]


def files(P):
    """Which trust pages this sample needs, and where the footer should point. A sample that is itself the About or Contact page links to itself."""
    path = P.get("path", "")
    P["about_file"] = "index.html" if path.startswith("about") else "about.html"
    P["contact_file"] = "index.html" if path.startswith("contact") else "contact.html"
    P["trust_links"] = [("About", P["about_file"]), ("Contact", P["contact_file"]), ("Privacy Policy", "privacy.html"), ("Terms", "terms.html"),
                        ("Refund Policy", "refunds.html")]


def about(P):
    b = P["brand"]
    first = b["person"].split()[-2] if b["person"].startswith("Dr ") else b["person"].split()[0]
    facts = [("Name", b["person"]), ("Role", b["role"]), ("Business", b["name"]), ("Based in", b.get("where", "Australia")), ("Contact", email(P))]
    secs = [
        ("hero_split", dict(_="About page: 1 page that is clearly about the person behind the business", eyebrow=f"About {b['name']}" if b["name"] != b["person"] else "About",
                            h=f"Meet *{b['person']}*", sub=f"{role_line(P)} {b.get('line', '')}", cta=("Get In Touch", P["contact_file"]),
                            visual=dict(label=f"Photo brief: a clear, friendly portrait of {first}. Use the same photo on every profile"))),
        ("legal", dict(_="The facts in 1 place: the same name, role and details that appear everywhere else", tone="alt", sub=True, eyebrow="The facts, in 1 place",
                       h=f"{first}, *At A Glance*", lead="Use these details word for word on your website, your social profiles and every directory. When they match, people and AI tools stop hedging.",
                       blocks=[("facts", facts), ("h2", "Your Story Goes Here"),
                               ("p", f"This starter page gives Google and AI tools 1 clear page about {first}. On your own site, add the story only you can tell: "
                                     "what you did before, why you started and who you have helped. Sample 005 in the library shows a full About page.")],
                       cta=("Back To The Main Page", "index.html"))),
    ]
    return secs, f"About {b['person']} | {b['name']}" if b["name"] != b["person"] else f"About {b['person']}", \
        f"{role_line(P)} Name, role, location and contact details in 1 place."


def contact(P):
    b = P["brand"]
    details = [("Email", email(P)), ("Based in", b.get("where", "Australia")), ("Reply time", "Within 1 business day")]
    parts = b.get("contact", "").split(" · ")
    if len(parts) > 1:
        details.insert(1, ("Phone", parts[1]))
    secs = [("hero_center", dict(_="Contact page: 1 headline, then the form", eyebrow="Contact", h=f"Get In Touch With *{b['name']}*",
                                 sub="Send a note and a real person will reply. 3 fields, and no phone number required.")),
            ("contact", dict(_="A short form, real details and a stated reply time", tone="alt", details=details,
                             form=dict(title="Send a message", button="Send Message", note="We reply within 1 business day.",
                                       fields=[("Your name", "text", "First and last name"), ("Email", "email", "you@email.com"), ("How can we help?", "area", "A few lines is plenty")])))]
    return secs, f"Contact | {b['name']}", f"Contact {b['name']}. Email, location and a reply within 1 business day."


def policy(P, kind):
    b = P["brand"]
    n, em = b["name"], email(P)
    if kind == "privacy":
        h, lead = "Privacy *Policy*", f"What {n} collects, why, and how to ask for it to be removed."
        blocks = [("h2", "What We Collect"), ("list", ["Your name and email address when you fill in a form on this site", "Messages you send us", "Basic, anonymous visit statistics"]),
                  ("h2", "What We Do With It"), ("p", "We use your details to reply to you and to send what you asked for. We do not sell or rent your details to anyone."),
                  ("h2", "Email"), ("p", "Every email we send has an unsubscribe link. 1 click removes you."),
                  ("h2", "Seeing Or Deleting Your Details"), ("p", f"Email {em} and we will show you what we hold or delete it, within 30 days."),
                  ("h2", "Who To Contact"), ("p", f"{n}, {b.get('where', 'Australia')}. {em}")]
        desc = f"How {n} collects, uses and protects your details, and how to have them removed."
    elif kind == "terms":
        h, lead = "Terms *Of Use*", f"The plain-English terms for using this site and buying from {n}."
        blocks = [("h2", "Using This Site"), ("p", "The content here is general information. It is not personal advice for your situation."),
                  ("h2", "Buying From Us"), ("p", "Prices are in Australian dollars. What each offer includes is described on its own page. If a page and these terms disagree, the page for that offer wins."),
                  ("h2", "Results"), ("p", "Any results described on this site belong to the people who achieved them. Yours will depend on your situation and the work you put in. Nothing here is a promise of income or a specific outcome."),
                  ("h2", "Our Content"), ("p", f"The words, templates and materials on this site belong to {n}. Please do not copy or resell them without written permission."),
                  ("h2", "Your Rights"), ("p", "Nothing in these terms limits your rights under Australian Consumer Law."),
                  ("h2", "Questions"), ("p", f"Email {em}.")]
        desc = f"The plain-English terms for using this site and buying from {n}."
    else:
        h, lead = "Refund *Policy*", "What happens if you change your mind, in plain words."
        stated = P.get("refund")
        if stated:
            blocks = [("h2", "The Short Version"), ("p", stated), ("h2", "How To Ask"), ("p", f"Email {em} with your name and the date you bought. You do not need to give a reason."),
                      ("h2", "How Long It Takes"), ("p", "Refunds go back to the original payment method within 10 business days."),
                      ("h2", "Your Rights"), ("p", "This policy sits on top of your rights under Australian Consumer Law. It does not replace them.")]
        else:
            blocks = [("h2", "The Short Version"), ("p", "[State your refund terms here in 1 or 2 sentences. If your sales page makes a promise or guarantee, repeat it here word for word.]"),
                      ("h2", "How To Ask"), ("p", f"Email {em} with your name and the date you bought."),
                      ("h2", "How Long It Takes"), ("p", "[Say how many days a refund takes and how it is paid.]"),
                      ("h2", "Your Rights"), ("p", "This policy sits on top of your rights under Australian Consumer Law. It does not replace them.")]
        desc = f"The refund policy for {n}: what is covered, how to ask and how long it takes."
    secs = [("legal", dict(_=f"{kind.title()} page, linked from the footer of every page", eyebrow=n, h=h, lead=lead, tpl=TPL, blocks=blocks, cta=("Back To The Main Page", "index.html")))]
    return secs, f"{h.replace('*', '')} | {n}", desc
