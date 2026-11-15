# 010 · Mastermind Application Page

**Group:** Offer Pages  
**For:** Coach, Consultant  
**Style:** Quiet Luxury (Cormorant Garamond + Jost)  
**Sample brand:** The Long Table (fictional)

A high-ticket page that sells by restraint. Few words, real selectivity, the price printed and an application instead of a buy button.

## Why This Page Works

- Restraint is the signal. Short copy, wide margins and 1 testimonial tell a senior buyer this is not a mass offer.
- The price is printed. Hiding a high price wastes both sides' time and reads as nervous.
- An application reverses the usual direction: the reader is asking to be chosen, which only works because the criteria are specific and real.
- Scarcity is exact and explained: 14 places, 9 returning, 5 open.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | A member's words now sit beside the investment, where the decision is made. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The first button says what applying does and does not commit you to, and when you will hear back. |
| Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%. | [Formstack data, reported by eSEOspace](https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/) | The application went from 5 fields to 4. It keeps 1 open question on purpose: an application should take a few minutes of thought. |
| Clarity beats persuasion: say plainly what it is, who it is for and what happens next. | [MarketingExperiments](https://marketingexperiments.com/?p=22070) | The price stays printed in full, with the payment schedule and what is not included. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Scarcity** (Robert Cialdini, Influence (1984, revised 2021)) | 14 places, 5 open, with the reason: a table only works at that size. |
| **Unity** (Robert Cialdini, Pre-Suasion (2016)) | The whole page is about being among peers: founders at the same stage. |
| **Commitment And Consistency** (Robert Cialdini, Influence (1984, revised 2021)) | A 15-minute application is a small, deliberate yes before the larger one. |
| **Authority** (Robert Cialdini, Influence (1984, revised 2021)) | Built and sold a 60-person agency: 1 credential, stated once. |
| **Anchoring** (Kahneman and Tversky, Judgment under Uncertainty (1974)) | The cost of 1 hiring mistake is set beside the fee. |
| **Aesthetic-Usability Effect** (Kurosu and Kashimura, Laws of UX) | Typography and space do the persuading. A calm page reads as a confident one. |
| **Tactical Empathy** (Chris Voss, Never Split the Difference (2016)) | The form's last question invites the reader to name the real worry, so the first call starts with understanding. |

## Page Structure

1. Hero: who it is for, stated narrowly, and a single action: apply
2. A short letter from the founder: belief first, then method
3. What the year contains: 4 pillars, described without hype
4. Selection criteria: clear on who is in and who is not
5. 1 testimonial, given room
6. The investment, printed, with what it includes
7. The application process: 3 steps, with timings
8. The application form itself: short, with the reason for each question clear

## Search Card

- **Title:** The Long Table | A 12-Month Mastermind For Agency Founders
- **Description:** The Long Table is a 12-month mastermind for 14 agency founders with revenue of $1.5m to $8m. 3 retreats, monthly sessions and a private adviser. By application.
- **Structured data:** WebSite, Service, Organization
- Keep the fee, the dates and the number of places identical wherever the mastermind is mentioned.
- The application form asks for a revenue range, not documents. Collect only what you need, and say who reads it.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “The Long Table | A 12-Month Mastermind For Agency Founders” (58 characters). |
| Description says who the page is for | **Good** | “The Long Table is a 12-month mastermind for 14 agency founders with revenue of $1.5m to $8m. 3 retreats, monthly sessions and a private adviser. By application.” (160 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “The Long Table”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://thelongtable.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://thelongtable.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 109 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “14 founders. 1 table. 12 months.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 669 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 2 image tags, all with alt text, width and height. They share 1 painting in 2 sizes: 37KB for phones and 132KB for desktops, in WebP. The first is loaded early and the rest wait until they are near the screen. |
| Real photographs | **Your turn** | The painting is original and can stay. If you would rather show yourself, save your photo under the same 2 file names. The brief for each shot is in LAUNCH.md. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 8.6 and the whole page at grade 8.3 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.2 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 57ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 8 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 11 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 6.7 to 1 for body text and 5.6 to 1 for large text. On a phone: 6.9 to 1 for body text and 6.7 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 43KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Service, Organization. |
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
| Proof is written as text | **Good** | 2 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 5 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Vivienne Ashcombe, states their role and carries ProfilePage and Person markup tied to the business. |
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

- a retreat dinner table, candid, no faces to camera

## Borrow This

- Cut your copy in half, then widen the margins.
- Print the price and the payment option.
- State how many places are genuinely open.
- Ask 1 application question that makes the reader think.

## Build Your Own

```text
Build me a mastermind application page for my business, modelled on sample 010 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: who it is for, stated narrowly, and a single action: apply
2. A short letter from the founder: belief first, then method
3. What the year contains: 4 pillars, described without hype
4. Selection criteria: clear on who is in and who is not
5. 1 testimonial, given room
6. The investment, printed, with what it includes
7. The application process: 3 steps, with timings
8. The application form itself: short, with the reason for each question clear

DESIGN DIRECTION
Quiet Luxury. Ivory, espresso and bronze. Thin rules, small capitals, lots of air. Says premium without shouting.
Fonts: Cormorant Garamond + Jost from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Robert Cialdini, Scarcity: 14 places, 5 open, with the reason: a table only works at that size.
- Robert Cialdini, Unity: The whole page is about being among peers: founders at the same stage.
- Robert Cialdini, Commitment And Consistency: A 15-minute application is a small, deliberate yes before the larger one.
- Robert Cialdini, Authority: Built and sold a 60-person agency: 1 credential, stated once.
- Kahneman and Tversky, Anchoring: The cost of 1 hiring mistake is set beside the fee.
- Kurosu and Kashimura, Aesthetic-Usability Effect: Typography and space do the persuading. A calm page reads as a confident one.
- Chris Voss, Tactical Empathy: The form's last question invites the reader to name the real worry, so the first call starts with understanding.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Service, Organization) that matches the visible text.
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
