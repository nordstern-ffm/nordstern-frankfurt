#!/usr/bin/env python3
"""Prüft das Repo. Exit-Code 1 = Fehler (nicht pushen).

python3 tools/check.py          Vorschau-Prüfung
python3 tools/check.py --launch zusätzlich Launch-Bedingungen (Impressum, Domain)
"""
import json, os, posixpath, re, sys
sys.dont_write_bytecode = True  # kein tools/__pycache__ im Repo
import beitraege

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fehler, warn = [], []
site = json.load(open(os.path.join(ROOT, "data/site.json"), encoding="utf-8"))
links = json.load(open(os.path.join(ROOT, "data/links.json"), encoding="utf-8"))["links"]
pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
if os.path.isdir(os.path.join(ROOT, "frankfurt")):
    pages += sorted("frankfurt/" + f for f in os.listdir(os.path.join(ROOT, "frankfurt")) if f.endswith(".html"))

for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    # 1. Keine Fremd-Ressourcen (Datenschutz-Zusage)
    for m in re.findall(r'(?:src|href)="(https?://[^"]+)"', t):
        if 'rel="stylesheet"' in t and m in t.split('rel="stylesheet"')[0][-200:]:
            fehler.append(f"{p}: externes Stylesheet {m}")
    if re.search(r"<script[^>]+src=", t) or "fonts.googleapis" in t:
        fehler.append(f"{p}: externes Skript/Google Fonts")
    # 2. Interne Links existieren
    for m in re.findall(r'href="((?:\.\./)?(?:[a-z0-9\-]+/)?[a-z0-9\-]+\.html)', t):
        ziel = posixpath.normpath(posixpath.join(posixpath.dirname(p), m))
        if ziel not in pages:
            fehler.append(f"{p}: toter Link {m}")
    # 3. Externe Links nur, wenn in links.json bestätigt oder ausdrücklich erlaubt
    ok = {l["url"] for l in links.values() if l.get("bestaetigt")} | {site["verein"]["website"]}
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

# 5. Blog-Beiträge (E10): Frontmatter, Status, Link-Platzhalter
STATUS = beitraege.STATUS
try:
    posts = beitraege.laden(ROOT)
except ValueError as e:
    posts = []
    fehler.append("data/beitraege: " + str(e))
slugs = {}
for b in posts:
    d, m = b["datei"], b["meta"]
    for k in ("titel", "slug", "datum", "status", "ortsbezirk"):
        if not m.get(k):
            fehler.append(f"{d}: Frontmatter-Feld {k} fehlt")
    if m.get("status") and m["status"] not in STATUS:
        fehler.append(f"{d}: status {m['status']!r} nicht in {STATUS}")
    ob = m.get("ortsbezirk")
    if ob and not (re.fullmatch(r"[0-9]{1,2}", ob) and 1 <= int(ob) <= 16):
        fehler.append(f"{d}: ortsbezirk {ob!r} muss eine Zahl von 1 bis 16 sein")
    if m.get("datum") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", m["datum"]):
        fehler.append(f"{d}: datum nicht im Format JJJJ-MM-TT")
    if m.get("slug"):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", m["slug"]) or m["slug"] == "index":
            fehler.append(f"{d}: slug {m['slug']!r} ungültig (nur a-z, 0-9, Bindestrich; nicht index)")
        if m["slug"] in slugs:
            fehler.append(f"{d}: slug doppelt (auch in {slugs[m['slug']]})")
        slugs[m["slug"]] = d
    keys = beitraege.link_keys(b["body"]) + (m["links"] if isinstance(m.get("links"), list) else [])
    for k in sorted(set(keys)):
        if k not in links:
            fehler.append(f"{d}: unbekannter Link-Schlüssel [[link:{k}]]")
        elif not links[k].get("bestaetigt"):
            warn.append(f"{d}: Link {k} ohne bestaetigt (erscheint nur als Text)")
    if re.search(r"\]\(\s*https?://|<a\s|<script", b["body"], re.I):
        fehler.append(f"{d}: rohe URL/HTML im Text – Links nur als [[link:schluessel]]")

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
