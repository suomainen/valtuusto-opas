# Valtuusto-opas

Selattavat kokousoppaat Paimion kaupunginvaltuuston kokouksiin ja työkalu niiden tekemiseen. Opas käy esityslistan läpi pykälä kerrallaan. Kustakin asiasta näkyvät asiakirjojen tiedot, keskeiset luvut nykytilanteeseen verrattuna, oma tilannearvio, avoimet kohdat ja nousseet kysymykset sekä linkit alkuperäisiin asiakirjoihin.

Sivusto: **https://suomainen.github.io/valtuusto-opas/**

> **Huom.** Oppaat ovat valtuutetun epävirallista valmistautumisaineistoa. Ne eivät ole Paimion kaupungin julkaisuja eivätkä kaupungin kantoja. Viralliset esityslistat, liitteet ja pöytäkirjat ovat kaupungin [kokousjulkaisussa](https://julkaisu.paimio.fi/dynasty10/).
>
> Oppaat on koottu tekoälyavustajan avulla, ja ne voivat sisältää virheitä. Tarkista olennaiset tiedot alkuperäisistä asiakirjoista. Korjaukset ja huomiot: oskari@summanen.org tai [GitHubin issues](https://github.com/suomainen/valtuusto-opas/issues).

## Tausta

Valtuuston esityslistat liitteineen ovat laajoja. Esimerkiksi marraskuun 2026 talousarviokokouksen aineistossa on 14 asiaa ja 19 liite-PDF:ää, yhteensä yli 200 sivua. Opas kokoaa aineiston yhteen näkymään: mitä päätettäväksi esitetään, mitä se tarkoittaa numeroina ja mitä kannattaa kysyä ennen päätöstä.

Oppaan tekee valtuutettu Oskari Summanen. Asiakirjoista poimitut tiedot ja oma tilannearvio pidetään oppaassa erillään, ja jokaisen luvun lähde on merkitty.

## Ominaisuudet

- Neljä näkymää: tilannekuva, asiat pykälittäin, nousseet kysymykset ja tarkennukset ja lähteet
- Jokaisessa asiassa nykytilanne → esitys -vertailu: nykyinen arvo, ehdotettu arvo ja muutos sekä vuosi ja tiedon laji (talousarvio, ennuste, toteuma)
- Asiat jaettu osiin: todettu ja päätösehdotus, oma tilannearvio, huomioitavaa ja avoimia kohtia, nousseet kysymykset
- Haku kaikista asioista. Kysymyksiä voi rastia käsitellyiksi kokouksen aikana.
- Linkit suoraan pykäliin ja liitteisiin kaupungin kokousjulkaisussa. Asiaan voi linkittää osoitteella, esim. `#asia-47`.
- Tulostus näkymä kerrallaan
- Toimii puhelimella, tabletilla ja tietokoneella sekä näppäimistöllä ja ruudunlukijalla (WCAG 2.1 AA)

## Käyttö

Jokainen opas on yksi itsenäinen HTML-tiedosto kansiossa `oppaat`. Palvelinta tai asennuksia ei tarvita.

- **Paikallisesti:** avaa oppaan HTML-tiedosto selaimessa. Koko sivuston voi esikatsella komennolla `python -m http.server` ja osoitteella http://localhost:8000/.
- **GitHub Pagesissa:** Settings → Pages → Source: *Deploy from a branch*, haara `main`, kansio `/ (root)`.

Oppaat eivät hae mitään verkosta. Tyylit, toiminnot ja data ovat tiedoston sisällä, ja fonttina käytetään laitteen järjestelmäfonttia. Opas toimii siis myös ilman verkkoyhteyttä. Vain alkuperäisten asiakirjojen linkit tarvitsevat verkon.

## Rakenne

```
valtuusto-opas/
├── index.html                 etusivu: oppaiden luettelo
├── oppaat/                    valmiit oppaat, yksi HTML-tiedosto kokousta kohden
├── valtuusto-opas/            työkalu (skill) uuden oppaan tekemiseen
│   ├── LUEMINUT.md            ohje uuden oppaan tekemiseen
│   ├── SKILL.md               laatimisohje tekoälyavustajalle
│   ├── assets/opas.html       oppaan HTML-pohja
│   ├── examples/              JSON-mallit (kuvitteellisia)
│   ├── references/            kokous-JSONin kenttien kuvaus
│   └── scripts/               prepare_meeting.py ja build_guide.py
├── rakennusohje.md            koko työkalu yhtenä jaettavana Markdown-tiedostona
├── aineisto/VVVV-KK-PP/       kokouksen lähdeaineisto tekstinä ja kuvina sekä tarkistusskriptit
├── CHANGELOG.md
├── LICENSE
└── .nojekyll                  Pages julkaisee tiedostot sellaisenaan
```

## Aineisto

Lähde: [Paimion kaupungin kokousjulkaisu](https://julkaisu.paimio.fi/dynasty10/), kaupunginvaltuuston esityslistat ja niiden liitteet.

Esityslista ja liitteet on muutettu tekstiksi ja tallennettu kansioon `aineisto/VVVV-KK-PP/`. Tiedostonimi on kokousjulkaisun asiakirjatunnus, esim. `2026768-3-43306.txt` = kokous 2026768, pykälän järjestysnumero 3, liite 43306. Kaaviot ja taulukot, joita ei saanut luettua tekstinä, ovat kansiossa `kuvat`.

Lakiviittaukset on tarkistettu ajantasaisesta [Finlexistä](https://www.finlex.fi/). Vertailuluvut on haettu kokouksen aineistosta tai aiemmista hyväksytyistä päätöksistä, talousarviosta ja tilinpäätöksestä. Omat laskelmat on merkitty oppaaseen.

| Opas | Kokous | Asiat | Liite-PDF:t | Tarkastelu |
|---|---|---:|---:|---|
| [11.11.2026](https://suomainen.github.io/valtuusto-opas/oppaat/paimio-valtuusto-11-11-2026.html) | [Esityslista 5/2026](https://julkaisu.paimio.fi/dynasty10/cgi/DREQUEST.PHP?page=meeting&id=2026768) | § 43–56 | 19 | 8.11.2026, vertailut 9.11.2026 |

## Rajoitukset ja huomiot

- **Esitys ei ole päätös.** Opas perustuu esityslistaan. Valtuusto voi muuttaa ehdotusta, ja lopullinen päätös on kokouksen pöytäkirjassa.
- **Tarkastelun ajankohta.** Opas kuvaa aineistoa sellaisena kuin se oli tarkastelupäivänä. Myöhemmin lisätyt liitteet tai korjaukset eivät näy oppaassa.
- **Puuttuva ja peitetty aineisto.** Salassa pidettäviä tai peitettyjä osia ei ole nähty. Jos liite on mainittu mutta puuttuu tai jäi lukematta, se on merkitty oppaaseen.
- **Vertailuluvut.** Vertailu tehdään aina samaan ajanjaksoon ja rajaukseen. Kun vertailukelpoista lähtölukua ei ole, sitä ei arvioida, ja puute kerrotaan. Luvut ovat usein pyöristettyjä, ja erotukset on laskettu näkyvistä luvuista.
- **Oma tilannearvio** on tekijän näkemys, ei oikeudellinen tai taloudellinen asiantuntijalausunto.
- **Linkitetyt PDF-liitteet** ovat kaupungin julkaisemia. Niiden saavutettavuus ei ole tämän sivuston hallinnassa.

## Uuden oppaan tekeminen

Opas kootaan kokous-JSONista HTML-pohjaan kansion `valtuusto-opas` skripteillä:

```
python scripts/prepare_meeting.py esityslista.json kokous.json
python scripts/build_guide.py kokous.json ../oppaat/paimio-valtuusto-PP-KK-VVVV.html
```

Tarkemmat ohjeet ovat tiedostossa [valtuusto-opas/LUEMINUT.md](valtuusto-opas/LUEMINUT.md). Tekoälyavustajalle tarkoitettu laatimisohje on [valtuusto-opas/SKILL.md](valtuusto-opas/SKILL.md), ja koko työkalu yhtenä tiedostona on [rakennusohje.md](rakennusohje.md).

## Saavutettavuus

Oppaat noudattavat WCAG 2.1 AA -tasoa. Ratkaisut ovat HTML-pohjassa `valtuusto-opas/assets/opas.html`, joten ne tulevat jokaiseen uuteen oppaaseen: ohituslinkki sisältöön, otsikkotasot ilman hyppyjä, taulukoiden sarake- ja riviotsikot, näppäimistöllä toimivat välilehdet, ruudunlukijalle ilmoitettavat hakutulokset ja näkymäkohtainen sivun otsikko. Saavutettavuuspuutteista voi ilmoittaa osoitteeseen oskari@summanen.org.

Pohjan muutosten jälkeen tarkistetaan vähintään:

- automaattinen tarkistus (esim. axe) kaikissa neljässä näkymässä 1280 px ja 375 px leveydellä
- käyttö pelkällä näppäimistöllä: ohituslinkki, välilehdet nuolinäppäimillä, haku, kysymysten rastit
- 320 px leveä näkymä ilman vaakavieritystä ja tekstin kontrasti vähintään 4,5:1

## Julkaisu ja versiointi

GitHub Pages julkaisee `main`-haaran juuren. Pages-välimuisti on 10 minuuttia, joten päivitä selain tarvittaessa Ctrl+F5:llä.

```
git pull --rebase
git add -A
git commit -m "Kuvaus muutoksesta"
git tag -a vX.Y.Z -m "Kuvaus"
git push --follow-tags
```

Jos push hylätään ("fetch first"), aja `git fetch origin` ja `git rebase origin/main` ja pushaa uudelleen.

Versionumero on muotoa **pää.osa.korjaus**: pää = rakenteen kokonaan uusi versio, osa = uusi kokousopas tai ominaisuus, korjaus = pieni korjaus tai tarkennus. Versio näkyy etusivun alareunassa (`index.html`), ja muutokset kirjataan tiedostoon [CHANGELOG.md](CHANGELOG.md). Pelkkä dokumentaation muutos ei nosta numeroa. `git push --follow-tags` vie myös tagit; pelkkä `git push` ei.

## Miten sivu on tehty

Oppaat, HTML-pohja ja skriptit on laadittu tekoälyavustajien kanssa: opas ja skill ChatGPT:n ja Codexin avulla, GitHub-julkaisu ja saavutettavuuskorjaukset Clauden kanssa. Tilannearviot ovat tekijän omia.

## Lisätietoa

- [Paimion kaupungin kokousjulkaisu](https://julkaisu.paimio.fi/dynasty10/) (esityslistat ja pöytäkirjat)
- [Kuntalaki 410/2015](https://www.finlex.fi/fi/lainsaadanto/2015/410) (Finlex)
- [Laki digitaalisten palvelujen tarjoamisesta 306/2019](https://www.finlex.fi/fi/lainsaadanto/2019/306) (saavutettavuusvaatimukset)

## Lisenssi

Koodi (HTML-pohja, skriptit ja sivujen rakenne) on julkaistu MIT-lisenssillä (katso `LICENSE`).

Lisenssi ei koske aineistoja. Kansion `aineisto` asiakirjat ovat Paimion kaupungin julkisia kokousasiakirjoja, ja niihin sovelletaan kaupungin käyttöehtoja. Viranomaisen päätökset ja lausunnot eivät ole tekijänoikeuden suojaamia (tekijänoikeuslaki 9 §), mutta liitteinä olevat ulkopuolisten laatimat asiakirjat, kuten sopimukset ja raportit, voivat olla. Oppaiden sisältämät tilannearviot ja kysymykset ovat tekijän tekstiä.
