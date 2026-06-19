import re, json

TEMPLATE = r'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root{{--bg:#0b1120;--line:#24314d;--text:#e8eefc;--muted:#8aa0c6;--accent:#38bdf8;--card:#13203b}}
  *{{box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
  html,body{{margin:0;min-height:100%;background:radial-gradient(1200px 800px at 70% -10%,#16233f,transparent),var(--bg);
    color:var(--text);font-family:'Segoe UI',Roboto,system-ui,Arial,sans-serif}}
  /* ===== DESKTOP: SVG tree ===== */
  @media(min-width:769px){{
    body{{overflow:hidden}}
    #mob{{display:none}}
  }}
  #top{{position:fixed;left:0;right:0;top:0;z-index:10;display:flex;align-items:center;gap:10px;flex-wrap:wrap;
    padding:10px 16px;background:linear-gradient(180deg,#0b1120ee,#0b112099);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}}
  #title{{display:flex;flex-direction:column;line-height:1.2}}
  #title b{{font-size:16px;letter-spacing:.3px}}
  #title span{{font-size:11px;color:var(--muted)}}
  .grow{{flex:1}}
  .btn{{background:#16233f;border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 12px;font-size:12px;cursor:pointer;white-space:nowrap;transition:.15s}}
  .btn:hover{{border-color:var(--accent);color:#fff}}
  #search{{background:#0b1428;border:1px solid var(--line);color:var(--text);border-radius:8px;padding:7px 12px;font-size:13px;min-width:140px;outline:none;flex:1;max-width:260px}}
  #search:focus{{border-color:var(--accent)}}
  .chip{{font-size:11px;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:4px 10px}}
  a.langlink{{color:var(--accent);font-size:12px;text-decoration:none;border:1px solid var(--line);border-radius:8px;padding:7px 12px;transition:.15s}}
  a.langlink:hover{{border-color:var(--accent);background:#16233f}}
  #stage{{position:fixed;inset:0;top:0;cursor:grab}}
  #stage.drag{{cursor:grabbing}}
  svg{{width:100%;height:100%;display:block}}
  .link{{fill:none;stroke-width:2}}
  .node-card{{cursor:pointer}}
  .nfo{{position:fixed;left:0;right:0;bottom:0;z-index:10;font-size:11px;color:var(--muted);text-align:center;padding:8px;background:linear-gradient(0deg,#0b1120ee,transparent)}}
  .fo-card{{height:100%;width:100%;display:flex;flex-direction:column;justify-content:center;border-radius:12px;padding:8px 12px;border:1px solid var(--line);background:linear-gradient(180deg,#13203b,#0e1830);box-shadow:0 6px 18px #0006;overflow:hidden}}
  .fo-card .t{{font-size:13px;font-weight:600;color:#eaf2ff;margin:0 0 3px;line-height:1.25}}
  .fo-card .d{{font-size:11px;color:var(--muted);line-height:1.3;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
  .fo-card .dt{{font-size:10px;color:#5f7099;margin-top:5px}}
  .fo-leaf{{transition:.12s}}
  .fo-leaf:hover{{border-color:var(--accent);transform:translateY(-1px)}}
  .fo-root{{align-items:center;text-align:center;border:1px solid #2b4a7a;background:linear-gradient(180deg,#1b2f55,#10203f)}}
  .fo-root .t{{font-size:18px}}
  .fo-cat{{align-items:flex-start}}
  .fo-cat .t{{font-size:14px;font-weight:700}}
  .badge{{display:inline-block;font-size:10px;color:#0b1120;border-radius:999px;padding:1px 8px;font-weight:700;margin-top:4px}}
  .dim{{opacity:.18}}
  .fo-card.hit{{outline:2px solid var(--accent);outline-offset:1px}}
  .toggle{{font-size:11px;color:#0b1120;font-weight:800}}
  /* ===== MOBILE: accordion list ===== */
  @media(max-width:768px){{
    #stage,.nfo{{display:none}}
    #top{{position:sticky;top:0}}
    .desk-only{{display:none!important}}
    body{{overflow:auto;padding-bottom:40px}}
  }}
  @media(min-width:769px){{#mob{{display:none}}}}
  #mob{{padding:80px 12px 40px}}
  .m-cat{{margin:0 0 6px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:var(--card)}}
  .m-cat-head{{display:flex;align-items:center;gap:10px;padding:14px 16px;cursor:pointer;-webkit-user-select:none;user-select:none}}
  .m-cat-head .ico{{font-size:22px}}
  .m-cat-head .h{{font-weight:700;font-size:15px;flex:1}}
  .m-cat-head .cnt{{font-size:11px;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 10px}}
  .m-cat-head .arrow{{font-size:14px;color:var(--muted);transition:.2s}}
  .m-cat.open .arrow{{transform:rotate(180deg)}}
  .m-items{{display:none;padding:0 10px 10px}}
  .m-cat.open .m-items{{display:block}}
  .m-item{{display:block;text-decoration:none;color:var(--text);border-radius:10px;padding:12px 14px;margin:6px 0;border:1px solid var(--line);background:#0e1830;transition:.12s}}
  .m-item:hover,.m-item:active{{border-color:var(--accent);background:#13203bcc}}
  .m-item .mt{{font-weight:600;font-size:14px;line-height:1.3;margin:0 0 4px}}
  .m-item .md{{font-size:12px;color:var(--muted);line-height:1.4}}
  .m-item .mdt{{font-size:10px;color:#5f7099;margin-top:6px}}
  .m-item.dim{{opacity:.18}}
  .m-item.hit{{outline:2px solid var(--accent);outline-offset:1px}}
  footer{{text-align:center;font-size:11px;color:var(--muted);padding:20px 16px;border-top:1px solid var(--line);margin-top:20px}}
</style>
</head>
<body>
<div id="top">
  <div id="title"><b>{header}</b><span>{sub}</span></div>
  <span class="chip" id="cnt"></span>
  <div class="grow"></div>
  <input id="search" placeholder="{search_ph}">
  <button class="btn desk-only" id="exp">{expand}</button>
  <button class="btn desk-only" id="col">{collapse}</button>
  <button class="btn desk-only" id="rst">{reset}</button>
  <a class="langlink" href="{other_href}">{other_label}</a>
</div>
<!-- DESKTOP SVG -->
<div id="stage"><svg id="svg"><g id="vp"></g></svg></div>
<div class="nfo">{hint}</div>
<!-- MOBILE ACCORDION -->
<div id="mob"></div>

<script>
const DATA = {data_json};
const S = {s_json};
const TOTAL = {total};
document.getElementById('cnt').textContent = TOTAL + ' ' + S.total;

/* ===== MOBILE ACCORDION ===== */
function renderMob() {{
  const mob = document.getElementById('mob');
  let h = '';
  DATA.forEach((cat, ci) => {{
    h += '<div class="m-cat open" data-ci="' + ci + '">';
    h += '<div class="m-cat-head" style="border-left:4px solid ' + cat.color + '">';
    h += '<span class="ico">' + cat.icon + '</span>';
    h += '<span class="h" style="color:' + cat.color + '">' + esc(cat.t) + '</span>';
    h += '<span class="cnt">' + cat.n + '</span>';
    h += '<span class="arrow">▼</span></div>';
    h += '<div class="m-items">';
    cat.children.forEach(leaf => {{
      h += '<a class="m-item" href="' + esc(leaf.u) + '" target="_blank" data-txt="' + esc((leaf.t + ' ' + leaf.d).toLowerCase()) + '">';
      h += '<div class="mt">' + esc(leaf.t) + '</div>';
      h += '<div class="md">' + esc(leaf.d) + '</div>';
      h += '<div class="mdt">' + (leaf.date || '') + ' · ' + S.open + '</div>';
      h += '</a>';
    }});
    h += '</div></div>';
  }});
  mob.innerHTML = h;
  mob.querySelectorAll('.m-cat-head').forEach(el => {{
    el.addEventListener('click', () => el.parentElement.classList.toggle('open'));
  }});
}}
if (window.innerWidth <= 768) renderMob();
window.addEventListener('resize', () => {{
  if (window.innerWidth <= 768 && !document.getElementById('mob').children.length) renderMob();
}});

/* ===== SEARCH (both modes) ===== */
const search = document.getElementById('search');
function applySearch() {{
  const q = search.value.trim().toLowerCase();
  document.querySelectorAll('.leaf, .m-item').forEach(el => {{
    const t = (el.getAttribute('data-txt') || '');
    const card = el.querySelector('.fo-card') || el;
    if (!q) {{ el.classList.remove('dim'); card.classList.remove('hit'); }}
    else if (t.includes(q)) {{ el.classList.remove('dim'); card.classList.add('hit'); }}
    else {{ el.classList.add('dim'); card.classList.remove('hit'); }}
  }});
}}
search.addEventListener('input', applySearch);

/* ===== DESKTOP SVG TREE ===== */
const ROOT_W=240,ROOT_H=80,CAT_W=240,CAT_H=64,LEAF_W=300,LEAF_H=92,COL_GAP=140,V_GAP=14;
const collapsed = {{}};
let nodes=[],links_=[];
function esc(s){{return(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}}
function layout(){{
  nodes=[];links_=[];
  const cats=DATA.map((c,i)=>({{...c,idx:i}}));
  let y=0;const catLayout=[];
  cats.forEach(c=>{{const vis=collapsed[c.idx]?0:c.children.length;const h=Math.max(1,vis)*(LEAF_H+V_GAP);catLayout.push({{c,y0:y,h,vis}});y+=h+30;}});
  const totalH=Math.max(y,ROOT_H+40);
  const xRoot=40,xCat=xRoot+ROOT_W+COL_GAP,xLeaf=xCat+CAT_W+COL_GAP;
  nodes.push({{id:"root",type:"root",x:xRoot,y:totalH/2-ROOT_H/2,w:ROOT_W,h:ROOT_H,t:S.root}});
  catLayout.forEach(cl=>{{
    const cy=cl.y0+cl.h/2-CAT_H/2,cid="c"+cl.c.idx;
    nodes.push({{id:cid,type:"cat",x:xCat,y:cy,w:CAT_W,h:CAT_H,t:cl.c.t,color:cl.c.color,icon:cl.c.icon,n:cl.c.n,idx:cl.c.idx}});
    links_.push({{a:"root",b:cid,color:cl.c.color}});
    if(!collapsed[cl.c.idx]){{let ly=cl.y0;
      cl.c.children.forEach((leaf,j)=>{{const lid=cid+"_"+j;nodes.push({{id:lid,type:"leaf",x:xLeaf,y:ly,w:LEAF_W,h:LEAF_H,leaf,color:cl.c.color}});links_.push({{a:cid,b:lid,color:cl.c.color}});ly+=LEAF_H+V_GAP;}});
    }}
  }});
  return{{totalH,width:xLeaf+LEAF_W+60}};
}}
const vp=document.getElementById('vp'),svg=document.getElementById('svg');
function nodeById(id){{return nodes.find(n=>n.id===id);}}
function edgePath(a,b){{const x1=a.x+a.w,y1=a.y+a.h/2,x2=b.x,y2=b.y+b.h/2,mx=(x1+x2)/2;return`M${{x1}},${{y1}} C${{mx}},${{y1}} ${{mx}},${{y2}} ${{x2}},${{y2}}`;}}
function render(){{
  layout();let h='';
  links_.forEach(l=>{{const a=nodeById(l.a),b=nodeById(l.b);if(a&&b)h+=`<path class="link" d="${{edgePath(a,b)}}" style="stroke:${{l.color}}55"></path>`;}});
  nodes.forEach(n=>{{
    if(n.type==='root'){{
      h+=`<foreignObject x="${{n.x}}" y="${{n.y}}" width="${{n.w}}" height="${{n.h}}"><div xmlns="http://www.w3.org/1999/xhtml" class="fo-card fo-root"><div class="t">${{esc(n.t)}}</div></div></foreignObject>`;
    }}else if(n.type==='cat'){{
      const sign=collapsed[n.idx]?'＋':'－';
      h+=`<foreignObject class="node-card" data-cat="${{n.idx}}" x="${{n.x}}" y="${{n.y}}" width="${{n.w}}" height="${{n.h}}"><div xmlns="http://www.w3.org/1999/xhtml" class="fo-card fo-cat" style="border-color:${{n.color}}88"><div class="t" style="color:${{n.color}}">${{n.icon}} ${{esc(n.t)}}</div><span class="badge" style="background:${{n.color}}">${{n.n}} · <span class="toggle">${{sign}}</span></span></div></foreignObject>`;
    }}else{{
      h+=`<foreignObject class="node-card leaf" data-url="${{esc(n.leaf.u)}}" data-txt="${{esc((n.leaf.t+' '+n.leaf.d).toLowerCase())}}" x="${{n.x}}" y="${{n.y}}" width="${{n.w}}" height="${{n.h}}"><div xmlns="http://www.w3.org/1999/xhtml" class="fo-card fo-leaf" style="border-left:3px solid ${{n.color}}"><div class="t">${{esc(n.leaf.t)}}</div><div class="d">${{esc(n.leaf.d)}}</div><div class="dt">${{n.leaf.date?esc(n.leaf.date)+' · ':''}}\${{S.open}}</div></div></foreignObject>`;
    }}
  }});
  vp.innerHTML=h;
  bindNodes();applySearch();
}}
function bindNodes(){{
  vp.querySelectorAll('[data-cat]').forEach(el=>el.addEventListener('click',e=>{{e.stopPropagation();const i=+el.getAttribute('data-cat');collapsed[i]=!collapsed[i];render();}}));
  vp.querySelectorAll('.leaf').forEach(el=>el.addEventListener('click',e=>{{e.stopPropagation();const u=el.getAttribute('data-url');if(u)window.open(u,'_blank');}}));
}}
let tx=0,ty=70,scale=1;
function applyVP(){{vp.setAttribute('transform',`translate(${{tx}},${{ty}}) scale(${{scale}})`);}}
function fit(){{const dim=layout();const vw=window.innerWidth,vh=window.innerHeight-80;scale=Math.min(1,Math.min(vw/(dim.width+40),vh/(dim.totalH+40)));if(!isFinite(scale)||scale<=0)scale=1;tx=20;ty=80+Math.max(0,(vh-dim.totalH*scale)/2);applyVP();}}
const stage=document.getElementById('stage');
let drag=false,sx,sy,stx,sty;
stage.addEventListener('mousedown',e=>{{drag=true;stage.classList.add('drag');sx=e.clientX;sy=e.clientY;stx=tx;sty=ty;}});
window.addEventListener('mousemove',e=>{{if(!drag)return;tx=stx+(e.clientX-sx);ty=sty+(e.clientY-sy);applyVP();}});
window.addEventListener('mouseup',()=>{{drag=false;stage.classList.remove('drag');}});
stage.addEventListener('wheel',e=>{{e.preventDefault();const f=e.deltaY<0?1.12:0.89;const r=svg.getBoundingClientRect();const mx=e.clientX-r.left,my=e.clientY-r.top;const ns=Math.max(.25,Math.min(2.5,scale*f));tx=mx-(mx-tx)*(ns/scale);ty=my-(my-ty)*(ns/scale);scale=ns;applyVP();}},{{passive:false}});
let pinch=null,ps=1;
stage.addEventListener('touchstart',e=>{{if(e.touches.length===1){{drag=true;sx=e.touches[0].clientX;sy=e.touches[0].clientY;stx=tx;sty=ty;}}else if(e.touches.length===2){{pinch=dist(e);ps=scale;}}}},{{passive:true}});
stage.addEventListener('touchmove',e=>{{if(e.touches.length===1&&drag){{tx=stx+(e.touches[0].clientX-sx);ty=sty+(e.touches[0].clientY-sy);applyVP();}}else if(e.touches.length===2&&pinch){{const d=dist(e);scale=Math.max(.25,Math.min(2.5,ps*d/pinch));applyVP();}}}},{{passive:true}});
stage.addEventListener('touchend',()=>{{drag=false;pinch=null;}});
function dist(e){{const a=e.touches[0],b=e.touches[1];return Math.hypot(a.clientX-b.clientX,a.clientY-b.clientY);}}
document.getElementById('exp').onclick=()=>{{DATA.forEach((c,i)=>collapsed[i]=false);render();}};
document.getElementById('col').onclick=()=>{{DATA.forEach((c,i)=>collapsed[i]=true);render();}};
document.getElementById('rst').onclick=()=>{{search.value='';render();fit();}};
if(window.innerWidth>768){{render();fit();}}
window.addEventListener('resize',()=>{{if(window.innerWidth>768)applyVP();}});
</script>
</body>
</html>'''

for fn, lang, title, header, sub, search_ph, expand, collapse, reset, hint, other_href, other_label, open_label in [
    ('docs/mindmap-en.html', 'en', 'P2P · Useful Posts', 'P2P · Useful Posts',
     "Curated map of Sanic27's publications · 4PDA", 'Search posts…',
     'Expand all', 'Collapse all', 'Reset view',
     'Click a branch to fold/unfold · click a post to open it on 4PDA · wheel to zoom · drag to pan',
     'mindmap-ru.html', 'Русская версия', 'Open post ↗'),
    ('docs/mindmap-ru.html', 'ru', 'P2P · Полезные посты', 'P2P · Полезные посты',
     'Карта публикаций Sanic27 · 4PDA', 'Поиск постов…',
     'Развернуть', 'Свернуть', 'Сбросить',
     'Клик по ветке — свернуть/развернуть · клик по посту — открыть на 4PDA · колесо — зум · перетаскивание',
     'mindmap-en.html', 'English version', 'Открыть пост ↗'),
]:
    src = open(fn, encoding='utf-8').read()
    data_m = re.search(r'const DATA = (\[.*?\]);', src)
    data_json = data_m.group(1)
    data = json.loads(data_json)
    total = sum(c.get('n', len(c.get('children',[]))) for c in data)

    s_obj = {"root": header, "sub": sub, "search": search_ph, "expand": expand, "collapse": collapse, "hint": hint, "total": "posts" if lang=='en' else "постов", "other": other_label, "reset": reset, "open": open_label, "thread": "Thread Prompts for Artificial Intelligence · 4PDA" if lang=='en' else "Промпты для Искусственного Интеллекта · 4PDA"}
    s_json = json.dumps(s_obj, ensure_ascii=False)

    html = TEMPLATE.format(
        lang=lang, title=title, header=header, sub=sub, search_ph=search_ph,
        expand=expand, collapse=collapse, reset=reset, hint=hint,
        other_href=other_href, other_label=other_label,
        data_json=data_json, s_json=s_json, total=total
    )
    open(fn, 'w', encoding='utf-8').write(html)
    print(f'{fn}: written {len(html)} bytes, {total} posts')
