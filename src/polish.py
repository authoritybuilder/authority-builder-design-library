"""The finishing layer shared by every sample: illustration colours, atmosphere, depth, the sticky header,
the proof cluster, the reassurance line and the mobile action bar. Each style direction then adds its own signature."""

GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' "
         "baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .5 0'/%3E%3C/filter%3E"
         "%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

POLISH_CSS = r"""
/* illustration colours follow the page's own tokens */
.i-1{fill:var(--ph1)}.i-2{fill:var(--ph2)}.i-a{fill:var(--accent)}.i-b{fill:var(--accent2)}.i-d{fill:var(--dark)}.i-c{fill:var(--card)}.i-g{fill:var(--bg2)}.i-l{fill:var(--line)}
.ph{box-shadow:0 34px 64px -30px color-mix(in srgb,var(--ink) 50%,transparent)}
.ph.person{background:radial-gradient(circle at 74% 22%,color-mix(in srgb,var(--card) 62%,transparent) 0 23%,transparent 23.5%),radial-gradient(90% 70% at 30% 18%,var(--ph1),var(--ph2))}
.ph.vid .play{box-shadow:0 12px 30px rgba(0,0,0,.3)}
.ph .cap{position:absolute;left:14px;bottom:14px;z-index:2;font:600 .76rem/1.2 var(--fb);background:rgba(0,0,0,.74);color:#fff;padding:.5em .8em;border-radius:6px;max-width:calc(100% - 28px)}
.av{display:block;width:44px;height:44px;border-radius:50%;flex:none;overflow:hidden;background:var(--bg2)}.av img{width:100%;height:100%;object-fit:cover;display:block}
/* photographs: framed, lifted off the page, and cropped from the top so a face is never cut */
.ph.photo{background:var(--bg2);box-shadow:0 38px 72px -36px color-mix(in srgb,var(--ink) 62%,transparent)}
.eyebrow.who{display:flex;align-items:center;gap:.75rem}.hcenter .eyebrow.who,.center .eyebrow.who{justify-content:center}
.eyebrow.who .av{width:38px;height:38px;box-shadow:0 0 0 2px rgba(255,255,255,.85),0 6px 16px -6px rgba(0,0,0,.5)}.eyebrow.who::before{display:none}
.host{display:flex;align-items:center;gap:.85rem;margin:1.4rem 0;text-align:left}.host .av{width:56px;height:56px;box-shadow:0 0 0 3px var(--card),0 0 0 4px var(--line)}
.host span{font-size:.9rem;color:var(--ink2);line-height:1.35}.host b{display:block;font-size:1.02rem;color:var(--ink)}.thx .host{justify-content:center}
.cta .host{justify-content:center;margin:2rem 0 0}.cta.bleed .host .av{box-shadow:0 0 0 2px rgba(255,255,255,.85)}.cta.bleed .host span{color:rgba(255,255,255,.9)}.cta.bleed .host b{color:#fff}
/* the name under a portrait: who this is, said once more where the eye already is */
.signed{margin-top:1.1rem;font-size:.9rem;color:var(--ink2);line-height:1.35}.signed b{display:block;font-family:var(--fd);font-weight:var(--hw);font-size:1.15rem;letter-spacing:var(--hls);color:var(--ink)}
.sp-v{position:relative}.sp-v .ph.photo{outline:1px solid color-mix(in srgb,var(--ink) 10%,transparent);outline-offset:-1px}
/* testimonials read as people: a larger face, the name in ink, and a quiet accent edge on the card */
.qt figcaption .av{width:52px;height:52px;box-shadow:0 0 0 3px var(--card),0 0 0 4px color-mix(in srgb,var(--accent) 40%,transparent)}
.qt figure.card{border-top:3px solid color-mix(in srgb,var(--accent) 55%,transparent)}.qt figcaption b{font-size:1rem}
input,select,textarea{font-size:max(16px,1rem)}
/* on a phone a form hero shows its form before its bullet points, so the first button is on the first screen */
@media(max-width:860px){.hf-g{gap:1.1rem}.hf-g>div:first-child{display:contents}.hf-g>div:first-child>*{margin-top:0}.hf-v{order:2}.hf-g .ticks,.hf-g .meta,.hf-g .crowd,.hf-g>div:first-child>.reassure,.hform.long .hf-g .lead{order:3}.hform .formcard{padding:1.2rem 1.2rem 1.3rem}}
.ic{width:22px;height:22px;flex:none}
/* header */
:root{--hh:76px}
.hdw{position:sticky;top:0;z-index:20;min-height:var(--hh);display:grid;align-items:center;color:var(--ink);background:color-mix(in srgb,var(--bg) 84%,transparent);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);border-bottom:1px solid color-mix(in srgb,var(--line) 60%,transparent)}
.hd{padding-block:.7rem;width:100%}
/* over a painted hero the menu floats as a bar of glass, shaped like the theme's buttons, and turns to frosted paper as the page scrolls.
   Browsers without scroll timelines get the frosted bar from the start */
.over{--hh:90px}
.over .hdw{background:transparent;border-color:transparent;-webkit-backdrop-filter:none;backdrop-filter:none;pointer-events:none;padding:12px clamp(10px,2vw,22px) 0}
.over .hd{pointer-events:auto;max-width:1180px;padding:.5rem .6rem .5rem clamp(1rem,2vw,1.5rem);border-radius:var(--rb);border:1px solid color-mix(in srgb,var(--line) 70%,transparent);
background:color-mix(in srgb,var(--bg) 88%,transparent);color:var(--ink);-webkit-backdrop-filter:blur(18px) saturate(1.4);backdrop-filter:blur(18px) saturate(1.4);box-shadow:0 14px 34px -22px rgba(0,0,0,.5)}
@supports(animation-timeline:scroll()){
.over .hd{background:var(--g0);border-color:rgba(255,255,255,.28);color:var(--h0);box-shadow:none;animation:hdw linear both;animation-timeline:scroll();animation-range:0 180px}
@keyframes hdw{to{background:color-mix(in srgb,var(--bg) 88%,transparent);border-color:color-mix(in srgb,var(--line) 70%,transparent);color:var(--ink);box-shadow:0 14px 34px -22px rgba(0,0,0,.5)}}
/* the painting drifts closer as the hero scrolls away */
@media(prefers-reduced-motion:no-preference){.hero.bleed picture.art img{transform-origin:50% 100%;animation:drift linear both;animation-timeline:scroll();animation-range:0 900px}@keyframes drift{to{transform:scale(1.1)}}}
}
.o-light{--g0:rgba(10,14,26,.3)}.o-dark{--g0:rgba(255,255,255,.6)}
.o-light{--h0:#fff}.o-dark{--h0:var(--ink)}
.mnav{display:none;position:relative}.mnav summary{list-style:none;cursor:pointer;width:48px;height:48px;display:grid;place-items:center;border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),12px)}
.mnav summary::-webkit-details-marker{display:none}.mnav ul{position:absolute;right:0;top:56px;min-width:230px;background:var(--card);color:var(--ink);border:max(1px,var(--bw)) solid var(--line);border-radius:min(var(--r),14px);padding:.5rem;box-shadow:0 24px 48px -20px rgba(0,0,0,.4)}
.mnav a{display:block;padding:.85rem .9rem;text-decoration:none;border-radius:8px;font-weight:600}.mnav a:hover{background:var(--bg2)}
@media(max-width:860px){.mnav{display:block}.hd.has-nav>.btn{display:none}}
.ann{background:var(--dark);color:var(--dark-ink);text-align:center;font-size:.88rem;font-weight:500;padding:.6rem 1rem}.ann b{color:var(--dark-accent)}.ann a{color:inherit;text-underline-offset:.2em;font-weight:700}
/* atmosphere */
:root{--grain:GRAIN}
.hero,.cta,.hart,.lb{position:relative;isolation:isolate;overflow:clip}
.lb::before{content:"";position:absolute;inset:0;z-index:-2;background:var(--atmo,none);pointer-events:none}
/* painted sections: the picture, a veil that keeps the words readable, then the words */
.bleed::before{content:"";position:absolute;inset:0;z-index:-2;pointer-events:none;-webkit-mask-image:none!important;mask-image:none!important}
.t-light{--ink:#fff;--ink2:rgba(255,255,255,.92);--line:rgba(255,255,255,.38);--accent-t:#fff;color:#fff}
/* each veil is tuned so every line of text measures at least 4.5 to 1 against the picture behind it (3 to 1 for large type). src/legible.mjs checks it */
.t-light::before{background:linear-gradient(180deg,rgba(6,10,22,.66) 0,rgba(6,10,22,.64) 62%,rgba(6,10,22,.4) 84%,rgba(6,10,22,.1))}
.hsplit.t-light::before,.hform.t-light::before,.hstage.t-light::before{background:linear-gradient(90deg,rgba(6,10,22,.78) 0,rgba(6,10,22,.7) 42%,rgba(6,10,22,.22) 70%,rgba(6,10,22,0) 90%),linear-gradient(180deg,rgba(6,10,22,.6) 0,rgba(6,10,22,.44) 11%,rgba(6,10,22,0) 30%)}
.t-dark::before{background:linear-gradient(180deg,rgba(255,255,255,.86) 0,rgba(255,255,255,.82) 58%,rgba(255,255,255,.42) 80%,rgba(255,255,255,0) 97%)}
.hsplit.t-dark::before,.hform.t-dark::before,.hstage.t-dark::before{background:linear-gradient(90deg,rgba(255,255,255,.9) 0,rgba(255,255,255,.84) 42%,rgba(255,255,255,.26) 68%,rgba(255,255,255,0) 86%),linear-gradient(180deg,rgba(255,255,255,.7) 0,rgba(255,255,255,.5) 11%,rgba(255,255,255,0) 30%)}
.cta.bleed::before{background:linear-gradient(180deg,rgba(6,10,22,.74),rgba(6,10,22,.62))}
@media(max-width:860px){.hero.t-light::before{background:linear-gradient(180deg,rgba(6,10,22,.7),rgba(6,10,22,.62))}.hero.t-dark::before{background:linear-gradient(180deg,rgba(255,255,255,.9),rgba(255,255,255,.82))}}
.t-dark{--ink2:var(--ink)}.t-dark .reassure,.t-dark .crowd,.t-dark .lead{color:var(--ink)}
.hero.bleed{min-height:min(94svh,880px);display:grid;align-content:center}
.over .hero.bleed{margin-top:calc(var(--hh)*-1);padding-top:calc(var(--hh) + clamp(36px,5vw,72px))}
.bleed h1 em,.bleed h2 em{background:none!important}.bleed.t-light h1 em,.bleed.t-light h2 em{color:#FFE6BF}
.t-light h1,.t-light h2,.t-light .lead{text-shadow:0 2px 26px rgba(0,0,0,.3)}
.t-light .btn.ghost{color:#fff;border-color:rgba(255,255,255,.78);background:rgba(8,12,24,.36);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.t-dark .btn.ghost{background:rgba(255,255,255,.72);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.bleed .chips li{background:rgba(255,255,255,.16);border-color:rgba(255,255,255,.44);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);color:inherit}
.t-light .chips li{background:rgba(8,12,24,.36)}.t-dark .chips li{background:rgba(255,255,255,.78)}
.bleed .bookwrap{background:transparent;padding:0}
.hform.bleed .hf-v>.reassure{margin-top:0;padding:.75rem 1rem;border-radius:14px;-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}
.hform.t-light .hf-v>.reassure{background:rgba(8,12,24,.58)}.hform.t-dark .hf-v>.reassure{background:rgba(255,255,255,.84)}
.t-light .hstats{background:rgba(6,10,22,.56);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.2);border-radius:18px;padding:1.3rem 1.6rem}
.t-dark .hstats{background:rgba(255,255,255,.8);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.7);border-radius:18px;padding:1.3rem 1.6rem}
.bleed .crowd .av{border-color:rgba(255,255,255,.85)}
/* the proof cards sit on the painting as glass, stacked in the lower corner where the picture is quietest */
.hsplit.bleed .hs-v:not(.has-card):not(.has-pic){display:grid;align-content:end;justify-items:end;gap:14px;min-height:clamp(220px,30vw,400px)}
.hsplit.bleed .float,.hsplit.bleed .float.f2{position:static;max-width:290px;width:100%;border:1px solid rgba(255,255,255,.34);border-radius:18px;box-shadow:0 24px 50px -24px rgba(0,0,0,.5);-webkit-backdrop-filter:blur(16px) saturate(1.2);backdrop-filter:blur(16px) saturate(1.2)}
.hsplit.t-light .float{background:rgba(10,14,28,.62);color:#fff}.hsplit.t-light .float b,.hsplit.t-light .float.f2 b{color:#fff}.hsplit.t-light .float.f2 span{color:rgba(255,255,255,.86)}
.hsplit.t-light .float.f2>.ic{background:rgba(255,255,255,.18);color:#fff}
.hsplit.t-dark .float{background:rgba(255,255,255,.82);color:var(--ink)}
/* a portrait in the hero: the photo is framed, an offset line sits behind it, and the proof cards overlap its edges */
.hsplit.bleed .hs-v.has-pic{display:block;position:relative;min-height:0;width:min(100%,430px);margin-left:auto}
.hs-v.has-pic .ph,.hst-v .ph{outline:1px solid rgba(255,255,255,.4);outline-offset:-1px;box-shadow:0 44px 90px -40px rgba(0,0,0,.7)}
.hs-v.has-pic::before,.hst-v::before{content:"";position:absolute;inset:20px -20px -20px 20px;border:1px solid rgba(255,255,255,.5);border-radius:var(--phr);z-index:-1}
.t-dark .hs-v.has-pic::before,.t-dark .hst-v::before{border-color:color-mix(in srgb,var(--ink) 34%,transparent)}
.hsplit.bleed .hs-v.has-pic .float{position:absolute;left:-16%;bottom:8%;width:auto;max-width:236px}
.hsplit.bleed .hs-v.has-pic .float.f2{left:auto;right:-13%;top:10%;bottom:auto;max-width:214px}
.hst-v{position:relative;width:min(100%,400px);margin-left:auto}
@media(max-width:860px){.hsplit.bleed .hs-v.has-pic{width:min(100%,340px);margin:1.6rem 0 0}.hs-v.has-pic .ph{--ar:1/1!important}
.hsplit.bleed .hs-v.has-pic .float,.hsplit.bleed .hs-v.has-pic .float.f2{position:static;max-width:none;margin-top:.8rem}.hst-v{margin:1.6rem 0 0;width:min(100%,340px)}.hst-v .ph{--ar:1/1!important}}
@media(max-width:860px){.hsplit.bleed .hs-v:not(.has-card):not(.has-pic){display:flex;min-height:0;margin-top:.4rem}.hsplit.bleed .float,.hsplit.bleed .float.f2{max-width:none;flex:1 1 150px}}
.cta.deep picture.art img{object-position:50% 84%}
.cta.deep{padding-block:clamp(88px,12vw,168px)}
.ph.art{box-shadow:0 34px 64px -30px color-mix(in srgb,var(--ink) 55%,transparent)}
.ph.vid .play{position:absolute;left:50%;top:50%;translate:-50% -50%;width:74px;height:74px;border-radius:50%;background:#fff;z-index:2}
.ph.vid .play::after{content:"";position:absolute;left:54%;top:50%;translate:-50% -50%;border-left:20px solid #111;border-block:13px solid transparent}
.cta:not(.bleed)::after{content:"";position:absolute;inset:0;z-index:-1;background-image:var(--grain);opacity:.07;pointer-events:none}
.cta:not(.bleed)::before{content:"";position:absolute;z-index:-1;width:min(92vw,840px);aspect-ratio:1;left:50%;top:50%;translate:-50% -50%;border-radius:50%;border:1px solid color-mix(in srgb,var(--ink) 14%,transparent);box-shadow:0 0 0 72px color-mix(in srgb,var(--ink) 4%,transparent),0 0 0 156px color-mix(in srgb,var(--ink) 3%,transparent);pointer-events:none}
/* proof beside the button, reassurance under it */
.crowd{display:flex;align-items:center;gap:.9rem;margin-top:1.7rem;font-size:.93rem;color:var(--ink2);line-height:1.4;text-align:left}.crowd b{color:var(--ink)}.crowd p{margin:0}
.crowd .avs{display:flex;flex:none}.crowd .av{width:40px;height:40px;border:2.5px solid var(--bg);margin-left:-12px}.crowd .av:first-child{margin-left:0}
.hcenter .crowd,.center .crowd{justify-content:center}
.reassure{display:flex;align-items:flex-start;gap:.5rem;margin-top:1rem;font-size:.9rem;color:var(--ink2);text-align:left}.reassure .ic{width:18px;height:18px;color:var(--accent-t);margin-top:.14em}
.hcenter .reassure,.cta .reassure{justify-content:center}
.float{border:0;border-radius:16px;box-shadow:0 26px 50px -20px rgba(0,0,0,.42)}
.float.f2{left:auto;right:-7%;top:9%;bottom:auto;display:flex;gap:.75rem;align-items:center;max-width:250px;padding:12px 16px}
.float.f2>.ic{width:40px;height:40px;padding:9px;border-radius:50%;background:color-mix(in srgb,var(--accent) 14%,transparent);color:var(--accent-t)}
.float.f2 b{font:700 .95rem/1.25 var(--fb);letter-spacing:0;text-transform:none;color:var(--ink)}.float.f2 span{font-size:.8rem;color:var(--ink2)}
@media(max-width:860px){.float.f2{right:-4px;top:5%}}
/* buttons and forms */
.btn{box-shadow:0 14px 28px -14px color-mix(in srgb,var(--accent) 75%,transparent)}
:where(.btn:not(.ghost)){background-image:linear-gradient(180deg,rgba(255,255,255,.17),rgba(255,255,255,0) 58%)}   /* a soft light across the top of every main button */
.cta.bleed h2{font-size:clamp(2.2rem,calc(5.2vw*var(--hs)),calc(4.2rem*var(--hs)))}
.stats b,.hstats b,.float b,.tier .price{font-variant-numeric:lining-nums tabular-nums}
/* the brand name, very large and very quiet, closes every page */
.ft{overflow:hidden}.ft-mark{font-family:var(--fd);font-weight:var(--hw);text-transform:var(--htt);letter-spacing:var(--hls);line-height:.82;white-space:nowrap;text-align:center;
font-size:min(15rem,calc(168vw / var(--n)));margin:clamp(28px,5vw,60px) 0 -.14em;user-select:none}.ft-mark::before{content:attr(data-mark)}.ft .ft-mark{color:color-mix(in srgb,var(--dark-ink) 11%,transparent)}   /* decoration, drawn by the stylesheet so it is not read out or indexed twice */
.btn:not(.ghost)::after{content:"";width:.44em;height:.44em;border-top:2px solid;border-right:2px solid;rotate:45deg;margin-left:.1em;transition:translate .2s}
.btn:not(.ghost):hover::after{translate:3px -3px}
.formcard{position:relative;border-top:4px solid var(--accent);box-shadow:0 34px 64px -34px rgba(0,0,0,.42)}
.field input:focus,.field select:focus,.field textarea:focus{outline:3px solid color-mix(in srgb,var(--accent) 45%,transparent);outline-offset:1px;border-color:var(--accent-t)}
.formcard .fine{display:flex;gap:.45rem;justify-content:center;align-items:flex-start;text-align:left}.formcard .fine .ic{width:16px;height:16px;margin-top:.15em}
.formcard .crowd{margin-top:1.1rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.86rem}.formcard .crowd .av{border-color:var(--card);width:34px;height:34px}
.cals{display:flex;flex-wrap:wrap;gap:.4rem 1rem;margin-top:.9rem;font-size:.86rem;justify-content:center}.cals span{color:var(--ink2)}.cals a{font-weight:600;text-underline-offset:.2em}
/* mock-ups */
.mk{padding:0;overflow:hidden;box-shadow:0 34px 64px -30px rgba(0,0,0,.4)}
.mk-email{padding:22px 24px 0;position:relative}.mk-top{display:flex;align-items:center;gap:.8rem;padding-bottom:.9rem;border-bottom:1px solid var(--line);margin-bottom:1rem}
.mk-top b{display:block;font-size:.95rem}.mk-top div span{font-size:.8rem;color:var(--ink2)}.mk-top i{margin-left:auto;font-style:normal;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;background:var(--bg2);border-radius:999px;padding:.35em .8em}
.mk-email h3{font-size:1.3rem;margin-bottom:.7rem}.mk-email p{font-size:.95rem;color:var(--ink2);line-height:1.55}.mk-email p+p{margin-top:.7em}
.mk-fade{height:70px;margin-top:-34px;position:relative;background:linear-gradient(transparent,var(--card))}
.mk-lesson .ph{border-radius:0;box-shadow:none}.mk-lesson ul{padding:.5rem 1.2rem 1rem}
.mk-lesson li{display:grid;grid-template-columns:auto 1fr auto;gap:.8rem;align-items:center;padding:.7rem 0;border-top:1px solid var(--line);font-size:.93rem}.mk-lesson li:first-child{border-top:0}
.mk-lesson li i{width:20px;height:20px;border-radius:50%;border:2px solid var(--line)}.mk-lesson li.done i{background:var(--accent-t);border-color:var(--accent-t)}.mk-lesson li.on{font-weight:700}.mk-lesson li.on i{border-color:var(--accent-t)}
.mk-lesson small{color:var(--ink2);font-size:.8rem}
/* mobile action bar */
.sticky{position:fixed;left:0;right:0;bottom:0;z-index:30;display:none;align-items:center;justify-content:space-between;gap:.8rem;padding:.65rem 1rem calc(.65rem + env(safe-area-inset-bottom));background:var(--card);color:var(--ink);border-top:max(1px,var(--bw)) solid var(--line);box-shadow:0 -10px 30px rgba(0,0,0,.14);font-size:.84rem;line-height:1.3}
.sticky b{display:block}.sticky .btn{min-height:48px;padding:.6em 1.1em;font-size:.92rem;white-space:nowrap;box-shadow:none}
@media(max-width:760px){.sticky{display:flex}body.has-sticky{padding-bottom:76px}}
.ft{position:relative}
@media(prefers-reduced-motion:no-preference){
.float{animation:bob 7s ease-in-out infinite}.float.f2{animation-delay:-3s}@keyframes bob{50%{translate:0 -8px}}
}
@media print{.sticky,.ann{display:none}}
""".replace("GRAIN", GRAIN)

THEME_POLISH = {
    "warm_editorial": ".card{box-shadow:0 1px 0 rgba(255,255,255,.7) inset,0 1px 2px rgba(20,16,10,.05),0 22px 44px -30px rgba(20,16,10,.3)}" ":root{--atmo:radial-gradient(52% 60% at 90% 6%,#F1D6B4 0,transparent 70%),radial-gradient(40% 50% at 0 100%,#EADCC3,transparent 70%)}"
                      ".eyebrow::before{content:\"\";display:inline-block;width:30px;height:1px;background:currentColor;margin-right:.8em;vertical-align:middle}"
                      ".center .eyebrow::before,.hcenter .eyebrow::before,.cta .eyebrow::before{display:none}"
                      ".card{border-radius:12px}.hs-v .ph{box-shadow:0 0 0 10px var(--bg),0 0 0 11px var(--line),0 44px 70px -30px rgba(60,30,10,.55)}",
    "quiet_luxury": ":root{--atmo:linear-gradient(180deg,#F8F4ED,transparent 62%)}"
                    ".hero .ph,.hero .bookwrap{outline:1px solid var(--accent2);outline-offset:12px}.btn{box-shadow:none}.btn:not(.ghost)::after{display:none}.sh{position:relative}"
                    ".sh::before{content:\"\";position:absolute;top:-1px;left:0;width:64px;height:1px;background:var(--accent2)}.sh.center::before{left:50%;translate:-50% 0}"
                    ".formcard{border-top:1px solid var(--accent2);background:var(--card)}.float{border-radius:0}.tier.hot{background:var(--card)}",
    "bold_type": ":root{--atmo:linear-gradient(var(--bg2) 2px,transparent 2px) 0 0/100% 72px}.hero{border-bottom:2px solid var(--ink)}"
                 ".cards .card:hover{translate:-3px -3px;box-shadow:10px 10px 0 var(--accent)}.hero .ph,.hero .mk{box-shadow:10px 10px 0 var(--accent);border:2px solid var(--ink)}"
                 ".res{background:var(--ink);color:var(--bg)}.float{border:2px solid var(--ink);border-radius:0;box-shadow:6px 6px 0 var(--ink)}"
                 ".formcard{border:2px solid var(--ink);box-shadow:8px 8px 0 var(--ink)}.btn:not(.ghost)::after{display:none}.tier.hot{box-shadow:10px 10px 0 var(--accent)}",
    "bento": ":root{--atmo:radial-gradient(38% 46% at 10% 0,#D9CCFF 0,transparent 70%),radial-gradient(34% 40% at 94% 14%,#C8F169 0,transparent 70%),radial-gradient(40% 40% at 60% 100%,#FFD7BF,transparent 70%)}"
             "main>.bento:first-child{position:relative;isolation:isolate}main>.bento:first-child::before{content:\"\";position:absolute;inset:-90px 0 0;z-index:-1;background:var(--atmo);opacity:.8}"
             ".tile{transition:translate .25s,box-shadow .25s}.tile:hover{translate:0 -5px;box-shadow:0 24px 44px -24px rgba(20,22,26,.4)}"
             ".card{box-shadow:0 1px 2px rgba(20,22,26,.05),0 20px 40px -28px rgba(20,22,26,.32)}.tile .ph{box-shadow:none}",
    "soft_organic": ".card{box-shadow:0 1px 0 rgba(255,255,255,.7) inset,0 1px 2px rgba(20,16,10,.05),0 22px 44px -30px rgba(20,16,10,.3)}" ":root{--atmo:radial-gradient(44% 56% at 96% 4%,#E4EBDD 0,transparent 70%),radial-gradient(36% 44% at 0 94%,#F3DCCB,transparent 70%)}"
                    ".sec.alt{border-radius:clamp(28px,5vw,64px);margin-inline:clamp(8px,2vw,28px)}.hero .ph.person,.split .ph.person{border-radius:48% 52% 46% 54% / 56% 50% 50% 44%}",
    "bright_playful": ":root{--atmo:radial-gradient(circle at 5% 30%,#FFD23F 0 26px,transparent 27px),radial-gradient(circle at 96% 78%,#3B6BFF 0 16px,transparent 17px),"
                      "radial-gradient(circle at 60% 6%,#FF5A4F 0 11px,transparent 12px),radial-gradient(circle at 40% 96%,#FF9A76 0 15px,transparent 16px)}"
                      ".hero .ph{rotate:2deg;border:2px solid var(--ink);box-shadow:8px 8px 0 var(--ink)}.cards .card:hover{rotate:-1deg}.float{border:2px solid var(--ink);box-shadow:4px 4px 0 var(--ink)}"
                      ".formcard{border:2px solid var(--ink);box-shadow:6px 6px 0 var(--ink)}.res{background:#FFD23F;color:var(--ink)}.tier.hot{box-shadow:8px 8px 0 var(--ink)}"
                      "@media(max-width:860px){:root{--atmo:none}}",
    "dark_stage": ":root{--atmo:radial-gradient(46% 70% at 78% 0,rgba(242,181,68,.22) 0,transparent 70%),radial-gradient(40% 60% at 6% 12%,rgba(229,72,77,.16),transparent 70%)}"
                  ".cards .n{font-size:3.4rem;color:transparent;-webkit-text-stroke:1.5px var(--accent)}"
                  ".hero .ph{box-shadow:0 0 0 1px #2F2F37,0 44px 84px -30px rgba(242,181,68,.4)}"
                  ".ph.scene .i-d{fill:#08080A}.ph.scene .i-c{fill:#F4F1EA}.ph.scene .i-2{fill:#2A2620}",
    "corporate_calm": ".card{box-shadow:0 1px 0 rgba(255,255,255,.7) inset,0 1px 2px rgba(20,16,10,.05),0 22px 44px -30px rgba(20,16,10,.3)}" ":root{--atmo:linear-gradient(#E9EEF3 1px,transparent 1px) 0 0/56px 56px,linear-gradient(90deg,#E9EEF3 1px,transparent 1px) 0 0/56px 56px}"
                      ".hero::before{-webkit-mask-image:radial-gradient(70% 85% at 72% 18%,#000,transparent);mask-image:radial-gradient(70% 85% at 72% 18%,#000,transparent)}"
                      ".hero .ph{box-shadow:0 1px 2px rgba(20,33,61,.08),0 44px 74px -36px rgba(20,33,61,.5)}",
    "magazine": ".hdw{border-bottom:3px double var(--ink)}"
                ".prose .wrap>p:first-of-type::first-letter{font-family:var(--fd);font-weight:800;float:left;font-size:4.2em;line-height:.8;padding:.06em .1em 0 0;color:var(--accent-t)}"
                ".hero .ph,.split .ph{box-shadow:14px 14px 0 var(--bg2)}.float{border:1px solid var(--ink);border-radius:0;box-shadow:none}.formcard{border:1px solid var(--ink);box-shadow:10px 10px 0 var(--bg2)}",
    "retro_scrapbook": ".ph{border:10px solid #FBF6EA;border-bottom-width:34px}.av,.auth .ph,.tile .ph{border:0}"
                       ".cards .card,.qt figure.card{position:relative}.cards .card::after,.qt figure.card::after{content:\"\";position:absolute;top:-12px;left:50%;width:84px;height:24px;translate:-50% 0;rotate:-3deg;background:rgba(242,193,78,.8)}"
                       ".float{border:2px dashed var(--ink);border-radius:10px;box-shadow:4px 4px 0 rgba(43,33,24,.9)}.formcard{border:2px solid var(--ink)}",
}
