#!/usr/bin/env python3
"""Pre-launch check: scan a site folder for anything from the demo that is still there.

    python3 src/prelaunch.py path/to/your/site

Run it on your own copy of a sample site before you publish. It prints each leftover with its file and line,
and exits with an error while anything remains. It changes nothing.
"""
import pathlib
import re
import sys

CHECKS = [
    (r"example\.com/connect/[a-z0-9-]+", "A link that still needs your real destination"),
    (r"[a-z0-9-]+\.example\b", "A demo address. Replace it with your real one"),
    (r"DEMO NOTE|class=\"demo\"", "The demo note in the footer. Delete it"),
    (r"ABN 00 000 000 000", "The placeholder ABN"),
    (r"\(0\d\) 5550 \d{4}|\+61 \d 5550 \d{4}|tel:\+61\d5550\d{4}", "A fictional phone number"),
    (r"Template wording for a fictional brand", "A policy page that is still the template"),
    (r"\[(?:State|Say) [^\]]+\]", "A blank in a policy page"),
    (r"Sample testimonials for a fictional brand|Sample figures|Sample data", "A note saying the proof is sample content"),
]
NEEDED = ("images/hero-1920.webp", "images/hero-960.webp", "icon-192.png", "share.jpg", "robots.txt", "sitemap.xml", "thank-you.html", "404.html")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = pathlib.Path(sys.argv[1])
    files = sorted(p for p in root.rglob("*") if p.suffix in (".html", ".xml", ".txt", ".ics", ".toml"))
    if not files:
        sys.exit(f"No site files found in {root}")
    found = 0
    for pattern, meaning in CHECKS:
        hits = []
        for f in files:
            for n, line in enumerate(f.read_text(errors="ignore").splitlines(), 1):
                hits += [(f.relative_to(root), n, m.group(0)) for m in re.finditer(pattern, line)]
        if hits:
            found += len(hits)
            print(f"\n{meaning} ({len(hits)})")
            for f, n, text in hits[:12]:
                print(f"  {f}:{n}  {text}")
            if len(hits) > 12:
                print(f"  and {len(hits) - 12} more")
    for name in NEEDED:
        if not (root / name).exists():
            found += 1
            print(f"\nMissing file: {name}")
    print(f"\n{found} things to fix." if found else "Nothing left from the demo. Ready to launch.")
    sys.exit(1 if found else 0)


if __name__ == "__main__":
    main()
