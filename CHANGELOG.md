# Muutosloki

Versionumero on muotoa **pää.osa.korjaus**: pää = sivuston tai oppaan rakenteen kokonaan uusi versio, osa = uusi kokousopas tai ominaisuus, korjaus = pieni korjaus tai tarkennus. Uusin versio ensin.

## 1.4.0

- Oppaaseen 11.11.2026 uusi Investoinnit-välilehti: yhteenveto toimielimittäin (TP2025–2031), hankkeet vuosittain 2026–2031 kymmenessä ryhmässä, suunnittelukauden ulkopuolelle jäävät hankkeet (25,9 milj. €), huomiot ja kysymykset. Hankkeiden summat tarkistettu kirjan välisummiin. § 45:stä linkki näkymään.
- HTML-pohjaan valinnainen `investments`-osio ja välilehti; `build_guide.py` tarkistaa investointiryhmien summat. Ohjeet päivitetty.

## 1.3.0

- Tekoälyhuomautus: oppaan tilannekuvaan "Tekoälyn kokoama opas" -osio, jokaisen näkymän alatunnisteeseen lyhyt maininta ja etusivulle "Tietoa oppaista". Lukijaa pyydetään tarkistamaan olennaiset tiedot alkuperäisistä asiakirjoista ja ilmoittamaan virheistä.
- HTML-pohjaan sama huomautus ja valinnainen `meeting.contact`-kenttä virheilmoitusten osoitteelle.

## 1.2.0

- Oppaasta paluulinkki etusivulle: "← Kaikki kokousoppaat" otsikkoalueen yläreunassa ja alatunnisteessa.
- HTML-pohjaan valinnainen `meeting.home`-kenttä paluulinkille; ohjeet päivitetty.

## 1.1.1

- Etusivun alatunnisteeseen lähde ja maininta epävirallisesta aineistosta.
- Dokumentaatio paimion-ostolaskudata-repon mallin mukaan: README uudistettu (tausta, ominaisuudet, käyttö, aineisto, rajoitukset, lisenssi), uusi ohje `valtuusto-opas/LUEMINUT.md` ja MIT-lisenssi koodille (`LICENSE`).

## 1.1.0

- Saavutettavuus (WCAG 2.1 AA) oppaaseen 11.11.2026 ja HTML-pohjaan: ohituslinkki sisältöön, main-alue, otsikkotasot ilman hyppyjä (lohko-otsikot h3, alaosiot h4), taulukoiden riviotsikot, näppäimistöllä vieritettävät taulukot, välilehtien tabulaattorijärjestys, näkymäkohtainen sivun otsikko, hakutulosten ja ilmoitusten ruudunlukijailmoitus, uuteen välilehteen avautuvien linkkien maininta, koristesymbolit piilotettu ruudunlukijalta ja liikkeen vähentäminen.
- Etusivulle saavutettavuusosio ja palauteosoite.
- Skill-ohjeeseen ja rakennusohjeeseen saavutettavuusohjeet; rakennusohjeen HTML-pohja päivitetty.

## 1.0.0

- Ensimmäinen julkaisu GitHub Pagesissa.
- Etusivu, jossa luettelo kokousoppaista ja linkit työkaluun.
- Kokousopas: Paimion kaupunginvaltuusto 11.11.2026 (§ 43–56).
- valtuusto-opas-skill: ohje, HTML-pohja, JSON-mallit ja Python-skriptit.
- Rakennusohje yhtenä Markdown-tiedostona.
- Kokouksen 11.11.2026 lähdeaineisto ja tarkistusskriptit.
