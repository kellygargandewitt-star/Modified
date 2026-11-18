// Shared code for fluency kits. Needs ../sam_the_spider/art.js loaded first
// (it provides sky, ground, sun, cloud, heart, sparkle, bubble, speech, panelSVG, iconSVG, applyColoring).

const P = s => ({ h: H, s });

// ---------- people ----------
function person(o){
  const s = o.s || 1, skin = o.skin || '#f2c9a0', skinDk = '#c99a74';
  let hair = o.hair || '#5a3a1e', shirt = o.shirt || '#3a8fc4', pants = o.pants || '#33415c', shoe = o.shoe || '#333';
  if (o.gear){ shirt = '#e5b52a'; pants = '#e5b52a'; shoe = '#222'; }
  const ARMS = {
    down:  [[24,-60],[22,-44]],
    up:    [[26,-96],[30,-114]],
    wave:  [[34,-80],[34,-108]],
    point: [[34,-80],[50,-82]],
    hip:   [[34,-66],[18,-52]],
    front: [[30,-64],[24,-58]],
    cheer: [[30,-96],[24,-118]],
    face:  [[24,-80],[8,-96]],
  };
  const ra = ARMS[o.arms || 'down'], la = ARMS[o.armsL || o.arms || 'down'];
  let g = '';
  if (o.tank) g += `<rect x="-14" y="-88" width="28" height="44" rx="10" fill="#9aa3ad" stroke="#59616a" stroke-width="2"/>`;
  // legs
  for (const sd of [-1,1]) {
    g += `<path d="M${7*sd} -44 L${9*sd} -6" stroke="${pants}" stroke-width="11" stroke-linecap="round"/>`;
    g += `<ellipse cx="${11*sd}" cy="-3" rx="${o.gear?10:8}" ry="${o.gear?6:4.5}" fill="${shoe}"/>`;
    if (o.gear) g += `<path d="M${4*sd} -22 L${14*sd} -22" stroke="#e8e8e8" stroke-width="4"/>`;
  }
  // body
  if (o.dress) g += `<path d="M-15 -84 H15 L24 -36 H-24 Z" fill="${shirt}" stroke="#00000033" stroke-width="2" stroke-linejoin="round"/>`;
  else g += `<rect x="-16" y="-84" width="32" height="44" rx="9" fill="${shirt}" stroke="#00000033" stroke-width="2"/>`;
  if (o.gear) g += `<rect x="-16" y="-62" width="32" height="5" fill="#e8e8e8" stroke="#999" stroke-width="1"/><rect x="-16" y="-50" width="32" height="5" fill="#e8e8e8" stroke="#999" stroke-width="1"/><line x1="0" y1="-84" x2="0" y2="-40" stroke="#b8901a" stroke-width="2"/>`;
  // arms
  for (const [sd, a] of [[1, ra], [-1, la]]) {
    const [c, h] = a;
    g += `<path d="M${16*sd} -78 Q ${c[0]*sd} ${c[1]} ${h[0]*sd} ${h[1]}" stroke="${shirt}" stroke-width="9" fill="none" stroke-linecap="round"/>`;
    g += `<circle cx="${h[0]*sd}" cy="${h[1]}" r="${o.gear?5.5:4.5}" fill="${o.gear?'#333':skin}"/>`;
  }
  // head
  g += `<circle cx="0" cy="-100" r="16" fill="${skin}" stroke="${skinDk}" stroke-width="1.5"/>`;
  const hs = o.hairStyle || 'short';
  if (!o.helmet){
    if (hs === 'long' || hs === 'pony') g += `<path d="M-17 -104 Q -22 -80 -14 -78 L -12 -100 Z M17 -104 Q 22 -80 14 -78 L 12 -100 Z" fill="${hair}"/>`;
    if (hs === 'pony') g += `<circle cx="-19" cy="-110" r="7" fill="${hair}"/>`;
    if (hs === 'bun') g += `<circle cx="0" cy="-121" r="8" fill="${hair}"/>`;
    if (hs === 'curly') for (const [x,y] of [[-14,-108],[-8,-116],[0,-118],[8,-116],[14,-108],[-17,-100],[17,-100]]) g += `<circle cx="${x}" cy="${y}" r="7" fill="${hair}"/>`;
    else g += `<path d="M-16.5 -102 Q -17 -119 0 -119 Q 17 -119 16.5 -102 Q 9 -110 -2 -108 Q -10 -107 -16.5 -102 Z" fill="${hair}"/>`;
  }
  // face
  g += `<circle cx="-5.5" cy="-101" r="2.1" fill="#111"/><circle cx="5.5" cy="-101" r="2.1" fill="#111"/>`;
  if (o.glasses) g += `<circle cx="-5.5" cy="-101" r="5" fill="none" stroke="#333" stroke-width="1.5"/><circle cx="5.5" cy="-101" r="5" fill="none" stroke="#333" stroke-width="1.5"/><line x1="-0.5" y1="-101" x2="0.5" y2="-101" stroke="#333" stroke-width="1.5"/>`;
  const m = o.mood || 'happy';
  if (m === 'happy') g += `<path d="M-6 -93 Q 0 -88 6 -93" stroke="#7a2d2d" stroke-width="2" fill="none" stroke-linecap="round"/>`;
  if (m === 'excited') g += `<path d="M-7 -94 Q 0 -84 7 -94 Z" fill="#c9304a" stroke="#7a2d2d" stroke-width="1.5" stroke-linejoin="round"/>`;
  if (m === 'talk') g += `<ellipse cx="0" cy="-92" rx="3.5" ry="3" fill="#c9304a" stroke="#7a2d2d" stroke-width="1.2"/>`;
  if (m === 'worried') g += `<path d="M-5 -91 Q 0 -95 5 -91" stroke="#7a2d2d" stroke-width="2" fill="none" stroke-linecap="round"/>`;
  g += `<circle cx="-10" cy="-95" r="2.8" fill="#ff8a8a" opacity="0.6"/><circle cx="10" cy="-95" r="2.8" fill="#ff8a8a" opacity="0.6"/>`;
  if (o.mask) g += `<ellipse cx="0" cy="-97" rx="15" ry="16" fill="#bfe3f5" fill-opacity="0.55" stroke="#333" stroke-width="2.5"/><circle cx="0" cy="-86" r="4" fill="#555"/>`;
  if (o.helmet) g += `<path d="M-20 -104 Q -19 -129 0 -129 Q 19 -129 20 -104 Z" fill="#d62828" stroke="#8f1515" stroke-width="2"/><ellipse cx="0" cy="-104" rx="25" ry="5" fill="#d62828" stroke="#8f1515" stroke-width="2"/><path d="M-6 -126 H6 V-112 L0 -108 L-6 -112 Z" fill="#ffd23f" stroke="#b8901a" stroke-width="1.5"/>`;
  if (o.cap) g += `<path d="M-17 -106 Q -16 -124 0 -124 Q 16 -124 17 -106 Z" fill="${o.cap}" stroke="#00000055" stroke-width="1.5"/><path d="M10 -107 Q 26 -110 30 -104 Q 20 -102 10 -104 Z" fill="${o.cap}" stroke="#00000055" stroke-width="1.5"/>`;
  const rot = o.rot ? ` rotate(${o.rot} 0 -60)` : '';
  return `<g transform="translate(${o.x} ${o.y}) scale(${s})${rot}">${g}</g>`;
}

// ---------- shared objects ----------
function house(x,y,s=1,c='#f0b56a'){
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <rect x="-34" y="-48" width="68" height="48" fill="${c}" stroke="#7a4f22" stroke-width="2"/>
    <path d="M-42 -46 L0 -80 L42 -46 Z" fill="#c0392b" stroke="#7a1f16" stroke-width="2" stroke-linejoin="round"/>
    <rect x="-8" y="-28" width="16" height="28" fill="#8b5a2b" stroke="#5a3a1e" stroke-width="2"/>
    <rect x="-28" y="-40" width="14" height="13" fill="#bfe6ff" stroke="#5a3a1e" stroke-width="2"/><rect x="14" y="-40" width="14" height="13" fill="#bfe6ff" stroke="#5a3a1e" stroke-width="2"/></g>`;
}
function tree(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-6" y="-40" width="12" height="40" fill="#8b5a2b" stroke="#5a3a1e" stroke-width="2"/>
    <circle cx="0" cy="-58" r="26" fill="#5cb85c" stroke="#3d7f3d" stroke-width="2"/><circle cx="-18" cy="-44" r="15" fill="#5cb85c" stroke="#3d7f3d" stroke-width="2"/><circle cx="18" cy="-44" r="15" fill="#5cb85c" stroke="#3d7f3d" stroke-width="2"/></g>`;
}
function noSign(x,y,r){
  const d = r*0.7071;
  return `<circle cx="${x}" cy="${y}" r="${r}" fill="none" stroke="#e02424" stroke-width="${f(r*0.16)}"/><line x1="${f(x-d)}" y1="${f(y-d)}" x2="${f(x+d)}" y2="${f(y+d)}" stroke="#e02424" stroke-width="${f(r*0.16)}"/>`;
}
function arrow(x1,y1,x2,y2,c='#2b2b2b',w=4){
  const a = Math.atan2(y2-y1, x2-x1), L = 11;
  const p1 = [x2 - L*Math.cos(a-0.5), y2 - L*Math.sin(a-0.5)], p2 = [x2 - L*Math.cos(a+0.5), y2 - L*Math.sin(a+0.5)];
  return `<path d="M${x1} ${y1} L${x2} ${y2} M${f(p1[0])} ${f(p1[1])} L${x2} ${y2} L${f(p2[0])} ${f(p2[1])}" stroke="${c}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`;
}
function label(x,y,t,size=16,c='#222',anchor='middle'){
  return `<text x="${x}" y="${y}" text-anchor="${anchor}" font-family="Andika" font-weight="700" font-size="${size}" fill="${c}">${t}</text>`;
}
function snowflake(x,y,r=7){
  let s='';
  for (let a=0;a<3;a++){ const t=a*60*Math.PI/180; s += `<line x1="${f(x-r*Math.cos(t))}" y1="${f(y-r*Math.sin(t))}" x2="${f(x+r*Math.cos(t))}" y2="${f(y+r*Math.sin(t))}" stroke="#5aa9d6" stroke-width="2" stroke-linecap="round"/>`; }
  return s;
}
function drop(x,y,s=1){ return `<path transform="translate(${x} ${y}) scale(${s})" d="M0 -9 Q 7 0 6 4 A 6 6 0 0 1 -6 4 Q -7 0 0 -9 Z" fill="#5bb8ff" stroke="#2f8de0" stroke-width="1.5"/>`; }
function thermometer(x,y,s=1,hot=true){
  const c = hot ? '#e8434b' : '#3a8fc4';
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-6" y="-44" width="12" height="44" rx="6" fill="#fff" stroke="#333" stroke-width="2"/><rect x="-2.5" y="${hot?-38:-14}" width="5" height="${hot?40:16}" fill="${c}"/><circle cx="0" cy="4" r="9" fill="${c}" stroke="#333" stroke-width="2"/></g>`;
}
function titleSign(id, l1, l2, decor){
  let s = sky(W,280,id) + decor.back;
  s += `<rect x="72" y="182" width="14" height="70" fill="#8b5a2b" stroke="#6b4220" stroke-width="2"/><rect x="226" y="182" width="14" height="70" fill="#8b5a2b" stroke="#6b4220" stroke-width="2"/>`;
  s += `<rect x="28" y="70" width="256" height="122" rx="10" fill="#e9c38f" stroke="#6b4220" stroke-width="4"/>`;
  s += `<rect x="38" y="80" width="236" height="102" rx="6" fill="#f6dfb4" stroke="#c99a5e" stroke-width="2"/>`;
  const fs = (l1.length > 9 || l2.length > 9) ? 38 : 44;
  s += `<text x="156" y="126" text-anchor="middle" font-family="Andika" font-weight="700" font-size="${fs}" fill="#222">${l1}</text>`;
  s += `<text x="156" y="172" text-anchor="middle" font-family="Andika" font-weight="700" font-size="${fs}" fill="#222">${l2}</text>`;
  s += decor.front;
  return { h: 280, s };
}

// ---------- page renderers (one per template) ----------
function headerIcon(ST, w=58, h=44){ return `<svg viewBox="0 0 80 60" width="${w}" height="${h}">${ST.icon()}</svg>`; }

function renderLevel1(ST){
  document.title = ST.title + ' Level 1';
  const grid = document.getElementById('grid');
  ST.l1.panels.forEach(([fn, text], i) => {
    const d = document.createElement('div');
    d.className = 'panel' + (text ? '' : ' title');
    d.innerHTML = panelSVG(fn('L1p'+i), i) + (text ? `<div class="cap${text.length > 62 ? ' long' : ''}">${text}</div>` : '');
    grid.appendChild(d);
  });
  document.getElementById('cvc').innerHTML = ST.l1.cvc;
  document.getElementById('wbicon').innerHTML = `<svg viewBox="0 0 80 60" width="80" height="60">${ST.icon()}</svg>`;
  document.getElementById('cards').innerHTML = ST.l1.cards.map(([w, fn], i) => `<div class="card">${iconSVG(fn(), i)}<span>${w}</span></div>`).join('');
  document.getElementById('qs').innerHTML = ST.l1.questions.map(q => `<li>${q}</li>`).join('');
  if (location.hash === '#coloring') applyColoring('#page svg');
}

function renderLevel2(ST){
  document.title = ST.title + ' Level 2';
  document.querySelectorAll('.ttl').forEach(e => e.textContent = ST.title);
  document.querySelectorAll('.hicon').forEach(e => e.innerHTML = headerIcon(ST, 62, 46));
  const panels = ST.l2.panels;
  const add = (el, from, to) => { for (let i=from;i<to;i++){ const [fn, text] = panels[i];
    const d = document.createElement('div'); d.className = 'panel panelwrap';
    d.innerHTML = `<div class="num">${i+1}</div>` + panelSVG(fn('L2p'+i), i) + `<div class="cap${text.length > 80 ? ' long' : ''}">${text}</div>`;
    el.appendChild(d); } };
  add(document.getElementById('g1'), 0, 9);
  add(document.getElementById('g2'), 9, 12);
  document.getElementById('stretch').innerHTML = ST.l2.stretch.map(([w, syl]) => `<div class="sw"><b>${w}</b><span>${syl}</span></div>`).join('');
  document.getElementById('heart').innerHTML = ST.l2.heart.map(w => `<div class="sw"><b>${w}</b></div>`).join('');
  document.getElementById('qs').innerHTML = ST.l2.questions.map(q => `<li>${q}</li>`).join('');
  // passage must match the panels word for word
  const norm = t => t.replace(/\s+/g, ' ').trim();
  if (norm(ST.l2.lines.join(' ')) !== norm(panels.map(p => p[1]).join(' '))) document.body.insertAdjacentHTML('afterbegin', '<h1 style="color:red">PASSAGE MISMATCH</h1>');
  if (ST.l2.lines.length > 17) document.getElementById('passage').classList.add('tight');
  let total = 0;
  document.getElementById('passage').innerHTML = ST.l2.lines.map(l => { total += l.split(/\s+/).length; return `<tr><td>${l}</td><td class="c">${total}</td></tr>`; }).join('');
  if (location.hash === '#coloring') applyColoring('.sheet svg');
}

function renderWarmup(ST){
  document.title = ST.title + ' Word Warm-Up';
  const sep = w => w.split('|').join('<b>•</b>');
  document.getElementById('pyr').innerHTML = ST.warm.steps.map(([tag, words]) => `
    <div class="rowwrap"><div class="tag">${tag}</div>
      <div style="display:flex;justify-content:center"><div class="step">${words.map(w => `<span class="w">${sep(w)}</span>`).join('')}</div></div>
      <div class="checks"><span></span><span></span><span></span><span></span></div></div>`).join('');
  document.getElementById('phr').innerHTML = ST.warm.phrases.map(lines => `<div class="pp">${lines.map(l => `<div>${l}</div>`).join('')}</div>`).join('');
  document.getElementById('ex1').innerHTML = ST.warm.tap;
  document.getElementById('ex3').innerHTML = ST.warm.chunk;
  document.getElementById('powerlead').innerHTML = `✂ Cut out the cards. Read the word, clap the parts, and tell what it means. These words are in the big-kid story <i>${ST.original}</i>.`;
  document.getElementById('cards').innerHTML = ST.power.map(([w, syl, mean, from, art], i) => `
    <div class="card">${iconSVG(art(), i)}<div><div class="word">${w}</div><div class="syl">${syl}</div><div class="mean">${mean}</div><div class="from">${from}</div></div></div>`).join('');
  document.querySelectorAll('.hi').forEach(e => e.innerHTML = headerIcon(ST));
  applyColoring('svg');
}

function renderHome(ST){
  document.title = ST.title + ' Home Packet';
  document.querySelectorAll('.ttl').forEach(e => e.textContent = ST.title);
  document.querySelectorAll('[data-k]').forEach(e => { e.innerHTML = ST.home[e.dataset.k]; });
  document.getElementById('hq').innerHTML = ST.l2.questions.map((q, i) => `<div class="q">${i+1}. ${q}</div><div class="lines"><div></div><div></div></div>`).join('');
  document.querySelectorAll('.hi').forEach(e => e.innerHTML = headerIcon(ST, 56, 42));
  applyColoring('.hi svg');
}

// load the story named in ?s=... (its art file, then its data file)
const KIT = new URLSearchParams(location.search).get('s');
document.write(`<script src="art_${KIT}.js"><\/script><script src="${KIT}.js"><\/script>`);
