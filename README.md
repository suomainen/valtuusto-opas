# Valtuusto-opas

Paimion kaupunginvaltuuston kokousoppaat ja työkalu niiden tekemiseen. Kukin opas on yksi selaimessa toimiva HTML-tiedosto. Siinä on kokouksen tilannekuva, pykäläkohtaiset arviot ja vertailuluvut, nousseet kysymykset ja lähteet. Opas toimii myös ilman verkkoyhteyttä. Alkuperäiset asiakirjat avautuvat linkeistä kaupungin Dynasty-julkaisusta.

Sivusto julkaistaan GitHub Pagesilla osoitteessa **https://suomainen.github.io/valtuusto-opas/**.

## Rakenne

```
valtuusto-opas/
├── index.html                 Etusivu: luettelo kokousoppaista ja linkit työkaluun
├── oppaat/
│   └── paimio-valtuusto-11-11-2026.html   Valmis opas, valtuusto 11.11.2026 (§ 43–56)
├── valtuusto-opas/            Skill uuden oppaan tekemiseen (Codex / Claude)
│   ├── SKILL.md               Laatimisohje: aineisto, analyysi ja toimitus
│   ├── assets/opas.html       HTML-pohja (sininen teema, neljä näkymää)
│   ├── examples/              Esityslista- ja kokous-JSONin mallit (kuvitteellisia)
│   ├── references/tietorakenne.md   Kokous-JSONin kenttien kuvaus
│   └── scripts/
│       ├── prepare_meeting.py Luo täytettävän kokous-JSONin esityslista-JSONista
│       └── build_guide.py     Rakentaa valmiin HTML-oppaan kokous-JSONista
├── rakennusohje.md            Koko työkalu yhtenä jaettavana Markdown-tiedostona
├── aineisto/
│   └── 2026-11-11/            Kokouksen 11.11.2026 lähdeaineisto
│       ├── 2026768.txt        Esityslista tekstinä
│       ├── 2026768-*.txt      Liitteet tekstinä (tiedostonimi = Dynastyn liitetunnus)
│       ├── kuvat/             Liitteiden kaaviot ja taulukot kuvina
│       └── tyokalut/          Oppaan tarkistus- ja päivitysskriptit
├── CHANGELOG.md               Muutosloki
└── README.md
```

## Esikatselu

Oppaan voi avata suoraan tiedostosta selaimessa. Koko sivuston voi esikatsella paikallisesti:

```
python -m http.server
```

ja avaamalla http://localhost:8000/.

## Uuden oppaan tekeminen

Ohjeet ovat tiedostossa [valtuusto-opas/SKILL.md](valtuusto-opas/SKILL.md). Lyhyesti:

```
cd valtuusto-opas
python scripts/prepare_meeting.py esityslista.json kokous.json
python scripts/build_guide.py kokous.json ../oppaat/paimio-valtuusto-PP-KK-VVVV.html
```

Tarvitaan Python 3, ei lisäpaketteja. Esimerkin voi kokeilla komennolla `python scripts/build_guide.py examples/kokous-esimerkki.json esimerkki.html`.

Kun opas on valmis:

1. Tallenna kokouksen lähdeaineisto kansioon `aineisto/VVVV-KK-PP/`.
2. Lisää oppaalle kortti `index.html`-tiedoston Kokousoppaat-osioon (uusin ensin).
3. Nosta versio ja päivitä muutosloki (ks. Versiointi).

Skillin voi ottaa käyttöön Codexissa kopioimalla `valtuusto-opas`-kansion hakemistoon `.codex/skills`, tai jakaa yhtenä tiedostona `rakennusohje.md`.

## Muokkaaminen

- **Etusivun tekstit ja oppaiden luettelo:** `index.html`.
- **Oppaan ulkoasu ja toiminnot:** `valtuusto-opas/assets/opas.html`. Muutos koskee vasta uudelleen rakennettavia oppaita. Jo julkaistut oppaat ovat itsenäisiä tiedostoja.
- **Yksittäisen oppaan sisältö:** opas 11.11.2026 on rakennettu ennen JSON-työkalua ja sen tiedot ovat suoraan HTML-tiedoston `<script>`-osassa (`items`, `comparisons`, `attachments`). Muokkaa sitä tiedostossa.
- **Oppaan tarkistus:** aja kansiossa `oppaat` komento `node ../aineisto/2026-11-11/tyokalut/check-guide.cjs`. Skripti tarkistaa, että kaikki pykälät, vertailut ja näkymät muodostuvat virheittä.

## Julkaisu

GitHub Pages julkaisee `main`-haaran juuren. Muutokset julkaistaan:

```
git pull --rebase
git add -A
git commit -m "Kuvaus muutoksesta"
git push --follow-tags
```

Jos push hylätään ("fetch first"), GitHubissa on commit, jota paikallisesti ei ole:

```
git fetch origin
git rebase origin/main
git push
```

Pages-välimuisti on 10 minuuttia. Jos sivu näyttää vanhalta, päivitä selain Ctrl+F5:llä.

## Versiointi

Versionumero on muotoa **pää.osa.korjaus**:

- **pää**: sivuston tai oppaan rakenteen kokonaan uusi versio
- **osa**: uusi kokousopas, uusi ominaisuus tai uusi osio
- **korjaus**: pieni korjaus tai tarkennus

Versio näkyy etusivun alareunassa (`index.html`). Jokaisessa sivuston muutoksessa:

1. Nosta numero `index.html`-tiedostossa.
2. Lisää muutos [CHANGELOG.md](CHANGELOG.md)-tiedostoon.
3. Tee commit ja tagi: `git tag -a vX.Y.Z -m "Kuvaus"`.
4. Julkaise: `git push --follow-tags` (pelkkä `git push` ei vie tageja).

Pelkkä dokumentaation muutos (README, muutosloki) ei nosta numeroa.

## Kolmannen osapuolen tiedostot ja oikeudet

| Tiedosto | Lähde | Oikeus |
|---|---|---|
| `aineisto/*/*.txt`, `aineisto/*/kuvat/*` | Paimion kaupungin julkiset kokousasiakirjat (julkaisu.paimio.fi/dynasty10) | Viranomaisen julkisia asiakirjoja; tekijänoikeuslain 9 §:n mukaan päätökset ja lausunnot eivät ole tekijänoikeuden suojaamia. Liitteinä olevat ulkopuolisten laatimat asiakirjat (esim. sopimukset, raportit) voivat olla suojattuja; ne ovat repossa lähdeaineistona. |
| Oppaiden lainsäädäntölinkit | Finlex | Linkkejä, ei kopioitua sisältöä |
| Ulkoiset kirjastot ja fontit | – | Ei käytössä: oppaat käyttävät järjestelmäfonttia eivätkä lataa mitään verkosta |

Oppaiden arviot ja kysymykset ovat tekijän tilannearvioita, eivät kaupungin virallisia kantoja.

© Oskari Summanen. Kaikki oikeudet pidätetään.
