# 016 · Quiz Or Scorecard Landing Page

**Group:** List Builders And Launches  
**For:** Coach, Consultant  
**Style:** Bento Grid (Bricolage Grotesque + Instrument Sans)  
**Sample brand:** Bright Signal (fictional)

A quiz landing page that shows the first question and a sample result up front, so starting feels like 1 tap, not a commitment.

## Why This Page Works

- The first question is on the page. Answering it is easier than deciding whether to start.
- The result is shown before any email is requested. People who then opt in for the plan are far better subscribers.
- All 4 results are flattering and useful, so there is no fear of a bad score.
- The quiz sorts people into 4 groups, which lets every later email speak to how that person likes to work.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| 40.1% of people who start a quiz become a lead, and 65% of starters finish. | [Interact, 2026 quiz conversion report](https://tryinteract.com/blog/quiz-conversion-rate-report/) | Length is stated before the start (8 questions, 3 minutes) and a progress bar shows on every question, because 2 in 3 people who start will finish if they can see the end. |
| A lead form people can skip still captures 25% to 30%. | [Outgrow, analytics guidance](https://support.outgrow.co/docs/analytics) | The result shows without an email. An optional field offers the 1-page plan, and the skip is stated in plain words. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The no-email promise sits directly under the start button. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **IKEA Effect** (Norton, Mochon and Ariely, Journal of Consumer Psychology (2012)) | People value a result they helped build. Their answers make the plan feel like theirs. |
| **Commitment And Consistency** (Robert Cialdini, Influence (1984, revised 2021)) | Answering 1 question is a small yes that makes finishing the quiz feel natural. |
| **Goal-Gradient Effect** (Clark Hull; Ran Kivetz, Laws of UX) | The progress bar starts part-filled at question 3 of 8, so the end feels close. |
| **Zeigarnik Effect** (Bluma Zeigarnik, 1927 study; Laws of UX) | A half-finished quiz is an open loop the reader wants to close. |
| **Identity And Dissonance** (Leon Festinger; Cialdini, A Theory of Cognitive Dissonance (1957)) | A named style is a small identity. People act in line with who they have just been told they are. |
| **Reactance** (Jack Brehm, A Theory of Psychological Reactance (1966)) | No email wall. The reader chooses whether to give an address. |
| **The Power Of Free** (Dan Ariely, Predictably Irrational (2008)) | The result itself is free and complete. |

## Page Structure

1. Hero: the question the quiz answers, with the time and the number of questions
2. A live preview: 1 real question and a sample result, so the reader has already begun
3. The 4 results: every outcome is a good one, which makes the quiz safe to take
4. What happens next: result first, email optional
5. Proof about what people did with their result
6. Closing call to action

## Search Card

- **Title:** What Is Your Visibility Style? | Free 3-Minute Quiz | Bright Signal
- **Description:** A free 8-question quiz for coaches and consultants. Find out which of 4 visibility styles fits you and get a 1-page plan for being seen without posting every day.
- **Structured data:** WebSite, WebPage
- A quiz that runs entirely in JavaScript is invisible to search. This page describes the quiz, the 4 styles and a sample result as plain text.
- Give each result its own page with a real description, so people can share and find their style.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “What Is Your Visibility Style? | Free 3-Minute Quiz | Bright Signal” (67 characters). |
| Description says who the page is for | **Good** | “A free 8-question quiz for coaches and consultants. Find out which of 4 visibility styles fits you and get a 1-page plan for being seen without posting every day.” (162 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Bright Signal”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://brightsignal.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://brightsignal.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 101 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “What is your visibility style?”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 677 words are readable in the raw HTML. The page runs 1 scripts: the quiz, whose questions are all in the HTML already. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Plain words | **Good** | The 218 words of body copy on the main page read at about school grade 3.5 on the Flesch-Kincaid scale. Unbounce's study of 41,000 landing pages, as reported by Apexure, found pages written at grade 5 to 7 converted at about twice the rate of professional-level copy. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 7 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 4 sizes, from 19KB for phones to 82KB for a laptop and a 2560px file for large screens, and the browser picks 1. 5 photo files, the largest 74KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 5 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 5.6 and the whole page at grade 6.2 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.2 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 33ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Start The Quiz”) ends 556px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Form fields do not make a phone zoom in | **Good** | The smallest text in any of the 1 form fields is 17px. Phones zoom the page when a field is under 16px. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 6 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 18 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 6.6 to 1 for body text and 6.8 to 1 for large text. On a phone: 6.6 to 1 for body text and 6.9 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 52KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, WebPage. |
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
| Proof is written as text | **Good** | 3 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 3 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Thandi Mokoena, states their role and carries ProfilePage and Person markup tied to the business. |
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

- Show question 1 on the landing page.
- Give the result before you ask for an email.
- Name your results so people want to say them aloud.
- Show a progress bar that starts ahead of zero.

## Build Your Own

```text
Build me a quiz or scorecard landing page for my business, modelled on sample 016 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the question the quiz answers, with the time and the number of questions
2. A live preview: 1 real question and a sample result, so the reader has already begun
3. The 4 results: every outcome is a good one, which makes the quiz safe to take
4. What happens next: result first, email optional
5. Proof about what people did with their result
6. Closing call to action

DESIGN DIRECTION
Bento Grid. Rounded tiles on soft grey, one cobalt accent, lime and lilac for colour. Scans in a glance.
Fonts: Bricolage Grotesque + Instrument Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Norton, Mochon and Ariely, IKEA Effect: People value a result they helped build. Their answers make the plan feel like theirs.
- Robert Cialdini, Commitment And Consistency: Answering 1 question is a small yes that makes finishing the quiz feel natural.
- Clark Hull; Ran Kivetz, Goal-Gradient Effect: The progress bar starts part-filled at question 3 of 8, so the end feels close.
- Bluma Zeigarnik, Zeigarnik Effect: A half-finished quiz is an open loop the reader wants to close.
- Leon Festinger; Cialdini, Identity And Dissonance: A named style is a small identity. People act in line with who they have just been told they are.
- Jack Brehm, Reactance: No email wall. The reader chooses whether to give an address.
- Dan Ariely, The Power Of Free: The result itself is free and complete.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, WebPage) that matches the visible text.
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
