// Art for "Fred the Fireman"
const FRED = o => person(Object.assign({ skin:'#f2c9a0', hair:'#6b3e1e', gear:true, helmet:true, mood:'happy' }, o));
const TEACHER = o => person(Object.assign({ skin:'#e9b48a', hair:'#b5651d', hairStyle:'bun', shirt:'#8e5cc2', dress:true, glasses:true, mood:'happy' }, o));
const KIDS = [
  { skin:'#c68a5e', hair:'#2b1b0e', hairStyle:'curly', shirt:'#ff8c42', pants:'#33415c' },
  { skin:'#f2c9a0', hair:'#e0b04a', hairStyle:'pony',  shirt:'#4caf50', pants:'#5b4a8a' },
  { skin:'#8d5a3b', hair:'#1b1008', hairStyle:'short', shirt:'#3a8fc4', pants:'#444' },
  { skin:'#f5d0b0', hair:'#7a3b12', hairStyle:'long',  shirt:'#e85d9a', pants:'#33415c' },
];
const KID = (i, o) => person(Object.assign({}, KIDS[i % KIDS.length], o));

function classroom(id){
  return `<rect width="312" height="210" fill="#f7efe0"/><rect y="168" width="312" height="42" fill="#d8b98a"/><line x1="0" y1="168" x2="312" y2="168" stroke="#a88a5a" stroke-width="2"/>
    <rect x="96" y="18" width="150" height="72" rx="4" fill="#fff" stroke="#8a8a8a" stroke-width="4"/>
    <rect x="16" y="26" width="56" height="58" fill="#bfe6ff" stroke="#8b5a2b" stroke-width="4"/><line x1="44" y1="26" x2="44" y2="84" stroke="#8b5a2b" stroke-width="3"/><line x1="16" y1="55" x2="72" y2="55" stroke="#8b5a2b" stroke-width="3"/>`;
}
function board(lines, size=16){
  return lines.map((t, i) => label(171, 44 + i*20, t, size, '#2b2b2b')).join('');
}
function door(x){ return `<rect x="${x}" y="70" width="52" height="98" fill="#b07a45" stroke="#6b4220" stroke-width="3"/><circle cx="${x+42}" cy="122" r="4" fill="#ffd23f" stroke="#b8901a"/>`; }
function fireTruck(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})">
    <rect x="-70" y="-46" width="96" height="40" rx="4" fill="#d62828" stroke="#8f1515" stroke-width="2.5"/>
    <path d="M26 -46 H50 Q 62 -46 66 -30 L70 -6 H26 Z" fill="#d62828" stroke="#8f1515" stroke-width="2.5" stroke-linejoin="round"/>
    <path d="M32 -40 H48 Q 56 -40 58 -28 H32 Z" fill="#bfe6ff" stroke="#555" stroke-width="2"/>
    <rect x="-66" y="-58" width="84" height="8" fill="#ccc" stroke="#777" stroke-width="2"/>
    ${[-58,-44,-30,-16,-2,12].map(lx => `<line x1="${lx}" y1="-58" x2="${lx}" y2="-50" stroke="#777" stroke-width="2"/>`).join('')}
    <rect x="34" y="-54" width="12" height="8" rx="2" fill="#3a8fc4" stroke="#1f5f8f" stroke-width="1.5"/>
    <rect x="-66" y="-30" width="88" height="5" fill="#fff" stroke="#999" stroke-width="1"/>
    <circle cx="-44" cy="-4" r="11" fill="#333" stroke="#111" stroke-width="2"/><circle cx="-44" cy="-4" r="4.5" fill="#bbb"/>
    <circle cx="44" cy="-4" r="11" fill="#333" stroke="#111" stroke-width="2"/><circle cx="44" cy="-4" r="4.5" fill="#bbb"/></g>`;
}
function axe(x,y,s=1,rot=-30){
  return `<g transform="translate(${x} ${y}) scale(${s}) rotate(${rot})"><rect x="-4" y="-60" width="8" height="70" rx="3" fill="#ffd23f" stroke="#b8901a" stroke-width="2"/>
    <path d="M4 -58 L26 -64 Q 34 -50 26 -36 L4 -42 Z" fill="#d62828" stroke="#8f1515" stroke-width="2"/><path d="M-4 -56 L-16 -52 L-4 -46 Z" fill="#999" stroke="#555" stroke-width="2"/></g>`;
}
function hose(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><circle r="26" fill="none" stroke="#8a8a8a" stroke-width="9"/><circle r="15" fill="none" stroke="#8a8a8a" stroke-width="9"/><circle r="26" fill="none" stroke="#5a5a5a" stroke-width="1.5"/>
    <path d="M24 10 Q 40 18 50 8" stroke="#8a8a8a" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M48 2 L64 -6 L66 2 L52 12 Z" fill="#ffd23f" stroke="#b8901a" stroke-width="2"/></g>`;
}
function spray(x,y,s=1){
  let d = '';
  for (let i=0;i<8;i++) d += drop(x + i*9*s, y - Math.sin(i/2)*10*s + i*2*s, 0.55*s);
  return d;
}
function flame(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M0 0 Q -20 -10 -12 -34 Q -6 -22 0 -24 Q -4 -40 8 -52 Q 8 -32 20 -24 Q 26 -12 0 0 Z" fill="#ff8c1a" stroke="#d9480f" stroke-width="2"/><path d="M0 -4 Q -8 -10 -4 -20 Q 2 -14 6 -18 Q 12 -10 0 -4 Z" fill="#ffd23f"/></g>`;
}
function firstAid(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-24" y="-30" width="48" height="34" rx="5" fill="#fff" stroke="#c0392b" stroke-width="2.5"/><path d="M-8 -36 H8 V-30 H-8 Z" fill="#fff" stroke="#c0392b" stroke-width="2"/><path d="M-4 -24 H4 V-17 H11 V-9 H4 V-2 H-4 V-9 H-11 V-17 H-4 Z" fill="#e02424"/></g>`;
}
function matches(x,y,s=1){
  let st = '';
  for (const [dx,r] of [[-10,-14],[0,-4],[10,8]]) st += `<g transform="rotate(${r} ${dx} 0)"><rect x="${dx-2}" y="-40" width="4" height="40" fill="#f2d7a6" stroke="#b8901a" stroke-width="1"/><ellipse cx="${dx}" cy="-41" rx="4" ry="5" fill="#d62828"/></g>`;
  return `<g transform="translate(${x} ${y}) scale(${s})">${st}<rect x="-22" y="-16" width="44" height="26" rx="3" fill="#3a8fc4" stroke="#1f5f8f" stroke-width="2"/><rect x="-16" y="-10" width="32" height="8" fill="#ffd23f"/></g>`;
}
function stove(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-36" y="-50" width="72" height="50" rx="4" fill="#e6e6e6" stroke="#777" stroke-width="2.5"/><rect x="-28" y="-36" width="56" height="28" rx="3" fill="#555" stroke="#333" stroke-width="2"/>
    <circle cx="-22" cy="-44" r="3" fill="#333"/><circle cx="-10" cy="-44" r="3" fill="#333"/><circle cx="10" cy="-44" r="3" fill="#333"/><circle cx="22" cy="-44" r="3" fill="#333"/>
    <path d="M-24 -52 H24 L20 -76 H-20 Z" fill="#9aa3ad" stroke="#59616a" stroke-width="2.5" stroke-linejoin="round"/><path d="M20 -66 H38" stroke="#59616a" stroke-width="5" stroke-linecap="round"/>
    <path d="M-10 -82 q 4 -6 0 -12 M2 -84 q 4 -6 0 -12" stroke="#999" stroke-width="2" fill="none"/></g>`;
}
function smoke(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})" fill="#9e9e9e" stroke="#6e6e6e" stroke-width="2"><circle cx="0" cy="0" r="18"/><circle cx="22" cy="-6" r="22"/><circle cx="48" cy="2" r="17"/><circle cx="70" cy="-4" r="20"/><circle cx="96" cy="2" r="16"/><rect x="0" y="0" width="96" height="16" stroke="none"/></g>`;
}
function exitSign(x,y,s=1){ return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-26" y="-12" width="52" height="24" rx="3" fill="#2fa84f" stroke="#1d7a36" stroke-width="2"/>${label(0,6,'EXIT',16,'#fff')}</g>`; }
function tag(x,y,t,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-22 -12 H18 L26 0 L18 12 H-22 Z" fill="#fff59d" stroke="#b8901a" stroke-width="2" stroke-linejoin="round"/><circle cx="18" cy="0" r="2.5" fill="#fff" stroke="#b8901a"/>${label(-2,6,t,15,'#222')}</g>`;
}
function jacket(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-18 -40 L-34 -30 L-40 2 L-28 4 L-24 -16 L-22 10 H22 L24 -16 L28 4 L40 2 L34 -30 L18 -40 Q 0 -30 -18 -40 Z" fill="#e5b52a" stroke="#9c7a12" stroke-width="2.5" stroke-linejoin="round"/>
    <rect x="-22" y="-6" width="44" height="5" fill="#e8e8e8" stroke="#999"/><line x1="0" y1="-34" x2="0" y2="10" stroke="#9c7a12" stroke-width="2"/></g>`;
}
function boots(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M-30 -36 H-12 V-8 H-2 V0 H-30 Z" fill="#333" stroke="#111" stroke-width="2" stroke-linejoin="round"/><path d="M6 -36 H24 V-8 H34 V0 H6 Z" fill="#333" stroke="#111" stroke-width="2" stroke-linejoin="round"/><rect x="-30" y="-20" width="18" height="4" fill="#e5b52a"/><rect x="6" y="-20" width="18" height="4" fill="#e5b52a"/></g>`;
}
function maskTank(x,y,s=1){
  return `<g transform="translate(${x} ${y}) scale(${s})"><rect x="-10" y="-50" width="24" height="50" rx="10" fill="#9aa3ad" stroke="#59616a" stroke-width="2.5"/><ellipse cx="-30" cy="-30" rx="15" ry="18" fill="#bfe3f5" stroke="#333" stroke-width="2.5"/><circle cx="-30" cy="-16" r="4" fill="#555"/><path d="M-26 -14 Q -10 0 -2 -10" stroke="#333" stroke-width="3" fill="none"/></g>`;
}
function stopSign(x,y,s=1){
  const pts = []; for (let i=0;i<8;i++){ const a = (22.5 + i*45)*Math.PI/180; pts.push(`${f(24*Math.cos(a))},${f(24*Math.sin(a))}`); }
  return `<g transform="translate(${x} ${y}) scale(${s})"><polygon points="${pts.join(' ')}" fill="#d62828" stroke="#8f1515" stroke-width="2.5"/>${label(0,5,'STOP',13,'#fff')}</g>`;
}
function motion(x,y){ return `<path d="M${x} ${y} q 10 -14 20 0 M${x+4} ${y+10} q 8 -10 16 0" stroke="#555" stroke-width="2.5" fill="none" stroke-linecap="round"/>`; }
function familyAtTree(x,y,s=1){
  return tree(x, y, 1.1*s) + person({x:x-38*s, y, s:0.62*s, skin:'#e9b48a', hair:'#3b2412', shirt:'#5b7bd5', arms:'wave'}) + person({x:x+38*s, y, s:0.58*s, skin:'#e9b48a', hair:'#b5651d', hairStyle:'long', shirt:'#e85d9a', dress:true}) + KID(0, {x:x+8*s, y, s:0.42*s, arms:'cheer', mood:'excited'});
}

const FS = {
  title: id => titleSign(id, 'Fred the', 'Fireman', {
    back: `<path d="M0 236 H312 V280 H0 Z" fill="#9e9e9e"/>` + fireTruck(250,236,0.8),
    front: FRED({x:44, y:272, s:0.62, arms:'wave', armsL:'down'}) }),
  classGlad: id => P(classroom(id) + board(['A fireman','will visit!'],18) + KID(0,{x:60,y:200,s:0.62,arms:'cheer',mood:'excited'}) + KID(1,{x:120,y:204,s:0.58,arms:'up',mood:'excited'}) + KID(2,{x:180,y:200,s:0.6,arms:'cheer',mood:'excited'}) + TEACHER({x:264,y:200,s:0.82,arms:'point',mood:'talk'}) + sparkle(30,110,0.8) + sparkle(220,110,0.8)),
  fredArrives: id => P(classroom(id) + board(['Welcome,','Fred!'],18) + door(250) + FRED({x:276,y:200,s:0.8,arms:'wave'}) + KID(1,{x:60,y:204,s:0.58,arms:'up',mood:'excited'}) + KID(2,{x:120,y:204,s:0.58,mood:'excited'}) + TEACHER({x:186,y:200,s:0.8,arms:'point',mood:'happy'})),
  strong: id => P(classroom(id) + board(['Firefighters','are strong!'],17) + FRED({x:110,y:200,s:0.9,arms:'cheer',mood:'excited',tank:true}) + `<rect x="166" y="150" width="70" height="40" rx="8" fill="#e5b52a" stroke="#9c7a12" stroke-width="2.5"/>` + label(201,177,'heavy',16) + KID(3,{x:274,y:204,s:0.55,mood:'excited'})),
  gear: id => P(sky(W,H,id) + `<rect y="176" width="312" height="34" fill="#9e9e9e"/>` + FRED({x:96,y:196,s:0.95,mask:true,tank:true,arms:'hip'}) + jacket(218,96,0.85) + boots(222,172,0.75) + label(236,40,'big and',16) + label(236,58,'heavy!',16)),
  gearWeights: id => P(classroom(id) + jacket(52,124,0.85) + tag(52,150,'15 lb') + boots(150,140,0.7) + `<path d="M140 92 H164 L168 132 H136 Z" fill="#e5b52a" stroke="#9c7a12" stroke-width="2"/>` + tag(150,158,'30 lb') + maskTank(262,140,0.85) + tag(250,158,'30 lb')),
  tools: id => P(sky(W,H,id) + `<rect y="170" width="312" height="40" fill="#9e9e9e"/>` + fireTruck(250,176,0.7) + axe(60,166,1.1,-20) + hose(140,140,1.1) + spray(206,120,1.2)),
  emt: id => P(classroom(id) + board(['EMT'],22) + FRED({x:100,y:200,s:0.85,arms:'front'}) + KID(3,{x:180,y:204,s:0.6,arms:'front',armsL:'down',mood:'happy'}) + `<rect x="194" y="150" width="14" height="7" rx="2" fill="#f5d0b0" stroke="#c99a74" stroke-width="1.5" transform="rotate(20 201 153)"/>` + firstAid(262,196,0.9)),
  calls: id => P(sky(W,H,id) + `<rect y="170" width="312" height="40" fill="#9e9e9e"/>` + fireTruck(150,186,1.05) + `<path d="M182 104 q 12 -10 0 -20 M192 108 q 18 -16 0 -30" stroke="#3a8fc4" stroke-width="3" fill="none" stroke-linecap="round"/>` + `<g transform="translate(50 70)"><rect x="-20" y="-28" width="40" height="56" rx="6" fill="#333" stroke="#111" stroke-width="2"/><rect x="-15" y="-21" width="30" height="36" fill="#bfe6ff"/>${label(0,4,'911',13,'#d62828')}</g>`),
  threePs: id => P(classroom(id) + board(['The Three Ps:','Prevent • Plan','• Practice'],15) + FRED({x:270,y:200,s:0.8,arms:'point',armsL:'down',mood:'talk',rot:0}).replace('scale(0.8)','scale(-0.8 0.8)') + KID(0,{x:60,y:204,s:0.55}) + KID(2,{x:130,y:204,s:0.55})),
  noMatches: id => P(classroom(id) + board(['Never play','with matches!'],16) + matches(150,170,1.4) + flame(150,120,0.6) + noSign(150,146,48) + FRED({x:262,y:200,s:0.75,arms:'point',mood:'talk'}).replace('scale(0.75)','scale(-0.75 0.75)')),
  noCook: id => P(`<rect width="312" height="210" fill="#fdf3e1"/><rect y="168" width="312" height="42" fill="#cfd8dc"/>` + stove(140,170,1.2) + noSign(140,112,58) + KID(1,{x:250,y:200,s:0.62,mood:'worried'})),
  prevent: id => P(classroom(id) + board(['Prevent'],22) + matches(80,170,1) + noSign(80,148,36) + stove(220,180,0.8) + noSign(220,136,44)),
  plan: id => P(sky(W,H,id) + ground(176) + house(70,176,1.2) + arrow(124,150,186,150,'#e02424',5) + label(156,138,'get out!',15,'#e02424') + familyAtTree(250,194,0.8)),
  meetSpot: id => P(sky(W,H,id) + ground(178) + house(60,170,0.8) + familyAtTree(200,194,1)),
  smoke: id => P(`<rect width="312" height="210" fill="#f7efe0"/><rect y="168" width="312" height="42" fill="#d8b98a"/>` + smoke(20,40,1.6) + smoke(150,70,1) + door(246) + exitSign(272,50,0.9) + `<g transform="translate(110 168) rotate(-72)">${KID(2,{x:0,y:0,s:0.55}).replace(/^<g transform="translate\(0 0\) scale\(0.55\)">/,'<g transform="scale(0.55)">')}</g>` + arrow(160,150,236,150,'#2fa84f',5) + label(130,108,'Get low!',17,'#d62828')),
  sdr: id => P(sky(W,H,id) + `<rect y="176" width="312" height="34" fill="#c9e3a5"/>` + KID(0,{x:46,y:196,s:0.62,arms:'down'}) + label(46,30,'stop',18,'#d62828')
      + `<g transform="translate(186 190) rotate(-90)">${KID(1,{x:0,y:0,s:0.55,arms:'face'})}</g>` + label(150,30,'drop',18,'#d62828')
      + `<g transform="translate(222 186) rotate(90)">${KID(3,{x:0,y:0,s:0.55,arms:'face'})}</g>` + motion(232,140) + motion(266,134) + label(262,30,'roll',18,'#d62828')
      + `<line x1="98" y1="10" x2="98" y2="176" stroke="#2b2b2b" stroke-width="2" stroke-dasharray="5 5"/><line x1="206" y1="10" x2="206" y2="176" stroke="#2b2b2b" stroke-width="2" stroke-dasharray="5 5"/>`),
  thanks: id => P(classroom(id) + board(['Thank you,','Fred!'],18) + FRED({x:270,y:200,s:0.8,arms:'wave'}) + KID(0,{x:46,y:204,s:0.55,arms:'cheer',mood:'excited'}) + KID(1,{x:106,y:204,s:0.55,arms:'up',mood:'excited'}) + KID(3,{x:166,y:204,s:0.55,arms:'cheer',mood:'excited'}) + heart(220,110,1.3) + heart(150,102,1)),
};

const FI = { // word card icons (150 x 100)
  Fred: () => FRED({x:75,y:98,s:0.66}),
  hat: () => `<g transform="translate(75 82) scale(1.8)"><path d="M-20 -4 Q -19 -29 0 -29 Q 19 -29 20 -4 Z" fill="#d62828" stroke="#8f1515" stroke-width="2"/><ellipse cx="0" cy="-4" rx="25" ry="5" fill="#d62828" stroke="#8f1515" stroke-width="2"/><path d="M-6 -26 H6 V-12 L0 -8 L-6 -12 Z" fill="#ffd23f" stroke="#b8901a" stroke-width="1.5"/></g>`,
  red: () => fireTruck(75,86,0.95),
  ax: () => axe(80,94,1.15,-30),
  hose: () => hose(60,52,1.1),
  wet: () => drop(50,44,2) + drop(90,40,1.6) + drop(116,64,1.3) + drop(70,76,1.2),
  mask: () => maskTank(96,90,1.4),
  help: () => firstAid(75,80,1.5),
  stop: () => stopSign(75,50,1.6),
  drop: () => `<g transform="translate(108 76) rotate(-90)">${KID(1,{x:0,y:0,s:0.5,arms:'face'})}</g>`,
  roll: () => `<g transform="translate(42 70) rotate(90)">${KID(3,{x:0,y:0,s:0.5,arms:'face'})}</g>` + motion(52,30) + motion(86,24),
  rug: () => `<rect x="20" y="40" width="110" height="46" rx="4" fill="#c0392b" stroke="#7a1f16" stroke-width="2"/><rect x="30" y="48" width="90" height="30" fill="none" stroke="#ffd23f" stroke-width="3"/><path d="M20 44 h-8 M20 54 h-8 M20 64 h-8 M20 74 h-8 M20 84 h-8 M130 44 h8 M130 54 h8 M130 64 h8 M130 74 h8 M130 84 h8" stroke="#7a1f16" stroke-width="2"/>`,
  kids: () => KID(0,{x:40,y:98,s:0.5,mood:'excited'}) + KID(1,{x:76,y:98,s:0.5,mood:'excited'}) + KID(2,{x:112,y:98,s:0.5,mood:'excited'}),
  plan: () => house(44,90,0.8) + tree(118,92,0.7) + arrow(74,72,100,72,'#e02424',4),
};

const FIRE_ICON = () => `<g transform="translate(40 52)"><path d="M-20 -4 Q -19 -29 0 -29 Q 19 -29 20 -4 Z" fill="#d62828" stroke="#8f1515" stroke-width="2"/><ellipse cx="0" cy="-4" rx="25" ry="5" fill="#d62828" stroke="#8f1515" stroke-width="2"/><path d="M-6 -26 H6 V-12 L0 -8 L-6 -12 Z" fill="#ffd23f" stroke="#b8901a" stroke-width="1.5"/></g>`;
