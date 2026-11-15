# 005 · About And Founder Story

**Group:** Home Bases  
**For:** Coach, Creator, Consultant  
**Style:** Magazine (Playfair Display + Libre Franklin)  
**Sample brand:** Dana Whitlock (fictional)

An About page written as a magazine profile. It tells 1 turning-point story, proves it with numbers and ends by sending the reader somewhere.

## Why This Page Works

- It tells 1 story with 1 turning point, instead of a career history. Stories are remembered; CVs are skimmed.
- The numbers come before the story, so the reader already trusts the narrator when the story starts.
- It ends with 3 next steps. An About page is often the second most visited page on a site, so it should never be a dead end.
- It is the 1 indexable page clearly about the person, which is what Google and AI tools need to answer a who-is question.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| About 1 in 10 visitors reach the About page, and its job is reassurance. | [Haden Interactive](https://www.hadeninteractive.com/your-website-page-by-page-about-us/) | The page is built to reassure: the story opens with Dana's own 6-year break, the numbers come with their caveat, and the facts match every other page. |
| Clarity beats persuasion: say plainly what it is, who it is for and what happens next. | [MarketingExperiments](https://marketingexperiments.com/?p=22070) | Email, location and reply time are now on the About page itself, so a reader who has just been reassured does not have to go looking. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | The 380-women proof number floats beside the portrait, next to the main button. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Epiphany Bridge** (Russell Brunson, Expert Secrets (2017)) | The interview scene lets the reader feel the realisation rather than being told the conclusion. |
| **StoryBrand** (Donald Miller, Building a StoryBrand (2017)) | The reader is the hero. Dana is the guide who has walked the path and now has a plan. |
| **Liking** (Robert Cialdini, Influence (1984, revised 2021)) | Shared experience and small human details (the kelpie, the lasagne) build warmth quickly. |
| **Authority** (Robert Cialdini, Influence (1984, revised 2021)) | A dated timeline and specific counts do the work that adjectives cannot. |
| **SUCCESs** (Chip and Dan Heath, Made to Stick (2007)) | The pull quote is simple, concrete and emotional: the line a reader will repeat. |
| **Identity And Dissonance** (Leon Festinger; Cialdini, A Theory of Cognitive Dissonance (1957)) | The beliefs section lets the right reader recognise herself and the wrong one leave. |
| **Structured Data** (Google Search Central; schema.org, Structured data documentation) | ProfilePage and Person markup tell Google this page is the authoritative page about this person. |

## Page Structure

1. Hero: the story in 1 line, with the reader's situation inside it
2. Numbers row: the story's proof, before the story
3. The turning-point story: 1 moment, told plainly, so the reader feels the realisation
4. A short timeline: credibility as dated facts, easy to scan and easy to quote
5. What I believe: 3 positions that let the right reader self-select
6. Press and credentials as text
7. The human details: a few specifics that make a real person
8. Next steps: an About page should always send the reader somewhere
9. Contact details on the About page, so a reassured reader can act straight away

## Search Card

- **Title:** About Dana Whitlock | Career Coach For Women Returning To Work
- **Description:** Dana Whitlock took 6 years out of the workforce, then rebuilt her career in 14 months. She has since coached 380 women back into roles they chose. Read her story.
- **Structured data:** WebSite, ProfilePage, Person
- Use the same 1-line bio here, on LinkedIn, Instagram and every podcast listing. Conflicting bios make AI tools hedge.
- Dates created and modified are declared, and the breadcrumb shows where the page sits.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “About Dana Whitlock | Career Coach For Women Returning To Work” (62 characters). |
| The person's name is in the title or description | **Good** | “Dana Whitlock” appears in the title. |
| Description says who the page is for | **Good** | “Dana Whitlock took 6 years out of the workforce, then rebuilt her career in 14 months. She has since coached 380 women back into roles they chose. Read her story.” (162 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Dana Whitlock”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://danawhitlock.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 4 other pages of its own site by plain name: contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 5 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 26 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://danawhitlock.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 7 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 167 internal links, buttons and form targets checked across 7 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 7 pages. This page's reads: “I took 6 years out. It became the best line on my CV.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 742 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 1 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 4 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 2 sizes: 44KB for phones and 150KB for desktops. 3 photo files, the largest 123KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 3 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 3.7 and the whole page at grade 7.4 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.4 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 55ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Work With Me”) ends 500px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 4 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 18 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 7.5 to 1 for body text and 7.3 to 1 for large text. On a phone: 8.1 to 1 for body text and 9.2 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 45KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, ProfilePage, Person. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | No image files are named. |
| Profile links (sameAs) | **Your turn** | The structured data carries no profile links, because a fictional brand has none and a placeholder would be published as fact. Add a sameAs list with your real profiles. |
| Google's Rich Results Test | **Couldn't check** | The test needs a live address. Run it on your page after launch. |

### Trust Signals

| Check | Result | What was seen |
|---|---|---|
| About, Contact, Privacy, Terms and Refunds exist and are linked from every page | **Fixed** | 5 real pages, linked in the footer of all 7 pages. In the first version these 5 footer links went nowhere. |
| Policy wording | **Your turn** | Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them. |
| Proof is written as text | **Good** | 0 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 3 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Good** | index.html names Dana Whitlock, states their role and carries ProfilePage and Person markup tied to the business. |
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

- an editorial portrait. Seated, relaxed, strong side light, looking just off camera
- off-duty. Dog, garden or kitchen bench. Warm and unposed

## Borrow This

- Pick 1 turning-point moment and tell it as a scene with a place, a question and a line of dialogue.
- Put 4 numbers above the story.
- Add a 5-line dated timeline.
- End with 3 doors: free, paid and read.

## Study The Real Thing

- **James Clear**: An About page that opens with a plain greeting, stacks specific numbers, then routes readers on to articles, books and a free course.

## Build Your Own

```text
Build me a about and founder story for my business, modelled on sample 005 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the story in 1 line, with the reader's situation inside it
2. Numbers row: the story's proof, before the story
3. The turning-point story: 1 moment, told plainly, so the reader feels the realisation
4. A short timeline: credibility as dated facts, easy to scan and easy to quote
5. What I believe: 3 positions that let the right reader self-select
6. Press and credentials as text
7. The human details: a few specifics that make a real person
8. Next steps: an About page should always send the reader somewhere
9. Contact details on the About page, so a reassured reader can act straight away

DESIGN DIRECTION
Magazine. Black rules, a high-contrast serif, a single red. Reads like a feature in a weekend paper.
Fonts: Playfair Display + Libre Franklin from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Russell Brunson, Epiphany Bridge: The interview scene lets the reader feel the realisation rather than being told the conclusion.
- Donald Miller, StoryBrand: The reader is the hero. Dana is the guide who has walked the path and now has a plan.
- Robert Cialdini, Liking: Shared experience and small human details (the kelpie, the lasagne) build warmth quickly.
- Robert Cialdini, Authority: A dated timeline and specific counts do the work that adjectives cannot.
- Chip and Dan Heath, SUCCESs: The pull quote is simple, concrete and emotional: the line a reader will repeat.
- Leon Festinger; Cialdini, Identity And Dissonance: The beliefs section lets the right reader recognise herself and the wrong one leave.
- Google Search Central; schema.org, Structured Data: ProfilePage and Person markup tell Google this page is the authoritative page about this person.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, ProfilePage, Person) that matches the visible text.
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
