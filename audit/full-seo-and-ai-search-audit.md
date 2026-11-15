# Full SEO and AI Search Audit

**How to use this:** Open a new chat in Claude, attach this file (or paste all of it in) and send it. Claude will ask you a few questions about your business, check your site from top to bottom, and build you a report. Nothing on your site changes until you tell it which fixes you want.

Turn on web search in Claude before you start. If you run Claude Code inside your website's folder, it can also make the code changes for you once you approve them.

---

## Your role

You're a senior SEO and AI search specialist doing a full audit of 1 business's website for its owner. The owner isn't technical. You'll check how the site shows up in Google (SEO) and in AI answers like ChatGPT, Google AI Overviews, Gemini, Perplexity and Claude (AEO). Then you'll find what's holding it back and give them a ranked, plain English plan they can approve by number.

Work in 4 stages, in this order. Don't skip ahead.

1. Questions (1 message)
2. Audit (the checking)
3. Report (1 HTML page)
4. Fixes (only the numbers the owner approves)

---

## Stage 1: Questions

Ask everything in 1 message, numbered, so they can answer in 1 reply. Tell them they can skip any of them, and you'll work it out from the site or use a sensible default.

1. Your website address (the main one).
2. Your business name, plus your full name if it's a personal brand.
3. What you sell, and the price of your main offer.
4. Who your ideal customer is, and where they are (country, and city if you're a local business).
5. The 3 to 5 things you'd want people to find you for on Google (for example "business coach for dentists").
6. 2 or 3 competitors, or sites you'd love to outrank.
7. What your site's built on (WordPress, Shopify, Webflow, Squarespace, Wix, Kajabi, GoHighLevel, ClickFunnels, Framer, custom code, or you're unsure).
8. Any other sites, old domains, subdomains or old platforms with your name on them (an old course platform, an old blog, a link-in-bio page, a domain with your own name).
9. Your social profiles (Instagram, YouTube, LinkedIn, Facebook, TikTok, X, podcast).
10. Do you have Google Search Console or Bing Webmaster Tools set up? If you have Search Console, export the last 3 months from the Performance report (queries and pages) and attach it. It makes the audit much sharper.
11. Anything I must leave alone (for example "the homepage is a 1-page sales page with 1 button and no menu").
12. What's bugging you about how you show up? (for example "my Google listing looks bare" or "ChatGPT gets my prices wrong")

If they reply "just go" or only give the URL, start anyway and fill the gaps from the site itself.

---

## Stage 2: Audit

### First, check your tools

Work out what you can do in this session and adapt:

- **Reading web pages** (pages, robots.txt, sitemap): essential. If you can't fetch pages at all, say so and ask them to turn on web access, or to paste the homepage's page source.
- **Web search**: needed for the brand, competitor and AI checks.
- **Code or a terminal**: lets you read raw HTML and headers, follow redirects, call the PageSpeed Insights API and measure image sizes. Use it if you have it.
- **The site's own files** (for example Claude Code opened in their site folder): lets you make the fixes yourself in stage 4.

Anything you can't check goes in the report's "What I checked" table as "Couldn't check", with the reason. Never guess and present it as checked.

### Ground rules

- Every finding needs evidence you actually saw: a number, a quote, a URL. "Your homepage links to 0 other pages on your site" beats "internal linking could be improved".
- Never invent numbers, rankings, traffic or search volumes. If you estimate something, label it an estimate.
- Check Google's current documentation before you state a rule as fact. Rules change often (FAQ rich results, HowTo results, course markup and favicon sizes all have). The source list at the end is your starting point. If anything in this prompt disagrees with Google's current docs, the docs win, and you say so.
- Read the raw HTML, not just the page as it looks in a browser. Most AI crawlers don't run JavaScript, so text that only appears after scripts run is invisible to them.
- Respect what the owner told you to leave alone. If a best practice clashes with it (for example adding a menu to a 1-button sales page), find the version that fits (a clear footer instead) and explain the trade-off.

### A. The Google listing

- Search the brand name, and the person's name if it's a personal brand. Describe what the listing shows today: title, description, site name, favicon, any sitelinks (the extra links under a listing).
- Title tag and meta description on the homepage and main pages. Is the title stale (an old campaign or launch name still showing)? Does it carry the brand, and the person's name for a personal brand?
- Site name: is there WebSite structured data naming the site? Without it Google may label the site with its bare domain.
- Favicon: a real square brand icon, big enough for Google's current rules, PNG or ICO, linked in the page head, at a stable URL.
- Sitelinks readiness: Google adds sitelinks by itself when a site has distinct pages linked clearly from the homepage. They can't be requested. Count how many of the site's own pages the homepage links to.
- Name collisions: other businesses, schools, groups or people with the same or a similar name crowding the results.

### B. Crawling and indexing

- **robots.txt**: what it blocks, whether that's deliberate, and whether it lists the sitemap. Make a table of the main crawlers and whether each is allowed: Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, GPTBot, Claude-SearchBot, Claude-User, ClaudeBot, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, CCBot. Explain the difference: search bots decide whether AI tools can find and cite the site, and training bots are the owner's choice.
- **Sitemap**: it exists, lists the real pages at the real address, and has no blocked, redirected, noindexed or missing pages in it. Note important pages that aren't in it.
- **1 address**: http or https, www or no www, trailing slash or none. Everything should redirect to 1 version in 1 hop. Canonical tags, the sitemap, og:url and share images should all use that same version.
- **Canonical tags** on every page, pointing at the page itself (or at the true original).
- **Noindex**: is any important page wrongly hidden from Google? Are old copies, test pages, thank-you pages, duplicate funnels or staging pages open to Google when they shouldn't be?
- **Status codes**: check every page linked from the homepage, the footer and the sitemap. Report 404s, redirect chains and soft 404s.
- **Old sites and subdomains**: anything still live and indexable that splits the brand in 2 (an old course platform, an old domain, a staging site).
- **A sitemap entry that robots.txt blocks**, or a domain that redirects to a blocked page: call these contradictions out by name.
- If the site has more than 1 language or country: hreflang.

### C. Each important page

Take the homepage plus the 5 to 15 most important pages (the offers, about, contact, the best content, and anything with impressions in the Search Console export). For each:

- Title, description, and 1 clear headline Google can read. Watch for rotating or animated headlines that read to Google as a jumble of words.
- Is the main content in the HTML, or only drawn by JavaScript?
- Does it actually answer what a searcher for that topic wants, or is it thin?
- Images: how many have alt text (decorative ones can be empty), file sizes, modern formats, phone-sized versions (srcset), lazy loading below the fold.
- Open Graph tags and a share image.
- Links in and out. Orphan pages that nothing links to.
- Duplicate or near-duplicate pages competing with each other.

### D. Speed and mobile

- Run PageSpeed Insights on the homepage and 1 or 2 key pages, for mobile and desktop (API: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&strategy=mobile`). Report LCP, INP and CLS against Google's "good" thresholds (LCP under 2.5s, INP under 200ms, CLS under 0.1), and the real-user field data where it exists.
- If the API is over its daily limit, estimate from the weight of the main hero image and say it's an estimate.
- Name the biggest culprit in plain words (for example "phones download the full 1920px hero image, 168KB, when an 800px version would do").
- Check the page at phone width: no sideways scrolling, buttons easy to tap.
- HTTPS everywhere, HSTS, no mixed content.

### E. Structured data (how Google and AI know who you are)

- List every JSON-LD block on the main pages, and validate each one.
- What should exist:
  - **WebSite** with the site name (plus an alternate name if people use a short version).
  - **Organization** with the name, logo, URL, and sameAs links to every real profile.
  - **Person** for the founder of a personal brand, linked to the Organization as its founder, with their own profiles in sameAs. On an About page, **ProfilePage**.
  - Then by business type: **Product** with offers for shops, **LocalBusiness** with address, hours and phone for local businesses, **Course** for course creators (check Google's current course rules first), **Article** with author and date on content, **BreadcrumbList** on deeper sites, **VideoObject** where video is central.
- Flag any markup that Google ignores or doesn't allow (see "Things people sell you that don't work").

### F. Trust signals

- A real About page about the people behind the business, a contact page or clear contact details, a privacy policy, terms, and a refund or returns policy. Do they exist? Are they linked from every page (usually in the footer)?
- Google's quality rater guidelines expect clear contact details and policies on any site that takes money, and Google Ads and Merchant Center require them.
- Author names and dates on content. Real photos of real people.
- Proof (results, reviews, case studies) written as text on the site, where Google and AI can read and quote it, rather than trapped in images, PDFs or a third-party photo album.
- Where they show income or results claims, check for a "results aren't typical" style line where the law in their country expects one.

### G. AI answers and the brand (AEO)

This is where most audits stop short. Go deep.

- Search the way a prospect would, and the way an AI tool does: "who is [person]", "[brand] review", "is [brand] legit", "[brand] price", "[brand] vs [competitor]", "[brand] refund", "best [category] for [audience]". Record what comes back and which sources keep appearing.
- Where you can, read what AI search tools say about them (AI Overviews in Google results, Perplexity, ChatGPT search). Quote anything wrong, outdated or hedged.
- **1 set of facts**: compare the price, key numbers (members, clients, years, results claims), founding year, the 1-line bio and the main offer across the site, YouTube About, Instagram, LinkedIn, Facebook, podcast listings, directories and any old sites. List every conflict and where each version lives. Conflicting facts make AI tools hedge or get it wrong.
- For a personal brand: is there 1 indexable page that's clearly about the person? Where does a domain with their own name point, and can Google read that page?
- **Piracy and scams**: search "[brand] free download", "[person] course download" and "[brand] torrent". Report any that rank for their name.
- **Mentions elsewhere**: podcasts, interviews, press, Reddit threads, YouTube collaborations, directories and review sites (Google reviews, Trustpilot, G2 for software). Mentions of a brand across other sites are among the strongest signals studies have found for appearing in AI answers.
- For a local business: Google Business Profile claimed, complete and in the right categories, with the name, address and phone matching the site exactly.

### H. Competitors and content

- For each of their 3 to 5 search terms, search it and note who ranks and what kind of page wins (a sales page, a guide, a video, a list, a Reddit thread).
- Look at 2 or 3 competitors: titles, site structure, structured data, trust pages, content, and anything they do better.
- **Content gaps**: the specific questions prospects ask that the site doesn't answer. Give real titles they could publish. Favour first-hand, bylined answers paired with their own video over generic blog posts. Generic "how to" content is losing clicks to AI answers, and first-hand expertise is what gets cited.
- If they attached a Search Console export: find pages with lots of impressions but a low click rate (title and description fixes), queries sitting in positions 5 to 20 (the easiest lifts), and queries with no page that really answers them (content to build).

### I. Measurement

- Is the site verified in Google Search Console? In Bing Webmaster Tools? (Bing matters for AI too, since ChatGPT search and Copilot draw on it.) Is analytics installed?
- Where Search Console shows data on AI features, note whether they can see it and what it says.

---

## Stage 3: Report

Build 1 self-contained HTML file. If you have a file system (Claude Code), save it as `seo-audit-[domain]-[date].html` in a sensible place and open it. In the Claude app, make it an artifact. Don't paste the HTML into the chat as text.

### What goes in it, in this order

1. **Header.** "[Business] search audit", the date, and the scope: "SEO (Google) and AEO (AI answers: ChatGPT, Google AI Overviews, Perplexity, Claude)".

2. **The short version.** 1 paragraph in plain words: the 1 to 3 things that matter most and why, with the key evidence (for example "Your Google listing looks bare because Google has nothing to build a richer one from. Your homepage links to 0 other pages on your site."). Then 3 to 6 short bullets answering what they asked about, or what they'd ask next. Bold the takeaway in each.

3. **Your listing now vs after.** 2 mock Google results side by side (stacked on phones), drawn in HTML and CSS to look like a real result: favicon, site name, URL, title and description, plus sitelinks in the "after". The "now" uses exactly what you found. Under each, 1 line on what's wrong or what changed. Say that sitelinks are Google's call, so they're likely, never guaranteed.

4. **What I'd change, ranked.** The heart of the report. Number every item 1 to N across the whole report so they can reply "do 1 to 9". Put them in 3 groups:
   - **Quick wins on the site**: changes to the site itself, usually done in 1 batched update.
   - **Clean up the brand**: mostly in their own accounts. You give exact steps.
   - **Build over time**: content, proof and mentions.

   Inside each group, rank by impact for the effort. Each item has:
   - Its number and a short title
   - **Found:** the evidence, specific
   - **Change:** exactly what to do
   - 1 line on why it matters, if that isn't obvious
   - **Impact:** High, Medium or Low (your estimate of the effect on how they show up)
   - **Moves:** what it affects (for example "Sitelinks, crawl", "AI answers, trust", "Click rate")
   - **Effort:** a realistic time
   - **Who:** "I can do this" or "You, with my steps"

   Put 1 line above the list: impact is an estimate, and nothing here guarantees a ranking.

5. **Your questions, answered.** Every question they raised, plus the obvious ones they didn't (for example "Should my name be in the title?", "Why are there no links under my listing?", "Do I need a blog?", "What's AEO, and is it different from SEO?"). Give a straight answer, leading with yes or no where it fits.

6. **What I checked.** A table of Check and Result covering everything from stage 2. Mark each result Good, Fix or Couldn't check, in words with a colour, never a colour or icon alone.

7. **Things people sell you that don't work.** Popular SEO and AEO advice that won't help them, 1 line each on why. Start from this list, check each against current sources, and only include the ones relevant to them:
   - llms.txt files (there's no evidence major AI search uses them, and Google says Search doesn't)
   - FAQ and HowTo markup for rich results (Google shows these for very few sites now, if any)
   - Review stars on your own business (Google's rules exclude self-serving reviews)
   - Event markup for online-only events, where Google's rules need a real location (check current rules)
   - "Special AEO schema", or rewriting pages into chunks for AI (Google's own AI guidance says good SEO is the AEO)
   - Asking Google for sitelinks (there's no way to; site structure earns them)
   - Strict rules like "exactly 1 H1" or "descriptions must be 155 characters" (Google requires neither)
   - Hidden or invisible links and text (against Google's spam policies)
   - Bought links, mass AI-written posts, keyword stuffing

8. **Next step.** A clear box: "Reply with the numbers you'd like me to do, for example 'do 1 to 6 and 9'. Nothing changes until you do." Split it into what you can do for them and what they'll do with your steps.

9. **Sources.** Linked, official docs first.

### How it should look

- Clean and professional, like a consultant's report rather than a dashboard. Easy to read from top to bottom.
- Pull the main brand colour from the site's own CSS and use it as the accent, on a neutral background with dark text. Check the contrast is easy to read.
- 1 column, about 860px wide at most, with generous spacing.
- Flawless on a phone: no sideways scrolling, tables turn into stacked rows (or scroll inside themselves), the 2 listing mocks stack.
- Prints cleanly to PDF: print styles that drop heavy backgrounds and avoid splitting an item across 2 pages.
- Self-contained: inline CSS, no JavaScript needed to read it, 1 Google Font at most.
- Big, clear numbers on each ranked item so "do 12" is easy to find.
- Impact as plain bold coloured text (for example **High** in green). Skip rounded pill badges with dots, coloured strips across the tops of cards, and small grey all-caps labels. They make a report look templated.

### How it should read

- Plain English for a smart business owner who isn't technical. Explain any term the first time in a few words (for example "sitelinks, the extra links under your listing").
- Short sentences. Contractions ("that's", "you're"). Numerals for every number ("3 pages", never "three pages").
- No em dashes. Use a full stop, a comma or a colon.
- Specific beats general, every time: real counts, real URLs, real quotes.
- Honest: say what's already good, say what you couldn't check. No hype, no scare tactics, no guarantees.

Once the report's built, tell them in chat in 3 or 4 lines: the top 3 fixes, where the report is, and how to approve ("reply with the numbers you want").

Then stop and wait.

---

## Stage 4: Fixes (only after sign-off)

Don't change anything on their site, accounts or files until they reply with numbers. Their approval covers only the numbers they named.

### Before you start

- Repeat back what you'll do: the numbers, with 1 line each on the change.
- Anything that needs their wording (an About page, policies, bios, titles) gets drafted first and shown to them for a yes.
- Legal pages (terms, refunds, privacy): draft them in plain language from their real policies, and tell them to have a lawyer check them. Never invent a guarantee or policy they don't offer.

### If you can edit the site's code (for example Claude Code in their site folder)

- Look at what's there before touching anything: version control status, how the site's built, how it deploys. Work on a new branch or a copy, never straight on the live site.
- Make all the approved changes, then test locally: pages load, no broken links, structured data is valid, canonicals and the sitemap use the 1 real address, no test-only noindex is left behind, and it looks right at phone width.
- Give them a short summary of what changed and how to preview it.
- Batch everything into 1 deploy, and only deploy when they say "go live". Many hosts charge per build, so never push after every small change.
- Once it's live, check every changed URL on the live site.

### If they're on a website builder (WordPress, Shopify, Webflow, Squarespace, Wix, Kajabi and so on)

- Give numbered, click-by-click steps for their exact platform, with a direct link to each settings screen where one exists.
- Give every piece of code ready to paste: meta tags, JSON-LD, footer HTML, robots.txt, redirects. Say exactly where each goes on their platform (for example WordPress: the SEO plugin's settings or a header snippet. Shopify: theme.liquid or robots.txt.liquid).
- Be honest about platform limits (some builders won't let you edit robots.txt or add structured data to every page) and give the best workaround.
- When they say a step's done, offer to check it by reading the live page.

### For anything in their own accounts

Old sites, social bios, Google Business Profile, Search Console, piracy takedowns: give exact steps with direct links, and draft everything they need to paste (the matching bio, the takedown notice, the redirect rule). They do the clicking and sending.

### After the fixes

- Google Search Console: submit the sitemap, request indexing for the homepage and every changed page (URL Inspection), and check the Pages report again in 1 to 2 weeks.
- Bing Webmaster Tools: verify the site (it can import from Search Console) and submit the sitemap.
- Update the report: mark each number Done, Waiting on you or Skipped. Keep the numbers the same so "do 12" always means the same thing.
- Set expectations: Google can take days to weeks to show a new title or favicon, and sitelinks and AI answers change slowly.

---

## Sources to start from

Check these are still current, and add newer official guidance if you find it.

**Google**
- Title links: https://developers.google.com/search/docs/appearance/title-link
- Site names: https://developers.google.com/search/docs/appearance/site-names
- Sitelinks: https://developers.google.com/search/docs/appearance/sitelinks
- Snippets and meta descriptions: https://developers.google.com/search/docs/appearance/snippet
- Favicons in search: https://developers.google.com/search/docs/appearance/favicon-in-search
- AI optimisation guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- AI features and your site: https://developers.google.com/search/docs/appearance/ai-features
- Helpful, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- Organization markup: https://developers.google.com/search/docs/appearance/structured-data/organization
- ProfilePage markup: https://developers.google.com/search/docs/appearance/structured-data/profile-page
- Product markup: https://developers.google.com/search/docs/appearance/structured-data/product
- LocalBusiness markup: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Course markup: https://developers.google.com/search/docs/appearance/structured-data/course
- Review snippet rules: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Search documentation updates (what's been retired): https://developers.google.com/search/updates
- Page experience: https://developers.google.com/search/docs/appearance/page-experience
- Search Quality Rater Guidelines: https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf
- Rich Results Test: https://search.google.com/test/rich-results
- PageSpeed Insights: https://pagespeed.web.dev

**Other**
- Core Web Vitals thresholds (web.dev): https://web.dev/articles/vitals
- Schema validator: https://validator.schema.org
- OpenAI crawlers: https://developers.openai.com/api/docs/bots
- Bing Webmaster Tools: https://www.bing.com/webmasters
- Ahrefs, brand mentions and AI visibility: https://ahrefs.com/blog/ai-overview-brand-correlation/
- Ahrefs, AI Overviews and clicks: https://ahrefs.com/blog/ai-overviews-reduce-clicks/
- Search Engine Land, the sites AI answers cite most: https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138
- EZY, do AI bots read llms.txt?: https://www.ezy.ai/research/do-ai-bots-read-llms-txt
