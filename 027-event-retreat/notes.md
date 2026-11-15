# 027 · Event, Workshop Or Retreat Page

**Group:** Trust And Content  
**For:** Coach, Consultant  
**Style:** Soft Organic (DM Serif Display + Nunito Sans)  
**Sample brand:** Slow Strategy (fictional)

An in-person event page that answers when, where, what happens and how much before the first scroll ends, then lets the place do the persuading.

## Why This Page Works

- When, where, how many and how much are answered in the hero. Event buyers will not scroll to find a date.
- The schedule shows empty time as a feature. Being honest about what happens builds more trust than a packed agenda.
- Refund and transfer terms are printed beside the price, which is the question everyone has about a booking months away.
- Access details are stated plainly rather than left for people to ask about.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| Show the refund and transfer policy, all costs upfront, add-to-calendar links and a contact for questions. | [i4a, event registration practices](https://www.i4a.com/blog/event-registration-best-practices/) | Refund and transfer terms, what the price includes and a contact for questions now sit in a strip directly under the prices. |
| Show the refund and transfer policy, all costs upfront, add-to-calendar links and a contact for questions. | [i4a, event registration practices](https://www.i4a.com/blog/event-registration-best-practices/) | The deposit and refund date are stated under the first button, and add-to-calendar links were added. |
| Repeat the registration button after each major section and place testimonials near the price. | [HeySummit, event landing page checklist](https://heysummit.com/blog/event-landing-page-checklist) | A reserve button now follows the 3-day agenda and the inclusions, and a guest's words sit beside the price. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Scarcity** (Robert Cialdini, Influence (1984, revised 2021)) | 16 places and 6 cabins. The numbers are real because the building is. |
| **Attention Above The Fold** (Nielsen Norman Group, Scrolling and Attention (2018 eyetracking)) | Date, place, group size and price sit in the first screen. |
| **Peak-End Rule** (Daniel Kahneman, Thinking, Fast and Slow (2011)) | The retreat ends with each founder reading their plan aloud: a designed final moment. |
| **Loss Aversion** (Kahneman and Tversky, Prospect theory (1979)) | A decision avoided for 2 years: the quote frames the cost of not going. |
| **Pain Of Paying** (Prelec and Loewenstein; Ariely, The Red and the Black (1998)) | A $500 deposit and a clear refund date soften a large commitment. |
| **Unity** (Robert Cialdini, Pre-Suasion (2016)) | 16 founders at 1 table. The group is part of the product. |
| **Trust Signals** (Google, Search Quality Rater Guidelines) | Refund terms, access information and what is not included are all in view. |

## Page Structure

1. Hero: the promise, with dates, place, group size and price as the 4 headline facts
2. The 3 days: what actually happens, with times, so it is clear this is work and rest
3. What is included, and what is not
4. The venue: the place is part of the offer
5. 2 room types with prices, and the payment terms
6. Trust strip: refund, transfer, what is included and who to ask
7. Past guests on what they left with
8. Practical questions: travel, access, refunds
9. Closing call to action with the remaining places

## Search Card

- **Title:** The Slow Strategy Retreat | 3 Days For Founders | Noosa Hinterland, May 2027
- **Description:** A 3-day strategy retreat for 16 founders in the Noosa hinterland, 14 to 16 May 2027. Leave with a 1-page plan for the next 12 months. From $2,950, all meals and accommodation included.
- **Structured data:** Event, BreadcrumbList
- Event markup carries the name, dates, venue and price for this in-person event. Remove or update it as soon as the event passes.
- Name the nearest town and region in the title. People search for retreats by place.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “The Slow Strategy Retreat | 3 Days For Founders | Noosa Hinterland, May 2027” (76 characters). |
| Description says who the page is for | **Good** | “A 3-day strategy retreat for 16 founders in the Noosa hinterland, 14 to 16 May 2027. Leave with a 1-page plan for the next 12 months. From $2,950, all meals and accommodation included.” (184 characters). |
| Site name is declared | **Your turn** | Site-name markup belongs on a home page, and this sample is an inner page. Add it to your home page the way sample 001 does. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. |
| 1 version of the address everywhere | **Good** | All 24 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://slowstrategy.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 6 pages checked. |
| Nothing important is hidden from Google | **Your turn** | 6 pages carry a line marked LIBRARY ONLY that keeps this fictional sample out of Google. Delete that 1 line on each page when the site is yours. |
| No broken links inside the site | **Good** | 145 internal links checked across 6 pages, 0 broken. |
| Links that still need a destination | **Your turn** | 3 links (article titles, social profiles, buy buttons) point at “#” because the fictional brand has nowhere to send them. Point each at a real page. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 6 pages. This page's reads: “3 days away. 12 months clearer.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 758 words are readable in the raw HTML and the page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Images have text alternatives and do not slow the page | **Good** | 2 illustrations, each drawn in the page's own code with a text label, and 0 image files to download. |
| Real photographs | **Your turn** | Every illustration stands in for a photo. The brief for each real shot is in the notes and in a comment beside it. Give each photo alt text and a phone-sized version. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the footer of every other page. |
| Reading level | **Good** | The first screen reads at grade 5.3 and the whole page at grade 5.7 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.1 seconds. Lighthouse lab test of this file on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 40ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100, tested without the LIBRARY ONLY line. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 12 were measured. |
| Page weight | **Good** | The whole page is 1 HTML file of 45KB before compression, plus the web fonts. No image downloads, no scripts. |
| HTTPS and security headers | **Couldn't check** | These are set by your host. After launch, check that every address is https and that HSTS is on. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: Event, BreadcrumbList. |
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
| Proof is written as text | **Good** | 4 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 7 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Maren Solberg, states their role and carries ProfilePage and Person markup tied to the business. |
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

- the real venue at golden hour. Wide, quiet, no people
- the verandah or the fire pit. 1 strong image beats a gallery

## Borrow This

- Put date, place, group size and price in the hero.
- Show the real schedule, including the empty parts.
- Print the refund terms next to the price.
- Say what is accessible and what is not.

## Build Your Own

```text
Build me a event, workshop or retreat page for my business, modelled on sample 027 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the promise, with dates, place, group size and price as the 4 headline facts
2. The 3 days: what actually happens, with times, so it is clear this is work and rest
3. What is included, and what is not
4. The venue: the place is part of the offer
5. 2 room types with prices, and the payment terms
6. Trust strip: refund, transfer, what is included and who to ask
7. Past guests on what they left with
8. Practical questions: travel, access, refunds
9. Closing call to action with the remaining places

DESIGN DIRECTION
Soft Organic. Sage, cream and clay with soft blob shapes. Calm, human and unhurried.
Fonts: DM Serif Display + Nunito Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Robert Cialdini, Scarcity: 16 places and 6 cabins. The numbers are real because the building is.
- Nielsen Norman Group, Attention Above The Fold: Date, place, group size and price sit in the first screen.
- Daniel Kahneman, Peak-End Rule: The retreat ends with each founder reading their plan aloud: a designed final moment.
- Kahneman and Tversky, Loss Aversion: A decision avoided for 2 years: the quote frames the cost of not going.
- Prelec and Loewenstein; Ariely, Pain Of Paying: A $500 deposit and a clear refund date soften a large commitment.
- Robert Cialdini, Unity: 16 founders at 1 table. The group is part of the product.
- Google, Trust Signals: Refund terms, access information and what is not included are all in view.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (Event, BreadcrumbList) that matches the visible text.
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
