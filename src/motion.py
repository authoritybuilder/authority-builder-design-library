"""Movement. One stylesheet and one small script shared by every site.

The rules it follows:
- Movement has a job: it shows what arrived, what answers the pointer and where the main action is. Nothing moves for decoration.
  No count-up numbers, no tickers, no tilting cards, no light following the pointer, no shine across buttons.
- Nothing is hidden unless the script is running, so a page with scripts off, and every crawler, sees all of it.
- The first screen is never touched. Only sections below it reveal as they scroll in, so the largest element paints straight away.
- Only transform, opacity and clip-path are animated. Layout never moves.
- A visitor who asks for reduced motion gets none of it.

Each site picks 1 of 4 quiet reveal styles (the data-m attribute on the html element) in src/variants.py.
"""

MOTION_CSS = r"""
/* the header steps aside on the way down and comes back on the way up */
.hdw{transition:transform .4s cubic-bezier(.2,.7,.2,1)}.down .hdw{transform:translateY(-120%)}
/* the action dock: on a desktop the main button follows the reader once the hero has gone, and leaves when the closing section arrives */
@media(min-width:761px){
.js .sticky{display:flex;left:auto;right:clamp(14px,2vw,26px);bottom:clamp(14px,2vw,26px);max-width:430px;gap:1.1rem;padding:.6rem .6rem .6rem 1.25rem;border:max(1px,var(--bw)) solid var(--line);
border-radius:min(calc(var(--rb) + 0px),40px);box-shadow:0 20px 44px -24px rgba(0,0,0,.45);transform:translateY(160%);transition:transform .5s cubic-bezier(.2,.8,.2,1);visibility:hidden}
.js.past:not(.end) .sticky{transform:none;visibility:visible}
}
@media(max-width:760px){.sticky.desk{display:none}.sticky{transition:transform .4s}.js.end .sticky{transform:translateY(120%)}}
@media(prefers-reduced-motion:no-preference){
/* reveal on scroll: short, quiet, once. The script marks only what starts below the first screen */
[data-rv]{opacity:0;transition:opacity .5s ease-out,transform .6s cubic-bezier(.2,.7,.2,1),clip-path .7s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--d,0)*50ms)}
[data-rv].in{opacity:1!important;transform:none!important;clip-path:inset(-40px)!important}
[data-m=rise] [data-rv]{transform:translateY(20px)}
[data-m=slide] [data-rv]{transform:translateX(-20px)}
[data-m=clip] [data-rv]{clip-path:inset(0 0 100% 0);transform:translateY(12px)}
@media(max-width:760px){[data-m=slide] [data-rv]{transform:translateY(20px)}}
/* the painting settles into place as the page opens */
.hero picture.art{animation:settle 2.2s cubic-bezier(.2,.7,.2,1) both}@keyframes settle{from{transform:scale(1.05)}}
.btn:active{transform:translateY(1px)}
/* pictures: a slow zoom under the pointer and a slight drift as they cross the screen */
.ph img{transition:scale 1.1s cubic-bezier(.2,.7,.2,1)}.ph:hover img{scale:1.04}
@supports(animation-timeline:view()){
.sp-v .ph.photo img,.feature .ph.photo img,.mos .ph img{animation:par linear both;animation-timeline:view();animation-range:cover}@keyframes par{from{translate:0 -3%}to{translate:0 3%}}
.sp-v .ph.photo img,.feature .ph.photo img{scale:1.08}
.band picture.art img{animation:bandpar linear both;animation-timeline:view();animation-range:cover}@keyframes bandpar{from{transform:scale(1.14) translateY(-4%)}to{transform:scale(1.14) translateY(4%)}}
}
/* answers open smoothly where the browser can animate to an automatic height */
@supports(interpolate-size:allow-keywords){
.faq details,.mod details{interpolate-size:allow-keywords}
.faq details::details-content,.mod details::details-content{block-size:0;overflow:clip;transition:block-size .4s cubic-bezier(.2,.7,.2,1),content-visibility .4s allow-discrete}
.faq details[open]::details-content,.mod details[open]::details-content{block-size:auto}
}
}
@media print{.sticky{display:none}}
"""

# What reveals. Each item arrives on its own, a beat after the one before it.
REVEAL = (".sh,.grid>*,.stp>li,.fd-l>li,.sch>li,.sp-g>*,.cmp>*,.st-g>*,.mod details,.faq details,.wall>figure,.feature>*,.pr-1>*,.pr-q,.pr-a,.mt-g>*,.mxw,"
          ".gu .card,.sw-g>*,.posts>*,.cap .wrap>*,.cta .wrap>*,.trust li,.bn>.tile,.band .bd-c>*,.mos>*,.lb-l a,.prose .wrap>*,.art .wrap>*")

MOTION_JS = r"""<script>
/* Movement only. Every word on this page is in the HTML above, so nothing here is needed to read it. Delete this block and the page still works. */
(function(){var d=document,R=d.documentElement,W=window,q=function(s,c){return [].slice.call((c||d).querySelectorAll(s))};R.classList.add('js');
if(!('IntersectionObserver'in W))return;
var hero=d.querySelector('main>.sec'),E=q('main>.cta,.ft');
if(hero)new IntersectionObserver(function(e){R.classList.toggle('past',!e[0].isIntersecting)}).observe(hero);
var eo=new IntersectionObserver(function(es){es.forEach(function(e){e.target._v=e.isIntersecting});R.classList.toggle('end',E.some(function(x){return x._v}))});
E.forEach(function(x){eo.observe(x)});
var ly=W.scrollY;W.addEventListener('scroll',function(){var y=W.scrollY;R.classList.toggle('down',y>ly&&y>600);ly=y},{passive:true});
if(W.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
/* positions are read directly, not with an observer: an observer cannot see an element that a clip-path is still hiding */
var vh=W.innerHeight,todo=[],tick=0;
function show(){tick=0;vh=W.innerHeight;todo=todo.filter(function(t){if(t.getBoundingClientRect().top>vh*.96)return 1;t.classList.add('in');
setTimeout(function(){t.removeAttribute('data-rv');t.classList.remove('in');t.style.removeProperty('--d')},1200)})}
q('__REVEAL__').forEach(function(el){if(el.closest('.hero,.hdw,.sticky,[data-rv]')||el.getBoundingClientRect().top<vh*.94)return;
el.style.setProperty('--d',[].indexOf.call(el.parentNode.children,el)%4);q('img[loading=lazy]',el).forEach(function(i){i.loading='eager'});el.setAttribute('data-rv','');todo.push(el)});
function ask(){if(!tick&&todo.length)tick=W.requestAnimationFrame(show)}W.addEventListener('scroll',ask,{passive:true});W.addEventListener('resize',ask);
})();
</script>""".replace("__REVEAL__", REVEAL)
