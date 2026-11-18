// Builds every PDF for each story kit. Run: node build.js [story ...]   (needs Playwright + Python pypdf)
// Adding a story = art_<name>.js + <name>.js, then add its name and file label below.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');
const D = __dirname;
const KITS = { desert: 'The_Desert', fireman: 'Fred_the_Fireman' };
const wanted = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(KITS);

(async () => {
  const b = await chromium.launch();
  for (const key of wanted) {
    const name = KITS[key], out = path.join(D, 'pdf', key);
    fs.mkdirSync(out, { recursive: true });
    const jobs = [
      ['level1.html', '',          `Level1_${name}_Color.pdf`],
      ['level1.html', '#coloring', `Level1_${name}_BW.pdf`],
      ['level2.html', '',          `Level2_${name}_Color.pdf`],
      ['level2.html', '#coloring', `Level2_${name}_BW.pdf`],
      ['warmup_cards.html', '',    `Word_WarmUp_and_Power_Cards_${name}.pdf`],
      ['home_pages.html', '',      '_home_pages.pdf'],
    ];
    for (const [tpl, hash, file] of jobs) {
      const p = await b.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push(e.message));
      await p.goto(`file://${path.join(D, tpl)}?s=${key}${hash}`, { waitUntil: 'networkidle' });
      await p.evaluate(() => document.fonts.ready);
      if (await p.evaluate(() => document.body.innerText.includes('MISMATCH'))) errs.push('passage does not match panels');
      if (errs.length) throw new Error(`${key}/${tpl}: ${errs.join('; ')}`);
      await p.pdf({ path: path.join(out, file), format: 'Letter', printBackground: true, preferCSSPageSize: true });
      await p.close();
    }
    // Home packet: letter, plan, warm-up, story 1 (B&W), story 2 (B&W, 3 pages), log, questions, cards
    execFileSync('python3', ['-c', `
import pypdf, os
o, n = ${JSON.stringify(out)}, ${JSON.stringify(name)}
r = lambda f: pypdf.PdfReader(os.path.join(o, f))
home, wc, l1, l2 = r('_home_pages.pdf'), r('Word_WarmUp_and_Power_Cards_' + n + '.pdf'), r('Level1_' + n + '_BW.pdf'), r('Level2_' + n + '_BW.pdf')
w = pypdf.PdfWriter()
for pg in [home.pages[0], home.pages[1], wc.pages[0], l1.pages[0], *l2.pages, home.pages[2], home.pages[3], wc.pages[1]]:
    w.add_page(pg)
w.write(os.path.join(o, n + '_Home_Packet.pdf'))
os.remove(os.path.join(o, '_home_pages.pdf'))
`]);
    console.log('built', key);
  }
  await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
