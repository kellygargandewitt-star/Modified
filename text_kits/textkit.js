// Text-only fluency kit: no pictures. Builds every sheet from one story data file (?s=<name>).
// Scaffold fades by level:  ★ CVC words underlined + heart words boxed
//                           ★★ heart words boxed
//                           ★★★ phrase-cued (/ and //), then the clean grade-level text

// Words that do not follow the usual sound rules (taught "by heart").
// 'the' is left out on purpose: it is everywhere and boxing it clutters the page.
const HEART = new Set(('to do of you your was were said says they their there what who one two once some come done won ' +
  'have give live are from again any many could would should been does very put pull full push only other mother brother ' +
  'father both gone sure eye buy whole whose any were where here our hour four great break nothing').split(/\s+/));
// Final r is left out: words like far and her are r-controlled, not short-vowel.
const CVC = /^[bcdfghjklmnpqrstvwxyz][aeiou][bcdfghjklmnpqstvxz]$/i;

function mark(tok, mode){
  const m = tok.match(/^([“"‘(]*)(.*?)([.,!?;:”"’)]*)$/);
  const [, lead, core, trail] = m;
  const lc = core.toLowerCase();
  if ((mode === 'l1' || mode === 'l2') && HEART.has(lc)) return `${lead}<span class="hw">${core}</span>${trail}`;
  if (mode === 'l1' && CVC.test(core)) return `${lead}<span class="cvc">${core}</span>${trail}`;
  return tok;
}

// mode: l1 | l2 | cued | clean.  withCounts adds a running word total at the end of every printed line.
function passage(el, paras, mode, withCounts, startCount = 0){
  el.classList.add('pwrap', 'mode-' + mode);
  const text = document.createElement('div'); text.className = 'ptext';
  text.innerHTML = paras.map(p => {
    const out = [];
    for (const t of p.split(/\s+/).filter(Boolean)) {
      if (t === '/' || t === '//') { if (mode === 'cued') out[out.length - 1] += `&nbsp;<span class="cue">${t}</span>`; }  // keep the mark on the same line as its word
      else out.push(`<span class="w">${mark(t, mode)}</span>`);
    }
    return '<p>' + out.join(' ') + '</p>';
  }).join('');
  el.appendChild(text);
  if (!withCounts) return;
  const layout = () => {
    el.querySelectorAll('.cnt').forEach(c => c.remove());
    const base = el.getBoundingClientRect().top;
    const rows = [];
    el.querySelectorAll('.w').forEach(w => {
      const r = w.getBoundingClientRect(), cy = r.top + r.height / 2;
      const row = rows.find(x => Math.abs(x.cy - cy) < 8);
      if (row) row.n++; else rows.push({ cy, n: 1 });
    });
    let total = startCount;
    rows.forEach(r => {
      total += r.n;
      const c = document.createElement('div'); c.className = 'cnt'; c.textContent = total;
      c.style.top = (r.cy - base - 10) + 'px';
      el.appendChild(c);
    });
  };
  return layout;
}
const cleanText = s => s.replace(/\s\/\/?(?=\s|$)/g, '');

function sheet(cls = ''){ const d = document.createElement('div'); d.className = 'sheet ' + cls; document.getElementById('book').appendChild(d); return d; }
function header(title, stars = '', right = 'Name: ______________________'){
  return `<header><h1>${title}${stars ? ` <span class="stars">${stars}</span>` : ''}</h1><div class="name">${right}</div></header>`;
}
const tracker = () => `<div class="track"><b>1-Minute Reads:</b> Try 1 <span></span> Try 2 <span></span> Try 3 <span></span> <i>words correct</i></div>`;

function renderAll(ST){
  document.title = ST.title + ' Fluency Kit';
  const layouts = [];

  // ---------- 1. family letter ----------
  sheet('letter').innerHTML = header(ST.title + ': Home Reading', '', '') + `
    <p>Dear Families,</p>
    <p>${ST.home.intro} Your child is working on <b>fluency</b>: reading words correctly, smoothly, and with expression.</p>
    <p>This week your child reads the <b>same story at three levels</b>. Each level has a little less help:</p>
    <table class="lv">
      <tr><td><b>★</b></td><td>Short, easy version. <span class="cvc">Underlined</span> words are short-vowel words to sound out (like <span class="cvc">${ST.home.cvcEx}</span>). <span class="hw">Boxed</span> words are heart words: they don’t follow the rules, so we know them by heart (like <span class="hw">said</span>).</td></tr>
      <tr><td><b>★★</b></td><td>Longer version. Only the heart words are boxed.</td></tr>
      <tr><td><b>★★★</b></td><td>The real grade-level article. First with <b>/</b> marks that show where to pause, then plain, the way it looks in the book.</td></tr>
    </table>
    <p>Please spend <b>10 to 15 minutes each night</b>. The plan on the next page tells you what to do. <b>It is okay if some words are hard.</b> A little struggle is how readers grow!</p>
    <h2>When your child gets stuck on a word</h2>
    <ol>
      <li><b>Wait.</b> Count to 5 in your head before you help.</li>
      <li>Underlined word? Say: <span class="say">“Tap the sounds.”</span> (${ST.warm.tap})</li>
      <li>Boxed word? Say: <span class="say">“That’s a heart word. Do you remember it?”</span></li>
      <li>Long word? Say: <span class="say">“Cover part of it. Read it in chunks.”</span> (${ST.warm.chunk})</li>
      <li>Say: <span class="say">“Go back and read the whole sentence again.”</span></li>
      <li>Still stuck? <b>Tell them the word</b>, then have them reread the sentence.</li>
    </ol>
    <div class="two">
      <div class="box"><h3>Please do</h3><ul><li>Praise trying: <span class="say">“You stuck with it!”</span></li><li>Let your child read to you, a pet, or a stuffed animal.</li><li>Sign the reading log each night.</li></ul></div>
      <div class="box"><h3>Please don’t</h3><ul><li>Read the whole story for them.</li><li>Give the word right away.</li><li>Rush. Smooth comes first, then fast.</li></ul></div>
    </div>
    <p class="sig">Please return this packet on: ______________________ &nbsp; Thank you! ______________________</p>`;

  // ---------- 2. nightly plan ----------
  sheet('plan').innerHTML = header('Nightly Plan') + `
    <p>Do one night at a time. Check each box when it is done. Each night takes about 10 to 15 minutes.</p>
    <table class="plan">
      <tr><th>Night</th><th style="width:150px">Warm up (2 min)</th><th style="width:270px">Read (8 to 10 min)</th><th>Finish</th><th>Grown-up</th></tr>
      <tr><td class="n">1</td><td><span class="cb"></span>Word Warm-Up: steps 1 to 3.</td>
        <td><span class="cb"></span>Read <b>★</b> together: take turns, one sentence each.<br><span class="cb"></span>Your child reads <b>★</b> alone.</td>
        <td><span class="cb"></span>Read just the <span class="cvc">underlined</span> words, then just the <span class="hw">boxed</span> words.</td><td></td></tr>
      <tr><td class="n">2</td><td><span class="cb"></span>Steps 1 to 5.<br><span class="cb"></span>Phrase Pyramid 1.</td>
        <td><span class="cb"></span><b>Echo read ★★</b>: you read a sentence, your child reads it back.<br><span class="cb"></span>Your child reads <b>★★</b> alone.</td>
        <td><span class="cb"></span>Cut out the Power Word Cards. Read each one and say what it means.</td><td></td></tr>
      <tr><td class="n">3</td><td><span class="cb"></span>All steps.<br><span class="cb"></span>Phrase Pyramids 2 and 3.</td>
        <td><span class="cb"></span><b>★★★ with / marks</b>: you read one chunk (up to a /), your child reads it back.<br><span class="cb"></span>Your child reads it alone, pausing at each / and stopping at each //.</td>
        <td><span class="cb"></span>Read the ${ST.home.boxName} box together.</td><td></td></tr>
      <tr><td class="n">4</td><td><span class="cb"></span>All steps. Try to read them smoothly.</td>
        <td><span class="cb"></span><b>1-Minute Reads</b>: read ★★ three times (or the plain ★★★ if your child is ready). Write each score.<br><span class="cb"></span>Color the bars on the graph.</td>
        <td><span class="cb"></span>Answer the Think About the Text questions.</td><td></td></tr>
      <tr><td class="n">Bonus</td><td colspan="3"><span class="cb"></span><b>Show time!</b> ${ST.home.bonus}</td><td></td></tr>
    </table>
    <div class="box"><h3>How to do a 1-Minute Read (Night 4)</h3><ol>
      <li>Set a timer for 1 minute. Your child starts at the top of the page.</li>
      <li>Lightly mark in pencil any word your child misses or skips.</li>
      <li>When the timer rings, mark the last word read. The number at the end of each line is the total words up to there. Count to the last word, then take away the missed words.</li>
      <li>Write the score and read again. <b>Can they beat it?</b> Smooth and correct matter more than fast.</li></ol></div>`;

  // ---------- 3. word warm-up ----------
  const sep = w => w.split('|').join('<b>•</b>');
  sheet('warm').innerHTML = header('Word Warm-Up') + `
    <p class="lead">Read each step from the top down. Tap the sounds. Chunk the long words. Check a box when you can read the whole step smoothly.</p>
    <div class="dayhead"><div></div><div></div><div><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span></div></div>
    <div class="pyr">${ST.warm.steps.map(([tag, words]) => `<div class="rowwrap"><div class="tag">${tag}</div>
      <div style="display:flex;justify-content:center"><div class="step">${words.map(w => `<span>${sep(w)}</span>`).join('')}</div></div>
      <div class="checks"><span></span><span></span><span></span><span></span></div></div>`).join('')}</div>
    <h2>Phrase Pyramids: read it smoothly, like talking</h2>
    <div class="phr">${ST.warm.phrases.map(l => `<div class="pp">${l.map(x => `<div>${x}</div>`).join('')}</div>`).join('')}</div>
    <div class="stuck"><div class="st-h">Stuck on a word? Don’t give up!</div><div class="st-g">
      <div><b>1</b>Tap the sounds.<br><i>${ST.warm.tap}</i></div><div><b>2</b>Find the vowel.<br><i>What sound?</i></div>
      <div><b>3</b>Chunk it.<br><i>${ST.warm.chunk}</i></div><div><b>4</b>Reread the<br>sentence.</div></div></div>`;

  // ---------- 4. level 1 ----------
  const s1 = sheet('l1');
  s1.innerHTML = header(ST.l1.title, '★') + `<div class="key"><span class="cvc">sat</span> Sound it out. &nbsp;&nbsp; <span class="hw">said</span> Know it by heart.</div><div class="pa"></div>` + tracker() +
    `<h2>Talk About It</h2><ol class="q">${ST.l1.questions.map(q => `<li>${q}</li>`).join('')}</ol>`;
  layouts.push(passage(s1.querySelector('.pa'), ST.l1.paras, 'l1', true));

  // ---------- 5. level 2 ----------
  const s2 = sheet('l2');
  s2.innerHTML = header(ST.l2.title, '★★') + `<div class="key"><span class="hw">said</span> Know it by heart. &nbsp;&nbsp; <b>Chunk it:</b> ${ST.l2.chunk.map(sep).join(' &nbsp; ')}</div><div class="pa"></div>` + tracker();
  layouts.push(passage(s2.querySelector('.pa'), ST.l2.paras, 'l2', true));

  // ---------- 6-7. level 3, phrase-cued (two pages) ----------
  const cut = ST.l3.pageBreak;
  const s3a = sheet('l3c');
  s3a.innerHTML = header(ST.l3.title, '★★★') + `<div class="key">Read each chunk smoothly. <b>/</b> = take a short pause. &nbsp; <b>//</b> = stop at the end of a sentence.</div><div class="pa"></div>`;
  passage(s3a.querySelector('.pa'), ST.l3.paras.slice(0, cut), 'cued', false);
  const s3b = sheet('l3c');
  s3b.innerHTML = header(ST.l3.title + ' <span class="pg">p. 2</span>', '★★★') + `<div class="pa"></div>`;
  passage(s3b.querySelector('.pa'), ST.l3.paras.slice(cut), 'cued', false);

  // ---------- 8. level 3, clean ----------
  const s4 = sheet('l3');
  s4.innerHTML = header(ST.l3.title, '★★★') + `<div class="pa"></div>` + tracker();
  layouts.push(passage(s4.querySelector('.pa'), ST.l3.paras.map(cleanText), 'clean', true));

  // ---------- 9. questions + word box ----------
  sheet('qs').innerHTML = header('Think About the Text') + `<p>Answer in full sentences. Look back at the text to find proof!</p>` +
    ST.questions.map((q, i) => `<div class="qq">${i+1}. ${q}</div><div class="lines"><div></div><div></div></div>`).join('') +
    `<div class="box words"><h3>${ST.home.boxName}</h3><dl>${ST.wordBox.map(([t, m]) => `<dt>${t}</dt><dd>${m}</dd>`).join('')}</dl></div>`;

  // ---------- 10. log + graph ----------
  const face = m => `<svg viewBox="0 0 30 30" width="26" height="26" style="vertical-align:middle;margin:0 4px"><circle cx="15" cy="15" r="13" fill="#fff" stroke="#111" stroke-width="2"/><circle cx="10.5" cy="12" r="1.8"/><circle cx="19.5" cy="12" r="1.8"/>${
    m === 'h' ? '<path d="M9 18 Q15 24 21 18" stroke="#111" stroke-width="2" fill="none"/>' : m === 'o' ? '<path d="M9.5 20 H20.5" stroke="#111" stroke-width="2"/>' : '<path d="M9 22 Q15 16 21 22" stroke="#111" stroke-width="2" fill="none"/>'}</svg>`;
  const gw = 720, gh0 = 520, left = 56, bottom = 40, top = 16, max = 180, gh = gh0 - bottom - top;
  let g = `<svg viewBox="0 0 ${gw} ${gh0}" width="${gw}" height="${gh0}" font-family="Andika">`;
  for (let v = 0; v <= max; v += 10){ const y = top + gh - v/max*gh;
    g += `<line x1="${left}" y1="${y}" x2="${gw-10}" y2="${y}" stroke="${v%50===0?'#555':'#bbb'}" stroke-width="${v%50===0?1.6:1}"/>`;
    if (v % 20 === 0) g += `<text x="${left-8}" y="${y+5}" text-anchor="end" font-size="15">${v}</text>`; }
  const bw = 120, gap = (gw - left - 10 - 3*bw) / 4;
  ['Try 1','Try 2','Try 3'].forEach((c, i) => { const x = left + gap + i*(bw+gap);
    g += `<rect x="${x}" y="${top}" width="${bw}" height="${gh}" fill="none" stroke="#111" stroke-width="2"/><text x="${x+bw/2}" y="${gh0-12}" text-anchor="middle" font-size="18" font-weight="700">${c}</text>`; });
  g += `<text transform="translate(16 ${top+gh/2}) rotate(-90)" text-anchor="middle" font-size="15">words correct</text></svg>`;
  sheet('log').innerHTML = header('My Reading Log') + `<table class="log"><tr><th>Night</th><th>What I read (★, ★★, or ★★★)</th><th>Minutes</th><th>How did it go?</th><th>Grown-up sign</th></tr>` +
    [1,2,3,4].map(n => `<tr><td><b>${n}</b></td><td></td><td></td><td>${face('h')+face('o')+face('s')}</td><td></td></tr>`).join('') + `</table>
    <h2>My 1-Minute Read Graph</h2><p>Which level did you read? ★ &nbsp; ★★ &nbsp; ★★★ (circle one). Color a bar up to your words correct.</p>${g}`;

  // ---------- 11. power word cards ----------
  sheet('cardsheet').innerHTML = header('Power Word Cards') + `<p class="cut">✂ Cut out the cards. Read the word, clap the parts, and tell what it means. Then use it in your own sentence.</p>
    <div class="cards">${ST.power.map(([w, syl, mean, from]) => `<div class="card"><div class="word">${w}</div><div class="syl">${syl}</div><div class="mean">${mean}</div><div class="from">${from}</div><div class="mine">My sentence: ________________________</div></div>`).join('')}</div>`;

  // lay out the word counts once the font is ready, then tell the build script we are done
  document.fonts.ready.then(() => {
    layouts.forEach(l => l && l());
    const over = [...document.querySelectorAll('.sheet')].map((s, i) => s.scrollHeight > s.clientHeight + 1 ? i + 1 : 0).filter(Boolean);
    window.__overflow = over;
    window.__ready = true;
  });
}

const KIT = new URLSearchParams(location.search).get('s');
document.write(`<script src="${KIT}.js"><\/script>`);
