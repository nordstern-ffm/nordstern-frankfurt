#!/usr/bin/env python3
"""Prüft das Repo. Exit-Code 1 = Fehler (nicht pushen).

python3 tools/check.py          Vorschau-Prüfung
python3 tools/check.py --launch zusätzlich Launch-Bedingungen (Impressum, Domain)
"""
import datetime, json, os, re, sys
sys.dont_write_bytecode = True  # kein tools/__pycache__ im Repo
import beitraege

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fehler, warn = [], []
site = json.load(open(os.path.join(ROOT, "data/site.json"), encoding="utf-8"))
links = json.load(open(os.path.join(ROOT, "data/links.json"), encoding="utf-8"))["links"]
bilder = json.load(open(os.path.join(ROOT, "data/bilder.json"), encoding="utf-8"))["bilder"]
# Erzeugte Seiten = alle HTML außer docs/ (Blog-Beiträge liegen in Unterordnern wie ratgeber/<slug>/)
pages = []
for _w, _o, _d in os.walk(ROOT):
    _o[:] = [o for o in _o if o not in (".git", "docs")]
    pages += [os.path.relpath(os.path.join(_w, f), ROOT).replace(os.sep, "/") for f in _d if f.endswith(".html")]
pages.sort()


def aufloesen(seite, url):
    """Relativen Link einer Seite in einen Pfad ab Hauptordner umrechnen (ohne #, Ordner → index.html)."""
    pfad = url.split("#")[0]
    if not pfad:
        return None
    ziel = os.path.normpath(os.path.join(os.path.dirname(seite), pfad)).replace(os.sep, "/")
    return ziel + "/index.html" if pfad.endswith("/") else ziel


for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    # 1. Keine Fremd-Ressourcen (Datenschutz-Zusage)
    for m in re.findall(r'(?:src|href)="(https?://[^"]+)"', t):
        if 'rel="stylesheet"' in t and m in t.split('rel="stylesheet"')[0][-200:]:
            fehler.append(f"{p}: externes Stylesheet {m}")
    if re.search(r"<script[^>]+src=", t) or "fonts.googleapis" in t:
        fehler.append(f"{p}: externes Skript/Google Fonts")
    # 1b. JavaScript nur als Ausnahme E13: inline, nur in handgepflegten Lernseiten lernen/*.html
    if re.search(r"<script", t, re.I) and not (p.startswith("lernen/") and p != "lernen/index.html"):
        fehler.append(f"{p}: JavaScript außerhalb der Ausnahme E13 (nur lernen/, nicht index)")
    # 2. Interne Links und Dateien existieren (auch aus Unterordnern, ../ wird aufgelöst)
    for m in re.findall(r'(?:href|src)="(?!https?:|mailto:|data:|#)([^"]+)"', t):
        z = aufloesen(p, m)
        if z and (z.startswith("..") or not os.path.isfile(os.path.join(ROOT, z))):
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
        elif aufloesen(p, src) not in komplett:
            fehler.append(f"{p}: <img src=\"{src}\"> ohne vollständigen Eintrag in data/bilder.json")
        if not re.search(r'\balt="[^"]+"', tag):
            fehler.append(f"{p}: <img src=\"{src}\"> ohne Alt-Text")

# 6. Icons (assets/icons.svg, Lucide ISC): Verweis existiert, Deko versteckt, jede Karte/Navi mit Icon
sprite = os.path.join(ROOT, "assets/icons.svg")
symbole = set(re.findall(r'<symbol id="([a-z0-9-]+)"', open(sprite, encoding="utf-8").read())) if os.path.isfile(sprite) else set()
if not os.path.isfile(os.path.join(ROOT, "assets/LICENSE-icons.txt")):
    fehler.append("assets/LICENSE-icons.txt fehlt (Lizenzpflicht für Icons)")
for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    for m in re.findall(r'<use href="(?:\.\./)*assets/icons\.svg#([^"]+)"', t):
        if m not in symbole:
            fehler.append(f"{p}: Icon „{m}“ fehlt in assets/icons.svg")
    for tag in re.findall(r"<svg\b[^>]*>", t):
        if 'aria-hidden="true"' not in tag and not ('role="img"' in tag and re.search(r'aria-label="[^"]+"', tag)):
            fehler.append(f"{p}: <svg> ohne aria-hidden bzw. role=img + aria-label")
    for k in re.findall(r'<article class="card.*?</h3>', t, re.S):
        if 'class="card-icon"' not in k:
            fehler.append(f"{p}: Karte ohne Icon: {re.sub('<[^>]+>', '', k)[:40]}")
    for a in re.findall(r"<nav\b.*?</nav>", t, re.S):
        if a.count("<li>") != a.count('class="icon"'):
            fehler.append(f"{p}: Menüpunkt ohne Icon")

# 7. Kennzahlen (data/zahlen.json): Primärquelle über bestätigten Link, Fundstelle, Stand, Prüfdatum
zahlen = json.load(open(os.path.join(ROOT, "data/zahlen.json"), encoding="utf-8"))["zahlen"]
for k, z in zahlen.items():
    fehlt = [f for f in ("wert", "text", "quelle", "link", "fundstelle", "stand", "geprueft") if not str(z.get(f, "")).strip()]
    if fehlt:
        fehler.append(f"zahlen.json: {k} – Pflichtfeld fehlt: {', '.join(fehlt)}")
    if z.get("link") and not links.get(z["link"], {}).get("bestaetigt"):
        fehler.append(f"zahlen.json: {k} – Quelle „{z['link']}“ fehlt in links.json oder ist unbestätigt")
    if z.get("geprueft") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", z["geprueft"]):
        fehler.append(f"zahlen.json: {k} – geprueft muss JJJJ-MM-TT sein")
for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    for s in re.findall(r'<li class="stat">.*?</li>', t, re.S):
        if "Quelle:" not in s or "Stand:" not in s:
            fehler.append(f"{p}: Kennzahl ohne Quelle/Stand: {re.sub('<[^>]+>', ' ', s)[:40]}")

# 8. Sicherheit für ALLE veröffentlichten Dateien (GitHub Pages + .nojekyll veröffentlicht das ganze Repo,
#    auch docs/mockups/*.html): keine Skripte (E16-Freigabe kommt mit P3/W4), keine Fremdabrufe, keine Formulare
alle_html, alle_css = [], []
for wurzel, ordner, dateien in os.walk(ROOT):
    ordner[:] = [o for o in ordner if o != ".git"]
    for d in dateien:
        rel = os.path.relpath(os.path.join(wurzel, d), ROOT).replace(os.sep, "/")
        if d.endswith(".html"):
            alle_html.append(rel)
        elif d.endswith(".css"):
            alle_css.append(rel)
def lernseite(p):
    """Handgepflegte Lernseiten (E13): einzige Ausnahme für Inline-JavaScript, eigene strengere CSP (E27)."""
    return p.startswith("lernen/") and p != "lernen/index.html"


for p in sorted(alle_html):
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    if re.search(r"<script\b", t, re.I) and not lernseite(p):
        fehler.append(f"{p}: <script> gefunden (kein JavaScript, E4/E13/E16)")
    if lernseite(p) and re.search(r"<script[^>]+\bsrc\s*=", t, re.I):
        fehler.append(f"{p}: Lernseite lädt ein externes Skript – nur Inline-JavaScript erlaubt (E13)")
    if lernseite(p) and re.search(r"\b(fetch|XMLHttpRequest|sendBeacon|WebSocket)\b", t):
        fehler.append(f"{p}: Lernseite mit Netzwerk-Aufruf (fetch/XHR/Beacon) – Daten dürfen das Gerät nicht verlassen (E13)")
    if re.search(r"<[a-z][^>]*\son[a-z]+\s*=", t, re.I):
        fehler.append(f"{p}: Inline-Event-Handler (on…=) gefunden")
    if re.search(r'(?:href|src|action)\s*=\s*"\s*javascript:', t, re.I):
        fehler.append(f"{p}: javascript:-Link gefunden")
    for tag in ("iframe", "object", "embed", "form", "base"):
        if re.search(rf"<{tag}\b", t, re.I):
            fehler.append(f"{p}: <{tag}> nicht erlaubt (Datenschutz/Sicherheit)")
    for tag in re.findall(r"<(?!a\b)[a-z]+\b[^>]*>", t, re.I):
        if re.search(r'rel="(?:canonical|alternate)"', tag):
            continue  # Verweis, kein Abruf
        for m in re.findall(r'\b(?:src|href|srcset|poster|data)\s*=\s*"((?:https?:)?//[^"]+)"', tag, re.I):
            fehler.append(f"{p}: Fremdabruf {m}")
    for tag in re.findall(r"<a\b[^>]*>", t, re.I):
        if 'target="_blank"' in tag and "noopener" not in tag:
            fehler.append(f"{p}: target=_blank ohne rel=noopener")
for c in sorted(alle_css):
    t = open(os.path.join(ROOT, c), encoding="utf-8").read()
    if re.search(r"@import|url\(\s*['\"]?(?:https?:)?//", t, re.I):
        fehler.append(f"{c}: externer Abruf in CSS (@import/url)")

# 9. Seitenstruktur der Hauptseiten: CSP, Referrer, Sprache, Titel, genau eine H1, keine Ebenen-Sprünge,
#    eindeutige IDs, Sprungmarken mit Ziel
CSP = "default-src 'self'; script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'"
# Lernseiten (E13/E27): Inline-Skripte ja, aber keinerlei Netzverbindung (connect-src 'none'), keine Fremdquellen
CSP_LERN = "default-src 'self'; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'"
for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    soll_csp = CSP_LERN if lernseite(p) else CSP
    if f'http-equiv="Content-Security-Policy" content="{soll_csp}"' not in t:
        fehler.append(f"{p}: Content-Security-Policy fehlt oder weicht ab")
    if '<meta name="referrer" content="no-referrer">' not in t:
        fehler.append(f"{p}: Referrer-Policy fehlt")
    if not re.search(r'<html lang="[a-z]{2}', t):
        fehler.append(f"{p}: <html lang> fehlt")
    if not re.search(r"<title>[^<]+</title>", t):
        fehler.append(f"{p}: <title> fehlt")
    ebenen = [int(h) for h in re.findall(r"<h([1-6])\b", t)]
    if ebenen.count(1) != 1:
        fehler.append(f"{p}: {ebenen.count(1)}× <h1> (genau 1 erwartet)")
    if lernseite(p):
        continue  # Überschriften, IDs und Sprungmarken entstehen dort teils per Skript – hier nicht statisch prüfbar
    for a, b in zip(ebenen, ebenen[1:]):
        if b > a + 1:
            fehler.append(f"{p}: Überschriften-Sprung h{a} → h{b}")
            break
    ids = re.findall(r'\bid="([^"]+)"', t)
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        fehler.append(f"{p}: doppelte id „{i}“")
    for m in set(re.findall(r'href="#([^"]+)"', t)):
        if m not in ids:
            fehler.append(f"{p}: Sprungmarke #{m} ohne Ziel")

# 10. Alle Datendateien sind gültiges JSON, alle Links in links.json sind https
for d in sorted(os.listdir(os.path.join(ROOT, "data"))):
    if d.endswith(".json"):
        try:
            json.load(open(os.path.join(ROOT, "data", d), encoding="utf-8"))
        except ValueError as e:
            fehler.append(f"data/{d}: ungültiges JSON ({e})")
for k, l in links.items():
    if not l["url"].startswith("https://"):
        fehler.append(f"links.json: {k} – URL muss mit https:// beginnen")

# 11. Repo ist öffentlich (E20): keine internen Prüfnotizen in data/*.json, Intern-Ordner bleiben ignoriert
def schluessel(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from schluessel(v)
    elif isinstance(o, list):
        for v in o:
            yield from schluessel(v)
for d in sorted(os.listdir(os.path.join(ROOT, "data"))):
    if d.endswith(".json"):
        try:
            inhalt = json.load(open(os.path.join(ROOT, "data", d), encoding="utf-8"))
        except ValueError:
            continue  # schon in Abschnitt 10 gemeldet
        if {"pruefen", "intern", "notiz_intern"} & set(schluessel(inhalt)):
            fehler.append(f"data/{d}: internes Feld (pruefen/intern) – gehört nach data/intern/ (E20)")
ignore = open(os.path.join(ROOT, ".gitignore"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, ".gitignore")) else ""
for o in ("docs/intern/", "data/intern/"):
    if o not in ignore.split():
        fehler.append(f".gitignore: {o} fehlt – interne Notizen würden veröffentlicht (E20)")

# 12. Blog-Beiträge (E10): Frontmatter, Status, Link-Platzhalter; dazu Rubrik (E21), Bilder (E14), interne Seiten
STATUS = beitraege.STATUS
try:
    posts = beitraege.laden(ROOT)
except ValueError as e:
    posts = []
    fehler.append("data/beitraege: " + str(e))
blog_rubriken = {r["id"] for r in json.load(open(os.path.join(ROOT, "data/blog.json"), encoding="utf-8"))["rubriken"]}
slugs = {}
for b in posts:
    d, m = b["datei"].replace(os.sep, "/"), b["meta"]
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
    if m.get("rubrik") and m["rubrik"] not in blog_rubriken:
        fehler.append(f"{d}: rubrik {m['rubrik']!r} fehlt in data/blog.json")
    keys = beitraege.link_keys(b["body"]) + (m["links"] if isinstance(m.get("links"), list) else [])
    for k in sorted(set(keys)):
        if k not in links:
            fehler.append(f"{d}: unbekannter Link-Schlüssel [[link:{k}]]")
        elif not links[k].get("bestaetigt"):
            warn.append(f"{d}: Link {k} ohne bestaetigt (erscheint nur als Text)")
    for bd in beitraege.bilder(b["body"]) + ([m["bild"]] if m.get("bild") else []):
        if bd not in komplett:
            fehler.append(f"{d}: Bild {bd} ohne vollständigen Eintrag in data/bilder.json")
    for z in beitraege.seiten(b["body"]):
        if z and not os.path.isfile(os.path.join(ROOT, z)):
            fehler.append(f"{d}: [[seite:{z}]] – Seite existiert nicht")
    if re.search(r"\]\(\s*https?://|<[a-z/!]", b["body"], re.I):
        fehler.append(f"{d}: rohe URL/HTML im Text – Links nur als [[link:schluessel]]")
    if m.get("status") == "veroeffentlicht":
        if f"frankfurt/{m.get('slug')}.html" not in pages:
            fehler.append(f"{d}: veröffentlicht, aber frankfurt/{m.get('slug')}.html fehlt – erst build.py")
        if isinstance(m.get("pruefen"), list) and m["pruefen"]:
            warn.append(f"{d}: veröffentlicht mit {len(m['pruefen'])} offenen Prüfpunkten (BETREUUNG.md: erst bei leerem pruefen)")

# 13. Termine/Ortsbezirke (E12): Quelle, Stand, 16 Bezirke mit eigener Seite
termine = json.load(open(os.path.join(ROOT, "data/termine.json"), encoding="utf-8"))
if not termine.get("quelle") or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", termine.get("stand", "")):
    fehler.append("data/termine.json: quelle oder stand fehlt")
obrs = json.load(open(os.path.join(ROOT, "data/ortsbezirke.json"), encoding="utf-8"))["ortsbezirke"]
if sorted(o["nr"] for o in obrs) != list(range(1, 17)):
    fehler.append("data/ortsbezirke.json: nicht genau die Ortsbezirke 1–16")
for o in obrs:
    if f"ortsbezirke/ortsbezirk-{o['nr']}.html" not in pages:
        fehler.append(f"Seite für Ortsbezirk {o['nr']} fehlt – erst python3 tools/build.py")
if termine.get("termine") and max(t["datum"] for t in termine["termine"]) < datetime.date.today().isoformat():
    warn.append("data/termine.json: alle Termine liegen in der Vergangenheit – neuen PARLIS-Export importieren")

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
print(f"{len(pages)} Seiten + {len(alle_html) - len(pages)} weitere HTML, {len(alle_css)} CSS geprüft · {len(fehler)} Fehler · {len(warn)} Warnungen")
sys.exit(1 if fehler else 0)
