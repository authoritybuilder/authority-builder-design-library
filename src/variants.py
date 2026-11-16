"""What makes each of the 28 sites its own design.

The 10 style directions in src/themes.py set the family. This file gives every site inside a family its own palette, type pairing,
section headers, card treatment, dividers, background texture, reveal style and picture band, so no 2 sites look alike.

A site's entry can set:
  name    what this variation is called, shown on the notes page
  v       colour and type tokens that replace the theme's
  fonts   the Google Fonts request, when the type pairing changes
  pair    the pairing in words
  traits  design traits from TRAITS below
  motion  how sections arrive: rise, slide, clip or fade. All 4 are short and quiet
  band    the picture band: wide, frame, mosaic or strip, with its line of copy
  css     anything else
Every palette is checked against WCAG AA when the build runs.
"""
import copy

from themes import THEMES, gf

TRAITS = {
    # --- section headers ---
    "sh-index": "main{counter-reset:sx}.sh{counter-increment:sx}.sh h2::before{content:counter(sx,decimal-leading-zero) \"  /\";display:block;font:600 .8rem/1 var(--fa);letter-spacing:.22em;"
                "text-transform:none;color:var(--accent-t);margin-bottom:1.1rem}",
    "sh-center": ".sh{margin-inline:auto;text-align:center}.sh .lead{margin-inline:auto}.sh .eyebrow::before{display:none}",
    "sh-split": "@media(min-width:900px){.sh:not(.center):has(.lead){max-width:none;display:grid;grid-template-columns:1.15fr .85fr;column-gap:clamp(28px,5vw,80px);align-items:end}"
                ".sh:not(.center):has(.lead) .eyebrow{grid-column:1/-1}.sh:not(.center):has(.lead) .lead{margin:0 0 .35em}}",
    "sh-bar": ".sh h2{padding-bottom:.55em;background:linear-gradient(var(--accent),var(--accent)) 0 100%/76px 4px no-repeat}.sh.center h2{background-position:50% 100%}",
    "sh-big": ".sh{max-width:980px}.sh h2{font-size:clamp(2.05rem,calc(4.5vw*var(--hs)),calc(3.7rem*var(--hs)))}",
    # --- cards ---
    "card-glass": ".card{background:color-mix(in srgb,var(--card) 58%,transparent);-webkit-backdrop-filter:blur(16px) saturate(1.3);backdrop-filter:blur(16px) saturate(1.3);"
                  "border:1px solid color-mix(in srgb,var(--ink) 14%,transparent);box-shadow:0 30px 60px -38px color-mix(in srgb,var(--ink) 60%,transparent)}.formcard,.bleed .card{background:var(--card)}",
    "card-outline": ".card:not(.formcard):not(.float):not(.mk){background:transparent;box-shadow:none;border:max(1px,var(--bw)) solid color-mix(in srgb,var(--ink) 28%,transparent)}"
                    ".cards .card:hover,.door:hover{background:var(--card)}",
    "card-lift": ".card:not(.float){border-color:transparent;box-shadow:0 2px 4px rgba(0,0,0,.04),0 44px 70px -44px color-mix(in srgb,var(--ink) 55%,transparent);transition:translate .3s,box-shadow .3s}"
                 ".cards .card:hover,.door:hover,.qt figure.card:hover{box-shadow:0 2px 4px rgba(0,0,0,.05),0 56px 80px -40px color-mix(in srgb,var(--accent) 60%,transparent)}",
    "card-corner": ".cards .card,.door{position:relative;overflow:hidden}.cards .card::before,.door::before{content:\"\";position:absolute;right:0;top:0;width:38px;height:38px;"
                   "background:linear-gradient(225deg,var(--accent) 50%,transparent 50%);transition:width .3s,height .3s}.cards .card:hover::before,.door:hover::before{width:56px;height:56px}",
    "card-topbar": ".card:not(.float):not(.mk){border-top:4px solid var(--accent)}.qt figure.card{border-top-width:4px}",
    # --- dividers between sections ---
    "div-slant": ".sec.alt{clip-path:polygon(0 clamp(18px,3.2vw,48px),100% 0,100% calc(100% - clamp(18px,3.2vw,48px)),0 100%);padding-block:clamp(88px,11vw,156px)}",
    "div-arc": ".sec.alt{border-radius:50% 50% 0 0/clamp(26px,4.5vw,68px) clamp(26px,4.5vw,68px) 0 0}",
    "div-rule": "main>.sec+.sec:not(.alt):not(.dark):not(.bleed):not(.logos){border-top:max(1px,var(--bw)) solid var(--line)}",
    "div-soft": ".sec.alt{border-radius:clamp(24px,4vw,56px);margin-inline:clamp(8px,2vw,28px)}",
    # --- background texture ---
    "bg-grain": "@media(min-width:900px){body::after{content:\"\";position:fixed;inset:0;z-index:45;pointer-events:none;background-image:var(--grain);opacity:.07;mix-blend-mode:overlay}}",
    "bg-dots": "body{background-image:radial-gradient(color-mix(in srgb,var(--ink) 15%,transparent) 1px,transparent 1.6px);background-size:22px 22px}",
    "bg-grid": "body{background-image:linear-gradient(color-mix(in srgb,var(--ink) 6%,transparent) 1px,transparent 1px),linear-gradient(90deg,color-mix(in srgb,var(--ink) 6%,transparent) 1px,transparent 1px);"
               "background-size:64px 64px}",
    "bg-lines": "body{background-image:repeating-linear-gradient(90deg,transparent 0 calc(25% - 1px),color-mix(in srgb,var(--ink) 8%,transparent) calc(25% - 1px) 25%)}",
    # --- numbered methods ---
    "steps-h": "@media(min-width:900px){.stp{grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:clamp(18px,2.6vw,36px)}"
               ".stp li{grid-template-columns:1fr;gap:1rem;border-top:3px solid var(--accent-t);padding-top:1.4rem}.stp li:hover{padding-left:0}}",
    "steps-line": ".stp{position:relative;padding-left:clamp(30px,4.4vw,54px)}.stp::before{content:\"\";position:absolute;left:7px;top:2rem;bottom:2rem;width:2px;"
                  "background:linear-gradient(var(--accent-t),color-mix(in srgb,var(--accent-t) 12%,transparent))}.stp li{position:relative;border-top:0}"
                  ".stp li::after{content:\"\";position:absolute;left:calc(clamp(30px,4.4vw,54px)*-1);top:clamp(30px,3.8vw,46px);width:16px;height:16px;border-radius:50%;background:var(--accent-t);"
                  "box-shadow:0 0 0 5px color-mix(in srgb,var(--accent-t) 22%,transparent)}",
    # --- hero finish ---
    "hero-frame": ".hero.bleed::after{content:\"\";position:absolute;inset:clamp(10px,1.4vw,18px);border:1px solid rgba(255,255,255,.44);border-radius:calc(var(--r) + 6px);pointer-events:none;z-index:-1}"
                  ".hero.t-dark::after{border-color:color-mix(in srgb,var(--ink) 30%,transparent)}",
    "hero-inset": "@media(min-width:761px){.over .hero.bleed{margin-inline:clamp(8px,1.2vw,16px);border-radius:0 0 clamp(24px,3vw,44px) clamp(24px,3vw,44px)}}",
    # --- small signatures ---
    "q-stagger": "@media(min-width:900px){.qt .grid>:nth-child(3n+2){margin-top:30px}.qt .grid>:nth-child(3n){margin-top:60px}}",
    "faq-cards": ".faq details,.faq details:last-of-type{border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),16px);margin-top:.7rem;padding-inline:1rem;background:var(--card)}",
    "stat-cards": ".st-g>div{border-left:0;padding:1.5rem;background:var(--card);border-radius:var(--r);border:max(1px,var(--bw)) solid var(--line);box-shadow:var(--shadow)}",
    "em-plain": "h1 em,h2 em,.bd-h em{font-style:normal}",
}

# Restraint, applied to every site before its own variation. These undo the habits that make a page look machine-made:
# a highlighted half on every heading, icons in tinted tiles, coloured glows under buttons and cards, things that bob.
REFINE = (
    ".sh h2 em,.sp-g h2 em,.gu h2 em{color:inherit}"                                                    # only the first and last headline carry the accent; section headings stay in ink
    ".chip-ic{display:block;width:auto;height:auto;background:none;border-radius:0;margin-bottom:1.2rem;padding-bottom:1.1rem;border-bottom:1px solid var(--line)}"
    ".chip-ic .ic{width:28px;height:28px;stroke-width:1.5}"
    ".float,.float.f2{animation:none}"
    ".tier.hot{box-shadow:0 30px 60px -38px color-mix(in srgb,var(--ink) 55%,transparent)}"
    "::selection{background:var(--accent);color:var(--accent-ink)}"
    "body{font-feature-settings:'kern','liga','calt';hanging-punctuation:first}"
    ".stats b,.st-g b,.hstats b,.tier .pc,.mt td{font-variant-numeric:lining-nums tabular-nums}"
    ".sh{margin-bottom:clamp(36px,5vw,64px)}.sh .eyebrow{margin-bottom:1.15rem}"
    ".card p,.stp p,.fd-l p{max-width:62ch}"
    "a:not(.btn):not(.logo):not(.door):not(.card){text-decoration-thickness:1px;text-underline-offset:.22em}"
    "\n")

SERIF = "Georgia,serif"
SANS = "system-ui,sans-serif"

V = {
    # ---------- Warm Editorial ----------
    1: dict(name="Terracotta Letter", traits=["sh-index", "card-lift", "div-arc", "bg-grain", "steps-line"], motion="rise",
            band=("wide", "Leading is a different job, *and it can be learned.*")),
    11: dict(name="Fig And Plaster", pair="Gloock + Figtree", fonts=gf("Gloock", "Figtree:wght@400;500;600;700"),
             v={"bg": "#F6F1F0", "bg2": "#EBDFDD", "ink": "#2A1A22", "ink2": "#5E4A54", "line": "#D9C7C8", "card": "#FFFBFA", "accent": "#7A2E4F", "accent-ink": "#FFF5F3", "accent-t": "#7A2E4F",
                "accent2": "#3F6A5E", "dark": "#2A1A22", "dark-ink": "#F6E9E6", "dark-accent": "#F0A9B8", "ph1": "#EBC9C4", "ph2": "#C58B93",
                "fd": f"'Gloock',{SERIF}", "fb": f"'Figtree',{SANS}", "fa": f"'Figtree',{SANS}", "hls": "-0.012em", "hs": ".98", "r": "18px", "phr": "18px"},
             traits=["sh-split", "card-topbar", "div-rule", "bg-dots", "steps-h", "hero-frame", "faq-cards", "em-plain"], motion="clip",
             band=("mosaic", "One scope and one price, *agreed before we start.*"),
             css=":root{--atmo:radial-gradient(52% 60% at 90% 6%,#EBC9C4 0,transparent 70%)}"),
    22: dict(name="Ink And Olive", pair="Newsreader + Hanken Grotesk",
             fonts=gf("Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700", "Hanken+Grotesk:wght@400;500;600;700"),
             v={"bg": "#F3F1E7", "bg2": "#E4E2D0", "ink": "#1C2118", "ink2": "#4F5646", "line": "#CFCDB6", "card": "#FDFCF6", "accent": "#4A5D23", "accent-ink": "#FBFAEF", "accent-t": "#44561F",
                "accent2": "#9A5B2B", "dark": "#1C2118", "dark-ink": "#EEECDD", "dark-accent": "#C9D58A", "ph1": "#DDD9B4", "ph2": "#A9A46F",
                "fd": f"'Newsreader',{SERIF}", "fb": f"'Hanken Grotesk',{SANS}", "fa": f"'Hanken Grotesk',{SANS}", "hw": "500", "hls": "-0.025em", "hs": "1", "r": "2px", "rb": "2px", "phr": "2px"},
             traits=["sh-center", "card-outline", "div-slant", "bg-lines", "q-stagger", "stat-cards"], motion="fade",
             band=("frame", "Results are individual. *The words are theirs.*"),
             css=":root{--atmo:none}"),
    # ---------- Corporate Calm ----------
    2: dict(name="Slate And Teal", traits=["sh-bar", "card-outline", "div-rule", "steps-h"], motion="slide",
            band=("mosaic", "Price the value, *not the hours.*")),
    13: dict(name="Graphite And Cobalt", pair="Schibsted Grotesk + IBM Plex Sans",
             fonts=gf("Schibsted+Grotesk:wght@400;500;600;700;800", "IBM+Plex+Sans:wght@400;500;600", "IBM+Plex+Mono:wght@400;500"),
             v={"bg": "#FFFFFF", "bg2": "#F2F4F8", "ink": "#171A21", "ink2": "#4D5361", "line": "#DCE0E8", "card": "#FFFFFF", "accent": "#2447D6", "accent-ink": "#FFFFFF", "accent-t": "#1F3FC4",
                "accent2": "#171A21", "dark": "#131722", "dark-ink": "#EEF1F7", "dark-accent": "#9DB4FF", "ph1": "#D6DDF0", "ph2": "#9FADD0",
                "fd": f"'Schibsted Grotesk',{SANS}", "hw": "700", "hls": "-0.035em", "hlh": "1.02", "hs": ".94", "r": "16px", "rb": "999px", "phr": "16px"},
             traits=["sh-index", "div-slant", "steps-line", "hero-inset", "stat-cards", "em-plain"], motion="fade",
             band=("wide", "Training that shows up *in Monday's work.*"),
             css=":root{--atmo:radial-gradient(50% 60% at 88% 0,#D6DDF0 0,transparent 70%)}.hero::before{-webkit-mask-image:none;mask-image:none}"),
    28: dict(name="Stone And Forest", pair="Lora + Albert Sans",
             fonts=gf("Lora:ital,wght@0,400..700;1,400..700", "Albert+Sans:wght@400;500;600;700", "IBM+Plex+Mono:wght@400;500"),
             v={"bg": "#FBFAF7", "bg2": "#F0EEE7", "ink": "#1E2A24", "ink2": "#50605A", "line": "#DDD9CE", "card": "#FFFFFF", "accent": "#1F5C45", "accent-ink": "#FFFFFF", "accent-t": "#1F5C45",
                "accent2": "#1E2A24", "dark": "#1E2A24", "dark-ink": "#EEF2EC", "dark-accent": "#9AD8B8", "ph1": "#D9E2D6", "ph2": "#A3B5A6",
                "fd": f"'Lora',{SERIF}", "fb": f"'Albert Sans',{SANS}", "hw": "500", "hs": ".96", "r": "22px", "rb": "999px", "phr": "22px"},
             traits=["sh-center", "card-lift", "div-arc", "bg-dots", "hero-frame", "faq-cards"], motion="rise", band=None,
             css=":root{--atmo:none}"),
    # ---------- Bento Grid ----------
    3: dict(name="Cobalt, Lime And Lilac", traits=["sh-big", "div-soft"], motion="rise",
            band=("strip", "One calm system, *every Sunday.*")),
    16: dict(name="Tangerine Tiles", pair="Sora + Instrument Sans", fonts=gf("Sora:wght@400;600;700;800", "Instrument+Sans:wght@400;500;600;700"),
             v={"bg": "#F1EEE9", "bg2": "#E6E1D9", "ink": "#1A1613", "ink2": "#5A534C", "line": "#D9D2C7", "card": "#FFFFFF", "accent": "#C73E08", "accent-ink": "#FFFFFF", "accent-t": "#B33606",
                "accent2": "#FFD166", "dark": "#1A1613", "dark-ink": "#F6F2EC", "dark-accent": "#FFD166", "ph1": "#FFD9B8", "ph2": "#F2A679",
                "fd": f"'Sora',{SANS}", "hls": "-0.045em", "hs": ".9", "r": "14px", "phr": "14px"},
             traits=["sh-center", "div-arc", "bg-dots", "hero-inset", "faq-cards"], motion="rise",
             band=("frame", "See where you stand *before you spend a cent.*"),
             css=":root{--t1:#FFD166;--t2:#BFE3D0;--t3:#FFD3C4;--atmo:radial-gradient(38% 46% at 10% 0,#FFD9B8 0,transparent 70%),radial-gradient(34% 40% at 94% 14%,#FFD166 0,transparent 70%)}"),
    25: dict(name="Mint Ledger", pair="Familjen Grotesk + Instrument Sans", fonts=gf("Familjen+Grotesk:wght@400;500;600;700", "Instrument+Sans:wght@400;500;600;700"),
             v={"bg": "#EEF2EF", "bg2": "#E0E7E2", "ink": "#10201A", "ink2": "#4C5C55", "line": "#CFD9D3", "card": "#FFFFFF", "accent": "#0B6B4F", "accent-ink": "#FFFFFF", "accent-t": "#0A6349",
                "accent2": "#F4C95D", "dark": "#10201A", "dark-ink": "#EFF5F1", "dark-accent": "#F4C95D", "ph1": "#BFE5D2", "ph2": "#7CC3A3",
                "fd": f"'Familjen Grotesk',{SANS}", "hls": "-0.03em", "hs": "1.04", "r": "6px", "rb": "6px", "phr": "6px"},
             traits=["sh-split", "card-topbar", "div-rule", "bg-grid"], motion="slide",
             band=("mosaic", "One real page taken apart, *in 5 minutes.*"),
             css=":root{--t1:#F4C95D;--t2:#BFE5D2;--t3:#D7D3F5;--atmo:radial-gradient(40% 46% at 8% 0,#BFE5D2 0,transparent 70%),radial-gradient(34% 40% at 94% 10%,#F4C95D 0,transparent 70%)}"),
    # ---------- Bright Playful ----------
    4: dict(name="Butter, Coral And Navy", traits=["sh-big", "card-corner", "div-slant"], motion="rise",
            band=("strip", "Your books done *and your evenings back.*")),
    12: dict(name="Bubblegum And Violet", pair="Fredoka + Plus Jakarta Sans", fonts=gf("Fredoka:wght@400;500;600;700", "Plus+Jakarta+Sans:wght@400;500;600;700"),
             v={"bg": "#FFF1F5", "bg2": "#FFD6E4", "ink": "#2A1038", "ink2": "#5A4468", "line": "#2A1038", "card": "#FFFFFF", "accent": "#7B2FF7", "accent-ink": "#FFFFFF", "accent-t": "#6A22E0",
                "accent2": "#FF5FA2", "dark": "#2A1038", "dark-ink": "#FFF1F5", "dark-accent": "#FFE066", "ph1": "#FFC2D9", "ph2": "#C9A7FF",
                "fd": f"'Fredoka',{SANS}", "hw": "600", "hls": "-0.02em", "hs": ".9", "r": "32px", "phr": "40px"},
             traits=["sh-center", "div-arc", "bg-dots"], motion="rise",
             band=("mosaic", "Look polished *by this afternoon.*"),
             css=":root{--atmo:radial-gradient(circle at 6% 28%,#FF5FA2 0 22px,transparent 23px),radial-gradient(circle at 95% 76%,#7B2FF7 0 15px,transparent 16px),radial-gradient(circle at 62% 5%,#FFE066 0 12px,transparent 13px)}"
                 ".btn{box-shadow:4px 4px 0 var(--ink)}.btn:not(.ghost){color:#fff}"),
    20: dict(name="Lagoon And Papaya", pair="Outfit + Plus Jakarta Sans", fonts=gf("Outfit:wght@400;500;600;700;800", "Plus+Jakarta+Sans:wght@400;500;600;700"),
             v={"bg": "#EFFBF8", "bg2": "#C9F2E7", "ink": "#0E2A33", "ink2": "#3F5A63", "line": "#0E2A33", "card": "#FFFFFF", "accent": "#FF7A1A", "accent-ink": "#0E2A33", "accent-t": "#A84300",
                "accent2": "#1E88E5", "dark": "#0E2A33", "dark-ink": "#EFFBF8", "dark-accent": "#7CF0D2", "ph1": "#7CF0D2", "ph2": "#FFB37A",
                "fd": f"'Outfit',{SANS}", "hw": "700", "hls": "-0.03em", "hs": ".94", "r": "14px", "phr": "50%"},
             traits=[], motion="rise", band=None,
             css=":root{--atmo:radial-gradient(circle at 8% 22%,#7CF0D2 0 24px,transparent 25px),radial-gradient(circle at 92% 70%,#FF7A1A 0 14px,transparent 15px)}"
                 "h1 em,h2 em{background:linear-gradient(transparent 62%,#7CF0D2 62%)}"),
    # ---------- Magazine ----------
    5: dict(name="Black, White And Red", traits=["sh-index", "card-outline", "div-rule", "hero-frame"], motion="clip",
            band=("wide", "The gap on your CV *is not the story.*")),
    21: dict(name="Salmon Paper And Teal", pair="DM Serif Display + DM Sans", fonts=gf("DM+Serif+Display:ital@0;1", "DM+Sans:wght@400;500;600;700"),
             v={"bg": "#FFF4EA", "bg2": "#F7E4D2", "ink": "#1A1410", "ink2": "#54483F", "line": "#1A1410", "card": "#FFFAF4", "accent": "#0D5C63", "accent-ink": "#FFFFFF", "accent-t": "#0D5C63",
                "accent2": "#1A1410", "dark": "#14201F", "dark-ink": "#F7EBDD", "dark-accent": "#8ED6D0", "ph1": "#F0D3B8", "ph2": "#C9A486",
                "fd": f"'DM Serif Display',{SERIF}", "fb": f"'DM Sans',{SANS}", "fa": f"'DM Sans',{SANS}", "hw": "400", "hls": "-0.015em", "hs": "1"},
             traits=["sh-bar", "bg-lines", "steps-h", "stat-cards"], motion="slide",
             band=("mosaic", "Count first. *Then fix what the numbers show.*"),
             css="h1 em,h2 em{font-weight:400}.hero .ph,.split .ph{box-shadow:14px 14px 0 var(--accent)}"),
    23: dict(name="Blueprint Journal", pair="Spectral + Inter", fonts=gf("Spectral:ital,wght@0,400;0,600;0,700;1,400;1,600", "Inter:wght@400;500;600;700"),
             v={"bg": "#FAFAF7", "bg2": "#EEF0F2", "ink": "#0F1B2D", "ink2": "#4A566A", "line": "#0F1B2D", "card": "#FFFFFF", "accent": "#1B4DD8", "accent-ink": "#FFFFFF", "accent-t": "#1B4DD8",
                "accent2": "#0F1B2D", "dark": "#0F1B2D", "dark-ink": "#F1F3F7", "dark-accent": "#9DB7FF", "ph1": "#D9E0EC", "ph2": "#A9B6CC",
                "fd": f"'Spectral',{SERIF}", "fb": f"'Inter',{SANS}", "fa": f"'Inter',{SANS}", "hw": "600", "hls": "-0.025em", "hs": ".98", "r": "10px", "rb": "10px", "phr": "10px"},
             traits=["sh-split", "bg-grid"], motion="fade", band=None,
             css="h1 em,h2 em{font-weight:400}.hdw{border-bottom:1px solid var(--ink)}"),
    # ---------- Dark Stage ----------
    6: dict(name="Black And Spotlight Gold", traits=["sh-big", "div-slant", "bg-grain"], motion="fade",
            band=("wide", "Attention is the scarcest thing *in the room.*")),
    15: dict(name="Midnight Violet", pair="Oswald + Manrope", fonts=gf("Oswald:wght@400;500;600;700", "Manrope:wght@400;500;600;700;800"),
             v={"bg": "#0E0B1A", "bg2": "#171228", "ink": "#F3F0FA", "ink2": "#B9B2CC", "line": "#2E2747", "card": "#1A1530", "accent": "#B79CFF", "accent-ink": "#0E0B1A", "accent-t": "#B79CFF",
                "accent2": "#FF6B8B", "dark": "#F3F0FA", "dark-ink": "#120E22", "dark-accent": "#4B2BB0", "ph1": "#2A2247", "ph2": "#171228",
                "fd": f"'Oswald','Arial Narrow',sans-serif", "hw": "600", "hls": "0", "hlh": "1", "hs": "1.1", "r": "18px", "rb": "999px", "phr": "18px"},
             traits=["sh-center", "faq-cards"], motion="fade",
             band=("frame", "An hour of your time *for a plan you can use.*"),
             css=":root{--atmo:radial-gradient(46% 70% at 78% 0,rgba(183,156,255,.24) 0,transparent 70%),radial-gradient(40% 60% at 6% 12%,rgba(255,107,139,.16),transparent 70%)}"
                 ".hero .ph{box-shadow:0 0 0 1px #2E2747,0 44px 84px -30px rgba(183,156,255,.45)}.ph span{background:#F3F0FA;color:#120E22}"),
    24: dict(name="Deep Sea Radio", pair="Big Shoulders Display + Manrope", fonts=gf("Big+Shoulders+Display:wght@600;700;800;900", "Manrope:wght@400;500;600;700;800"),
             v={"bg": "#071318", "bg2": "#0D1D24", "ink": "#EAF4F2", "ink2": "#A9BFBD", "line": "#21363E", "card": "#10232B", "accent": "#4FE0C0", "accent-ink": "#071318", "accent-t": "#4FE0C0",
                "accent2": "#FF9F5A", "dark": "#EAF4F2", "dark-ink": "#0A161B", "dark-accent": "#0B6B5A", "ph1": "#1D3A40", "ph2": "#0D1D24",
                "fd": f"'Big Shoulders Display','Arial Narrow',sans-serif", "hw": "800", "hls": ".005em", "hlh": ".94", "hs": "1.22", "r": "0px", "rb": "0px", "phr": "0px"},
             traits=["sh-index", "card-outline", "div-rule", "bg-grain"], motion="rise",
             band=("strip", "Stories of people *who changed course.*"),
             css=":root{--atmo:radial-gradient(46% 70% at 78% 0,rgba(79,224,192,.2) 0,transparent 70%),radial-gradient(40% 60% at 6% 12%,rgba(255,159,90,.14),transparent 70%)}"
                 ".hero .ph{box-shadow:0 0 0 1px #21363E,0 44px 84px -30px rgba(79,224,192,.4)}.ph span{background:#EAF4F2;color:#0A161B}"),
    # ---------- Soft Organic ----------
    7: dict(name="Sage, Cream And Clay", traits=["sh-center", "card-lift", "steps-line"], motion="rise",
            band=("frame", "A steady business *is built on purpose.*")),
    14: dict(name="Lavender Dusk", pair="Young Serif + Nunito Sans", fonts=gf("Young+Serif", "Nunito+Sans:wght@400;600;700;800"),
             v={"bg": "#F8F5FA", "bg2": "#E9E2F0", "ink": "#2C2440", "ink2": "#5B5270", "line": "#D5CBE0", "card": "#FFFFFF", "accent": "#5B3F8C", "accent-ink": "#FAF6FF", "accent-t": "#5B3F8C",
                "accent2": "#C96F8F", "dark": "#2C2440", "dark-ink": "#F3EEF8", "dark-accent": "#E3BBD0", "ph1": "#E3CDE8", "ph2": "#B79BCB",
                "fd": f"'Young Serif',{SERIF}", "hw": "400", "hls": "-0.02em", "hs": ".94", "r": "20px", "phr": "50% 50% 20px 20px"},
             traits=["sh-split", "card-lift", "bg-dots", "em-plain"], motion="fade",
             band=("mosaic", "Start with one clear page. *It costs nothing.*"),
             css="h1 em,h2 em{color:#9A3F6B}:root{--atmo:radial-gradient(44% 56% at 96% 4%,#E9E2F0 0,transparent 70%),radial-gradient(36% 44% at 0 94%,#F3D9E4,transparent 70%)}"),
    27: dict(name="Clay And River", pair="Marcellus + Nunito Sans", fonts=gf("Marcellus", "Nunito+Sans:wght@400;600;700;800"),
             v={"bg": "#F7F3EC", "bg2": "#EADFD0", "ink": "#33261E", "ink2": "#655447", "line": "#D9CBB8", "card": "#FFFDF9", "accent": "#9A4A2A", "accent-ink": "#FFF6EE", "accent-t": "#8F4324",
                "accent2": "#3E6B73", "dark": "#2B3A3D", "dark-ink": "#F2EDE3", "dark-accent": "#F0C19F", "ph1": "#E8CDB1", "ph2": "#C9906C",
                "fd": f"'Marcellus',{SERIF}", "hw": "400", "hls": "-0.01em", "hs": "1", "r": "4px", "rb": "4px", "phr": "200px 200px 4px 4px"},
             traits=["sh-index", "card-topbar", "bg-grain", "steps-h", "hero-frame", "em-plain"], motion="clip",
             band=("wide", "3 days away *for one clear strategy.*"),
             css="h1 em,h2 em{color:#3E6B73}.sec.alt{border-radius:0;margin-inline:0}:root{--atmo:radial-gradient(44% 56% at 96% 4%,#EADFD0 0,transparent 70%)}"),
    # ---------- Bold Type-Led ----------
    8: dict(name="Paper, Black And Orange", traits=["sh-big", "card-corner", "div-rule"], motion="slide",
            band=("strip", "A better proposal *starts with a better structure.*")),
    19: dict(name="Acid Court", pair="Anton + Inter", fonts=gf("Anton", "Inter:wght@400;500;600;700"),
             v={"bg": "#F4F4EF", "bg2": "#E6E6DD", "ink": "#0B0B0B", "ink2": "#45453F", "line": "#0B0B0B", "card": "#FFFFFF", "accent": "#C6F432", "accent-ink": "#0B0B0B", "accent-t": "#3C5A00",
                "accent2": "#0B0B0B", "dark": "#0B0B0B", "dark-ink": "#F4F4EF", "dark-accent": "#C6F432", "ph1": "#D9DACB", "ph2": "#A8AA93",
                "fd": f"'Anton','Arial Narrow',sans-serif", "hw": "400", "hls": ".004em", "hlh": "1", "hs": "1.08", "r": "999px", "rb": "999px", "phr": "28px"},
             traits=["sh-index", "div-slant", "bg-grid"], motion="rise",
             band=("wide", "A short call *and a straight answer.*"),
             css="h1,h2,h3,.logo{font-stretch:100%}.card{border-radius:28px}.formcard{border-radius:28px}h1 em,h2 em{color:var(--ink);background:linear-gradient(transparent 58%,var(--accent) 58%)}"
                 ".dark h1 em,.dark h2 em{background:none}"),
    # ---------- Retro Scrapbook ----------
    9: dict(name="Kraft, Tomato And Teal", traits=["sh-center", "bg-grain"], motion="rise",
            band=("strip", "Making is solitary. *Selling does not have to be.*")),
    17: dict(name="Riso Sunrise", pair="Rozha One + Space Grotesk (+ Caveat notes)", fonts=gf("Rozha+One", "Space+Grotesk:wght@400;500;600;700", "Caveat:wght@500;700"),
             v={"bg": "#F6EBDD", "bg2": "#F0D9C0", "ink": "#2A1E3F", "ink2": "#564A6B", "line": "#2A1E3F", "card": "#FFF8EE", "accent": "#C92A60", "accent-ink": "#FFF6E9", "accent-t": "#B32456",
                "accent2": "#2B5FD9", "dark": "#2A1E3F", "dark-ink": "#F9EEDD", "dark-accent": "#FFC857", "ph1": "#FFC857", "ph2": "#F28B66",
                "fd": f"'Rozha One',{SERIF}", "hls": "-0.01em", "hs": ".96", "r": "22px", "rb": "999px", "phr": "22px", "shadow": "5px 5px 0 #2B5FD9"},
             traits=["sh-big", "div-slant", "bg-dots"], motion="rise",
             band=("mosaic", "20 minutes a day *for 5 days.*"),
             css=".card{border-style:solid}.btn{box-shadow:3px 3px 0 #2B5FD9}.cards .card::after,.qt figure.card::after{background:rgba(43,95,217,.75)}"),
    # ---------- Quiet Luxury ----------
    10: dict(name="Ivory, Espresso And Bronze", traits=["sh-center", "div-rule", "hero-frame"], motion="clip",
             band=("wide", "The right room *changes the next decision.*")),
    18: dict(name="Noir And Champagne", pair="Prata + Jost", fonts=gf("Prata", "Jost:wght@300;400;500;600"),
             v={"bg": "#14110F", "bg2": "#1C1815", "ink": "#EFE7DA", "ink2": "#B9AD9B", "line": "#3A322A", "card": "#1C1815", "accent": "#D9B97C", "accent-ink": "#14110F", "accent-t": "#D9B97C",
                "accent2": "#D9B97C", "dark": "#EFE7DA", "dark-ink": "#1A1512", "dark-accent": "#6E4E1C", "ph1": "#3A3026", "ph2": "#1F1A15",
                "fd": f"'Prata',{SERIF}", "hw": "400", "hls": "-0.01em", "hs": ".92"},
             traits=["sh-index", "bg-grain", "em-plain"], motion="fade",
             band=("frame", "A small intake, *worth the wait.*"),
             css=":root{--atmo:linear-gradient(180deg,#1C1815,transparent 62%)}h1 em,h2 em{color:var(--accent-t)}.ph span{background:#EFE7DA;color:#1A1512}"),
    26: dict(name="Sage Estate", pair="Libre Caslon Display + Jost", fonts=gf("Libre+Caslon+Display", "Jost:wght@300;400;500;600"),
             v={"bg": "#F1F2EC", "bg2": "#E3E6DA", "ink": "#1F2A22", "ink2": "#4E5948", "line": "#C5CBB8", "card": "#F8F9F4", "accent": "#1F2A22", "accent-ink": "#F1F2EC", "accent-t": "#4A5A26",
                "accent2": "#8C7A3F", "dark": "#1B241D", "dark-ink": "#EDF0E4", "dark-accent": "#C9D29A", "ph1": "#D5DBC3", "ph2": "#9DAA80",
                "fd": f"'Libre Caslon Display',{SERIF}", "hw": "400", "hls": "-0.015em", "hs": "1.06", "r": "999px", "rb": "999px", "phr": "999px 999px 0 0"},
             traits=["sh-split", "bg-lines", "hero-inset", "em-plain"], motion="rise",
             band=("mosaic", "A calmer way *to fill a practice.*"),
             css=":root{--atmo:linear-gradient(180deg,#F8F9F4,transparent 62%)}.card,.formcard{border-radius:26px}.float{border-radius:18px}h1 em,h2 em{color:var(--accent-t)}"),
}


def theme(P):
    """The theme for 1 site: its family's tokens with this site's own on top."""
    if "_theme" in P:
        return P["_theme"]
    base = THEMES[P["theme"]]
    x = V.get(P["n"], {})
    t = copy.deepcopy(base)
    t["v"].update(x.get("v", {}))
    for k in ("fonts", "pair"):
        if x.get(k):
            t[k] = x[k]
    t["variant"] = x.get("name", base["label"])
    t["vcss"] = REFINE + "/* this site's own variation: " + t["variant"] + " */\n" + "".join(TRAITS[k] for k in x.get("traits", [])) + x.get("css", "")
    t["motion"] = x.get("motion", "rise")
    t["flags"] = x.get("flags", [])
    t["traits"] = x.get("traits", [])
    P["_theme"] = t
    return t


def html_attrs(P):
    t = theme(P)
    return f' data-m="{t["motion"]}"'


BLEED = ("hero_split", "hero_center", "hero_form", "hero_stage", "cta", "band")


def enrich(P):
    """Add the picture band: a painted break in the middle of the page that repeats the main button, placed after the proof when there is some."""
    b = V.get(P["n"], {}).get("band")
    secs = P["sections"]
    if not b or len(secs) < 5:
        return
    names = [n for n, _ in secs]
    at = names.index("quotes") + 1 if "quotes" in names[1:-2] else len(secs) // 2
    at = max(2, min(at, len(secs) - 2))
    while at < len(secs) - 1 and (names[at - 1] in BLEED or names[at] in BLEED):
        at += 1
    if names[at - 1] in BLEED or names[at] in BLEED:
        return
    hero = secs[0][1]
    cta = P.get("cta") or hero.get("cta")   # a page with no menu button repeats its hero's action, or points back to its form
    if not cta and hero.get("form"):
        cta = (hero["form"].get("button", "Get Started"), "#" + hero.get("fid", "signup"))
    secs.insert(at, ("band", dict(_="Picture band: a painted pause in the middle of the page that repeats the main button, straight after the proof",
                                  kind=b[0], h=b[1], cta=cta, eyebrow=P["brand"]["name"])))


WORDS = {
    "sh-index": "numbered section headers", "sh-center": "centred section headers", "sh-split": "headers split into 2 columns", "sh-bar": "headers underlined in the accent",
    "sh-big": "oversized section headers","card-outline": "outlined cards", "card-lift": "cards lifted on soft shadows",
    "card-corner": "cards with a folded accent corner", "card-topbar": "cards with an accent top edge", "div-slant": "slanted section breaks", "div-arc": "arched section breaks",
    "div-rule": "hairline section breaks", "div-soft": "rounded section panels", "bg-grain": "a paper grain", "bg-dots": "a dotted ground", "bg-grid": "a drafting grid",
    "bg-lines": "column guide lines","steps-h": "the method laid out side by side", "steps-line": "the method on a timeline",
    "hero-frame": "a hairline frame inside the hero", "hero-inset": "a hero set in as a rounded panel",
    "q-stagger": "testimonials on a stagger", "faq-cards": "questions as cards", "stat-cards": "numbers as cards",
}
MOVES = {"rise": "rise a short way into place", "slide": "slide in a short way from the side", "clip": "wipe open from the top", "fade": "fade in"}
BANDS = {"wide": "a full-width painted band", "frame": "a painted band set in a rounded frame", "mosaic": "3 crops of the painting beside the line", "strip": "a row of crops from the painting"}


def describe(P):
    """This site's own variation, in a sentence, for its notes page."""
    t = theme(P)
    x = V.get(P["n"], {})
    bits = [WORDS[k] for k in t["traits"] if k in WORDS]
    band = f' The picture band is {BANDS[x["band"][0]]}.' if x.get("band") else ""
    return f'{t["variant"]}. Sections {MOVES[t["motion"]]} as they scroll in. It uses {", ".join(bits)}.{band}'
