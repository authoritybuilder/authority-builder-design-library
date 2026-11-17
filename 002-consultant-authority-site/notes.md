# 002 · Consultant Authority Site

**Group:** Home Bases  
**For:** Consultant  
**Style:** Corporate Calm (Source Serif 4 + IBM Plex Sans)  
**Sample brand:** Incognito Rowe Advisory (fictional)

A B2B consultant site that reads like a board paper: a sharp position, a method, measured results and 1 action, a conversation.

## Why This Page Works

- The headline is a position, not a description. A managing partner knows in 1 line what this firm believes.
- The problem cards use the buyer's private language: write-offs, corridor discounts, capped seniors.
- Results are a table of 4 measures with before and after figures. A board can check a number; it cannot check an adjective.
- There is exactly 1 action on the page, repeated 3 times: request a conversation.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| 71% of business buyers rate customer and peer case studies as highly valuable. | [Forrester, reported by Digital Commerce 360](https://www.digitalcommerce360.com/?p=767377) | The case study moved up to sit straight after the problem, ahead of the method, and gained a chart and its own button. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The hero button now carries the line a managing partner needs: no proposal until you ask. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | The headline result (81% to 94%) floats beside the portrait, next to the main button. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Positioning** (Al Ries and Jack Trout, Positioning (1981)) | The firm owns 1 idea, pricing for professional services, and says no to everything else. |
| **Obviously Awesome** (April Dunford, Obviously Awesome (2019)) | The hero names who it is for (firms of 20 to 200) and what it replaces (the timesheet). |
| **Enter The Conversation** (Robert Collier, The Robert Collier Letter Book (1931)) | The 3 problem cards are written in the words partners use among themselves. |
| **Authority** (Robert Cialdini, Influence (1984, revised 2021)) | Credentials are specific and checkable: FCA, 20 years, 61 firms, a named book. |
| **Reason-Why And Specifics** (John E. Kennedy; Claude Hopkins, Scientific Advertising (1923)) | Every claim carries a number and a timeframe: 18% in year 1, 90 days, 3 deliverables. |
| **Scarcity** (Robert Cialdini, Influence (1984, revised 2021)) | 8 firms a year with a named next start date. A real limit set by the adviser's calendar. |
| **Von Restorff Effect** (Hedwig von Restorff, Laws of UX) | Teal appears only on the action and the key figures, so the eye lands on both. |

## Page Structure

1. Hero: a narrow position, the outcome in numbers, and 1 action
2. Proof strip: the kinds of firms served
3. Asset showcase: the thing itself, shown. Swap the files for your own video still, screenshots, slides or posts
4. The problem, stated the way a managing partner would say it
5. Case study numbers as a table: before and after, with the firm type named
6. 1 featured testimonial with name, title and firm size
7. Picture band: a painted pause in the middle of the page that repeats the main button, straight after the proof
8. Named method with a fixed timeframe
9. Insights hub: the content that brings the enquiries
10. About the adviser: credentials a board would check
11. Closing call to action: a conversation, not a sales call

## Search Card

- **Title:** Incognito Rowe Advisory | Pricing Strategy For Professional Services Firms
- **Description:** Guy Incognito and Incognito Rowe Advisory help accounting, legal and engineering firms of 20 to 200 people move from hourly billing to value pricing. 61 firms advised since 2016.
- **Structured data:** WebSite, Organization, Person
- The alternate name (Incognito Rowe) is declared, so Google can use the short form people actually search for.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Incognito Rowe Advisory | Pricing Strategy For Professional Services Firms” (74 characters). |
| The person's name is in the title or description | **Good** | “Guy Incognito” appears in the description. |
| Description says who the page is for | **Good** | “Guy Incognito and Incognito Rowe Advisory help accounting, legal and engineering firms of 20 to 200 people move from hourly billing to value pricing. 61 firms advised since 2016.” (178 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Incognito Rowe Advisory”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://incognitorowe.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 6 other pages of its own site by plain name: about.html, book.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 7 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 34 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://incognitorowe.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 9 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 214 internal links, buttons and form targets checked across 9 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 4 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 9 pages. This page's reads: “Stop selling hours. Start pricing the outcome.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 687 words are readable in the raw HTML. The page runs 1 small script, for movement only. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Plain words | **Good** | The 336 words of body copy on the main page read at about school grade 5.3 on the Flesch-Kincaid scale. Unbounce's study of 41,000 landing pages, as reported by Apexure, found pages written at grade 5 to 7 converted at about twice the rate of professional-level copy. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 17 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 4 sizes, from 19KB for phones to 42KB for a laptop and a 2560px file for large screens, and the browser picks 1. 11 photo files, the largest 68KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 3 of the 11 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 8.8 and the whole page at grade 10.3 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.7 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 6ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Request A Conversation”) ends 479px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 5 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 31 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 9 to 1 for body text and 11.5 to 1 for large text. On a phone: 9.2 to 1 for body text and 10.4 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 64KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Organization, Person. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | 1 image addresses named, all present in the site folder. The first version named portrait and shopfront files that did not exist. |
| Profile links (sameAs) | **Your turn** | The structured data carries no profile links, because a fictional brand has none and a placeholder would be published as fact. Add a sameAs list with your real profiles. |
| Google's Rich Results Test | **Couldn't check** | The test needs a live address. Run it on your page after launch. |

### Trust Signals

| Check | Result | What was seen |
|---|---|---|
| About, Contact, Privacy, Terms and Refunds exist and are linked from every page | **Fixed** | 5 real pages, linked in the footer of all 9 pages. In the first version these 5 footer links went nowhere. |
| Policy wording | **Your turn** | Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them. |
| Proof is written as text | **Good** | 1 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 4 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Guy Incognito, states their role and carries ProfilePage and Person markup tied to the business. |
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

- Guy at a whiteboard with a client team. Working, not posing
- the client, in their own office
- a plain, well-lit portrait. Jacket, no tie, direct eye contact

## Borrow This

- Write your headline as a belief your best client already half-holds.
- Turn 1 case study into a 4-row before and after table.
- Give your method a name, a length and a count of deliverables.
- State a real capacity limit and the next available start.

## Study The Real Thing

- **April Dunford**: Work split into Consulting, Speaking and Books. Proof as named testimonials with job titles and a count of companies served.

## Build Your Own

```text
Build me a consultant authority site for my business, modelled on sample 002 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: a narrow position, the outcome in numbers, and 1 action
2. Proof strip: the kinds of firms served
3. Asset showcase: the thing itself, shown. Swap the files for your own video still, screenshots, slides or posts
4. The problem, stated the way a managing partner would say it
5. Case study numbers as a table: before and after, with the firm type named
6. 1 featured testimonial with name, title and firm size
7. Picture band: a painted pause in the middle of the page that repeats the main button, straight after the proof
8. Named method with a fixed timeframe
9. Insights hub: the content that brings the enquiries
10. About the adviser: credentials a board would check
11. Closing call to action: a conversation, not a sales call

DESIGN DIRECTION
Corporate Calm. White, slate navy and one teal. A serious serif, mono labels, hairline grids. Reassures a board.
This site's own variation: Slate And Teal. Sections slide in a short way from the side as they scroll in. It uses headers underlined in the accent, outlined cards, hairline section breaks, the method laid out side by side. The picture band is 3 crops of the painting beside the line.
Fonts: Source Serif 4 + IBM Plex Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Al Ries and Jack Trout, Positioning: The firm owns 1 idea, pricing for professional services, and says no to everything else.
- April Dunford, Obviously Awesome: The hero names who it is for (firms of 20 to 200) and what it replaces (the timesheet).
- Robert Collier, Enter The Conversation: The 3 problem cards are written in the words partners use among themselves.
- Robert Cialdini, Authority: Credentials are specific and checkable: FCA, 20 years, 61 firms, a named book.
- John E. Kennedy; Claude Hopkins, Reason-Why And Specifics: Every claim carries a number and a timeframe: 18% in year 1, 90 days, 3 deliverables.
- Robert Cialdini, Scarcity: 8 firms a year with a named next start date. A real limit set by the adviser's calendar.
- Hedwig von Restorff, Von Restorff Effect: Teal appears only on the action and the key figures, so the eye lands on both.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Organization, Person) that matches the visible text.
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
