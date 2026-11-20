// Builds the PDFs for each text-only kit. Run: node build.js [story ...]   (needs Playwright + Python pypdf)
// Adding a story = one data file <name>.js, plus a line in KITS below.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const path = require('path'), fs = require('fs');
const D = __dirname;
const KITS = { little_league: 'Little_League_Champs' };
const wanted = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(KITS);

(async () => {
  const b = await chromium.launch();
  for (const key of wanted) {
    const name = KITS[key], out = path.join(D, 'pdf');
    fs.mkdirSync(out, { recursive: true });
    const p = await b.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    await p.goto(`file://${path.join(D, 'kit.html')}?s=${key}`, { waitUntil: 'networkidle' });
    await p.waitForFunction('window.__ready === true', null, { timeout: 20000 });
    const over = await p.evaluate(() => window.__overflow);
    if (over.length) errs.push('text runs off sheet(s) ' + over.join(', '));
    if (errs.length) throw new Error(`${key}: ${errs.join('; ')}`);
    const full = path.join(out, `${name}_Home_Packet.pdf`);
    await p.pdf({ path: full, format: 'Letter', printBackground: true, preferCSSPageSize: true });
    await p.close();
    // Sheets: 1 letter, 2 plan, 3 warm-up, 4 ★, 5 ★★, 6-7 ★★★ cued, 8 ★★★ plain, 9 questions, 10 log, 11 cards
    execFileSync('python3', ['-c', `
import pypdf, os
src, o, n = ${JSON.stringify(full)}, ${JSON.stringify(out)}, ${JSON.stringify(name)}
r = pypdf.PdfReader(src)
def save(pages, f):
    w = pypdf.PdfWriter()
    for i in pages: w.add_page(r.pages[i-1])
    w.write(os.path.join(o, f))
save([4,5,6,7,8,9], n + '_Passages_and_Questions.pdf')
save([3,11], n + '_WarmUp_and_Power_Cards.pdf')
`]);
    console.log('built', key);
  }
  await b.close();
})().catch(e => { console.error(e.message); process.exit(1); });
