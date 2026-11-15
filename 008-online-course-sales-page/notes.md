# 008 · Online Course Sales Page

**Group:** Offer Pages  
**For:** Creator, Coach  
**Style:** Bold Type-Led (Archivo + Inter)  
**Sample brand:** Sam Okonkwo Studio (fictional)

A course sales page that sells 1 skill and 1 outcome. Loud type up top, calm detail below, and a 3-tier price table with an obvious best choice.

## Why This Page Works

- The headline is the outcome in 6 words. The course format comes second, as bullets.
- Outcomes are written as abilities, so the reader pictures themselves doing the thing.
- 3 tiers do the selling: the middle one is clearly the best value, which is where most buyers land.
- Every number that could be read as an earnings claim carries a plain note beside it.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| A highlighted plan is chosen more often, and more so when the dearest plan is listed first. | [HubSpot, pricing page best practices](https://blog.hubspot.com/marketing/best-practices-pricing-page) | The 3 options now run from dearest to cheapest, with the middle 1 highlighted, so the first price a reader sees is the anchor. |
| The average page offers 3.5 packages, and only half of them highlight 1. | [Process Street, study of 250 pricing pages](https://www.process.st/2015/12/saas-pricing-pages/) | 3 options, 1 clearly marked as the choice most students make. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The 14-day refund is stated under the hero button and under every enrol button. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | Student numbers and the review score sit beside the first button, and a student quote sits beside the prices. |
| For 56% of shoppers the first action on a product page is exploring the images. Descriptive text on those images helps, and 52% of sites leave it off. | [Baymard Institute](https://baymard.com/blog/product-images-descriptive-text) | The hero shows the course itself: the free preview lesson and the first 3 modules, in place of a generic picture. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **The Headline Does The Work** (David Ogilvy, Ogilvy on Advertising (1983)) | The 6-word headline carries the whole promise, because most visitors read little else. |
| **Value Equation** (Alex Hormozi, $100M Offers (2021)) | 4 hours, a weekend and ready-made templates cut the time and effort side of the equation. |
| **Decoy Effect** (Dan Ariely, Predictably Irrational (2008)) | The Course tier makes the Toolkit look like obvious value for $100 more. |
| **Defaults And Choice Architecture** (Thaler and Sunstein, Nudge (2008)) | The recommended tier is visually highlighted and labelled. |
| **Endowment Effect** (Richard Thaler, Nudge (2008)) | A free preview lesson lets the reader start owning the course before paying. |
| **Epiphany Bridge** (Russell Brunson, Expert Secrets (2017)) | 19 lost proposals, then 1 page: the teacher's turning point is the course's argument. |
| **Von Restorff Effect** (Hedwig von Restorff, Laws of UX) | Vermilion is used only on actions and key numbers against black and off-white. |

## Page Structure

1. Hero: the outcome as a headline, the format and proof beneath, a preview video beside
2. Numbers row: course proof at a glance
3. Outcomes: what you will be able to do, not what you will watch
4. Curriculum: every module and what you make in it
5. The teacher: first-hand experience, with numbers
6. Student proof with the result as a label
7. 3 tiers with a clear recommended option and a visible price comparison
8. Guarantee with plain terms
9. Objections, answered briefly
10. Closing call to action

## Search Card

- **Title:** Proposals That Close | Course For Freelance Designers | Sam Okonkwo
- **Description:** Proposals That Close is a self-paced course for freelance designers. 5 modules, 22 lessons and a proposal template that 2,300 students have used. From $290.
- **Structured data:** WebSite, Course
- Course markup names the course and its provider. Google retired course info rich results in June 2025, so expect clarity, not a visual extra.
- The free preview lesson needs captions and a transcript so the content is readable as text.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Proposals That Close | Course For Freelance Designers | Sam Okonkwo” (67 characters). |
| The person's name is in the title or description | **Good** | “Sam Okonkwo” appears in the title. |
| Description says who the page is for | **Good** | “Proposals That Close is a self-paced course for freelance designers. 5 modules, 22 lessons and a proposal template that 2,300 students have used. From $290.” (156 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Sam Okonkwo Studio”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://samokonkwo.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://samokonkwo.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 109 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 3 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Send the proposal. Win the project.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 917 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 1 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Plain words | **Good** | The 429 words of body copy on the main page read at about school grade 4.5 on the Flesch-Kincaid scale. Unbounce's study of 41,000 landing pages, as reported by Apexure, found pages written at grade 5 to 7 converted at about twice the rate of professional-level copy. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 13 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 4 sizes, from 27KB for phones to 102KB for a laptop and a 2560px file for large screens, and the browser picks 1. 8 photo files, the largest 76KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 3 of the 8 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 7.3 and the whole page at grade 6.9 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 2.0 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 4ms. |
| Lighthouse scores | **Good** | Performance 99, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Enrol From $290”) ends 660px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 16 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 22 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 5.8 to 1 for body text and 5.8 to 1 for large text. On a phone: 5.8 to 1 for body text and 5.8 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 54KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Course. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | No image files are named. |
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
| 1 set of facts | **Good** | All 4 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Sam Okonkwo, states their role and carries ProfilePage and Person markup tied to the business. |
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

- lesson 1 as a free preview, with captions
- Sam at a desk, laptop open, proposal on screen

## Borrow This

- Write outcomes as You will be able to, then a verb.
- Give lesson counts and total hours in the hero.
- Offer 3 tiers and make the middle one the generous one.
- Put the caveat beside the number, not in the footer alone.

## Study The Real Thing

- **Marie Forleo's B-School**: Numbered modules with what-you-will-learn bullets, verified-purchase testimonials and a results-vary disclaimer.

## Build Your Own

```text
Build me a online course sales page for my business, modelled on sample 008 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the outcome as a headline, the format and proof beneath, a preview video beside
2. Numbers row: course proof at a glance
3. Outcomes: what you will be able to do, not what you will watch
4. Curriculum: every module and what you make in it
5. The teacher: first-hand experience, with numbers
6. Student proof with the result as a label
7. 3 tiers with a clear recommended option and a visible price comparison
8. Guarantee with plain terms
9. Objections, answered briefly
10. Closing call to action

DESIGN DIRECTION
Bold Type-Led. Huge condensed capitals, hard edges, one loud accent. The headline is the design.
Fonts: Archivo + Inter from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- David Ogilvy, The Headline Does The Work: The 6-word headline carries the whole promise, because most visitors read little else.
- Alex Hormozi, Value Equation: 4 hours, a weekend and ready-made templates cut the time and effort side of the equation.
- Dan Ariely, Decoy Effect: The Course tier makes the Toolkit look like obvious value for $100 more.
- Thaler and Sunstein, Defaults And Choice Architecture: The recommended tier is visually highlighted and labelled.
- Richard Thaler, Endowment Effect: A free preview lesson lets the reader start owning the course before paying.
- Russell Brunson, Epiphany Bridge: 19 lost proposals, then 1 page: the teacher's turning point is the course's argument.
- Hedwig von Restorff, Von Restorff Effect: Vermilion is used only on actions and key numbers against black and off-white.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Course) that matches the visible text.
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
