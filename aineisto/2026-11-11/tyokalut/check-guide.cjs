const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync('paimio-valtuusto-11-11-2026.html', 'utf8');
let script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
const elements = new Map();
function element(id) { if (!elements.has(id)) elements.set(id, { innerHTML: '', textContent: '', hidden: false, dataset: {}, setAttribute(){}, addEventListener(){}, focus(){} }); return elements.get(id); }
const tabs = ['overview','item','questions','sources'].map(view => ({dataset:{view},setAttribute(){},focus(){}}));
const context = { document: {getElementById:element,querySelectorAll:s=>s==='.tab'?tabs:[],querySelector:()=>element('tabs'),addEventListener(){}}, location:{hash:''},history:{replaceState(){}},window:{scrollTo(){}},setTimeout(){},navigator:{},console };
script = script.replace(/\}\)\(\);\s*$/, 'globalThis.testGuide={items,allPdfSources,navigate,render,issues,questionsFor,comparisons,compareRows};})();');
vm.createContext(context); vm.runInContext(script,context);
const api=context.testGuide;
assert.equal(api.items.length,14); assert.equal(api.allPdfSources().length,19);
for(const i of api.items){api.navigate('item',i.n);const out=element('panel').innerHTML;assert(out.includes(i.title));assert(out.includes('04 / Nousseet kysymykset'));assert(out.includes('Nykytilanne → esitys'));assert(api.compareRows(i).length>0);assert(!out.includes('undefined'));}
assert.equal(Object.keys(api.comparisons).length,14);
const taxes=api.comparisons[47].rows;
for(const label of ['Yleinen vero, rakennukset','Yleinen vero, maapohja','Vakituinen asuinrakennus','Muut asuinrakennukset','Rakentamattomat rakennuspaikat','Voimalaitokset']){
 const r=taxes.find(x=>x[0]===label); assert(r); assert(r[1].includes('2026')); assert(r[2].includes('2027')); assert(r[3].includes('ennallaan'));
}
const changes=api.comparisons[52].rows;
assert(changes.some(r=>r[0]==='Kiinteistövero'&&r[1]==='2 700 000 €'&&r[2]==='2 515 000 €'));
assert(api.comparisons[54].numeric.some(r=>r[0]==='Vuosikate'&&r[1]===1995752&&r[2]===2813912));
for(const v of ['overview','questions','sources']){api.navigate(v);assert(element('panel').innerHTML.length>500);}
console.log('OK: 14 asiakohtaa vertailuineen, 19 liitelinkkiä, veroprosenttien 2026/2027-parit, määrärahamuutokset ja toteumavertailu. Kaikki neljä näkymää muodostuvat ilman virheitä.');
