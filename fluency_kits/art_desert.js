// Art for "The Desert"
const SAND = '#f3d38b', SANDDK = '#d9ad5b', ICE = '#eef8ff', ICEDK = '#9cc9e6';

function dunes(y, w=312, h=210){
  return `<path d="M0 ${y} Q 60 ${y-30} 130 ${y-6} T 312 ${y-14} V ${h} H 0 Z" fill="${SANDDK}"/>` +
         `<path d="M0 ${y+18} Q 90 ${y-6} 180 ${y+14} T 312 ${y+8} V ${h} H 0 Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>`;
}
function iceGround(y, w=312, h=210){
  return `<path d="M0 ${y} L 40 ${y-10} L 90 ${y-2} L 150 ${y-14} L 220 ${y-4} L 312 ${y-12} V ${h} H 0 Z" fill="${ICE}" stroke="${ICEDK}" stroke-width="2"/>`;
}
function iceberg(x,y,s=1){
  return `<path transform="translate(${x} ${y}) scale(${s})" d="M-40 0 L-26 -40 L-10 -30 L4 -62 L22 -36 L40 0 Z" fill="#fff" stroke="${ICEDK}" stroke-width="2" stroke-linejoin="round"/>`;
}
function cactus(x,y,s=1){
  const g = '#4caf50', gd = '#2e7d32';
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-12 0 V-86 Q -12 -100 0 -100 Q 12 -100 12 -86 V0 Z" fill="${g}" stroke="${gd}" stroke-width="2.5"/>
    <path d="M-12 -40 H-26 Q -34 -40 -34 -50 V-70 Q -34 -78 -28 -78 Q -22 -78 -22 -70 V-54 H-12" fill="${g}" stroke="${gd}" stroke-width="2.5"/>
    <path d="M12 -52 H24 Q 32 -52 32 -62 V-76 Q 32 -84 26 -84 Q 20 -84 20 -76 V-64 H12" fill="${g}" stroke="${gd}" stroke-width="2.5"/>
    <path d="M-4 -92 V-6 M4 -92 V-6" stroke="${gd}" stroke-width="1.5"/>
    <path d="M-14 -70 l-5 -2 M14 -30 l5 -2 M-14 -20 l-5 2 M14 -80 l5 -2 M-36 -64 l-5 0 M34 -70 l5 0" stroke="#333" stroke-width="1.3"/>
    <circle cx="0" cy="-102" r="5" fill="#ff7aa8" stroke="#c2185b" stroke-width="1.2"/></g>`;
}
function rock(x,y,s=1){
  return `<path transform="translate(${x} ${y}) scale(${s})" d="M-30 0 Q -34 -18 -18 -26 Q -6 -38 10 -30 Q 30 -26 32 -8 L34 0 Z" fill="#b3a18a" stroke="#7d6a52" stroke-width="2"/>`;
}
function mesa(x,y,s=1){
  return `<path transform="translate(${x} ${y}) scale(${s})" d="M-60 0 L-46 -46 L46 -46 L60 0 Z" fill="#d98c5f" stroke="#a35a32" stroke-width="2"/><path transform="translate(${x} ${y}) scale(${s})" d="M-50 -30 H50 M-55 -15 H55" stroke="#a35a32" stroke-width="1.5"/>`;
}
function penguin(x,y,s=1,o={}){
  const rot = o.rot ? ` rotate(${o.rot})` : '';
  return `<g transform="translate(${x} ${y}) scale(${s})${rot}">
    ${o.blubber ? `<ellipse cx="0" cy="-34" rx="29" ry="39" fill="#ffe8a3" stroke="#e0a800" stroke-width="2" stroke-dasharray="5 3"/>` : ''}
    <ellipse cx="0" cy="-34" rx="22" ry="32" fill="#222" stroke="#000" stroke-width="2"/>
    <ellipse cx="0" cy="-28" rx="15" ry="24" fill="#fff" stroke="#999" stroke-width="1"/>
    <path d="M-21 -40 Q -34 -26 -26 -12" stroke="#222" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M21 -40 Q 34 -26 26 -12" stroke="#222" stroke-width="7" fill="none" stroke-linecap="round"/>
    <circle cx="-7" cy="-52" r="4.5" fill="#fff" stroke="#000" stroke-width="1"/><circle cx="7" cy="-52" r="4.5" fill="#fff" stroke="#000" stroke-width="1"/>
    <circle cx="-6" cy="-52" r="2.2" fill="#111"/><circle cx="8" cy="-52" r="2.2" fill="#111"/>
    <path d="M-5 -46 L0 -40 L5 -46 Z" fill="#ff9f1c" stroke="#c96f00" stroke-width="1.2"/>
    <ellipse cx="-9" cy="-1" rx="8" ry="3.5" fill="#ff9f1c" stroke="#c96f00" stroke-width="1.2"/><ellipse cx="9" cy="-1" rx="8" ry="3.5" fill="#ff9f1c" stroke="#c96f00" stroke-width="1.2"/>
  </g>`;
}
function fish(x,y,s=1,c='#ff9f1c',flip=false){
  return `<g transform="translate(${x} ${y}) scale(${flip?-s:s} ${s})"><path d="M-18 0 Q 0 -14 16 0 Q 0 14 -18 0 Z" fill="${c}" stroke="#00000066" stroke-width="1.5"/><path d="M-16 0 L-28 -9 L-28 9 Z" fill="${c}" stroke="#00000066" stroke-width="1.5"/><circle cx="8" cy="-2" r="2" fill="#111"/></g>`;
}
function camel(x,y,s=1){
  const c = '#c99a5e', d = '#8b6233';
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-30 -20 L-32 0 M-18 -20 L-18 0 M18 -20 L18 0 M30 -20 L32 0" stroke="${c}" stroke-width="7" stroke-linecap="round"/>
    <path d="M-40 -30 Q -42 -46 -26 -48 Q -18 -72 0 -50 Q 14 -72 26 -48 Q 40 -46 40 -30 Q 40 -18 -40 -18 Z" fill="${c}" stroke="${d}" stroke-width="2"/>
    <path d="M36 -36 Q 52 -40 54 -62" stroke="${c}" stroke-width="12" fill="none" stroke-linecap="round"/>
    <ellipse cx="60" cy="-64" rx="13" ry="8" fill="${c}" stroke="${d}" stroke-width="2"/>
    <circle cx="60" cy="-67" r="2" fill="#111"/><path d="M52 -71 l-2 -6" stroke="${d}" stroke-width="3" stroke-linecap="round"/>
    <path d="M-40 -32 Q -50 -26 -46 -16" stroke="${d}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  </g>`;
}
function snake(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-50 0 Q -38 -16 -24 0 T 2 0 T 28 -2" stroke="#6aa84f" stroke-width="10" fill="none" stroke-linecap="round"/>
    <path d="M-50 0 Q -38 -16 -24 0 T 2 0 T 28 -2" stroke="#3d7a2a" stroke-width="2" fill="none" stroke-dasharray="3 6"/>
    <ellipse cx="36" cy="-4" rx="11" ry="8" fill="#6aa84f" stroke="#3d7a2a" stroke-width="2"/>
    <circle cx="39" cy="-7" r="2" fill="#111"/><path d="M46 -3 l7 0 l3 -3 M53 -3 l3 3" stroke="#e8434b" stroke-width="1.5" fill="none"/>
  </g>`;
}
function lizard(x,y,s=1,o={}){
  const c = o.thorny ? '#d9a45b' : '#8bc34a', d = o.thorny ? '#9c6a2a' : '#5a8f2a';
  let spikes = '';
  if (o.thorny) for (let i=0;i<9;i++){ const px = -22 + i*6; spikes += `<path d="M${px} -12 l3 -8 l3 8" fill="${c}" stroke="${d}" stroke-width="1.2"/>`; }
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-24 -4 Q -50 0 -62 -10" stroke="${c}" stroke-width="7" fill="none" stroke-linecap="round"/>
    <path d="M-14 -4 L-22 8 M14 -4 L22 8 M-10 -10 L-20 -18 M12 -10 L22 -18" stroke="${c}" stroke-width="5" stroke-linecap="round"/>
    ${spikes}
    <ellipse cx="0" cy="-7" rx="28" ry="10" fill="${c}" stroke="${d}" stroke-width="2"/>
    <ellipse cx="34" cy="-9" rx="11" ry="8" fill="${c}" stroke="${d}" stroke-width="2"/>
    <circle cx="38" cy="-12" r="2.3" fill="#111"/>
  </g>`;
}
function lungfish(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <path d="M-34 0 Q -10 -14 22 -6 Q 34 -2 34 4 Q 22 12 -10 8 Q -26 6 -34 0 Z" fill="#8a9a5b" stroke="#55622f" stroke-width="2"/>
    <path d="M-34 0 L-44 -6 L-44 6 Z" fill="#8a9a5b" stroke="#55622f" stroke-width="2"/>
    <circle cx="26" cy="-1" r="2.2" fill="#111"/><path d="M-4 8 l-4 8 M8 8 l-2 8" stroke="#55622f" stroke-width="2"/>
  </g>`;
}
function moonStars(){
  let s = `<circle cx="262" cy="36" r="18" fill="#fff6c2" stroke="#e0c35a" stroke-width="2"/><circle cx="271" cy="30" r="15" fill="#253a6b"/>`;
  for (const [x,y] of [[40,30],[90,52],[150,24],[200,60],[120,80],[296,90],[20,84]]) s += sparkle(x,y,0.6,'#fff6c2');
  return s;
}
function nightSky(id){
  return `<defs><linearGradient id="n${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2a52"/><stop offset="1" stop-color="#3f4f80"/></linearGradient></defs><rect width="312" height="210" fill="url(#n${id})"/>`;
}
function globe(x,y,r){
  return `<g><circle cx="${x}" cy="${y}" r="${r}" fill="#6ec1ff" stroke="#2b7bbf" stroke-width="2.5"/>
    <path d="M${x-r*0.55} ${y-r*0.35} Q ${x-r*0.2} ${y-r*0.6} ${x+r*0.05} ${y-r*0.4} Q ${x+r*0.35} ${y-r*0.1} ${x+r*0.1} ${y+r*0.35} Q ${x-r*0.1} ${y+r*0.6} ${x-r*0.25} ${y+r*0.2} Q ${x-r*0.55} ${y} ${x-r*0.55} ${y-r*0.35} Z" fill="#7cc66b" stroke="#4e9a3a" stroke-width="2"/>
    <path d="M${x-r*0.45} ${y-r*0.3} Q ${x-r*0.15} ${y-r*0.45} ${x+r*0.05} ${y-r*0.3} Q ${x+r*0.1} ${y-r*0.1} ${x-r*0.1} ${y-r*0.05} Q ${x-r*0.4} ${y-r*0.05} ${x-r*0.45} ${y-r*0.3} Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>
    <path d="M${x+r*0.4} ${y-r*0.2} Q ${x+r*0.7} ${y-r*0.3} ${x+r*0.75} ${y} Q ${x+r*0.55} ${y+r*0.3} ${x+r*0.4} ${y+r*0.1} Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>
    <path d="M${x-r*0.75} ${y+r*0.65} Q ${x} ${y+r*0.85} ${x+r*0.75} ${y+r*0.65} A ${r} ${r} 0 0 1 ${x-r*0.75} ${y+r*0.65} Z" fill="#fff" stroke="${ICEDK}" stroke-width="1.5"/>
    <path d="M${x-r*0.6} ${y-r*0.8} Q ${x} ${y-r*0.92} ${x+r*0.6} ${y-r*0.8} A ${r} ${r} 0 0 0 ${x-r*0.6} ${y-r*0.8} Z" fill="#fff" stroke="${ICEDK}" stroke-width="1.5"/></g>`;
}
function rainGauge(x,y,s=1){
  let ticks = '';
  for (let i=0;i<=10;i++){ const ty = -8 - i*9; ticks += `<line x1="-14" y1="${ty}" x2="${i%5===0?-2:-7}" y2="${ty}" stroke="#333" stroke-width="1.5"/>`; if (i%5===0) ticks += `<text x="18" y="${ty+4}" font-family="Andika" font-size="11" fill="#333">${i}</text>`; }
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-14" y="-104" width="28" height="104" rx="4" fill="#e9f6ff" stroke="#333" stroke-width="2"/>
    <rect x="-12" y="-20" width="24" height="18" fill="#5bb8ff" opacity="0.9"/>${ticks}<path d="M-22 -112 L22 -112 L14 -104 L-14 -104 Z" fill="#cfe8f7" stroke="#333" stroke-width="2"/></g>`;
}
function crack(){
  return `<path d="M30 170 l20 10 l-6 14 l22 6 M140 176 l14 -8 l20 10 l8 -10 M220 184 l18 8 l-4 10 l26 2" stroke="#a37a3c" stroke-width="2.5" fill="none" stroke-linejoin="round"/>`;
}
function mudPit(){
  return `<rect x="0" y="120" width="312" height="90" fill="#8d6e4c"/><path d="M0 120 Q 80 110 160 122 T 312 118" stroke="#6b4f33" stroke-width="3" fill="none"/>
    <ellipse cx="160" cy="168" rx="70" ry="28" fill="#6b4f33" stroke="#4a3622" stroke-width="2"/>`;
}
function kidThink(x,y,s){ return person({x,y,s,hair:'#2b1b0e',hairStyle:'curly',shirt:'#ff8c42',skin:'#c68a5e',arms:'face',armsL:'down',mood:'happy'}); }

const DS = {
  title: id => titleSign(id, 'The', 'Desert', {
    back: sun(268,36,14) + dunes(250,312,280),
    front: cactus(26,270,0.75) + cactus(292,262,0.55) + lizard(160,268,0.55) }),
  dryLand: id => P(sky(W,H,id) + sun(260,40,20) + `<path d="M0 150 H312 V210 H0 Z" fill="${SAND}"/>` + crack() + cloud(60,40,0.9) + drop(78,74,0.9) + cactus(170,160,0.5) + rock(250,166,0.8)),
  hotCold: id => P(sky(W,H,id) + `<rect x="156" width="156" height="210" fill="#dff1ff"/>` + sun(60,40,16) + `<path d="M0 160 Q 70 140 156 160 V210 H0 Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>` + cactus(90,176,0.55) + thermometer(30,150,0.8,true)
      + `<path d="M156 160 L210 150 L260 158 L312 148 V210 H156 Z" fill="#fff" stroke="${ICEDK}" stroke-width="2"/>` + iceberg(270,150,0.7) + penguin(206,176,0.75) + thermometer(292,196,0.6,false) + snowflake(190,40) + snowflake(240,70) + snowflake(290,30)
      + `<line x1="156" y1="0" x2="156" y2="210" stroke="#2b2b2b" stroke-width="3"/>`),
  rocky: id => P(sky(W,H,id) + sun(40,36,14) + `<path d="M0 160 H312 V210 H0 Z" fill="#c9a67c"/>` + mesa(220,162,1.3) + rock(60,180,1.2) + rock(140,192,0.9) + rock(280,196,0.8) + cactus(110,176,0.45) + noSign(250,60,22) + `<path d="M232 70 Q 250 50 268 70 Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>`),
  sahara: id => P(sky(W,H,id) + sun(270,34,16) + dunes(130) + camel(130,176,0.9) + `<path d="M20 196 l40 0 M300 196 l-40 0" stroke="#2b2b2b" stroke-width="2.5"/>` + arrow(60,196,14,196) + arrow(260,196,306,196) + label(156,202,'very big!',16)),
  coldIce: id => P(sky(W,H,id) + snowflake(40,30) + snowflake(120,50) + snowflake(220,24) + snowflake(290,60) + iceberg(250,150,1.2) + iceGround(160) + penguin(110,180,0.95) + penguin(170,176,0.7)),
  blubber: id => P(sky(W,H,id) + iceGround(170) + penguin(150,186,1.35,{blubber:true}) + snowflake(40,40) + snowflake(70,110) + snowflake(250,40) + snowflake(280,120) + label(250,180,'fat',18,'#b8901a') + arrow(238,172,196,150,'#b8901a',3)),
  dive: id => P(`<rect width="312" height="210" fill="#4aa3df"/><rect width="312" height="34" fill="#dff1ff"/><path d="M0 34 Q 40 28 80 34 T 160 34 T 240 34 T 312 34" stroke="#fff" stroke-width="3" fill="none"/>` + penguin(110,110,0.8,{rot:150}) + fish(220,150,1.2) + fish(260,176,0.9,'#ffd23f') + fish(180,186,0.8) + `<circle cx="90" cy="60" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="80" cy="46" r="3" fill="none" stroke="#fff" stroke-width="2"/>` + arrow(40,50,40,190,'#fff',4)),
  animals: id => P(sky(W,H,id) + sun(40,34,14) + dunes(150) + camel(220,172,0.75) + snake(70,192,0.8) + lizard(140,160,0.6)),
  shadeRest: id => P(sky(W,H,id) + sun(50,40,22) + dunes(150) + `<path d="M140 90 Q 160 60 220 70 Q 290 76 300 150 L 140 150 Z" fill="#b3a18a" stroke="#7d6a52" stroke-width="2"/><path d="M150 150 H300 V190 H130 Z" fill="#00000022"/>` + lizard(190,172,0.55) + snake(250,186,0.55) + label(70,112,'z z',18,'#5b6b7a')),
  night: id => P(nightSky(id) + moonStars() + `<path d="M0 150 Q 80 130 160 150 T 312 146 V210 H0 Z" fill="#7a6a4f"/>` + snake(80,180,0.8) + lizard(210,168,0.6) + cactus(286,170,0.5)),
  dayNight: id => P(sky(W,H,id) + `<path d="M156 0 H312 V210 H156 Z" fill="#253a6b"/>` + sun(40,34,13) + `<circle cx="276" cy="34" r="14" fill="#fff6c2" stroke="#e0c35a" stroke-width="2"/><circle cx="283" cy="29" r="12" fill="#253a6b"/>` + sparkle(200,40,0.6,'#fff6c2') + sparkle(230,80,0.5,'#fff6c2')
      + `<path d="M0 150 Q 80 136 156 150 V210 H0 Z" fill="${SAND}"/><path d="M156 150 Q 230 136 312 150 V210 H156 Z" fill="#7a6a4f"/>` + `<path d="M40 100 Q 80 76 130 100 L 130 150 L 40 150 Z" fill="#b3a18a" stroke="#7d6a52" stroke-width="2"/>` + lizard(88,166,0.45) + label(90,128,'z z',14,'#5b6b7a') + snake(230,180,0.6) + lizard(250,152,0.45) + `<line x1="156" y1="0" x2="156" y2="210" stroke="#2b2b2b" stroke-width="3"/>`),
  lungfish: id => P(sky(W,H,id) + sun(270,34,14) + mudPit() + lungfish(160,170,1.1) + `<circle cx="196" cy="140" r="4" fill="none" stroke="#fff" stroke-width="2"/><circle cx="206" cy="128" r="3" fill="none" stroke="#fff" stroke-width="2"/>` + arrow(80,130,110,160,'#fff',3)),
  cactus: id => P(sky(W,H,id) + cloud(60,30,0.9) + drop(70,64,0.8) + drop(96,80,0.8) + drop(50,90,0.8) + `<rect x="0" y="130" width="312" height="80" fill="#c9a67c"/><line x1="0" y1="130" x2="312" y2="130" stroke="#8d6e4c" stroke-width="2"/>`
      + `<path d="M156 132 Q 110 150 40 146 M156 132 Q 210 152 280 144 M156 134 Q 120 160 80 170 M156 134 Q 196 160 240 172 M156 136 L156 156" stroke="#8d6e4c" stroke-width="3" fill="none" stroke-linecap="round"/>` + cactus(156,132,1.0)),
  thinkDesert: id => P(`<rect width="312" height="210" fill="#f7efe0"/><rect y="170" width="312" height="40" fill="#d8b98a"/>` + kidThink(70,196,1.15) + bubble(210,72,90,56,110,100, sun(178,52,12) + `<path d="M130 106 Q 170 80 210 100 T 290 96 V 118 H 130 Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="1.5"/>` + cactus(250,108,0.35) + label(226,64,'?',30,'#e8434b'))),
  notAll: id => P(`<rect width="156" height="210" fill="#dff1ff"/><rect x="156" width="156" height="210" fill="#bfe6ff"/>` + iceGround(160).replace('M0','M0') + penguin(80,180,0.7) + snowflake(30,40) + snowflake(110,30)
      + `<path d="M156 160 H312 V210 H156 Z" fill="#c9a67c"/>` + mesa(236,162,0.95) + rock(186,190,0.7) + sun(290,30,12) + label(80,30,'cold',20,'#2b7bbf') + label(234,72,'no sand',18,'#a35a32') + `<line x1="156" y1="0" x2="156" y2="210" stroke="#2b2b2b" stroke-width="3"/>`),
  rainGauge: id => P(sky(W,H,id) + sun(270,34,14) + dunes(170) + rainGauge(110,186,1.2) + drop(100,40,0.8) + label(220,96,'less than',18) + label(220,120,'10 inches',22,'#2b7bbf') + label(220,142,'of rain a year',16)),
  globe: id => P(`<rect width="312" height="210" fill="#1b2a52"/>` + sparkle(30,30,0.6,'#fff6c2') + sparkle(280,40,0.6,'#fff6c2') + sparkle(40,180,0.5,'#fff6c2') + globe(156,105,88) + label(60,186,'cold desert',14,'#fff') + arrow(80,174,104,180,'#fff',2.5) + label(262,180,'hot desert',14,'#fff') + arrow(236,170,212,118,'#fff',2.5)),
  thorny: id => P(sky(W,H,id) + sun(40,34,13) + dunes(160) + lizard(160,170,1.5,{thorny:true}) + drop(70,96,0.9) + drop(100,120,0.7) + drop(120,90,0.7) + `<path d="M130 140 Q 180 132 210 150" stroke="#2f8de0" stroke-width="2.5" fill="none" stroke-dasharray="4 4"/>` + arrow(196,146,212,154,'#2f8de0',2.5)),
};

const DI = { // icons for word cards (150 x 100)
  sun: () => sun(75,50,22),
  hot: () => thermometer(75,80,1.2,true) + sun(120,28,10),
  sand: () => `<path d="M0 70 Q 50 30 90 62 T 150 56 V100 H0 Z" fill="${SAND}" stroke="${SANDDK}" stroke-width="2"/>`,
  rocks: () => rock(50,84,1.1) + rock(108,90,0.8) + rock(84,96,0.6),
  ice: () => iceberg(75,88,1.2) + snowflake(20,20) + snowflake(130,24),
  big: () => camel(62,92,0.8) + lizard(128,88,0.3),
  fat: () => penguin(75,96,1.2,{blubber:true}),
  dip: () => `<rect width="150" height="100" fill="#bfe3f5"/>` + penguin(60,46,0.6,{rot:150}) + fish(118,74,1),
  fish: () => fish(75,50,2),
  snake: () => snake(70,62,1.1),
  camel: () => camel(60,92,0.85),
  dig: () => `<rect y="40" width="150" height="60" fill="#8d6e4c"/>` + lungfish(80,72,1),
  mud: () => `<path d="M10 70 Q 30 40 70 52 Q 110 34 140 62 Q 140 92 80 90 Q 10 94 10 70 Z" fill="#8d6e4c" stroke="#4a3622" stroke-width="2"/>`,
  cactus: () => cactus(75,98,0.85),
  dry: () => `<rect y="50" width="150" height="50" fill="${SAND}"/>` + crack().replace(/(\d+) (\d+)/g, (m, a, b) => m) ,
};

const DESERT_ICON = () => cactus(40,56,0.48);
