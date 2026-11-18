// Shared drawing code for the Sam the Spider materials.
// ---------- helpers ----------
let seed = 7;
function rnd(){ seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
const f = n => Math.round(n*10)/10;

const C = {
  sky1:'#bfe6ff', sky2:'#eaf7ff', grass:'#7cc66b', grassDk:'#5aa64c',
  bark:'#8b5a2b', barkDk:'#6b4220', barkLt:'#d9a86c', web:'#9aa7b4',
  sam:'#1d1d1f', will:'#b8621b', mom:'#6a3fa0'
};

function sky(w=312,h=210, id){ return `<defs><linearGradient id="sky${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${C.sky1}"/><stop offset="1" stop-color="${C.sky2}"/></linearGradient></defs><rect width="${w}" height="${h}" fill="url(#sky${id})"/>`; }
function ground(y, w=312, h=210){
  let s = `<path d="M0 ${y} Q ${w*0.25} ${y-8} ${w*0.5} ${y} T ${w} ${y} V ${h} H 0 Z" fill="${C.grass}"/>`;
  for (let i=0;i<14;i++){ const x = 10 + i*22 + rnd()*8; s += `<path d="M${f(x)} ${y+6} l3 -9 l3 9" fill="none" stroke="${C.grassDk}" stroke-width="2" stroke-linecap="round"/>`; }
  return s;
}
function flower(x,y,c='#ff7aa8'){
  let s = `<line x1="${x}" y1="${y}" x2="${x}" y2="${y+16}" stroke="${C.grassDk}" stroke-width="2.5"/>`;
  for (let a=0;a<5;a++){ const t=a*72*Math.PI/180; s += `<circle cx="${f(x+5*Math.cos(t))}" cy="${f(y+5*Math.sin(t))}" r="4" fill="${c}"/>`; }
  return s + `<circle cx="${x}" cy="${y}" r="3" fill="#ffd23f"/>`;
}
function sun(x,y,r=16){
  let s = '';
  for (let a=0;a<12;a++){ const t=a*30*Math.PI/180; s += `<line x1="${f(x+(r+4)*Math.cos(t))}" y1="${f(y+(r+4)*Math.sin(t))}" x2="${f(x+(r+11)*Math.cos(t))}" y2="${f(y+(r+11)*Math.sin(t))}" stroke="#ffc928" stroke-width="3" stroke-linecap="round"/>`; }
  return s + `<circle cx="${x}" cy="${y}" r="${r}" fill="#ffd84a" stroke="#f0b400" stroke-width="2"/>`;
}
function cloud(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})" fill="#fff"><circle cx="0" cy="0" r="12"/><circle cx="14" cy="-6" r="14"/><circle cx="30" cy="0" r="11"/><rect x="0" y="0" width="30" height="11"/></g>`;
}
function heart(x,y,s=1,c='#ff4f7b'){
  return `<path transform="translate(${x} ${y}) scale(${s})" d="M0 6 C -10 -2 -8 -12 0 -7 C 8 -12 10 -2 0 6 Z" fill="${c}" stroke="#c2185b" stroke-width="1"/>`;
}
function sparkle(x,y,s=1,c='#ffc928'){
  return `<path transform="translate(${x} ${y}) scale(${s})" d="M0 -9 L2.4 -2.4 L9 0 L2.4 2.4 L0 9 L-2.4 2.4 L-9 0 L-2.4 -2.4 Z" fill="${c}" stroke="#e0a000" stroke-width="0.8"/>`;
}
function branch(x1,y1,x2,y2,w=9){
  const mx=(x1+x2)/2, my=(y1+y2)/2 + 6;
  return `<path d="M${x1} ${y1} Q ${mx} ${my} ${x2} ${y2}" stroke="${C.bark}" stroke-width="${w}" fill="none" stroke-linecap="round"/>` +
         `<ellipse cx="${f(mx)}" cy="${f(my-6)}" rx="9" ry="5" fill="#6fbf5a" transform="rotate(-25 ${f(mx)} ${f(my-6)})"/>`;
}
function log(x,y,w,h){
  // horizontal log with cut end on the right
  let s = `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${h/2}" fill="${C.bark}" stroke="${C.barkDk}" stroke-width="2.5"/>`;
  for (let i=0;i<4;i++){ const lx = x+22+i*(w-60)/4; s += `<path d="M${f(lx)} ${y+h*0.3} q 14 -3 26 0" stroke="${C.barkDk}" stroke-width="2" fill="none" stroke-linecap="round"/>`; s += `<path d="M${f(lx+12)} ${y+h*0.68} q 14 3 24 0" stroke="${C.barkDk}" stroke-width="2" fill="none" stroke-linecap="round"/>`; }
  const ex = x+w-h*0.45, ey = y+h/2;
  s += `<ellipse cx="${f(ex)}" cy="${f(ey)}" rx="${f(h*0.42)}" ry="${f(h/2-1)}" fill="${C.barkLt}" stroke="${C.barkDk}" stroke-width="2.5"/>`;
  s += `<ellipse cx="${f(ex)}" cy="${f(ey)}" rx="${f(h*0.27)}" ry="${f(h*0.32)}" fill="none" stroke="#b5814a" stroke-width="1.6"/>`;
  s += `<ellipse cx="${f(ex)}" cy="${f(ey)}" rx="${f(h*0.12)}" ry="${f(h*0.15)}" fill="none" stroke="#b5814a" stroke-width="1.6"/>`;
  return s;
}
function gift(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <rect x="-22" y="-14" width="44" height="34" rx="3" fill="#e8434b" stroke="#a51f2a" stroke-width="2"/>
    <rect x="-26" y="-22" width="52" height="11" rx="3" fill="#f25a61" stroke="#a51f2a" stroke-width="2"/>
    <rect x="-5" y="-22" width="10" height="42" fill="#ffd23f" stroke="#d9a400" stroke-width="1.5"/>
    <path d="M0 -22 C -18 -40 -26 -22 0 -22 Z" fill="#ffd23f" stroke="#d9a400" stroke-width="1.5"/>
    <path d="M0 -22 C 18 -40 26 -22 0 -22 Z" fill="#ffd23f" stroke="#d9a400" stroke-width="1.5"/>
  </g>`;
}
function bubble(x,y,rx,ry,tailX,tailY,inner=''){
  return `<g><circle cx="${tailX}" cy="${tailY}" r="4" fill="#fff" stroke="#333" stroke-width="2"/>
    <circle cx="${f((tailX+x)/2 + (tailX<x?-4:4)*0)}" cy="${f((tailY+y+ry)/2)}" r="6.5" fill="#fff" stroke="#333" stroke-width="2"/>
    <ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#fff" stroke="#333" stroke-width="2.5"/>${inner}</g>`;
}
function speech(x,y,rx,ry,tx,ty,inner=''){
  return `<g><path d="M${x-10} ${y+ry-4} L ${tx} ${ty} L ${x+8} ${y+ry-2} Z" fill="#fff" stroke="#333" stroke-width="2.5" stroke-linejoin="round"/>
    <ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="#fff" stroke="#333" stroke-width="2.5"/>
    <rect x="${x-14}" y="${y+ry-8}" width="24" height="7" fill="#fff" stroke="none"/>${inner}</g>`;
}

// ---------- webs ----------
function web(cx,cy,R,opts={}){
  const n = opts.spokes || 10, rings = opts.rings ?? 6, col = opts.color || C.web, sw = opts.sw || 1.6;
  const gapFrom = opts.gap ? opts.gap[0] : -1, gapTo = opts.gap ? opts.gap[1] : -1;
  const rot = opts.rot || -90;
  let s = '';
  const ang = i => (rot + i*360/n) * Math.PI/180;
  const inGap = i => opts.gap && i>=gapFrom && i<gapTo;
  for (let i=0;i<n;i++){
    const a = ang(i);
    if (opts.gap && i>gapFrom && i<gapTo) continue;
    s += `<line x1="${cx}" y1="${cy}" x2="${f(cx+R*Math.cos(a))}" y2="${f(cy+R*Math.sin(a))}" stroke="${col}" stroke-width="${sw}"/>`;
  }
  const maxRing = opts.partial ? Math.min(rings, opts.partial) : rings;
  for (let k=1;k<=maxRing;k++){
    const r = R*k/(rings+0.4);
    for (let i=0;i<n;i++){
      if (inGap(i) && k>1) continue;
      const a1 = ang(i), a2 = ang(i+1), am = (a1+a2)/2;
      const x1=cx+r*Math.cos(a1), y1=cy+r*Math.sin(a1), x2=cx+r*Math.cos(a2), y2=cy+r*Math.sin(a2);
      const qx=cx+r*0.86*Math.cos(am), qy=cy+r*0.86*Math.sin(am);
      s += `<path d="M${f(x1)} ${f(y1)} Q ${f(qx)} ${f(qy)} ${f(x2)} ${f(y2)}" stroke="${col}" stroke-width="${sw}" fill="none"/>`;
    }
  }
  if (opts.gap && opts.mark){
    const am = (ang(gapFrom)+ang(gapTo))/2, gr = R*0.58;
    s += `<circle cx="${f(cx+gr*Math.cos(am))}" cy="${f(cy+gr*Math.sin(am))}" r="${f(R*0.36)}" fill="none" stroke="#e8434b" stroke-width="2.5" stroke-dasharray="6 4"/>`;
  }
  return s;
}
function messyWeb(cx,cy,w,h,n=34,sd=11){
  seed = sd;
  let s = '';
  const pts = [];
  for (let i=0;i<n;i++) pts.push([cx + (rnd()-0.5)*w, cy + (rnd()-0.5)*h]);
  let d = `M${f(pts[0][0])} ${f(pts[0][1])}`;
  for (let i=1;i<n;i++){
    const c = [cx + (rnd()-0.5)*w*1.1, cy + (rnd()-0.5)*h*1.1];
    d += ` Q ${f(c[0])} ${f(c[1])} ${f(pts[i][0])} ${f(pts[i][1])}`;
  }
  s += `<path d="${d}" stroke="#7d8a97" stroke-width="1.7" fill="none" stroke-linecap="round"/>`;
  for (let i=0;i<5;i++){
    const x = cx+(rnd()-0.5)*w*0.8, y = cy+(rnd()-0.5)*h*0.8, r = 5+rnd()*8;
    s += `<path d="M${f(x)} ${f(y)} c ${f(r)} ${f(-r)} ${f(2*r)} ${f(r)} ${f(r*0.3)} ${f(r*1.2)} s ${f(-r*1.4)} ${f(-r*1.6)} ${f(r*0.6)} ${f(-r*0.9)}" stroke="#7d8a97" stroke-width="1.7" fill="none"/>`;
  }
  return s;
}

// ---------- spider ----------
// unit body radius 40; legs reach about +-90 x, -55..72 y
const BASE_LEGS = [ // right side [start, control, foot]
  [[28,-22],[66,-66],[86,-30]],
  [[36,-8],[84,-34],[96,6]],
  [[36,8],[84,10],[90,46]],
  [[28,22],[66,44],[66,74]],
];
function spider(o){
  const s = o.s || 1, col = o.color || C.sam, x = o.x, y = o.y;
  const mood = o.mood || 'happy', flip = o.flip ? -1 : 1;
  const lk = o.look || [0,0];
  let legs = '';
  for (const side of [1,-1]){
    BASE_LEGS.forEach((L,i)=>{
      let leg = L;
      const key = (side===1?'r':'l')+i;
      if (o.legs && o.legs[key]) leg = o.legs[key];
      if (o.legs && o.legs[key] === null) return;
      const [a,b,c] = leg;
      legs += `<path d="M${a[0]*side} ${a[1]} Q ${b[0]*side} ${b[1]} ${c[0]*side} ${c[1]}" fill="none" stroke="${col}" stroke-width="7" stroke-linecap="round"/>`;
    });
  }
  // fuzzy body
  let pts = [];
  const N = 44;
  for (let i=0;i<N;i++){
    const t = i/N*Math.PI*2, r = (i%2? 45.5 : 39) + (i%4===1? 1.5:0);
    pts.push(`${f(r*Math.cos(t))},${f(r*Math.sin(t))}`);
  }
  let body = `<polygon points="${pts.join(' ')}" fill="${col}" stroke="${col}" stroke-width="2" stroke-linejoin="round"/>`;
  if (o.shine !== false) body += `<ellipse cx="-16" cy="-24" rx="9" ry="5" fill="#fff" opacity="0.13" transform="rotate(-30 -16 -24)"/>`;
  // eyes
  let eyes = '';
  if (o.eyes === 'closed'){
    eyes = `<path d="M-25 -6 Q -15 -18 -5 -6" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M5 -6 Q 15 -18 25 -6" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>`;
  } else {
    for (const ex of [-14, 14]){
      eyes += `<ellipse cx="${ex}" cy="-8" rx="11.5" ry="13.5" fill="#fff" stroke="#000" stroke-width="1.5"/>`;
      eyes += `<circle cx="${ex+lk[0]+1}" cy="${-6+lk[1]}" r="6" fill="#111"/><circle cx="${ex+lk[0]+3}" cy="${-9+lk[1]}" r="2" fill="#fff"/>`;
    }
  }
  if (o.eyes === 'tired'){
    for (const ex of [-14,14]) eyes += `<path d="M${ex-12.5} -7 A 12.5 14.5 0 0 1 ${ex+12.5} -7 Z" fill="${col}" stroke="#fff" stroke-width="1.5"/>`;
  }
  if (o.lashes){
    eyes += `<path d="M-24 -18 l-6 -5 M-20 -21 l-4 -7 M24 -18 l6 -5 M20 -21 l4 -7" stroke="#111" stroke-width="2.2" stroke-linecap="round"/>`;
  }
  // brows
  let brows = '';
  if (mood==='sad') brows = `<path d="M-24 -27 L-6 -31 M24 -27 L6 -31" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>`;
  if (mood==='worried') brows = `<path d="M-23 -28 Q -14 -34 -5 -30 M23 -28 Q 14 -34 5 -30" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>`;
  if (mood==='determined') brows = `<path d="M-24 -32 L-6 -26 M24 -32 L6 -26" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/>`;
  // mouth
  let mouth = '';
  const pink = '#ff8fa3';
  if (mood==='happy' || mood==='determined') mouth = `<path d="M-10 13 Q 0 26 10 13 Z" fill="${pink}" stroke="#fff" stroke-width="1.5" stroke-linejoin="round"/>`;
  if (mood==='smile') mouth = `<path d="M-9 14 Q 0 22 9 14" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>`;
  if (mood==='grin') mouth = `<path d="M-17 10 Q 0 34 17 10 Z" fill="#c9304a" stroke="#fff" stroke-width="2" stroke-linejoin="round"/><path d="M-14 11.5 L14 11.5 L12 15 L-12 15 Z" fill="#fff"/><ellipse cx="0" cy="22" rx="6" ry="3.5" fill="${pink}"/>`;
  if (mood==='sad') mouth = `<path d="M-10 21 Q 0 11 10 21" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>`;
  if (mood==='worried') mouth = `<path d="M-10 18 q 3.5 -4 7 0 t 7 0 t 6 0" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>`;
  if (mood==='surprised') mouth = `<ellipse cx="0" cy="17" rx="6" ry="7.5" fill="#c9304a" stroke="#fff" stroke-width="1.5"/>`;
  let extra = '';
  if (o.cheeks !== false && mood!=='sad') extra += `<circle cx="-27" cy="9" r="5" fill="#ff7c9c" opacity="0.75"/><circle cx="27" cy="9" r="5" fill="#ff7c9c" opacity="0.75"/>`;
  if (o.tear) extra += `<path d="M-22 6 q -5 9 0 12 q 5 -3 0 -12 Z" fill="#5bb8ff" stroke="#2f8de0" stroke-width="1"/>`;
  if (o.bow) extra += `<g transform="translate(22 -38) rotate(15)"><path d="M0 0 L-15 -10 L-15 10 Z M0 0 L15 -10 L15 10 Z" fill="#ff5fa2" stroke="#c2185b" stroke-width="1.8" stroke-linejoin="round"/><circle r="4.5" fill="#ff8cc0" stroke="#c2185b" stroke-width="1.5"/></g>`;
  if (o.cap) extra += `<g transform="translate(0 -30)"><path d="M-30 0 Q -28 -30 0 -31 Q 28 -30 30 0 Z" fill="#2fa84f" stroke="#1d7a36" stroke-width="2"/><path d="M14 -2 Q 36 -6 46 2 Q 34 6 14 3 Z" fill="#26913f" stroke="#1d7a36" stroke-width="2"/><circle cx="0" cy="-30" r="3.5" fill="#1d7a36"/></g>`;
  const face = `<g transform="scale(${flip} 1)">${eyes}</g>${brows}${mouth}${extra}`;
  const thread = o.thread != null ? `<line x1="${x}" y1="${o.thread}" x2="${x}" y2="${y-40*s}" stroke="#555" stroke-width="1.5"/>` : '';
  return `${thread}<g transform="translate(${x} ${y}) scale(${s*flip} ${s})${o.rot?` rotate(${o.rot})`:''}">${legs}${body}<g transform="scale(${flip} 1)">${face}</g></g>`;
}
// leg poses
const POSE = {
  wave: { r0: [[28,-22],[58,-52],[64,-78]] },
  waveL: { l0: [[28,-22],[58,-52],[64,-78]] },
  cheeks: { r0: [[28,-22],[56,-30],[34,6]], l0: [[28,-22],[56,-30],[34,6]] },
  sit: { r2: [[36,8],[70,24],[86,56]], l2:[[36,8],[70,24],[86,56]], r3:[[28,22],[50,44],[50,56]], l3:[[28,22],[50,44],[50,56]] },
  armsUp: { r0: [[28,-22],[50,-56],[66,-74]], l0: [[28,-22],[50,-56],[66,-74]] },
};
function merge(...p){ return Object.assign({}, ...p); }


function applyColoring(sel='svg') {
  const NS = 'http://www.w3.org/2000/svg';
  const els = [...document.querySelectorAll(sel + ' *')].filter(e => !e.closest('clipPath,defs'));
  for (const e of els) {
    const tag = e.tagName;
    if (e.hasAttribute('data-keep')) { e.removeAttribute('opacity'); continue; }  // white backing behind the I LOVE YOU letters
    if (tag === 'g') { if (e.getAttribute('fill')) e.remove(); continue; } // clouds
    const op = e.getAttribute('opacity');
    if (op && parseFloat(op) < 1) { e.remove(); continue; }               // shine + cheeks
    const fill = e.getAttribute('fill'), stroke = e.getAttribute('stroke');
    const sw = parseFloat(e.getAttribute('stroke-width') || '1');
    if (tag === 'text') { e.setAttribute('fill','#fff'); e.setAttribute('stroke','#000'); e.setAttribute('stroke-width','1.8'); continue; }
    if (fill && fill !== 'none') {
      if (fill.startsWith('url')) { e.setAttribute('fill','#fff'); continue; }  // sky
      if (fill === '#111' || fill === '#000') continue;                          // pupils
      e.setAttribute('fill','#fff');
      const tiny = tag === 'circle' && parseFloat(e.getAttribute('r')) <= 2.5;
      if (!stroke && !tiny) { e.setAttribute('stroke','#000'); e.setAttribute('stroke-width','1.5'); }
    }
    if (stroke && stroke !== 'none') {
      if ((!fill || fill === 'none') && sw >= 4.5 && (tag === 'path' || tag === 'line')) {
        const c = e.cloneNode(); c.setAttribute('stroke','#000'); c.setAttribute('stroke-width', sw + 3);
        e.parentNode.insertBefore(c, e);
        e.setAttribute('stroke','#fff'); e.setAttribute('stroke-width', Math.max(sw - 1.5, 2.5));
      } else {
        const isWeb = ['#9aa7b4','#a7b4c0','#7d8a97','#555'].includes(stroke);
        e.setAttribute('stroke', isWeb ? '#333' : '#000');
        if (isWeb) e.setAttribute('stroke-width', Math.min(sw, 0.9));
      }
    }
  }
}

// ---------- new art for the matched Level 1 / Level 2 stories ----------
const W = 312, H = 210;

function worm(o){
  const s = o.s || 1, flip = o.flip ? -1 : 1, body = o.color || '#f5a3b7', edge = '#c4627d';
  const P = o.pose === 'flat' ? [[-74,10],[-40,8],[0,8],[26,0]] : [[-70,10],[-52,-48],[0,-50],[22,-4]];
  const lk = o.look || [1,0];
  let g = '';
  const n = 11;
  for (let i=0;i<=n;i++){
    const t = i/n, m = 1-t;
    const px = m*m*m*P[0][0] + 3*m*m*t*P[1][0] + 3*m*t*t*P[2][0] + t*t*t*P[3][0];
    const py = m*m*m*P[0][1] + 3*m*m*t*P[1][1] + 3*m*t*t*P[2][1] + t*t*t*P[3][1];
    g += `<circle cx="${f(px)}" cy="${f(py)}" r="${f(9+5*t)}" fill="${body}" stroke="${edge}" stroke-width="2"/>`;
  }
  const hx = P[3][0] + 14, hy = P[3][1] - 12;
  g += `<circle cx="${hx}" cy="${hy}" r="19" fill="${body}" stroke="${edge}" stroke-width="2.2"/>`;
  // face is drawn un-flipped so it always reads correctly
  let face = '';
  for (const ex of [-7,7]){
    face += `<ellipse cx="${ex}" cy="-4" rx="5.8" ry="7" fill="#fff" stroke="#000" stroke-width="1.3"/>`;
    face += `<circle cx="${ex+lk[0]}" cy="${-3+lk[1]}" r="3.2" fill="#111"/><circle cx="${ex+lk[0]+1.2}" cy="${-4.5+lk[1]}" r="1.1" fill="#fff"/>`;
  }
  const mood = o.mood || 'happy';
  if (mood==='happy') face += `<path d="M-7 7 Q 0 14 7 7" stroke="#7a2d43" stroke-width="2.2" fill="none" stroke-linecap="round"/>`;
  if (mood==='talk') face += `<ellipse cx="0" cy="9" rx="5" ry="4.5" fill="#c9304a" stroke="#7a2d43" stroke-width="1.5"/>`;
  if (mood==='worried') face += `<path d="M-7 10 q 3.5 -4 7 0 t 7 0" stroke="#7a2d43" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M-12 -14 Q -7 -17 -3 -15 M12 -14 Q 7 -17 3 -15" stroke="#7a2d43" stroke-width="1.8" fill="none" stroke-linecap="round"/>`;
  face += `<circle cx="-13" cy="5" r="3.2" fill="#ff7c9c" opacity="0.8"/><circle cx="13" cy="5" r="3.2" fill="#ff7c9c" opacity="0.8"/>`;
  if (o.cap !== false) face += `<path d="M-17 -10 Q -15 -30 0 -30 Q 15 -30 17 -10 Z" fill="#2fa84f" stroke="#1d7a36" stroke-width="1.8"/><path d="M${8*flip} -11 Q ${24*flip} -14 ${30*flip} -8 Q ${22*flip} -5 ${8*flip} -8 Z" fill="#26913f" stroke="#1d7a36" stroke-width="1.8"/>`;
  return `<g transform="translate(${o.x} ${o.y}) scale(${s})"><g transform="scale(${flip} 1)">${g}</g><g transform="translate(${hx*flip} ${hy})">${face}</g></g>`;
}

function cake(x,y,s=1){
  let candles = '';
  for (const cx of [-12,0,12]) candles += `<rect x="${cx-2.5}" y="-50" width="5" height="18" fill="#8fd3ff" stroke="#3a8fc4" stroke-width="1.2"/><path d="M${cx} -62 q -5 7 0 10 q 5 -3 0 -10 Z" fill="#ffb627" stroke="#e07b00" stroke-width="1.2"/>`;
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <ellipse cx="0" cy="22" rx="44" ry="7" fill="#e6e6e6" stroke="#888" stroke-width="1.5"/>
    <rect x="-36" y="-8" width="72" height="30" rx="4" fill="#ffb3c7" stroke="#c4627d" stroke-width="2"/>
    <path d="M-36 -2 q 6 10 12 0 q 6 10 12 0 q 6 10 12 0 q 6 10 12 0 q 6 10 12 0 q 6 10 12 0 V -8 H -36 Z" fill="#fff" stroke="#c4627d" stroke-width="1.5"/>
    <rect x="-24" y="-32" width="48" height="24" rx="4" fill="#ffe08a" stroke="#d1a21c" stroke-width="2"/>
    <circle cx="-12" cy="8" r="2.5" fill="#e8434b"/><circle cx="4" cy="12" r="2.5" fill="#2fa84f"/><circle cx="20" cy="8" r="2.5" fill="#3a8fc4"/>
    ${candles}</g>`;
}

function lightbulb(x,y,s=1){
  let rays='';
  for (const a of [-150,-110,-70,-30]){ const t=a*Math.PI/180; rays += `<line x1="${f(17*Math.cos(t))}" y1="${f(-4+17*Math.sin(t))}" x2="${f(24*Math.cos(t))}" y2="${f(-4+24*Math.sin(t))}" stroke="#f0b400" stroke-width="2.5" stroke-linecap="round"/>`; }
  return `<g transform="translate(${x} ${y}) scale(${s})">${rays}<circle cx="0" cy="-4" r="12" fill="#fff59d" stroke="#e0a800" stroke-width="2"/><rect x="-6" y="7" width="12" height="9" rx="2" fill="#bbb" stroke="#777" stroke-width="1.5"/></g>`;
}

function zzz(x,y){
  return `<text x="${x}" y="${y}" font-family="Andika" font-weight="700" fill="#5b6b7a"><tspan font-size="12">z</tspan><tspan font-size="16" dy="-6">Z</tspan><tspan font-size="20" dy="-7">Z</tspan></text>`;
}

function crookedWeb(cx,cy,R,sd=9,n=9,rings=5){
  seed = sd;
  const sc = [], an = [];
  for (let i=0;i<n;i++){ sc.push(0.62 + rnd()*0.55); an.push((-90 + i*360/n + (rnd()-0.5)*26)*Math.PI/180); }
  let s = '';
  for (let i=0;i<n;i++) s += `<line x1="${cx}" y1="${cy}" x2="${f(cx+R*sc[i]*Math.cos(an[i]))}" y2="${f(cy+R*sc[i]*Math.sin(an[i]))}" stroke="${C.web}" stroke-width="1.6"/>`;
  for (let k=1;k<=rings;k++){
    let d = '';
    for (let i=0;i<=n;i++){
      const j = i % n, r = R*sc[j]*k/(rings+0.3) * (0.9 + rnd()*0.2);
      d += (i ? ' L ' : 'M') + `${f(cx+r*Math.cos(an[j]))} ${f(cy+r*Math.sin(an[j]))}`;
    }
    s += `<path d="${d}" stroke="${C.web}" stroke-width="1.6" fill="none" stroke-linejoin="round"/>`;
  }
  return s;
}

function loveWeb(cx,cy,R,opts={}){
  let s = web(cx,cy,R,{spokes:12,rings:6});
  const h = R*0.2, w = h*0.72, gap = h*0.3, lg = h*0.4;
  const lines = [['I'],['L','O','V','E'],['Y','O','U']];
  const total = 3*h + 2*lg;
  s += `<ellipse data-keep="1" cx="${cx}" cy="${cy}" rx="${f(R*0.58)}" ry="${f(R*0.5)}" fill="#fff" opacity="0.8"/>`;
  const col = '#3f4a55', sw = Math.max(1.8, R*0.035);
  let eBox = null;
  seed = 5;
  lines.forEach((ln,li)=>{
    const lw = ln.length*w + (ln.length-1)*gap;
    ln.forEach((ch,ci)=>{
      const x = cx - lw/2 + ci*(w+gap), y = cy - total/2 + li*(h+lg) + (rnd()-0.5)*h*0.25;
      const m = (u,v) => `${f(x+u*w)} ${f(y+v*h)}`;
      const rot = f((rnd()-0.5)*16);
      const tr = `transform="rotate(${rot} ${f(x+w/2)} ${f(y+h/2)})"`;
      const st = `stroke="${col}" stroke-width="${f(sw)}" fill="none" stroke-linecap="round" stroke-linejoin="round"`;
      let d = '';
      if (ch==='I') d = `M${m(.5,0)} L${m(.5,1)}`;
      if (ch==='L') d = `M${m(0,0)} L${m(0,1)} L${m(1,1)}`;
      if (ch==='V') d = `M${m(0,0)} L${m(.5,1)} L${m(1,0)}`;
      if (ch==='E') { d = `M${m(1,0)} L${m(0,0)} L${m(0,1)} M${m(0,.5)} L${m(.75,.5)}`; eBox = [x+w/2, y+h/2]; }
      if (ch==='Y') d = `M${m(0,0)} L${m(.5,.5)} L${m(1,0)} M${m(.5,.5)} L${m(.5,1)}`;
      if (ch==='U') d = `M${m(0,0)} L${m(0,.65)} Q${m(0,1)} ${m(.5,1)} Q${m(1,1)} ${m(1,.65)} L${m(1,0)}`;
      if (ch==='O') s += `<ellipse cx="${f(x+w/2)}" cy="${f(y+h/2)}" rx="${f(w/2)}" ry="${f(h/2)}" ${st} ${tr}/>`;
      else s += `<path d="${d}" ${st} ${tr}/>`;
    });
  });
  if (opts.mark && eBox) s += `<circle cx="${f(eBox[0])}" cy="${f(eBox[1])}" r="${f(h*1.05)}" fill="none" stroke="#e8434b" stroke-width="2.4" stroke-dasharray="5 3"/>`;
  return s;
}

function trunk(x,w=40){
  let s = `<rect x="${x}" y="-5" width="${w}" height="220" fill="${C.bark}" stroke="${C.barkDk}" stroke-width="2.5"/>`;
  for (let i=0;i<6;i++){ const y = 16+i*34; s += `<path d="M${x+8} ${y} q 6 8 0 16 M${x+w-10} ${y+14} q -5 8 0 15" stroke="${C.barkDk}" stroke-width="2" fill="none" stroke-linecap="round"/>`; }
  return s;
}
function bigBranch(){
  // thick branch across the panel, joining a trunk on the right
  let s = trunk(284,44);
  s += `<path d="M-10 160 Q 140 150 290 136" stroke="${C.bark}" stroke-width="20" fill="none" stroke-linecap="round"/>`;
  s += `<path d="M-10 160 Q 140 150 290 136" stroke="${C.barkDk}" stroke-width="2" fill="none" transform="translate(0 8)"/>`;
  s += `<path d="M40 152 Q 30 128 46 112" stroke="${C.bark}" stroke-width="6" fill="none" stroke-linecap="round"/>`;
  for (const [x,y,r] of [[46,110,-30],[20,150,20],[250,128,-20],[140,140,35]]) s += `<ellipse cx="${x}" cy="${y}" rx="11" ry="5.5" fill="#6fbf5a" stroke="#4e9a3a" stroke-width="1.2" transform="rotate(${r} ${x} ${y})"/>`;
  return s;
}

// ---------- scenes (each returns the inside of a 312 x 210 panel) ----------
const S = {
  title(id, line1='Sam the', line2='Spider'){
    seed=3;
    let s = sky(W,280,id) + sun(268,36,14) + cloud(30,34,0.9) + ground(236,W,280);
    s += web(W,0,70,{spokes:6,rings:4,rot:90,color:'#a7b4c0'});
    s += `<rect x="72" y="182" width="14" height="70" fill="${C.bark}" stroke="${C.barkDk}" stroke-width="2"/><rect x="226" y="182" width="14" height="70" fill="${C.bark}" stroke="${C.barkDk}" stroke-width="2"/>`;
    s += `<rect x="28" y="70" width="256" height="122" rx="10" fill="#e9c38f" stroke="${C.barkDk}" stroke-width="4"/>`;
    s += `<rect x="38" y="80" width="236" height="102" rx="6" fill="#f6dfb4" stroke="#c99a5e" stroke-width="2"/>`;
    s += `<text x="156" y="126" text-anchor="middle" font-family="Andika" font-weight="700" font-size="44" fill="#222">${line1}</text>`;
    s += `<text x="156" y="172" text-anchor="middle" font-family="Andika" font-weight="700" font-size="44" fill="#222">${line2}</text>`;
    s += spider({x:252, y:58, s:0.44, thread:0, mood:'happy', look:[-3,2]});
    s += worm({x:150, y:250, s:0.62, pose:'flat', look:[2,-1]});
    s += flower(26,246,'#ff7aa8') + flower(286,250,'#ffb84d');
    return {h:280, s};
  },
  spin(id){
    seed=5;
    let s = sky(W,H,id) + cloud(250,30,0.8) + ground(188);
    s += branch(-10,22,170,8,10) + `<rect x="276" y="0" width="22" height="200" fill="${C.bark}" stroke="${C.barkDk}" stroke-width="2"/>`;
    s += `<line x1="70" y1="20" x2="110" y2="58" stroke="${C.web}" stroke-width="1.6"/><line x1="276" y1="96" x2="214" y2="100" stroke="${C.web}" stroke-width="1.6"/><line x1="150" y1="186" x2="160" y2="160" stroke="${C.web}" stroke-width="1.6"/>`;
    s += web(156,100,82,{spokes:12,rings:6});
    s += spider({x:156, y:104, s:0.46, mood:'happy'});
    s += flower(40,176) + flower(242,180,'#ffb84d');
    return {h:H,s};
  },
  planCake(id){
    seed=8;
    let s = sky(W,H,id) + ground(176);
    const inner = web(168,64,32,{spokes:10,rings:4}) + `<text x="204" y="72" font-family="Andika" font-weight="700" font-size="22" fill="#e8434b">+</text>` + cake(250,74,0.62);
    s += bubble(212,64,90,50, 96,128, inner);
    s += spider({x:66, y:160, s:0.5, mood:'happy', look:[3,-3]});
    s += flower(150,180) + flower(286,182,'#b388ff');
    return {h:H,s};
  },
  climb(id){
    seed=9;
    let s = sky(W,H,id) + ground(192) + trunk(46,52);
    s += `<path d="M98 40 Q 130 30 150 14" stroke="${C.bark}" stroke-width="10" fill="none" stroke-linecap="round"/><ellipse cx="140" cy="24" rx="12" ry="6" fill="#6fbf5a" stroke="#4e9a3a" stroke-width="1.2"/>`;
    s += spider({x:72, y:120, s:0.36, mood:'happy', look:[3,-3]});
    s += `<path d="M72 160 L72 186" stroke="#888" stroke-width="2" stroke-dasharray="3 4"/><path d="M66 172 l6 -8 l6 8" stroke="#888" stroke-width="2" fill="none"/>`;
    const inner = web(186,96,30,{spokes:10,rings:4}) + `<text x="221" y="104" font-family="Andika" font-weight="700" font-size="22" fill="#e8434b">+</text>` + cake(264,106,0.58);
    s += bubble(224,96,80,50, 112,112, inner);
    return {h:H,s};
  },
  bent(id){
    seed=12;
    let s = sky(W,H,id) + ground(186);
    s += branch(-10,20,220,12,10) + `<path d="M296 186 L 296 40" stroke="#5aa64c" stroke-width="4"/>`;
    s += `<path d="M70 22 L 96 52 M296 96 L 236 102" stroke="${C.web}" stroke-width="1.6"/>`;
    s += crookedWeb(140,100,78,21);
    s += spider({x:258, y:160, s:0.38, mood:'worried', look:[-4,-3]});
    return {h:H,s};
  },
  small(id){
    seed=14;
    let s = sky(W,H,id) + sun(40,34,13) + ground(180);
    s += `<path d="M196 182 L 192 132 M236 182 L 240 130" stroke="#5aa64c" stroke-width="3"/>`;
    s += web(216,148,16,{spokes:8,rings:3});
    s += spider({x:110, y:132, s:0.56, mood:'surprised', look:[5,3]});
    s += `<path d="M180 120 l 14 14 M262 120 l -14 14" stroke="#e8434b" stroke-width="2.5" stroke-linecap="round"/>`;
    s += flower(290,182,'#b388ff');
    return {h:H,s};
  },
  mess(id){
    seed=17;
    let s = sky(W,H,id) + ground(178);
    s += branch(-10,30,140,14,9) + `<path d="M300 178 L 300 22" stroke="#5aa64c" stroke-width="4"/>`;
    s += messyWeb(160,90,210,120,40,23);
    s += `<path d="M60 22 L 92 50 M296 60 L 252 74" stroke="#7d8a97" stroke-width="1.6"/>`;
    s += spider({x:56, y:160, s:0.38, mood:'surprised', look:[4,-4]});
    s += `<text x="92" y="132" font-family="Andika" font-weight="700" font-size="28" fill="#e8434b">!</text>`;
    return {h:H,s};
  },
  quit(id){
    seed=19;
    let s = sky(W,H,id) + bigBranch();
    s += messyWeb(214,56,70,64,18,31);
    s += spider({x:120, y:118, s:0.5, mood:'sad', tear:true, look:[0,4], legs:merge(POSE.cheeks, POSE.sit)});
    return {h:H,s};
  },
  willArrives(id){
    seed=23;
    let s = sky(W,H,id) + cloud(150,30,0.8) + bigBranch();
    s += spider({x:70, y:126, s:0.44, mood:'sad', look:[4,1], legs:POSE.sit});
    s += worm({x:222, y:123, s:0.72, flip:true, mood:'talk', look:[-2,0]});
    return {h:H,s};
  },
  tired(id){
    seed=27;
    let s = sky(W,H,id) + bigBranch();
    s += spider({x:96, y:124, s:0.46, mood:'worried', eyes:'tired', look:[0,3], legs:POSE.sit});
    s += zzz(118,72);
    s += worm({x:216, y:123, s:0.72, flip:true, mood:'worried', look:[-2,0]});
    return {h:H,s};
  },
  talk(id){
    seed=29;
    let s = sky(W,H,id) + bigBranch();
    s += spider({x:86, y:124, s:0.44, mood:'smile', look:[4,-2], legs:POSE.sit});
    s += worm({x:200, y:123, s:0.72, flip:true, mood:'talk', look:[-2,-1]});
    s += speech(236,40,46,26,198,82, heart(224,40,1.3) + heart(248,42,1.0));
    return {h:H,s};
  },
  think(id){
    seed=30;
    let s = sky(W,H,id) + bigBranch();
    s += spider({x:96, y:124, s:0.46, mood:'happy', look:[2,-4], legs:POSE.sit});
    s += bubble(150,40,32,26, 112,78, lightbulb(150,42,1));
    s += worm({x:220, y:123, s:0.72, flip:true, mood:'happy', look:[-2,-1]});
    return {h:H,s};
  },
  loveSpin(id){
    seed=31;
    let s = sky(W,H,id) + sun(286,26,11) + ground(192);
    s += branch(-10,14,250,10,10);
    s += `<line x1="96" y1="14" x2="118" y2="32" stroke="${C.web}" stroke-width="1.6"/>`;
    s += loveWeb(124,104,76);
    s += `<line x1="200" y1="104" x2="240" y2="104" stroke="#7d8a97" stroke-width="1.6"/>`;
    s += spider({x:252, y:104, s:0.38, mood:'determined', look:[-4,0], thread:14});
    s += sparkle(222,58,0.9) + sparkle(290,150,0.8);
    return {h:H,s};
  },
  flaw(id){
    seed=37;
    let s = sky(W,H,id) + ground(192);
    s += branch(-10,12,240,10,10);
    s += loveWeb(120,104,80,{mark:true});
    s += spider({x:258, y:150, s:0.42, mood:'grin', eyes:'closed', legs:POSE.wave});
    s += sparkle(222,70,0.9);
    return {h:H,s};
  },
  hug(id){
    seed=41;
    let s = sky(W,H,id) + ground(186);
    s += branch(-10,10,150,6,9);
    s += loveWeb(74,92,64);
    s += spider({x:206, y:120, s:0.62, color:C.mom, bow:true, lashes:true, mood:'happy', eyes:'closed', legs:{l0:null,l1:null}});
    s += spider({x:158, y:146, s:0.42, mood:'happy', eyes:'closed'});
    s += `<path d="M188 110 Q 160 96 138 126" stroke="${C.mom}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`;
    s += `<path d="M186 134 Q 172 174 138 160" stroke="${C.mom}" stroke-width="4.5" fill="none" stroke-linecap="round"/>`;
    s += heart(190,48,1.4) + heart(228,30,1) + heart(160,64,0.9);
    return {h:H,s};
  },
  proud(id){
    seed=43;
    let s = sky(W,H,id) + ground(188);
    s += branch(-10,10,230,8,10);
    s += loveWeb(112,100,78);
    s += `<g transform="translate(112 22)"><path d="M0 0 L-14 -9 L-14 9 Z M0 0 L14 -9 L14 9 Z" fill="#ff5fa2" stroke="#c2185b" stroke-width="1.6" stroke-linejoin="round"/><circle r="4" fill="#ff8cc0" stroke="#c2185b" stroke-width="1.4"/></g>`;
    s += spider({x:250, y:142, s:0.46, mood:'happy', look:[-5,-2]});
    s += heart(246,76,1.3) + heart(282,96,0.9) + cake(206,178,0.38);
    return {h:H,s};
  },
};

function panelSVG(sceneOut, i){
  const h = sceneOut.h;
  return `<svg viewBox="0 0 ${W} ${h}" xmlns="http://www.w3.org/2000/svg"><clipPath id="c${i}"><rect width="${W}" height="${h}"/></clipPath><g clip-path="url(#c${i})">${sceneOut.s}</g></svg>`;
}
function iconSVG(inner, i, w=150, h=100){
  return `<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg"><clipPath id="k${i}"><rect width="${w}" height="${h}"/></clipPath><g clip-path="url(#k${i})">${inner}</g></svg>`;
}
