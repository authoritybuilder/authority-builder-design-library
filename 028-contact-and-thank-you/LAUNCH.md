# Launch Checklist · 028 Contact Page And Thank-You Page

The `site` folder is a complete website. Upload it to Netlify, or any static host, and every page, link and form works.
What it cannot contain is you. Work through this list, then run the pre-launch check at the end.

## 1. Make It Yours

- [ ] Replace the demo brand (Calloway Finch), the copy, the prices and the proof with your own. The comments in the HTML say what each section is for.
- [ ] Delete the demo note in the footer of all 7 pages. Search for `DEMO NOTE`.
- [ ] Replace `callowayfinch.example` with your real address. It appears 75 times across the pages, `sitemap.xml` and `robots.txt`.
- [ ] Replace the contact details: hello@callowayfinch.example · (08) 5550 0163, Adelaide, South Australia and the placeholder ABN 00 000 000 000.

## 2. Pictures

- [ ] The painting in `site/images/` can stay. To use your own photo, save it as `hero-1920.webp` (1920px wide) and `hero-960.webp` (960px wide) in the same folder. Nothing in the code needs to change.
- [ ] Replace `icon-192.png`, `icon-512.png` and `share.jpg` with your own mark and share image, keeping the file names.
- [ ] Testimonials show initials. Add client photos only with their permission.

## 3. Connect Your Accounts (0 Links)

None. Every link on this site already goes to a real page.

## 4. Forms (1)

- `enquiry` on index.html

Every form posts to the thank-you page, names its fields, marks what is required and carries a hidden spam trap. They follow Netlify's own pattern for plain HTML forms.

- [ ] **On Netlify:** open Forms for your site, select Enable form detection, then deploy again. Netlify scans for forms from the next deploy. Entries appear under Forms, and you can have them emailed to you.
- [ ] **On another host, or to send entries straight to your email tool:** change each form's `action` to the address your tool gives you. On a host with no form handling, a form will show an error until you do.
- [ ] Netlify writes the thank-you path with a leading slash. With your site at the top of your domain, `thank-you.html` and `/thank-you.html` are the same page. Use the second if you move a form into a subfolder.
- [ ] Send a test entry through every form, then check that the thank-you page appears and the entry arrived.

## 6. Policies

- [ ] Rewrite `privacy.html`, `terms.html` and `refunds.html` in your own words and have a lawyer check them. They are marked as template wording on the page.
- [ ] Never publish a guarantee you do not actually offer.

## 7. Structured Data

- [ ] In the `application/ld+json` block near the top of each page, check every fact against the visible page after your edits.
- [ ] Add a `sameAs` list with your real profile links (LinkedIn, Instagram, YouTube) to the Organization and Person entries.
- [ ] Adding this page to a site you already have, at an address like `/masterclass/`? Update its canonical link, its `og:url` and its line in `sitemap.xml` to that address, and add breadcrumb markup.

## 8. After Launch

- [ ] Check that http, https, www and non-www all land on 1 address.
- [ ] Verify the site in Google Search Console and Bing Webmaster Tools, and submit `sitemap.xml`.
- [ ] Run Google's Rich Results Test and PageSpeed Insights on the live address.

## Pre-Launch Check

From the library folder, run:

```bash
python3 src/prelaunch.py path/to/your/site
```

It lists anything from this checklist that is still in the files. Launch when it reports nothing left from the demo.
