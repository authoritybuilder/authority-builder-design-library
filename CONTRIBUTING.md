# Adding A Site To The Library

Every sample is generated from a short page definition. You describe the main page as data. The build writes the whole site around it (trust pages, the action page, thank-you and not-found pages, policies, crawler files and host settings), runs the audit on it, then writes the launch checklist, the notes page, the notes file and the gallery card.

## The Short Version

1. Open a file in `src/pages` and copy an existing page definition (a Python `dict`).
2. Give it the next number in `n`, a `slug`, a `name`, a `group` and a `theme`.
3. Invent a fictional brand. Use a `.example` domain.
4. List the sections in order. Each section is a pair: the pattern name and its content.
5. Fill in `why`, `principles`, `borrow` and, if you studied a real site, `study`.
6. Research that page type. Add a function for it in `src/upgrades.py` that makes each change and returns the finding it came from. Add each new source to `R` with a link you have actually read.
7. Give it a painting. Add the page to `ART` in `src/paint.py` (scene, seed, palette) and to `ART` in `src/upgrades.py` (scene, whether the words on it are light or dark, and the alt text).
8. Run the build, the painting, the check, the screenshots and the measurements, then the build once more:

```bash
python3 src/build.py
python3 src/paint.py 029      # only the entry you added: its painting in 2 sizes
python3 src/build.py          # lists the photo files the new site needs
python3 src/people.py 029     # paints its photo placeholders
python3 src/check.py
python3 src/shots.py 029      # preview, icons and share image
node src/speed.mjs 029        # Lighthouse, for the audit table
node src/legible.mjs 029      # text contrast over the painting, for the audit table
python3 src/build.py          # picks up the new files and measurements
```

The build prints any audit check that still fails. Fix the page until it prints none.

The 3 building-block entries always take the last 3 numbers, so they move down by 1 when you add a page. The build renumbers them for you.

## What Each Field Does

| Field | Purpose |
|---|---|
| `n`, `slug`, `name` | Number, folder name and display name. |
| `group` | 1 of the 4 gallery groups. |
| `aud` | Who it is for: Coach, Creator, Consultant, Business Owner. Drives the gallery filter. |
| `theme` | 1 of the 10 style directions in `src/themes.py`. |
| `brand` | The fictional brand: name, person, role, domain, monogram, footer line. |
| `title`, `desc` | The title tag and meta description. Write them as carefully as the headline. |
| `schema` | Which structured data types to generate. Extra facts go in `ld`. |
| `nav`, `cta` | Menu links and header button. Use `nav=None` for landing pages with no menu. |
| `sections` | The page, in order. Add `_="…"` to each section to say what it is for. That line becomes a code comment and a step in the build prompt. |
| `why` | 3 or 4 plain reasons the page works. |
| `principles` | Pairs of a principle id from `src/canon.py` and where it shows up on this page. |
| `borrow` | 3 or 4 things a reader can lift straight away. |
| `seo` | Notes for the search card that are specific to this page type. |

## Section Patterns

Every pattern is shown once on the Section Patterns page (entry 031). The pattern names are the function names in `src/sections.py`: `hero_split`, `hero_center`, `hero_form`, `hero_stage`, `hero_article`, `bento`, `linkbio`, `logos`, `stats`, `quotes`, `metrics`, `doors`, `prose`, `cards`, `steps`, `split`, `compare`, `modules`, `pricing`, `guarantee`, `faq`, `cta`, `feed`, `capture`, `schedule`, `article`, `player`, `products`, `contact`, `quiz`, `thanks`, `bios`, `trust`, `matrix`, `shownotes` and `legal`.

In any text field, `*word*` gives emphasis, `**word**` gives bold and `|` forces a line break.

## Adding A Style Direction

Add an entry to `THEMES` in `src/themes.py`: a Google Fonts link, the colour tokens and a few signature rules. The build checks every text and button pairing against WCAG AA (4.5 to 1) and prints any failures. Fix them before you ship.

## Adding A Principle

Add an entry to `C` in `src/canon.py` with its group, name, originator, source and a plain-English meaning. Cite the book or the page you actually read. If you cannot name the source, leave it out.

## House Rules

- **Fictional brands only.** Never use a real business, a real person or a real testimonial in a sample.
- **Borrow the technique, never the copy, the images or the layout.** If a sample still looks or reads like the site that inspired it, keep working.
- **No fake urgency.** No countdown timers. No invented scarcity. Limits must be the kind that could be real.
- **Caveat every results claim.** Income and outcome figures carry a results-are-not-typical line.
- **Everything in the HTML.** No content that needs JavaScript to appear. Only the quiz runs a script, and its questions are in the HTML either way.
- **No dead ends.** Every button leads to a real page, a real section or a working form. A destination that needs the owner's own account uses `kit.connect("what it is")`, which the launch checklist then lists.
- **Every form sends.** Build forms with `form_open` in `src/sections.py` so they get a name, named fields, the spam trap and the thank-you page.
- **Words over a painting must measure up.** `src/legible.mjs` has to report no line below the bar before you ship.
- **Every picture is a named file with a brief.** A visual with `kind="person"` becomes a photo of the owner, `kind="scene"` a photo of a place, and every testimonial name gets a face file. Write the `label` as the brief for the real photo. It becomes a code comment, a line in the notes and a row in the launch checklist.
- **A person at every decision.** The owner's face belongs on the first screen, beside the form and under the closing button. The components do this for you; do not remove it.
- **Proof beside the button.** Each page puts 1 line of reassurance and 1 piece of proof next to its main action.
- **Check the rule before you teach it.** Search guidance changes. Read Google's current page before adding a search note.
- **Australian spelling. No em dashes. Numerals for numbers.**
