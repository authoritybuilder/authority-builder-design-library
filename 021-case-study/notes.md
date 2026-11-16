# 021 · Case Study Page

**Group:** Trust And Content  
**For:** Consultant, Coach  
**Style:** Magazine (DM Serif Display + DM Sans)  
**Sample brand:** Lumen Practice Growth (fictional)

A case study told as a story with a table in the middle: the situation, the insight, what was done, the measured result and what a reader can copy.

## Why This Page Works

- The headline is the result. A reader who goes no further still gets the point.
- The numbers come before the story, in a table of 4 measures, so the proof is seen even by people who only skim.
- The story has a turn: the problem was not what the client thought. That insight is what readers remember and repeat.
- It ends with what to copy. Giving away the lesson builds more trust than hiding it.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| 44.2% of AI citations come from the first 30% of a page's text. Comparison tables and cited sources raise the odds. | Superlines study, reported on dev.to | A 4-line summary of client, problem, change and result now opens the page, so the whole story sits in the first third of the text. |
| 44.2% of AI citations come from the first 30% of a page's text. Comparison tables and cited sources raise the odds. | Superlines study, reported on dev.to | The 3 changes are set out in a table as well as in the story. |
| 71% of business buyers rate customer and peer case studies as highly valuable. | [Forrester, reported by Digital Commerce 360](https://www.digitalcommerce360.com/?p=767377) | The headline numbers gained a chart beside the table. |
| AI Overviews appear on nearly 65% of question-style searches, and an author bio alone does not predict being cited. | [Seer Interactive, May 2026](https://www.seerinteractive.com/insights/what-it-takes-to-rank-in-googles-ai-overviews-in-2026-is-not-what-you-think) | The byline links to a page about the author, and the page shows its publish date. The author box stays, but the page does not rely on it. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **SUCCESs** (Chip and Dan Heath, Made to Stick (2007)) | A simple, unexpected story: he thought it was marketing, it was rebooking. |
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | A named client in the same industry as the reader, with real figures. |
| **Reason-Why And Specifics** (John E. Kennedy; Claude Hopkins, Scientific Advertising (1923)) | 4 measures with before and after values. Nothing is described as amazing. |
| **Epiphany Bridge** (Russell Brunson, Expert Secrets (2017)) | The reader meets the insight the same way the client did, by counting first. |
| **Reciprocity** (Robert Cialdini, Influence (1984, revised 2021)) | The what-to-copy box gives the method away. |
| **First-Hand Expertise** (Google Search Central, Helpful, people-first content) | First-hand, bylined and dated, with a named author who did the work. |
| **Serial Position Effect** (Hermann Ebbinghaus, Laws of UX) | The result opens the page and the client's quote closes it. |

## Page Structure

1. Article header: the result as the headline, a 2-line summary, a named author and a date
2. The numbers first: a before and after table a skimmer can take in at once
3. The story: situation, insight, the 3 changes, and what to copy, with first-hand detail
4. The client's own words, with name and role
5. Picture band: a painted pause in the middle of the page that repeats the main button, straight after the proof
6. Related case studies: keeps the reader moving and links the pages together
7. Closing call to action that follows naturally from the story

## Search Card

- **Title:** How A 3-Person Physio Clinic Filled Its Books In 90 Days | Lumen Practice Growth
- **Description:** Case study: a 3-practitioner physiotherapy clinic went from 61% to 93% of appointments filled in 90 days by fixing rebooking, not marketing. The numbers, the steps and what to copy.
- **Structured data:** WebSite, Article
- Article markup carries the headline, the author and both dates. Update the modified date when you revise the figures.
- Case studies are the pages other sites and AI answers quote. Specific numbers written as text are what make them quotable.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “How A 3-Person Physio Clinic Filled Its Books In 90 Days | Lumen Practice Growth” (80 characters). |
| Description says who the page is for | **Good** | “Case study: a 3-practitioner physiotherapy clinic went from 61% to 93% of appointments filled in 90 days by fixing rebooking, not marketing. The numbers, the steps and what to copy.” (181 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Lumen Practice Growth”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://lumenpractice.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 6 other pages of its own site by plain name: about.html, book.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 7 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 34 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://lumenpractice.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 9 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 217 internal links, buttons and form targets checked across 9 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 3 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 9 pages. This page's reads: “How A 3-Person Physio Clinic Filled Its Books In 90 Days”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 791 words are readable in the raw HTML. The page runs 1 small script, for movement only. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Plain words | **Good** | The 393 words of body copy on the main page read at about school grade 4.5 on the Flesch-Kincaid scale. Unbounce's study of 41,000 landing pages, as reported by Apexure, found pages written at grade 5 to 7 converted at about twice the rate of professional-level copy. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 10 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 4 sizes, from 22KB for phones to 56KB for a laptop and a 2560px file for large screens, and the browser picks 1. 5 photo files, the largest 82KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 5 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 5.0 and the whole page at grade 6.8 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.1 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 37ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | This page opens with reading, so its first button in the page (“Book A Clinic Review”) is 5544px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 3 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 8 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 6.8 to 1 for body text and 6.6 to 1 for large text. On a phone: 7 to 1 for body text and 8 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 63KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, BlogPosting. |
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
| Author name and date on the content | **Good** | Byline for Guy Incognito with a publish date in the page and in the structured data. |
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

- the real clinic's reception or treatment room, with the owner's permission
- Sam in the clinic, natural light

## Borrow This

- Make the result your headline.
- Put a 4-row before and after table above the story.
- Find the turn: what the client believed versus what was true.
- End with a what-to-copy box.

## Study The Real Thing

- **April Dunford**: Proof presented as named people with job titles, not anonymous praise.

## Build Your Own

```text
Build me a case study page for my business, modelled on sample 021 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Article header: the result as the headline, a 2-line summary, a named author and a date
2. The numbers first: a before and after table a skimmer can take in at once
3. The story: situation, insight, the 3 changes, and what to copy, with first-hand detail
4. The client's own words, with name and role
5. Picture band: a painted pause in the middle of the page that repeats the main button, straight after the proof
6. Related case studies: keeps the reader moving and links the pages together
7. Closing call to action that follows naturally from the story

DESIGN DIRECTION
Magazine. Black rules, a high-contrast serif, a single red. Reads like a feature in a weekend paper.
This site's own variation: Salmon Paper And Teal. Sections slide in a short way from the side as they scroll in. It uses headers underlined in the accent, column guide lines, the method laid out side by side, numbers as cards. The picture band is 3 crops of the painting beside the line.
Fonts: DM Serif Display + DM Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Chip and Dan Heath, SUCCESs: A simple, unexpected story: he thought it was marketing, it was rebooking.
- Robert Cialdini, Social Proof: A named client in the same industry as the reader, with real figures.
- John E. Kennedy; Claude Hopkins, Reason-Why And Specifics: 4 measures with before and after values. Nothing is described as amazing.
- Russell Brunson, Epiphany Bridge: The reader meets the insight the same way the client did, by counting first.
- Robert Cialdini, Reciprocity: The what-to-copy box gives the method away.
- Google Search Central, First-Hand Expertise: First-hand, bylined and dated, with a named author who did the work.
- Hermann Ebbinghaus, Serial Position Effect: The result opens the page and the client's quote closes it.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Article) that matches the visible text.
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
