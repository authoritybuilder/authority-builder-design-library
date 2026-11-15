# 024 · Podcast Home And Episode Page

**Group:** Trust And Content  
**For:** Creator, Coach  
**Style:** Dark Stage (Bebas Neue + Manrope)  
**Sample brand:** The Second Act (fictional)

A podcast home that works for listeners and for search: the latest episode playable at the top, a start-here set and full show notes as text.

## Why This Page Works

- The latest episode can be played without leaving the page, and every platform is named in text.
- A start-here set stops a new listener facing 112 episodes with no idea where to begin.
- Each episode has a real title with the guest's name and a 1-line summary, and links to its own page with full notes and a transcript.
- The show is tied clearly to the host and her work, without turning the page into a sales pitch.

## Research Applied To This Page

| What the research found | Source | What changed in the code |
|---|---|---|
| Search engines rank the text about an episode: its own page, the show notes and a full transcript. | [Podder, podcast SEO practices](https://www.podderapp.com/post/podcast-seo-best-practices) | The latest episode now has show notes with timestamps and a transcript excerpt as real text on the page, with a link to the full transcript. |
| Google shows no podcast-specific rich results, but structured data still helps it identify the show. | [Clutch, podcast SEO](https://clutch.co/resources/podcast-seo) | The structured data names the show and now the latest episode too. No rich-result markup is added, because Google shows none for podcasts. |
| A testimonial and credibility markers placed beside the call to action gave a 12% relative lift. | [MarketingSherpa and MECLABS, research-based swipe file](https://www.marketingsherpa.com/freestuff/Research-based-Ecommerce-Swipe-File) | The show's rating sits beside the email sign-up button. |

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Jakob's Law** (Jakob Nielsen, Laws of UX) | A player at the top and a list of episodes beneath: the layout every listener already knows. |
| **Hick's Law** (William Hick and Ray Hyman, Laws of UX) | 3 start-here episodes instead of an archive of 112. |
| **Reciprocity** (Robert Cialdini, Influence (1984, revised 2021)) | The show is free and says it always will be. |
| **Liking** (Robert Cialdini, Influence (1984, revised 2021)) | The host's own career change at 43 makes her one of the audience. |
| **STEPPS** (Jonah Berger, Contagious (2013)) | Listeners forward specific episodes. Clear numbers and titles make that easy. |
| **Content In The HTML** (How AI crawlers read pages, Full SEO and AI Search Audit, ground rules) | Titles, summaries, notes and transcripts are text. Audio alone cannot be searched. |
| **Brand Mentions** (Ahrefs (Louise Linehan), 75,000-brand AI Overview study (May 2025)) | Every guest is a reason for another site to mention the show by name. |

## Page Structure

1. Hero: the show's premise in 1 line, with the numbers that prove it is worth a listen
2. The latest episode, playable, with every platform named as text
3. Show notes and transcript as text, because the words about an episode are what search engines and AI tools read
4. Start here: 3 episodes for a new listener, each sold by what you will learn
5. Episode list: number, title, guest and length as text, each linking to its own page
6. The host: who she is and how the show connects to her work
7. Listener reviews as text
8. Email capture: episodes by email, for people who do not use podcast apps

## Search Card

- **Title:** The Second Act Podcast | Career Change After 40 With Lois Adeyemi
- **Description:** The Second Act is a weekly podcast of honest conversations with people who changed careers after 40. 112 episodes, hosted by career change coach Lois Adeyemi.
- **Structured data:** PodcastSeries, Person, BreadcrumbList
- PodcastSeries markup names the show and its host. Use the same show name and description here and in every podcast directory.
- Give every episode its own page with notes and a transcript. That is where the search value of a podcast lives.

## SEO And AI Search Audit: What Was Checked

### The Google Listing

| Check | Result | What was seen |
|---|---|---|
| Title carries the brand or the person's name | **Good** | “The Second Act Podcast | Career Change After 40 With Lois Adeyemi” (65 characters). |
| Description says who the page is for | **Good** | “The Second Act is a weekly podcast of honest conversations with people who changed careers after 40. 112 episodes, hosted by career change coach Lois Adeyemi.” (158 characters). |
| Site name is declared | **Your turn** | Site-name markup belongs on a home page, and this sample is an inner page. Add it to your home page the way sample 001 does. |
| Favicon is a real square image Google can use | **Fixed** | icon-192.png is a 192 by 192 PNG (192 is a multiple of 48), linked in the head of every page. The first version used an inline SVG, which has no stable address. |
| Sitelinks readiness | **Good** | The page links to 5 other pages of its own site by plain name: about.html, contact.html, privacy.html, refunds.html, terms.html. Sitelinks are Google's call. Give each offer its own page as well. |
| Other businesses with the same name | **Couldn't check** | This is a fictional brand, so there is nothing live to look at. Check it for your own business. |

### Crawling And Indexing

| Check | Result | What was seen |
|---|---|---|
| robots.txt allows search and AI crawlers | **Fixed** | 13 of 13 crawlers are named and allowed, nothing is blocked and the sitemap is listed. Search crawlers and training crawlers sit in separate groups, so you can opt out of training without disappearing from AI answers. |
| Sitemap lists every real page and nothing else | **Fixed** | sitemap.xml lists 6 pages. Each matches that page's canonical address. |
| 1 version of the address everywhere | **Good** | All 24 of the site's own addresses in the canonical tags, share tags, structured data and sitemap start with https://secondactshow.example/. |
| Every page has a canonical tag pointing at itself | **Good** | 6 pages checked. |
| Nothing important is hidden from Google | **Your turn** | 6 pages carry a line marked LIBRARY ONLY that keeps this fictional sample out of Google. Delete that 1 line on each page when the site is yours. |
| No broken links inside the site | **Good** | 141 internal links checked across 6 pages, 0 broken. |
| Links that still need a destination | **Your turn** | 11 links (article titles, social profiles, buy buttons) point at “#” because the fictional brand has nowhere to send them. Point each at a real page. |
| Redirects, status codes and old sites | **Couldn't check** | These only exist on a live host. After launch, check that http, https, www and non-www all land on 1 address in 1 hop. |

### The Page Itself

| Check | Result | What was seen |
|---|---|---|
| 1 clear headline Google can read | **Good** | 1 H1 on each of the 6 pages. This page's reads: “It is not too late. It is the second act.”. It is plain text, not a rotating or animated headline. |
| The content is in the HTML, not drawn by JavaScript | **Good** | 657 words are readable in the raw HTML and the page runs 0 scripts. AI crawlers that do not run JavaScript see everything a visitor sees. |
| Images have text alternatives and do not slow the page | **Good** | 2 illustrations, each drawn in the page's own code with a text label, and 0 image files to download. |
| Real photographs | **Your turn** | Every illustration stands in for a photo. The brief for each real shot is in the notes and in a comment beside it. Give each photo alt text and a phone-sized version. |
| Share tags and a share image | **Fixed** | Open Graph tags are set and share.jpg is a real 1200 by 630 image in the site folder. The first version pointed at an image that did not exist. |
| No orphan pages | **Good** | Every page is linked from the footer of every other page. |
| Reading level | **Good** | The first screen reads at grade 7.6 and the whole page at grade 7.9 (Flesch-Kincaid). Landing pages written at grade 5 to 7 convert best in Unbounce's data. |

### Speed And Mobile

| Check | Result | What was seen |
|---|---|---|
| Main content loads fast (LCP under 2.5 seconds) | **Good** | 0.9 seconds. Lighthouse lab test of this file on a simulated mid-range phone and slow 4G, run on a local server with the web fonts already installed. Your host and font loading will add to this. |
| Nothing jumps around while loading (CLS under 0.1) | **Good** | 0.000 in the same lab test. |
| The page responds quickly to taps (INP under 200ms) | **Couldn't check** | INP is measured from real visitors, so it cannot be tested before launch. The lab stand-in, Total Blocking Time, was 3ms. |
| Lighthouse scores | **Good** | Performance 100, Accessibility 100, Best Practices 100, SEO 100, out of 100, tested without the LIBRARY ONLY line. |
| No sideways scrolling on a phone | **Good** | At 390px wide the page content is 390px wide. |
| Buttons are easy to tap | **Good** | The smallest button or form field on a phone is 48px tall. 6 were measured. |
| Page weight | **Good** | The whole page is 1 HTML file of 42KB before compression, plus the web fonts. No image downloads, no scripts. |
| HTTPS and security headers | **Couldn't check** | These are set by your host. After launch, check that every address is https and that HSTS is on. |

### Structured Data

| Check | Result | What was seen |
|---|---|---|
| Structured data is present and valid JSON | **Good** | 1 JSON-LD block per page parses cleanly. This page declares: PodcastSeries, PodcastEpisode, Person, BreadcrumbList. |
| Structured data matches what the page shows | **Good** | Every name, headline, price, phone number and address in the structured data also appears in the visible text. |
| No markup Google ignores or disallows | **Good** | No FAQ or HowTo markup (FAQ rich results stopped appearing on 7 May 2026) and no review stars on the business's own site. |
| Every image the structured data names exists | **Fixed** | No image files are named. |
| Profile links (sameAs) | **Your turn** | 3 placeholder profile links marked YOUR-HANDLE. Replace them with your real LinkedIn, Instagram and YouTube addresses, or delete the lines. |
| Google's Rich Results Test | **Couldn't check** | The test needs a live address. Run it on your page after launch. |

### Trust Signals

| Check | Result | What was seen |
|---|---|---|
| About, Contact, Privacy, Terms and Refunds exist and are linked from every page | **Fixed** | 5 real pages, linked in the footer of all 6 pages. In the first version these 5 footer links went nowhere. |
| Policy wording | **Your turn** | Privacy, Terms and Refunds are plain-English starting templates, marked as such on the page. Replace them with your own terms and have a lawyer check them. |
| Proof is written as text | **Good** | 3 testimonials and every number on the page are real text, where Google and AI tools can read and quote them. None are trapped in images. |
| Results claims carry a plain caveat | **Good** | The page shows results, and says in plain words that they are individual and not guaranteed. |

### AI Answers And The Brand

| Check | Result | What was seen |
|---|---|---|
| 1 set of facts | **Good** | All 2 figures in the search description match the page, and every price on the About, Contact and policy pages matches the main page. |
| 1 page that is clearly about the person | **Fixed** | about.html names Lois Adeyemi, states their role and carries ProfilePage and Person markup tied to the business. |
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

- Lois at the microphone, headphones on, mid-laugh

## Borrow This

- Put a playable latest episode in the first screen.
- Curate 3 start-here episodes.
- Write each episode title with the guest's name and the hook.
- Publish a transcript on every episode page.

## Study The Real Thing

- **April Dunford**: Podcast and newsletter kept in the navigation as their own destinations, linked to the consulting work without crowding it.

## Build Your Own

```text
Build me a podcast home and episode page for my business, modelled on sample 024 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the show's premise in 1 line, with the numbers that prove it is worth a listen
2. The latest episode, playable, with every platform named as text
3. Show notes and transcript as text, because the words about an episode are what search engines and AI tools read
4. Start here: 3 episodes for a new listener, each sold by what you will learn
5. Episode list: number, title, guest and length as text, each linking to its own page
6. The host: who she is and how the show connects to her work
7. Listener reviews as text
8. Email capture: episodes by email, for people who do not use podcast apps

DESIGN DIRECTION
Dark Stage. Near-black with a spotlight gold and tall condensed capitals. Built for presence.
Fonts: Bebas Neue + Manrope from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Jakob Nielsen, Jakob's Law: A player at the top and a list of episodes beneath: the layout every listener already knows.
- William Hick and Ray Hyman, Hick's Law: 3 start-here episodes instead of an archive of 112.
- Robert Cialdini, Reciprocity: The show is free and says it always will be.
- Robert Cialdini, Liking: The host's own career change at 43 makes her one of the audience.
- Jonah Berger, STEPPS: Listeners forward specific episodes. Clear numbers and titles make that easy.
- How AI crawlers read pages, Content In The HTML: Titles, summaries, notes and transcripts are text. Audio alone cannot be searched.
- Ahrefs (Louise Linehan), Brand Mentions: Every guest is a reason for another site to mention the show by name.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (PodcastSeries, Person, BreadcrumbList) that matches the visible text.
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
