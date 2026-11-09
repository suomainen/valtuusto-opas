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
