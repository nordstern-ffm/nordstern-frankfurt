#!/usr/bin/env python3
"""Prüft das Repo. Exit-Code 1 = Fehler (nicht pushen).

python3 tools/check.py          Vorschau-Prüfung
python3 tools/check.py --launch zusätzlich Launch-Bedingungen (Impressum, Domain)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fehler, warn = [], []
site = json.load(open(os.path.join(ROOT, "data/site.json"), encoding="utf-8"))
links = json.load(open(os.path.join(ROOT, "data/links.json"), encoding="utf-8"))["links"]
bilder = json.load(open(os.path.join(ROOT, "data/bilder.json"), encoding="utf-8"))["bilder"]
pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))

for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    # 1. Keine Fremd-Ressourcen (Datenschutz-Zusage)
    for m in re.findall(r'(?:src|href)="(https?://[^"]+)"', t):
        if 'rel="stylesheet"' in t and m in t.split('rel="stylesheet"')[0][-200:]:
            fehler.append(f"{p}: externes Stylesheet {m}")
    if re.search(r"<script[^>]+src=", t) or "fonts.googleapis" in t:
        fehler.append(f"{p}: externes Skript/Google Fonts")
    # 2. Interne Links existieren
    for m in re.findall(r'href="([a-z0-9\-]+\.html)', t):
        if m not in pages:
            fehler.append(f"{p}: toter Link {m}")
    # 3. Externe Links nur, wenn in links.json bestätigt oder ausdrücklich erlaubt
    ok = {l["url"] for l in links.values() if l.get("bestaetigt")} | {site["verein"]["website"]}
    ok |= {b[k] for b in bilder if b.get("geprueft") for k in ("quelle_url", "lizenz_url") if b.get(k)}
    for m in re.findall(r'href="(https?://[^"]+)"', t):
        zahlung = m.startswith("https://buy.stripe.com/") or re.match(r"https://[a-z0-9-]+\.gumroad\.com/", m)
        if m not in ok and "openpetition" not in m and not zahlung:
            warn.append(f"{p}: ungeprüfter externer Link {m}")
    # 3b. Zahlungslinks: nur gehostete Seiten (Stripe Payment Link / Gumroad), nie eigene Checkout-Skripte
    # 4. Keine Lorem/Platzhalter
    # Fehler 2026-11-15: re.I + "TODO" traf die CSS-Klasse class="todo" → nur Großschreibung prüfen
    if re.search(r"lorem ipsum|\[NAME\]|\[ADRESSE\]|\bTODO\b", t):
        fehler.append(f"{p}: Platzhaltertext")
    if 'name="robots" content="noindex' not in t and not (site["launch"] and site["domain_bestaetigt"]):
        fehler.append(f"{p}: Vorschau ohne noindex")

# 5. Bildrechte – Null-Fehler-Regel (docs/UX-KONZEPT.md Abschnitt 4)
BILD_PFLICHT = ("datei", "titel", "autor", "quelle_url", "lizenz", "lizenz_url", "geaendert", "geprueft", "alt")
BILD_ENDUNGEN = (".webp", ".avif", ".jpg", ".jpeg", ".png", ".gif", ".svg")
komplett = set()
for i, b in enumerate(bilder):
    name = b.get("datei") or f"Eintrag {i + 1}"
    fehlt = [k for k in BILD_PFLICHT if not str(b.get(k, "")).strip()]
    if fehlt:
        fehler.append(f"bilder.json: {name} – Pflichtfeld fehlt: {', '.join(fehlt)}")
    if b.get("geprueft") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", b["geprueft"]):
        fehler.append(f"bilder.json: {name} – geprueft muss JJJJ-MM-TT sein")
    for k in ("quelle_url", "lizenz_url"):
        if b.get(k) and not b[k].startswith("https://"):
            fehler.append(f"bilder.json: {name} – {k} muss mit https:// beginnen")
    if b.get("datei") and not os.path.isfile(os.path.join(ROOT, b["datei"])):
        fehler.append(f"bilder.json: {name} – Datei existiert nicht")
    if not fehlt:
        komplett.add(b["datei"])
img_dir = os.path.join(ROOT, "img")
if os.path.isdir(img_dir):
    for wurzel, _, dateien in os.walk(img_dir):
        for d in dateien:
            rel = os.path.relpath(os.path.join(wurzel, d), ROOT).replace(os.sep, "/")
            if d.lower().endswith(BILD_ENDUNGEN) and rel not in komplett:
                fehler.append(f"{rel}: Bilddatei ohne vollständigen Eintrag in data/bilder.json")
for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    for tag in re.findall(r"<img\b[^>]*>", t):
        src = re.search(r'\bsrc="([^"]*)"', tag)
        src = src.group(1) if src else ""
        if src.startswith(("http://", "https://", "//")):
            fehler.append(f"{p}: externes Bild {src} (Fremdabruf)")
        elif src not in komplett:
            fehler.append(f"{p}: <img src=\"{src}\"> ohne vollständigen Eintrag in data/bilder.json")
        if not re.search(r'\balt="[^"]+"', tag):
            fehler.append(f"{p}: <img src=\"{src}\"> ohne Alt-Text")

if "--launch" in sys.argv:
    b = site["betreiber"]
    for k in ("anschrift", "email", "telefon"):
        if not b[k]:
            fehler.append(f"Launch: betreiber.{k} in data/site.json fehlt (Impressumspflicht)")
    if not site["domain_bestaetigt"]:
        fehler.append("Launch: Domain noch nicht gekauft/bestätigt (domain_bestaetigt=false)")
    if not links["fw_programm"]["bestaetigt"]:
        warn.append("Launch: Link zum FW-Programm noch nicht im Browser bestätigt")

for w in warn:
    print("WARNUNG", w)
for f in fehler:
    print("FEHLER ", f)
print(f"{len(pages)} Seiten geprüft · {len(fehler)} Fehler · {len(warn)} Warnungen")
sys.exit(1 if fehler else 0)
