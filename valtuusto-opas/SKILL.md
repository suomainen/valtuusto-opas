---
name: valtuusto-opas
description: Laadi tai päivitä Paimion tai muun kunnan valtuustokokouksen suomenkielinen, klikattava kokousopas esityslistan ja liitteiden pohjalta. Käytä, kun pyydetään edellisen valtuusto-oppaan kaltaista tilannekuvaa, pykäläkohtaisia arvioita ja vertailulukuja tai itsenäistä HTML-kokousopasta.
---

# Valtuuston kokousopas

Tuota valtuutetun valmistautumiseen yksi selainkäyttöinen HTML-tiedosto. Käytä [HTML-pohjaa](assets/opas.html), joka säilyttää Paimion aiemman oppaan sinisen teeman, aaltoilevan otsikkoalueen ja neljä näkymää. Täytä pohja uuden kokouksen tiedoilla. Valmis opas toimii ilman verkkoa. Alkuperäiset lähteet avataan erillisistä linkeistä.

## Aineisto ja tarkistus

1. Tunnista oikea kokous, toimielin, päivä ja vaihe. Aloita annetusta kokouslinkistä tai etsi kunnan virallinen esityslista. Jos kokouksesta on jo pöytäkirja, kerro tarkastelun vaihe ja erota esitys ja päätös. Jos esityslistaa ei ole julkaistu, kerro mikä aineisto puuttuu.
2. Avaa kaikki pykälät, niiden liitteet ja julkaistut alaliitteet. Kirjaa pykälänumero, suora lähdeosoite, liitteen nimi ja tilanne. Lue myös skannatut sivut, kaaviot ja taulukot, jos tekstiote on vajaa. Tarkista pykälälinkit kokoussivulta. Älä päättele osoitteita pykälänumerosta. Jos ensisijainen verkkotyökalu ei tavoita Dynasty-sivua, kokeile tavallista selainta.
3. Erota pykälät ilman liitteitä, ilmoitettu mutta puuttuva liite, peitetty tai salassa pidettävä sisältö sekä lisäselvitys, jota ei ole luvattu liitteeksi. Merkitse erikseen linkitetty liite, jota et saanut luettua. Kerro tarkistuspäivä ja todellinen kattavuus. Linkitä virallisiin asiakirjoihin ja merkitse tarvittaessa sivut ja taulukot. Tarkista oikeudellisen arvion kannalta olennainen säädös ajantasaisesta Finlexistä.

## Analyysi

- Kerro jokaisesta pykälästä, mitä valtuustolle esitetään ja missä vaiheessa asia on. Pidä asiakirjoissa todetut tiedot ja oma tilannearvio erillään. Arvioi talous, oikeudelliset vaikutukset, toimeenpano, riskit ja avoimet kohdat, kun ne ovat asian kannalta olennaisia. Yksilöi ristiriidat, niiden lähteet ja vaikutus päätökseen.
- Lisää jokaiselle päätöksenteossa olennaiselle luvulle nykyinen arvo tai paras vertailukelpoinen lähtöluku, ehdotettu arvo ja muutos. Merkitse vuosi, jakso, yksikkö ja tiedon laji (voimassa oleva vero tai maksu, alkuperäinen tai muutettu talousarvio, ennuste, toteuma). Hae vertailu tarvittaessa aiemmasta hyväksytystä päätöksestä, talousarviosta tai tilinpäätöksestä. Käytä samaa ajanjaksoa ja rajausta. Ilmaise veroprosenttien erot prosenttiyksikköinä. Näytä euromääräiset kertymät eri riveillä. Merkitse omat laskelmat ja selitä vertailukelpoisuutta rajoittavat erot.
- Jos lähtöluku puuttuu, kerro mistä sitä etsittiin ja mitä tästä seuraa. Älä päättele puuttuvaa kokonaismäärää ilmoitetusta vähennyksestä. Jos pykälässä ei ole vertailtavaa päätöslukua, riittää lyhyt perustelu. Avaa suurten talousasioiden erittelyt tarvittaessa taitettaviin osioihin.
- Kirjoita suomeksi neutraalisti ja konkreettisesti. Käytä esimerkiksi otsikoita **04 / Nousseet kysymykset**, **Huomioitavaa ja avoimia kohtia**, **Tarkennukset ja lähteet**. Muotoile kysymykset niin, että niihin voi vastata luvulla, asiakirjalla, vastuulla, päätösvaiheella tai määräajalla.

## Toimitus

Lue [JSON-ohje](references/tietorakenne.md) ja käytä mukana olevia työkaluja. Komennot ajetaan skillin kansiosta tai antamalla skripteille täydet polut. Tarvitset Python 3:n. Skriptit käyttävät sen vakiokirjastoa.

1. Tallenna tarkistetut kokous-, pykälä- ja liitetiedot [esityslista-JSONin mallin](examples/esityslista-esimerkki.json) mukaan. Luo täytettävä tiedosto komennolla `python scripts/prepare_meeting.py esityslista.json kokous.json`.
2. Täydennä kokous-JSON aineiston pohjalta. [Täytetty esimerkki](examples/kokous-esimerkki.json) näyttää vertailurivin, liitteen ja tarkennuskohdan. Tee uudet päätelmät ja laskelmat aina uuden kokouksen lähteistä.
3. Rakenna yksi HTML-tiedosto komennolla `python scripts/build_guide.py kokous.json paimio-valtuusto-PP-KK-VVVV.html`. Tallenna lopputulos työtilaan uudella kokouspäivän nimellä. Väliaineisto ja luonnokset eivät kuulu jaettavaan pakettiin.

Tarkista, että listatut pykälät ja liitteet vastaavat aineistoa ja uudet tiedot näkyvät tilannekuvassa, pykälänäkymässä, kysymyksissä ja lähteissä. Kokeile pykälähakua, linkkejä ja puhelinnäkymää, kun selain on käytettävissä. Varmista, ettei tiedosto lataa tyylejä, kirjasimia, ohjelmakoodia, kuvia tai dataa verkosta. Kerro mahdollisista aineiston katveista ja anna linkki valmiiseen HTML-tiedostoon.

## Saavutettavuus

Opas noudattaa WCAG 2.1 AA -tasoa (laki 306/2019). HTML-pohja hoitaa rakenteen: ohituslinkki sisältöön, otsikkotasot h1 → h2 → h3 → h4 ilman hyppyjä, sarake- ja riviotsikot taulukoissa, näppäimistöllä toimivat välilehdet, ruudunlukijalle ilmoitettavat hakutulokset ja ilmoitukset, uuteen välilehteen avautuvien linkkien maininta, näkymäkohtainen sivun otsikko sekä liikkeen vähentäminen käyttäjän asetuksen mukaan. Sisältöä kirjoittaessa:

- Kirjoita pykälien otsikot, nostot ja linkkien nimet niin, että ne ymmärtää ilman ympäröivää tekstiä. Älä käytä linkin nimenä pelkkää ”tästä” tai ”linkki”.
- Taulukon ensimmäinen sarake on riviotsikko. Laita siihen mittarin tai erän nimi, ei lukua.
- Älä välitä tietoa pelkällä värillä, symbolilla tai lyhenteellä. Avaa lyhenteet (esim. TA, EN) tekstissä vähintään kerran.
- Kun muutat HTML-pohjaa, tarkista näppäimistökäyttö (Tab, nuolinäppäimet välilehdillä), tekstin kontrasti vähintään 4,5:1 ja 320 px leveä näkymä ilman vaakavieritystä. Automaattisen tarkistuksen voi tehdä esimerkiksi axe-työkalulla.

## Käyttöönotto ja jakaminen

Jaa koko `valtuusto-opas`-kansio. Kun kansio on omassa Codexin `.codex/skills`-hakemistossa, aloita uusi keskustelu ja käytä pyyntöä: ”$valtuusto-opas Tee Paimion seuraavan valtuuston kokousopas tästä esityslistasta” ja lisää esityslistan linkki. Valmiin oppaan lukijalle riittää pelkkä HTML-tiedosto.
