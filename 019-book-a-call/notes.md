# 019 · Book-A-Call Page

**Group:** List Builders And Launches  
**For:** Consultant, Coach  
**Style:** Bold Type-Led (Archivo + Inter)  
**Sample brand:** Okoro Strategy (fictional)

A booking page that answers the 3 fears behind every sales call: will it waste my time, will I be pressured, and am I even the right fit.

## Why This Page Works

- The headline promises an outcome from the call itself, so booking is worth it even if you never buy.
- A minute-by-minute plan removes the fear of a rambling sales call.
- The first testimonial is from someone who did not hire her. Nothing proves no-pressure like that.
- A qualification list protects the consultant's calendar and makes the right reader feel chosen.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%. | [Formstack data, reported by eSEOspace](https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/) | The request form has 3 fields: name, email and the times that suit. No calendar tool is needed to use the page, and 1 can be dropped in later. |
| A required phone number raises form abandonment. | [UX Movement](https://uxmovement.com/?p=8014) | The page says in plain words that no phone number is needed and that the invite arrives by email. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | What happens after you book is stated directly under the calendar. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | 3 named clients sit beside the promise, with their full quotes further down. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Reactance** (Jack Brehm, A Theory of Psychological Reactance (1966)) | No pitch is in the headline, and 1 testimonial is from a person who did not buy. |
| **Reciprocity** (Robert Cialdini, Influence (1984, revised 2021)) | 3 priorities and a written summary are given whether or not there is a sale. |
| **SPIN Selling** (Neil Rackham, SPIN Selling (1988)) | The call moves from situation to problem to implication to what solving it is worth. |
| **Tactical Empathy** (Chris Voss, Never Split the Difference (2016)) | You talk for 20 of the 30 minutes: the page promises listening before proposing. |
| **Fogg Behaviour Model** (BJ Fogg, Tiny Habits (2019)) | A visible calendar and 1 tap to choose a time make the action easy. |
| **Anchoring** (Kahneman and Tversky, Judgment under Uncertainty (1974)) | The starting fee is stated in the questions, so nobody is surprised later. |
| **Hick's Law** (William Hick and Ray Hyman, Laws of UX) | No menu. The only decision is which time. |

## Page Structure

1. Hero: what the call is, how long, and what you leave with, beside the calendar
2. What happens on the call, minute by minute
3. Fit check: who should book and who should not, yet
4. Proof about the call itself, not the paid work
5. The last objections
6. Closing call to action

## Search Card

- **Title:** Book A 30-Minute Strategy Call | Okoro Strategy
- **Description:** Book a free 30-minute strategy call with Ngozi Okoro. For clinic and practice owners with $500k or more in revenue. Leave with 3 priorities, whether or not we work together.
- **Structured data:** WebSite, WebPage, Organization
- Booking widgets load from another company's servers and can slow a page badly. Put text first and let the widget load below it.
- Show the time zone in words. Add the booking-confirmed page to your noindex list.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Book A 30-Minute Strategy Call | Okoro Strategy” (47 characters). |
| The person's name is in the title or description | **Good** | “Ngozi Okoro” appears in the description. |
| Description says who the page is for | **Good** | “Book a free 30-minute strategy call with Ngozi Okoro. For clinic and practice owners with $500k or more in revenue. Leave with 3 priorities, whether or not we work together.” (173 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Okoro Strategy”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://okorostrategy.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://okorostrategy.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 84 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “30 minutes. 3 priorities. No pitch.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 539 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 2 image tags, all with alt text, width and height. They share 1 painting in 2 sizes: 49KB for phones and 171KB for desktops, in WebP. The first is loaded early and the rest wait until they are near the screen. |
| Real photographs | **Your turn** | The painting is original and can stay. If you would rather show yourself, save your photo under the same 2 file names. The brief for each shot is in LAUNCH.md. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 5.7 and the whole page at grade 5.6 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.4 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 32ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 10 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 23 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 7.1 to 1 for body text and 7 to 1 for large text. On a phone: 7.3 to 1 for body text and 8.7 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 38KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, WebPage, Organization. |
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
| Proof is written as text | **Good** | 3 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 3 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Ngozi Okoro, states their role and carries ProfilePage and Person markup tied to the business. |
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

## Borrow This

- Promise something the caller keeps even if they never hire you.
- Publish the agenda of the call.
- Include a testimonial from someone who did not buy.
- State your starting fee somewhere on the page.

## Build Your Own

```text
Build me a book-a-call page for my business, modelled on sample 019 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: what the call is, how long, and what you leave with, beside the calendar
2. What happens on the call, minute by minute
3. Fit check: who should book and who should not, yet
4. Proof about the call itself, not the paid work
5. The last objections
6. Closing call to action

DESIGN DIRECTION
Bold Type-Led. Huge condensed capitals, hard edges, one loud accent. The headline is the design.
Fonts: Archivo + Inter from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Jack Brehm, Reactance: No pitch is in the headline, and 1 testimonial is from a person who did not buy.
- Robert Cialdini, Reciprocity: 3 priorities and a written summary are given whether or not there is a sale.
- Neil Rackham, SPIN Selling: The call moves from situation to problem to implication to what solving it is worth.
- Chris Voss, Tactical Empathy: You talk for 20 of the 30 minutes: the page promises listening before proposing.
- BJ Fogg, Fogg Behaviour Model: A visible calendar and 1 tap to choose a time make the action easy.
- Kahneman and Tversky, Anchoring: The starting fee is stated in the questions, so nobody is surprised later.
- William Hick and Ray Hyman, Hick's Law: No menu. The only decision is which time.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, WebPage, Organization) that matches the visible text.
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
