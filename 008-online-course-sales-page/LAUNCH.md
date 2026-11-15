# Launch Checklist · 008 Online Course Sales Page

The `site` folder is a complete website. Upload it to Netlify, or any static host, and every page, link and form works.
What it cannot contain is you. Work through this list, then run the pre-launch check at the end.

## 1. Make It Yours

- [ ] Replace the demo brand (Sam Okonkwo Studio), the copy, the prices and the proof with your own. The comments in the HTML say what each section is for.
- [ ] Delete the demo note in the footer of all 8 pages. Search for `DEMO NOTE`.
- [ ] Replace `samokonkwo.example` with your real address. It appears 82 times across the pages, `sitemap.xml` and `robots.txt`.
- [ ] Replace the contact details: hello@samokonkwo.example, Melbourne, Victoria and the placeholder ABN 00 000 000 000.

## 2. Your Photos

Every picture is a file in `site/images/`. To use your own, save it under the same file name, at about the size shown. Nothing in the code needs to change.
The files that ship are painted stand-ins, each labelled with its file name. The pre-launch check tells you which are still in place.

| File | Size | Who Or What | On | The Photo To Take |
|---|---|---|---|---|
| `hero-2560.webp`, `hero-1920.webp`, `hero-1280.webp`, `hero-960.webp` | 2560, 1920, 1280 and 960 wide, all 16:10 | The background painting | every painted section | It can stay. A wide photo with a quiet area for the words also works |
| `video-1.jpg` | 1280 × 720 | A video still | index.html | lesson 1 as a free preview, with captions |
| `you-headshot.jpg` | 240 × 240 | You | index.html, contact.html, thank-you.html, 404.html | Your headshot, cropped square. It appears small wherever your name does |
| `face-1.jpg` | 200 × 200 | Aiko M. | index.html | A square headshot, used with their permission |
| `face-2.jpg` | 200 × 200 | Luis F. | index.html | A square headshot, used with their permission |
| `face-3.jpg` | 200 × 200 | Hannah O. | index.html | A square headshot, used with their permission |
| `you-1.jpg` | 900 × 1125 | You | index.html | Sam at a desk, laptop open, proposal on screen |
| `face-4.jpg` | 200 × 200 | Noah B. | index.html | A square headshot, used with their permission |
| `you-2.jpg` | 900 × 1125 | You | about.html | a clear, friendly portrait of Sam. Use the same photo on every profile |

- [ ] Replace every photo of you. Use the same headshot on your social profiles so people recognise you.
- [ ] Replace client photos only with their permission. If you have none yet, delete that `<img>` tag and the quote stands on the name alone.
- [ ] After swapping a photo, read its `alt` text in the HTML and make it describe your picture.
- [ ] Replace `icon-192.png`, `icon-512.png` and `share.jpg` with your own mark and share image, keeping the file names.

## 3. Connect Your Accounts (3 Links)

These can only be finished with your own accounts. Each points at example.com until you give it a real destination, so nothing breaks in the meantime.
Search the folder for `example.com/connect` to find them all.

| Replace this | Shown on the page as | In | Times |
|---|---|---|---|
| `example.com/connect/checkout` | Enrol With A Review | index.html | 3 |

## 4. Forms (1)

- `contact` on contact.html

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
