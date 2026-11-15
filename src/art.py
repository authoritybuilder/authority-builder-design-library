"""Illustration for the samples, drawn as inline SVG so every page stays a single file.

Portraits are faceless editorial figures. Scenes are small flat illustrations. Colours come from the
page's own tokens (the i-* classes), so one drawing suits every style direction.
Swap any of them for a real photograph when you make a page yours: the HTML comment beside each one is the photo brief.
"""
import hashlib

SKIN = ["#F3CDAA", "#E3AE82", "#C98B5B", "#A96D43", "#80502F", "#5B3721"]
SHADE = ["#E2B48E", "#CE9568", "#B07447", "#8F5833", "#693F23", "#472A17"]
HAIR = ["#1E1A18", "#3A2A21", "#6A4428", "#A56A33", "#CDAA72", "#9A9A9E", "#B24A30"]

FRINGE = "M134 212 C132 148 172 128 204 130 C248 132 270 170 266 210 C244 194 220 178 196 176 C172 178 150 194 134 212Z"
CAP = "M134 214 C126 150 168 128 202 130 C244 132 276 158 266 216 C256 186 236 170 200 168 C166 168 144 186 134 214Z"
STYLES = {
    "short": ("", CAP),
    "bob": ("M124 222 C116 146 160 120 200 120 C242 120 284 146 276 222 L280 296 Q280 318 258 316 L142 316 Q120 318 120 296Z", FRINGE),
    "long": ("M118 222 C108 142 160 116 200 116 C242 116 292 142 282 222 L298 430 Q300 452 276 450 L124 450 Q100 452 102 430Z", FRINGE),
    "wavy": ("M120 222 C112 144 160 118 200 118 C242 118 288 144 280 222 C292 262 276 300 290 340 C296 372 262 380 250 356 L150 356 C138 380 104 372 110 340 C124 300 108 262 120 222Z",
             "M134 214 C130 150 176 128 210 132 C250 136 268 178 266 212 C246 200 232 174 190 172 C168 178 150 196 134 214Z"),
    "bun": ("M200 84 a31 31 0 1 0 .1 0Z", CAP),
    "curly": ("M146 156a30 30 0 1 0 .1 0Z M160 118a34 34 0 1 0 .1 0Z M196 96a38 38 0 1 0 .1 0Z M236 110a36 36 0 1 0 .1 0Z M256 152a30 30 0 1 0 .1 0Z M132 200a22 22 0 1 0 .1 0Z M268 200a22 22 0 1 0 .1 0Z", CAP),
    "shaved": ("", "M136 206 C138 156 172 136 200 136 C228 136 262 156 264 206 C252 180 228 168 200 168 C172 168 148 180 136 206Z"),
}

# name: (skin, hair style, hair colour, top, extras)
PEOPLE = {
    "Imogen Wren": (0, "bob", 6, "blazer", ""), "Marcus Halden": (3, "short", 0, "blazer", "g"), "Tash Okafor": (4, "curly", 0, "crew", "e"),
    "Bec Tran": (1, "long", 0, "crew", ""), "Dana Whitlock": (0, "wavy", 4, "blazer", ""), "Jonah Reyes": (2, "shaved", 1, "blazer", "b"),
    "Leila Hart": (2, "long", 1, "crew", ""), "Sam Okonkwo": (5, "shaved", 0, "crew", "b"), "Odette Laurent": (0, "bun", 5, "roll", ""),
    "Vivienne Ashcombe": (0, "bob", 5, "blazer", "e"), "Mira Castellanos": (2, "long", 0, "crew", "g"), "Ruby Nakamura": (1, "bob", 0, "crew", ""),
    "Dr Anika Shah": (3, "bun", 0, "blazer", "g"), "Nadia Flores": (2, "wavy", 2, "crew", ""), "Carmen Ortiz": (2, "bob", 1, "blazer", "e"),
    "Thandi Mokoena": (5, "curly", 0, "roll", "e"), "Frankie Doyle": (0, "short", 6, "crew", "g"), "Celeste Marchetti": (1, "long", 1, "roll", ""),
    "Ngozi Okoro": (5, "bun", 0, "blazer", "e"), "Poppy Achebe": (4, "curly", 0, "crew", "e"), "Estelle Nguyen": (1, "bob", 0, "blazer", ""),
    "Sage Holloway": (0, "short", 5, "blazer", ""), "Hattie Lindqvist": (0, "long", 4, "crew", "g"), "Lois Adeyemi": (4, "short", 0, "blazer", "e"),
    "Kofi Mensah": (5, "shaved", 0, "crew", "bg"), "Harriet Vale": (0, "bob", 2, "roll", ""), "Maren Solberg": (0, "bun", 4, "crew", ""),
    "Imelda Calloway": (2, "wavy", 5, "blazer", ""),
}


def _h(s, n):
    return int(hashlib.md5(s.encode()).hexdigest(), 16) % n


def who(name):
    if name in PEOPLE:
        return PEOPLE[name]
    st = ["short", "bob", "long", "wavy", "bun", "curly", "shaved"][_h(name + "s", 7)]
    return (_h(name, 6), st, _h(name + "h", 7), ["crew", "blazer", "roll"][_h(name + "t", 3)], ["", "g", "e", "b" if st in ("short", "shaved") else ""][_h(name + "x", 4)])


def figure(name):
    sk, st, hc, top, ex = who(name)
    back, front = STYLES[st]
    s, sh, hr = SKIN[sk], SHADE[sk], HAIR[hc]
    body = '<path class="i-a" d="M36 500 C40 404 110 356 168 346 Q200 372 232 346 C290 356 360 404 364 500Z"/>'
    if top == "blazer":
        body = ('<path class="i-c" d="M36 500 C40 404 110 356 168 346 Q200 372 232 346 C290 356 360 404 364 500Z"/>'
                '<path class="i-d" d="M166 346 L200 452 L200 500 L36 500 C40 404 110 356 166 346Z M234 346 L200 452 L200 500 L364 500 C360 404 290 356 234 346Z"/>')
    neck = f'<path fill="{sh}" d="M172 268 L228 268 L232 352 Q200 378 168 352Z"/>'
    if top == "roll":
        neck += '<path class="i-a" d="M166 306 Q200 326 234 306 L238 356 Q200 380 162 356Z"/>'
    extra = ""
    if "b" in ex:
        extra += f'<path fill="{hr}" d="M138 236 C140 296 170 314 200 314 C230 314 260 296 262 236 C252 272 230 288 200 288 C170 288 148 272 138 236Z"/>'
    if "g" in ex:
        extra += '<g fill="none" stroke="#1E1A18" stroke-width="5"><rect x="150" y="204" width="42" height="32" rx="12"/><rect x="208" y="204" width="42" height="32" rx="12"/><path d="M192 218h16"/></g>'
    if "e" in ex:
        extra += '<circle cx="134" cy="252" r="6" fill="#D9A441"/><circle cx="266" cy="252" r="6" fill="#D9A441"/>'
    return (f'<path fill="{hr}" d="{back}"/>{body}{neck}<ellipse cx="136" cy="226" rx="8" ry="14" fill="{sh}"/><ellipse cx="264" cy="226" rx="8" ry="14" fill="{sh}"/>'
            f'<ellipse cx="200" cy="218" rx="64" ry="76" fill="{s}"/><path fill="{hr}" d="{front}"/>{extra}')


DESK = ('<rect class="i-2" x="-200" y="452" width="800" height="120"/><rect class="i-d" x="118" y="366" width="164" height="92" rx="8"/>'
        '<rect class="i-c" opacity=".16" x="128" y="376" width="144" height="72" rx="3"/><circle class="i-c" opacity=".5" cx="200" cy="412" r="9"/>'
        '<path class="i-d" d="M96 458h208l10 12H86z"/><path class="i-a" d="M318 420h34v36a10 10 0 0 1-10 10h-14a10 10 0 0 1-10-10z"/>'
        '<path class="i-b" d="M52 458c-6-34 4-58 12-70 5 26 18 34 12 70z"/><rect class="i-d" x="44" y="452" width="40" height="24" rx="5"/>')


def portrait(name, wide=False, pose=0):
    """Head and shoulders. wide=True frames the figure for a 16:9 video still. pose=1 seats them at a desk, so a second picture on a page is not a repeat."""
    box = "-150 96 700 394" if wide else ("20 70 360 450" if pose else "44 84 312 390")
    extra = DESK if pose else ""
    fit = "xMidYMax" if pose or wide else "xMidYMin"
    return f'<svg viewBox="{box}" preserveAspectRatio="{fit} slice" aria-hidden="true" focusable="false">{figure(name)}{extra}</svg>'


def avatar(name):
    """Initials in a coloured disc. A real site swaps these for client photos, used with permission."""
    words = [w for w in name.replace(",", " ").split() if w.lower() not in ("dr", "the") and w[:1].isalpha()]
    ini = "".join(w[0] for w in words[:2]).upper() or "?"
    return f'<span class="av av{_h(name, 4)}" aria-hidden="true">{ini}</span>'


LINES = '<rect x="0" y="0" width="{w}" height="6" rx="3"/><rect x="0" y="14" width="{v}" height="6" rx="3"/><rect x="0" y="28" width="{w}" height="6" rx="3"/>'


def _page(x, y, rot, head, w=150, hgt=200):
    ln = "".join(f'<rect x="{x + 16}" y="{y + 52 + i * 15}" width="{(w - 32) * f:.0f}" height="6" rx="3"/>' for i, f in enumerate((1, .8, .92, .6, 1, .74, .88)))
    return (f'<g transform="rotate({rot} {x + w / 2} {y + hgt / 2})"><rect class="i-c" x="{x}" y="{y}" width="{w}" height="{hgt}" rx="9"/>'
            f'<rect class="{head}" x="{x + 16}" y="{y + 18}" width="{w * .5:.0f}" height="16" rx="8"/><g class="i-l">{ln}</g>'
            f'<rect class="{head}" x="{x + 16}" y="{y + hgt - 36}" width="{w * .34:.0f}" height="18" rx="9" opacity=".85"/></g>')


SCENES = {
    "hills": ('<rect class="i-1" width="400" height="300"/><circle class="i-c" cx="296" cy="84" r="40" opacity=".9"/>'
              '<path class="i-2" opacity=".6" d="M0 188 C80 128 150 150 220 178 C290 138 350 150 400 168 V300 H0Z"/>'
              '<path class="i-b" opacity=".8" d="M0 222 C90 180 170 200 250 226 C310 204 360 206 400 216 V300 H0Z"/>'
              '<path class="i-d" d="M0 258 C100 232 220 248 400 242 V300 H0Z"/>'
              '<g class="i-d"><path d="M66 240l15-48 15 48z"/><path d="M94 246l11-34 11 34z"/><path d="M326 236l14-44 14 44z"/></g>'
              '<path class="i-c" d="M194 232h50v-24l-25-17-25 17z"/><path class="i-a" d="M187 210l32-22 32 22-4 6-28-19-28 19z"/><rect class="i-d" x="212" y="214" width="13" height="18"/>'),
    "desk": ('<rect class="i-1" width="400" height="300"/><rect class="i-2" y="214" width="400" height="86" opacity=".75"/>'
             '<rect class="i-d" x="106" y="92" width="188" height="122" rx="9"/><rect class="i-c" x="116" y="102" width="168" height="102" rx="3"/>'
             '<g class="i-l"><rect x="130" y="118" width="74" height="9" rx="4.5"/><rect x="130" y="138" width="136" height="6" rx="3"/><rect x="130" y="151" width="112" height="6" rx="3"/></g>'
             '<rect class="i-a" x="130" y="170" width="56" height="20" rx="10"/><path class="i-d" opacity=".9" d="M88 214h224l12 13H76z"/>'
             '<path class="i-a" d="M320 182h36v36a11 11 0 0 1-11 11h-14a11 11 0 0 1-11-11z"/>'
             '<path class="i-b" d="M44 216c-8-42 4-72 15-88 6 32 23 42 14 88z"/><path class="i-b" opacity=".7" d="M60 216c10-32 31-46 46-50-4 25-15 42-30 50z"/><rect class="i-d" x="36" y="210" width="48" height="28" rx="6"/>'),
    "stage": ('<rect class="i-d" width="400" height="300"/><path class="i-a" opacity=".26" d="M118 0 L50 236 H214Z"/><path class="i-c" opacity=".16" d="M292 0 L196 236 H366Z"/>'
              '<rect class="i-c" opacity=".12" x="246" y="56" width="124" height="80" rx="7"/><rect class="i-a" opacity=".7" x="262" y="76" width="60" height="9" rx="4.5"/>'
              '<rect class="i-c" opacity=".3" x="262" y="94" width="88" height="6" rx="3"/><rect class="i-c" opacity=".3" x="262" y="108" width="70" height="6" rx="3"/>'
              '<rect class="i-2" opacity=".55" y="232" width="400" height="68"/><circle class="i-c" cx="170" cy="150" r="15"/><path class="i-c" d="M148 232c0-40 9-58 22-58s22 18 22 58z"/>'
              '<g class="i-2"><circle cx="30" cy="278" r="24"/><circle cx="96" cy="286" r="26"/><circle cx="166" cy="280" r="24"/><circle cx="238" cy="288" r="27"/><circle cx="310" cy="280" r="24"/><circle cx="376" cy="288" r="26"/></g>'),
    "shop": ('<rect class="i-1" x="-300" width="1000" height="300"/><rect class="i-2" x="-300" y="262" width="1000" height="38"/><rect class="i-c" x="66" y="64" width="268" height="198"/>'
             '<rect class="i-d" x="116" y="36" width="168" height="38" rx="7"/><rect class="i-c" opacity=".85" x="140" y="50" width="120" height="10" rx="5"/>'
             '<path class="i-a" d="M54 96h292l-16 38H70z"/><g class="i-c" opacity=".45"><path d="M96 96h36l-6 38H88z"/><path d="M170 96h36l-2 38h-36z"/><path d="M244 96h36l6 38h-36z"/></g>'
             '<rect class="i-b" x="178" y="162" width="48" height="100" rx="4"/><circle class="i-c" cx="216" cy="214" r="4"/>'
             '<rect class="i-2" opacity=".55" x="88" y="152" width="72" height="72" rx="5"/><rect class="i-2" opacity=".55" x="244" y="152" width="72" height="72" rx="5"/>'
             '<circle class="i-b" cx="52" cy="242" r="20"/><rect class="i-d" x="40" y="250" width="24" height="18" rx="4"/><circle class="i-b" cx="350" cy="242" r="20"/><rect class="i-d" x="338" y="250" width="24" height="18" rx="4"/>'),
    "table": ('<rect class="i-2" width="400" height="300"/><rect class="i-c" opacity=".95" x="36" y="56" width="328" height="188" rx="94"/>'
              '<g class="i-1"><circle cx="110" cy="120" r="30"/><circle cx="290" cy="120" r="30"/><circle cx="110" cy="190" r="26"/><circle cx="290" cy="186" r="28"/></g>'
              '<g class="i-c"><circle cx="110" cy="120" r="19"/><circle cx="290" cy="120" r="19"/><circle cx="290" cy="186" r="17"/></g>'
              '<circle class="i-a" cx="200" cy="100" r="15"/><circle class="i-b" cx="176" cy="196" r="13"/><circle class="i-a" cx="236" cy="204" r="11"/>'
              '<rect class="i-d" x="170" y="126" width="62" height="44" rx="5" transform="rotate(-8 200 148)"/><rect class="i-c" opacity=".7" x="180" y="138" width="34" height="5" rx="2.5" transform="rotate(-8 200 148)"/>'),
    "map": ('<rect class="i-g" width="400" height="300"/><path class="i-2" opacity=".45" d="M0 0h130v96H0zM160 0h110v70H160zM300 0h100v130H300zM0 130h96v170H0zM126 110h140v96H126zM300 166h100v134H300z"/>'
            '<path class="i-b" opacity=".5" d="M126 232h140v68H126z"/><g fill="none" stroke="var(--card)" stroke-width="14"><path d="M0 112h400M112 0v300M284 0v300M112 218h172"/></g>'
            '<path class="i-a" d="M200 84c-26 0-46 20-46 46 0 34 46 80 46 80s46-46 46-80c0-26-20-46-46-46z"/><circle class="i-c" cx="200" cy="130" r="17"/>'),
    "mic": ('<rect class="i-d" width="400" height="300"/><circle class="i-a" opacity=".2" cx="200" cy="140" r="130"/><rect class="i-a" x="168" y="56" width="64" height="122" rx="32"/>'
            '<g fill="none" stroke="var(--card)" stroke-width="7" stroke-linecap="round"><path d="M142 138c0 34 26 58 58 58s58-24 58-58M200 196v44M166 244h68"/><path opacity=".5" d="M104 100c-12 26-12 54 0 80M296 100c12 26 12 54 0 80"/></g>'),
    "arch": ('<rect class="i-1" width="400" height="300"/><path class="i-2" opacity=".7" d="M60 300V170a90 90 0 0 1 180 0v130z"/><path class="i-a" opacity=".85" d="M200 300V200a70 70 0 0 1 140 0v100z"/>'
             '<circle class="i-c" opacity=".9" cx="310" cy="78" r="34"/><circle class="i-b" opacity=".6" cx="96" cy="76" r="20"/>'),
}
SCENES["docs"] = '<rect class="i-1" width="400" height="300"/>' + _page(52, 62, -11, "i-a") + _page(196, 46, 9, "i-b") + _page(124, 52, -1, "i-d")

KEYS = [("map", "map"), ("mic", "microphone|podcast|episode|recorder"), ("stage", "stage|keynote|reel|audience|session|slide|talk|workshop"),
        ("shop", "shopfront|street|exterior|reception|front desk|clinic|practice|treatment|office"), ("hills", "venue|retreat|outdoor|garden|verandah|golden|fire pit|off-duty"),
        ("table", "table|meet-up|workbench|dinner|coffee"), ("docs", "template|pages|cover|workbook|proposal|notes|pack|tiles|flat lay|kit|portal|profile|notebook|thumbnail|image brief"),
        ("desk", "desk|laptop|lesson|working|course")]


def kind_of(label):
    import re
    low = label.lower()
    return next((k for k, pat in KEYS if re.search(pat, low)), "arch")


def scene(label, ar="4/3"):
    """A small flat illustration chosen from the words of the photo brief. A tall subject is shown whole in a wide frame, not cropped."""
    kind = kind_of(label)
    w, hgt = (float(x) for x in ar.split("/"))
    width = max(400, round(300 * w / hgt)) if kind == "shop" else 400
    return (f'<svg viewBox="{(400 - width) // 2} 0 {width} 300" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">{SCENES[kind]}</svg>')


def bars(rows, unit=""):
    """A small before-and-after bar chart: rows are (label, before, after)."""
    top = max(max(b, a) for _, b, a in rows) or 1
    out, y = "", 8
    for label, b, a in rows:
        wb, wa = 250 * b / top, 250 * a / top
        out += (f'<text x="0" y="{y + 9}" class="ct">{label}</text><rect class="i-l" x="0" y="{y + 16}" width="{wb:.0f}" height="12" rx="6"/>'
                f'<text x="{wb + 8:.0f}" y="{y + 27}" class="cv">{b:g}{unit}</text><rect class="i-a" x="0" y="{y + 34}" width="{wa:.0f}" height="12" rx="6"/>'
                f'<text x="{wa + 8:.0f}" y="{y + 45}" class="cv cb">{a:g}{unit}</text>')
        y += 68
    return f'<svg viewBox="0 0 320 {y}" role="img" aria-label="Before and after chart">{out}</svg>'


ICONS = {
    "check": "M5 13l4 4L19 7", "clock": "M12 7v5l3 2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z", "cal": "M4 9h16M8 3v4M16 3v4M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z",
    "chat": "M4 5h16v11H9l-5 4z", "chart": "M4 20V10M10 20V4M16 20v-7M22 20H2", "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z M9 12l2 2 4-4",
    "spark": "M12 3l2.2 6.8L21 12l-6.8 2.2L12 21l-2.2-6.8L3 12l6.8-2.2z", "users": "M16 19v-1a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4v1M9.5 10a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7zM21 19v-1a4 4 0 0 0-3-3.8M15.5 3.2a3.5 3.5 0 0 1 0 6.6",
    "doc": "M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6", "play": "M8 5v14l11-7z", "pin": "M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z",
    "mail": "M3 6h18v12H3zM3 7l9 6 9-6", "phone": "M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z", "heart": "M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z",
    "target": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM12 12h.01", "lock": "M6 11h12v9H6zM9 11V8a3 3 0 0 1 6 0v3", "arrow": "M5 12h14M13 6l6 6-6 6", "menu": "M4 7h16M4 12h16M4 17h16",
}
ICON_KEYS = [("clock", "week|hour|minute|time|day|month|friday|monday"), ("cal", "call|session|workshop|book|date|schedule"), ("chart", "price|pricing|profit|margin|number|fee|rate|result|maths"),
             ("users", "team|people|group|member|client|co-working|cohort"), ("doc", "page|template|script|plan|guide|notes|list|proposal|write"), ("chat", "question|answer|conversation|feedback|ask|talk"),
             ("shield", "guarantee|trust|safe|included|never|refund"), ("target", "focus|offer|outcome|goal|problem"), ("heart", "believe|care|experience|confidence")]


def icon(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{ICONS[name]}"/></svg>'


def icon_for(text, i=0):
    import re
    low = text.lower()
    return next((k for k, pat in ICON_KEYS if re.search(pat, low)), ["spark", "target", "heart", "chat"][i % 4])
