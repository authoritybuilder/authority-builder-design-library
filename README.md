# Authority Builder™ Design Library

Website design inspiration for coaches, creators, consultants and business owners.

28 live page samples, each one a single HTML file you can open, read and adapt. Every sample comes with the psychology behind it, a search card showing how it is set up for Google and AI answers, and a copy-paste prompt for building your own.

**Open `index.html` in a browser to browse the library.**

## What Is In Here

| Path | What it is |
|---|---|
| `index.html` | The gallery. Filter by who you are and by style. |
| `001-…` to `028-…` | 1 folder per page type. |
| `029-…` to `031-…` | Building blocks: font pairings, colour palettes and section patterns. |
| `canon/index.html` | The research page: 74 principles with their sources, linked to the samples that use them. |
| `audit/` | The Full SEO and AI Search Audit prompt. Run it on your site after you build. |
| `src/` | The small Python build that generates everything. You do not need it to use the library. |

Each entry folder holds:

- `sample.html`: the live page. Self-contained, fonts from Google Fonts, no build step.
- `index.html`: the notes page. Why it works, the psychology, the search card, what to borrow and the build prompt.
- `notes.md`: the same notes as plain text, ready to hand to an AI assistant.
- `preview.jpg`: a screenshot of the sample.

## How To Use It

1. **Pick the page you need.** Open the gallery, filter, and scroll the live sample on your phone.
2. **Read why it works.** The notes page maps each section to a principle and a source.
3. **Copy the prompt.** Paste it into Claude with your real proof. Then run the audit prompt on the finished page.

## The Index

<!-- INDEX:START -->
| # | Page | Group | For | Style |
|---|---|---|---|---|
| 001 | [Coach Homepage](001-coach-homepage/index.html) | Home Bases | Coach | Warm Editorial |
| 002 | [Consultant Authority Site](002-consultant-authority-site/index.html) | Home Bases | Consultant | Corporate Calm |
| 003 | [Creator Hub](003-creator-hub/index.html) | Home Bases | Creator | Bento Grid |
| 004 | [Local Service Business Homepage](004-local-service-business/index.html) | Home Bases | Business Owner | Bright Playful |
| 005 | [About And Founder Story](005-about-founder-story/index.html) | Home Bases | Coach, Creator, Consultant | Magazine |
| 006 | [Speaker And Media Kit](006-speaker-media-kit/index.html) | Home Bases | Coach, Consultant, Creator | Dark Stage |
| 007 | [Signature Program Sales Page](007-signature-program-sales-page/index.html) | Offer Pages | Coach | Soft Organic |
| 008 | [Online Course Sales Page](008-online-course-sales-page/index.html) | Offer Pages | Creator, Coach | Bold Type-Led |
| 009 | [Membership Or Community Join Page](009-membership-community-join/index.html) | Offer Pages | Creator, Coach | Retro Scrapbook |
| 010 | [Mastermind Application Page](010-mastermind-application/index.html) | Offer Pages | Coach, Consultant | Quiet Luxury |
| 011 | [Services And Pricing Page](011-services-and-pricing/index.html) | Offer Pages | Consultant, Business Owner | Warm Editorial |
| 012 | [Digital Product Shop](012-digital-product-shop/index.html) | Offer Pages | Creator, Coach | Bright Playful |
| 013 | [Corporate Training Page](013-corporate-training/index.html) | Offer Pages | Consultant, Coach | Corporate Calm |
| 014 | [Lead Magnet Opt-In Page](014-lead-magnet-opt-in/index.html) | List Builders And Launches | Coach, Creator, Consultant | Soft Organic |
| 015 | [Webinar Or Masterclass Registration](015-webinar-registration/index.html) | List Builders And Launches | Consultant, Coach | Dark Stage |
| 016 | [Quiz Or Scorecard Landing Page](016-quiz-scorecard-landing/index.html) | List Builders And Launches | Coach, Consultant | Bento Grid |
| 017 | [Challenge Page](017-challenge-page/index.html) | List Builders And Launches | Coach, Creator | Retro Scrapbook |
| 018 | [Waitlist Or Launching-Soon Page](018-waitlist-launching-soon/index.html) | List Builders And Launches | Coach, Creator, Consultant | Quiet Luxury |
| 019 | [Book-A-Call Page](019-book-a-call/index.html) | List Builders And Launches | Consultant, Coach | Bold Type-Led |
| 020 | [Link-In-Bio Page](020-link-in-bio/index.html) | List Builders And Launches | Creator, Coach | Bright Playful |
| 021 | [Case Study Page](021-case-study/index.html) | Trust And Content | Consultant, Coach | Magazine |
| 022 | [Wall Of Proof](022-wall-of-proof/index.html) | Trust And Content | Coach, Consultant, Creator | Warm Editorial |
| 023 | [Blog Article Template](023-blog-article/index.html) | Trust And Content | Coach, Creator, Consultant | Magazine |
| 024 | [Podcast Home And Episode Page](024-podcast-home/index.html) | Trust And Content | Creator, Coach | Dark Stage |
| 025 | [Newsletter Sign-Up And Archive](025-newsletter-sign-up-archive/index.html) | Trust And Content | Creator, Consultant | Bento Grid |
| 026 | [Book Launch Page](026-book-launch/index.html) | Trust And Content | Consultant, Coach, Creator | Quiet Luxury |
| 027 | [Event, Workshop Or Retreat Page](027-event-retreat/index.html) | Trust And Content | Coach, Consultant | Soft Organic |
| 028 | [Contact Page And Thank-You Page](028-contact-and-thank-you/index.html) | Trust And Content | Business Owner, Consultant, Coach | Corporate Calm |
| 029 | [Font Pairings For Personal Brands](029-font-pairings/index.html) | Building Blocks | Everyone | All 10 |
| 030 | [Colour Palettes, Contrast-Checked](030-colour-palettes/index.html) | Building Blocks | Everyone | All 10 |
| 031 | [Section Patterns](031-section-patterns/index.html) | Building Blocks | Everyone | All 10 |
<!-- INDEX:END -->

## Rules Every Sample Follows

- **Fictional brands only.** Every name, testimonial, price and result is invented for teaching. Replace all of it with your own real proof. Never publish invented testimonials or numbers.
- **No stock photos.** Image slots are labelled placeholders that double as a photo brief.
- **Honest persuasion.** No fake countdown timers and no invented scarcity. Any limit shown is the kind that could be real: seats, dates, a calendar.
- **Search-ready code.** 1 H1, a real title and description, canonical and Open Graph tags, JSON-LD that matches the visible text, and every word in the HTML itself.
- **A trust footer everywhere.** About, Contact, Privacy, Terms and Refunds, even on pages with no menu.
- **Accessible by default.** Contrast is checked at build time against WCAG AA. Tap targets are 48px or more. Focus states are visible. Motion respects the reduced-motion setting.
- **Kept out of Google on purpose.** Each sample carries a clearly commented `noindex` line because the brands are fictional. Delete that line when the page is yours.

## The Research

The library draws on four bodies of work, all listed with sources on the research page:

- **Behaviour and decision science:** Kahneman and Tversky, Cialdini, Fogg, Ariely, Thaler, Berger, Deci and Ryan.
- **Page and interface laws:** Nielsen Norman Group's eyetracking research and the Laws of UX.
- **Marketing and copy:** Schwartz, Ogilvy, Caples, Hopkins, Dunford, Ries and Trout, Hormozi, Brunson, Miller, Rackham, Voss.
- **Search and AI answers:** Google's own documentation and current reporting on it, including the retirement of FAQ rich results on 7 May 2026 and Google's May 2026 guide to its generative AI features.

Search rules change often. Before you rely on any rule here, check Google's current documentation. If this library and Google disagree, Google wins.

## Rebuilding

The library is generated from page definitions in `src/pages`. You only need Python 3.

```bash
python3 src/build.py     # writes every sample, notes page, the gallery and the research page
python3 src/check.py     # checks tags, headings, structured data, links, labels and dashes
python3 src/shots.py     # optional: regenerates preview.jpg (needs Google Chrome and Pillow)
```

To add a page type, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits And Licence

© Authority Builder™ · Yasmin Cronin. All rights reserved.

Members of the Authority Builder communities may adapt the sample pages for their own business websites. The library itself, including its notes and prompts, may not be resold, redistributed or republished without written permission.

The gallery format (numbered folders, each with a reference and a live self-contained sample) is adapted from [robonuggets-design-inspo](https://github.com/robonuggets/robonuggets-design-inspo) by RoboNuggets, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The format was adapted. Every sample, the code, the notes and the research in this repository are new. See [CREDITS.md](CREDITS.md).

Nothing in this library is legal, financial or professional advice. See the disclaimer in the footer of the gallery.
