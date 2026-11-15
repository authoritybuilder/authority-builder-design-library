# 020 · Link-In-Bio Page

**Group:** List Builders And Launches  
**For:** Creator, Coach  
**Style:** Bright Playful (Syne + Plus Jakarta Sans)  
**Sample brand:** Poppy Achebe (fictional)

A link-in-bio page on your own domain. 1 featured action, 5 plain links, each with a line saying what it is.

## Why This Page Works

- It lives on the creator's own domain, so the visit, the search value and the email address all stay with them.
- 1 link is featured. If everything is equal, nothing is chosen.
- Every link has a line of description and a price or tag, so people know what they will get before they tap.
- The headshot matches the social profile. A visitor arriving from a bio needs to know in half a second they are in the right place.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| The first link gets the highest click rate, and pages with 7 or fewer links do best. | [Beacons, analysis of about 3,000 link pages](https://beacons.ai/i/blog/optimizing-your-links-for-clicks) | The page holds 1 featured action and 5 links, 6 in all, under the 7 that performs best. |
| The first link gets the highest click rate, and pages with 7 or fewer links do best. | [Beacons, analysis of about 3,000 link pages](https://beacons.ai/i/blog/optimizing-your-links-for-clicks) | The free calculator sits first and largest, because the first link takes the most taps. Paid offers follow in order of commitment. |
| Putting the guarantee and a line of reassurance right at the main button raised sales by 29% in their test. | [Conversion Rate Experts, button microcopy win report](https://conversion-rate-experts.com/button-microcopy-win-report/) | The featured button carries its own reassurance: free, no sign-up, 60 seconds. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Hick's Law** (William Hick and Ray Hyman, Laws of UX) | 6 choices in total, and 1 is clearly the main one. |
| **Von Restorff Effect** (Hedwig von Restorff, Laws of UX) | The featured card looks different from the plain links beneath it. |
| **Fitts's Law** (Paul Fitts, Laws of UX) | Every link is a full-width target at least 64px tall, sized for a thumb. |
| **The Power Of Free** (Dan Ariely, Predictably Irrational (2008)) | The featured action is free and takes 60 seconds. |
| **Serial Position Effect** (Hermann Ebbinghaus, Laws of UX) | The strongest action is first and the About link is last: the 2 positions best remembered. |
| **Jakob's Law** (Jakob Nielsen, Laws of UX) | It looks like the link pages people already know, so nobody has to think. |
| **One Set Of Facts** (Authority Builder SEO audit, Full SEO and AI Search Audit, section G) | The same bio line, prices and name as every other profile. |

## Page Structure

1. The whole page: a face, a 1-line promise, 1 featured action, then 5 labelled links

## Search Card

- **Title:** Poppy Achebe | Links | Money Coaching For Freelancers
- **Description:** Everything from Poppy Achebe in 1 place: the free Tax Jar Calculator, the Friday Money Minute newsletter, coaching and the podcast.
- **Structured data:** WebSite, WebPage, Person
- A link page on your own address is a real page Google can index, with your name in the title. A third-party link tool gives that value away.
- Person markup ties the page to your name. Use exactly the same bio line here as on each social profile.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “Poppy Achebe | Links | Money Coaching For Freelancers” (53 characters). |
| The person's name is in the title or description | **Good** | “Poppy Achebe” appears in the title. |
| Description says who the page is for | **Good** | “Everything from Poppy Achebe in 1 place: the free Tax Jar Calculator, the Friday Money Minute newsletter, coaching and the podcast.” (131 characters). |
| Site name is declared | **Good** | WebSite markup on the home page names the site “Poppy Achebe”. |
| The address the page claims is where it lives | **Good** | The main page is index.html at the top of the site folder, and its canonical link says https://poppyachebe.example/. The first version claimed a sub-folder address that the folder did not contain. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. 404.html and thank-you.html are left out on purpose. |
| 1 version of the address everywhere | **Good** | All 30 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://poppyachebe.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 8 pages checked. |
| Nothing important is hidden from Google | **Good** | No page carries a noindex except 404.html and thank-you.html, which should never be found by search. The first version put a noindex on every page, which a new owner could forget to remove. The library now keeps its demo brands out of search with host settings instead. |
| No broken or dead links inside the site | **Good** | 83 internal links, buttons and form targets checked across 8 pages, 0 broken. Every button leads to a real page or section. The first version had buttons that pointed at their own section and links that went nowhere. |
| Links that need your own accounts | **Your turn** | 8 links (checkout, social profiles, podcast apps and similar) point at example.com until you connect them. Each is listed in LAUNCH.md. |
| A page for wrong addresses | **Good** | 404.html exists, says the page is missing and links back to the main page and to Contact. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 8 pages. This page's reads: “Poppy Achebe”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 187 words are readable in the raw HTML. The page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Forms work | **Good** | 1 forms across the site. Each posts to thank-you.html, names its fields, marks what is required and carries a spam trap. They collect entries on Netlify once form detection is on, or on any host once the action points at your form tool. The first version's forms did nothing. |
| Dates and weekdays agree | **Good** | Every weekday named beside a date is the right one for the coming year. |
| Images are sized, described and sent in a phone size | **Good** | 1 image tags, all with alt text, width and height. They share 1 painting in 2 sizes: 59KB for phones and 203KB for desktops, in WebP. The first is loaded early and the rest wait until they are near the screen. |
| Real photographs | **Your turn** | The painting is original and can stay. If you would rather show yourself, save your photo under the same 2 file names. The brief for each shot is in LAUNCH.md. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the main page. |
| Reading level | **Good** | The first screen reads at grade 5.2 and the whole page at grade 7.4 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 0.9 seconds. Lighthouse lab test of this page on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 1ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 50px tall. 6 were measured. |
| Page weight | **Good** | The HTML is 30KB before compression, plus the web fonts and 1 painting. |
| HTTPS and security headers | **Your turn** | netlify.toml sets the security headers and long-term caching for images, and Netlify adds HTTPS by default. On another host, set the same headers there. After launch, check that every address is https. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: WebSite, WebPage, Person. |
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
| Proof is written as text | **Good** | 0 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 1 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Poppy Achebe, states their role and carries ProfilePage and Person markup tied to the business. |
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

- the same headshot as your social profile, so people know they are in the right place

## Borrow This

- Host your link page on your own domain.
- Feature 1 free action above the rest.
- Add a 1-line description and a price tag to each link.
- Use the same photo as your profile.

## Build Your Own

```text
Build me a link-in-bio page for my business, modelled on sample 020 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. The whole page: a face, a 1-line promise, 1 featured action, then 5 labelled links

DESIGN DIRECTION
Bright Playful. Butter yellow, coral and navy with sticker shadows and chunky outlines. Friendly and fast.
Fonts: Syne + Plus Jakarta Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- William Hick and Ray Hyman, Hick's Law: 6 choices in total, and 1 is clearly the main one.
- Hedwig von Restorff, Von Restorff Effect: The featured card looks different from the plain links beneath it.
- Paul Fitts, Fitts's Law: Every link is a full-width target at least 64px tall, sized for a thumb.
- Dan Ariely, The Power Of Free: The featured action is free and takes 60 seconds.
- Hermann Ebbinghaus, Serial Position Effect: The strongest action is first and the About link is last: the 2 positions best remembered.
- Jakob Nielsen, Jakob's Law: It looks like the link pages people already know, so nobody has to think.
- Authority Builder SEO audit, One Set Of Facts: The same bio line, prices and name as every other profile.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, WebPage, Person) that matches the visible text.
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
