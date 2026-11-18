// Builds every Sam the Spider PDF. Run: node build.js   (needs Playwright + Python pypdf)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path');
const D = __dirname, OUT = path.join(D, 'pdf');
require('fs').mkdirSync(OUT, { recursive: true });
const jobs = [
  ['level1_picture_story.html', '',          'Level1_Sam_the_Spider_Color.pdf'],
  ['level1_picture_story.html', '#coloring', 'Level1_Sam_the_Spider_BW.pdf'],
  ['level2_picture_story.html', '',          'Level2_Sam_the_Spider_Color.pdf'],
  ['level2_picture_story.html', '#coloring', 'Level2_Sam_the_Spider_BW.pdf'],
  ['warmup_and_cards.html',     '',          'Word_WarmUp_and_Power_Cards.pdf'],
  ['home_packet_pages.html',    '',          '_home_pages.pdf'],
];
(async () => {
  const b = await chromium.launch();
  for (const [src, hash, out] of jobs) {
    const p = await b.newPage();
    await p.goto('file://' + path.join(D, src) + hash, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    if (await p.evaluate(() => document.body.innerText.includes('MISMATCH'))) throw new Error('passage mismatch in ' + src);
    await p.pdf({ path: path.join(OUT, out), format: 'Letter', printBackground: true, preferCSSPageSize: true });
    await p.close();
  }
  await b.close();
  // Home packet order: letter, plan, warm-up, story 1, story 2 (3 pages), log, questions, cards
  execFileSync('python3', ['-c', `
import pypdf, os
o = '${OUT}'
r = lambda n: pypdf.PdfReader(os.path.join(o, n))
home, wc, l1, l2 = r('_home_pages.pdf'), r('Word_WarmUp_and_Power_Cards.pdf'), r('Level1_Sam_the_Spider_BW.pdf'), r('Level2_Sam_the_Spider_BW.pdf')
w = pypdf.PdfWriter()
for pg in [home.pages[0], home.pages[1], wc.pages[0], l1.pages[0], *l2.pages, home.pages[2], home.pages[3], wc.pages[1]]:
    w.add_page(pg)
w.write(os.path.join(o, 'Sam_the_Spider_Home_Packet.pdf'))
os.remove(os.path.join(o, '_home_pages.pdf'))
`]);
  console.log('done');
})();
