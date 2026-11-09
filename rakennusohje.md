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
- Jos lähtöluku puuttuu, kerro mistä sitä etsittiin ja mitä tästä seuraa. Älä päättele puuttuvaa kokonaismäärää ilmoitetusta vähennyksestä. Jos pykälässä ei ole vertailtavaa päätöslukua, riittää lyhyt perustelu. Avaa suurten talousasioiden erittelyt tarvittaessa taitettaviin osioihin.
- Kirjoita suomeksi neutraalisti ja konkreettisesti. Käytä esimerkiksi otsikoita **04 / Nousseet kysymykset**, **Huomioitavaa ja avoimia kohtia**, **Tarkennukset ja lähteet**. Muotoile kysymykset niin, että niihin voi vastata luvulla, asiakirjalla, vastuulla, päätösvaiheella tai määräajalla.

## Kokous-JSONin kentät

- `meeting.time` ja `meeting.venue` ovat valinnaisia. `meeting.sources` voi sisältää koko oppaan yhteisiä lähteitä ja säädöslinkkejä.
- `overview.stats`, `overview.highlights`, `overview.sources` ja `overview.comparisonNote` ovat valinnaisia. Nostoissa ja tarkennuksissa `n` viittaa olemassa olevaan pykälään.
- Jokaisella pykälällä on `facts`, `risks` ja `questions` tekstilistoina. Tyhjä lista sopii, jos riskiä tai kysymystä ei noussut. `critical` on valinnainen huomion merkki. `sources` sisältää pykälän muut lähteet.
- Jokaisella pykälällä on `comparison.note`. Jos vertailtavaa lukua ei ole, selitä syy siinä. `rows` voi silloin puuttua. Oletuksena jokainen rivi sisältää neljä solua. `headers` voi korvata oletusotsikot esimerkiksi toteumavertailussa.
- `attachments` listaa liitteet ja alaliitteet. Käytä kuvaavaa tilaa, esimerkiksi **Luettu**, **Osin peitetty**, **Linkki puuttuu** tai **Linkitetty, jäi lukematta**. Jätä `url` pois vain, kun osoitetta ei ole. Kerro olennainen liitteen sisältö tai saatavuuden syy kentässä `summary`.
- `details` on valinnainen lista taitettavia erittelyjä. Kukin osio sisältää `title` ja tarvittaessa `text`, `sources` tai taulukon `headers` ja `rows`.
- Kaikki `sources`-kentät ovat `[nimi, URL]`-pareja. Käytä suoria https-osoitteita, kun sellaisia on. Lisää sivunumero linkin nimeen, vaikka PDF:n sivuankkuri ei toimisi kaikissa selaimissa.

## Tarkista ennen jakamista

- Vertaa pykäläluetteloa ja liitteitä viralliseen esityslistaan. Tarkista, että jokaisen luvun vuosi, vertailupohja ja lähde näkyvät ja että puuttuvat tiedot on merkitty.
- Avaa HTML selaimessa. Tarkista tilannekuva, pykälänäkymä, nousseet kysymykset ja tarkennukset. Kokeile hakua, pykälien välillä liikkumista, lähdelinkkejä ja puhelinnäkymää.
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

</style>
</head>
<body>
<header><div class="topline"><div><div class="eyebrow" id="guide-city"></div><h1 id="guide-date"></h1><div class="sub" id="guide-meta"></div></div><button class="btn print" id="print">Tulosta näkymä</button></div>
<div class="tabs" role="tablist" aria-label="Kokousoppaan näkymät"><button class="tab" id="tab-overview" role="tab" aria-controls="panel" aria-selected="true" data-view="overview">Tilannekuva</button><button class="tab" id="tab-item" role="tab" aria-controls="panel" aria-selected="false" data-view="item">Asiat</button><button class="tab" id="tab-questions" role="tab" aria-controls="panel" aria-selected="false" data-view="questions">Nousseet kysymykset</button><button class="tab" id="tab-sources" role="tab" aria-controls="panel" aria-selected="false" data-view="sources">Tarkennukset ja lähteet</button></div></header>
<div class="layout"><aside class="sidebar" aria-label="Esityslistan asiat"><div class="eyebrow nav-caption">Esityslista</div><label for="search" class="sr-only" style="position:absolute;clip-path:inset(50%);width:1px;height:1px;overflow:hidden">Hae asioista</label><input class="search" id="search" type="search" placeholder="Hae asiaa tai teemaa…" autocomplete="off"><select id="mobile-nav" class="mobile-select" aria-label="Valitse esityslistan asia"><option value="">Siirry asiaan…</option></select><nav id="agenda"></nav><div class="small" style="margin-top:20px">Punainen piste merkitsee asiaa, joka kaipaa tarkennusta.</div></aside><main class="content" id="panel" role="tabpanel" aria-labelledby="tab-overview" tabindex="-1"></main></div><div class="toast" id="toast" role="status" hidden></div>
<script type="application/json" id="guide-data">__GUIDE_DATA__</script>
<script>
(() => {
'use strict';
const {meeting, overview: summary, items, issues = []} = JSON.parse(document.getElementById('guide-data').textContent);
const checked = new Set();
let view = 'overview', selected = items[0].n, query = '';
const el=id=>document.getElementById(id);
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const list=arr=>'<ul>'+arr.map(x=>'<li>'+escape(x)+'</li>').join('')+'</ul>';
const link=(name,url,cls='source')=>`<a class="${cls}" href="${escape(url)}" target="_blank" rel="noopener noreferrer">${escape(name)} ↗</a>`;
const row=(cells,head=false)=>'<tr>'+cells.map(c=>`<${head?'th scope="col"':'td'}>${escape(c)}</${head?'th':'td'}>`).join('')+'</tr>';
const table=(headers,rows,cls='')=>`<div class="table-scroll"><table class="${cls}"><thead>${row(headers,true)}</thead><tbody>${rows.map(r=>row(r)).join('')}</tbody></table></div>`;
const matches = item => !query || JSON.stringify(item).toLocaleLowerCase('fi').includes(query);
const links = entries => (entries || []).map(([label, url]) => link(label, url)).join('');
el('guide-city').textContent = meeting.city + ' / valtuutetun kokousopas';
el('guide-date').textContent = meeting.date;
el('guide-meta').textContent = [meeting.time, meeting.venue, 'Esityslista § ' +
  (items.length === 1 ? items[0].n : items[0].n + '–' + items.at(-1).n)].filter(Boolean).join(' · ');
document.title = meeting.city + ' · Valtuuston kokous ' + meeting.date;

function overview() {
  const stats = summary.stats || [];
  const highlights = summary.highlights || [];
  return `<div class="intro"><div class="eyebrow">Kokouksen tilannekuva</div><h2>${escape(summary.title)}</h2>
    <p class="lead">${escape(summary.lead)}</p><p class="sub">${escape(meeting.stage)} Avaa asia esityslistasta tai käytä hakua.</p></div>
    ${stats.length ? `<div class="stats">${stats.map(({label, value, note}) => `<div class="stat">
      <span class="small">${escape(label)}</span><span class="value">${escape(value)}</span>
      <p class="small">${escape(note)}</p></div>`).join('')}</div>` : ''}
    <div class="sources">${link('Koko esityslista', meeting.url)}${links(summary.sources)}</div>
    ${summary.comparisonNote ? `<div class="note"><strong>Vertailulukujen lukutapa</strong><br>${escape(summary.comparisonNote)}</div>` : ''}
    ${highlights.length ? `<section class="section"><h3>Nostot esityslistalta</h3><div class="priority-grid">
      ${highlights.map(({n, title, text}) => `<button class="priority" data-item="${n}">
        <span class="badge">§ ${n}</span><strong>${escape(title)} →</strong><p>${escape(text)}</p></button>`).join('')}</div></section>` : ''}
    ${issues.length ? '<div class="note warn"><strong>Päätöksentekoa tukevat tarkennukset</strong><br><button class="jump" data-view="sources">Avaa tarkennuskohdat →</button></div>' : ''}
    <section class="section"><h3>Tarkistettu aineisto</h3><p class="small">${escape(meeting.coverage)}</p></section>`;
}

function comparison(item) {
  const {note, headers, rows = [], sources} = item.comparison;
  return `<section class="block comparison"><div class="block-label">Nykytilanne → esitys</div>
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
  return details + (attachments ? '<h3 class="section">Liitteet</h3>' + attachments : '');
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
    <section class="block"><div class="block-label">01 / Todettu ja päätösehdotus</div>${list(current.facts)}${extras(current)}</section>
    <section class="block"><div class="block-label assess">02 / Oma tilannearvio</div><p>${escape(current.assessment)}</p></section>
    ${current.risks.length ? `<section class="block"><div class="block-label risks">03 / Huomioitavaa ja avoimia kohtia</div>${list(current.risks)}</section>` : ''}
    <section class="block"><div class="block-label">04 / Nousseet kysymykset</div>
      ${current.questions.length ? questionsFor(current) : '<p class="small">Ei avoimia kysymyksiä.</p>'}</section>
    <section class="block"><h3>Alkuperäiset lähteet</h3><div class="sources">
      ${link('Asian asiakirja', current.url)}${links(current.sources)}</div></section>
    <div class="pager">
      <button class="btn" ${previous ? `data-item="${previous.n}"` : 'disabled'}>← Edellinen</button>
      <span class="small">${index + 1} / ${items.length}</span>
      <button class="btn" ${next ? `data-item="${next.n}"` : 'disabled'}>Seuraava →</button>
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
    <strong>§ ${n} · ${escape(title)}</strong><p>${escape(text)}</p><button class="jump" data-item="${n}">Avaa asia →</button></div>`).join('')}`
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
  el('panel').setAttribute('aria-labelledby', 'tab-' + view);
  el('panel').innerHTML = ({overview, item, questions, sources})[view]() +
    `<footer>Valtuutetun valmistautumisaineisto · Aineisto tarkistettu ${escape(meeting.reviewed)} · ${escape(meeting.stage)}</footer>`;
}

function renderNav(){const shown=items.filter(matches);el('agenda').innerHTML=shown.length?shown.map(i=>`<button class="nav-item" data-item="${i.n}" aria-current="${view==='item'&&selected===i.n}"><span class="num">§ ${i.n}</span><span class="navtext">${escape(i.short)}</span>${i.critical?'<span class="dot" aria-label="Kaipaa tarkennusta"></span>':''}</button>`).join(''):'<p class="empty">Ei hakutuloksia.</p>';el('mobile-nav').innerHTML='<option value="">Siirry asiaan…</option>'+shown.map(i=>`<option value="${i.n}" ${view==='item'&&selected===i.n?'selected':''}>§ ${i.n} · ${escape(i.short)}</option>`).join('');}
function questionsFor(i){return '<ul class="q-list">'+i.questions.map((q,k)=>{let id=i.n+'-'+k;return `<li><label><input type="checkbox" data-question="${id}" ${checked.has(id)?'checked':''}><span>${escape(q)}</span></label></li>`;}).join('')+'</ul>';}
function questions(){const found=items.filter(matches);const total=items.reduce((s,i)=>s+i.questions.length,0);return `<div class="eyebrow">Oma kokouslista</div><h2 style="margin-top:10px">Nousseet kysymykset</h2><p class="sub">Merkitse käsitelty kysymys rastilla. Merkinnät säilyvät tämän sivuistunnon aikana. Haku rajaa asioita myös tässä näkymässä.</p><div class="q-toolbar"><span class="small" id="qcount">${checked.size} / ${total} kysymystä käsitelty</span><button class="btn" id="reset-questions">Tyhjennä rastit</button></div>${found.map(i=>`<details ${i.critical?'open':''}><summary>§ ${i.n} · ${escape(i.short)} <span class="small">(${i.questions.length})</span></summary>${questionsFor(i)}<button class="jump" data-item="${i.n}">Lue asian tausta →</button></details>`).join('')||'<p class="empty">Ei hakutuloksia.</p>'}`;}
function navigate(v,n){view=v;if(n)selected=Number(n);render();if(v==='item')history.replaceState(null,'','#asia-'+selected);else history.replaceState(null,'','#'+v);window.scrollTo({top:0,behavior:'instant'});el('panel').focus({preventScroll:true});}
document.addEventListener('click',async e=>{const itemButton=e.target.closest('[data-item]');if(itemButton){navigate('item',itemButton.dataset.item);return;}const viewButton=e.target.closest('[data-view]');if(viewButton){navigate(viewButton.dataset.view);return;}if(e.target.id==='print'){document.querySelectorAll('#panel details').forEach(d=>d.open=true);window.print();}if(e.target.id==='reset-questions'){checked.clear();render();}if(e.target.id==='copy-issues'){const text=issues.map(i=>`§ ${i.n} — ${i.title}\n${i.text}`).join('\n\n');try{await navigator.clipboard.writeText(text);notify('Tarkistuslista kopioitu.');}catch{const ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();const ok=document.execCommand('copy');ta.remove();notify(ok?'Tarkistuslista kopioitu.':'Kopiointi ei onnistunut tässä selaimessa.');}}});
document.addEventListener('change',e=>{if(e.target.dataset.question){const id=e.target.dataset.question;e.target.checked?checked.add(id):checked.delete(id);document.querySelectorAll(`[data-question="${id}"]`).forEach(x=>x.checked=e.target.checked);if(el('qcount'))el('qcount').textContent=checked.size+' / '+items.reduce((s,i)=>s+i.questions.length,0)+' kysymystä käsitelty';}});
el('search').addEventListener('input',e=>{query=e.target.value.trim().toLocaleLowerCase('fi');if(query&&view!=='questions')view='questions';render();});el('mobile-nav').addEventListener('change',e=>{if(e.target.value)navigate('item',e.target.value);});
document.querySelector('[role=tablist]').addEventListener('keydown',e=>{if(!['ArrowRight','ArrowLeft','Home','End'].includes(e.key))return;const tabs=[...document.querySelectorAll('.tab')];let k=tabs.indexOf(document.activeElement);if(k<0)return;e.preventDefault();k=e.key==='Home'?0:e.key==='End'?tabs.length-1:(k+(e.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;tabs[k].focus();navigate(tabs[k].dataset.view);tabs[k].focus();});
function notify(t){el('toast').textContent=t;el('toast').hidden=false;setTimeout(()=>el('toast').hidden=true,2500);}

const hash = location.hash.slice(1);
const requestedItem = items.find(item => hash === 'asia-' + item.n);
if (requestedItem) {
  view = 'item';
  selected = requestedItem.n;
} else if (['overview', 'questions', 'sources'].includes(hash)) {
  view = hash;
}
render();
})();
</script>
</body>
</html>
```
