#!/usr/bin/env python3
"""PARLIS-Kalender (.ics) → data/termine.json

Aufruf:  python3 tools/ics_import.py <datei.ics>
Die .ics-Datei im eigenen Browser aus PARLIS herunterladen (frankfurt.de blockt
Zugriffe aus Rechenzentren, siehe FEHLER-LOG) und unter docs/recherche/parlis/ ablegen.
Nur Standardbibliothek. Doppelte Einträge (PARLIS liefert jeden Termin zweimal) werden entfernt.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def einlesen(pfad):
    with open(pfad, encoding="utf-8", errors="replace") as f:
        t = f.read().replace("\r\n", "\n")
    t = re.sub(r"\n[ \t]", "", t)  # gefaltete Zeilen zusammenführen
    events = []
    for block in re.findall(r"BEGIN:VEVENT\n(.*?)END:VEVENT", t, re.S):
        d = {}
        for zeile in block.split("\n"):
            if ":" in zeile:
                k, v = zeile.split(":", 1)
                d[k.split(";")[0]] = v.strip()
        events.append(d)
    return events


def gremium(summary):
    """Liefert (typ, ortsbezirk|None, name) aus 'Sitzung des OBR 10 - geplanter Termin'."""
    name = re.sub(r"^Sitzung (des|der)\s+", "", summary.split(" - ")[0]).strip()
    m = re.fullmatch(r"OBR (\d{1,2})", name)
    if m:
        return "ortsbeirat", int(m.group(1)), "Ortsbeirat " + m.group(1)
    if name == "Stadtverordnetenversammlung":
        return "stvv", None, name
    if name == "KAV":
        return "kav", None, "KAV (Kommunale Ausländerinnen- und Ausländervertretung)"
    return "ausschuss", None, re.sub(r"usschusses\b", "usschuss", name)  # Genitiv → Nominativ


def main(pfad):
    events = einlesen(pfad)
    termine, gesehen, stand = [], set(), ""
    for e in events:
        ds = e.get("DTSTART", "")
        if not re.match(r"\d{8}T\d{4}", ds):
            continue
        typ, obr, name = gremium(e.get("SUMMARY", ""))
        datum = ds[0:4] + "-" + ds[4:6] + "-" + ds[6:8]
        zeit = ds[9:11] + ":" + ds[11:13]
        key = (datum, zeit, name)
        if key in gesehen:
            continue
        gesehen.add(key)
        stand = max(stand, e.get("DTSTAMP", "")[:8])
        termine.append({"datum": datum, "zeit": zeit, "typ": typ, "ortsbezirk": obr,
                        "gremium": name, "status": "geplant" if "geplant" in e.get("SUMMARY", "") else "",
                        "uid": e.get("UID", "")})
    termine.sort(key=lambda x: (x["datum"], x["zeit"], x["gremium"]))
    out = {"quelle": "PARLIS-Kalender der Stadt Frankfurt am Main (Export .ics, alle Termine)",
           "datei": os.path.relpath(os.path.abspath(pfad), ROOT).replace(os.sep, "/"),
           "stand": stand[0:4] + "-" + stand[4:6] + "-" + stand[6:8] if stand else "",
           "hinweis": "Geplante Termine ohne Ort und Tagesordnung – beides vor Veröffentlichung in PARLIS prüfen.",
           "termine": termine}
    ziel = os.path.join(ROOT, "data", "termine.json")
    with open(ziel, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(str(len(termine)) + " Termine (" + str(len(events)) + " Einträge in der Datei) → data/termine.json, Stand " + out["stand"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Aufruf: python3 tools/ics_import.py <datei.ics>")
    main(sys.argv[1])
