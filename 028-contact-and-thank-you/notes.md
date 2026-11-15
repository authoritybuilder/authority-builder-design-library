# 028 · Contact Page And Thank-You Page

**Group:** Trust And Content  
**For:** Business Owner, Consultant, Coach  
**Style:** Corporate Calm (Source Serif 4 + IBM Plex Sans)  
**Sample brand:** Calloway Finch (fictional)

The 2 most neglected pages on any site. A contact page that routes people and sets expectations, and a thank-you page that keeps the conversation going.

## Why This Page Works

- It tells people how fast they will hear back and who from. Most contact pages leave that to the imagination.
- 3 routing cards mean each kind of visitor knows where to go and the form stays short.
- Name, address, phone and hours are written as text, matching every other listing of the business.
- The thank-you page confirms, explains the next 3 steps and offers something to read. It is kept out of Google on purpose.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%. | [Formstack data, reported by eSEOspace](https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/) | The form went from 4 fields to 3. The role drop-down is gone. |
| A required phone number raises form abandonment. | [UX Movement](https://uxmovement.com/?p=8014) | 1 field takes an email address or a phone number, so nobody is forced to give a number. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The reply time is stated at the button, and the thank-you page says what happens next, hour by hour. |
| 60% of customers prefer to call a local business. | [Small Business Trends, customer contact statistics](https://smallbiztrends.com/2019/05/customer-contact-statistics.html) | The phone number is printed large as a tap-to-call link, beside the form. |
| Across 41,000 landing pages, copy at a 5th to 7th grade reading level converted at 11.1%, against 5.3% for professional-level copy. | [Unbounce benchmark data, reported by Colorlib](https://colorlib.com/wp/landing-page-statistics/) | The opening lines were rewritten in shorter, plainer sentences. The measured reading grade is in the audit table. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Fogg Behaviour Model** (BJ Fogg, Tiny Habits (2019)) | 4 fields, and email or phone is 1 flexible field. The prompt meets high ability. |
| **Hick's Law** (William Hick and Ray Hyman, Laws of UX) | 3 routes, clearly labelled, with the most common one first. |
| **Trust Signals** (Google, Search Quality Rater Guidelines) | Address, phone, hours and a named reader. A real business, plainly reachable. |
| **Tactical Empathy** (Chris Voss, Never Split the Difference (2016)) | No names needed at this stage: the form anticipates the worry before the reader voices it. |
| **Peak-End Rule** (Daniel Kahneman, Thinking, Fast and Slow (2011)) | The thank-you page is the end of the first interaction. It is designed, not left to a default message. |
| **One Set Of Facts** (Authority Builder SEO audit, Full SEO and AI Search Audit, section G) | Name, address and phone are identical here, in the footer and in the structured data. |
| **Index The Right Pages** (Google Search Central, Crawling and indexing documentation) | The thank-you page carries a permanent noindex, so a confirmation step never appears in search. |

## Page Structure

1. Hero: reassurance and a response time. Short on purpose
2. Routing: 3 kinds of enquiry, so each person lands in the right place
3. The form and every other way to reach the business, as text
4. What happens next: removes the uncertainty of sending a message into the void

## Search Card

- **Title:** Contact Calloway Finch | Workplace Mediation, Adelaide
- **Description:** Contact Imelda Calloway at Calloway Finch for workplace mediation or conflict coaching. Call (08) 5550 0163, email or send a confidential enquiry. A reply within 1 business day.
- **Structured data:** ContactPage, Organization, BreadcrumbList
- The thank-you page is noindexed deliberately. It should not be in your sitemap, and it is where you fire your analytics conversion event.
- The contact page is 1 of the pages Google's quality guidelines expect on any site that takes money. Link it from every page.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Contact Calloway Finch | Workplace Mediation, Adelaide” (54 characters). |
| The person's name is in the title or description | **Good** | “Imelda Calloway” appears in the description. |
| Description says who the page is for | **Good** | “Contact Imelda Calloway at Calloway Finch for workplace mediation or conflict coaching. Call (08) 5550 0163, email or send a confidential enquiry. A reply within 1 business day.” (177 characters). |
| Site name is declared | **Your turn** | Site-name markup belongs on a home page, and this sample is an inner page. Add it to your home page the way sample 001 does. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 4 other pages of its own site by plain name: about.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 5 pages. Each matches that page's canonical address. thank-you.html is left out on purpose. |
| 1 version of the address everywhere | **Good** | All 23 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://callowayfinch.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 6 pages checked. |
| Nothing important is hidden from Google | **Your turn** | 5 pages carry a line marked LIBRARY ONLY that keeps this fictional sample out of Google. Delete that 1 line on each page when the site is yours. thank-you.html keeps its noindex for good, because a confirmation page should never be found by search. |
| No broken links inside the site | **Good** | 130 internal links checked across 6 pages, 0 broken. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 6 pages. This page's reads: “Tell us what is happening. A person will reply.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 327 words are readable in the raw HTML and the page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Images have text alternatives and do not slow the page | **Good** | 1 illustrations, each drawn in the page's own code with a text label, and 0 image files to download. |
| Real photographs | **Your turn** | Every illustration stands in for a photo. The brief for each real shot is in the notes and in a comment beside it. Give each photo alt text and a phone-sized version. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the footer of every other page. |
| Reading level | **Good** | The first screen reads at grade 8.1 and the whole page at grade 9.2 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 0.9 seconds. Lighthouse lab test of this file on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 0ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100, tested without the LIBRARY ONLY line. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 9 were measured. |
| Page weight | **Good** | The whole page is 1 HTML file of 30KB before compression, plus the web fonts. No image downloads, no scripts. |
| HTTPS and security headers | **Couldn't check** | These are set by your host. After launch, check that every address is https and that HSTS is on. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: ContactPage, Organization, BreadcrumbList. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | 1 image addresses named, all present in the site folder. The first version named portrait and shopfront files that did not exist. |
| Profile links (sameAs) | **Your turn** | 3 placeholder profile links marked YOUR-HANDLE. Replace them with your real LinkedIn, Instagram and YouTube addresses, or delete the lines. |
| Google's Rich Results Test | **Couldn't check** | The test needs a live address. Run it on your page after launch. |

### Trust Signals

| Check | Result | What was seen |
|---|---|---|
| About, Contact, Privacy, Terms and Refunds exist and are linked from every page | **Fixed** | 5 real pages, linked in the footer of all 6 pages. In the first version these 5 footer links went nowhere. |
| Policy wording | **Your turn** | Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them. |
| Proof is written as text | **Good** | 0 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 4 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Imelda Calloway, states their role and carries ProfilePage and Person markup tied to the business. |
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

- Map placeholder: embed your map here, lazy-loaded

## Borrow This

- State your reply time and who replies.
- Add 3 routing cards above the form.
- Write a thank-you page with 3 next steps.
- Set the thank-you page to noindex and leave it out of your sitemap.

## Build Your Own

```text
Build me a contact page and thank-you page for my business, modelled on sample 028 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: reassurance and a response time. Short on purpose
2. Routing: 3 kinds of enquiry, so each person lands in the right place
3. The form and every other way to reach the business, as text
4. What happens next: removes the uncertainty of sending a message into the void

DESIGN DIRECTION
Corporate Calm. White, slate navy and one teal. A serious serif, mono labels, hairline grids. Reassures a board.
Fonts: Source Serif 4 + IBM Plex Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- BJ Fogg, Fogg Behaviour Model: 4 fields, and email or phone is 1 flexible field. The prompt meets high ability.
- William Hick and Ray Hyman, Hick's Law: 3 routes, clearly labelled, with the most common one first.
- Google, Trust Signals: Address, phone, hours and a named reader. A real business, plainly reachable.
- Chris Voss, Tactical Empathy: No names needed at this stage: the form anticipates the worry before the reader voices it.
- Daniel Kahneman, Peak-End Rule: The thank-you page is the end of the first interaction. It is designed, not left to a default message.
- Authority Builder SEO audit, One Set Of Facts: Name, address and phone are identical here, in the footer and in the structured data.
- Google Search Central, Index The Right Pages: The thank-you page carries a permanent noindex, so a confirmation step never appears in search.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (ContactPage, Organization, BreadcrumbList) that matches the visible text.
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
