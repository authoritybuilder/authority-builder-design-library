# 004 · Local Service Business Homepage

**Group:** Home Bases  
**For:** Business Owner  
**Style:** Bright Playful (Syne + Plus Jakarta Sans)  
**Sample brand:** Tideline Bookkeeping (fictional)

A local business home page that answers the 4 questions every local searcher has: what, where, how much and can I trust you.

## Why This Page Works

- The headline, eyebrow and title tag all carry the suburb and the audience. That is how a local page gets matched to a local search.
- Prices are printed. Most local competitors hide them, so showing them is the differentiator.
- Name, address and phone appear as text in the same form everywhere, matching the Google Business Profile.
- Reviews carry a suburb and a trade, which is the detail a local reader checks.

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Jakob's Law** (Jakob Nielsen, Laws of UX) | The layout is the one locals expect: services, prices, reviews, hours, map. Nothing to learn. |
| **Anchoring** (Kahneman and Tversky, Judgment under Uncertainty (1974)) | The $2,400 in-house figure is stated before the $290 plan. |
| **Decoy Effect** (Dan Ariely, Predictably Irrational (2008)) | 3 tiers with the middle plan marked most popular make the choice easy. |
| **Fogg Behaviour Model** (BJ Fogg, Tiny Habits (2019)) | A phone-number button, a 15-minute call and a quote by tomorrow keep the first step small. |
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | Reviews name the suburb and the trade, so the reader sees someone like them. |
| **Trust Signals** (Google, Search Quality Rater Guidelines) | Registration, address, hours and policies are all visible, which is what Google's quality guidelines expect of a business that takes money. |
| **One Set Of Facts** (Authority Builder SEO audit, Full SEO and AI Search Audit, section G) | The same name, address and phone are used in the page, the footer and the structured data. |

## Page Structure

1. Hero: the service, the suburb and the audience in 1 line, with a phone number as a button
2. Numbers row: proof a local can sanity-check
3. Services: 3 plain cards, named the way customers ask for them
4. How it works: 3 steps so starting feels easy
5. Pricing in the open: 3 tiers with the middle one recommended
6. Reviews as text with suburb and trade, the details locals trust
7. Contact block: name, address and phone exactly as they appear on the Google Business Profile, plus hours
8. Questions answered in plain words, written for people, not for markup
9. Closing call to action: the phone number again, as text

## Search Card

- **Title:** Tideline Bookkeeping | Bookkeeper For Sunshine Coast Trades And Cafes
- **Description:** Tideline Bookkeeping keeps the books for 70+ Sunshine Coast trades and cafes. Fixed monthly fees from $290, BAS lodged on time, and a real person on the phone in Mooloolaba.
- **Structured data:** WebSite, LocalBusiness
- LocalBusiness uses the specific subtype AccountingService, with address, hours, phone and service area.
- The map is a placeholder below the fold. On a live site, lazy-load the embed so it does not slow the first screen.
- No review stars in the markup: Google excludes self-serving reviews on your own business.

## Borrow This

- Put your suburb and your customer in the headline and the title.
- Print your prices, with a comparison number first.
- Add suburb and trade to every review.
- Show hours as a table and your phone number as text, not an image.

## Build Your Own

```text
Build me a local service business homepage for my business, modelled on sample 004 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: the service, the suburb and the audience in 1 line, with a phone number as a button
2. Numbers row: proof a local can sanity-check
3. Services: 3 plain cards, named the way customers ask for them
4. How it works: 3 steps so starting feels easy
5. Pricing in the open: 3 tiers with the middle one recommended
6. Reviews as text with suburb and trade, the details locals trust
7. Contact block: name, address and phone exactly as they appear on the Google Business Profile, plus hours
8. Questions answered in plain words, written for people, not for markup
9. Closing call to action: the phone number again, as text

DESIGN DIRECTION
Bright Playful. Butter yellow, coral and navy with sticker shadows and chunky outlines. Friendly and fast.
Fonts: Syne + Plus Jakarta Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Jakob Nielsen, Jakob's Law: The layout is the one locals expect: services, prices, reviews, hours, map. Nothing to learn.
- Kahneman and Tversky, Anchoring: The $2,400 in-house figure is stated before the $290 plan.
- Dan Ariely, Decoy Effect: 3 tiers with the middle plan marked most popular make the choice easy.
- BJ Fogg, Fogg Behaviour Model: A phone-number button, a 15-minute call and a quote by tomorrow keep the first step small.
- Robert Cialdini, Social Proof: Reviews name the suburb and the trade, so the reader sees someone like them.
- Google, Trust Signals: Registration, address, hours and policies are all visible, which is what Google's quality guidelines expect of a business that takes money.
- Authority Builder SEO audit, One Set Of Facts: The same name, address and phone are used in the page, the footer and the structured data.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (WebSite, LocalBusiness) that matches the visible text.
- Canonical tag, Open Graph tags and a share image, all on 1 version of my address.
- A footer linking About, Contact, Privacy, Terms and Refunds.
- No llms.txt, no FAQ rich-result markup, no review stars on my own business, no hidden text.
- No images above the fold heavier than they need to be. Aim for the main content to load in under 2.5 seconds.

HONESTY RULES
- Use only the proof I gave you. Do not invent testimonials, client names, numbers or press.
- Where I have not given you something, leave a clearly marked placeholder.
- No fake countdown timers and no invented scarcity. If I make an income or results claim, add a line that results are not typical.

OUTPUT
1 self-contained HTML file with inline CSS. Australian spelling. No em dashes.
```
