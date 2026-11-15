"""Ten style directions. Each theme is a set of design tokens plus a few signature rules.
Change a token here and every sample that uses the theme updates on the next build."""


def gf(*fams):
    return "https://fonts.googleapis.com/css2?" + "&".join("family=" + f for f in fams) + "&display=swap"


THEMES = {
    "warm_editorial": dict(
        label="Warm Editorial",
        mood="Paper tones, a bookish serif, italic emphasis. Feels like a considered letter.",
        pair="Instrument Serif + Inter",
        fonts=gf("Instrument+Serif:ital@0;1", "Inter:wght@400;500;600;700"),
        v={"bg": "#F7F2E8", "bg2": "#EEE4D3", "ink": "#221C16", "ink2": "#5B5045", "line": "#D8CCB6", "card": "#FFFDF8",
           "accent": "#A8431F", "accent-ink": "#FFF8EF", "accent-t": "#983A18", "accent2": "#2F5D50",
           "dark": "#241C16", "dark-ink": "#F4EBDD", "dark-accent": "#EBA884", "ph1": "#E9CFAF", "ph2": "#C98C64",
           "fd": "'Instrument Serif',Georgia,serif", "fb": "'Inter',system-ui,sans-serif", "fa": "'Inter',system-ui,sans-serif",
           "r": "6px", "rb": "999px", "hw": "400", "hls": "-0.018em", "hlh": "1.02", "htt": "none", "hs": "1.08", "bw": "1px",
           "shadow": "none", "phr": "999px 999px 6px 6px"},
        css="h1 em,h2 em{font-style:italic;font-weight:400;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}"
            ".eyebrow{letter-spacing:.2em}.card{box-shadow:0 1px 0 var(--line)}",
    ),
    "quiet_luxury": dict(
        label="Quiet Luxury",
        mood="Ivory, espresso and bronze. Thin rules, small capitals, lots of air. Says premium without shouting.",
        pair="Cormorant Garamond + Jost",
        fonts=gf("Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500", "Jost:wght@300;400;500;600"),
        v={"bg": "#F3EEE6", "bg2": "#E9E1D5", "ink": "#26201B", "ink2": "#5F5449", "line": "#CDBFAC", "card": "#FAF7F1",
           "accent": "#26201B", "accent-ink": "#F3EEE6", "accent-t": "#74552A", "accent2": "#8A6A3B",
           "dark": "#1E1915", "dark-ink": "#EDE5D8", "dark-accent": "#CDAA72", "ph1": "#DCCDB6", "ph2": "#A88F6E",
           "fd": "'Cormorant Garamond',Georgia,serif", "fb": "'Jost',system-ui,sans-serif", "fa": "'Jost',system-ui,sans-serif",
           "r": "0px", "rb": "0px", "hw": "500", "hls": "-0.012em", "hlh": "1.02", "htt": "none", "hs": "1.12", "bw": "1px",
           "shadow": "none", "phr": "0px"},
        css="h1 em,h2 em{font-style:italic;font-weight:400}.btn{text-transform:uppercase;letter-spacing:.16em;font-size:.78rem;font-weight:500;padding:1.15em 2.1em}"
            ".eyebrow{letter-spacing:.3em;font-size:.72rem}.card{background:transparent}body{font-weight:300;font-size:1.1rem}"
            ".sh{border-top:1px solid var(--line);padding-top:1.6rem}.logo{letter-spacing:.14em;text-transform:uppercase;font-size:1.05rem}",
    ),
    "bold_type": dict(
        label="Bold Type-Led",
        mood="Huge condensed capitals, hard edges, one loud accent. The headline is the design.",
        pair="Archivo + Inter",
        fonts=gf("Archivo:wdth,wght@62..125,400..900", "Inter:wght@400;500;600;700"),
        v={"bg": "#F2EFE8", "bg2": "#E4DFD3", "ink": "#0D0D0D", "ink2": "#46463F", "line": "#0D0D0D", "card": "#FFFFFF",
           "accent": "#FF4A1C", "accent-ink": "#0D0D0D", "accent-t": "#B92F0A", "accent2": "#0D0D0D",
           "dark": "#0D0D0D", "dark-ink": "#F2EFE8", "dark-accent": "#FF6A3D", "ph1": "#D8D2C4", "ph2": "#A9A292",
           "fd": "'Archivo','Arial Narrow',sans-serif", "fb": "'Inter',system-ui,sans-serif", "fa": "'Inter',system-ui,sans-serif",
           "r": "0px", "rb": "0px", "hw": "800", "hls": "-0.03em", "hlh": ".92", "htt": "uppercase", "hs": "1.14", "bw": "2px",
           "shadow": "6px 6px 0 var(--ink)", "phr": "0px"},
        css="h1,h2,h3,.logo{font-stretch:80%}h1 em,h2 em{font-style:normal;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}"
            ".btn{box-shadow:4px 4px 0 var(--ink);text-transform:uppercase;font-weight:700;letter-spacing:.04em}.dark .btn{box-shadow:4px 4px 0 var(--dark-ink)}"
            ".eyebrow{font-weight:700;letter-spacing:.12em}h3{letter-spacing:-.01em}",
    ),
    "bento": dict(
        label="Bento Grid",
        mood="Rounded tiles on soft grey, one cobalt accent, lime and lilac for colour. Scans in a glance.",
        pair="Bricolage Grotesque + Instrument Sans",
        fonts=gf("Bricolage+Grotesque:opsz,wght@12..96,400..800", "Instrument+Sans:wght@400;500;600;700"),
        v={"bg": "#ECEEF0", "bg2": "#E1E4E8", "ink": "#14161A", "ink2": "#525863", "line": "#D3D7DD", "card": "#FFFFFF",
           "accent": "#1F3FFF", "accent-ink": "#FFFFFF", "accent-t": "#1A36DB", "accent2": "#C8F169",
           "dark": "#14161A", "dark-ink": "#F3F4F6", "dark-accent": "#C8F169", "ph1": "#D9CCFF", "ph2": "#A995F0",
           "fd": "'Bricolage Grotesque',system-ui,sans-serif", "fb": "'Instrument Sans',system-ui,sans-serif", "fa": "'Instrument Sans',system-ui,sans-serif",
           "r": "24px", "rb": "999px", "hw": "700", "hls": "-0.035em", "hlh": "1", "htt": "none", "hs": "1", "bw": "0px",
           "shadow": "0 1px 2px rgba(20,22,26,.05)", "phr": "24px"},
        css=":root{--t1:#C8F169;--t2:#D9CCFF;--t3:#FFD7BF}h1 em,h2 em{font-style:normal;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}"
            ".alt{background:var(--bg)}.eyebrow{font-weight:600;letter-spacing:.06em;text-transform:none;font-size:.9rem}",
    ),
    "soft_organic": dict(
        label="Soft Organic",
        mood="Sage, cream and clay with soft blob shapes. Calm, human and unhurried.",
        pair="Fraunces + Nunito Sans",
        fonts=gf("Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700", "Nunito+Sans:wght@400;600;700;800"),
        v={"bg": "#FAF6EE", "bg2": "#E4EBDD", "ink": "#26352B", "ink2": "#51625A", "line": "#CDD8C5", "card": "#FFFFFF",
           "accent": "#2F5A40", "accent-ink": "#FAF6EE", "accent-t": "#2F5A40", "accent2": "#C9744F",
           "dark": "#26352B", "dark-ink": "#F3EFE4", "dark-accent": "#E9B899", "ph1": "#E9C9AE", "ph2": "#C9906C",
           "fd": "'Fraunces',Georgia,serif", "fb": "'Nunito Sans',system-ui,sans-serif", "fa": "'Nunito Sans',system-ui,sans-serif",
           "r": "28px", "rb": "999px", "hw": "500", "hls": "-0.032em", "hlh": "1.03", "htt": "none", "hs": "1.02", "bw": "1px",
           "shadow": "0 12px 30px rgba(38,53,43,.07)", "phr": "58% 42% 55% 45% / 48% 55% 45% 52%"},
        css="h1 em,h2 em{font-style:italic;color:#A8552F}.dark h1 em,.dark h2 em{color:var(--dark-accent)}.eyebrow{font-weight:800;letter-spacing:.14em}"
            ".card{border-color:transparent}.ph.scene{border-radius:28px}",
    ),
    "bright_playful": dict(
        label="Bright Playful",
        mood="Butter yellow, coral and navy with sticker shadows and chunky outlines. Friendly and fast.",
        pair="Syne + Plus Jakarta Sans",
        fonts=gf("Syne:wght@500;600;700;800", "Plus+Jakarta+Sans:wght@400;500;600;700"),
        v={"bg": "#FFF7E6", "bg2": "#FFE9A8", "ink": "#1B1B3A", "ink2": "#474766", "line": "#1B1B3A", "card": "#FFFFFF",
           "accent": "#FF5A4F", "accent-ink": "#1B1B3A", "accent-t": "#BC2A20", "accent2": "#3B6BFF",
           "dark": "#1B1B3A", "dark-ink": "#FFF7E6", "dark-accent": "#FFD23F", "ph1": "#FFD23F", "ph2": "#FF9A76",
           "fd": "'Syne',system-ui,sans-serif", "fb": "'Plus Jakarta Sans',system-ui,sans-serif", "fa": "'Plus Jakarta Sans',system-ui,sans-serif",
           "r": "20px", "rb": "999px", "hw": "700", "hls": "-0.04em", "hlh": "1", "htt": "none", "hs": ".84", "bw": "2px",
           "shadow": "5px 5px 0 var(--ink)", "phr": "28px"},
        css="h1 em,h2 em{font-style:normal;background:linear-gradient(transparent 62%,#FFD23F 62%)}.dark h1 em,.dark h2 em{background:none;color:var(--dark-accent)}"
            ".btn{box-shadow:4px 4px 0 var(--ink);font-weight:700}.dark .btn{box-shadow:4px 4px 0 rgba(0,0,0,.45)}.eyebrow{font-weight:700;letter-spacing:.1em}"
            "h3{font-size:1.15rem}.st-g b,.hstats b{font-size:clamp(2rem,3.8vw,3rem);white-space:nowrap}.hs-g>*,.hf-g>*{min-width:0}",
    ),
    "dark_stage": dict(
        label="Dark Stage",
        mood="Near-black with a spotlight gold and tall condensed capitals. Built for presence.",
        pair="Bebas Neue + Manrope",
        fonts=gf("Bebas+Neue", "Manrope:wght@400;500;600;700;800"),
        v={"bg": "#0F0F11", "bg2": "#17171B", "ink": "#F4F1EA", "ink2": "#B8B3A8", "line": "#2F2F37", "card": "#1A1A1F",
           "accent": "#F2B544", "accent-ink": "#0F0F11", "accent-t": "#F2B544", "accent2": "#E5484D",
           "dark": "#F4F1EA", "dark-ink": "#121214", "dark-accent": "#7A4E00", "ph1": "#3A3327", "ph2": "#1F1C17",
           "fd": "'Bebas Neue','Arial Narrow',sans-serif", "fb": "'Manrope',system-ui,sans-serif", "fa": "'Manrope',system-ui,sans-serif",
           "r": "4px", "rb": "4px", "hw": "400", "hls": ".012em", "hlh": ".9", "htt": "uppercase", "hs": "1.3", "bw": "1px",
           "shadow": "none", "phr": "4px"},
        css="h1 em,h2 em{font-style:normal;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}.btn{font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:.86rem}"
            ".eyebrow{font-weight:800;letter-spacing:.22em}h3{font-size:1.6rem}.ph span{background:#F4F1EA;color:#121214}",
    ),
    "corporate_calm": dict(
        label="Corporate Calm",
        mood="White, slate navy and one teal. A serious serif, mono labels, hairline grids. Reassures a board.",
        pair="Source Serif 4 + IBM Plex Sans",
        fonts=gf("Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700", "IBM+Plex+Sans:wght@400;500;600", "IBM+Plex+Mono:wght@400;500"),
        v={"bg": "#FFFFFF", "bg2": "#F3F5F7", "ink": "#14213D", "ink2": "#4B576F", "line": "#DAE0E7", "card": "#FFFFFF",
           "accent": "#0F6E66", "accent-ink": "#FFFFFF", "accent-t": "#0D645D", "accent2": "#14213D",
           "dark": "#14213D", "dark-ink": "#EEF2F7", "dark-accent": "#7FD6CC", "ph1": "#D5DEE8", "ph2": "#9FB0C4",
           "fd": "'Source Serif 4',Georgia,serif", "fb": "'IBM Plex Sans',system-ui,sans-serif", "fa": "'IBM Plex Mono',ui-monospace,monospace",
           "r": "8px", "rb": "8px", "hw": "600", "hls": "-0.018em", "hlh": "1.08", "htt": "none", "hs": ".94", "bw": "1px",
           "shadow": "0 1px 2px rgba(20,33,61,.05),0 10px 28px rgba(20,33,61,.06)", "phr": "8px"},
        css="h1 em,h2 em{font-style:italic;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}.eyebrow{letter-spacing:.08em;font-size:.76rem}",
    ),
    "magazine": dict(
        label="Magazine",
        mood="Black rules, a high-contrast serif, a single red. Reads like a feature in a weekend paper.",
        pair="Bodoni Moda + Libre Franklin",
        fonts=gf("Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900", "Libre+Franklin:wght@400;500;600;700"),
        v={"bg": "#FFFFFF", "bg2": "#F5F2EC", "ink": "#111111", "ink2": "#4F4F4F", "line": "#111111", "card": "#FFFFFF",
           "accent": "#C8102E", "accent-ink": "#FFFFFF", "accent-t": "#C8102E", "accent2": "#111111",
           "dark": "#111111", "dark-ink": "#F5F2EC", "dark-accent": "#FF8A9B", "ph1": "#E3DED4", "ph2": "#B4AC9C",
           "fd": "'Bodoni Moda',Georgia,serif", "fb": "'Libre Franklin',system-ui,sans-serif", "fa": "'Libre Franklin',system-ui,sans-serif",
           "r": "0px", "rb": "0px", "hw": "700", "hls": "-0.03em", "hlh": "1", "htt": "none", "hs": "1.04", "bw": "1px",
           "shadow": "none", "phr": "0px"},
        css="h1 em,h2 em{font-style:italic;font-weight:500;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}"
            ".eyebrow{font-weight:700;letter-spacing:.16em}.sh{border-top:3px solid var(--ink);padding-top:1rem}.dark .sh{border-color:var(--dark-ink)}"
            ".btn{text-transform:uppercase;letter-spacing:.1em;font-size:.82rem;font-weight:700}",
    ),
    "retro_scrapbook": dict(
        label="Retro Scrapbook",
        mood="Kraft paper, tomato and teal, taped-on cards and handwritten notes. Warm and a bit cheeky.",
        pair="Caprasimo + Space Grotesk (+ Caveat notes)",
        fonts=gf("Caprasimo", "Space+Grotesk:wght@400;500;600;700", "Caveat:wght@500;700"),
        v={"bg": "#F0E6D2", "bg2": "#E6D8BD", "ink": "#2B2118", "ink2": "#5A4A3B", "line": "#2B2118", "card": "#FBF6EA",
           "accent": "#C23B1E", "accent-ink": "#FFF6E9", "accent-t": "#A93217", "accent2": "#1F6F78",
           "dark": "#1F4A4F", "dark-ink": "#F6EEDC", "dark-accent": "#F2C14E", "ph1": "#F2C14E", "ph2": "#E08A4F",
           "fd": "'Caprasimo',Georgia,serif", "fb": "'Space Grotesk',system-ui,sans-serif", "fa": "'Caveat',cursive",
           "r": "10px", "rb": "10px", "hw": "400", "hls": "-0.005em", "hlh": "1.05", "htt": "none", "hs": ".98", "bw": "2px",
           "shadow": "4px 4px 0 rgba(43,33,24,.9)", "phr": "10px"},
        css="h1 em,h2 em{font-style:normal;color:var(--accent-t)}.dark h1 em,.dark h2 em{color:var(--dark-accent)}"
            ".eyebrow{font-size:1.45rem;letter-spacing:0;text-transform:none;font-weight:700;rotate:-2deg;display:inline-block}"
            ".card{border-style:dashed}.grid>.card:nth-child(odd){rotate:-.6deg}.grid>.card:nth-child(even){rotate:.5deg}"
            ".btn{font-weight:700;box-shadow:3px 3px 0 var(--ink)}.ph{rotate:1.5deg;border:8px solid var(--card);box-shadow:var(--shadow)}",
    ),
}
