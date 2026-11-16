"""The 2 pages a member actually uses: the index of all sites, and 1 short page per site with its preview and its code.

Both follow the Authority Builder brand at yasmincronin.com: deep forest, lime, cream, Plus Jakarta Sans.
The long teaching notes for each site still exist as notes.md in its folder. They are no longer put in front of the reader.
"""
import re

import shell
from kit import e

# Where the repository's files can be loaded from on the open web. The code block on each site's page points its pictures here,
# so the code works, pictures included, wherever it is pasted. Change this if the repository moves.
RAW = "https://raw.githubusercontent.com/authoritybuilder/authority-builder-design-library/main"

CSS = r"""<style>
.bar{background:var(--deep);color:#F6F5F0}.bar .top{padding-block:1rem}
.intro{background:linear-gradient(180deg,var(--deep),var(--forest));color:#F6F5F0;padding-block:clamp(40px,6vw,84px) clamp(44px,6vw,88px)}
.intro h1{font-size:clamp(2.1rem,5vw,3.6rem);max-width:17ch}.intro h1 em{font-style:normal;color:var(--gold)}
.intro p{margin-top:1.1rem;font-size:clamp(1.02rem,1.5vw,1.2rem);color:rgba(246,245,240,.82);max-width:54ch}
.pick{position:sticky;top:0;z-index:5;background:rgba(246,245,240,.95);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);padding-block:.75rem}
.pick .wrap{display:flex;flex-wrap:wrap;gap:.45rem;align-items:center}.pick span{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--ink2);margin-right:.3rem}
.chip[aria-pressed=true]{background:var(--forest);color:#F6F5F0;border-color:var(--forest)}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:clamp(18px,2.4vw,30px);padding-block:clamp(32px,5vw,64px) clamp(56px,8vw,104px)}
.tile{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;transition:transform .2s,box-shadow .2s,border-color .2s}
.tile:hover{transform:translateY(-4px);box-shadow:0 26px 50px -28px rgba(11,42,34,.45);border-color:var(--gold)}
.tile[hidden]{display:none}
.tile .th{display:block;aspect-ratio:16/10;background:var(--cream);overflow:hidden}.tile .th img{width:100%;height:100%;object-fit:cover;object-position:top;transition:transform .5s}
.tile:hover .th img{transform:scale(1.04)}
.tile .bd{padding:1rem 1.15rem 1.2rem;display:flex;flex-direction:column;gap:.85rem;flex:1}
.tile h2{font-size:1.12rem;line-height:1.25;letter-spacing:-.01em}.tile h2 small{display:block;font:600 .72rem/1.3 'Inter',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--sage);margin-bottom:.3rem}
.tile .go{display:flex;gap:.5rem;margin-top:auto}
.b{flex:1;display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:.5em 1em;border-radius:999px;font:700 .9rem 'Inter',sans-serif;text-decoration:none;border:2px solid var(--forest);color:var(--forest);background:transparent;cursor:pointer;transition:transform .15s,background .15s}
.b.main{background:var(--gold);border-color:var(--gold);color:var(--deep)}.b:hover{transform:translateY(-2px)}
/* a site's page */
.one{padding-block:clamp(28px,4vw,52px) clamp(56px,8vw,96px)}.one .back{font-size:.9rem;color:var(--sage);font-weight:600}
.one h1{font-size:clamp(1.9rem,4.4vw,3rem);margin:.9rem 0 1.4rem}.one h1 small{display:block;font:600 .78rem/1.3 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--sage);margin-bottom:.5rem}
.one .shot{display:block;border-radius:20px;overflow:hidden;border:1px solid var(--line);box-shadow:0 34px 70px -40px rgba(11,42,34,.5);background:#fff}.one .shot img{width:100%;height:auto}
.one .go{display:flex;flex-wrap:wrap;gap:.6rem;margin:1.4rem 0 0}.one .go .b{flex:0 1 auto;padding-inline:1.5rem}
.code{margin-top:clamp(28px,4vw,44px);background:var(--deep);border-radius:20px;overflow:hidden;color:#EAF3E2}
.code header{display:flex;flex-wrap:wrap;gap:.6rem 1rem;align-items:center;justify-content:space-between;padding:.9rem 1rem .9rem 1.3rem;border-bottom:1px solid rgba(246,245,240,.14)}
.code header b{font:700 .95rem 'Plus Jakarta Sans',sans-serif}.code header span{display:block;font-size:.8rem;color:rgba(234,243,226,.7);font-weight:400}
.code .b{flex:none;min-height:42px;border-color:var(--gold);background:var(--gold);color:var(--deep)}
.code pre{margin:0;padding:1.2rem 1.3rem;max-height:520px;overflow:auto;font:400 .8rem/1.6 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;white-space:pre-wrap;word-break:break-word;tab-size:2}
.code.alt{background:#fff;color:var(--ink);border:1px solid var(--line)}.code.alt header{border-color:var(--line)}.code.alt header span{color:var(--ink2)}.code.alt pre{max-height:300px}
.code.alt .b{background:transparent;border-color:var(--forest);color:var(--forest)}
</style>"""

COPY_JS = """<script>
document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){var t=document.getElementById(b.dataset.copy).textContent,was=b.textContent;
function ok(){b.textContent='Copied';setTimeout(function(){b.textContent=was},1600)}
if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(ok)}else{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();document.execCommand('copy');a.remove();ok()}})});
</script>"""


def bar(root=""):
    return f'<div class="bar"><div class="wrap">{shell.top(root)}</div></div>'


def gallery(pages):
    auds = ["Coach", "Creator", "Consultant", "Business Owner"]
    chips = "".join(f'<button class="chip" type="button" data-v="{e(x)}" aria-pressed="false">{e(x)}</button>' for x in auds)
    tiles = "".join(
        f'<article class="tile" data-a="{e("|".join(P["aud"]))}"><a class="th" href="{P["dir"]}/site/index.html" aria-label="Open the live {e(P["name"])} site">'
        f'<img src="{P["dir"]}/preview.jpg" alt="" loading="lazy" width="960" height="600"></a>'
        f'<div class="bd"><h2><small>{P["num"]} · {e(P["group"])}</small>{e(P["name"])}</h2>'
        f'<div class="go"><a class="b main" href="{P["dir"]}/site/index.html">View Live</a><a class="b" href="{P["dir"]}/index.html">Get The Code</a></div></div></article>'
        for P in pages)
    body = f"""{CSS}{bar()}
<header class="intro"><div class="wrap"><p class="kick" style="color:var(--gold)">Authority Builder™ · Design Library</p>
<h1>{len(pages)} websites, <em>ready to make yours.</em></h1>
<p>Open any site to see it live, then copy its code.</p></div></header>
<main id="main">
<div class="pick"><div class="wrap"><span>I am a</span>{chips}<button class="chip" type="button" id="all" style="border-style:dashed">Show all</button></div></div>
<div class="wrap"><div class="tiles">{tiles}</div></div>
</main>
<script>
(function(){{var on=null,chips=document.querySelectorAll('.chip[data-v]'),tiles=document.querySelectorAll('.tile');
function run(){{tiles.forEach(function(t){{t.hidden=!!on&&t.dataset.a.split('|').indexOf(on)<0}});chips.forEach(function(c){{c.setAttribute('aria-pressed',on===c.dataset.v)}})}}
chips.forEach(function(c){{c.addEventListener('click',function(){{on=on===c.dataset.v?null:c.dataset.v;run()}})}});document.getElementById('all').addEventListener('click',function(){{on=null;run()}})}})();
</script>"""
    return shell.page("Authority Builder Design Library", f"{len(pages)} complete websites for coaches, creators, consultants and business owners. See each one live and copy its code.", body)


def portable(html, P):
    """The site's main page as code that works wherever it is pasted: every picture and icon is loaded from the library's own address,
    and links to the site's other pages point at the files in its folder."""
    base = f'{RAW}/{P["dir"]}/site/'
    html = re.sub(r'(?<=["\s,])images/', base + "images/", html)
    html = re.sub(r'href="(icon-\d+\.png)"', lambda m: f'href="{base}{m.group(1)}"', html)
    return html


def entry(P, site_html, prompt):
    code = portable(site_html, P)
    body = f"""{CSS}{bar("../")}
<main id="main"><div class="wrap narrow one">
<a class="back" href="../index.html">← All websites</a>
<h1><small>{P["num"]} · {e(P["group"])}</small>{e(P["name"])}</h1>
<a class="shot" href="site/index.html"><img src="preview.jpg" alt="Preview of the {e(P["name"])} site" width="960" height="600"></a>
<div class="go"><a class="b main" href="site/index.html">View Live</a></div>
<section class="code" aria-label="The page's code"><header><div><b>The Code</b><span>The whole page in 1 file. Paste it into a new .html file and open it.</span></div>
<button class="b" type="button" data-copy="src">Copy Code</button></header><pre id="src" tabindex="0">{e(code)}</pre></section>
<section class="code alt" aria-label="Build prompt"><header><div><b>Or Build It With AI</b><span>Paste this prompt into Claude with your own details.</span></div>
<button class="b" type="button" data-copy="ask">Copy Prompt</button></header><pre id="ask" tabindex="0">{e(prompt)}</pre></section>
</div></main>
{COPY_JS}"""
    return shell.page(f'{P["num"]} · {P["name"]} | Authority Builder Design Library', f'{P["name"]}: see it live and copy its code.', body, root="../")
