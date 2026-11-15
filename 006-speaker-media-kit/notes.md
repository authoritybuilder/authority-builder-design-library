# 006 · Speaker And Media Kit

**Group:** Home Bases  
**For:** Coach, Consultant, Creator  
**Style:** Dark Stage (Bebas Neue + Manrope)  
**Sample brand:** Jonah Reyes (fictional)

A speaker page built for the person who actually books speakers: an event organiser with 10 tabs open and a committee to convince.

## Why This Page Works

- It is written for the booker, not the fan. Topics, proof, bios, files and a date check are all on 1 page.
- The headline is the speaker's idea, not the speaker's name. An organiser is buying a message for their audience.
- Copy-ready bios and downloads remove work for the event team, and people book whoever makes their job easier.
- A fee guide is printed. It filters out mismatched enquiries and signals confidence.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| Event planners' top 2 factors are fitting the budget (75.5%) and topic relevance (65.7%). | [All American Entertainment, speaking industry benchmark](https://www.allamericanspeakers.com/blog/key-takeaways-from-aaes-2022-speaking-industry-benchmark-report/amp/) | A printed fee guide with 3 formats now sits above the enquiry form, and the starting fee is stated under the hero button. |
| Planners want a relevant topic, a demo video, named social proof, a one sheet and fast replies. | [The Speaker Lab](https://thespeakerlab.com/blog/what-event-planners-want-in-speakers/) | The speaker reel moved from the middle of the page to straight under the client strip. The media kit gained a one-sheet download. |
| Forms with 3 fields or fewer convert near 25%. With 6 or more fields that drops below 15%. | [Formstack data, reported by eSEOspace](https://eseospace.com/blog/how-to-optimize-your-contact-form-for-more-leads/) | The enquiry form went from 4 fields to 3, and the reply time is stated at the button. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Jobs To Be Done** (Clayton Christensen; Bob Moesta, Competing Against Luck (2016)) | The organiser's job is to look good to their committee. Every section hands them something they can forward. |
| **Authority** (Robert Cialdini, Influence (1984, revised 2021)) | Counts, ratings and named stages establish that this is a safe choice. |
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | Testimonials come from organisers, the buyer's own peers, not from audience members. |
| **Fogg Behaviour Model** (BJ Fogg, Tiny Habits (2019)) | The enquiry form asks for 4 facts and promises a reply in 1 day. Ability is high, so the prompt works. |
| **Anchoring** (Kahneman and Tversky, Judgment under Uncertainty (1974)) | A printed fee guide sets expectations before the first email. |
| **SUCCESs** (Chip and Dan Heath, Made to Stick (2007)) | The headline is simple, unexpected and concrete: lazy versus interrupted. |
| **Content In The HTML** (How AI crawlers read pages, Full SEO and AI Search Audit, ground rules) | Bios, topics and the video transcript are text in the page, so they can be found and quoted. |

## Page Structure

1. Hero: the speaker's 1 idea at full volume, with the numbers an organiser needs
2. Proof strip: stages spoken on, as text
3. The reel: a video above the fold of the decision, with a transcript for search
4. Topics: 3 keynotes, each sold by the outcome for the audience
5. Testimonials from organisers, not attendees: the buyer's peers
6. Copy-ready bios: the exact words an organiser can paste into a program
7. Downloads list: everything an event team asks for, in 1 place
8. Fee guide: printed, because budget fit is the first thing a planner checks
9. Booking enquiry: the 4 facts an agent needs, nothing more

## Search Card

- **Title:** Jonah Reyes | Keynote Speaker On Attention At Work
- **Description:** Jonah Reyes has delivered 140 keynotes on attention, focus and meeting culture to audiences of 50 to 5,000. Topics, speaker reel, bios and booking details.
- **Structured data:** WebSite, Person, WebPage
- A video needs a text transcript on the page. Search engines and most AI crawlers cannot watch it.
- Keep 1 fee figure and 1 bio everywhere they appear: site, speaker bureau listings and LinkedIn.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Jonah Reyes | Keynote Speaker On Attention At Work” (50 characters). |
| The person's name is in the title or description | **Good** | “Jonah Reyes” appears in the title. |
| Description says who the page is for | **Good** | “Jonah Reyes has delivered 140 keynotes on attention, focus and meeting culture to audiences of 50 to 5,000. Topics, speaker reel, bios and booking details.” (155 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Jonah Reyes”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://jonahreyes.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://jonahreyes.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 193 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 5 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Your team is not lazy. They are interrupted.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 762 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 2 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Plain words | **Good** | The 360 words of body copy on the main page read at about school grade 5 on the Flesch-Kincaid scale. Unbounce's study of 41,000 landing pages, as reported by Apexure, found pages written at grade 5 to 7 converted at about twice the rate of professional-level copy. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 7 image tags on the main page, all with alt text, width and height, so nothing jumps as they load. The painting comes in 4 sizes, from 11KB for phones to 41KB for a laptop and a 2560px file for large screens, and the browser picks 1. 6 photo files, the largest 43KB. Only the painting loads early. Everything else waits until it is near the screen. |
| A real person is on the page | **Your turn** | 2 of the 6 photo files are for pictures of you, and your face appears on the first screen, beside the form and on the thank-you page. The files that ship are painted stand-ins. Save your own under the same names. LAUNCH.md lists each file, its size and the shot to take. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 7.5 and the whole page at grade 8.8 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 1.3 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 58ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| A button is on the first screen of a phone | **Good** | On a 390 by 844 phone the first button in the page (“Check A Date”) ends 479px down. A bar pinned to the bottom of the phone screen carries the main button the whole way down the page. |
| Form fields do not make a phone zoom in | **Good** | The smallest text in any of the 3 form fields is 17px. Phones zoom the page when a field is under 16px. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 12 were measured. |
| Words on the painting stay readable | **Good** | A contrast checker cannot read text over a picture, so each of the 23 lines of text on a painted section was measured against the pixels directly behind it, at the hardest-to-read part of the line. Lowest result on a desktop: 12.6 to 1 for body text and 13.8 to 1 for large text. On a phone: 13.4 to 1 for body text and 13.1 to 1 for large text. The bar is 4.5 to 1 for body text and 3 to 1 for large text. |
| Page weight | **Good** | The HTML is 54KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, Person, WebPage. |
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
| 1 page that is clearly about the person | **Fixed** | about.html names Jonah Reyes, states their role and carries ProfilePage and Person markup tied to the business. |
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

- on stage, mid-gesture, audience visible in the foreground
- 3-minute reel. Host it properly and add a text transcript beneath

## Borrow This

- Lead with your idea as a headline. Your name is already in the logo.
- Publish a 40-word bio and a 30-second stage introduction.
- List your downloads with file type and size.
- Print a fee guide, even if it is a starting figure.

## Study The Real Thing

- **April Dunford**: Speaking gets its own section with a video and a Learn More button, separate from consulting and books.

## Build Your Own

```text
Build me a speaker and media kit for my business, modelled on sample 006 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the speaker's 1 idea at full volume, with the numbers an organiser needs
2. Proof strip: stages spoken on, as text
3. The reel: a video above the fold of the decision, with a transcript for search
4. Topics: 3 keynotes, each sold by the outcome for the audience
5. Testimonials from organisers, not attendees: the buyer's peers
6. Copy-ready bios: the exact words an organiser can paste into a program
7. Downloads list: everything an event team asks for, in 1 place
8. Fee guide: printed, because budget fit is the first thing a planner checks
9. Booking enquiry: the 4 facts an agent needs, nothing more

DESIGN DIRECTION
Dark Stage. Near-black with a spotlight gold and tall condensed capitals. Built for presence.
Fonts: Bebas Neue + Manrope from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Clayton Christensen; Bob Moesta, Jobs To Be Done: The organiser's job is to look good to their committee. Every section hands them something they can forward.
- Robert Cialdini, Authority: Counts, ratings and named stages establish that this is a safe choice.
- Robert Cialdini, Social Proof: Testimonials come from organisers, the buyer's own peers, not from audience members.
- BJ Fogg, Fogg Behaviour Model: The enquiry form asks for 4 facts and promises a reply in 1 day. Ability is high, so the prompt works.
- Kahneman and Tversky, Anchoring: A printed fee guide sets expectations before the first email.
- Chip and Dan Heath, SUCCESs: The headline is simple, unexpected and concrete: lazy versus interrupted.
- How AI crawlers read pages, Content In The HTML: Bios, topics and the video transcript are text in the page, so they can be found and quoted.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, Person, WebPage) that matches the visible text.
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
