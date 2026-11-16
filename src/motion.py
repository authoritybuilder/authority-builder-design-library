"""Movement. One stylesheet and one small script shared by every site.

The rules it follows:
- Nothing is hidden unless the script is running, so a page with scripts off, and every crawler, sees all of it.
- The first screen is never touched. Only sections below it reveal as they scroll in, so the largest element paints straight away.
- Only transform, opacity, clip-path and filter are animated. Layout never moves.
- A visitor who asks for reduced motion gets none of it.

Each site picks 1 reveal style (the data-m attribute on the html element) in src/variants.py.
"""

MOTION_CSS = r"""
/* scroll progress: a thin bar in the brand colour, drawn by the browser's own scroll timeline */
.prog{position:fixed;inset:0 0 auto 0;height:3px;z-index:40;background:var(--accent);transform-origin:0 50%;transform:scaleX(0);pointer-events:none}
@supports(animation-timeline:scroll()){.prog{animation:prog linear both;animation-timeline:scroll(root)}@keyframes prog{to{transform:scaleX(1)}}}
/* the header steps aside on the way down and comes back on the way up */
.hdw{transition:transform .4s cubic-bezier(.2,.7,.2,1)}.down .hdw{transform:translateY(-120%)}
/* the action dock: on a desktop the main button follows the reader once the hero has gone, and leaves when the closing section arrives */
@media(min-width:761px){
.js .sticky{display:flex;left:auto;right:clamp(14px,2vw,26px);bottom:clamp(14px,2vw,26px);max-width:430px;gap:1.1rem;padding:.6rem .6rem .6rem 1.25rem;border:max(1px,var(--bw)) solid var(--line);
border-radius:min(calc(var(--rb) + 0px),40px);box-shadow:0 26px 56px -22px rgba(0,0,0,.5);transform:translateY(160%);transition:transform .55s cubic-bezier(.2,.8,.2,1);visibility:hidden}
.js.past:not(.end) .sticky{transform:none;visibility:visible}
}
@media(max-width:760px){.sticky.desk{display:none}.sticky{transition:transform .4s}.js.end .sticky{transform:translateY(120%)}}
@media(prefers-reduced-motion:no-preference){
/* reveal on scroll. The script marks only what starts below the first screen */
[data-rv]{opacity:0;transition:opacity .55s cubic-bezier(.2,.7,.2,1),transform .75s cubic-bezier(.2,.7,.2,1),clip-path .8s cubic-bezier(.2,.7,.2,1),filter .6s;transition-delay:calc(var(--d,0)*60ms);will-change:transform,opacity}
[data-rv].in{opacity:1!important;transform:none!important;clip-path:inset(-40px)!important;filter:none!important}
[data-m=rise] [data-rv]{transform:translateY(38px)}
[data-m=slide] [data-rv]{transform:translateX(-46px)}[data-m=slide] [data-rv]:nth-child(even){transform:translateX(46px)}
@media(max-width:760px){[data-m=slide] [data-rv],[data-m=slide] [data-rv]:nth-child(even){transform:translateY(30px)}}
[data-m=zoom] [data-rv]{transform:scale(.9)}
[data-m=clip] [data-rv]{clip-path:inset(0 0 100% 0);transform:translateY(22px)}
[data-m=blur] [data-rv]{filter:blur(16px);transform:translateY(18px)}
[data-m=flip] [data-rv]{transform:perspective(1000px) rotateX(22deg) translateY(34px);transform-origin:50% 0}
[data-m=pop] [data-rv]{transform:scale(.78) rotate(-2.5deg);transition-timing-function:cubic-bezier(.2,.7,.2,1),cubic-bezier(.34,1.56,.64,1),ease,ease}
[data-m=drift] [data-rv]{transform:translateY(64px) rotate(1.6deg)}
/* the painting settles into place as the page opens */
.hero picture.art{animation:settle 2.6s cubic-bezier(.2,.7,.2,1) both}@keyframes settle{from{transform:scale(1.09)}}
/* a light crosses the main button on hover */
.btn:not(.ghost){position:relative;overflow:hidden}
.btn:not(.ghost)::before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,transparent 34%,rgba(255,255,255,.38) 50%,transparent 66%);translate:-130% 0;transition:translate .75s ease;pointer-events:none}
.btn:not(.ghost):hover::before{translate:130% 0}
.btn:active{transform:translateY(1px) scale(.98)}
/* pictures breathe: a slow zoom on hover and a drift as they cross the screen */
.ph img{transition:scale 1.1s cubic-bezier(.2,.7,.2,1)}.ph:hover img{scale:1.06}
@supports(animation-timeline:view()){
.sp-v .ph.photo img,.feature .ph.photo img,.mos .ph img{animation:par linear both;animation-timeline:view();animation-range:cover}@keyframes par{from{translate:0 -3.5%}to{translate:0 3.5%}}
.sp-v .ph.photo img,.feature .ph.photo img{scale:1.09}
.band picture.art img{animation:bandpar linear both;animation-timeline:view();animation-range:cover}@keyframes bandpar{from{transform:scale(1.16) translateY(-5%)}to{transform:scale(1.16) translateY(5%)}}
}
/* answers open smoothly where the browser can animate to an automatic height */
@supports(interpolate-size:allow-keywords){
.faq details,.mod details{interpolate-size:allow-keywords}
.faq details::details-content,.mod details::details-content{block-size:0;overflow:clip;transition:block-size .45s cubic-bezier(.2,.7,.2,1),content-visibility .45s allow-discrete}
.faq details[open]::details-content,.mod details[open]::details-content{block-size:auto}
}
.faq summary::after,.mod summary::after{transition:rotate .3s}.faq details[open] summary::after,.mod details[open] summary::after{rotate:180deg}
/* links and list rows answer the pointer */
.fd-l li,.sch li,.stp li{transition:padding-left .3s cubic-bezier(.2,.7,.2,1)}.fd-l li:hover{padding-left:.6rem}
.lb-l a,.door,.tier{will-change:translate}
.tier:hover{translate:0 -6px}.tier.hot:hover{translate:0 -14px}
.av{transition:scale .3s}.crowd:hover .av{scale:1.06}
/* the proof strip can run as a slow ticker (data-mq). It pauses under the pointer */
.mq{overflow:hidden;flex:1 1 100%;min-width:0;-webkit-mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);mask-image:linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent)}
.logos .mq ul{flex-wrap:nowrap;width:max-content;justify-content:flex-start;gap:0;animation:mq 38s linear infinite}.logos .mq li{padding-inline:1.5rem;white-space:nowrap}
.mq:hover ul{animation-play-state:paused}@keyframes mq{to{transform:translateX(-50%)}}
/* cards can follow the pointer with a soft light (data-spot) or a slight tilt (data-tilt) */
[data-spot] .card:not(.float),[data-spot] .tile{background-image:radial-gradient(280px circle at var(--mx,-999px) var(--my,-999px),color-mix(in srgb,var(--accent) 16%,transparent),transparent 72%)}
[data-tilt] .cards .card:hover,[data-tilt] .door:hover,[data-tilt] .qt figure.card:hover,[data-tilt] .tile:hover{transform:perspective(900px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:transform .12s linear}
}
@media print{.prog,.sticky{display:none}}
"""

# What reveals. Each item fades and moves in on its own, a beat after the one before it.
REVEAL = (".sh,.grid>*,.stp>li,.fd-l>li,.sch>li,.sp-g>*,.cmp>*,.st-g>*,.mod details,.faq details,.wall>figure,.feature>*,.pr-1>*,.pr-q,.pr-a,.mt-g>*,.mxw,"
          ".gu .card,.cap .wrap>*,.cta .wrap>*,.trust li,.bn>.tile,.band .bd-c>*,.mos>*,.lb-l a,.prose .wrap>*,.art .wrap>*")

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
function show(){tick=0;vh=W.innerHeight;todo=todo.filter(function(t){if(t.getBoundingClientRect().top>vh*.95)return 1;t.classList.add('in');
setTimeout(function(){t.removeAttribute('data-rv');t.classList.remove('in');t.style.removeProperty('--d')},1500)})}
q('__REVEAL__').forEach(function(el){if(el.closest('.hero,.hdw,.sticky,[data-rv]')||el.getBoundingClientRect().top<vh*.94)return;
el.style.setProperty('--d',[].indexOf.call(el.parentNode.children,el)%6);q('img[loading=lazy]',el).forEach(function(i){i.loading='eager'});el.setAttribute('data-rv','');todo.push(el)});
function ask(){if(!tick&&todo.length)tick=W.requestAnimationFrame(show)}W.addEventListener('scroll',ask,{passive:true});W.addEventListener('resize',ask);
var co=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var b=e.target;co.unobserve(b);
var m=b.textContent.match(/^(\D*)(\d[\d,]*\.?\d*)([\s\S]*)$/);if(!m)return;var n=parseFloat(m[2].replace(/,/g,'')),dp=(m[2].split('.')[1]||'').length,cm=m[2].indexOf(',')>-1,t0=0;
if(!cm&&!dp&&n>1900&&n<2100)return;
W.requestAnimationFrame(function f(t){t0=t0||t;var p=Math.min(1,(t-t0)/1400),s=(n*(1-Math.pow(1-p,3))).toFixed(dp);if(cm)s=s.replace(/\B(?=(\d{3})+(?!\d))/g,',');
b.textContent=m[1]+s+m[3];if(p<1)W.requestAnimationFrame(f)})})},{threshold:.5});
q('.st-g b,.tile .big').forEach(function(b){if(!b.children.length&&b.getBoundingClientRect().top>vh*.94)co.observe(b)});
if(R.hasAttribute('data-mq'))q('.logos ul').forEach(function(u){var w=d.createElement('div');w.className='mq';u.parentNode.insertBefore(w,u);w.appendChild(u);
q('li',u).forEach(function(li){var c=li.cloneNode(true);c.setAttribute('aria-hidden','true');u.appendChild(c)})});
if(R.hasAttribute('data-spot')||R.hasAttribute('data-tilt'))d.addEventListener('pointermove',function(e){var c=e.target.closest&&e.target.closest('.card,.tile');if(!c)return;
var r=c.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top,s=c.style;s.setProperty('--mx',x+'px');s.setProperty('--my',y+'px');
s.setProperty('--rx',((y/r.height-.5)*-5).toFixed(2)+'deg');s.setProperty('--ry',((x/r.width-.5)*5).toFixed(2)+'deg')},{passive:true});
})();
</script>""".replace("__REVEAL__", REVEAL)
