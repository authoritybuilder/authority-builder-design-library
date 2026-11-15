# 004 · Local Service Business Homepage

**Group:** Home Bases  
**For:** Business Owner  
**Style:** Bright Playful (Syne + Plus Jakarta Sans)  
**Sample brand:** Tideline Bookkeeping (fictional)

A local business home page that answers the 4 questions every local searcher has: what, where, how much and can I trust you.

## Why This Page Works

- The headline, eyebrow and title tag all carry the suburb and the audience. That is how a local page gets matched to a local search.
- Prices are printed. Most local competitors hide them, so showing them is the differentiator.
- Name, address and phone appear as text in the same form everywhere, matching the Google Business Profile.
- Reviews carry a suburb and a trade, which is the detail a local reader checks.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| The details people want most are the list of services, prices, a phone number, the address and opening hours. A missing phone number puts them off. | [BrightLocal, what local consumers want from a business website](https://www.brightlocal.com/research/what-local-consumers-want-most-from-local-business-websites/) | Services, printed prices, the phone number, the street address and opening hours are all on the page as text. Hours and address now sit in the first screen. |
| 60% of customers prefer to call a local business. | [Small Business Trends, customer contact statistics](https://smallbiztrends.com/2019/05/customer-contact-statistics.html) | The main button in the hero, the header and the closing section is a tap-to-call link. Phones get a call bar fixed to the bottom of the screen. |
| Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%. | [Formstack data, reported by eSEOspace](https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/) | The quote form went from 4 fields to 3. |
| A required phone number raises form abandonment. | [UX Movement](https://uxmovement.com/?p=8014) | It no longer demands a phone number: 1 field takes a phone number or an email, whichever the person prefers. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | A local review now sits directly under the price cards. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Jakob's Law** (Jakob Nielsen, Laws of UX) | The layout is the one locals expect: services, prices, reviews, hours, map. Nothing to learn. |
| **Anchoring** (Kahneman and Tversky, Judgment under Uncertainty (1974)) | The $2,400 in-house figure is stated before the $290 plan. |
| **Decoy Effect** (Dan Ariely, Predictably Irrational (2008)) | 3 tiers with the middle plan marked most popular make the choice easy. |
| **Fogg Behaviour Model** (BJ Fogg, Tiny Habits (2019)) | A phone-number button, a 15-minute call and a quote by tomorrow keep the first step small. |
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | Reviews name the suburb and the trade, so the reader sees someone like them. |
| **Trust Signals** (Google, Search Quality Rater Guidelines) | Registration, address, hours and policies are all visible, which is what Google's quality guidelines expect of a business that takes money. |
| **One Set Of Facts** (Authority Builder SEO audit, Full SEO and AI Search Audit, section G) | The same name, address and phone are used in the page, the footer and the structured data. |

## Page Structure

1. Hero: the service, the suburb and the audience in 1 line, with a phone number as a button
2. Numbers row: proof a local can sanity-check
3. Services: 3 plain cards, named the way customers ask for them
4. How it works: 3 steps so starting feels easy
5. Pricing in the open: 3 tiers with the middle one recommended
6. Reviews as text with suburb and trade, the details locals trust
7. Contact block: name, address and phone exactly as they appear on the Google Business Profile, plus hours
8. Questions answered in plain words, written for people, not for markup
9. Closing call to action: the phone number again, as text

## Search Card

- **Title:** Tideline Bookkeeping | Bookkeeper For Sunshine Coast Trades And Cafes
- **Description:** Tideline Bookkeeping keeps the books for 70+ Sunshine Coast trades and cafes. Fixed monthly fees from $290, BAS lodged on time, and a real person on the phone in Mooloolaba.
- **Structured data:** WebSite, LocalBusiness
- LocalBusiness uses the specific subtype AccountingService, with address, hours, phone and service area.
- The map is a placeholder below the fold. On a live site, lazy-load the embed so it does not slow the first screen.
- No review stars in the markup: Google excludes self-serving reviews on your own business.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Tideline Bookkeeping | Bookkeeper For Sunshine Coast Trades And Cafes” (69 characters). |
| Description says who the page is for | **Good** | “Tideline Bookkeeping keeps the books for 70+ Sunshine Coast trades and cafes. Fixed monthly fees from $290, BAS lodged on time, and a real person on the phone in Mooloolaba.” (173 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Tideline Bookkeeping”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://tidelinebooks.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://tidelinebooks.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 175 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Books done. BAS lodged. Weekends back.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 804 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 2 image tags, all with alt text, width and height. They share 1 painting in 2 sizes: 59KB for phones and 203KB for desktops, in WebP. The first is loaded early and the rest wait until they are near the screen. |
| Real photographs | **Your turn** | The painting is original and can stay. If you would rather show yourself, save your photo under the same 2 file names. The brief for each shot is in LAUNCH.md. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 6.7 and the whole page at grade 6.8 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.5 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 22ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 15 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 26 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 6.3 to 1 for body text and 6.4 to 1 for large text. On a phone: 6.6 to 1 for body text and 7.4 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 49KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, AccountingService. |
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
| 1 page that is clearly about the person | **Fixed** | about.html names Bec Tran, states their role and carries ProfilePage and Person markup tied to the business. |
| What Google and AI tools say about the brand today | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. Search your name, your brand and “[brand] review”, and read what ChatGPT, Perplexity and AI Overviews say. |
| Mentions on other sites, old profiles and copies of your work | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. Mentions on other sites are among the strongest signals for appearing in AI answers. |
| Google Business Profile matches the site | **Your turn** | Name, address and phone are identical in the page text, the footer and the structured data. Make your Google Business Profile match them character for character. |

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

- Bec at the shopfront with the street sign visible. Locals recognise the spot

## Borrow This

- Put your suburb and your customer in the headline and the title.
- Print your prices, with a comparison number first.
- Add suburb and trade to every review.
- Show hours as a table and your phone number as text, not an image.

## Build Your Own

```text
Build me a local service business homepage for my business, modelled on sample 004 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the service, the suburb and the audience in 1 line, with a phone number as a button
2. Numbers row: proof a local can sanity-check
3. Services: 3 plain cards, named the way customers ask for them
4. How it works: 3 steps so starting feels easy
5. Pricing in the open: 3 tiers with the middle one recommended
6. Reviews as text with suburb and trade, the details locals trust
7. Contact block: name, address and phone exactly as they appear on the Google Business Profile, plus hours
8. Questions answered in plain words, written for people, not for markup
9. Closing call to action: the phone number again, as text

DESIGN DIRECTION
Bright Playful. Butter yellow, coral and navy with sticker shadows and chunky outlines. Friendly and fast.
Fonts: Syne + Plus Jakarta Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Jakob Nielsen, Jakob's Law: The layout is the one locals expect: services, prices, reviews, hours, map. Nothing to learn.
- Kahneman and Tversky, Anchoring: The $2,400 in-house figure is stated before the $290 plan.
- Dan Ariely, Decoy Effect: 3 tiers with the middle plan marked most popular make the choice easy.
- BJ Fogg, Fogg Behaviour Model: A phone-number button, a 15-minute call and a quote by tomorrow keep the first step small.
- Robert Cialdini, Social Proof: Reviews name the suburb and the trade, so the reader sees someone like them.
- Google, Trust Signals: Registration, address, hours and policies are all visible, which is what Google's quality guidelines expect of a business that takes money.
- Authority Builder SEO audit, One Set Of Facts: The same name, address and phone are used in the page, the footer and the structured data.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, LocalBusiness) that matches the visible text.
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
