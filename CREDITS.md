# Credits

## Format

The gallery format is adapted from **robonuggets-design-inspo** by RoboNuggets.

- Source: https://github.com/robonuggets/robonuggets-design-inspo
- Licence: Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/
- What was adapted: the idea of a gallery index with 1 numbered folder per entry, each holding a self-contained live HTML sample.
- What changed: everything else. No reference images, sample files, text or code from the original repository are included here. All 28 sample sites, their paintings, the 3 building-block pages, the build system, the teaching notes, the prompts and the research page were made new for this library.
- This credit does not imply that RoboNuggets endorses this library.

## Fonts

All typefaces are loaded from Google Fonts under their open licences: Newsreader, DM Sans, Cormorant Garamond, Jost, Archivo, Inter, Bricolage Grotesque, Instrument Sans, DM Serif Display, Nunito Sans, Syne, Plus Jakarta Sans, Bebas Neue, Manrope, Source Serif 4, IBM Plex Sans, IBM Plex Mono, Playfair Display, Libre Franklin, Caprasimo, Space Grotesk, Caveat and Fraunces.

## Paintings, Illustrations And Icons

Every picture in the samples is original and was made for this library.

- **Paintings.** Each site's painting is composed and painted by `src/paint.py`, a program in this repository. It builds a scene from shapes, gradients and noise, then lays down brush strokes that follow the shapes, large brushes first and fine brushes last. No stock photos, no photographs of real people and no AI image model are used.
- **Icons, sketches and initials.** Drawn as inline SVG by `src/art.py` and coloured from each page's own tokens. No icon library is used.

A painting can stay on a site you launch, or you can replace it with your own photograph. The brief for each photograph is in that site's `LAUNCH.md` and in its notes.

## Research

Books are cited beside each principle on the research page (`canon/index.html`). Web sources read in November 2026 are listed at the foot of that page.

The research applied to each page type is listed, with links, on that page's notes and collected on the research page. These are benchmarks published by testing firms and software vendors, and several are reported second-hand. They are credited as findings, not reproduced.

## Audit And Measurement

The SEO and AI search checks in `src/audit.py` follow the Full SEO and AI Search Audit by Yasmin Cronin. Speed and accessibility scores come from Lighthouse (Google, Apache 2.0), run locally by `src/speed.mjs`. Text contrast over the paintings is measured by `src/legible.mjs`, which uses the browser driver that comes with Lighthouse. Lighthouse is not included in this repository.

The forms follow the pattern in Netlify's documentation for plain HTML forms. Netlify is not affiliated with this library.

## Real Sites Studied

4 real sites were read for structure and messaging only: James Clear, Justin Welsh, April Dunford and Marie Forleo's B-School. No words, images or layouts from those sites are reproduced. Each is credited on the research page and on the notes page of any sample that learned from it.

## Sample Content

Every brand, person, business, testimonial, price and result in the sample pages is fictional and was invented for teaching. Any resemblance to a real business or person is coincidental. Sample domains use the reserved `.example` ending and sample phone numbers use ranges set aside for fiction.
