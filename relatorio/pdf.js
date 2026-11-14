// Converte o HTML do relatório em PDF A4 usando o Chromium do Playwright.
// Uso: node relatorio/pdf.js entrada.html saida.pdf [--png pasta]
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [entrada, saida, flag, pastaPng] = process.argv.slice(2);
  if (!entrada || !saida) {
    console.error('Uso: node pdf.js entrada.html saida.pdf [--png pasta]');
    process.exit(1);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
  await page.goto('file://' + path.resolve(entrada), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // Aviso se algum conteúdo passou do limite da página (fica cortado no PDF).
  const estouros = await page.$$eval('.pagina', (ps) => ps.map((p, i) => {
    const corpo = p.querySelector('.corpo');
    const ultimo = corpo && corpo.lastElementChild;
    if (!ultimo) return null;
    const falta = ultimo.getBoundingClientRect().bottom - corpo.getBoundingClientRect().bottom;
    return falta > 1 ? `página ${i + 1} estourou ${Math.round(falta)}px` : null;
  }).filter(Boolean));
  if (estouros.length) console.error('ATENÇÃO: ' + estouros.join('; '));
  await page.pdf({ path: saida, format: 'A4', printBackground: true, preferCSSPageSize: true });
  if (flag === '--png' && pastaPng) {
    const paginas = await page.$$('.pagina');
    for (let i = 0; i < paginas.length; i++) {
      await paginas[i].screenshot({ path: path.join(pastaPng, `pagina-${i + 1}.png`) });
    }
  }
  await browser.close();
})();
