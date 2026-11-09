# Työkalu: uuden kokousoppaan tekeminen

Näillä tiedostoilla tehdään uusi opas kansioon `oppaat`, kun kaupunki julkaisee seuraavan valtuuston esityslistan. Analyysin laatimisohje (mitä luetaan, miten vertaillaan, miten kirjoitetaan) on tiedostossa [SKILL.md](SKILL.md).

## Kansiorakenne

```
valtuusto-opas/                       (GitHub-repo = paikallinen kansio C:\Koodauksia\valtuusto-opas)
├── index.html                        etusivu: oppaiden luettelo
├── oppaat/                           valmiit oppaat
├── aineisto/VVVV-KK-PP/              kokouksen lähdeaineisto
└── valtuusto-opas/                   tämä kansio
    ├── LUEMINUT.md                   tämä ohje
    ├── SKILL.md                      laatimisohje (Codex / Claude)
    ├── assets/opas.html              oppaan HTML-pohja (ulkoasu, toiminnot, saavutettavuus)
    ├── examples/
    │   ├── esityslista-esimerkki.json   esityslistan perustiedot (malli)
    │   └── kokous-esimerkki.json        täytetty kokous-JSON (malli)
    ├── references/tietorakenne.md    kokous-JSONin kentät
    └── scripts/
        ├── prepare_meeting.py        esityslista-JSON → täytettävä kokous-JSON
        └── build_guide.py            kokous-JSON + pohja → valmis HTML-opas
```

Skriptit tarvitsevat vain Python 3:n. Lisäkirjastoja ei tarvita.

## Uuden oppaan lisääminen

1. Avaa kokouksen esityslista kaupungin [kokousjulkaisusta](https://julkaisu.paimio.fi/dynasty10/). Kopioi kokouksen, jokaisen pykälän ja liitteen osoite (hiiren oikea painike → Kopioi linkin osoite). Älä päättele osoitteita pykälänumerosta.
2. Tallenna esityslista ja liitteet tekstinä kansioon `aineisto/VVVV-KK-PP/`. Tallenna kuvina kaaviot ja taulukot, joita ei saa tekstinä, alikansioon `kuvat`.
3. Tee kansioon `valtuusto-opas` tiedosto `esityslista.json` mallin `examples/esityslista-esimerkki.json` mukaan: kokouksen tiedot ja kaikki pykälät liitteineen esityslistan järjestyksessä.
4. Luo täytettävä kokous-JSON:
   ```
   python scripts/prepare_meeting.py esityslista.json kokous.json
   ```
5. Täydennä `kokous.json` aineiston perusteella [SKILL.md](SKILL.md):n ja kenttäkuvauksen [references/tietorakenne.md](references/tietorakenne.md) mukaan. Täytetty malli on `examples/kokous-esimerkki.json`.
6. Rakenna opas:
   ```
   python scripts/build_guide.py kokous.json ../oppaat/paimio-valtuusto-PP-KK-VVVV.html
   ```
7. Avaa opas selaimessa ja tarkista se: pykälät ja liitteet vastaavat esityslistaa, luvuilla on vuosi ja lähde, haku ja linkit toimivat, ja opas toimii puhelimella ja pelkällä näppäimistöllä.
8. Lisää oppaalle kortti `index.html`:n Kokousoppaat-osioon (uusin ensin) ja rivi README:n Aineisto-taulukkoon. Nosta versio (osa: x.+1.0) ja päivitä `CHANGELOG.md`.
9. Julkaise: `git add -A`, `git commit`, `git tag -a vX.Y.0 -m "…"` ja `git push --follow-tags`.

`esityslista.json` ja `kokous.json` ovat työtiedostoja. Säilytä ne tarvittaessa kokouksen aineistokansiossa (`aineisto/VVVV-KK-PP/`).

## Jos jokin menee pieleen

- **"Kokousdatan pohjan luonti ei onnistunut: … File exists":** `prepare_meeting.py` ei kirjoita olemassa olevan tiedoston päälle, ettei täytetty data katoa. Anna uusi tiedostonimi tai siirrä vanha pois.
- **"Puuttuva tai tyhjä tekstikenttä: …":** kokous-JSONista puuttuu pakollinen teksti. Pakolliset kentät: `meeting`: `city`, `date`, `reviewed`, `stage`, `coverage`, `url`; `overview`: `title`, `lead`; jokaisella pykälällä `title`, `short`, `tag`, `assessment`, `url` ja `comparison.note`; liitteellä `title`, `status`, `summary`.
- **"Lähdelinkin pitää olla kokonainen verkko-osoite":** linkin pitää alkaa `https://`. Tarkista, ettei `sources`-parin järjestys ole väärin: ensin nimi, sitten osoite.
- **"Taulukon rivien ja otsikoiden sarakemäärät eivät vastaa toisiaan":** vertailutaulukon riveissä on oletuksena neljä solua (mittari, nyt, esitys, muutos). Jos käytät omia `headers`-otsikoita, jokaisessa rivissä on oltava yhtä monta solua.
- **"Noston pykälä puuttuu" / "Tarkennuskohdan pykälä puuttuu":** `overview.highlights`- tai `issues`-kohdan `n` viittaa pykälään, jota ei ole `items`-listassa.
- **"Pykälänumerot eivät saa toistua":** samaa pykälää on kaksi kertaa. Pykälänumero on kokonaisluku ilman §-merkkiä.
- **JSON-virhe ("Expecting ',' delimiter" tms.):** tiedostossa on pilkku- tai lainausmerkkivirhe. Virheilmoitus kertoo rivin ja sarakkeen. Tallenna tiedosto UTF-8-muodossa.

## Sivun muokkaaminen

Ulkoasu, toiminnot ja saavutettavuusratkaisut ovat tiedostossa `assets/opas.html`. Paikkamerkki `__GUIDE_DATA__` korvataan rakennettaessa kokousdatalla. Älä poista sitä.

- Pohjan muutos koskee vain uudelleen rakennettavia oppaita. Jo julkaistut oppaat ovat itsenäisiä tiedostoja, joten tee sama muutos niihin erikseen, jos se on tarpeen.
- Opas 11.11.2026 on tehty ennen JSON-työkalua, ja sen tiedot ovat suoraan HTML-tiedoston `<script>`-osassa (`items`, `comparisons`, `attachments`). Tarkista se muutosten jälkeen komennolla `node ../aineisto/2026-11-11/tyokalut/check-guide.cjs` kansiossa `oppaat`.
- Värit ovat pohjan alussa CSS-muuttujina (`--navy`, `--blue`, `--yellow` …). Tarkista värejä muuttaessasi, että tekstin kontrasti on vähintään 4,5:1.
- Kun muutat pohjaa, päivitä sama sisältö myös tiedoston `rakennusohje.md` kohtaan `assets/opas.html`.
- Tarkista pohjan muutosten jälkeen saavutettavuus README:n Saavutettavuus-kohdan mukaan.
