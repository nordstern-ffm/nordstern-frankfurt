#!/usr/bin/env python3
"""Nordstern Frankfurt – erzeugt alle Seiten aus data/*.json.

Aufruf im Repo-Hauptordner:  python3 tools/build.py
Danach immer:                 python3 tools/check.py
Blog-Vorschau:                 python3 tools/build.py --entwuerfe <ordner außerhalb des Repos>
Kein Framework, kein npm, kein JavaScript, keine externen Abrufe.
Läuft in Termux (python3) und Git Bash gleich.
"""
import datetime, glob, html, json, os, shutil, sys
sys.dont_write_bytecode = True  # kein tools/__pycache__ im Repo
import beitraege

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
LIVE = SITE["launch"] and SITE["domain_bestaetigt"]
B = SITE["betreiber"]

# Blog (E10): nur status "veroeffentlicht" wird gebaut und verlinkt; Entwürfe nie.
BEITRAEGE = beitraege.laden(ROOT)
for _b in BEITRAEGE:
    if _b["meta"].get("status") not in beitraege.STATUS:
        sys.exit("Unbekannter status in " + _b["datei"] + " – erst python3 tools/check.py")
# Termine (PARLIS-Export, tools/ics_import.py) und Ortsbezirke (E11/E12)
TERMINE = load("termine.json")
ORTSBEZIRKE = load("ortsbezirke.json")["ortsbezirke"]
# Stichtag für "nächste Termine": NORDSTERN_HEUTE=JJJJ-MM-TT erlaubt reproduzierbare Builds
HEUTE = os.environ.get("NORDSTERN_HEUTE") or datetime.date.today().isoformat()
KOMMEND = [t for t in TERMINE["termine"] if t["datum"] >= HEUTE]

VEROEFF = sorted((b for b in BEITRAEGE if b["meta"]["status"] == "veroeffentlicht"),
                 key=lambda b: b["meta"]["datum"], reverse=True)

NAV = [
    ("index.html", "Start"),
    ("nachbarschaft.html", "Nachbarschaft"),
    ("frankfurt.html", "Frankfurt-Info"),
    ("ortsbezirke/index.html", "Ortsbezirke"),
    ("mitmachen.html", "Melden & Petitionen"),
    ("dienste.html", "Vermittlung"),
    ("standpunkte.html", "Standpunkte"),
    ("lernen/index.html", "Lernen"),
    ("agentur.html", "Für Vereine & Firmen"),
]

STAR = ('<svg class="star" viewBox="0 0 64 64" aria-hidden="true" focusable="false">'
        '<path d="M32 2 L37 27 L62 32 L37 37 L32 62 L27 37 L2 32 L27 27 Z"/>'
        '<path class="star-inner" d="M32 14 L35 29 L50 32 L35 35 L32 50 L29 35 L14 32 L29 29 Z"/></svg>')


def link(key):
    """Bestätigte Links als <a>, unbestätigte nur als Text (keine ungeprüfte URL online)."""
    if key not in LINKS:
        sys.exit("Unbekannter Link-Schlüssel: " + key + " (fehlt in data/links.json)")
    l = LINKS[key]
    if l.get("bestaetigt"):
        return f'<a href="{E(l["url"])}" rel="noopener">{E(l["titel"])}</a>'
    return f'{E(l["titel"])} <span class="small">(Link wird nach Prüfung ergänzt)</span>'


def kontakt_zeile():
    if B["email"]:
        return f'<a class="btn btn-primary" href="mailto:{E(B["email"])}">E-Mail schreiben</a>'
    return '<p class="notice">Kontaktadresse wird vor dem Start ergänzt.</p>'


def page(path, title, desc, body, out=ROOT, aktiv=None):
    """path relativ zum Ausgabeordner; Unterordner (frankfurt/…) bekommen ../ vor allen internen Pfaden."""
    cur = ' aria-current="page"'
    pre = "../" * path.count("/")
    aktiv = aktiv or path
    nav = "".join(
        f'<li><a href="{pre}{h}"{cur if h == aktiv else ""}>{l}</a></li>'
        for h, l in NAV)
    robots = "" if LIVE else '<meta name="robots" content="noindex, nofollow">\n'
    canon = f'<link rel="canonical" href="https://{SITE["domain"]}/{"" if path == "index.html" else path}">\n' if LIVE else ""
    entwurf = "" if LIVE else '<div class="draft" role="note">Vorschau – noch nicht offiziell gestartet.</div>'
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} – {E(SITE["marke"])}</title>
<meta name="description" content="{E(desc)}">
{robots}{canon}<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0B1630">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Cpath fill='%23E0B84A' d='M32 2 L37 27 L62 32 L37 37 L32 62 L27 37 L2 32 L27 27 Z'/%3E%3C/svg%3E">
<link rel="stylesheet" href="{pre}css/style.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
{entwurf}
<header class="site-header">
<div class="wrap head">
<a class="brand" href="{pre}index.html">{STAR}<span>{E(SITE["marke"])}<small>Frankfurter Norden · Frankfurt am Main</small></span></a>
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
<p><a href="{pre}impressum.html">Impressum</a> · <a href="{pre}datenschutz.html">Datenschutz</a> · Stand: {E(SITE["stand"])}</p>
<p class="small">Ohne Tracker, ohne Cookies, ohne Fremd-Schriften. Keine Rechts- oder Steuerberatung.</p>
</div>
</footer>
</body>
</html>
"""
    ziel = os.path.join(out, path)
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(doc)


def card(t, body, extra=""):
    return f'<article class="card{extra}"><h3>{t}</h3>{body}</article>'


# ------------------------------------------------------- Termine-Helfer
WOCHENTAG = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]


def datum_text(t, lang=False):
    d = datetime.date.fromisoformat(t["datum"])
    tag = WOCHENTAG[d.weekday()]
    return tag + " " + d.strftime("%d.%m.%Y") + ", " + t["zeit"] + " Uhr"


def naechster(pred):
    for t in KOMMEND:
        if pred(t):
            return t
    return None


def obr_seite(nr):
    return "ortsbezirke/ortsbezirk-" + str(nr) + ".html"


def termin_hinweis():
    return (f'<p class="small">Geplante Termine laut PARLIS-Kalender der Stadt (Stand {E(TERMINE["stand"])}). '
            'Ort und Tagesordnung stehen im Ratsinformationssystem PARLIS – bitte dort prüfen.</p>')


def kalender_ticker():
    """Rotierende News-Zeile ohne JavaScript (E12): CSS-Animation, pausiert bei Hover/Fokus/Schalter,
    bei prefers-reduced-motion als ruhige Liste. Immer genau 5 Einträge."""
    eintraege = []
    if VEROEFF:
        b = VEROEFF[0]["meta"]
        eintraege.append(("Neu im Blog", E(b["titel"]), "frankfurt/" + E(b["slug"]) + ".html"))
    for pred, label, ziel in [
        (lambda t: t["ortsbezirk"] == 10, "Ortsbeirat 10", obr_seite(10)),
        (lambda t: t["typ"] == "stvv", "Stadtverordnetenversammlung", "ortsbezirke/index.html"),
        (lambda t: t["typ"] == "kav", "KAV – Ausländerinnen- und Ausländervertretung", "ortsbezirke/index.html"),
    ]:
        t = naechster(pred)
        if t:
            eintraege.append(("Nächste Sitzung", label + ": " + datum_text(t), ziel))
    woche = (datetime.date.fromisoformat(HEUTE) + datetime.timedelta(days=7)).isoformat()
    n = len([t for t in KOMMEND if t["typ"] == "ortsbeirat" and t["datum"] <= woche])
    wort = "Ortsbeiratssitzung" if n == 1 else "Ortsbeiratssitzungen"
    eintraege.append(("Alle 16 Ortsbezirke", str(n) + " " + wort + " in den nächsten 7 Tagen", "ortsbezirke/index.html"))
    eintraege.append(("Mitmachen", "Mangel gesehen? So meldest du ihn der Stadt", "mitmachen.html"))
    eintraege = eintraege[:5]
    li = "".join(
        f'<li class="tick" style="--i:{i}"><span class="tick-label">{lab}</span> '
        f'<a href="{ziel}">{txt}</a></li>'
        for i, (lab, txt, ziel) in enumerate(eintraege))
    return ('<section class="ticker" aria-labelledby="h-ticker">'
            '<h2 id="h-ticker" class="ticker-h">Termine &amp; Neues</h2>'
            '<input type="checkbox" id="ticker-pause" class="ticker-pause">'
            '<label for="ticker-pause" class="ticker-btn">Laufband anhalten</label>'
            f'<ol class="ticker-list">{li}</ol></section>')


# ------------------------------------------------------------------ Start
pillars = "".join(card(f'<a href="{h}">{t}</a>', f"<p>{d}</p>") for h, t, d in [
    ("nachbarschaft.html", "Nachbarschaftshilfe", "Einkaufen, Begleitung, Gesellschaft, kleine Reparaturen – für ältere Menschen im Frankfurter Norden. Ein Verein in Gründung."),
    ("frankfurt.html", "Frankfurt verstehen", "Wie Stadt und Ortsbeirat funktionieren, wo man was meldet und was Bürgerinnen und Bürger wirklich brauchen."),
    ("mitmachen.html", "Melden & bewegen", "Mängel direkt an die Stadt melden. Anliegen bündeln – Ziel: 220 Unterstützer je Projekt."),
    ("dienste.html", "Vermittlung", "Personal, Hotel, Taxi, Massage, Nähen: Wir vermitteln an Menschen und Betriebe, die wir kennen."),
])
page("index.html", "Start",
     "Nordstern Frankfurt: Nachbarschaftshilfe, Stadt-Infos, Mängelmelder und Petitionen für den Frankfurter Norden – plus persönliche Vermittlung.",
     f"""
{kalender_ticker()}
<section class="hero">
<p class="eyebrow">Frankfurter Norden · Preungesheim und Nachbarschaft</p>
<h1>Ein Stern für den Norden.<br><span>Damit niemand allein durch Frankfurt muss.</span></h1>
<p class="lead">Nordstern verbindet Nachbarschaftshilfe, verständliche Infos über unsere Stadt und kurze Wege zu Menschen, die anpacken.</p>
<div class="buttons"><a class="btn btn-primary" href="nachbarschaft.html">Hilfe &amp; Mitmachen</a><a class="btn" href="mitmachen.html">Mangel melden</a></div>
</section>
<section aria-labelledby="h-saeulen"><h2 id="h-saeulen">Vier Wege, ein Ziel</h2><div class="grid grid-2">{pillars}</div></section>
<section aria-labelledby="h-familie"><h2 id="h-familie">Die Nordstern-Familie</h2><div class="grid">
{card(link("bangla_hilfe"), "<p>Visum, FSJ und Bundesfreiwilligendienst – erklärt auf Bangla und Deutsch.</p>")}
{card(link("wege_nach_frankfurt"), "<p>Geschichten von Menschen aus Eritrea, Thailand und Laos, die in Frankfurt angekommen sind.</p>")}
{card(f'<a href="{E(SITE["verein"]["website"])}" rel="noopener">Nachbarschaftshilfe Preungesheim</a>', "<p>Die Initiative für praktische Alltagshilfe – eigenständig und parteipolitisch neutral.</p>")}
</div></section>
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
<div class="grid">
{card("Was geplant ist", "<ul><li>Einkaufen und Botengänge</li><li>Begleitung zu Arzt und Behörde</li><li>Spaziergang und Gesellschaft</li><li>Hilfe mit Post und Handy</li><li>Kleine Handwerksarbeiten (keine Strom-, Gas-, Wasserinstallation)</li></ul>")}
{card("Wen wir suchen", "<ul><li><strong>Eine Fachkraft</strong> (Pflege, Sozialarbeit, Pädagogik) für wenige Stunden im Monat – auch im Ruhestand</li><li>Gründungsmitglieder (sieben werden gebraucht)</li><li>Helfende aus der Nachbarschaft</li></ul>")}
</div>
<p>Alle Details, Fachkraft-Ausschreibung und Blog: <a href="{E(SITE["verein"]["website"])}" rel="noopener">Website der Initiative</a>.</p>
<div class="callout"><h2>Warum hier getrennt?</h2><p>Der Verein soll gemeinnützig werden. Gemeinnützige Vereine dürfen keine Partei unterstützen und kein Geschäft für Dritte machen. Darum hat der Verein eine eigene Seite, und Nordstern verlinkt nur dorthin.</p></div>
""")

# -------------------------------------------------------------- Frankfurt
blog_hinweis = ('<p><a class="btn" href="frankfurt/index.html">Alle Beiträge aus dem Frankfurter Norden</a></p>'
                if VEROEFF else "") + ("\n" if VEROEFF else "")
page("frankfurt.html", "Frankfurt-Info",
     "Frankfurt einfach erklärt: Stadtverordnete, Ortsbeiräte, Bürgerbeteiligung und wo Bürger welche Hilfe finden.",
     f"""
<h1>Frankfurt verstehen</h1>
<p class="lead">Wer entscheidet was in unserer Stadt – und wo kann ich mitreden?</p>
<div class="grid">
{card("Stadtverordnetenversammlung", "<p>Das Parlament der Stadt. Es beschließt Haushalt, Satzungen und große Vorhaben. Gewählt bei der Kommunalwahl, zuletzt am 15. März 2026, für fünf Jahre.</p>")}
{card("Ortsbeiräte", "<p>Frankfurt hat 16 Ortsbeiräte. Sie beraten über alles, was den eigenen Stadtteil betrifft – Verkehr, Spielplätze, Grünflächen. Preungesheim gehört zum Ortsbezirk 10. Die Sitzungen sind öffentlich, Bürgerinnen und Bürger dürfen in der Bürgerfragestunde sprechen.</p>")}
{card("Beteiligung online", f"<p>{link('ffm_start')}: Mängel melden, Ideen einreichen, Vorhaben unterstützen.</p>")}
</div>
<h2>Was Bürgerinnen und Bürger brauchen</h2>
<p>Unsere Themen, über die wir hier regelmäßig schreiben:</p>
<ul class="topics"><li>Bezahlbares Wohnen und Hilfe bei Wohnungssuche</li><li>Behördengänge verständlich erklärt – auch auf Bengalisch, Tigrinya, Thai und Lao (siehe {link("bangla_hilfe")} und {link("wege_nach_frankfurt")})</li><li>Sichere Wege für Ältere, Kinder und Rollstuhl</li><li>Pflege zu Hause und Entlastung für Angehörige</li><li>Arbeit finden im Frankfurter Norden</li></ul>
{blog_hinweis}<p class="small">Wir schreiben parteiunabhängig. Positionen einzelner Parteien stehen ausschließlich unter <a href="standpunkte.html">Standpunkte</a> und sind dort als solche gekennzeichnet.</p>
""")

# ------------------------------------------------- Mängel & Petitionen
pets = [p for p in PET["eintraege"] if p["veroeffentlicht"]]
ziel = PET["ziel_unterstuetzer"]
if pets:
    pet_html = '<div class="grid">' + "".join(card(
        E(p["titel"]),
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
<h2>1 · Mangel sehen – direkt melden</h2>
<p>Kaputte Laterne, Schlagloch, wilder Müll: Melden Sie es dort, wo die Stadt es bearbeitet – beim offiziellen {link('maengelmelder')}. Ein eigener Melder auf dieser Seite würde nur Umwege erzeugen.</p>
<h2>2 · Anliegen bündeln – {ziel} Stimmen</h2>
<p>Größere Wünsche brauchen viele Unterstützer. Wir helfen beim Formulieren, sammeln im Stadtteil und reichen es auf der {link('ideenplattform')} oder als Petition ein. Unser Ziel je Projekt: <strong>{ziel} Unterstützerinnen und Unterstützer</strong>.</p>
{pet_html}
<h2>3 · Selbst ein Anliegen starten</h2>
<ol><li>Problem in zwei Sätzen beschreiben – wo, was, für wen.</li><li>Uns schreiben; wir prüfen, ob Stadt, Ortsbeirat oder Land zuständig ist.</li><li>Gemeinsam Text und Fotos fertig machen und einreichen.</li></ol>
{kontakt_zeile()}
<p class="small">Unterschriften sammeln wir nicht auf dieser Seite – Ihre politische Meinung bleibt bei der Plattform, auf der Sie unterschreiben.</p>
""")

# ---------------------------------------------------------- Vermittlung
dienst_html = "".join(card(E(d["titel"]), f'<p>{E(d["kurz"])}</p><ul>' + "".join(f"<li>{E(x)}</li>" for x in d["punkte"]) + "</ul>") for d in DIENSTE)
page("dienste.html", "Vermittlung",
     "Persönliche Vermittlung in Frankfurt: Personal, Hotelzimmer, Taxi, Massage und Nähen – im kleinen Kreis.",
     f"""
<h1>Vermittlung im kleinen Kreis</h1>
<p class="lead">Kein Portal, kein Algorithmus. Wir kennen die Menschen, die wir empfehlen.</p>
<div class="grid">{dienst_html}</div>
{kontakt_zeile()}
<p class="small">Gewerbliches Angebot von {E(B["firma"])}. Nicht Teil des Vereins. Wir befördern, beherbergen und behandeln nicht selbst, sondern vermitteln an Fachbetriebe und Fachkräfte.</p>
""")

# ---------------------------------------------------------- Standpunkte
frei = [s for s in STAND["eintraege"] if s.get("freigegeben")]
if frei:
    sp = '<div class="grid">' + "".join(card(E(s["titel"]), f'<p>{E(s["teaser"])}</p><p class="small">Quelle: {E(s["quelle"])}</p>') for s in frei) + "</div>"
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
    return '<h2>Pakete</h2><div class="grid">' + "".join(card(E(p["titel"]),
        f'<p class="small">Für {E(p["fuer"])}</p><ul>' + "".join(f"<li>{E(x)}</li>" for x in p["leistung"])
        + f'</ul><p><strong>{E(p["preis"])}</strong></p><a class="btn btn-primary" href="{E(p["zahl_link"])}" rel="noopener">Jetzt buchen</a>')
        for p in ps) + '</div><p class="small">Die Zahlung läuft über eine gesicherte Zahlungsseite unseres Zahlungsdienstleisters. Wir sehen keine Kartendaten.</p>'


page("agentur.html", "Für Vereine & Firmen",
     "Copy & Code Agency Frankfurt: Websites, Texte und digitale Werkzeuge für Vereine, Ortsbeiräte und kleine Betriebe.",
     f"""
<h1>Diese Seite gibt es auch für Ihren Stadtteil</h1>
<p class="lead">Nordstern ist unser Schaufenster. {E(B["firma"])} baut so etwas für Vereine, Initiativen und kleine Betriebe – schnell, barrierearm, ohne Tracker.</p>
<div class="grid">
{card("Stadtteil-Seite", "<p>Info-Seite für Verein oder Initiative: Inhalte aus einer Datei, Pflege ohne Programmierkenntnisse, Hosting fast kostenlos.</p>")}
{card("Texte, die ankommen", "<p>Websites, Anträge, Flyer, Bewerbungen und politische Texte – klar, prüfbar, in einfacher Sprache auf Wunsch.</p>")}
{card("Digitale Werkzeuge", "<p>Koordinations-Apps für Nachbarschaftshilfe, Hotel-Werkzeuge, mehrsprachige Info-Portale. Rechte bleiben klar geregelt.</p>")}
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
<p><strong>Kurz:</strong> Diese Seite setzt keine Cookies, nutzt keine Tracker, lädt keine Schriften oder Skripte von Dritten und hat keine Formulare. Ausnahme Lernseiten (<code>lernen/</code>): Sie speichern den Lernfortschritt nur im eigenen Browser (localStorage); nichts davon wird an uns oder Dritte übertragen.</p>
<h2>Verantwortlich</h2><p>Siehe <a href="impressum.html">Impressum</a>.</p>
<h2>Hosting</h2><p>Die Seite wird über GitHub Pages (GitHub Inc., USA) ausgeliefert. Dabei verarbeitet GitHub technisch notwendige Daten wie die IP-Adresse. Rechtsgrundlage: Art. 6 Abs. 1 lit. f DSGVO. Hinweis des Betreibers: Ein Umzug zu einem Hoster in der EU ist geplant.</p>
<h2>E-Mail</h2><p>Wenn Sie uns schreiben, nutzen wir Ihre Angaben nur zur Beantwortung und löschen sie, wenn der Vorgang erledigt ist.</p>
<h2>Externe Links</h2><p>Links zu ffm.de oder Petitionsplattformen führen zu deren eigenen Datenschutzregeln.</p>
<h2>Ihre Rechte</h2><p>Auskunft, Berichtigung, Löschung, Einschränkung, Widerspruch und Beschwerde beim Hessischen Beauftragten für Datenschutz und Informationsfreiheit.</p>
""")

# ---------------------------------------------------------------- Lernen (E13)
# Übersicht wird gebaut; die Lernseiten selbst (lernen/*.html außer index) sind handgepflegt
# und dürfen als einzige Ausnahme Inline-JavaScript enthalten (kein CDN, keine Datenübertragung).
page("lernen/index.html", "Lernen", "Kostenlose Lernseiten für Deutsch – mit Erklärungen in der Muttersprache.", """
<p class="eyebrow">Lernen</p>
<h1>Deutsch lernen im Frankfurter Norden</h1>
<p class="lead">Kostenlose Übungsseiten fürs Handy. Ohne Anmeldung, in deinem Tempo.</p>
<div class="grid">
<article class="card"><h3><a href="deutsch-lao.html">Deutsch selbst lernen – für Lao-Sprechende</a></h3>
<p lang="lo">ຮຽນພາສາເຢຍລະມັນດ້ວຍຕົນເອງ</p>
<p>Dativ und Akkusativ in 10 Lektionen: Einstiegstest, Regeln auf Deutsch und Laotisch, Übungsfragen, Hör-Diktat, Lückentext, Abschlusstest.</p></article>
<article class="card"><h3><a href="deutsch-lao-mama.html">Teil 2: Deutsch im Alltag – für Mütter in Frankfurt</a></h3>
<p lang="lo">ພາສາເຢຍລະມັນໃນຊີວິດປະຈຳວັນ – ສຳລັບແມ່ໃນແຟຣັງເຟີດ</p>
<p>8 Lückentexte (B1): Schule, Kinderarzt, Elternabend, Markt, Familienkasse, U-Bahn, Spielplatz, E-Mail an die Lehrerin. Mit Tipps bei Fehlern, Fehler-Training, Abschlusstest und Druckansicht.</p></article>
</div>
<div class="callout"><h2>Gut zu wissen</h2><p>Die Lernseiten nutzen JavaScript für Übungen und Vorlesen. Dein Fortschritt bleibt nur in deinem Browser gespeichert und wird nicht übertragen. Die laotischen Texte werden noch von einer Muttersprachlerin gegengelesen.</p></div>
""")

page("404.html", "Seite nicht gefunden", "Seite nicht gefunden.", '<h1>Hier ist kein Stern.</h1><p><a class="btn btn-primary" href="index.html">Zur Startseite</a></p>')

# ------------------------------------------------------------------ Blog
def beitrag_html(b, pre):
    m = b["meta"]
    kopf = (f'<p class="small">{E(m["datum"])} · <a href="{pre}{obr_seite(m["ortsbezirk"])}">Ortsbezirk {E(m["ortsbezirk"])}</a>'
            + (" · " + E(", ".join(m["stadtteile"])) if isinstance(m.get("stadtteile"), list) else "")
            + "</p>")
    rumpf = beitraege.markdown(b["body"], link)
    zurueck = f'<p><a href="{pre}frankfurt/index.html">Alle Beiträge</a></p>' if b in VEROEFF else ""
    return f'<article class="beitrag">{kopf}\n{rumpf}\n</article>\n{zurueck}'


def beitrag_seite(b, out=ROOT):
    m = b["meta"]
    page("frankfurt/" + m["slug"] + ".html", m["titel"], m.get("beschreibung") or m["titel"],
         beitrag_html(b, "../"), out=out, aktiv="frankfurt.html")


BLOG = os.path.join(ROOT, "frankfurt")
soll = {"index.html"} if VEROEFF else set()
for b in VEROEFF:
    beitrag_seite(b)
    soll.add(b["meta"]["slug"] + ".html")
if VEROEFF:
    liste = "".join(card(f'<a href="{E(b["meta"]["slug"])}.html">{E(b["meta"]["titel"])}</a>',
                         f'<p class="small">{E(b["meta"]["datum"])}</p>') for b in VEROEFF)
    page("frankfurt/index.html", "Beiträge aus dem Frankfurter Norden",
         "Neutrale Beiträge über Stadt, Ortsbeirat 10 und Alltag im Frankfurter Norden.",
         f'<h1>Beiträge aus dem Frankfurter Norden</h1><div class="grid">{liste}</div>', aktiv="frankfurt.html")
# Veraltete Blog-Seiten entfernen (z. B. Beitrag zurück auf "entwurf")
if os.path.isdir(BLOG):
    for alt in glob.glob(os.path.join(BLOG, "*.html")):
        if os.path.basename(alt) not in soll:
            os.remove(alt)
    if not os.listdir(BLOG):
        os.rmdir(BLOG)

# ----------------------------------------------------------- Ortsbezirke
def obr_karte(o):
    t = naechster(lambda x: x["ortsbezirk"] == o["nr"])
    nxt = f'<p>Nächste Sitzung: <strong>{datum_text(t)}</strong></p>' if t else "<p>Keine geplanten Sitzungen im Kalender.</p>"
    status = '<span class="badge">betreut</span>' if o["status"] == "aktiv" else '<span class="small">noch ohne Betreuung</span>'
    return card(f'<a href="ortsbezirk-{o["nr"]}.html">{o["nr"]} · {E(o["name"])}</a>',
                f'<p class="small">{E(", ".join(o["stadtteile"]))}</p>{nxt}{status}')


page("ortsbezirke/index.html", "Ortsbezirke",
     "Alle 16 Frankfurter Ortsbezirke: Stadtteile, nächste Ortsbeiratssitzungen und Neues aus dem Stadtteil.",
     f"""<h1>Die 16 Ortsbezirke</h1>
<p class="lead">Frankfurt hat 16 Ortsbeiräte. Hier stehen die nächsten Sitzungen und Neues aus jedem Bezirk.</p>
<div class="grid">{"".join(obr_karte(o) for o in ORTSBEZIRKE)}</div>
{termin_hinweis()}
<h2>Stadtweit</h2>
<ul>{"".join(f'<li>{lab}: {datum_text(t)}</li>' for lab, t in [
    ("Stadtverordnetenversammlung", naechster(lambda x: x["typ"] == "stvv")),
    ("KAV – Kommunale Ausländerinnen- und Ausländervertretung", naechster(lambda x: x["typ"] == "kav"))] if t)}</ul>
<p class="small">Stadtteilzuordnung wird vor dem offiziellen Start noch einmal mit der Stadt abgeglichen.</p>
""", aktiv="ortsbezirke/index.html")

for o in ORTSBEZIRKE:
    nr = o["nr"]
    news = [b for b in VEROEFF if str(b["meta"].get("ortsbezirk")) == str(nr)]
    if news:
        news_html = '<div class="grid">' + "".join(card(
            f'<a href="../frankfurt/{E(b["meta"]["slug"])}.html">{E(b["meta"]["titel"])}</a>',
            f'<p class="small">{E(b["meta"]["datum"])}</p>') for b in news) + "</div>"
    elif o["status"] == "aktiv":
        news_html = '<p class="notice">Der nächste Beitrag aus diesem Ortsbezirk ist in Arbeit.</p>'
    else:
        news_html = ('<p class="notice">Für diesen Ortsbezirk suchen wir noch jemanden, der ihn betreut – '
                     'erst dann erscheinen hier eigene Beiträge.</p>')
    sitzungen = [t for t in KOMMEND if t["ortsbezirk"] == nr][:6]
    termin_html = ("<ol class=\"termine\">" + "".join(f"<li>{datum_text(t)}</li>" for t in sitzungen) + "</ol>"
                   if sitzungen else "<p>Keine geplanten Sitzungen im Kalender.</p>")
    page(obr_seite(nr), f"Ortsbezirk {nr} – {o['name']}",
         f"Ortsbezirk {nr} ({', '.join(o['stadtteile'])}): nächste Ortsbeiratssitzungen und Neues aus dem Stadtteil.",
         f"""<p class="eyebrow">Ortsbezirk {nr}</p>
<h1>{E(o["name"])}</h1>
<p class="lead">{E(", ".join(o["stadtteile"]))}</p>
<section aria-labelledby="h-news"><h2 id="h-news">Neues aus dem Ortsbezirk</h2>{news_html}</section>
<section aria-labelledby="h-termine"><h2 id="h-termine">Nächste Sitzungen des Ortsbeirats {nr}</h2>
{termin_html}
{termin_hinweis()}
<p>Die Sitzungen sind öffentlich. In der Bürgerfragestunde können Anwohnerinnen und Anwohner Fragen stellen.</p></section>
<p><a class="btn" href="index.html">Alle 16 Ortsbezirke</a></p>
""", aktiv="ortsbezirke/index.html")

if "--entwuerfe" in sys.argv:
    i = sys.argv.index("--entwuerfe")
    if i + 1 >= len(sys.argv):
        sys.exit("Aufruf: python3 tools/build.py --entwuerfe <ordner außerhalb des Repos>")
    vz = os.path.abspath(sys.argv[i + 1])
    if vz == ROOT or vz.startswith(ROOT + os.sep):
        sys.exit("Vorschau-Ordner muss außerhalb des Repos liegen (sonst landet der Entwurf im Commit).")
    for d in ("css", "fonts"):
        shutil.rmtree(os.path.join(vz, d), ignore_errors=True)
        shutil.copytree(os.path.join(ROOT, d), os.path.join(vz, d))
    for b in BEITRAEGE:
        beitrag_seite(b, out=vz)
    print(f"Vorschau: {len(BEITRAEGE)} Beitrag/Beiträge in {vz}/frankfurt/ (Navigation führt dort ins Leere)")

# -------------------------------------------------- Launch-Dateien
with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write("User-agent: *\n" + ("Allow: /\n" if LIVE else "Disallow: /\n"))
cname = os.path.join(ROOT, "CNAME")
if LIVE:
    with open(cname, "w") as f:
        f.write(SITE["domain"] + "\n")
elif os.path.exists(cname):
    os.remove(cname)
print(f"Gebaut: {len(NAV) + 3 + len(soll) + len(ORTSBEZIRKE)} Seiten · Modus: {'LIVE ' + SITE['domain'] if LIVE else 'Vorschau (noindex, kein CNAME)'}")
