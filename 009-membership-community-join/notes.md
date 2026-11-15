# 009 · Membership Or Community Join Page

**Group:** Offer Pages  
**For:** Creator, Coach  
**Style:** Retro Scrapbook (Caprasimo + Space Grotesk (+ Caveat notes))  
**Sample brand:** The Makers' Table (fictional)

A membership page that sells belonging before features: who is at the table, what a normal month looks like, and a price that is easy to say yes to.

## Why This Page Works

- It sells the people and the rhythm, not a feature list. A month-inside timeline makes the membership real.
- The trial terms are completely plain: card needed, reminder sent, cancel in 2 clicks. Clear exits make joining feel safe.
- Proof is about speed of help and belonging, which is what a member is really buying.
- The yearly plan states its saving in dollars and adds a price lock, so the larger commitment feels like the safer choice.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| The median free trial is 14 days, and monthly plans convert from a trial better than annual ones. | [Recurly, subscriber acquisition benchmarks](https://recurly.com/research/subscriber-acquisition-benchmarks) | The free trial is 14 days, matching the median, and the monthly plan is now the highlighted way in because monthly plans convert better from a trial. |
| Annual subscribers are 36% less likely to leave. | [Circle, subscription business models](https://circle.so/fr/blog/subscription-business-model-creators) | The yearly plan shows its monthly equivalent ($24 a month) so the saving is easy to see for members ready to commit. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | Price after the trial and the 2-click cancel sit directly under the hero button and under each plan button. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | Member numbers, the 92% retention figure and a member's words sit beside the join buttons. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Unity** (Robert Cialdini, Pre-Suasion (2016)) | The copy says who is at the table. People join people like them. |
| **Self-Determination Theory** (Edward Deci and Richard Ryan, Self-Determination Theory (2017)) | Co-working gives belonging, workshops build competence, and cancel-any-time protects autonomy. |
| **The Power Of Free** (Dan Ariely, Predictably Irrational (2008)) | A 14-day free trial removes the risk of the first step. |
| **Reactance** (Jack Brehm, A Theory of Psychological Reactance (1966)) | Cancel in 2 clicks is said 3 times. An easy exit lowers resistance to entering. |
| **Framing** (Kahneman and Tversky, The Framing of Decisions (1981)) | $290 a year is also framed as $24 a month and as 2 months free. |
| **STEPPS** (Jonah Berger, Contagious (2013)) | Wins threads and stall swaps are social currency: things members want to talk about. |
| **Peak-End Rule** (Daniel Kahneman, Thinking, Fast and Slow (2011)) | The timeline ends on the wins thread, so the last thing remembered is success. |

## Page Structure

1. Hero: who the community is for, the feeling, the price and the trial in the first screen
2. Numbers row: the community's vital signs
3. What you get: 4 things, each named as a benefit
4. A month inside: makes an invisible product concrete
5. Member voices: belonging, shown through specifics
6. 2 ways to join, with the annual saving in dollars
7. The usual membership worries
8. Closing call to action

## Search Card

- **Title:** Join The Makers' Table | Membership For Handmade Sellers
- **Description:** The Makers' Table is a $29 a month membership for people who sell what they make. Weekly co-working, a monthly workshop and 900 makers who answer questions fast.
- **Structured data:** WebSite, Organization, WebPage
- Membership content behind a login cannot be read by Google. This public page has to carry the whole pitch as text.
- Keep the price identical here, in your community listing and in your social bios.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Join The Makers' Table | Membership For Handmade Sellers” (56 characters). |
| Description says who the page is for | **Good** | “The Makers' Table is a $29 a month membership for people who sell what they make. Weekly co-working, a monthly workshop and 900 makers who answer questions fast.” (161 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “The Makers' Table”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://makerstable.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://makerstable.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 109 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 2 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Stop figuring it out on your own.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 690 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 1 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 12 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 2 sizes: 40KB for phones and 142KB for desktops. 7 photo files, the largest 114KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 7 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 5.6 and the whole page at grade 5.4 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 2.4 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 83ms. |
| Lighthouse scores | **Good** | Performance 97, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Start A 14-Day Free Trial”) ends 507px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 10 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 19 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 7.1 to 1 for body text and 5.4 to 1 for large text. On a phone: 7.2 to 1 for body text and 5.6 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 48KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Organization, WebPage. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | 1 image addresses named, all present in the site folder. The first version named portrait and shopfront files that did not exist. |
| Profile links (sameAs) | **Your turn** | The structured data carries no profile links, because a fictional brand has none and a placeholder would be published as fact. Add a sameAs list with your real profiles. |
| Google's Rich Results Test | **Couldn't check** | The test needs a live address. Run it on your page after launch. |

### Trust Signals

| Check | Result | What was seen |
|---|---|---|
| About, Contact, Privacy, Terms and Refunds exist and are linked from every page | **Fixed** | 5 real pages, linked in the footer of all 8 pages. In the first version these 5 footer links went nowhere. |
| Policy wording | **Your turn** | Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them. |
| Proof is written as text | **Good** | 4 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 2 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Odette Laurent, states their role and carries ProfilePage and Person markup tied to the business. |
| What Google and AI tools say about the brand today | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. Search your name, your brand and “[brand] review”, and read what ChatGPT, Perplexity and AI Overviews say. |
| Mentions on other sites, old profiles and copies of your work | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. Mentions on other sites are among the strongest signals for appearing in AI answers. |

### Competitors And Measurement

| Check | Result | What was seen |
|---|---|---|
| Who ranks for your terms, and content gaps | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |
| Search Console and Bing Webmaster Tools | **Your turn** | After launch: verify the site in both, submit sitemap.xml and ask Google to index the changed pages. |

### Things That Do Not Work

| Check | Result | What was seen |
|---|---|---|
| None of the popular shortcuts are used | **Good** | No llms.txt, no FAQ markup chasing a results bonus, no self-awarded review stars, no hidden text and no page rewritten into chunks for AI. |

## Photo Briefs

Each illustration stands in for a real photo. Shoot these to replace them.

- a real members' meet-up or a busy workbench. Hands, clay, mess

## Borrow This

- Show 1 real month as a dated timeline.
- Quote your median time to a first answer.
- State exactly how the trial ends.
- Express the yearly saving in dollars.

## Build Your Own

```text
Build me a membership or community join page for my business, modelled on sample 009 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: who the community is for, the feeling, the price and the trial in the first screen
2. Numbers row: the community's vital signs
3. What you get: 4 things, each named as a benefit
4. A month inside: makes an invisible product concrete
5. Member voices: belonging, shown through specifics
6. 2 ways to join, with the annual saving in dollars
7. The usual membership worries
8. Closing call to action

DESIGN DIRECTION
Retro Scrapbook. Kraft paper, tomato and teal, taped-on cards and handwritten notes. Warm and a bit cheeky.
Fonts: Caprasimo + Space Grotesk (+ Caveat notes) from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Robert Cialdini, Unity: The copy says who is at the table. People join people like them.
- Edward Deci and Richard Ryan, Self-Determination Theory: Co-working gives belonging, workshops build competence, and cancel-any-time protects autonomy.
- Dan Ariely, The Power Of Free: A 14-day free trial removes the risk of the first step.
- Jack Brehm, Reactance: Cancel in 2 clicks is said 3 times. An easy exit lowers resistance to entering.
- Kahneman and Tversky, Framing: $290 a year is also framed as $24 a month and as 2 months free.
- Jonah Berger, STEPPS: Wins threads and stall swaps are social currency: things members want to talk about.
- Daniel Kahneman, Peak-End Rule: The timeline ends on the wins thread, so the last thing remembered is success.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Organization, WebPage) that matches the visible text.
- Canonical tag, Open Graph tags and a share image, all on 1 version of my address.
- Real About, Contact, Privacy, Terms and Refund pages, linked from the footer of every page.
- A robots.txt that allows search and AI-answer crawlers and lists the sitemap, and a sitemap.xml of every real page.
- A square PNG icon (192px) at a stable address.
- No llms.txt, no FAQ rich-result markup, no review stars on my own business, no hidden text.
- No images above the fold heavier than they need to be. Aim for the main content to load in under 2.5 seconds.

CONVERSION RULES
- The main button, 1 line of reassurance and 1 piece of proof sit together in the first screen.
- Ask for as little as possible in every form. State the reply time at the button.
- Print the price. Put the guarantee or refund terms beside every buy button.
- On phones, keep the main action in a bar at the bottom of the screen.

HONESTY RULES
- Use only the proof I gave you. Do not invent testimonials, client names, numbers or press.
- Where I have not given you something, leave a clearly marked placeholder.
- No fake countdown timers and no invented scarcity. If I make an income or results claim, add a line that results are not typical.

OUTPUT
1 self-contained HTML file with inline CSS. Australian spelling. No em dashes.
```
