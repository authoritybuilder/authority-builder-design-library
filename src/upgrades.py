"""Research applied to each page.

Every page type was researched on its own (November 2026). This file turns each finding into a change in that
page's code, and records the finding, its source and the change so the notes page can show its working.
The figures are benchmarks from testing firms and software vendors. Treat them as direction, not guarantees.
"""

import kit
import trust

# The page each booking, enrolment or reservation button leads to. It works with no calendar or checkout tool:
# the owner replies with times or an invoice. Swap the buttons for your own booking or payment link whenever you have one.
ACTIONS = {
    1: dict(file="book.html", kind="call", eyebrow="Free fit call", h="Book Your *Free Fit Call*", button="Request My Call", q="What is happening in your role right now?",
            sub="25 minutes by video with Imogen. No pitch. A clear no is completely fine."),
    2: dict(file="book.html", kind="call", eyebrow="A first conversation", h="Request A *Conversation*", button="Request A Conversation", q="Where does your pricing hurt most?",
            sub="30 minutes with Marcus, partner to partner. No proposal until you ask for one."),
    7: dict(file="enrol.html", kind="enrol", eyebrow="February intake", h="Reserve Your Place In *The Steady Founder*", button="Reserve My Place",
            select=("How would you like to pay?", ["Pay in full: $3,600", "Pay monthly: $1,300 x 3 months"]),
            sub="Choose how you would like to pay. Your invoice and welcome pack arrive within 1 business day, and the 30-day guarantee starts on the first call."),
    11: dict(file="book.html", kind="call", eyebrow="Intro call", h="Book A Free *Intro Call*", button="Request My Call", q="What are you hoping to fix or launch?",
             sub="30 minutes with Mira. You will leave knowing which package fits and when you could start."),
    21: dict(file="book.html", kind="call", eyebrow="Clinic review", h="Book A Free *Clinic Review*", button="Request My Review", q="How many practitioners do you have, and how full is the diary?",
             sub="45 minutes. We count first, then tell you what we would fix. Free for clinics with 2 or more practitioners."),
    22: dict(file="book.html", kind="call", eyebrow="A first conversation", h="Book A First *Conversation*", button="Request A Conversation", q="What decision are you turning over?",
             sub="45 minutes, confidential. Most people come with 1 decision they are turning over."),
    27: dict(file="reserve.html", kind="reserve", eyebrow="14 to 16 May 2027", h="Reserve Your *Place*", button="Reserve My Place",
             select=("Which room would you like?", ["Lodge room: $2,950", "Cabin: $3,650"]),
             sub="A $500 deposit holds your place. Your deposit invoice arrives within 1 business day, with a full refund until 14 March 2027."),
}
# What the thank-you page should promise, for pages whose main form is something other than a general enquiry
KINDS = {3: "signup", 10: "application", 12: "signup", 14: "signup", 15: "signup", 16: "signup", 17: "signup", 18: "signup", 19: "call", 23: "signup", 24: "signup",
         25: "signup", 26: "signup"}
# Pages whose buy buttons can only be finished with the owner's own checkout
CHECKOUT = {8, 9, 12}
# Dated events get a real calendar file and a Google Calendar link. Times are UTC.
EVENTS = {
    15: dict(title="Fully Booked, Without Posting Daily: free masterclass", start="20270311T010000Z", end="20270311T021500Z", where="Online",
             details="A free 60-minute masterclass with Carmen Ortiz, plus Q and A. The link is in your confirmation email."),
    17: dict(title="The 5-Day Offer Sprint: day 1", start="20270228T190000Z", end="20270228T192000Z", where="Online",
             details="Day 1 of the free 5-day Offer Sprint. 20 minutes. The task arrives by email at 6am AEDT."),
    27: dict(title="The Slow Strategy Retreat", start="20270514T050000Z", end="20270516T040000Z", where="Kin Kin Valley Lodge, Kin Kin QLD",
             details="3 days in the Noosa hinterland. Arrive from 3pm Friday. Depart 2pm Sunday."),
}

# id: (who found it, link or None, the finding in plain words)
R = {
    "cre": ("Conversion Rate Experts, button microcopy win report", "https://conversion-rate-experts.com/button-microcopy-win-report/",
            "Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test."),
    "mecl": ("MarketingSherpa and MECLABS, research-based swipe file", "https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File",
             "A testimonial and credibility markers placed beside the call to action gave a 12% relative lift."),
    "clarity": ("MarketingExperiments", "https://marketingexperiments.com/?p=22070", "Clarity beats persuasion: say plainly what it is, who it is for and what happens next."),
    "fold": ("Nielsen Norman Group, Scrolling and Attention", "https://www.nngroup.com/articles/scrolling-and-attention/",
             "57% of viewing time goes to the first screen and 74% to the first 2 screens."),
    "read": ("Unbounce benchmark data, reported by Colorlib", "https://colorlib.com/wp/landing-page-statistics/",
             "Across 41,000 landing pages, copy at a 5th to 7th grade reading level converted at 11.1%, against 5.3% for professional-level copy."),
    "fields": ("Unbounce 2026 data, reported by Digital Applied", "https://digitalapplied.com/blog/landing-page-statistics-2026-conversion-data-points",
               "1-field forms converted at 13.4%, 3-field forms at 10.1% and 9-field forms at 3.6%."),
    "hubspot": ("HubSpot, pricing page best practices", "https://blog.hubspot.com/marketing/best-practices-pricing-page",
                "A highlighted plan is chosen more often, and more so when the dearest plan is listed first."),
    "tiers": ("Process Street, study of 250 pricing pages", "https://www.process.st/2015/12/saas-pricing-pages/",
              "The average page offers 3.5 packages, and only half of them highlight 1."),
    "webform": ("SureForms, webinar registration benchmarks", "https://sureforms.com/?p=32679",
                "Strong registration pages convert 35% to 45%, and 2-field forms beat longer ones by 34%."),
    "webfold": ("WebinarJam", "https://webinarjam.com/?p=6617", "Keep the headline, the subheadline and the form together in the first screen."),
    "time": ("Sequel, webinar landing page practices", "https://sequel.io/webinar-landing-page-best-practices/",
             "Specific outcomes and a stated length ease the worry about time. Reminders matter because only 40% to 50% of sign-ups attend."),
    "local": ("BrightLocal, what local consumers want from a business website",
              "https://www.brightlocal.com/research/what-local-consumers-want-most-from-local-business-websites/",
              "The details people want most are the list of services, prices, a phone number, the address and opening hours. A missing phone number puts them off."),
    "call": ("Small Business Trends, customer contact statistics", "https://smallbiztrends.com/2019/05/customer-contact-statistics.html",
             "60% of customers prefer to call a local business."),
    "quiz": ("Interact, 2026 quiz conversion report", "https://tryinteract.com/blog/quiz-conversion-rate-report/",
             "40.1% of people who start a quiz become a lead, and 65% of starters finish."),
    "gate": ("Outgrow, analytics guidance", "https://support.outgrow.co/docs/analytics", "A lead form people can skip still captures 25% to 30%."),
    "three": ("Formstack data, reported by eSEOspace", "https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/",
              "Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%."),
    "phone": ("UX Movement", "https://uxmovement.com/?p=8014", "A required phone number raises form abandonment."),
    "cases": ("Forrester, reported by Digital Commerce 360", "https://www.digitalcommerce360.com/?p=767377",
              "71% of business buyers rate customer and peer case studies as highly valuable."),
    "images": ("Baymard Institute", "https://baymard.com/blog/product-images-descriptive-text",
               "For 56% of shoppers the first action on a product page is exploring the images. Descriptive text on those images helps, and 52% of sites leave it off."),
    "about": ("Haden Interactive", "https://www.hadeninteractive.com/your-website-page-by-page-about-us/",
              "About 1 in 10 visitors reach the About page, and its job is reassurance."),
    "aio": ("Seer Interactive, May 2026", "https://www.seerinteractive.com/insights/what-it-takes-to-rank-in-googles-ai-overviews-in-2026-is-not-what-you-think",
            "AI Overviews appear on nearly 65% of question-style searches, and an author bio alone does not predict being cited."),
    "first30": ("Superlines study, reported on dev.to", None,
                "44.2% of AI citations come from the first 30% of a page's text. Comparison tables and cited sources raise the odds."),
    "links": ("Beacons, analysis of about 3,000 link pages", "https://beacons.ai/i/blog/optimizing-your-links-for-clicks",
              "The first link gets the highest click rate, and pages with 7 or fewer links do best."),
    "podtext": ("Podder, podcast SEO practices", "https://www.podderapp.com/post/podcast-seo-best-practices",
                "Search engines rank the text about an episode: its own page, the show notes and a full transcript."),
    "podld": ("Clutch, podcast SEO", "https://clutch.co/resources/podcast-seo",
              "Google shows no podcast-specific rich results, but structured data still helps it identify the show."),
    "planners": ("All American Entertainment, speaking industry benchmark", "https://www.allamericanspeakers.com/blog/key-takeaways-from-aaes-2022-speaking-industry-benchmark-report/amp/",
                 "Event planners' top 2 factors are fitting the budget (75.5%) and topic relevance (65.7%)."),
    "reel": ("The Speaker Lab", "https://thespeakerlab.com/blog/what-event-planners-want-in-speakers/",
             "Planners want a relevant topic, a demo video, named social proof, a one sheet and fast replies."),
    "event": ("i4a, event registration practices", "https://www.i4a.com/blog/event-registration-best-practices/",
              "Show the refund and transfer policy, all costs upfront, add-to-calendar links and a contact for questions."),
    "repeat": ("HeySummit, event landing page checklist", "https://heysummit.com/blog/event-landing-page-checklist",
               "Repeat the registration button after each major section and place testimonials near the price."),
    "trial": ("Recurly, subscriber acquisition benchmarks", "https://recurly.com/research/subscriber-acquisition-benchmarks",
              "The median free trial is 14 days, and monthly plans convert from a trial better than annual ones."),
    "annual": ("Circle, subscription business models", "https://circle.so/fr/blog/subscription-business-model-creators",
               "Annual subscribers are 36% less likely to leave."),
}


# Where to crop each kind of painting when a page needs a second or third picture: (focal point, zoom)
CROPS = {
    "summit": [(72, 76, 2.4), (24, 60, 1.9), (50, 90, 2.0)], "city": [(50, 66, 2.2), (16, 86, 2.0), (82, 62, 2.4)],
    "studio": [(52, 62, 1.25), (76, 78, 1.9), (20, 72, 1.8)], "coast": [(82, 56, 2.6), (36, 70, 2.4), (60, 92, 2.0)],
    "stage": [(50, 66, 2.6), (30, 30, 1.8), (70, 90, 2.2)], "valley": [(52, 82, 2.4), (10, 78, 1.9), (50, 58, 2.6)],
    "desk": [(50, 58, 2.0), (84, 62, 2.4), (20, 50, 2.2)], "alpine": [(46, 34, 2.2), (12, 84, 2.0), (60, 72, 2.2)],
    "desert": [(50, 70, 2.0), (84, 56, 2.2), (16, 78, 2.2)], "night": [(50, 82, 2.6), (74, 22, 2.4), (12, 80, 1.9)],
    "fields": [(30, 56, 2.6), (56, 80, 2.0), (82, 56, 2.4)], "lodge": [(72, 70, 2.6), (10, 76, 1.8), (40, 60, 2.2)],
}

# page: (scene, mirrored, colour of the words that sit on it, what the picture shows). The pictures are made by src/paint.py.
ART = {
    1: ("summit", False, "light", "Painting of a woman standing on a hilltop at first light, with misty ranges below"),
    2: ("city", False, "light", "Painting of a river city at blue hour, its windows lit and reflected in the water"),
    3: ("studio", False, "dark", "Painting of arches, steps and spheres in lilac, cobalt and lime"),
    4: ("coast", False, "light", "Painting of a sunny bay with a lighthouse on the headland and flowers in the dunes"),
    5: ("summit", True, "light", "Painting of a woman in a red coat on a hilltop, looking out over ranges at dawn"),
    6: ("stage", False, "light", "Painting of a lone speaker on a dark stage under gold light, the audience in silhouette"),
    7: ("valley", False, "dark", "Painting of soft green hills on a calm morning, with a path winding toward a far town"),
    8: ("desk", False, "dark", "Painting of a desk under a window with an open laptop, a lamp and a stack of books"),
    9: ("studio", True, "dark", "Painting of arches, steps and spheres in tomato, mustard and teal"),
    10: ("alpine", False, "light", "Painting of a still mountain lake at dusk, framed by dark pines"),
    11: ("studio", False, "dark", "Painting of arches, steps and spheres in peach, rust and sage"),
    12: ("studio", True, "dark", "Painting of arches, steps and spheres in coral, yellow and blue"),
    13: ("alpine", False, "dark", "Painting of snow peaks above a still lake, with pines on both sides"),
    14: ("desk", True, "dark", "Painting of a calm desk by a window, with a laptop, a lamp and a plant"),
    15: ("city", True, "light", "Painting of a city at night, gold windows reflected in a dark river"),
    16: ("studio", True, "dark", "Painting of arches, steps and spheres in lime, cobalt and peach"),
    17: ("desert", False, "light", "Painting of a long road through red country toward flat-topped ranges"),
    18: ("studio", False, "dark", "Painting of arches, steps and spheres in bronze, ivory and espresso"),
    19: ("valley", True, "light", "Painting of bright green country under a blue sky, a path leading toward a far town"),
    20: ("coast", True, "light", "Painting of a sunny tropical bay with flowers in the dunes"),
    21: ("coast", False, "dark", "Painting of a pale dawn over a quiet bay"),
    22: ("city", False, "light", "Painting of a city skyline at sunrise, reflected in the river"),
    23: ("alpine", True, "dark", "Painting of mountains and a still lake in soft morning light"),
    24: ("night", False, "light", "Painting of a starry night with a low moon, and a single lit cabin among the pines"),
    25: ("desk", False, "dark", "Painting of a tidy desk by a window, with a laptop showing a page being edited"),
    26: ("fields", False, "light", "Painting of golden rows running to the horizon, with a farmhouse and cypress trees"),
    27: ("lodge", False, "light", "Painting of a lit lodge on a hillside at golden hour, with mist in the valleys"),
    28: ("lodge", True, "dark", "Painting of calm green hills in morning mist, with a house on the near rise"),
}


def art_for(n):
    scene, mirror, tone, alt = ART[n]
    crops = [(f"{100 - cx if mirror else cx}% {cy}%", z) for cx, cy, z in CROPS[scene]]
    cropn = [((100 - cx if mirror else cx) / 100, cy / 100, min(z, 1.5)) for cx, cy, z in CROPS[scene]]   # the same spots as numbers, for photo placeholders
    return dict(scene=scene, tone=tone, alt=alt, crops=crops, cropn=cropn)


def S(P, name, nth=0):
    return [d for n, d in P["sections"] if n == name][nth]


def idx(P, name, nth=0):
    return [i for i, (n, _) in enumerate(P["sections"]) if n == name][nth]


def after(P, name, new, nth=0):
    P["sections"].insert(idx(P, name, nth) + 1, new)


def move(P, name, anchor):
    """Move the first `name` section to sit straight after the first `anchor` section."""
    item = P["sections"].pop(idx(P, name))
    P["sections"].insert(idx(P, anchor) + 1, item)


def swap(o, pairs):
    """Replace text everywhere inside a page definition."""
    if isinstance(o, str):
        for a, b in pairs:
            o = o.replace(a, b)
        return o
    if isinstance(o, list):
        return [swap(x, pairs) for x in o]
    if isinstance(o, tuple):
        return tuple(swap(x, pairs) for x in o)
    if isinstance(o, dict):
        return {k: swap(v, pairs) for k, v in o.items()}
    return o


# A testimonial beside the price should answer the price worry, and should not repeat a quote used elsewhere on the page.
PRICE_QUOTES = {
    4: ("The fee has not moved in 2 years, and I have not opened a spreadsheet in that time either.", "Mick D.", "Landscaper, Nambour"),
    7: ("I nearly did not join because of the price. I made it back in week 6 by letting go of 1 client I should have dropped years ago.", "Carla V.", "Signwriting business"),
    8: ("I took the middle option. The templates paid for it on the first proposal I sent.", "Noah B.", "Brand designer"),
    9: ("I joined for the co-working sessions and stayed for the answers. $29 is less than 1 bad supplier order.", "Wen L.", "Ceramicist"),
    10: ("The fee made me pause. Then 1 conversation at the first retreat stopped a hire that would have cost me twice that.", "Founder", "22-person performance agency"),
    11: ("We chose the Full Identity. Knowing the price and the dates before we began is why we said yes.", "Dr Amara Osei", "Paediatric clinic owner"),
    12: ("I bought the bundle instead of 3 separate files. I have used 5 of the 6 already.", "Sian M.", "Health coach"),
    13: ("The proposal was 2 pages with 1 fixed price. Procurement approved it inside a week.", "Learning and development lead", "State government agency"),
    27: ("I hesitated at the cabin price. Having my own deck to think on turned out to be half the value.", "Priya K.", "Studio founder"),
}


def first_quote(P):
    q, name, role = PRICE_QUOTES[P["n"]]
    return dict(q=q, name=name, role=role)


def u01(P):
    hero = S(P, "hero_split")
    hero.update(reassure="25 minutes by video. No pitch. A clear no is completely fine.", float2=("shield", "ICF-accredited coach", "Professional Certified Coach"))
    S(P, "capture")["proof"] = "Read by **3,100 managers** every Monday"
    P["sticky"] = dict(text="**Free 25-minute fit call**|No pitch. A clear no is fine.", cta=("Book A Call", "#call"))
    return [("cre", "The reassurance line now sits directly under the hero button, not only at the foot of the page."),
            ("mecl", "A stack of client faces and the 214-managers proof line sit beside the main button. The email sign-up carries its own reader count."),
            ("fold", "Audience, promise, button, reassurance and proof all fit in the first screen. On a phone the button stays in reach in a bar at the bottom.")]


def u02(P):
    hero = S(P, "hero_split")
    hero.update(reassure="A 30-minute conversation with Marcus. No proposal until you ask for one.", float2=("chart", "81% to 94%", "realisation rate, 9 months"))
    m = S(P, "metrics")
    m.update(tone="alt", cta=("Request A Conversation", "#talk"),
             chart=dict(title="Before and 9 months later", rows=[("Realisation rate (%)", 81, 94), ("Partner hours on fee disputes, a month", 31, 7)]))
    S(P, "quotes")["tone"] = ""
    move(P, "steps", "quotes")
    S(P, "steps")["tone"] = "alt"
    P["sticky"] = dict(text="**Pricing advisory**|8 firms a year. Next start: February.", cta=("Start A Conversation", "#talk"))
    return [("cases", "The case study moved up to sit straight after the problem, ahead of the method, and gained a chart and its own button."),
            ("cre", "The hero button now carries the line a managing partner needs: no proposal until you ask."),
            ("mecl", "The headline result (81% to 94%) floats beside the portrait, next to the main button.")]


def u03(P):
    for t in S(P, "bento")["tiles"]:
        if t["kind"] == "form":
            t["proof"] = "Join **42,000 freelancers** who read it every Sunday"
    pr = S(P, "products")
    tags = ["6 Notion templates", "90 min video + calculator", "Replay + slides"]
    for x, t in zip(pr["items"], tags):
        x["tag"] = t
    pr["under"] = "Instant access. 14-day refund."
    for tiles in (S(P, "bento", 0)["tiles"], S(P, "bento", 1)["tiles"]):
        for t in tiles:
            if t.get("cta") and t["cta"][0] == "Read the story":
                t["cta"] = ("Read the story", "about.html")
            if t.get("cta") and t["cta"][0] == "Enquire":
                t["cta"] = ("Enquire", "contact.html")
    P["refund"] = "Digital products come with a 14-day refund. Email within 14 days of buying and you get your money back."
    P["sticky"] = dict(text="**The Sunday System**|Free. 4 minutes to read.", cta=("Subscribe", "#newsletter"))
    return [("fields", "The sign-up tile asks for an email address and nothing else. It now shows the reader count and faces right under the button."),
            ("images", "Each product picture carries a plain label saying what is inside, and the refund terms sit beside every buy button."),
            ("links", "The 3 most-forwarded issues come first in the start-here list, in order of popularity.")]


def u04(P):
    tel = "tel:+61755500142"
    P["cta"] = ("Call (07) 5550 0142", tel)
    hero = S(P, "hero_split")
    hero.update(cta=("Call (07) 5550 0142", tel), cta2=("Get A Fixed Quote", "#contact"),
                reassure="Open Monday to Thursday 8:30am to 5pm, Friday to 3pm. Shop 4, 18 Example Parade, Mooloolaba.")
    c = S(P, "contact")
    c["form"]["fields"] = [("Your name", "text", "First and last name"), ("Phone or email", "text", "Whichever you prefer"),
                           ("What do you need a hand with?", "area", "For example: 2 quarters behind on BAS, 4 staff")]
    c["call"] = ("(07) 5550 0142", tel, "Answered by a real person, Monday to Friday.")
    pr = S(P, "pricing")
    pr["under"] = "Your fixed price in writing within 1 business day."
    pr["quote"] = first_quote(P)
    S(P, "cta").update(cta=("Call (07) 5550 0142", tel), cta2=("Get A Fixed Quote", "#contact"))
    P["sticky"] = dict(text="**Tideline Bookkeeping**|Open weekdays from 8:30am", cta=("Call Now", tel))
    P["refund"] = "Our promise: your BAS is lodged on time or that quarter's lodgement is free. Monthly plans can be stopped with 30 days' notice."
    return [("local", "Services, printed prices, the phone number, the street address and opening hours are all on the page as text. Hours and address now sit in the first screen."),
            ("call", "The main button in the hero, the header and the closing section is a tap-to-call link. Phones get a call bar fixed to the bottom of the screen."),
            ("three", "The quote form went from 4 fields to 3."), ("phone", "It no longer demands a phone number: 1 field takes a phone number or an email, whichever the person prefers."),
            ("mecl", "A local review now sits directly under the price cards.")]


def u05(P):
    S(P, "hero_split").update(float2=("users", "380 women", "coached back into work"))
    d = P["brand"]["domain"]
    i = idx(P, "doors")
    P["sections"].insert(i + 1, ("contact", dict(_="Contact details on the About page, so a reassured reader can act straight away", tone="alt", eyebrow="Get in touch",
        h="Ask Me *Anything First*", paras=["Not sure coaching is the right step yet? Send me a note. I read every email myself and I will tell you honestly what I would do in your position."],
        cta=("Email Dana", f"mailto:dana@{d}"), details=[("Email", f"dana@{d}"), ("Based in", "Adelaide, South Australia. Coaching online, Australia-wide"), ("Reply time", "Within 2 business days")])))
    P["brand"]["contact"] = f"dana@{d}"
    P["sticky"] = dict(text="**Career coaching**|For women returning to work", cta=("Work With Dana", "#work"))
    return [("about", "The page is built to reassure: the story opens with Dana's own 6-year break, the numbers come with their caveat, and the facts match every other page."),
            ("clarity", "Email, location and reply time are now on the About page itself, so a reader who has just been reassured does not have to go looking."),
            ("mecl", "The 380-women proof number floats beside the portrait, next to the main button.")]


def u06(P):
    move(P, "split", "logos")
    S(P, "split").update(tone="", reassure="3 minutes. Captions on. A text summary sits under the video.")
    S(P, "cards")["tone"] = "alt"
    hero = S(P, "hero_stage")
    hero["reassure"] = "Keynotes from $12,000 plus travel. A reply within 1 business day."
    c = S(P, "contact")
    c["form"]["fields"] = [("Your name", "text", "First and last name"), ("Email", "email", "you@organisation.com"),
                           ("Event date, city and audience size", "text", "For example: 14 May, Brisbane, 400 people")]
    i = idx(P, "contact")
    P["sections"].insert(i, ("pricing", dict(_="Fee guide: printed, because budget fit is the first thing a planner checks", id="fees", eyebrow="Fee guide",
        h="Fees, *Up Front*", tiers=[
            dict(name="Virtual keynote", price="$7,500", per="45 minutes", desc="Live from a studio, with Q and A.", feats=["Tailoring call with your team", "Studio-quality video and sound", "Recording rights for 30 days"],
                 cta=("Check A Date", "#book")),
            dict(name="Keynote", price="$12,000", per="plus travel", desc="On stage, 45 to 60 minutes.", hot=True, badge="Most booked",
                 feats=["Tailoring call with your team", "Slides in your event format", "Stays for the Q and A and the break after"], cta=("Check A Date", "#book")),
            dict(name="Keynote + workshop", price="$18,000", per="plus travel", desc="The keynote, then 90 minutes with your leaders.",
                 feats=["Everything in the keynote", "A working session for up to 40 leaders", "A 1-page team focus plan"], cta=("Check A Date", "#book"))],
        under="Not-for-profit rates on request.", note="Australian dollars, plus GST. Travel is quoted at cost from Brisbane.")))
    S(P, "bios").update(cta=("Download The One Sheet (PDF)", kit.connect("one sheet pdf")))
    P["sticky"] = dict(text="**Keynotes from $12,000**|Reply within 1 business day", cta=("Check A Date", "#book"))
    return [("planners", "A printed fee guide with 3 formats now sits above the enquiry form, and the starting fee is stated under the hero button."),
            ("reel", "The speaker reel moved from the middle of the page to straight under the client strip. The media kit gained a one-sheet download."),
            ("three", "The enquiry form went from 4 fields to 3, and the reply time is stated at the button.")]


def u07(P):
    P["ann"] = "February intake · 24 places · Enrolment closes **30 January**"
    hero = S(P, "hero_center")
    hero.update(reassure="30-day guarantee: do the first 4 weeks, then decide.", proof="Owners in the last intake freed a median of **9 hours a week**")
    hero["under"]["cap"] = "A 2-minute welcome from Leila"
    S(P, "modules").update(cta=("Join The February Intake", "#join"))
    pr = S(P, "pricing")
    pr.update(under="30-day guarantee. A full refund if it is not right for you.", quote=first_quote(P))
    P["sticky"] = dict(text="**The Steady Founder**|From $1,300 a month. 30-day guarantee.", cta=("Join", "#join"))
    P["refund"] = ("The Steady Founder has a 30-day guarantee. Come to the first 4 calls and complete the first module. "
                   "If you do not think the program is right for you, email by day 30 for a full refund.")
    return [("cre", "The 30-day guarantee is stated under the hero button and again under each payment button, not only in its own section further down."),
            ("mecl", "A member's result now sits beside the price, and the median hours freed sits beside the first button."),
            ("clarity", "Start date, length, group size and guarantee are in the first screen as 4 plain labels, and repeated in a bar above the header."),
            ("repeat", "A join button was added after the curriculum, so a convinced reader does not have to scroll to find one.")]


def u08(P):
    hero = S(P, "hero_split")
    mods = S(P, "modules")["items"]
    hero["visual"] = dict(kind="lesson", label="Video brief: lesson 1 as a free preview, with captions", cap="Free preview · Lesson 1",
                          items=[("done", f"1. {mods[0]['h']}", "40 min"), ("on", f"2. {mods[1]['h']}", "55 min"), ("", f"3. {mods[2]['h']}", "60 min")])
    hero.update(reassure="14-day refund. No form and no questions.", proof="**2,300 designers** enrolled · 4.9 out of 5 from 640 reviews")
    pr = S(P, "pricing")
    pr["tiers"] = list(reversed(pr["tiers"]))
    pr.update(under="14-day refund. Lifetime access.", quote=first_quote(P))
    P["sticky"] = dict(text="**Proposals That Close**|From $290. 14-day refund.", cta=("Enrol", "#enrol"))
    P["refund"] = "Proposals That Close has a 14-day refund. Email within 14 days of enrolling for a full refund. No form and no questions."
    return [("hubspot", "The 3 options now run from dearest to cheapest, with the middle 1 highlighted, so the first price a reader sees is the anchor."),
            ("tiers", "3 options, 1 clearly marked as the choice most students make."),
            ("cre", "The 14-day refund is stated under the hero button and under every enrol button."),
            ("mecl", "Student numbers and the review score sit beside the first button, and a student quote sits beside the prices."),
            ("images", "The hero shows the course itself: the free preview lesson and the first 3 modules, in place of a generic picture.")]


def u09(P):
    P.update(swap({k: P[k] for k in ("sections", "title", "desc", "why", "principles", "borrow", "blurb", "seo") if k in P},
                  [("7-day", "14-day"), ("7-Day", "14-Day"), ("7 days free", "14 days free"), ("7 Days Free", "14 Days Free")]))
    hero = S(P, "hero_split")
    hero.update(reassure="Then $29 a month. Cancel in 2 clicks.", proof="**900 makers** at the table · 92% stay past month 3")
    pr = S(P, "pricing")
    mo, yr = pr["tiers"]
    mo.update(hot=True, badge="Start here")
    yr.update(hot=False, eq="Works out at **$24 a month**", desc="2 months free, billed once a year.")
    pr.update(under="Cancel in 2 clicks. We email you 2 days before the trial ends.", quote=first_quote(P))
    P["sticky"] = dict(text="**14 days free**|Then $29 a month. Cancel in 2 clicks.", cta=("Start Trial", "#join"))
    P["refund"] = "Your first 14 days are free. After that you can cancel in 2 clicks from your account page and you will not be charged again. Yearly plans are refunded in full within 14 days of payment."
    return [("trial", "The free trial is 14 days, matching the median, and the monthly plan is now the highlighted way in because monthly plans convert better from a trial."),
            ("annual", "The yearly plan shows its monthly equivalent ($24 a month) so the saving is easy to see for members ready to commit."),
            ("cre", "Price after the trial and the 2-click cancel sit directly under the hero button and under each plan button."),
            ("mecl", "Member numbers, the 92% retention figure and a member's words sit beside the join buttons.")]


def u10(P):
    hero = S(P, "hero_center")
    hero["reassure"] = "Applying is not committing. Vivienne reads and answers every application herself, within 5 working days."
    pr = S(P, "pricing")
    pr.update(quote=first_quote(P), under="5 places open for 2027. Applications close 28 February 2027.")
    c = S(P, "contact")
    c["form"]["fields"] = [f for f in c["form"]["fields"] if f[0] != "Team size"]
    c["form"]["fields"][1] = ("Agency, website and team size", "text", "For example: Northfold, northfold.example, 34 people")
    c["details"].append(("Reply time", "Within 5 working days, from Vivienne"))
    P["sticky"] = dict(text="**The 2027 Table**|5 places open. Closes 28 February.", cta=("Apply", "#apply"))
    return [("mecl", "A member's words now sit beside the investment, where the decision is made."),
            ("cre", "The first button says what applying does and does not commit you to, and when you will hear back."),
            ("three", "The application went from 5 fields to 4. It keeps 1 open question on purpose: an application should take a few minutes of thought."),
            ("clarity", "The price stays printed in full, with the payment schedule and what is not included.")]


def u11(P):
    S(P, "hero_center")["reassure"] = "50% to book, 50% on delivery. Dates agreed before you pay."
    pr = S(P, "pricing")
    pr.update(under="Fixed scope, fixed fee, fixed dates.", quote=first_quote(P))
    after(P, "pricing", ("matrix", dict(_="Comparison table: every package side by side, so the difference is seen in 1 look", eyebrow="Side by side",
        h="What Is In *Each Package*", hot=2, cols=["", "Brand Sprint", "Full Identity", "Studio Retainer"], rows=[
            ("Positioning line and key messages", True, True, "Reviewed quarterly"), ("Brand guide", "1 page", "30 pages", "Kept up to date"),
            ("Logo suite, colour and type system", False, True, "Extended as needed"), ("Website and social templates", False, True, True),
            ("Campaign and launch design", False, False, True), ("Timeframe", "5 working days", "6 weeks", "Monthly, 3-month minimum"),
            ("Price", "$2,400", "$9,800", "$1,900 a month")],
        note="Not sure which column you are in? The intro call is free and takes 30 minutes.")))
    P["sticky"] = dict(text="**Packages from $2,400**|Fixed scope, fee and dates", cta=("Compare", "#packages"))
    return [("hubspot", "1 package is highlighted as the choice most clients make, and lifted above the other 2."),
            ("tiers", "3 packages, each with its price printed, followed by a side-by-side table so nobody has to compare bullet lists by eye."),
            ("mecl", "A client's words sit directly under the prices."), ("cre", "The payment terms sit under every package button.")]


def u12(P):
    refund = "Instant download. 7-day refund if a file is faulty or not as described."
    S(P, "hero_split")["reassure"] = refund
    after(P, "hero_split", ("trust", dict(_="Trust strip: delivery, format, licence and refund, answered before anyone asks", tone="alt", items=[
        ("spark", "Instant download"), ("doc", "Edit in Canva or Google Docs"), ("users", "Use with unlimited clients"), ("shield", "7-day refund if faulty")])))
    pr = S(P, "products")
    for x, t in zip(pr["items"], ["12 pages, in your colours", "5 linked files", "2-page proposal + agreement", "40 mix-and-match pages", "1 page per client", "30 ready-made posts"]):
        x["tag"] = t
    pr["under"] = "Instant download. 7-day refund if faulty."
    b = S(P, "pricing")
    b.update(under=refund, quote=first_quote(P))
    P["sticky"] = dict(text="**Templates from $19**|Instant download", cta=("Shop", "#shop"))
    P["refund"] = "Because downloads are instant, refunds are offered within 7 days if a file is faulty or not as described. Your rights under Australian Consumer Law apply."
    return [("images", "Every product picture now carries a plain label saying what is in the file, because the picture is the first thing a shopper studies."),
            ("images", "The refund terms are printed beside every buy button and in a strip under the hero, not left to the questions at the bottom."),
            ("mecl", "A buyer's words sit beside the bundle price."), ("cre", "Delivery and refund terms sit directly under the first button.")]


def u13(P):
    S(P, "hero_split").update(eyebrow="Feedback That Lands · A workshop for managers", proof="**4,200 managers** trained in 90 workplaces",
                              sub="A half-day workshop built on practice, not slides. Your managers have the talks they keep putting off, within a week.",
                              reassure="A written proposal in 2 business days. No sales call unless you ask.")
    m = S(P, "metrics")
    rows = []
    for a, b, c in m["items"]:
        try:
            rows.append((a, float(b.strip("%$").replace(",", "")), float(c.strip("%$").replace(",", ""))))
        except ValueError:
            pass
    if rows:
        m["chart"] = dict(title="Before and after the workshop", rows=rows[:2])
    S(P, "pricing").update(quote=first_quote(P), under="Indicative. Your proposal has a fixed price.")
    c = S(P, "contact")
    c["form"]["fields"] = [("Your name", "text", "First and last name"), ("Work email", "email", "you@organisation.com"),
                           ("Group size and preferred month", "text", "For example: 18 managers, March")]
    c["details"].append(("Reply time", "A written proposal within 2 business days"))
    P["sticky"] = dict(text="**Workshops from $4,500**|Proposal within 2 business days", cta=("Get A Proposal", "#enquire"))
    return [("cases", "The results table gained a before-and-after chart, so a buyer scanning the page sees the outcome without reading the table."),
            ("three", "The enquiry form went from 5 fields to 3, and the reply time is stated on the page."),
            ("hubspot", "1 format is highlighted as the most booked."), ("mecl", "A client's words sit directly under the prices."),
            ("read", "The opening lines were rewritten in shorter, plainer sentences. The measured reading grade is in the audit table.")]


def u14(P):
    hero = S(P, "hero_form")
    hero["form"]["fields"] = [("Email", "email", "you@email.com")]
    hero["form"]["proof"] = "Used by **11,000 new coaches**"
    P["sticky"] = dict(text="**Free 6-page script**|In your inbox in 2 minutes", cta=("Get The Script", "#signup"))
    return [("fields", "The form went from 2 fields to 1. It asks for an email address and nothing else."),
            ("read", "The headline, promise and bullets were checked for reading level. The measured grade is in the audit table below."),
            ("mecl", "The 11,000-coaches proof line and 2 faces now sit inside the form, under the button."),
            ("webfold", "Headline, promise and form share the first screen on a laptop. On a phone the form now comes before the guide cover, and a bar at the bottom jumps straight to it.")]


def u15(P):
    P.update(swap({k: P[k] for k in ("sections", "title", "desc", "why", "principles", "borrow", "blurb", "seo") if k in P}, [("Thursday 12 March", "Thursday 11 March")]))
    P["ann"] = "Free live masterclass · **Thursday 11 March, 12:00pm AEDT** · 48-hour replay"
    hero = S(P, "hero_form")
    hero["form"].update(name="masterclass", cals=trust.cals(EVENTS[15]))
    P["cta"] = ("Save My Seat", "#signup")
    S(P, "cta")["cta"] = ("Save My Seat", "#signup")
    P["sticky"] = dict(text="**Thursday 11 March, 12pm AEDT**|Free. 60 minutes.", cta=("Save My Seat", "#signup"))
    return [("webform", "The form stays at 2 fields: first name and email."),
            ("webfold", "Headline, subheadline and form sit together in the first screen, with date, time, length and replay as 4 plain labels."),
            ("time", "Add-to-calendar links sit under the button and the form says a reminder is coming, because about half of sign-ups do not turn up without one."),
            ("time", "The date and time are repeated in a bar above the header and in the phone action bar.")]


def u16(P):
    q = S(P, "quiz")
    q["result"]["gate"] = dict(label="Want the 1-page plan for your style? (optional)", button="Email My Plan",
                               skip="No email needed. Your result stays on screen either way.")
    q["styles"] = {"w": ("Writing", "The Quiet Authority", "You build trust through depth, not volume. 1 strong article a month will do more for you than 20 posts."),
                   "s": ("Speaking", "The Room Reader", "You are at your best live. 1 talk, workshop or podcast interview a month will do more for you than a content calendar."),
                   "r": ("Referral", "The Connector", "People find you through other people. A simple habit of 2 introductions a week will outperform any campaign."),
                   "m": ("Showing work", "The Maker", "Your work does the talking. Show 1 finished piece a week, with the thinking behind it, and let it sell for you.")}
    q["questions"] = [
        ("A stranger asks what you do. You would rather:", [("s", "Explain it in a 2-minute chat"), ("w", "Send them something you wrote"), ("r", "Introduce them to a happy client"), ("m", "Show them a piece of your work")]),
        ("You have a free afternoon for marketing. You:", [("w", "Write 1 long, useful article"), ("s", "Record a conversation or go live"), ("r", "Call 3 past clients to catch up"), ("m", "Finish a project and share it")]),
        ("The compliment you hear most:", [("m", "Your work is beautiful"), ("s", "You explain things so clearly"), ("w", "I saved what you wrote"), ("r", "Everyone says I should talk to you")]),
        ("At an industry event you are usually:", [("r", "Introducing 2 people who should meet"), ("s", "In the middle of a lively conversation"), ("w", "Taking notes for something to write later"), ("m", "Showing someone a recent project")]),
        ("Your best client found you through:", [("w", "Something you wrote"), ("s", "Hearing you speak"), ("r", "A recommendation"), ("m", "Seeing your work")]),
        ("When you have an idea to share, you first:", [("w", "Draft it in a document"), ("s", "Talk it through out loud"), ("r", "Tell the person who most needs it"), ("m", "Make an example of it")]),
        ("You feel most like yourself when you are:", [("m", "Making something"), ("w", "Thinking on the page"), ("s", "In front of a room"), ("r", "Bringing people together")]),
        ("If you could keep only 1 channel, it would be:", [("s", "A stage or a podcast"), ("w", "A newsletter"), ("r", "Your contact list"), ("m", "Your portfolio")]),
    ]
    S(P, "hero_center")["reassure"] = "Your result shows on screen. No email needed."
    P["sticky"] = dict(text="**8 questions. 3 minutes.**|No email needed", cta=("Start The Quiz", "#quiz"))
    return [("quiz", "Length is stated before the start (8 questions, 3 minutes) and a progress bar shows on every question, because 2 in 3 people who start will finish if they can see the end."),
            ("gate", "The result shows without an email. An optional field offers the 1-page plan, and the skip is stated in plain words."),
            ("cre", "The no-email promise sits directly under the start button.")]


def u17(P):
    P.update(swap({k: P[k] for k in ("sections", "title", "desc", "why", "principles", "borrow", "blurb", "seo") if k in P}, [("Monday 2 March", "Monday 1 March")]))
    P["ann"] = "Free 5-day challenge · Starts **Monday 1 March** · 20 minutes a day"
    hero = S(P, "hero_form")
    hero["form"]["fields"] = [("Email", "email", "you@email.com")]
    hero["form"].update(name="challenge", cals=trust.cals(EVENTS[17]))
    P["cta"] = ("Join Free", "#signup")
    S(P, "cta")["cta"] = ("Join The Sprint", "#signup")
    P["sticky"] = dict(text="**Starts Monday 1 March**|Free. 20 minutes a day.", cta=("Join Free", "#signup"))
    return [("fields", "The form went from 2 fields to 1."),
            ("time", "The daily time (20 minutes) is in the headline area, the bar above the header and the phone action bar, and add-to-calendar links sit under the button."),
            ("read", "The copy was checked for reading level. The measured grade is in the audit table below.")]


def u18(P):
    hero = S(P, "hero_form")
    hero["form"]["proof"] = "**412 designers** are already on the list"
    hero["after"] = "What happens next: 1 email to confirm, then the founding rate before anyone else sees it."
    P["sticky"] = dict(text="**Opens April 2027**|30 founding places", cta=("Join The Waitlist", "#signup"))
    return [("fields", "The form stays at 1 field."), ("mecl", "The size of the waitlist and 3 faces sit inside the form, under the button."),
            ("cre", "The line under the form says exactly what happens after you join, so the sign-up carries no surprise.")]


def u19(P):
    hero = S(P, "hero_form")
    hero["visual"] = None
    hero["form"] = dict(name="call", title="Request a time", button="Request My Call", note="Ngozi replies within 1 business day with 3 times to choose from.",
                        fields=[("Your name", "text", "First and last name"), ("Email", "email", "you@clinic.com"), ("Best days and times for you", "text", "For example: Tuesday or Thursday mornings")])
    hero["after"] = "No phone number needed. You get a calendar invite with a video link, and a reminder the day before."
    hero["proof"] = "**Alan, Mel and Grace** all started with this call. Their words are below."
    S(P, "cta")["cta"] = ("Choose A Time", "#signup")
    P["sticky"] = dict(text="**Free 30-minute call**|Written summary within 24 hours", cta=("Choose A Time", "#signup"))
    return [("three", "The request form has 3 fields: name, email and the times that suit. No calendar tool is needed to use the page, and 1 can be dropped in later."),
            ("phone", "The page says in plain words that no phone number is needed and that the invite arrives by email."),
            ("cre", "What happens after you book is stated directly under the calendar."), ("mecl", "3 named clients sit beside the promise, with their full quotes further down.")]


def u20(P):
    lb = S(P, "linkbio")
    dest = [kit.connect("newsletter signup"), "contact.html", kit.connect("course"), kit.connect("podcast"), "about.html"]
    lb["links"] = [tuple(l) + (hr,) for l, hr in zip(lb["links"], dest)]
    lb["feature"]["cta"] = (lb["feature"]["cta"][0], kit.connect("calculator"))
    lb["proof"] = "**The Friday Money Minute** is read by 9,200 freelancers"
    lb["feature"]["reassure"] = "Free. No sign-up. Takes 60 seconds."
    return [("links", "The page holds 1 featured action and 5 links, 6 in all, under the 7 that performs best."),
            ("links", "The free calculator sits first and largest, because the first link takes the most taps. Paid offers follow in order of commitment."),
            ("cre", "The featured button carries its own reassurance: free, no sign-up, 60 seconds.")]


def u21(P):
    hero = S(P, "hero_article")
    hero.update(short_h="The Short Version", short=[
        "**Client:** Coastline Physio, a 3-practitioner clinic.", "**Problem:** $2,800 a month on ads and a diary only 61% full.",
        "**What we changed:** a written treatment plan, rebooking at the table and a day-2 message.",
        "**Result in 90 days:** 93% of slots filled, ad spend down to $900, monthly revenue up from $41,000 to $63,500."],
        toc=[("The problem", "problem"), ("What we changed", "changed"), ("What happened", "happened")])
    m = S(P, "metrics")
    m["chart"] = dict(title="Day 1 and day 90", rows=[("Appointment slots filled (%)", 61, 93), ("Patients rebooking before they leave (%)", 38, 81)])
    a = S(P, "article")
    ids = {"The Problem Was Not The Front Door": "problem", "What We Changed": "changed", "What Happened": "happened"}
    blocks = []
    for b in a["blocks"]:
        if b[0] == "h2" and b[1] in ids:
            b = ("h2", b[1], ids[b[1]])
        blocks.append(b)
        if b[0] == "list":
            blocks.append(("table", ["Week", "Change", "Who does it", "Time it takes"], [
                ("Week 1", "A written treatment plan card", "The practitioner", "2 minutes a patient"),
                ("Week 3", "Rebook before the patient stands up", "The practitioner", "1 minute a patient"),
                ("Week 5", "A 2-line message on day 2", "The practitioner", "5 minutes a day")], None, "The 3 changes, in the order they were made."))
    a["blocks"] = blocks
    S(P, "quotes")["cta"] = ("Book A Clinic Review", "#next")
    P["sticky"] = dict(text="**Free clinic review**|45 minutes. We count first.", cta=("Book A Review", "#next"))
    return [("first30", "A 4-line summary of client, problem, change and result now opens the page, so the whole story sits in the first third of the text."),
            ("first30", "The 3 changes are set out in a table as well as in the story."), ("cases", "The headline numbers gained a chart beside the table."),
            ("aio", "The byline links to a page about the author, and the page shows its publish date. The author box stays, but the page does not rely on it.")]


def u22(P):
    S(P, "hero_center")["reassure"] = "Named where clients have agreed. Unedited apart from length."
    S(P, "quotes").update(cta=("Book A Conversation", "#talk"))
    P["sticky"] = dict(text="**First conversation**|45 minutes, confidential", cta=("Book A Conversation", "#talk"))
    return [("cases", "Every quote leads with the result in a label, so a reader scanning the wall sees 9 outcomes before reading a word of praise."),
            ("mecl", "Each quote carries a face, a name or role and a result. A button now follows the wall instead of waiting for the end of the page."),
            ("clarity", "The headline numbers state how they were collected, and a results line sits in the footer.")]


def u23(P):
    hero = S(P, "hero_article")
    hero.update(read="7 minute read", updated="9 November 2026", updated_iso="2026-11-09",
                toc=[("Why most bios fail", "why"), ("The 4-sentence structure", "structure"), ("Use the same bio everywhere", "same")])
    a = S(P, "article")
    ids = {"Why Most Bios Fail": "why", "The 4-Sentence Structure": "structure", "Use The Same Bio Everywhere": "same"}
    blocks = []
    for b in a["blocks"]:
        if b[0] == "h2" and b[1] in ids:
            b = ("h2", b[1], ids[b[1]])
        if b[0] == "p" and b[1].startswith("A bio is not about you."):
            b = ("p", b[1] + " And they have seconds to decide: eye-tracking research from Nielsen Norman Group found 57% of viewing time goes to the first screen of a page.")
        if b[0] == "p" and b[1].startswith("Once you have it"):
            b = ("p", b[1] + " An Ahrefs study of 75,000 brands found that mentions of a brand across the web were the strongest signal for showing up in AI answers.")
        blocks.append(b)
        if b[0] == "quote":
            blocks.append(("table", ["", "Credential-led bio", "Client-led bio"], [
                ("Opens with", "A qualification", "The person you help"), ("Proof", "Adjectives", "1 number or fact"),
                ("Ends with", "A hobby", "The next step"), ("Length", "150 words or more", "Under 80 words")], 2, "The 2 kinds of bio, side by side."))
    blocks.append(("sources", [
        ("Scrolling and Attention", "https://www.nngroup.com/articles/scrolling-and-attention/", "Nielsen Norman Group"),
        ("An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)", "https://ahrefs.com/blog/ai-overview-brand-correlation/", "Ahrefs")]))
    a["blocks"] = blocks
    S(P, "capture")["name"] = "template"
    P["sticky"] = dict(text="**The 4-sentence bio**|Free 1-page template", cta=("Get The Template", "#template"))
    return [("first30", "The answer comes first: the 4 sentences are in a box above the opening paragraph, inside the first third of the page."),
            ("first30", "A side-by-side comparison table was added, and the article now cites and links its 2 outside sources."),
            ("aio", "The page shows a publish date and an updated date, links the byline to a page about the author, and gained jump links to each section.")]


def u24(P):
    after(P, "player", ("shownotes", dict(_="Show notes and transcript as text, because the words about an episode are what search engines and AI tools read",
        id="notes", tone="alt", eyebrow="Episode 112", h="Show Notes And *Transcript*", stamps=[
            ("02:10", "Why Margot left the bar after 22 years"), ("11:45", "The pay cut, in real numbers"), ("18:20", "A second apprenticeship at 47"),
            ("29:30", "What her old colleagues said"), ("38:05", "The advice she would give herself at 40")],
        transcript=[("Lois", "You went from running a courtroom to being the newest person in a kitchen. What did that feel like on day 1?"),
                    ("Margot", "Humbling, and oddly restful. For 22 years I was the person with the answer. Now I was the person asking where the flour was kept.")],
        more="Read the full transcript")))
    P.setdefault("ld", {})["episode"] = dict(name="From Barrister To Baker At 47, With Margot Lindley", number=112, date="2026-11-10")
    S(P, "capture")["proof"] = "Rated **4.8** from 2,300 ratings"
    P["sticky"] = dict(text="**The Second Act**|New episode every Tuesday", cta=("Play Latest", "#latest"))
    return [("podtext", "The latest episode now has show notes with timestamps and a transcript excerpt as real text on the page, with a link to the full transcript."),
            ("podld", "The structured data names the show and now the latest episode too. No rich-result markup is added, because Google shows none for podcasts."),
            ("mecl", "The show's rating sits beside the email sign-up button.")]


def u25(P):
    hero = S(P, "hero_form")
    hero["form"]["proof"] = "Read by **27,000 marketers and founders**"
    after(P, "stats", ("split", dict(_="A real sample issue, shown before anyone is asked to subscribe twice", eyebrow="See 1 first", flip=True,
        h="What Lands In Your Inbox *On Tuesday*",
        paras=["1 real landing page. 3 changes I would make, in the order I would make them. The reason for each, in plain words. That is the whole email."],
        bullets=["5 minutes to read", "No theory you cannot use the same day", "Every back issue is free in the archive"], cta=("Subscribe Free", "#signup"),
        visual=dict(kind="email", sender="The Tuesday Teardown", when="Tuesday, 7:00am", tag="Issue 164", subject="This pricing page hides its *best plan*",
                    lines=["Morning. This week: a pricing page with 4 plans and no recommendation.",
                           "**Change 1.** Mark 1 plan as the choice most people make.", "**Change 2.** Put the price in the first screen, not behind a toggle."]))))
    P["cta"] = ("Subscribe", "#signup")
    S(P, "cta")["cta"] = ("Subscribe Free", "#signup")
    P["sticky"] = dict(text="**Every Tuesday, 7am**|Free. 5 minutes to read.", cta=("Subscribe", "#signup"))
    return [("fields", "The form stays at 1 field: the email address."), ("mecl", "The reader count and 3 faces sit inside the form, under the button."),
            ("clarity", "A real sample issue is now shown on the page, so a reader can see exactly what they are signing up for before they do.")]


def u26(P):
    P["ann"] = "Out **3 March 2027** · Pre-orders are open"
    hero = S(P, "hero_split")
    hero.update(reassure="Paperback, ebook and audiobook. 248 pages.", proof="Early praise from **Ian Mbeki, Dr Clare Whitby and Rosa Delgado**")
    S(P, "capture")["proof"] = "18 pages. Sent as a PDF, straight away."
    P["sticky"] = dict(text="**Enough Clients**|Out 3 March 2027", cta=("Pre-Order", "#buy"))
    return [("mecl", "The names behind the early praise sit beside the pre-order button, with their full words further down."),
            ("cre", "Formats and length sit directly under the button, and the release date runs in a bar above the header."),
            ("clarity", "No research specific to book pages was found, so this page applies the general findings above and nothing more.")]


def u27(P):
    S(P, "hero_stage")["reassure"] = "A $500 deposit holds your place. Full refund until 14 March 2027."
    S(P, "schedule").update(cta=("Reserve A Place", "#rooms"))
    S(P, "cards").update(cta=("Reserve A Place", "#rooms"))
    pr = S(P, "pricing")
    pr.update(quote=first_quote(P), under="$500 deposit. Full refund until 14 March 2027.")
    after(P, "pricing", ("trust", dict(_="Trust strip: refund, transfer, what is included and who to ask", tone="alt", items=[
        ("shield", "Full refund until 14 March"), ("users", "Transferable after that"), ("check", "2 nights and all meals included"),
        ("mail", f"Questions: hello@{P['brand']['domain']}")])))
    S(P, "faq").update(ask="Add the dates to your calendar:", cals=trust.cals(EVENTS[27]))
    P["sticky"] = dict(text="**14 to 16 May 2027**|9 places left. From $2,950.", cta=("Reserve", "#rooms"))
    P["refund"] = "A $500 deposit holds your place. You can have a full refund until 14 March 2027. After that your place can be transferred to another person."
    return [("event", "Refund and transfer terms, what the price includes and a contact for questions now sit in a strip directly under the prices."),
            ("event", "The deposit and refund date are stated under the first button, and add-to-calendar links were added."),
            ("repeat", "A reserve button now follows the 3-day agenda and the inclusions, and a guest's words sit beside the price.")]


def u28(P):
    tel = "tel:+61855500163"
    P["cta"] = ("Call (08) 5550 0163", tel)
    S(P, "hero_center")["cta"] = ("Send A Message", "#form")   # a contact page's first screen should offer the form, not only describe it
    c = S(P, "contact")
    c["form"]["fields"] = [("Your name", "text", "First and last name"), ("Email or phone", "text", "Whichever you prefer"),
                           ("What is happening?", "area", "A few lines is plenty")]
    c["form"]["note"] = "We reply within 1 business day. Read only by Imelda."
    c["call"] = ("(08) 5550 0163", tel, "Monday to Friday, 9am to 5pm ACST.")
    S(P, "hero_center")["sub"] = "Imelda reads every message herself and replies within 1 business day. What you tell us stays private."
    P["sticky"] = dict(text="**Reply within 1 business day**|Confidential", cta=("Call Now", tel))
    return [("three", "The form went from 4 fields to 3. The role drop-down is gone."),
            ("phone", "1 field takes an email address or a phone number, so nobody is forced to give a number."),
            ("cre", "The reply time is stated at the button, and the thank-you page says what happens next, hour by hour."),
            ("call", "The phone number is printed large as a tap-to-call link, beside the form."),
            ("read", "The opening lines were rewritten in shorter, plainer sentences. The measured reading grade is in the audit table.")]


UP = {1: u01, 2: u02, 3: u03, 4: u04, 5: u05, 6: u06, 7: u07, 8: u08, 9: u09, 10: u10, 11: u11, 12: u12, 13: u13, 14: u14,
      15: u15, 16: u16, 17: u17, 18: u18, 19: u19, 20: u20, 21: u21, 22: u22, 23: u23, 24: u24, 25: u25, 26: u26, 27: u27, 28: u28}


def finish_links(P):
    """No button may lead nowhere. A button that pointed at its own section, at the closing section or at the top of the page
    now goes to the page where the action actually happens."""
    n = P["n"]
    if n in ACTIONS:
        P["action"] = ACTIONS[n]
        P["action_file"] = ACTIONS[n]["file"]
    P["thanks_kind"] = ACTIONS[n]["kind"] if n in ACTIONS else KINDS.get(n, "enquiry")
    names = [s for s, _ in P["sections"]]
    form_top = "hero_form" in names
    closing = {"#" + d["id"] for s, d in P["sections"] if s == "cta" and d.get("id")}
    target = kit.connect("checkout") if n in CHECKOUT else P["action_file"]

    def fix(c, own):
        if not c:
            return c
        label, href = c[0], c[1]
        if href == "#top":
            href = "#signup" if form_top else target
        elif href == own or href in closing:
            href = target
        return (label, href)

    for s, d in P["sections"]:
        own = "#" + d.get("id", "\0")
        for key in ("cta", "cta2"):
            if d.get(key):
                d[key] = fix(d[key], own)
        for t in d.get("tiers", []):
            t["cta"] = fix(t["cta"], own)
        if s == "feed":
            d.setdefault("link", {24: "episode", 21: "case study", 26: "retailer"}.get(n, "article"))
    if P.get("cta"):
        P["cta"] = fix(P["cta"], "\0")
    if P.get("sticky"):
        P["sticky"]["cta"] = fix(P["sticky"]["cta"], "\0")
    for ex in P.get("extra", []):
        for s, d in ex["sections"]:
            for key in ("cta", "cta2"):
                if d.get(key) and d[key][1].startswith("#"):
                    d[key] = (d[key][0], "index.html")


def apply(P):
    """Apply the research to 1 page, then record what was found and what changed."""
    P["art"] = art_for(P["n"])
    P["research"] = [(R[k][0], R[k][1], R[k][2], change) for k, change in UP[P["n"]](P)]
    finish_links(P)
    names = []
    for n, d in P["sections"]:
        if n == "quotes":
            names += [q["name"] for q in d["items"]]
            if any(q.get("result") for q in d["items"]) and "guaranteed" not in d.get("note", ""):
                d["note"] = (d.get("note", "") + " Results are individual and never guaranteed.").strip()
    if len(names) < 3:
        names += [f"{P['slug']} reader {i}" for i in range(4 - len(names))]
    P["faces"] = list(dict.fromkeys(names))
    return P
