# 003 · Creator Hub

**Group:** Home Bases  
**For:** Creator  
**Style:** Bento Grid (Bricolage Grotesque + Instrument Sans)  
**Sample brand:** Tash Okafor (fictional)

A content-first home for a creator: newsletter, podcast, best-of and shop in 1 scannable bento grid, with the email sign-up as the main event.

## Why This Page Works

- The site is a hub, not a brochure. The content does the selling and every tile is a way deeper into it.
- The email sign-up appears in the first screen, mid-page and at the end, always with the same promise.
- A new visitor gets a Start Here list of 3 proven pieces, so they are never dropped into the archive cold.
- The shop sits after the free value, and each product follows from an issue the reader has already enjoyed.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| 1-field forms converted at 13.4%, 3-field forms at 10.1% and 9-field forms at 3.6%. | [Unbounce 2026 data, reported by Digital Applied](https://digitalapplied.com/blog/landing-page-statistics-2026-conversion-data-points) | The sign-up tile asks for an email address and nothing else. It now shows the reader count and faces right under the button. |
| For 56% of shoppers the first action on a product page is exploring the images. Descriptive text on those images helps, and 52% of sites leave it off. | [Baymard Institute](https://baymard.com/blog/product-images-descriptive-text) | Each product picture carries a plain label saying what is inside, and the refund terms sit beside every buy button. |
| The first link gets the highest click rate, and pages with 7 or fewer links do best. | [Beacons, analysis of about 3,000 link pages](https://beacons.ai/i/blog/optimizing-your-links-for-clicks) | The 3 most-forwarded issues come first in the start-here list, in order of popularity. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Miller's Law** (George Miller, Laws of UX) | Content is chunked into tiles of 1 idea each. Nothing asks the reader to hold more than a few things in mind. |
| **Reciprocity** (Robert Cialdini, Influence (1984, revised 2021)) | 147 free issues and a podcast come before any product is mentioned. |
| **Value Ladder** (Russell Brunson, DotCom Secrets (2015)) | Free newsletter, then a $39 replay, a $49 kit and a $129 course. Trust and price rise together. |
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | The reader count is specific and repeated, and the quote names a real kind of reader. |
| **Commitment And Consistency** (Robert Cialdini, Influence (1984, revised 2021)) | Subscribing is the small yes. Each product asks for only a slightly larger one. |
| **Distinctive Assets** (Byron Sharp, How Brands Grow (2010)) | The lime, lilac and cobalt tiles and the Sunday rhythm make the brand easy to recognise anywhere. |
| **First-Hand Expertise** (Google Search Central, Helpful, people-first content) | Every issue is dated and bylined, which is the first-hand content AI answers cite. |

## Page Structure

1. Bento hero: the promise, the sign-up and the proof visible together without scrolling
2. Start here: the 3 best pieces, a podcast and a quote, so a new visitor is never lost
3. Latest issues as a plain list with dates: fresh, bylined content
4. A small shop: 3 products that follow from the free content
5. Podcast teaser with a real episode and every platform named
6. Closing call to action: the same single ask as the top

## Search Card

- **Title:** Tash Okafor | The Sunday System: Calm Systems For Freelancers
- **Description:** Tash Okafor writes The Sunday System, a weekly newsletter on calm work systems read by 42,000 freelancers. Start with the newsletter, the podcast or the starter kit.
- **Structured data:** WebSite, Person, Organization
- For a personal brand, the Person markup carries the name people search, and the home page is the 1 page clearly about them.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Tash Okafor | The Sunday System: Calm Systems For Freelancers” (61 characters). |
| The person's name is in the title or description | **Good** | “Tash Okafor” appears in the title. |
| Description says who the page is for | **Good** | “Tash Okafor writes The Sunday System, a weekly newsletter on calm work systems read by 42,000 freelancers. Start with the newsletter, the podcast or the starter kit.” (165 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Tash Okafor”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://tashokafor.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://tashokafor.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 192 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 14 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Run your freelance week like a calm studio.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 505 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 7 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 2 sizes: 36KB for phones and 128KB for desktops. 6 photo files, the largest 113KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 6 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 6.9 and the whole page at grade 8.3 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.9 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 2ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Read The Latest Issue”) ends 430px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Form fields do not make a phone zoom in | **Good** | The smallest text in any of the 1 form fields is 17px. Phones zoom the page when a field is under 16px. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 11 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 6 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 7.5 to 1 for body text and 7.4 to 1 for large text. On a phone: 7.6 to 1 for body text and 7.2 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 51KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Person, Organization. |
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
| Proof is written as text | **Good** | 0 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 1 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Tash Okafor, states their role and carries ProfilePage and Person markup tied to the business. |
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

- Tash at her desk, colour-blocked wall, real mess included

## Borrow This

- Put your email sign-up in the first screen with the reading time and the send day.
- Add a Start Here list of your 3 most-forwarded pieces.
- Name every podcast platform as text, and link the transcript.
- Price your first product low enough to be an easy second yes.

## Study The Real Thing

- **Justin Welsh**: 1 promise for the newsletter, the reader count stated twice, and a stated reading time.
- **James Clear**: An About page that routes visitors on to articles, books and a free email course.

## Build Your Own

```text
Build me a creator hub for my business, modelled on sample 003 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Bento hero: the promise, the sign-up and the proof visible together without scrolling
2. Start here: the 3 best pieces, a podcast and a quote, so a new visitor is never lost
3. Latest issues as a plain list with dates: fresh, bylined content
4. A small shop: 3 products that follow from the free content
5. Podcast teaser with a real episode and every platform named
6. Closing call to action: the same single ask as the top

DESIGN DIRECTION
Bento Grid. Rounded tiles on soft grey, one cobalt accent, lime and lilac for colour. Scans in a glance.
Fonts: Bricolage Grotesque + Instrument Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- George Miller, Miller's Law: Content is chunked into tiles of 1 idea each. Nothing asks the reader to hold more than a few things in mind.
- Robert Cialdini, Reciprocity: 147 free issues and a podcast come before any product is mentioned.
- Russell Brunson, Value Ladder: Free newsletter, then a $39 replay, a $49 kit and a $129 course. Trust and price rise together.
- Robert Cialdini, Social Proof: The reader count is specific and repeated, and the quote names a real kind of reader.
- Robert Cialdini, Commitment And Consistency: Subscribing is the small yes. Each product asks for only a slightly larger one.
- Byron Sharp, Distinctive Assets: The lime, lilac and cobalt tiles and the Sunday rhythm make the brand easy to recognise anywhere.
- Google Search Central, First-Hand Expertise: Every issue is dated and bylined, which is the first-hand content AI answers cite.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Person, Organization) that matches the visible text.
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
