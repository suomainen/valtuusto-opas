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
