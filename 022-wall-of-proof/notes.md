# 022 · Wall Of Proof

**Group:** Trust And Content  
**For:** Coach, Consultant, Creator  
**Style:** Warm Editorial (Newsreader + DM Sans)  
**Sample brand:** Sage Holloway (fictional)

A testimonial page that reads as evidence, not applause. Every quote leads with a result, and the page explains how the quotes were gathered.

## Why This Page Works

- Every quote starts with a result label, so the page can be scanned for the outcome a reader cares about.
- It says how the reviews are gathered and who cannot be named. Explaining the method is what makes the praise credible.
- All of it is text. Testimonials in images, PDFs or a third-party widget cannot be read or quoted by Google and AI tools.
- There are no star ratings in the code. Google excludes self-serving reviews, so the page relies on words and specifics.

## The Psychology At Work

| Principle | Where you can see it |
|---|---|
| **Social Proof** (Robert Cialdini, Influence (1984, revised 2021)) | 9 people in the reader's exact situation, each with a role and company type. |
| **Authority** (Robert Cialdini, Influence (1984, revised 2021)) | Independent collection at 12 months lends the numbers weight. |
| **Reason-Why And Specifics** (John E. Kennedy; Claude Hopkins, Scientific Advertising (1923)) | Each quote carries a concrete detail: week 3, 4 rehearsals, 11 reports to 6. |
| **Liking** (Robert Cialdini, Influence (1984, revised 2021)) | Small human outcomes (sleep, Fridays) sit beside the big professional ones. |
| **Miller's Law** (George Miller, Laws of UX) | Result labels chunk 9 quotes into scannable pieces. |
| **Content In The HTML** (How AI crawlers read pages, Full SEO and AI Search Audit, ground rules) | Every testimonial is text in the page, including the video's transcript. |
| **No Self-Awarded Stars** (Google Search Central, Review snippet guidelines) | No review-star markup on the coach's own site. |

## Page Structure

1. Hero: a plain claim about what the page contains
2. Numbers row: the summary for skimmers
3. The wall: each quote led by its result, grouped so a reader can find someone like them
4. A longer story on video, with a transcript, for the reader who wants depth
5. How the reviews are collected: the section that makes all the others believable
6. Closing call to action

## Search Card

- **Title:** Client Results And Reviews | Sage Holloway, Executive Coach
- **Description:** What 9 first-time chief executives say about coaching with Sage Holloway, in their own words, with the result each one came for. Plus how these reviews are collected.
- **Structured data:** CollectionPage, BreadcrumbList
- Keep proof on your own page as text. Reviews trapped in screenshots or a slider loaded by script are invisible to search.
- Reviews on independent sites (Google reviews, industry directories) help in a different way: they are mentions of your name elsewhere.

## Borrow This

- Lead every testimonial with a 1 to 3 word result.
- Say how and when you collect reviews.
- Give role and company type even when a name is withheld.
- Add a transcript under any video testimonial.

## Build Your Own

```text
Build me a wall of proof for my business, modelled on sample 022 in the Authority Builder Design Library.

ABOUT MY BUSINESS
- Business name and my name: [yours]
- Who I help and the result they get: [1 line]
- My main offer and its price: [yours]
- The 1 action I want a visitor to take on this page: [yours]
- Real proof I can use (names, results, numbers, press): [paste it here]

STRUCTURE, IN THIS ORDER
1. Hero: a plain claim about what the page contains
2. Numbers row: the summary for skimmers
3. The wall: each quote led by its result, grouped so a reader can find someone like them
4. A longer story on video, with a transcript, for the reader who wants depth
5. How the reviews are collected: the section that makes all the others believable
6. Closing call to action

DESIGN DIRECTION
Warm Editorial. Paper tones, a bookish serif, italic emphasis. Feels like a considered letter.
Fonts: Newsreader + DM Sans from Google Fonts. Keep 1 accent colour and use it only for the main action.
Mobile-first. Buttons at least 48px tall. Visible focus states. Respect reduced motion.

PERSUASION RULES
- Robert Cialdini, Social Proof: 9 people in the reader's exact situation, each with a role and company type.
- Robert Cialdini, Authority: Independent collection at 12 months lends the numbers weight.
- John E. Kennedy; Claude Hopkins, Reason-Why And Specifics: Each quote carries a concrete detail: week 3, 4 rehearsals, 11 reports to 6.
- Robert Cialdini, Liking: Small human outcomes (sleep, Fridays) sit beside the big professional ones.
- George Miller, Miller's Law: Result labels chunk 9 quotes into scannable pieces.
- How AI crawlers read pages, Content In The HTML: Every testimonial is text in the page, including the video's transcript.
- Google Search Central, No Self-Awarded Stars: No review-star markup on the coach's own site.

SEARCH-READY RULES
- 1 clear H1. A title that includes my brand name. A description that says who the page is for.
- Every word in the HTML itself. Nothing that needs JavaScript to appear.
- JSON-LD structured data (CollectionPage, BreadcrumbList) that matches the visible text.
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
