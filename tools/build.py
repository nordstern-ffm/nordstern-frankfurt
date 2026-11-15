#!/usr/bin/env python3
"""Nordstern Frankfurt – erzeugt alle Seiten aus data/*.json.

Aufruf im Repo-Hauptordner:  python3 tools/build.py
Danach immer:                 python3 tools/check.py
Kein Framework, kein npm, kein JavaScript, keine externen Abrufe.
Läuft in Termux (python3) und Git Bash gleich.
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


SITE = load("site.json")
DIENSTE = [d for d in load("dienste.json")["dienste"] if d.get("aktiv")]
PET = load("petitionen.json")
STAND = load("standpunkte.json")
LINKS = load("links.json")["links"]
ZAHLUNG = load("zahlung.json")
BILDER = {b["datei"]: b for b in load("bilder.json")["bilder"]}
ZAHLEN = load("zahlen.json")["zahlen"]
ABL = load("ablaeufe.json")
LIVE = SITE["launch"] and SITE["domain_bestaetigt"]
B = SITE["betreiber"]

NAV = [
    ("index.html", "Start", "house"),
    ("nachbarschaft.html", "Nachbarschaft", "hand-heart"),
    ("frankfurt.html", "Frankfurt-Info", "landmark"),
    ("mitmachen.html", "Melden & Petitionen", "megaphone"),
    ("dienste.html", "Vermittlung", "handshake"),
    ("standpunkte.html", "Standpunkte", "flag"),
    ("agentur.html", "Für Vereine & Firmen", "briefcase"),
]

STAR = ('<svg class="star" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<path d="M32 2 L37 27 L62 32 L37 37 L32 62 L27 37 L2 32 L27 27 Z"/>'
        '<path class="star-inner" d="M32 14 L35 29 L50 32 L35 35 L32 50 L29 35 L14 32 L29 29 Z"/></svg>')


with open(os.path.join(ROOT, "assets", "icons.svg"), encoding="utf-8") as f:
    ICONS = set(re.findall(r'<symbol id="([a-z0-9-]+)"', f.read()))


def icon(name, label=""):
    """Lucide-Icon aus assets/icons.svg. Ohne label = Deko (aria-hidden), mit label = Bild mit Namen."""
    if name not in ICONS:
        raise SystemExit(f"FEHLER: Icon „{name}“ fehlt in assets/icons.svg – in tools/icons.py ergänzen.")
    a = f'role="img" aria-label="{E(label)}"' if label else 'aria-hidden="true" focusable="false"'
    return f'<svg class="icon" {a}><use href="assets/icons.svg#{name}"/></svg>'


def link(key):
    """Bestätigte Links als <a>, unbestätigte nur als Text (keine ungeprüfte URL online)."""
    l = LINKS[key]
    if l.get("bestaetigt"):
        return f'<a href="{E(l["url"])}" rel="noopener">{E(l["titel"])}</a>'
    return f'{E(l["titel"])} <span class="small">(Link wird nach Prüfung ergänzt)</span>'


def nachweis(b):
    """Bildnachweis nach TULLU: Titel, Urheber, Lizenz (Link), Quelle (Link), Änderungen."""
    t = f'<a href="{E(b["quelle_url"])}" rel="noopener">{E(b["titel"])}</a> · {E(b["autor"])} · '
    t += f'<a href="{E(b["lizenz_url"])}" rel="noopener license">{E(b["lizenz"])}</a>'
    if b["geaendert"] != "nein":
        t += f' · geändert: {E(b["geaendert"])}'
    return t


def bild(datei, cls=""):
    """Bild nur mit Eintrag in data/bilder.json – fehlt er, bricht der Build ab."""
    if datei not in BILDER:
        raise SystemExit(f"FEHLER: {datei} fehlt in data/bilder.json – Bild nicht eingebunden.")
    b = BILDER[datei]
    c = f' class="{cls}"' if cls else ""
    return (f'<figure{c}><img src="{E(datei)}" alt="{E(b["alt"])}" loading="lazy" decoding="async">'
            f'<figcaption class="small">{nachweis(b)}</figcaption></figure>')


def kacheln(ids, titel="Zahlen, die zählen"):
    """Kennzahl-Kacheln aus data/zahlen.json – jede mit Quelle (Link nur wenn bestätigt) und Stand."""
    li = ""
    for k in ids:
        z = ZAHLEN[k]
        l = LINKS[z["link"]]
        q = f'<a href="{E(l["url"])}" rel="noopener">{E(z["quelle"])}</a>' if l.get("bestaetigt") else E(z["quelle"])
        li += (f'<li class="stat"><span class="stat-wert">{E(z["wert"])}</span> <span class="stat-text">{E(z["text"])}</span>'
               f'<span class="stat-quelle">Quelle: {q} · Stand: {E(z["stand"])}</span></li>')
    return f'<section aria-label="{E(titel)}"><ul class="stats">{li}</ul></section>'


def ziel_text(s):
    """{ziel} aus petitionen.json einsetzen – die Zahl steht nur dort (E3)."""
    return E(s).replace("{ziel}", str(PET["ziel_unterstuetzer"]))


def steps(key, titel=None):
    """Ablauf-Diagramm: <ol> = Reihenfolge für Screenreader, Nummer und Icon nur visuell."""
    a = ABL["ablaeufe"][key]
    hid = f"h-ablauf-{key}"
    li = ""
    for n, s in enumerate(a["schritte"], 1):
        t = f'<a href="{E(s["ziel"])}">{E(s["titel"])}</a>' if s.get("ziel") else E(s["titel"])
        li += (f'<li class="step"><span class="step-kopf"><span class="step-nr" aria-hidden="true">{n}</span>'
               f'<span class="step-icon">{icon(s["icon"])}</span></span><h3>{t}</h3><p>{ziel_text(s["text"])}</p></li>')
    hinweis = f'<p class="notice">{E(a["hinweis"])}</p>' if a["hinweis"] else ""
    return (f'<section aria-labelledby="{hid}"><h2 id="{hid}">{E(titel or a["titel"])}</h2>{hinweis}'
            f'<ol class="steps" role="list">{li}</ol></section>')


def timeline():
    """Zeitleiste: Status als Text (nicht nur Farbe), Datum nur wenn in den Daten bestätigt."""
    z = ABL["zeitleiste"]
    li = ""
    for e in z["eintraege"]:
        cls = "tl-" + e["status"].lower().replace(" ", "-")
        wann = f' · <span class="tl-wann">{E(e["wann"])}</span>' if e["wann"] else ""
        li += (f'<li class="tl {cls}"><p class="tl-status"><span class="status">{E(e["status"])}</span>{wann}</p>'
               f'<h3>{E(e["titel"])}</h3><p>{ziel_text(e["text"])}</p></li>')
    return (f'<section aria-labelledby="h-zeitleiste"><h2 id="h-zeitleiste">{E(z["titel"])}</h2>'
            f'<ol class="timeline" role="list">{li}</ol></section>')


def kontakt_zeile():
    if B["email"]:
        return f'<a class="btn btn-primary" href="mailto:{E(B["email"])}">{icon("mail")}E-Mail schreiben</a>'
    return '<p class="notice">Kontaktadresse wird vor dem Start ergänzt.</p>'


def page(path, title, desc, body):
    cur = ' aria-current="page"'
    nav = "".join(
        f'<li><a href="{h}"{cur if h == path else ""}>{icon(i)}<span>{l}</span></a></li>'
        for h, l, i in NAV)
    robots = "" if LIVE else '<meta name="robots" content="noindex, nofollow">\n'
    canon = f'<link rel="canonical" href="https://{SITE["domain"]}/{"" if path == "index.html" else path}">\n' if LIVE else ""
    entwurf = "" if LIVE else '<div class="draft" role="note">Vorschau – noch nicht offiziell gestartet.</div>'
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'">
<meta name="referrer" content="no-referrer">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} – {E(SITE["marke"])}</title>
<meta name="description" content="{E(desc)}">
{robots}{canon}<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0B1630">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath fill='%23E0B84A' d='M32 2 L37 27 L62 32 L37 37 L32 62 L27 37 L2 32 L27 27 Z'/%3E%3C/svg%3E">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
{entwurf}
<header class="site-header">
<div class="wrap head">
<a class="brand" href="index.html">{STAR}<span>{E(SITE["marke"])}<small>Frankfurter Norden · Frankfurt am Main</small></span></a>
<nav aria-label="Hauptmenü"><ul>{nav}</ul></nav>
</div>
</header>
<main id="inhalt" class="wrap">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<p><strong>{E(SITE["marke"])}</strong> – {E(SITE["claim"])}</p>
<p>Betrieben von {E(B["name"])} · {E(B["firma"])}. Der Verein „{E(SITE["verein"]["name"])}“ ist eigenständig und parteipolitisch neutral.</p>
<p><a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a> · <a href="bildnachweise.html">Bildnachweise</a> · Stand: {E(SITE["stand"])}</p>
<p class="small">Ohne Tracker, ohne Cookies, ohne Fremd-Schriften. Keine Rechts- oder Steuerberatung.</p>
</div>
</footer>
</body>
</html>
"""
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as f:
        f.write(doc)


def card(ico, t, body, extra=""):
    """Karte mit Deko-Icon als visuellem Anker (UX-KONZEPT: Bild vor Text)."""
    return f'<article class="card{extra}"><span class="card-icon">{icon(ico)}</span><h3>{t}</h3>{body}</article>'


# ------------------------------------------------------------------ Start
pillars = "".join(card(i, f'<a href="{h}">{t}</a>', f"<p>{d}</p>") for i, h, t, d in [
    ("hand-heart", "nachbarschaft.html", "Nachbarschaftshilfe", "Einkaufen, Begleitung, Gesellschaft, kleine Reparaturen – für ältere Menschen im Frankfurter Norden. Ein Verein in Gründung."),
    ("landmark", "frankfurt.html", "Frankfurt verstehen", "Wie Stadt und Ortsbeirat funktionieren, wo man was meldet und was Bürgerinnen und Bürger wirklich brauchen."),
    ("megaphone", "mitmachen.html", "Melden & bewegen", "Mängel direkt an die Stadt melden. Anliegen bündeln – Ziel: 220 Unterstützer je Projekt."),
    ("handshake", "dienste.html", "Vermittlung", "Personal, Hotel, Taxi, Massage, Nähen: Wir vermitteln an Menschen und Betriebe, die wir kennen."),
])
page("index.html", "Start",
     "Nordstern Frankfurt: Nachbarschaftshilfe, Stadt-Infos, Mängelmelder und Petitionen für den Frankfurter Norden – plus persönliche Vermittlung.",
     f"""
<section class="hero">
<p class="eyebrow">Frankfurter Norden · Preungesheim und Nachbarschaft</p>
<h1>Ein Stern für den Norden.<br><span>Damit niemand allein durch Frankfurt muss.</span></h1>
<p class="lead">Nordstern verbindet Nachbarschaftshilfe, verständliche Infos über unsere Stadt und kurze Wege zu Menschen, die anpacken.</p>
<div class="buttons"><a class="btn btn-primary" href="nachbarschaft.html">Hilfe &amp; Mitmachen</a><a class="btn" href="mitmachen.html">Mangel melden</a></div>
</section>
{kacheln(["einwohner_preungesheim", "einwohner_frankfurt", "entlastungsbetrag"])}
<section aria-labelledby="h-saeulen"><h2 id="h-saeulen">Vier Wege, ein Ziel</h2><div class="grid grid-2">{pillars}</div></section>
<section aria-labelledby="h-familie"><h2 id="h-familie">Die Nordstern-Familie</h2><div class="grid">
{card("languages", link("bangla_hilfe"), "<p>Visum, FSJ und Bundesfreiwilligendienst – erklärt auf Bangla und Deutsch.</p>")}
{card("route", link("wege_nach_frankfurt"), "<p>Geschichten von Menschen aus Eritrea, Thailand und Laos, die in Frankfurt angekommen sind.</p>")}
{card("users", f'<a href="{E(SITE["verein"]["website"])}" rel="noopener">Nachbarschaftshilfe Preungesheim</a>', "<p>Die Initiative für praktische Alltagshilfe – eigenständig und parteipolitisch neutral.</p>")}
</div></section>
{timeline()}
<section class="callout"><h2>So arbeiten wir</h2>
<ul><li><strong>Ehrlich:</strong> Was noch in Planung ist, steht auch so da.</li>
<li><strong>Getrennt:</strong> Ehrenamt, Politik und Geschäft laufen in eigenen Bereichen mit eigener Verantwortung.</li>
<li><strong>Sparsam mit Daten:</strong> keine Tracker, keine Formulare mit Gesundheitsdaten.</li></ul></section>
""")

# ---------------------------------------------------------- Nachbarschaft
page("nachbarschaft.html", "Nachbarschaftshilfe",
     "Nachbarschaftshilfe Frankfurter Norden e.V. in Gründung: praktische Alltagshilfe für ältere Menschen in Preungesheim.",
     f"""
<h1>Nachbarschaftshilfe im Frankfurter Norden</h1>
<p class="lead">Wir ersetzen niemanden. Wir übernehmen die praktische Hilfe zu Hause, die es in Preungesheim noch nicht gibt.</p>
<p><span class="badge">Verein in Gründung</span></p>
{kacheln(["einwohner_preungesheim", "entlastungsbetrag"])}
<h2>Auf einen Blick</h2>
<div class="grid">
{card("shopping-basket", "Was geplant ist", "<ul><li>Einkaufen und Botengänge</li><li>Begleitung zu Arzt und Behörde</li><li>Spaziergang und Gesellschaft</li><li>Hilfe mit Post und Handy</li><li>Kleine Handwerksarbeiten (keine Strom-, Gas-, Wasserinstallation)</li></ul>")}
{card("user-search", "Wen wir suchen", "<ul><li><strong>Eine Fachkraft</strong> (Pflege, Sozialarbeit, Pädagogik) für wenige Stunden im Monat – auch im Ruhestand</li><li>Gründungsmitglieder (sieben werden gebraucht)</li><li>Helfende aus der Nachbarschaft</li></ul>")}
</div>
{steps("nachbarschaft")}
<p>Alle Details, Fachkraft-Ausschreibung und Blog: <a href="{E(SITE["verein"]["website"])}" rel="noopener">Website der Initiative</a>.</p>
<div class="callout"><h2>Warum hier getrennt?</h2><p>Der Verein soll gemeinnützig werden. Gemeinnützige Vereine dürfen keine Partei unterstützen und kein Geschäft für Dritte machen. Darum hat der Verein eine eigene Seite, und Nordstern verlinkt nur dorthin.</p></div>
""")

# -------------------------------------------------------------- Frankfurt
page("frankfurt.html", "Frankfurt-Info",
     "Frankfurt einfach erklärt: Stadtverordnete, Ortsbeiräte, Bürgerbeteiligung und wo Bürger welche Hilfe finden.",
     f"""
<h1>Frankfurt verstehen</h1>
<p class="lead">Wer entscheidet was in unserer Stadt – und wo kann ich mitreden?</p>
<h2>Stadt, Ortsbeirat, Beteiligung</h2>
<div class="grid">
{card("building-2", "Stadtverordnetenversammlung", "<p>Das Parlament der Stadt. Es beschließt Haushalt, Satzungen und große Vorhaben. Gewählt bei der Kommunalwahl, zuletzt am 15. März 2026, für fünf Jahre.</p>")}
{card("map-pinned", "Ortsbeiräte", "<p>Frankfurt hat 16 Ortsbeiräte. Sie beraten über alles, was den eigenen Stadtteil betrifft – Verkehr, Spielplätze, Grünflächen. Preungesheim gehört zum Ortsbezirk 10. Die Sitzungen sind öffentlich, Bürgerinnen und Bürger dürfen in der Bürgerfragestunde sprechen.</p>")}
{card("laptop", "Beteiligung online", f"<p>{link('ffm_start')}: Mängel melden, Ideen einreichen, Vorhaben unterstützen.</p>")}
</div>
<h2>Was Bürgerinnen und Bürger brauchen</h2>
<p>Unsere Themen, über die wir hier regelmäßig schreiben:</p>
<ul class="topics"><li>Bezahlbares Wohnen und Hilfe bei Wohnungssuche</li><li>Behördengänge verständlich erklärt – auch auf Bengalisch, Tigrinya, Thai und Lao (siehe {link("bangla_hilfe")} und {link("wege_nach_frankfurt")})</li><li>Sichere Wege für Ältere, Kinder und Rollstuhl</li><li>Pflege zu Hause und Entlastung für Angehörige</li><li>Arbeit finden im Frankfurter Norden</li></ul>
<p class="small">Wir schreiben parteiunabhängig. Positionen einzelner Parteien stehen ausschließlich unter <a href="standpunkte.html">Standpunkte</a> und sind dort als solche gekennzeichnet.</p>
""")

# ------------------------------------------------- Mängel & Petitionen
pets = [p for p in PET["eintraege"] if p["veroeffentlicht"]]
ziel = PET["ziel_unterstuetzer"]
if pets:
    pet_html = '<div class="grid">' + "".join(card(
        "megaphone", E(p["titel"]),
        f'<p>{E(p["anliegen"])}</p><p class="small">{E(p["stadtteil"])}</p>'
        f'<div class="meter" role="img" aria-label="{p["unterstuetzer"]} von {ziel} Unterstützern">'
        f'<span style="width:{min(100, round(p["unterstuetzer"] * 100 / ziel))}%"></span></div>'
        f'<p><strong>{p["unterstuetzer"]}</strong> von {ziel}</p>'
        + (f'<a class="btn btn-primary" href="{E(p["plattform_url"])}" rel="noopener">Jetzt unterstützen</a>' if p["plattform_url"] else ""))
        for p in pets) + "</div>"
else:
    pet_html = '<p class="notice">Die ersten Anliegen werden gerade mit Nachbarinnen und Nachbarn gesammelt. Sie haben ein Thema? Schreiben Sie uns.</p>'
page("mitmachen.html", "Melden & Petitionen",
     f"Mängel in Frankfurt direkt an die Stadt melden und Anliegen bündeln – Ziel {ziel} Unterstützer je Projekt.",
     f"""
<h1>Melden. Bündeln. Bewegen.</h1>
{steps("melden")}
<h2 id="melden">1 · Mangel sehen – direkt melden</h2>
<p>Kaputte Laterne, Schlagloch, wilder Müll: Melden Sie es dort, wo die Stadt es bearbeitet – beim offiziellen {link('maengelmelder')}. Ein eigener Melder auf dieser Seite würde nur Umwege erzeugen.</p>
<h2 id="buendeln">2 · Anliegen bündeln – {ziel} Stimmen</h2>
<p>Größere Wünsche brauchen viele Unterstützer. Wir helfen beim Formulieren, sammeln im Stadtteil und reichen es auf der {link('ideenplattform')} oder als Petition ein. Unser Ziel je Projekt: <strong>{ziel} Unterstützerinnen und Unterstützer</strong>.</p>
{pet_html}
{steps("anliegen", "3 · Selbst ein Anliegen starten")}
{kontakt_zeile()}
<p class="small">Unterschriften sammeln wir nicht auf dieser Seite – Ihre politische Meinung bleibt bei der Plattform, auf der Sie unterschreiben.</p>
""")

# ---------------------------------------------------------- Vermittlung
dienst_html = "".join(card(d["icon"], E(d["titel"]), f'<p>{E(d["kurz"])}</p><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["punkte"]) + "</ul>") for d in DIENSTE)
page("dienste.html", "Vermittlung",
     "Persönliche Vermittlung in Frankfurt: Personal, Hotelzimmer, Taxi, Massage und Nähen – im kleinen Kreis.",
     f"""
<h1>Vermittlung im kleinen Kreis</h1>
<p class="lead">Kein Portal, kein Algorithmus. Wir kennen die Menschen, die wir empfehlen.</p>
<h2>Was wir vermitteln</h2>
<div class="grid">{dienst_html}</div>
{kontakt_zeile()}
<p class="small">Gewerbliches Angebot von {E(B["firma"])}. Nicht Teil des Vereins. Wir befördern, beherbergen und behandeln nicht selbst, sondern vermitteln an Fachbetriebe und Fachkräfte.</p>
""")

# ---------------------------------------------------------- Standpunkte
frei = [s for s in STAND["eintraege"] if s.get("freigegeben")]
if frei:
    sp = '<div class="grid">' + "".join(card("flag", E(s["titel"]), f'<p>{E(s["teaser"])}</p><p class="small">Quelle: {E(s["quelle"])}</p>') for s in frei) + "</div>"
else:
    sp = f'<p class="notice">{len(STAND["eintraege"])} Positionen sind vorbereitet und erscheinen nach Freigabe durch den Vorstand der {E(STAND["herausgeber"])}.</p>'
page("standpunkte.html", "Standpunkte",
     "Gekennzeichnete Positionen der FREIEN WÄHLER Frankfurt aus dem Kommunalwahlprogramm 2026.",
     f"""
<h1>Standpunkte</h1>
<div class="callout"><p><strong>Gekennzeichneter Bereich:</strong> Hier stehen Positionen der {E(STAND["herausgeber"])}. Verantwortlich für den Inhalt ist die Partei. Der Rest von Nordstern ist parteiunabhängig.</p></div>
{sp}
<p>Volltext: {link('fw_programm')}</p>
""")

# ------------------------------------------------------------- Agentur
def pakete_html():
    """Nur aktive Pakete mit Preis UND gehostetem Zahlungslink; sonst Anfrage per E-Mail."""
    ps = [p for p in ZAHLUNG["pakete"] if p["aktiv"] and p["preis"] and p["zahl_link"]]
    if not ps:
        return ""
    return '<h2>Pakete</h2><div class="grid">' + "".join(card("package", E(p["titel"]),
        f'<p class="small">Für {E(p["fuer"])}</p><ul>' + "".join(f"<li>{E(x)}</li>" for x in p["leistung"])
        + f'</ul><p><strong>{E(p["preis"])}</strong></p><a class="btn btn-primary" href="{E(p["zahl_link"])}" rel="noopener">Jetzt buchen</a>')
        for p in ps) + '</div><p class="small">Die Zahlung läuft über eine gesicherte Zahlungsseite unseres Zahlungsdienstleisters. Wir sehen keine Kartendaten.</p>'


page("agentur.html", "Für Vereine & Firmen",
     "Copy & Code Agency Frankfurt: Websites, Texte und digitale Werkzeuge für Vereine, Ortsbeiräte und kleine Betriebe.",
     f"""
<h1>Diese Seite gibt es auch für Ihren Stadtteil</h1>
<p class="lead">Nordstern ist unser Schaufenster. {E(B["firma"])} baut so etwas für Vereine, Initiativen und kleine Betriebe – schnell, barrierearm, ohne Tracker.</p>
<h2>Was wir anbieten</h2>
<div class="grid">
{card("layout-template", "Stadtteil-Seite", "<p>Info-Seite für Verein oder Initiative: Inhalte aus einer Datei, Pflege ohne Programmierkenntnisse, Hosting fast kostenlos.</p>")}
{card("pen-line", "Texte, die ankommen", "<p>Websites, Anträge, Flyer, Bewerbungen und politische Texte – klar, prüfbar, in einfacher Sprache auf Wunsch.</p>")}
{card("wrench", "Digitale Werkzeuge", "<p>Koordinations-Apps für Nachbarschaftshilfe, Hotel-Werkzeuge, mehrsprachige Info-Portale. Rechte bleiben klar geregelt.</p>")}
</div>
{pakete_html()}
<h2>Referenzen aus eigener Arbeit</h2>
<ul><li>Nachbarschaftshilfe Preungesheim – Website und Koordinations-Prototyp</li><li>BanglaHilfe – zweisprachige Behörden-Hilfe Deutsch/Bengalisch</li><li>wege-nach-frankfurt – Geschichten aus Eritrea, Thailand und Laos</li><li>Housekeeping-Werkzeug für ein Frankfurter Hotel</li></ul>
{kontakt_zeile()}
""")

# ------------------------------------------------------- Rechtstexte
def feld(v):
    return E(v) if v else '<span class="todo">wird vor dem Start ergänzt</span>'

page("impressum.html", "Impressum", "Impressum von Nordstern Frankfurt.", f"""
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG</p>
<p>{E(B["name"])}<br>{E(B["firma"])}<br>{feld(B["anschrift"])}</p>
<p>E-Mail: {feld(B["email"])}<br>Telefon: {feld(B["telefon"])}</p>
<p>{feld(B["ust_id_oder_hinweis"])}</p>
<p>Inhaltlich verantwortlich nach § 18 Abs. 2 MStV: {E(B["name"])}, Anschrift wie oben.</p>
<p>Für den Bereich „Standpunkte“ ist die {E(STAND["herausgeber"])} verantwortlich.</p>
""")
page("datenschutz.html", "Datenschutz", "Datenschutzerklärung von Nordstern Frankfurt.", f"""
<h1>Datenschutz</h1>
<p><strong>Kurz:</strong> Diese Seite setzt keine Cookies, nutzt keine Tracker, lädt keine Schriften oder Skripte von Dritten und hat keine Formulare.</p>
<h2>Verantwortlich</h2><p>Siehe <a href="impressum.html">Impressum</a>.</p>
<h2>Hosting</h2><p>Die Seite wird über GitHub Pages (GitHub Inc., USA) ausgeliefert. Dabei verarbeitet GitHub technisch notwendige Daten wie die IP-Adresse. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. Hinweis des Betreibers: Ein Umzug zu einem Hoster in der EU ist geplant.</p>
<h2>E-Mail</h2><p>Wenn Sie uns schreiben, nutzen wir Ihre Angaben nur zur Beantwortung und löschen sie, wenn der Vorgang erledigt ist.</p>
<h2>Externe Links</h2><p>Links zu ffm.de oder Petitionsplattformen führen zu deren eigenen Datenschutzregeln.</p>
<h2>Ihre Rechte</h2><p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch und Beschwerde beim Hessischen Beauftragten für Datenschutz und Informationsfreiheit.</p>
""")

if BILDER:
    zeilen = "".join(
        f'<tr><td><a href="{E(d)}">{E(b["titel"])}</a></td><td>{E(b["autor"])}</td>'
        f'<td><a href="{E(b["lizenz_url"])}" rel="noopener license">{E(b["lizenz"])}</a></td>'
        f'<td><a href="{E(b["quelle_url"])}" rel="noopener">Original</a></td>'
        f'<td>{E(b["geaendert"])}</td><td>{E(b["geprueft"])}</td></tr>'
        for d, b in sorted(BILDER.items()))
    bn = ('<div class="table-wrap"><table><caption class="small">Alle Bilder und Grafiken dieser Website</caption>'
          '<thead><tr><th scope="col">Titel</th><th scope="col">Urheber</th><th scope="col">Lizenz</th>'
          '<th scope="col">Quelle</th><th scope="col">Änderungen</th><th scope="col">Lizenz geprüft</th></tr></thead>'
          f'<tbody>{zeilen}</tbody></table></div>')
else:
    bn = '<p class="notice">Derzeit verwendet diese Website keine Fotos oder fremden Grafiken. Stern-Symbol und Gestaltung sind eigene Arbeit.</p>'
page("bildnachweise.html", "Bildnachweise", "Urheber, Lizenzen und Quellen aller Bilder auf Nordstern Frankfurt.", f"""
<h1>Bildnachweise</h1>
<p class="lead">Jedes Bild steht hier mit Urheber, Lizenz und Quelle. Die Lizenz wurde jeweils am Original geprüft.</p>
{bn}
<p class="small">Schriften: Fraunces und Atkinson Hyperlegible, lokal eingebunden unter der SIL Open Font License (Lizenztexte im Ordner <code>fonts/</code>).</p>
""")

page("404.html", "Seite nicht gefunden", "Seite nicht gefunden.", '<h1>Hier ist kein Stern.</h1><p><a class="btn btn-primary" href="index.html">Zur Startseite</a></p>')

# -------------------------------------------------- Launch-Dateien
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write("User-agent: *\n" + ("Allow: /\n" if LIVE else "Disallow: /\n"))
cname = os.path.join(ROOT, "CNAME")
if LIVE:
    with open(cname, "w") as f:
        f.write(SITE["domain"] + "\n")
elif os.path.exists(cname):
    os.remove(cname)
print(f"Gebaut: {len(NAV) + 4} Seiten · Modus: {'LIVE ' + SITE['domain'] if LIVE else 'Vorschau (noindex, kein CNAME)'}")
