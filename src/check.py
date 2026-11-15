#!/usr/bin/env python3
"""Checks every built page. Run after build.py.

    python3 src/check.py

Looks for: unbalanced tags, missing or repeated H1, missing title, description or canonical,
structured data that does not parse, broken local links, images without alt text,
form fields without labels, and stray em or en dashes.
"""
import json
import pathlib
import re
import sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent.parent
VOID = {"meta", "link", "br", "img", "input", "hr", "source"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errs, self.h1, self.links, self.labels, self.inputs, self.noalt = [], [], 0, [], set(), [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        if tag in ("a", "link") and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.links.append(a.get("src", ""))
            if "alt" not in a:
                self.noalt += 1
        if tag == "label" and a.get("for"):
            self.labels.add(a["for"])
        if tag in ("input", "select", "textarea") and a.get("type") != "radio":
            self.inputs.append(a.get("id"))
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errs.append(f"closing </{tag}> but open is <{self.stack[-1] if self.stack else None}>")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def main():
    bad = 0
    files = [ROOT / "index.html", ROOT / "canon" / "index.html"] + sorted(ROOT.glob("[0-9][0-9][0-9]-*/*.html")) + sorted(ROOT.glob("[0-9][0-9][0-9]-*/site/*.html"))
    for f in files:
        t = f.read_text()
        p = P()
        p.feed(t)
        errs = list(p.errs[:3])
        if p.stack:
            errs.append(f"unclosed: {p.stack[-3:]}")
        if p.h1 != 1 and "section-patterns" not in str(f):
            errs.append(f"{p.h1} H1 elements")
        if "<title>" not in t or 'name="description"' not in t:
            errs.append("missing title or description")
        if f.parent.name == "site" and 'rel="canonical"' not in t:
            errs.append("missing canonical")
        for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try:
                json.loads(m)
            except ValueError as ex:
                errs.append(f"JSON-LD: {ex}")
        for l in p.links:
            if not l or l.startswith(("http", "#", "data:", "mailto:", "tel:")):
                continue
            target = (f.parent / l.split("#")[0]).resolve()
            if not target.exists():
                errs.append(f"broken link: {l}")
        if f.parent.name == "site":
            ids = set(re.findall(r'\bid="([^"]+)"', t))
            for l in p.links:
                if l.startswith("#") and len(l) > 1 and l[1:] not in ids:
                    errs.append(f"anchor with no target: {l}")
        if p.noalt:
            errs.append(f"{p.noalt} images without alt")
        for i in p.inputs:
            if i not in p.labels:
                errs.append(f"field without label: {i}")
        if re.search("[—–]", t):
            errs.append("em or en dash found")
        if errs:
            bad += 1
            print(f.relative_to(ROOT), "\n   " + "\n   ".join(dict.fromkeys(errs)))
    print(f"Checked {len(files)} pages. {bad} with problems.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
