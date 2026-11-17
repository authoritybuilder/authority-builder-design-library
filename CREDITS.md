# Credits

## Format

The gallery format is adapted from **robonuggets-design-inspo** by RoboNuggets.

- Source: https://github.com/robonuggets/robonuggets-design-inspo
- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/
- What was adapted: the idea of a gallery index with 1 numbered folder per entry, each holding a self-contained live HTML sample.
- What changed: everything else. No reference images, sample files, text or code from the original repository are included here. All 28 sample sites, their paintings, the 3 building-block pages, the build system, the teaching notes, the prompts and the research page were made new for this library.
- This credit does not imply that RoboNuggets endorses this library.

## Fonts

All typefaces are loaded from Google Fonts under their open licences: Instrument Serif, Inter, Cormorant Garamond, Jost, Archivo, Bricolage Grotesque, Instrument Sans, Fraunces, Nunito Sans, Syne, Plus Jakarta Sans, Bebas Neue, Manrope, Source Serif 4, IBM Plex Sans, IBM Plex Mono, Bodoni Moda, Libre Franklin, Caprasimo, Space Grotesk and Caveat.

The 10 pairings follow 1 rule: an expressive display face for the headline over a quiet, highly readable sans for everything else. 3 were changed in November 2026 after a review of current editorial typography: Instrument Serif replaced Newsreader, Fraunces replaced DM Serif Display and Bodoni Moda replaced Playfair Display.

## Paintings, Illustrations And Icons

Every picture in the samples is original and was made for this library.

- **Paintings.** Each site's painting is composed and painted by `src/paint.py`, a program in this repository. It builds a scene from shapes, gradients and noise, then lays down brush strokes that follow the shapes, large brushes first and fine brushes last. No stock photos, no photographs of real people and no AI image model are used.
- **Photo placeholders.** Every picture of a person or place is a named file in a site's `images` folder. The files that ship are painted by `src/people.py`: a back-lit figure with no face over a soft-focus piece of that site's painting, or a crop of the painting for a place. They stand in for the owner's real photographs and depict no real person.
- **Icons and sketches.** Drawn as inline SVG by `src/art.py` and coloured from each page's own tokens. No icon library is used.

A painting can stay on a site you launch. The photo placeholders are there to be replaced. The brief for each photograph is in that site's `LAUNCH.md` and in its notes.

## Research

Books are cited beside each principle on the research page (`canon/index.html`). Web sources read in November 2026 are listed at the foot of that page.

Sources read for the design and conversion review in November 2026:

- Unbounce, Conversion Benchmark Report (41,000 landing pages), on reading level and conversion, as reported by Apexure (https://www.apexure.com/blog/landing-page-conversion-rate-benchmarks-by-industry) and Colorlib (https://colorlib.com/wp/landing-page-statistics/). Unbounce's own method is at https://unbounce.com/conversion-benchmark-report/methodology/. The figure is second-hand, so each audit table says so.
- Made Good Designs, Web Typography Trends 2026 (https://madegooddesigns.com/web-typography-trends-2026/), on the return of display serifs set over a plain sans.
- Thrive Themes, 7 Coaching Landing Page Examples (https://thrivethemes.com/coaching-landing-page-examples/), on 1 focused offer per page, a benefit-led headline, real proof and 1 clear action.
- The robonuggets-design-inspo samples themselves, studied again for technique only: full-bleed painted heroes, a floating glass menu, pill-shaped controls, tightly tracked display type and very small, widely tracked labels.

The research applied to each page type is listed, with links, on that page's notes and collected on the research page. These are benchmarks published by testing firms and software vendors, and several are reported second-hand. They are credited as findings, not reproduced.

## Audit And Measurement

The SEO and AI search checks in `src/audit.py` follow the Full SEO and AI Search Audit by Yasmin Cronin. Speed and accessibility scores come from Lighthouse (Google, Apache 2.0), run locally by `src/speed.mjs`. Text contrast over the paintings is measured by `src/legible.mjs`, which uses the browser driver that comes with Lighthouse. Lighthouse is not included in this repository.

The forms follow the pattern in Netlify's documentation for plain HTML forms. Netlify is not affiliated with this library.

## Real Sites Studied

4 real sites were read for structure and messaging only: James Clear, Justin Welsh, April Dunford and Marie Forleo's B-School. No words, images or layouts from those sites are reproduced. Each is credited on the research page and on the notes page of any sample that learned from it.

## Sample Content

Every brand, person, business, testimonial, price and result in the sample pages is fictional and was invented for teaching. Any resemblance to a real business or person is coincidental. Sample domains use the reserved `.example` ending and sample phone numbers use ranges set aside for fiction.

## Photographs

Each site's hero photograph is from [Pexels](https://www.pexels.com), used under the [Pexels licence](https://www.pexels.com/license/): free to use, no attribution required,
not to be sold or redistributed as stand-alone files. Each link leads to the photograph's page, which names its photographer. They are fetched and cut to size by `src/photos.py`.

| Site | Page | Pexels photo | Shows |
|---|---|---|---|
| 001 | Coach Homepage | [733170](https://www.pexels.com/photo/733170/) | Sunrise over mountain ridges, with cloud filling the valleys below |
| 002 | Consultant Authority Site | [11506719](https://www.pexels.com/photo/11506719/) | A city skyline at dusk under an orange sky, reflected in the river |
| 003 | Creator Hub | [19749051](https://www.pexels.com/photo/19749051/) | A building facade of bright yellow, pink and orange panels |
| 004 | Local Service Business | [37542742](https://www.pexels.com/photo/37542742/) | A sandy beach with grassy dunes and small waves on a clear day |
| 005 | About Founder Story | [34741211](https://www.pexels.com/photo/34741211/) | Layers of misty hills at dawn in soft purple light |
| 006 | Speaker Media Kit | [27806693](https://www.pexels.com/photo/27806693/) | An empty theatre stage with dark curtains under dim light |
| 007 | Signature Program Sales Page | [33315930](https://www.pexels.com/photo/33315930/) | Green hills fading into morning mist |
| 008 | Online Course Sales Page | [1128207](https://www.pexels.com/photo/1128207/) | A bright desk by a window with an open laptop and a glass of water |
| 009 | Membership Community Join | [37078917](https://www.pexels.com/photo/37078917/) | A pottery studio with shelves of handmade pots and tools |
| 010 | Mastermind Application | [15896696](https://www.pexels.com/photo/15896696/) | A still mountain lake at dusk, framed by dark pine trees |
| 011 | Services And Pricing | [27544679](https://www.pexels.com/photo/27544679/) | A minimal plaster interior with a palm leaf in a vase and soft shadows |
| 012 | Digital Product Shop | [19309633](https://www.pexels.com/photo/19309633/) | A wall of pastel panels in green, peach, lilac and coral under a blue sky |
| 013 | Corporate Training | [4863995](https://www.pexels.com/photo/4863995/) | Snow-capped mountains reflected in a still lake |
| 014 | Lead Magnet Opt In | [34803978](https://www.pexels.com/photo/34803978/) | A wooden desk with an open laptop, a coffee cup and a plant |
| 015 | Webinar Registration | [20208915](https://www.pexels.com/photo/20208915/) | A city skyline at night, its lights reflected in dark water |
| 016 | Quiz Scorecard Landing | [7354510](https://www.pexels.com/photo/7354510/) | A pink and mint still life of simple shapes with a single leaf |
| 017 | Challenge Page | [32915493](https://www.pexels.com/photo/32915493/) | A red dirt road running through outback scrub |
| 018 | Waitlist Launching Soon | [32485141](https://www.pexels.com/photo/32485141/) | A desk and lamp in silhouette against a lit window at night |
| 019 | Book A Call | [31874086](https://www.pexels.com/photo/31874086/) | A country road curving past a green field under a blue sky |
| 020 | Link In Bio | [5876967](https://www.pexels.com/photo/5876967/) | A tropical beach with palm trees leaning over turquoise water |
| 021 | Case Study | [8594371](https://www.pexels.com/photo/8594371/) | A calm sea at dawn in soft pink and blue light |
| 022 | Wall Of Proof | [18201085](https://www.pexels.com/photo/18201085/) | A city skyline at sunrise, seen from above |
| 023 | Blog Article | [37109411](https://www.pexels.com/photo/37109411/) | A lake in morning mist with mountains behind |
| 024 | Podcast Home | [12989652](https://www.pexels.com/photo/12989652/) | The Milky Way above the silhouettes of trees |
| 025 | Newsletter Sign Up Archive | [36123565](https://www.pexels.com/photo/36123565/) | A white desk with an open laptop, a notebook and a cup |
| 026 | Book Launch | [11987205](https://www.pexels.com/photo/11987205/) | A wheat field in golden evening light |
| 027 | Event Retreat | [1005258](https://www.pexels.com/photo/1005258/) | A small cabin on a hillside at golden hour, with cloud in the valley |
| 028 | Contact And Thank You | [19806361](https://www.pexels.com/photo/19806361/) | Green hills and trees under low morning mist |

## Sample Video Clips

Sites 001, 004 and 027 each ship with a 4-second clip at `site/media/video-1.mp4`. Each was generated from that site's Pexels photograph with the open
Wan 2.2 image-to-video model, run on a public Hugging Face Space. They are AI-generated stand-ins that show how a video slot plays. Replace them with your own footage.
