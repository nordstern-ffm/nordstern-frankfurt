# Entscheidungen – Alternativen doppelt geprüft (Nutzen / Sicherheit / neuer Weg)

## E1 · Eine Marke, getrennte Verantwortung
**Gewählt:** Nordstern als Dach, betrieben von André / Copy & Code Agency. Verein, Partei und Vermittlung je in eigenem, gekennzeichnetem Bereich.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Alles als Vereinsseite | ein Absender | **Gemeinnützigkeit in Gefahr**: Ein gemeinnütziger Verein darf keine Partei fördern (§ 55 Abs. 1 Nr. 1 AO) und keine gewerbliche Vermittlung im Vordergrund haben | verworfen |
| Alles gemischt ohne Kennzeichnung | einfach | Glaubwürdigkeit leidet; Senioren, die Hilfe suchen, landen bei Parteiwerbung | verworfen |
| **Dach + Bereiche** | Reichweite wird geteilt, Risiken getrennt | Verein verlinkt nicht zurück auf Partei/Geschäft | **gewählt** – vor Gründung mit Steuerberatung bestätigen |

## E2 · Mängelmelder
**Gewählt:** Verlinken auf den städtischen Mängelmelder (ffm.de). Eigener Melder hätte Fotos mit Standort/Personen (DSGVO), Moderation und keine Weiterleitung an die Verwaltung bedeutet. **Neuer Weg später:** Monatlicher Blogbeitrag „Was im Norden gemeldet wurde“ – Mehrwert ohne Datenhaltung.

## E3 · Petitionen „220 Bürger“
**Gewählt:** Anliegen hier vorstellen und Fortschritt zeigen; Unterschriften extern (ffm.de-Ideenplattform oder openPetition). Eigene Unterschriftenliste = politische Meinung = besondere Kategorie (Art. 9 DSGVO) → zu riskant für eine statische Seite. Zahl 220 steht nur in `data/petitionen.json`.
**Zu prüfen:** Gilt für ffm.de-Ideen wirklich eine 200er-Schwelle? (laut Bürgerplattform-FEHLER-LOG unbestätigt). Für ein Bürgerbegehren gelten andere, viel höhere Quoren (HGO § 8b).

## E4 · Technik
**Gewählt:** Statisches HTML aus Python-Skript, kein JS, kein npm. Läuft in Termux.
| Alternative | Warum nicht |
| --- | --- |
| React (wie Frankfurt_FW-Wurzel) | Build-Kette, auf Termux fehleranfällig, für Infoseite unnötig |
| Tailwind-CDN | Besucher-IP an Dritte; laut eigenem FEHLER-LOG bereits einmal ersetzt |
| WordPress | Hosting-Kosten, Updates, Angriffsfläche |
| **Neuer Weg geprüft:** Eleventy/Hugo | sinnvoll ab ~30 Seiten/Blog; bis dahin reicht build.py |

## E5 · Hosting & Domain
**Gewählt (Start):** GitHub Pages + eigene Domain (kostenlos, HTTPS automatisch).
**Später:** EU-Hoster (z. B. ein deutscher Anbieter mit statischem Hosting), weil Pages in den USA liegt – steht ehrlich in der Datenschutzerklärung.

## E6 · Kontakt
**Gewählt:** `mailto:`-Link. Formspree (früher in copy-code-agency genutzt) = US-Dienst, Formulardaten außerhalb der EU → verworfen. Später EU-Formulardienst prüfen.

## E7 · Vermittlung – Risiken je Dienst (nicht öffentlich, steht in `data/dienste.json` → `pruefen`)
- Personal: private Arbeitsvermittlung ist erlaubnisfrei, Gewerbeanmeldung genügt; Zeitarbeit braucht AÜG-Erlaubnis, Vermittlungsgutscheine eine AZAV-Zulassung.
- Hotel: Interessenkonflikt mit eigenem Arbeitgeber vorab klären.
- Taxi: nur vermitteln, nicht befördern (Personenbeförderungsgesetz).
- Massage: nur Fachpersonal, keine Heilversprechen, strikt getrennt vom Projekt STAFF.
- Nähen: Status der Näherinnen klären (Scheinselbstständigkeit).
- Strom & Gas (TeleSon): vorbereitet, `aktiv: false`. Vertragsform (Handelsvertreter?), Provision offen nennen, Markenname nur mit Freigabe.
- Amway: vorbereitet, `aktiv: false`. Website-/Social-Media-Regeln von Amway für Geschäftspartner vorher lesen; keine Einkommens- oder Heilversprechen; Kennzeichnung „unabhängiger Geschäftspartner“.

## E8 · Bezahlen (Gumroad oder Stripe)
**Gewählt:** Gehostete Zahlungsseite per Link (Stripe Payment Link oder Gumroad) in `data/zahlung.json`. Kein eigener Checkout-Code, keine Kartendaten, kein Server.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Eigenes Stripe-Backend (wie mindful7777/stripe-api auf Vercel) | Abos, Kundenportal | Secrets, Webhooks, Server – dort schon Fehler „STRIPE_SECRET_KEY is not set“ | erst wenn Abos nötig |
| Gumroad | sofort startklar, übernimmt Steuern als Händler | höhere Gebühr, eher für digitale Produkte | gut für Vorlagen/E-Books |
| **Stripe Payment Link** | Dienstleistungen mit Festpreis, eigenes Branding | gehostet von Stripe | **gewählt für Agentur-Pakete** |
Wichtig: eigenes Stripe-Konto für die Agentur (nicht das von Gumroad verwaltete bangla-hilfe-Konto, nicht das mindful7777-Konto). Pakete erscheinen erst mit `aktiv`, Preis und Link. Preise legen André und Sam fest.

## E9 · Verknüpfung mit BanglaHilfe und wege-nach-frankfurt
**Gewählt:** Nordstern verlinkt beide auf Start („Nordstern-Familie“) und Frankfurt-Info; Links am 15.11.2026 erreichbar geprüft (HTTP 200). **Rückverlinkung** aus beiden Repos erst nach Domain-Start (sonst zeigen sie auf eine `noindex`-Vorschau). Repos bleiben eigenständig – kein Zusammenlegen, damit sie einzeln verkaufbar bleiben (Repo-Verkauf).

## E10 · Bildrechte technisch erzwingen (Phase 2, Aufgabe 1)
**Gewählt:** Doppelte Sperre. `build.py` bindet Bilder nur über `bild(datei)` ein und bricht ab, wenn `data/bilder.json` keinen Eintrag hat. `check.py` prüft zusätzlich jede Datei unter `img/` und jedes `<img src>` in allen HTML-Seiten auf einen vollständigen Eintrag (9 Pflichtfelder, Datum JJJJ-MM-TT, https-Links, Datei vorhanden, Alt-Text, kein externes Bild). Beleg: `tools/test_check.py` (8 Fälle).
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Nur Prüfung in check.py | einfacher | Bild fällt erst nach dem Build auf | ergänzt, nicht ersetzt |
| Nur Bildnachweis-Seite, keine Unterschrift | ruhigere Optik | CC BY/BY-SA verlangt Nennung „in angemessener Weise“ – unter dem Bild ist der sichere Weg | verworfen |
| Bild-Links in `data/links.json` doppeln | eine Link-Liste | doppelte Pflege, Fehlerquelle | verworfen: `quelle_url`/`lizenz_url` aus `bilder.json` gelten mit `geprueft`-Datum als bestätigt |
Inline-SVGs (Stern, später Icons/Illustrationen) sind keine Dateien unter `img/`; ihre Herkunft wird in Aufgabe 2/7 über Lizenzdatei bzw. eigenen Eintrag nachgewiesen.

## E11 · Icon-System (Phase 2, Aufgabe 2)
**Gewählt:** Lucide v1.73.0 (ISC), nur 26 benötigte Symbole als `<symbol>` in `assets/icons.svg` (6,4 KB), eingebunden per `<svg><use href="assets/icons.svg#name"></use></svg>`. Lizenz in `assets/LICENSE-icons.txt`. Neue Icons über `tools/icons.py` (übernimmt aus Downloads nur Geometrie, keine Skripte/Links). Icon-Namen der Dienste stehen in `data/dienste.json` → `icon`.
| Alternative | Nutzen | Sicherheit / Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Tabler Icons (MIT) | größere Auswahl | gleichwertig; Lucide hat ruhigere Linien, passt zu Atkinson | verworfen |
| Icons inline in jede Seite kopieren | funktioniert auch per `file://` | jede Seite schwerer, kein Browser-Cache | verworfen – lokal ansehen nur über `python -m http.server` |
| Icon-Font | ein Abruf | schlecht für Screenreader, unscharf, Fremdformat | verworfen |
| Emoji | null Aufwand | je Gerät anders, auf alten Android-Geräten teils Kästchen | verworfen |
Barrierefreiheit: Icons neben Text sind Deko (`aria-hidden="true"`, `focusable="false"`); `icon(name, label)` setzt `role="img"` + `aria-label`, falls ein Icon einmal allein steht. `check.py` erzwingt das sowie Icon in jeder Karte und jedem Menüpunkt.

## E12 · Kennzahlen (Phase 2, Aufgabe 3)
**Gewählt:** `data/zahlen.json` mit Wert, Text, Quelle, `link` (Schlüssel in `links.json`), wörtlicher Fundstelle, Stand und Prüfdatum. Kacheln über `kacheln([...])` in build.py; jede zeigt „Quelle · Stand“. Start: Einwohner Preungesheim, Einwohner Frankfurt, Entlastungsbetrag. Nachbarschaft: Preungesheim, Entlastungsbetrag.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Quell-URL direkt in zahlen.json | eine Datei | zweite Link-Liste neben links.json | verworfen – ein Ort für Links |
| Einwohnerzahl Ende 2024 (15.770) | im UX-Konzept vorgesehen | nur über Aggregator auffindbar, älter | verworfen – 15.896 (Ende 2025) direkt von der Stadt |
| „16 Ortsbeiräte“ als dritte Kachel | thematisch passend | Primärquelle nicht abrufbar (frankfurt.de 403) | in docs/OFFEN.md |
Wortlaut eng an der Quelle: „Einwohnerinnen und Einwohner“ (Statistik) und „bis 131 €“ (Gesetz: „bis zu 131 Euro monatlich“). Kein Hinweis, dass Nachbarschaftshilfe über den Entlastungsbetrag abgerechnet werden kann – das setzt eine Anerkennung nach Landesrecht voraus und ist nicht belegt.
Quellen-Links in `links.json` am 15.11.2026 per Abruf mit Inhaltsprüfung bestätigt (nicht im Browser des Nutzers) – vor Launch einmal im Browser öffnen.
