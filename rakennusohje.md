# Paimion valtuuston kokousopas – koko rakennusohje

Tämän yhden Markdown-tiedoston voi jakaa sellaisenaan. Se sisältää kokousoppaan laatimisohjeen, molemmat JSON-mallit, Python-skriptit ja täydellisen HTML-pohjan. Lopputulos on yksi klikattava HTML-tiedosto. Sen avaamiseen riittää selain, ja alkuperäiset lähdelinkit toimivat verkkoyhteydellä.

## Käytä ohjetta Codexissa

Liitä tämä Markdown-tiedosto keskusteluun ja anna uuden kokouksen esityslistan linkki. Voit käyttää tätä pyyntöä:

> Lue liitetty valtuusto-oppaan rakennusohje. Tee Paimion kaupunginvaltuuston kokouksesta sen mukainen suomenkielinen HTML-opas. Luo koodilohkoista tarvittavat tiedostot, käy läpi esityslista ja sen liitteet, täytä kokous-JSON tarkistetuilla tiedoilla ja rakenna jaettava HTML-tiedosto. Esityslistan linkki on [lisää linkki tähän].

## Rakenna opas itse

1. Tee työkansio. Tallenna alla olevat viisi koodilohkoa otsikoissa annetuilla nimillä ja kansiopoluilla. Käytä UTF-8-koodausta. Otsikot ja koodilohkojen aidat kuuluvat tähän ohjeeseen.
2. Kopioi esimerkin esityslista-JSON nimelle `esityslista.json` työkansion juureen. Vaihda siihen oikean kokouksen tiedot ja lisää kaikki pykälät ja niiden liitteet esityslistan järjestyksessä. Käytä tarkistettuja suoria lähdelinkkejä.
3. Luo täytettävä `kokous.json` ensimmäisellä komennolla. Täydennä se aineiston perusteella. Täytetty JSON-esimerkki havainnollistaa, miltä valmis pykälä, vertailu ja tarkennus näyttävät.
4. Rakenna HTML toisella komennolla. Korvaa tiedostonimen päivämäärä kokouspäivällä. Komennot ajetaan työkansion juuresta Python 3:lla. Lisäpaketteja ei tarvita.

```text
python scripts/prepare_meeting.py esityslista.json kokous.json
python scripts/build_guide.py kokous.json paimio-valtuusto-PP-KK-VVVV.html
```

Voit kokeilla rakentamista suoraan täytetystä esimerkistä komennolla `python scripts/build_guide.py examples/kokous-esimerkki.json opas-esimerkki.html`. Esimerkkikokous ja sen luvut ovat kuvitteellisia.

## Aineisto ja tarkistus

1. Tunnista oikea kokous, toimielin, päivä ja vaihe. Aloita annetusta kokouslinkistä tai etsi kunnan virallinen esityslista. Jos kokouksesta on jo pöytäkirja, kerro tarkastelun vaihe ja erota esitys ja päätös. Jos esityslistaa ei ole julkaistu, kerro mikä aineisto puuttuu.
2. Avaa kaikki pykälät, niiden liitteet ja julkaistut alaliitteet. Kirjaa pykälänumero, suora lähdeosoite, liitteen nimi ja tilanne. Lue myös skannatut sivut, kaaviot ja taulukot, jos tekstiote on vajaa. Tarkista pykälälinkit kokoussivulta. Älä päättele osoitteita pykälänumerosta. Jos ensisijainen verkkotyökalu ei tavoita Dynasty-sivua, kokeile tavallista selainta.
3. Erota pykälät ilman liitteitä, ilmoitettu mutta puuttuva liite, peitetty tai salassa pidettävä sisältö sekä lisäselvitys, jota ei ole luvattu liitteeksi. Merkitse erikseen linkitetty liite, jota et saanut luettua. Kerro tarkistuspäivä ja todellinen kattavuus. Linkitä virallisiin asiakirjoihin ja merkitse tarvittaessa sivut ja taulukot. Tarkista oikeudellisen arvion kannalta olennainen säädös ajantasaisesta Finlexistä.

## Analyysi

- Kerro jokaisesta pykälästä, mitä valtuustolle esitetään ja missä vaiheessa asia on. Pidä asiakirjoissa todetut tiedot ja oma tilannearvio erillään. Arvioi talous, oikeudelliset vaikutukset, toimeenpano, riskit ja avoimet kohdat, kun ne ovat asian kannalta olennaisia. Yksilöi ristiriidat, niiden lähteet ja vaikutus päätökseen.
- Lisää jokaiselle päätöksenteossa olennaiselle luvulle nykyinen arvo tai paras vertailukelpoinen lähtöluku, ehdotettu arvo ja muutos. Merkitse vuosi, jakso, yksikkö ja tiedon laji (voimassa oleva vero tai maksu, alkuperäinen tai muutettu talousarvio, ennuste, toteuma). Hae vertailu tarvittaessa aiemmasta hyväksytystä päätöksestä, talousarviosta tai tilinpäätöksestä. Käytä samaa ajanjaksoa ja rajausta. Ilmaise veroprosenttien erot prosenttiyksikköinä. Näytä euromääräiset kertymät eri riveillä. Merkitse omat laskelmat ja selitä vertailukelpoisuutta rajoittavat erot.
- Kun käsitellään talousarviota, kokoa investointiosa omaksi Investoinnit-näkymäksi (`investments`): yhteenveto toimielimittäin, hankkeet vuosittain koko suunnittelukaudelta ja suunnittelukauden ulkopuolelle jäävät hankkeet. Jos tekstiotteen tyhjät vuosisarakkeet ovat sulautuneet, päättele vuodet välisummista ja varmista, että jokainen ryhmä täsmää. Kirjaa välisummien ja yhteenvedon ristiriidat huomioihin.
- Jos lähtöluku puuttuu, kerro mistä sitä etsittiin ja mitä tästä seuraa. Älä päättele puuttuvaa kokonaismäärää ilmoitetusta vähennyksestä. Jos pykälässä ei ole vertailtavaa päätöslukua, riittää lyhyt perustelu. Avaa suurten talousasioiden erittelyt tarvittaessa taitettaviin osioihin.
- Kirjoita suomeksi neutraalisti ja konkreettisesti. Käytä esimerkiksi otsikoita **04 / Nousseet kysymykset**, **Huomioitavaa ja avoimia kohtia**, **Tarkennukset ja lähteet**. Muotoile kysymykset niin, että niihin voi vastata luvulla, asiakirjalla, vastuulla, päätösvaiheella tai määräajalla. Hae lopuksi jokaiseen kysymykseen vastausta kokousaineistosta ja verkosta (kunnan muut päätökset, Finlex, muiden kuntien ja kuntayhtymien asiakirjat, Kuntaliitto, Verohallinto, uutiset) ja kirjaa se `answers`-kenttään tilan ja lähteiden kanssa. Merkitse omat laskelmat ja päätelmät, äläkä esitä löytymätöntä tietoa vastauksena.

## Kokous-JSONin kentät

- `meeting.time` ja `meeting.venue` ovat valinnaisia. `meeting.sources` voi sisältää koko oppaan yhteisiä lähteitä ja säädöslinkkejä. Valinnainen `meeting.home` on paluulinkin osoite oppaiden luetteloon, esimerkiksi `"../index.html"`, kun opas tallennetaan repon `oppaat`-kansioon. Ilman sitä paluulinkkiä ei näytetä. Valinnainen `meeting.contact` on sähköpostiosoite, johon lukija voi ilmoittaa virheistä; se näkyy tilannekuvan tekoälyhuomautuksessa.
- `overview.stats`, `overview.highlights`, `overview.sources` ja `overview.comparisonNote` ovat valinnaisia. Nostoissa ja tarkennuksissa `n` viittaa olemassa olevaan pykälään.
- Jokaisella pykälällä on `facts`, `risks` ja `questions` tekstilistoina. Tyhjä lista sopii, jos riskiä tai kysymystä ei noussut. `critical` on valinnainen huomion merkki. `sources` sisältää pykälän muut lähteet.
- Jokaisella pykälällä on `comparison.note`. Jos vertailtavaa lukua ei ole, selitä syy siinä. `rows` voi silloin puuttua. Oletuksena jokainen rivi sisältää neljä solua. `headers` voi korvata oletusotsikot esimerkiksi toteumavertailussa.
- `attachments` listaa liitteet ja alaliitteet. Käytä kuvaavaa tilaa, esimerkiksi **Luettu**, **Osin peitetty**, **Linkki puuttuu** tai **Linkitetty, jäi lukematta**. Jätä `url` pois vain, kun osoitetta ei ole. Kerro olennainen liitteen sisältö tai saatavuuden syy kentässä `summary`.
- `answers` on valinnainen pykäläkohtainen lista, jonka järjestys vastaa `questions`-listaa. Kukin vastaus sisältää `status` (esim. **Vastaus löytyi**, **Osittainen vastaus**, **Ei löytynyt**), `text` ja `sources`. Vastaus näkyy kysymyksen alla ”Mitä löytyi” -kohtana. Tyhjä kohta (`null`) jättää vastauksen pois.
- `investments` on valinnainen. Kun se on annettu, oppaaseen tulee Investoinnit-välilehti. Kentät: `title`, `lead`, `note`, valinnaiset `eyebrow`, `focusYear` (esim. `"TA2027"`) ja `stats`; `years` (sarakeotsikot, esim. `["TA2026","TA2027","2028",…]`); `summary` (`title`, `note`, `headers`, `rows`, `totals`, `sources`); `groups` (kukin `title`, `page`, `total` vuosittain, valinnainen `income` ja `rows` muodossa `[hanke, laji, arvo vuosittain…]`, tyhjä vuosi `null`); `outside` (`title`, `note`, `tables`: `title`, `rows` `[hanke, arvio]`, `total`; sekä `total`); `risks`, `questions` ja `sources`. Luvut ovat tuhansia euroja. `build_guide.py` tarkistaa, että hankkeiden summat täsmäävät välisummiin.
- `details` on valinnainen lista taitettavia erittelyjä. Kukin osio sisältää `title` ja tarvittaessa `text`, `sources` tai taulukon `headers` ja `rows`.
- Kaikki `sources`-kentät ovat `[nimi, URL]`-pareja. Käytä suoria https-osoitteita, kun sellaisia on. Lisää sivunumero linkin nimeen, vaikka PDF:n sivuankkuri ei toimisi kaikissa selaimissa.

## Saavutettavuus

Opas noudattaa WCAG 2.1 AA -tasoa (laki 306/2019). HTML-pohja hoitaa rakenteen: ohituslinkki sisältöön, otsikkotasot h1 → h2 → h3 → h4 ilman hyppyjä, sarake- ja riviotsikot taulukoissa, näppäimistöllä toimivat välilehdet, ruudunlukijalle ilmoitettavat hakutulokset ja ilmoitukset, uuteen välilehteen avautuvien linkkien maininta, näkymäkohtainen sivun otsikko sekä liikkeen vähentäminen käyttäjän asetuksen mukaan. Sisältöä kirjoittaessa:

- Kirjoita pykälien otsikot, nostot ja linkkien nimet niin, että ne ymmärtää ilman ympäröivää tekstiä. Älä käytä linkin nimenä pelkkää ”tästä” tai ”linkki”.
- Taulukon ensimmäinen sarake on riviotsikko. Laita siihen mittarin tai erän nimi, ei lukua.
- Älä välitä tietoa pelkällä värillä, symbolilla tai lyhenteellä. Avaa lyhenteet (esim. TA, EN) tekstissä vähintään kerran.
- Kun muutat HTML-pohjaa, tarkista näppäimistökäyttö (Tab, nuolinäppäimet välilehdillä), tekstin kontrasti vähintään 4,5:1 ja 320 px leveä näkymä ilman vaakavieritystä. Automaattisen tarkistuksen voi tehdä esimerkiksi axe-työkalulla.

## Tarkista ennen jakamista

- Vertaa pykäläluetteloa ja liitteitä viralliseen esityslistaan. Tarkista, että jokaisen luvun vuosi, vertailupohja ja lähde näkyvät ja että puuttuvat tiedot on merkitty.
- Avaa HTML selaimessa. Tarkista tilannekuva, pykälänäkymä, nousseet kysymykset ja tarkennukset. Kokeile hakua, pykälien välillä liikkumista, lähdelinkkejä ja puhelinnäkymää.
- Kokeile oppaan käyttöä pelkällä näppäimistöllä ja 320 px leveällä näkymällä.
- Avaa sama HTML ilman verkkoyhteyttä. Oppaan sisällön ja toimintojen pitää avautua tiedostosta. Jaa lukijalle valmis HTML-tiedosto.

## Kokonaiset tiedostot

### `examples/esityslista-esimerkki.json`

```json
{
  "meeting": {
    "city": "Esimerkkikunta",
    "date": "12.5.2027",
    "time": "Klo 18.00",
    "venue": "Valtuustosali",
    "url": "https://example.org/esityslista"
  },
  "items": [
    {
      "n": 7,
      "title": "Palvelumaksun tarkistus",
      "short": "Palvelumaksu",
      "url": "https://example.org/pykala-7",
      "attachments": [
        {"title": "Maksutaulukko", "url": "https://example.org/maksut.pdf"}
      ]
    }
  ]
}
```

### `examples/kokous-esimerkki.json`

```json
{
  "meeting": {
    "city": "Esimerkkikunta",
    "date": "12.5.2027",
    "time": "Klo 18.00",
    "venue": "Valtuustosali",
    "reviewed": "10.5.2027",
    "stage": "Tarkastelu perustuu kokouksen esityslistaan.",
    "coverage": "Tarkistettu yksi pykälä ja sen julkinen liite.",
    "url": "https://example.org/esityslista"
  },
  "overview": {
    "title": "Palvelumaksu esitetään korotettavaksi",
    "lead": "Ehdotus nostaisi kuukausimaksua 5 euroa.",
    "stats": [
      {"label": "Kuukausimaksu", "value": "25 €", "note": "Voimassa 20 €. Ehdotus 25 €."}
    ],
    "highlights": [
      {"n": 7, "title": "Palvelumaksu", "text": "Kuukausimaksuun ehdotetaan 5 euron korotusta."}
    ]
  },
  "items": [
    {
      "n": 7,
      "title": "Palvelumaksun tarkistus",
      "short": "Palvelumaksu",
      "tag": "Maksut",
      "critical": true,
      "url": "https://example.org/pykala-7",
      "facts": ["Kuukausimaksuksi esitetään 25 euroa 1.8.2027 alkaen."],
      "assessment": "Korotuksen vaikutus kunnan tuloihin riippuu käyttäjämäärästä.",
      "risks": ["Päätöksen käyttäjävaikutuksista ei ole laskelmaa."],
      "questions": ["Kuinka monen käyttäjän maksua muutos koskee?"],
      "comparison": {
        "note": "Vertailu koskee samaa palvelua ja kuukausimaksua.",
        "rows": [["Kuukausimaksu", "20 € · voimassa", "25 € · ehdotus 1.8.2027", "+5 € / kk"]],
        "sources": [["Maksutaulukko, s. 2", "https://example.org/maksut.pdf#page=2"]]
      },
      "attachments": [
        {"title": "Maksutaulukko", "status": "Luettu", "summary": "Taulukossa näkyvät nykyinen ja ehdotettu maksu.", "url": "https://example.org/maksut.pdf"}
      ]
    }
  ],
  "issues": [
    {"n": 7, "type": "Täydentävä tieto", "title": "Käyttäjämäärä", "text": "Käyttäjämäärää ei kerrota julkisessa aineistossa."}
  ]
}
```

### `scripts/prepare_meeting.py`

```python
"""Muodosta täytettävä kokousdata tarkistetuista esityslistan tiedoista."""

import argparse
import json
from pathlib import Path

from build_guide import require_text, require_url


def prepare(agenda):
    source = agenda["meeting"]
    require_text(source, "city", "date", "url")
    require_url(source["url"])
    items = []
    seen = set()
    for entry in agenda["items"]:
        number = entry["n"]
        if type(number) is not int or number < 1 or number in seen:
            raise ValueError(f"Virheellinen tai toistuva pykälänumero: {number}")
        seen.add(number)
        require_text(entry, "title", "url")
        require_url(entry["url"])
        attachments = []
        for source_attachment in entry.get("attachments", []):
            require_text(source_attachment, "title")
            attachment = {
                "title": source_attachment["title"],
                "status": "Tarkistamatta",
                "summary": "",
            }
            if source_attachment.get("url"):
                require_url(source_attachment["url"])
                attachment["url"] = source_attachment["url"]
            attachments.append(attachment)
        items.append({
            "n": number,
            "title": entry["title"],
            "short": entry.get("short", entry["title"]),
            "tag": "",
            "url": entry["url"],
            "facts": [],
            "assessment": "",
            "risks": [],
            "questions": [],
            "comparison": {"note": "", "rows": []},
            "attachments": attachments,
        })
    if not items:
        raise ValueError("Esityslistassa pitää olla vähintään yksi pykälä.")

    meeting = {key: source[key] for key in ("city", "date", "url", "time", "venue") if key in source}
    meeting.update(reviewed="", stage="", coverage="")
    return {
        "meeting": meeting,
        "overview": {"title": "", "lead": "", "stats": [], "highlights": []},
        "items": items,
        "issues": [],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Kokouksen ja pykälien perustiedot JSON-tiedostona")
    parser.add_argument("output", type=Path, help="Uusi täytettävä kokous-JSON")
    args = parser.parse_args()
    try:
        if args.output.suffix.lower() != ".json":
            raise ValueError("Tulostiedoston päätteen pitää olla .json.")
        agenda = json.loads(args.input.read_text(encoding="utf-8-sig"))
        draft = prepare(agenda)
        # Leave an existing draft or source file intact.
        with args.output.open("x", encoding="utf-8") as output:
            output.write(json.dumps(draft, ensure_ascii=False, indent=2) + "\n")
    except (KeyError, TypeError, ValueError, AttributeError, OSError) as error:
        parser.exit(1, f"Kokousdatan pohjan luonti ei onnistunut: {error}\n")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
```

### `scripts/build_guide.py`

```python
"""Build a self-contained council guide from UTF-8 JSON and the bundled HTML."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit


TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "opas.html"
MARKER = "__GUIDE_DATA__"


def require_text(record, *keys):
    for key in keys:
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError(f"Puuttuva tai tyhjä tekstikenttä: {key}")


def require_url(url):
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Lähdelinkin pitää olla kokonainen verkko-osoite: {url}")


def validate_links(record):
    for label, url in record.get("sources", []):
        require_text({"label": label}, "label")
        require_url(url)


def validate_table(record, default_columns=None):
    rows = record.get("rows", [])
    headers = record.get("headers")
    if rows:
        columns = len(headers) if headers else default_columns
        if not columns or any(not isinstance(row, list) or len(row) != columns for row in rows):
            raise ValueError("Taulukon rivien ja otsikoiden sarakemäärät eivät vastaa toisiaan.")


def validate(data):
    meeting, overview, items = (data[key] for key in ("meeting", "overview", "items"))
    require_text(meeting, "city", "date", "reviewed", "stage", "coverage", "url")
    require_url(meeting["url"])
    require_text(overview, "title", "lead")
    for stat in overview.get("stats", []):
        require_text(stat, "label", "value", "note")

    numbers = [item["n"] for item in items]
    if not numbers or any(type(n) is not int or n < 1 for n in numbers):
        raise ValueError("Tarvitaan vähintään yksi pykälä ja positiiviset pykälänumerot.")
    if len(set(numbers)) != len(numbers):
        raise ValueError("Pykälänumerot eivät saa toistua.")
    for highlight in overview.get("highlights", []):
        require_text(highlight, "title", "text")
        if highlight["n"] not in numbers:
            raise ValueError(f"Noston pykälä puuttuu: {highlight['n']}")
    for issue in data.get("issues", []):
        require_text(issue, "type", "title", "text")
        if issue["n"] not in numbers:
            raise ValueError(f"Tarkennuskohdan pykälä puuttuu: {issue['n']}")

    validate_links(meeting)
    validate_links(overview)
    for item in items:
        require_text(item, "title", "short", "tag", "assessment", "url")
        require_url(item["url"])
        for key in ("facts", "risks", "questions"):
            if not isinstance(item[key], list) or any(not isinstance(value, str) for value in item[key]):
                raise ValueError(f"§ {item['n']}: {key} on tekstilista.")
        comparison = item["comparison"]
        require_text(comparison, "note")
        validate_table(comparison, default_columns=4)
        validate_links(comparison)
        validate_links(item)
        for section in item.get("details", []):
            require_text(section, "title")
            validate_table(section)
            validate_links(section)
        for attachment in item.get("attachments", []):
            require_text(attachment, "title", "status", "summary")
            if attachment.get("url"):
                require_url(attachment["url"])
        answers = item.get("answers", [])
        if len(answers) > len(item["questions"]):
            raise ValueError(f"§ {item['n']}: vastauksia on enemmän kuin kysymyksiä.")
        for answer in answers:
            if answer:
                require_text(answer, "status", "text")
                validate_links(answer)

    investments = data.get("investments")
    if investments:
        validate_investments(investments)


def validate_investments(inv):
    require_text(inv, "title", "lead", "note")
    years = inv["years"]
    if not years or any(not isinstance(year, str) for year in years):
        raise ValueError("investments.years on lista vuosien otsikoita.")
    summary = inv["summary"]
    require_text(summary, "title", "note")
    validate_table({"headers": summary["headers"], "rows": summary["rows"] + summary.get("totals", [])})
    validate_links(summary)
    for group in inv["groups"]:
        require_text(group, "title")
        if len(group["total"]) != len(years) or any(len(row) != len(years) + 2 for row in group["rows"]):
            raise ValueError(f"Investointiryhmän sarakkeet eivät vastaa vuosia: {group['title']}")
        for k, year in enumerate(years):
            total = sum(row[k + 2] or 0 for row in group["rows"])
            if total != group["total"][k]:
                raise ValueError(f"Investointiryhmän {group['title']} hankkeiden summa {year} on {total}, välisumma {group['total'][k]}.")
    outside = inv.get("outside")
    if outside:
        require_text(outside, "title", "note")
        for table in outside["tables"]:
            if sum(row[1] for row in table["rows"]) != table["total"]:
                raise ValueError(f"Taulukon {table['title']} rivien summa ei vastaa yhteissummaa.")
    for key in ("risks", "questions"):
        if any(not isinstance(value, str) for value in inv.get(key, [])):
            raise ValueError(f"investments.{key} on tekstilista.")
    validate_links(inv)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Kokoustiedot JSON-tiedostona")
    parser.add_argument("output", type=Path, help="Valmis HTML-tiedosto")
    args = parser.parse_args()
    try:
        if args.output.suffix.lower() != ".html" or args.output.resolve() == TEMPLATE:
            raise ValueError("Valitse pohjasta erillinen .html-tulostiedosto.")
        data = json.loads(args.input.read_text(encoding="utf-8-sig"))
        validate(data)
        template = TEMPLATE.read_text(encoding="utf-8")
        if template.count(MARKER) != 1:
            raise ValueError("HTML-pohjan kokoustietojen paikka puuttuu tai toistuu.")
        # Prevent source text from closing the HTML script element.
        payload = json.dumps(data, ensure_ascii=False, allow_nan=False).replace("<", r"\u003c")
        args.output.write_text(template.replace(MARKER, payload), encoding="utf-8")
    except (KeyError, TypeError, ValueError, AttributeError, OSError) as error:
        parser.exit(1, f"Kokousoppaan luonti ei onnistunut: {error}\n")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
```

### `assets/opas.html`

```html
<!doctype html>
<html lang="fi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Valtuuston kokousopas</title>
<style>
:root{--navy:#072b4c;--blue:#0f5ba1;--yellow:#ffd166;--gray:#f2f2f2;--bg:#fff;--paper:#fff;--ink:#2d2f30;--soft:#6b6f73;--line:#e3e3e3;--brand:#0f5ba1;--tint:#e4ebf5;--tint-2:#ecf5fd;--warn:#805300;--warnbg:#fff5da;--risk:#a13632;--riskbg:#fbece8;--shadow:0 2px 10px rgba(0,0,0,.07)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}button,input,a{-webkit-tap-highlight-color:transparent}button,input{font:inherit}button,a{touch-action:manipulation}button{cursor:pointer}a{color:var(--brand);text-underline-offset:3px}a:hover{text-decoration-thickness:2px}button:focus-visible,a:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--brand);outline-offset:4px}button{color:inherit}header{background:var(--paper);border-bottom:1px solid var(--line);padding:25px 34px 22px}.topline{display:flex;align-items:center;justify-content:space-between;gap:20px;max-width:1450px;margin:auto}.eyebrow{text-transform:uppercase;font-size:12px;font-weight:750;letter-spacing:1.8px;color:var(--brand)}h1{font-size:clamp(24px,3vw,36px);line-height:1.2;letter-spacing:-1.2px;margin:5px 0 8px}h2{font-size:28px;line-height:1.25;letter-spacing:-.7px;margin:0 0 14px}h3{font-size:18px;line-height:1.4;margin:0 0 10px}p{margin:0 0 14px}.sub{color:var(--soft);font-size:14px}.small{font-size:13px;color:var(--soft)}.btn{border:1px solid var(--line);background:var(--paper);border-radius:9px;padding:8px 14px;font-size:14px;font-weight:600}.btn:hover{background:var(--tint)}.tabs{display:flex;gap:6px;flex-wrap:wrap;max-width:1450px;margin:22px auto 0}.tab{border:0;background:transparent;border-radius:8px;padding:9px 15px;font-size:14px;font-weight:650;color:var(--soft)}.tab[aria-selected=true]{background:var(--ink);color:var(--paper)}.layout{display:grid;grid-template-columns:284px minmax(0,1fr);max-width:1518px;margin:auto;align-items:start}.sidebar{position:sticky;top:0;height:100dvh;overflow:auto;padding:26px 18px 30px 34px;border-right:1px solid var(--line)}.search{width:100%;border:1px solid var(--line);border-radius:9px;padding:10px 12px;background:var(--paper);color:var(--ink);margin:9px 0 12px;font-size:14px}.nav-item{display:flex;width:100%;text-align:left;gap:10px;border:0;background:transparent;padding:10px 11px;border-radius:8px;font-size:13px;line-height:1.4;margin:3px 0}.nav-item:hover{background:var(--paper)}.nav-item[aria-current=true]{background:var(--tint);color:var(--brand);font-weight:700}.num{font-variant-numeric:tabular-nums;flex:0 0 29px;color:var(--soft)}.nav-item[aria-current=true] .num{color:var(--brand)}.dot{height:6px;width:6px;background:var(--risk);border-radius:50%;margin-top:6px;flex:0 0 6px}.navtext{flex:1}.content{padding:32px 40px 70px;min-width:0;max-width:1150px}.intro{max-width:780px}.lead{font-size:19px;line-height:1.6;max-width:800px}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin:24px 0}.stat,.box{background:var(--paper);border:1px solid var(--line);border-radius:13px;padding:21px;box-shadow:var(--shadow)}.value{display:block;font-size:28px;font-weight:730;letter-spacing:-1px;font-variant-numeric:tabular-nums;line-height:1.4}.stat .small{display:block;margin-top:5px}.section{margin-top:27px}.priority-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.priority{display:block;width:100%;text-align:left;border:1px solid var(--line);border-radius:12px;background:var(--paper);padding:18px;color:inherit}.priority:hover{border-color:var(--brand);transform:translateY(-1px)}.priority strong{display:block;font-size:16px;margin:6px 0}.priority p{font-size:14px;color:var(--soft);margin:0}.badge{display:inline-block;padding:3px 9px;border-radius:5px;background:var(--tint);color:var(--brand);font-size:12px;font-weight:700;line-height:1.6}.badge.warn{background:var(--warnbg);color:var(--warn)}.badge.risk{background:var(--riskbg);color:var(--risk)}.note{border-left:3px solid var(--brand);padding:10px 16px;background:var(--tint);border-radius:0 8px 8px 0;margin:18px 0;font-size:14px}.note.warn{border-color:var(--warn);background:var(--warnbg)}.legend{display:flex;gap:18px;flex-wrap:wrap;margin:22px 0 18px;font-size:13px;color:var(--soft)}.legend b{color:var(--ink)}.item-head{display:flex;justify-content:space-between;gap:15px;margin-bottom:12px}.item-head h2{margin:6px 0 10px}.tagrow{display:flex;gap:7px;flex-wrap:wrap}.block{padding:23px 0;border-top:1px solid var(--line)}.block:first-of-type{border-top:0}.block-label{display:flex;align-items:center;gap:8px;margin-bottom:12px;font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--brand)}.block-label.assess{color:var(--warn)}.block-label.risks{color:var(--risk)}ul,ol{padding-left:23px;margin:8px 0 0}li{margin:7px 0}table{width:100%;border-collapse:collapse;font-size:14px}th{text-align:left;color:var(--soft);font-size:12px;letter-spacing:.3px}td,th{padding:11px 10px;border-bottom:1px solid var(--line);vertical-align:top}td:first-child,th:first-child{padding-left:0}td:last-child,th:last-child{padding-right:0}.table-scroll{overflow-x:auto}.financial td:not(:first-child),.financial th:not(:first-child){text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}.sources{display:flex;gap:8px;flex-wrap:wrap}.source{display:inline-block;border:1px solid var(--line);padding:7px 10px;border-radius:7px;font-size:13px;background:var(--paper);text-decoration:none}.source:hover{background:var(--tint)}.pager{display:flex;justify-content:space-between;gap:10px;margin-top:24px;border-top:1px solid var(--line);padding-top:20px}details{border-bottom:1px solid var(--line);padding:16px 0}summary{cursor:pointer;font-weight:650;line-height:1.4}details[open] summary{margin-bottom:15px}summary .small{font-weight:400}.q-list{list-style:none;padding:0}.q-list label{display:flex;gap:12px;align-items:flex-start;cursor:pointer;padding:7px 0}.q-list input{margin-top:7px;accent-color:var(--brand);width:17px;height:17px;flex-shrink:0}.q-list input:checked+span{text-decoration:line-through;color:var(--soft)}.q-toolbar{display:flex;gap:12px;justify-content:space-between;align-items:center;margin:20px 0}.empty{padding:20px 0;color:var(--soft)}.issue{padding:19px 0;border-bottom:1px solid var(--line)}.issue strong{display:block;margin:6px 0}.issue p{margin:0;font-size:14px}.jump{border:0;background:transparent;color:var(--brand);font-weight:650;padding:0;text-decoration:underline;text-underline-offset:3px}.mobile-select{display:none}footer{margin-top:35px;padding-top:18px;border-top:1px solid var(--line);font-size:12px;color:var(--soft)}[hidden]{display:none!important}.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:var(--ink);color:var(--paper);padding:10px 20px;border-radius:9px;z-index:5}.all-source-list{display:grid;gap:8px}.all-source-list a{font-size:14px}.count{font-variant-numeric:tabular-nums}

@media(max-width:900px){header{padding:22px}.layout{grid-template-columns:240px 1fr}.sidebar{padding:24px 14px 24px 22px}.content{padding:27px 25px 55px}.stats{grid-template-columns:1fr}.stat{padding:14px 18px}.value{font-size:25px}.priority-grid{grid-template-columns:1fr}}
@media(max-width:650px){header{padding:21px 18px 16px}.topline{align-items:start}.print{display:none}.tabs{gap:3px;margin-top:18px}.tab{padding:8px 10px;font-size:13px}.layout{display:block}.sidebar{position:static;height:auto;border:0;padding:16px 18px 0}.sidebar nav,.sidebar .nav-caption,.sidebar .small{display:none}.search{margin:0}.mobile-select{display:block;width:100%;padding:10px;margin-top:9px;border:1px solid var(--line);border-radius:8px;background:var(--paper);color:var(--ink);font:inherit;font-size:14px}.content{padding:23px 18px 45px}h2{font-size:25px}.lead{font-size:17px}.stats{gap:8px;margin:20px 0}.stat .value{display:inline;font-size:24px;margin-right:9px}.stat .small{display:inline}.stat p{font-size:12px;margin:3px 0 0}.block{padding:20px 0}.source{font-size:12px}table{font-size:13px}.item-head{display:block}.legend{gap:9px;font-size:12px}.q-toolbar{align-items:start}.badge{font-size:11px}}
@media print{body{background:white;color:black;font-size:11pt}header{padding:0 0 14px}.tabs,.sidebar,.print,.pager,.q-toolbar,.toast{display:none!important}.layout{display:block}.content{padding:20px 0;max-width:none}.stat,.box{box-shadow:none;break-inside:avoid}a{color:inherit}.block,details,.issue{break-inside:avoid}details:not([open])>*:not(summary){display:block}.stats{grid-template-columns:repeat(3,1fr)}footer{font-size:9pt}}

/* Teeman esikuva: https://suomainen.github.io/paimion-ostolaskudata/#year=5 */
body{border-top:14px solid var(--blue)}
header{padding:20px 20px 0;border-bottom:0}
.topline{position:relative;isolation:isolate;overflow:hidden;min-height:228px;padding:35px 32px 64px;border-radius:24px 24px 0 0;background:linear-gradient(105deg,var(--navy),#164e7d 68%,#3f7fbf);color:#fff}
.topline::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:38px;z-index:-1;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 70' preserveAspectRatio='none'%3E%3Cpath fill='white' d='M0 48C200 80 420 0 680 16S1120 70 1440 12V70H0Z'/%3E%3C/svg%3E") center/100% 100% no-repeat}
.topline .eyebrow{color:var(--yellow);font-size:13px;letter-spacing:1px;font-weight:500}
h1{font-size:clamp(28px,3.8vw,46px);letter-spacing:-.8px;font-weight:600;line-height:1.15;margin:13px 0 15px}
.topline .sub{color:#fff;font-size:15px}
h2,h3,.value{color:var(--navy);font-weight:600}
h2{letter-spacing:-.4px}h3{font-size:19px}
.btn{background:var(--blue);color:#fff;border-color:var(--blue);border-radius:8px;font-weight:500;min-height:42px}
.btn:hover{background:var(--navy);border-color:var(--navy)}
.topline .btn{border:1px solid #ffffff99;background:transparent;flex-shrink:0}
.topline .btn:hover{background:#ffffff20;border-color:#fff}
.tabs{gap:8px;margin:12px auto 22px;padding:0 12px}
.tab{background:#fff;border:2px solid var(--blue);color:var(--blue);font-weight:500;min-height:44px;padding:8px 16px}
.tab:hover{background:var(--tint-2)}
.tab[aria-selected=true]{background:var(--blue);color:#fff}
.sidebar{padding-top:24px;background:var(--paper)}
.search,.mobile-select{background:var(--gray);border-color:var(--gray);border-radius:8px}
.nav-item:hover{background:var(--tint-2)}
.nav-item[aria-current=true]{background:var(--blue);color:#fff;font-weight:500}
.nav-item[aria-current=true] .num{color:#fff}
.nav-item[aria-current=true] .dot{background:var(--yellow)}
.content{padding-top:24px}
.stat,.box,.priority{border-radius:12px;box-shadow:var(--shadow);border-color:#ececec}
.stat{background:var(--gray);border-color:var(--gray);padding:16px 18px}
.value{font-size:28px;letter-spacing:-.5px}
.priority:hover{background:var(--tint-2);border-color:var(--blue)}
.badge{border-radius:999px;font-weight:500;padding:4px 11px}
.block-label{font-weight:600;letter-spacing:.7px}
.table-scroll{border:1px solid var(--line);border-radius:8px}
th{background:var(--tint);color:var(--navy);font-weight:600}
td:first-child,th:first-child{padding-left:12px}td:last-child,th:last-child{padding-right:12px}
tbody tr:hover{background:var(--tint-2)}
.source{border-color:var(--blue);border-radius:8px}
.source:hover{background:var(--tint-2)}
button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid var(--yellow);outline-offset:3px}
.toast{background:var(--navy);color:#fff}
@media(max-width:900px){header{padding:16px 16px 0}.topline{padding:30px 25px 58px;min-height:210px}.tabs{padding:0}}
@media(max-width:650px){body{border-top-width:10px}header{padding:12px 8px 0}.topline{min-height:190px;padding:25px 18px 52px;border-radius:16px 16px 0 0}.topline .eyebrow{font-size:11px;letter-spacing:.6px}.topline .sub{font-size:13px}h1{font-size:30px}.tabs{margin:10px 10px 5px;gap:6px}.tab{font-size:12px;padding:7px 10px;min-height:42px}.sidebar{padding-top:16px}.content{padding-top:23px}}
@media print{body{border:0}header{padding:0}.topline{min-height:0;padding:0;border-radius:0;background:none;color:black}.topline::after{display:none}.topline .sub,.topline .eyebrow{color:black}h1{font-size:24pt}.table-scroll{overflow:visible}th{background:#eee}.stat{background:white}.btn{display:none}}


/* Saavutettavuus (WCAG 2.1 AA) */
.sr{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap;border:0}
.skip{position:absolute;left:12px;top:-60px;z-index:10;background:var(--navy);color:#fff;padding:10px 16px;border-radius:8px;font-weight:600;text-decoration:none}
.skip:focus{top:12px}
#panel:focus{outline:none}#panel:focus-visible{outline:3px solid var(--brand);outline-offset:6px}
h3.block-label{margin:0 0 12px}
h4{font-size:17px;line-height:1.4;margin:22px 0 8px;color:var(--navy);font-weight:600}
.table-scroll:focus-visible{outline:3px solid var(--brand);outline-offset:3px}
tbody th{font:inherit;color:inherit;letter-spacing:0;text-align:left}
.toast:empty{display:none}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;animation:none!important;scroll-behavior:auto!important}.priority:hover{transform:none}}
.home{display:inline-flex;gap:6px;align-items:center;color:#fff;font-size:14px;margin-bottom:12px;text-underline-offset:3px}.home:hover{text-decoration-thickness:2px}.home:focus-visible{outline-color:var(--yellow)}
.ai-note{border-left:5px solid var(--blue);padding:4px 0 4px 22px;margin:26px 0;max-width:820px}.ai-note h3{margin:0 0 8px}.ai-note p{margin:0 0 10px}.ai-note p:last-child{margin-bottom:0}
.answer{margin:2px 0 12px 29px;padding:6px 0 6px 13px;border-left:3px solid var(--line);font-size:14px;line-height:1.55}.answer .badge{margin-right:6px}.answer p{margin:4px 0}.answer .sources{margin-top:6px}.badge.ok{background:#e3f1e6;color:#1d5e2c}
.inv td.kind{text-align:left;white-space:nowrap;color:var(--soft)}.inv tfoot th,.inv tfoot td{font-weight:650;border-top:2px solid var(--line);border-bottom:0}.inv th[scope=row]{min-width:220px}.inv tfoot th{font-size:inherit;color:inherit;letter-spacing:0}.inv.with-kind thead th:nth-child(2){text-align:left}
@media print{.skip,.sr,.home{display:none!important}}
</style>
</head>
<body>
<a class="skip" href="#panel">Siirry sisältöön</a>
<header><div class="topline"><div><a class="home" id="guide-home" hidden><span aria-hidden="true">←</span> Kaikki kokousoppaat</a><div class="eyebrow" id="guide-city"></div><h1 id="guide-date"></h1><div class="sub" id="guide-meta"></div></div><button class="btn print" id="print">Tulosta näkymä</button></div>
<div class="tabs" role="tablist" aria-label="Kokousoppaan näkymät"><button class="tab" id="tab-overview" role="tab" aria-controls="panel" aria-selected="true" data-view="overview">Tilannekuva</button><button class="tab" id="tab-item" role="tab" aria-controls="panel" aria-selected="false" tabindex="-1" data-view="item">Asiat</button><button class="tab" id="tab-investments" role="tab" aria-controls="panel" aria-selected="false" tabindex="-1" data-view="investments" hidden>Investoinnit</button><button class="tab" id="tab-questions" role="tab" aria-controls="panel" aria-selected="false" tabindex="-1" data-view="questions">Nousseet kysymykset</button><button class="tab" id="tab-sources" role="tab" aria-controls="panel" aria-selected="false" tabindex="-1" data-view="sources">Tarkennukset ja lähteet</button></div></header>
<div class="layout"><aside class="sidebar" aria-label="Esityslistan asiat"><div class="eyebrow nav-caption">Esityslista</div><label for="search" class="sr">Hae asioista</label><input class="search" id="search" type="search" placeholder="Hae asiaa tai teemaa…" autocomplete="off"><select id="mobile-nav" class="mobile-select" aria-label="Valitse esityslistan asia"><option value="">Siirry asiaan…</option></select><nav id="agenda"></nav><div class="small" style="margin-top:20px">Punainen piste merkitsee asiaa, joka kaipaa tarkennusta.</div></aside><main class="content" id="sisalto"><div id="panel" role="tabpanel" aria-labelledby="tab-overview" tabindex="-1"></div></main></div><div class="toast" id="toast" aria-hidden="true"></div><div class="sr" id="live" role="status" aria-live="polite"></div>
<script type="application/json" id="guide-data">__GUIDE_DATA__</script>
<script>
(() => {
'use strict';
const {meeting, overview: summary, items, issues = [], investments: INV = null} = JSON.parse(document.getElementById('guide-data').textContent);
const checked = new Set();
let view = 'overview', selected = items[0].n, query = '';
const el=id=>document.getElementById(id);
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const list=arr=>'<ul>'+arr.map(x=>'<li>'+escape(x)+'</li>').join('')+'</ul>';
const link=(name,url,cls='source')=>`<a class="${cls}" href="${escape(url)}" target="_blank" rel="noopener noreferrer">${escape(name)} <span aria-hidden="true">↗</span><span class="sr"> (avautuu uuteen välilehteen)</span></a>`;
const row=(cells,head=false)=>'<tr>'+cells.map((c,k)=>{const t=head?'th scope="col"':k===0?'th scope="row"':'td';return `<${t}>${escape(c)}</${t.slice(0,2)}>`;}).join('')+'</tr>';
const table=(headers,rows,cls='')=>`<div class="table-scroll" tabindex="0" role="region" aria-label="Taulukko: ${escape(headers.join(', '))}"><table class="${cls}"><thead>${row(headers,true)}</thead><tbody>${rows.map(r=>row(r)).join('')}</tbody></table></div>`;
const matches = item => !query || JSON.stringify(item).toLocaleLowerCase('fi').includes(query);
const links = entries => (entries || []).map(([label, url]) => link(label, url)).join('');
el('guide-city').textContent = meeting.city + ' / valtuutetun kokousopas';
el('guide-date').textContent = meeting.date;
if (meeting.home) { el('guide-home').href = meeting.home; el('guide-home').hidden = false; }
el('guide-meta').textContent = [meeting.time, meeting.venue, 'Esityslista § ' +
  (items.length === 1 ? items[0].n : items[0].n + '–' + items.at(-1).n)].filter(Boolean).join(' · ');
document.title = meeting.city + ' · Valtuuston kokous ' + meeting.date;

function overview() {
  const stats = summary.stats || [];
  const highlights = summary.highlights || [];
  return `<div class="intro"><div class="eyebrow">Kokouksen tilannekuva</div><h2>${escape(summary.title)}</h2>
    <p class="lead">${escape(summary.lead)}</p><p class="sub">${escape(meeting.stage)} Avaa asia esityslistasta tai käytä hakua.</p></div>
    <section class="ai-note" aria-labelledby="ai-note-h"><h3 id="ai-note-h">Tekoälyn kokoama opas</h3><p>Opas on koottu tekoälyavustajan avulla kaupungin julkaisemasta esityslistasta ja liitteistä. Tekoäly voi lukea asiakirjan väärin, laskea virheellisesti tai jättää jotain olennaista huomaamatta. Tilannearviot ja kysymykset ovat tekijän näkemyksiä, eivät kaupungin kantoja.</p><p>Tarkista päätöksen kannalta tärkeät luvut ja tiedot alkuperäisistä asiakirjoista, joihin opas linkittää. Jos huomaat virheen tai puutteen, ilmoita siitä: oppaan saa korjata ja täydentää.</p>${meeting.contact ? `<p>Korjaukset ja huomiot: <a href="mailto:${escape(meeting.contact)}">${escape(meeting.contact)}</a>.</p>` : ''}</section>
    ${stats.length ? `<div class="stats">${stats.map(({label, value, note}) => `<div class="stat">
      <span class="small">${escape(label)}</span><span class="value">${escape(value)}</span>
      <p class="small">${escape(note)}</p></div>`).join('')}</div>` : ''}
    <div class="sources">${link('Koko esityslista', meeting.url)}${links(summary.sources)}</div>
    ${summary.comparisonNote ? `<div class="note"><strong>Vertailulukujen lukutapa</strong><br>${escape(summary.comparisonNote)}</div>` : ''}
    ${highlights.length ? `<section class="section"><h3>Nostot esityslistalta</h3><div class="priority-grid">
      ${highlights.map(({n, title, text}) => `<button class="priority" data-item="${n}">
        <span class="badge">§ ${n}</span><strong>${escape(title)} <span aria-hidden="true">→</span></strong><p>${escape(text)}</p></button>`).join('')}</div></section>` : ''}
    ${issues.length ? '<div class="note warn"><strong>Päätöksentekoa tukevat tarkennukset</strong><br><button class="jump" data-view="sources">Avaa tarkennuskohdat <span aria-hidden="true">→</span></button></div>' : ''}
    <section class="section"><h3>Tarkistettu aineisto</h3><p class="small">${escape(meeting.coverage)}</p></section>`;
}

function comparison(item) {
  const {note, headers, rows = [], sources} = item.comparison;
  return `<section class="block comparison"><h3 class="block-label">Nykytilanne → esitys</h3>
    <p class="small">${escape(note)}</p>
    ${rows.length ? table(headers || ['Mittari','Nyt / vertailupohja','Esitys / seuraava tilanne','Muutos'], rows) : ''}
    <div class="sources" style="margin-top:13px">${links(sources || [['Asian esittely', item.url]])}</div></section>`;
}

function extras(item) {
  const details = (item.details || []).map(section => `<details><summary>${escape(section.title)}</summary>
    ${section.text ? `<p>${escape(section.text)}</p>` : ''}
    ${section.rows?.length ? table(section.headers, section.rows) : ''}
    <div class="sources">${links(section.sources)}</div></details>`).join('');
  const attachments = (item.attachments || []).map(({title, status, summary, url}) => `<details>
    <summary>${escape(title)} · ${escape(status)}</summary><p>${escape(summary)}</p>
    ${url ? link('Avaa liite', url) : ''}</details>`).join('');
  return details + (attachments ? '<h4 class="section">Liitteet</h4>' + attachments : '');
}

function item() {
  const index = items.findIndex(entry => entry.n === selected);
  const current = items[index];
  const previous = items[index - 1], next = items[index + 1];
  return `<div class="item-head"><div><div class="tagrow"><span class="badge">§ ${current.n}</span>
    <span class="badge">${escape(current.tag)}</span>${current.critical ? '<span class="badge warn">Kaipaa tarkennusta</span>' : ''}
    </div><h2>${escape(current.title)}</h2></div></div>
    <div class="legend"><span><b>Todettu</b> = asiakirjan tieto</span><span><b>Arvio</b> = oma johtopäätös</span></div>
    ${comparison(current)}
    <section class="block"><h3 class="block-label">01 / Todettu ja päätösehdotus</h3>${list(current.facts)}${extras(current)}</section>
    <section class="block"><h3 class="block-label assess">02 / Oma tilannearvio</h3><p>${escape(current.assessment)}</p></section>
    ${current.risks.length ? `<section class="block"><h3 class="block-label risks">03 / Huomioitavaa ja avoimia kohtia</h3>${list(current.risks)}</section>` : ''}
    <section class="block"><h3 class="block-label">04 / Nousseet kysymykset</h3>
      ${current.questions.length ? questionsFor(current) : '<p class="small">Ei avoimia kysymyksiä.</p>'}</section>
    <section class="block"><h3>Alkuperäiset lähteet</h3><div class="sources">
      ${link('Asian asiakirja', current.url)}${links(current.sources)}</div></section>
    <div class="pager">
      <button class="btn" ${previous ? `data-item="${previous.n}"` : 'disabled'}><span aria-hidden="true">←</span> Edellinen</button>
      <span class="small">${index + 1} / ${items.length}</span>
      <button class="btn" ${next ? `data-item="${next.n}"` : 'disabled'}>Seuraava <span aria-hidden="true">→</span></button>
    </div>`;
}

function sources() {
  const attachments = items.flatMap(item => (item.attachments || []).map(attachment =>
    ({...attachment, title: '§ ' + item.n + ' · ' + attachment.title})));
  return `<div class="eyebrow">Aineiston tarkistus</div><h2>Aineiston tarkennuskohdat</h2>
    <p class="sub">${escape(meeting.coverage)}</p>
    ${issues.length ? `<div class="q-toolbar"><span class="small">${issues.length} tarkennuskohtaa</span>
    <button class="btn" id="copy-issues">Kopioi tarkistuslista</button></div>
    ${issues.map(({n, type, title, text}) => `<div class="issue"><span class="badge warn">${escape(type)}</span>
    <strong>§ ${n} · ${escape(title)}</strong><p>${escape(text)}</p><button class="jump" data-item="${n}">Avaa asia <span aria-hidden="true">→</span></button></div>`).join('')}`
    : '<p>Ei erillisiä tarkennuskohtia.</p>'}
    ${attachments.length ? `<section class="section"><h3>Liitteet ja niiden saatavuus</h3><ul>
      ${attachments.map(({title, url, status}) => `<li>${url ? link(title, url, '') : escape(title)}
      <span class="small"> · ${escape(status)}</span></li>`).join('')}</ul></section>` : ''}
    <section class="section"><h3>Muut lähteet</h3><div class="sources">
      ${link('Kokouksen esityslista', meeting.url)}${links(meeting.sources)}</div></section>`;
}

function render() {
  renderNav();
  document.querySelectorAll('.tab').forEach(tab => tab.setAttribute('aria-selected', tab.dataset.view === view));
  document.querySelectorAll('.tab').forEach(tab => tab.tabIndex = tab.dataset.view === view ? 0 : -1);
  setTitle();
  el('panel').setAttribute('aria-labelledby', 'tab-' + view);
  el('panel').innerHTML = ({overview, item, investments, questions, sources})[view]() +
    `<footer>Valtuutetun valmistautumisaineisto, koottu tekoälyn avulla: tarkista olennaiset tiedot alkuperäisistä asiakirjoista · Aineisto tarkistettu ${escape(meeting.reviewed)} · ${escape(meeting.stage)}${meeting.home ? ` <a href="${escape(meeting.home)}">Kaikki kokousoppaat</a>` : ''}</footer>`;
}

const invNum=v=>v===null||v===undefined?'<span aria-hidden="true">–</span><span class="sr">ei määrärahaa</span>':escape(new Intl.NumberFormat('fi-FI').format(v).replace('-','−'));
const invTable=(headers,rows,foot=[],label='')=>`<div class="table-scroll" tabindex="0" role="region" aria-label="${escape(label||headers.join(', '))}"><table class="financial inv${headers[1]==='Laji'?' with-kind':''}"><thead><tr>${headers.map(h=>`<th scope="col">${escape(h)}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr><th scope="row">${escape(r[0])}</th>${r.slice(1).map(c=>typeof c==='string'?`<td class="kind">${escape(c)}</td>`:`<td>${invNum(c)}</td>`).join('')}</tr>`).join('')}</tbody>${foot.length?`<tfoot>${foot.map(r=>`<tr><th scope="row">${escape(r[0])}</th>${r.slice(1).map(c=>typeof c==='string'?`<td></td>`:`<td>${invNum(c)}</td>`).join('')}</tr>`).join('')}</tfoot>`:''}</table></div>`;
const invLinks=list=>(list||[]).map(([n,u])=>link(n,u)).join('');
function investments(){const v=INV,ys=v.years,k27=v.focusYear?Math.max(0,ys.indexOf(v.focusYear)):Math.min(1,ys.length-1);
return `<div class="eyebrow">${escape(v.eyebrow||'Investoinnit')}</div><h2 style="margin-top:10px">${escape(v.title)}</h2><p class="lead">${escape(v.lead)}</p><p class="sub">${escape(v.note)}</p>
${(v.stats||[]).length?`<div class="stats">${v.stats.map(s=>`<div class="stat"><span class="small">${escape(s.label)}</span><span class="value">${escape(s.value)}</span><p class="small">${escape(s.note)}</p></div>`).join('')}</div>`:''}
<section class="section"><h3>${escape(v.summary.title)}</h3><p class="small">${escape(v.summary.note)}</p>${invTable(v.summary.headers,v.summary.rows,v.summary.totals,v.summary.title)}<div class="sources" style="margin-top:13px">${invLinks(v.summary.sources)}</div></section>
<section class="section"><h3>Hankkeet vuosittain</h3><p class="small">Investointimenot hankkeittain, 1 000 €. Avaa ryhmä nähdäksesi hankkeet. Suluissa ryhmän summa vuodelle ${escape(ys[k27])} ja koko kaudelle ${escape(ys[0])}–${escape(ys.at(-1))}.</p>
${v.groups.map(g=>{const sum=g.total.reduce((a,b)=>a+b,0);const foot=[['Yhteensä','',...g.total]];if(g.income)foot.push(['Investointitulot','',...g.income]);return `<details><summary>${escape(g.title)} <span class="small">(${escape(ys[k27])}: ${invNum(g.total[k27])} · ${escape(ys[0])}–${escape(ys.at(-1))}: ${invNum(sum)}${g.page?' · '+escape(g.page):''})</span></summary>${invTable(['Hanke','Laji',...ys],g.rows.map(r=>[r[0],r[1],...r.slice(2)]),foot,g.title)}</details>`;}).join('')}</section>
<section class="section"><h3>${escape(v.outside.title)}</h3><p class="small">${escape(v.outside.note)}</p>
${v.outside.tables.map(t=>`<h4>${escape(t.title)} · ${invNum(t.total)} t€</h4>${invTable(['Hanke','Arvio, 1 000 €'],t.rows,[['Yhteensä',t.total]],t.title)}`).join('')}
<p style="margin-top:14px"><strong>Investointitarve yhteensä ${invNum(v.outside.total)} tuhatta euroa.</strong></p></section>
${(v.risks||[]).length?`<section class="section"><h3>Huomioitavaa ja avoimia kohtia</h3>${list(v.risks)}</section>`:''}
${(v.questions||[]).length?`<section class="section"><h3>Nousseet kysymykset</h3>${list(v.questions)}</section>`:''}
<section class="section"><h3>Lähteet</h3><div class="sources">${invLinks(v.sources)}</div></section>`;}

if (INV) el('tab-investments').hidden = false;
const ansBadge=s=>`<span class="badge ${s==='Vastaus löytyi'?'ok':s==='Ei löytynyt'?'risk':'warn'}">${escape(s)}</span>`;
const answerHtml=a=>a?`<div class="answer"><strong class="small">Mitä löytyi:</strong> ${ansBadge(a.status)}<p>${escape(a.text)}</p>${(a.sources||[]).length?`<div class="sources">${a.sources.map(([n,u])=>link(n,u)).join('')}</div>`:''}</div>`:'';
function renderNav(){const shown=items.filter(matches);el('agenda').innerHTML=shown.length?shown.map(i=>`<button class="nav-item" data-item="${i.n}" aria-current="${view==='item'&&selected===i.n}"><span class="num">§ ${i.n}</span><span class="navtext">${escape(i.short)}</span>${i.critical?'<span class="dot" aria-hidden="true"></span><span class="sr">, kaipaa tarkennusta</span>':''}</button>`).join(''):'<p class="empty">Ei hakutuloksia.</p>';el('mobile-nav').innerHTML='<option value="">Siirry asiaan…</option>'+shown.map(i=>`<option value="${i.n}" ${view==='item'&&selected===i.n?'selected':''}>§ ${i.n} · ${escape(i.short)}</option>`).join('');}
function questionsFor(i){return '<ul class="q-list">'+i.questions.map((q,k)=>{let id=i.n+'-'+k;return `<li><label><input type="checkbox" data-question="${id}" ${checked.has(id)?'checked':''}><span>${escape(q)}</span></label>${answerHtml((i.answers||[])[k])}</li>`;}).join('')+'</ul>';}
function questions(){const found=items.filter(matches);const total=items.reduce((s,i)=>s+i.questions.length,0);return `<div class="eyebrow">Oma kokouslista</div><h2 style="margin-top:10px">Nousseet kysymykset</h2><p class="sub">Merkitse käsitelty kysymys rastilla. Merkinnät säilyvät tämän sivuistunnon aikana. Haku rajaa asioita myös tässä näkymässä.</p><div class="q-toolbar"><span class="small" id="qcount">${checked.size} / ${total} kysymystä käsitelty</span><button class="btn" id="reset-questions">Tyhjennä rastit</button></div>${found.map(i=>`<details ${i.critical?'open':''}><summary>§ ${i.n} · ${escape(i.short)} <span class="small">(${i.questions.length})</span></summary>${questionsFor(i)}<button class="jump" data-item="${i.n}">Lue asian tausta <span aria-hidden="true">→</span></button></details>`).join('')||'<p class="empty">Ei hakutuloksia.</p>'}`;}
function navigate(v,n){view=v;if(n)selected=Number(n);render();if(v==='item')history.replaceState(null,'','#asia-'+selected);else history.replaceState(null,'','#'+v);window.scrollTo({top:0,behavior:'instant'});el('panel').focus({preventScroll:true});}
document.addEventListener('click',async e=>{const itemButton=e.target.closest('[data-item]');if(itemButton){navigate('item',itemButton.dataset.item);return;}const viewButton=e.target.closest('[data-view]');if(viewButton){navigate(viewButton.dataset.view);return;}if(e.target.id==='print'){document.querySelectorAll('#panel details').forEach(d=>d.open=true);window.print();}if(e.target.id==='reset-questions'){checked.clear();render();}if(e.target.id==='copy-issues'){const text=issues.map(i=>`§ ${i.n} — ${i.title}\n${i.text}`).join('\n\n');try{await navigator.clipboard.writeText(text);notify('Tarkistuslista kopioitu.');}catch{const ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();const ok=document.execCommand('copy');ta.remove();notify(ok?'Tarkistuslista kopioitu.':'Kopiointi ei onnistunut tässä selaimessa.');}}});
document.addEventListener('change',e=>{if(e.target.dataset.question){const id=e.target.dataset.question;e.target.checked?checked.add(id):checked.delete(id);document.querySelectorAll(`[data-question="${id}"]`).forEach(x=>x.checked=e.target.checked);if(el('qcount'))el('qcount').textContent=checked.size+' / '+items.reduce((s,i)=>s+i.questions.length,0)+' kysymystä käsitelty';}});
el('search').addEventListener('input',e=>{query=e.target.value.trim().toLocaleLowerCase('fi');if(query&&view!=='questions')view='questions';render();announce(query?items.filter(matches).length+' asiaa vastaa hakua':'Haku tyhjennetty, kaikki asiat näkyvissä');});el('mobile-nav').addEventListener('change',e=>{if(e.target.value)navigate('item',e.target.value);});
document.querySelector('[role=tablist]').addEventListener('keydown',e=>{if(!['ArrowRight','ArrowLeft','Home','End'].includes(e.key))return;const tabs=[...document.querySelectorAll('.tab:not([hidden])')];let k=tabs.indexOf(document.activeElement);if(k<0)return;e.preventDefault();k=e.key==='Home'?0:e.key==='End'?tabs.length-1:(k+(e.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;tabs[k].focus();navigate(tabs[k].dataset.view);tabs[k].focus();});

const baseTitle=document.title;
function setTitle(){const cur=items.find(x=>x.n===selected);const names={overview:'Tilannekuva',investments:'Investoinnit',questions:'Nousseet kysymykset',sources:'Tarkennukset ja lähteet'};document.title=(view==='item'&&cur?'§ '+cur.n+' '+cur.title:names[view])+' · '+baseTitle;}
function announce(t){el('live').textContent='';setTimeout(()=>el('live').textContent=t,50);}
function notify(t){el('toast').textContent=t;announce(t);setTimeout(()=>el('toast').textContent='',2500);}

const hash = location.hash.slice(1);
const requestedItem = items.find(item => hash === 'asia-' + item.n);
if (requestedItem) {
  view = 'item';
  selected = requestedItem.n;
} else if (['overview', 'questions', 'sources'].includes(hash) || (INV && hash === 'investments')) {
  view = hash;
}
render();
})();
</script>
</body>
</html>
```
