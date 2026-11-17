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

## E7 · Vermittlung – rechtliche Prüfung je Dienst vor dem Start
Je Dienst wird vor `aktiv`/Kontaktfreigabe geprüft: Gewerbeanmeldung und Erlaubnispflichten, Verträge mit Partnern, Nachweise der Fachkräfte, Status der Mitwirkenden, Kennzeichnungspflichten. Wir vermitteln nur, wir befördern, beherbergen und behandeln nicht selbst. Die einzelnen Prüfpunkte sind intern (nicht im öffentlichen Repo, siehe E19).

## E8 · Bezahlen (Gumroad oder Stripe)
**Gewählt:** Gehostete Zahlungsseite per Link (Stripe Payment Link oder Gumroad) in `data/zahlung.json`. Kein eigener Checkout-Code, keine Kartendaten, kein Server.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Eigenes Stripe-Backend (wie in einem früheren Projekt auf Vercel) | Abos, Kundenportal | Secrets, Webhooks, Server – dort schon Fehler „STRIPE_SECRET_KEY is not set“ | erst wenn Abos nötig |
| Gumroad | sofort startklar, übernimmt Steuern als Händler | höhere Gebühr, eher für digitale Produkte | gut für Vorlagen/E-Books |
| **Stripe Payment Link** | Dienstleistungen mit Festpreis, eigenes Branding | gehostet von Stripe | **gewählt für Agentur-Pakete** |
Wichtig: eigenes Stripe-Konto für die Agentur (getrennt von allen anderen Projekt-Konten). Pakete erscheinen erst mit `aktiv`, Preis und Link. Preise legen André und die Agentur-Partnerin bzw. der Agentur-Partner fest.

## E9 · Verknüpfung mit BanglaHilfe und wege-nach-frankfurt
**Gewählt:** Nordstern verlinkt beide auf Start („Nordstern-Familie“) und Frankfurt-Info; Links am 15.11.2026 erreichbar geprüft (HTTP 200). **Rückverlinkung** aus beiden Repos erst nach Domain-Start (sonst zeigen sie auf eine `noindex`-Vorschau). Repos bleiben eigenständig – kein Zusammenlegen, damit sie einzeln verkaufbar bleiben (Repo-Verkauf).

## E10 · Blog-Build für `data/beitraege/*.md` – entschieden 17.11.2026: Variante 1 (Nutzer)
**Gewählt:** eigener Mini-Parser in `tools/beitraege.py`, genutzt von `build.py` und `check.py`. Nur `status: veroeffentlicht` erzeugt `frankfurt/<slug>.html` (+ Übersicht `frankfurt/index.html`); Entwürfe werden nie gebaut oder verlinkt. Pflichtfeld `ortsbezirk` (1–16) im Frontmatter. Links im Text nur als `[[link:schluessel]]` aus `data/links.json`. Vorschau: `python3 tools/build.py --entwuerfe <ordner außerhalb des Repos>`.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| (1) Eigener Mini-Parser in `build.py` (Frontmatter, Überschriften, Absätze, Listen, Fett/Kursiv, Links nur über Schlüssel aus `data/links.json`) | keine Abhängigkeit, läuft unverändert in Termux und Git Bash | volle Kontrolle über erlaubtes HTML, kein JS/CDN | **Empfehlung** |
| (2) Python-Paket `markdown` | vollständiges Markdown, wenig eigener Code | neue Abhängigkeit (auch in Termux zu installieren), rohes HTML im Markdown möglich → filtern | Rückfall, falls (1) zu aufwendig wird |
| (3) Beiträge als JSON in `data/` wie die übrigen Inhalte | einheitlich mit dem Rest, kein Parser | lange Texte in JSON schwer zu schreiben und zu prüfen | verworfen für Fließtext |

## E11 · Umfang: Variante A, entschieden 17.11.2026 (Nutzer)
**Gewählt:** Start mit Ortsbezirk 10 (Berkersheim, Bonames, Eckenheim, Frankfurter Berg, Preungesheim). Die Struktur (Pflichtfeld `ortsbezirk` 1–16 in Beiträgen, Tabelle in `docs/BETREUUNG.md`) ist für alle 16 Ortsbezirke angelegt. Weitere Bezirke gehen erst online, wenn jemand sie dauerhaft betreut.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| **A · OBR 10 zuerst, Struktur für alle 16** | Qualität dort, wo wir uns auskennen; Ausbau ohne Umbau | jede Angabe hat eine verantwortliche Person, die Quellen prüft | **gewählt** |
| B · ganze Stadt sofort | große Reichweite ab Tag 1 | 16 Bezirke ohne Betreuung → veraltete Termine, ungeprüfte Angaben, Glaubwürdigkeit leidet; Rechercheaufwand vervielfacht sich, solange PARLIS/frankfurt.de in der Cloud-Umgebung gesperrt sind | verworfen |
| C · nur Frankfurter Norden, keine Struktur für mehr | am einfachsten | spätere Erweiterung braucht Umbau (Datenmodell, Navigation); Name „Frankfurt“ verspricht mehr, als die Seite hält | verworfen |

## E12 · Termine, 16 Ortsbezirksseiten und Kalender-Laufband – entschieden 17.11.2026 (Nutzer)
**Gewählt:** Termine aus dem PARLIS-Kalender (.ics, vom Nutzer geladen) → `tools/ics_import.py` → `data/termine.json`. Jede der 16 Ortsbezirke bekommt eine Seite mit „Neues“ (veröffentlichte Beiträge mit passendem `ortsbezirk`) und den nächsten Sitzungen. Startseite oben: Laufband „Termine & Neues“ mit 5 Einträgen, **ohne JavaScript** (CSS-Animation).
Verhältnis zu E11 (Variante A): Die 16 Seiten sind die angekündigte Struktur. Ohne Betreuung zeigen sie nur amtliche Termine und den Hinweis „noch ohne Betreuung“, keine eigenen Inhalte.
| Alternative | Nutzen | Sicherheit / Regeln | Ergebnis |
| --- | --- | --- | --- |
| **CSS-Laufband mit Pause** (Hover, Tastaturfokus, Schalter „Laufband anhalten“; bei `prefers-reduced-motion` ruhige Liste) | rotiert wie gewünscht, kein JS | erfüllt WCAG 2.2.2 (anhaltbar), Tastatur erreicht bei Fokus alle Einträge | **gewählt** |
| JavaScript-Karussell | flexibler | Muss-Regel „kein JavaScript“ | verworfen |
| Nur statische Liste | am einfachsten, am barrierefreiesten | erfüllt nicht den Wunsch „rotierend“ | bleibt als Rückfall bei reduzierter Bewegung |
| PARLIS-Kalender einbetten (iframe) | immer aktuell | Fremdabruf, Datenweitergabe an Dritte; frankfurt.de blockt ohnehin | verworfen |
**Grenze:** „Nächste Termine“ werden beim Bauen berechnet (Stichtag = Build-Datum, reproduzierbar mit `NORDSTERN_HEUTE=JJJJ-MM-TT`). Ohne neuen Build veralten sie → mindestens wöchentlich bauen; `check.py` warnt, wenn alle Termine vorbei sind. **Neuer Weg später:** GitHub Action mit wöchentlichem Build (Entscheidung offen).
## E13 · Bildrechte technisch erzwingen (Phase 2, Aufgabe 1)
**Gewählt:** Doppelte Sperre. `build.py` bindet Bilder nur über `bild(datei)` ein und bricht ab, wenn `data/bilder.json` keinen Eintrag hat. `check.py` prüft zusätzlich jede Datei unter `img/` und jedes `<img src>` in allen HTML-Seiten auf einen vollständigen Eintrag (9 Pflichtfelder, Datum JJJJ-MM-TT, https-Links, Datei vorhanden, Alt-Text, kein externes Bild). Beleg: `tools/test_check.py` (8 Fälle).
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Nur Prüfung in check.py | einfacher | Bild fällt erst nach dem Build auf | ergänzt, nicht ersetzt |
| Nur Bildnachweis-Seite, keine Unterschrift | ruhigere Optik | CC BY/BY-SA verlangt Nennung „in angemessener Weise“ – unter dem Bild ist der sichere Weg | verworfen |
| Bild-Links in `data/links.json` doppeln | eine Link-Liste | doppelte Pflege, Fehlerquelle | verworfen: `quelle_url`/`lizenz_url` aus `bilder.json` gelten mit `geprueft`-Datum als bestätigt |
Inline-SVGs (Stern, später Icons/Illustrationen) sind keine Dateien unter `img/`; ihre Herkunft wird in Aufgabe 2/7 über Lizenzdatei bzw. eigenen Eintrag nachgewiesen.

## E14 · Icon-System (Phase 2, Aufgabe 2)
**Gewählt:** Lucide v1.73.0 (ISC), nur 26 benötigte Symbole als `<symbol>` in `assets/icons.svg` (6,4 KB), eingebunden per `<svg><use href="assets/icons.svg#name"></use></svg>`. Lizenz in `assets/LICENSE-icons.txt`. Neue Icons über `tools/icons.py` (übernimmt aus Downloads nur Geometrie, keine Skripte/Links). Icon-Namen der Dienste stehen in `data/dienste.json` → `icon`.
| Alternative | Nutzen | Sicherheit / Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Tabler Icons (MIT) | größere Auswahl | gleichwertig; Lucide hat ruhigere Linien, passt zu Atkinson | verworfen |
| Icons inline in jede Seite kopieren | funktioniert auch per `file://` | jede Seite schwerer, kein Browser-Cache | verworfen – lokal ansehen nur über `python -m http.server` |
| Icon-Font | ein Abruf | schlecht für Screenreader, unscharf, Fremdformat | verworfen |
| Emoji | null Aufwand | je Gerät anders, auf alten Android-Geräten teils Kästchen | verworfen |
Barrierefreiheit: Icons neben Text sind Deko (`aria-hidden="true"`, `focusable="false"`); `icon(name, label)` setzt `role="img"` + `aria-label`, falls ein Icon einmal allein steht. `check.py` erzwingt das sowie Icon in jeder Karte und jedem Menüpunkt.

## E15 · Lokale Skripte für Lern- und Spiel-Elemente (André, 15.11.2026: JA)
**Ursprung (Nachtrag 15.11.2026):** Lückentext-Sofortprüfung im Sprachraum – eine kleine lokale Datei `assets/uebung.js`, nur auf Sprachraum-Seiten, ohne Bibliotheken, ohne Datenspeicherung; Seite funktioniert vollständig ohne Skript (Lösungen per `<details>`). Alternative „nur `<details>`“ verworfen: weniger motivierend. (Nummernverlauf: im Phase-3b-Dokument zunächst „E11“, im Nachtrag „E12“; seit dem Zusammenführen mit `main` am 17.11.2026 **E15**, weil E10–E12 dort vom Nutzer vergeben wurden.)
**Erweitert (André, 15.11.2026: JA):** Die lokale Skript-Regel gilt für alle Lern- und Spiel-Elemente: Lückentext-Sofortprüfung, Quiz („Wie gut kennst du Frankfurt?“, „Welche Sprache ist das?“), Wort-Memory und Zuordnen.
**Bedingungen (unverändert):** lokale Dateien unter `assets/`, keine Bibliotheken, kein CDN, nichts wird gespeichert (kein `localStorage`, keine Cookies), jede Seite funktioniert vollständig ohne Skript (Lösungen per `<details>`).
**Prüfung:** `check.py` prüft: Skripte nur aus `assets/`, nur auf Sprachraum- und Quiz-Seiten. Stand heute verbietet `check.py` noch jedes `<script src>` (strenger als E15). Die Freigabe samt Prüfung (Liste der erlaubten Seiten, Verbot von `localStorage`/`document.cookie`, Testfälle) wird mit der ersten Sprachraum- bzw. Quiz-Seite gebaut (P3/W4), weil die Seitennamen erst dann feststehen.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Nur `<details>` ohne Skript | null Risiko | weniger motivierend, keine Sofortrückmeldung | verworfen (André) |
| Lern-Bibliothek / Quiz-Dienst | schneller gebaut | Fremdabruf, Tracking-Risiko, gegen E4 | verworfen |
| **Kleine lokale Skripte mit Fallback** | Sofortrückmeldung, kein Datenabfluss | Seite bleibt ohne Skript vollständig | **gewählt** |

## E16 · Kennzahlen (Phase 2, Aufgabe 3)
**Gewählt:** `data/zahlen.json` mit Wert, Text, Quelle, `link` (Schlüssel in `links.json`), wörtlicher Fundstelle, Stand und Prüfdatum. Kacheln über `kacheln([...])` in build.py; jede zeigt „Quelle · Stand“. Start: Einwohner Preungesheim, Einwohner Frankfurt, Entlastungsbetrag. Nachbarschaft: Preungesheim, Entlastungsbetrag.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Quell-URL direkt in zahlen.json | eine Datei | zweite Link-Liste neben links.json | verworfen – ein Ort für Links |
| Einwohnerzahl Ende 2024 (15.770) | im UX-Konzept vorgesehen | nur über Aggregator auffindbar, älter | verworfen – 15.896 (Ende 2025) direkt von der Stadt |
| „16 Ortsbeiräte“ als dritte Kachel | thematisch passend | Primärquelle nicht abrufbar (frankfurt.de 403) | in docs/OFFEN.md |
Wortlaut eng an der Quelle: „Einwohnerinnen und Einwohner“ (Statistik) und „bis 131 €“ (Gesetz: „bis zu 131 Euro monatlich“). Kein Hinweis, dass Nachbarschaftshilfe über den Entlastungsbetrag abgerechnet werden kann – das setzt eine Anerkennung nach Landesrecht voraus und ist nicht belegt.
Quellen-Links in `links.json` am 15.11.2026 per Abruf mit Inhaltsprüfung bestätigt (nicht im Browser des Nutzers) – vor Launch einmal im Browser öffnen.

## E17 · Ablauf-Diagramme und Zeitleiste (Phase 2, Aufgabe 4)
**Gewählt:** `steps(key)` und `timeline()` in build.py, Inhalte in `data/ablaeufe.json`. Beide als `<ol role="list">`: Die Liste trägt Reihenfolge und Anzahl für Screenreader; Schrittnummer (`aria-hidden`) und Icons sind nur visuell. Zeitleiste ohne Datum, solange keins bestätigt ist; Status als Text („in Arbeit“, „geplant“) plus Punktform (voll/halb/leer), nicht nur Farbe. `{ziel}` holt die 220 aus `petitionen.json` (E3).
| Alternative | Nutzen | Sicherheit / Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Diagramm als SVG-Grafik | freiere Gestaltung | Text in Grafik, schlecht skalierbar, extra Text-Alternative nötig | verworfen |
| CSS-Zähler statt Nummer im HTML | weniger Markup | manche Screenreader lesen `::before`-Inhalt doppelt | verworfen |
| Zeitleiste mit geschätzten Monaten | lebendiger | erfundene Termine (Auftrag Regel 4) | verworfen |
Nachbarschafts-Ablauf ist ausdrücklich als „geplant“ gekennzeichnet (Verein in Gründung).

## E18 · Content-Security-Policy, Referrer-Policy und Sicherheitsprüfung über das ganze Repo (15.11.2026)
**Gewählt:** Jede Hauptseite trägt `<meta http-equiv="Content-Security-Policy">` mit `default-src 'self'; script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'` und `<meta name="referrer" content="no-referrer">`. Im Browser geprüft: alle Abrufe nur eigene Domain, keine Verstöße im Normalbetrieb, eingeschleustes Inline-Skript wird blockiert. `check.py` prüft Sicherheitsregeln jetzt in **allen** HTML/CSS-Dateien (auch `docs/mockups/`), weil GitHub Pages mit `.nojekyll` das ganze Repo veröffentlicht.
| Alternative | Nutzen | Sicherheit / Nachteil | Ergebnis |
| --- | --- | --- | --- |
| CSP als HTTP-Header | auch `frame-ancestors` (Schutz vor Einbettung) möglich | GitHub Pages erlaubt keine eigenen Header | später beim EU-Hoster (TODO P1) |
| Keine CSP, nur check.py | einfacher | schützt nicht, falls doch einmal Fremdcode ins HTML gerät | verworfen – zwei Sperren |
| `style-src 'self'` ohne `'unsafe-inline'` | strenger | Fortschrittsbalken der Petitionen nutzt `style="width:…"` | `'unsafe-inline'` nur für Stile; ohne Skripte geringes Risiko |
| Referrer `strict-origin-when-cross-origin` (Standard) | Zielseiten sehen Herkunft | verrät besuchte Seite an ffm.de usw. | `no-referrer` gewählt (Datensparsamkeit) |
**Bei E15 (Lern-Skripte) beachten:** dort `script-src 'self'` nur auf den freigegebenen Seiten, check.py-Liste anpassen.

## E19 · Interna nicht ins öffentliche Repo (15.11.2026)
**Gewählt:** Repo und GitHub Pages sind öffentlich. Interne Prüfnotizen, Vornamen Dritter, das Repo-Audit und Listen privater/fremder Projekte liegen nur lokal in `docs/intern/` und `data/intern/` (per `.gitignore` ausgeschlossen). `check.py` meldet interne Felder (`pruefen`, `intern`) in `data/*.json` und fehlende `.gitignore`-Einträge.
| Alternative | Nutzen | Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Repo privat | alles verborgen | Pages aus privatem Repo nur mit bezahltem Plan | offen (André) |
| Zweites privates Repo für Interna | versioniert, gesichert | mehr Pflege, zweites Konto-Recht | später möglich |
| **Lokale, ignorierte Ordner** | sofort wirksam, kein Aufwand | keine Sicherung durch Git → selbst sichern (TODO P3 „Sicherung“) | **gewählt** |
Die Git-Historie enthält die alten Fassungen weiterhin (siehe `docs/OFFEN.md`).

## E20 · Blog-Reiter mit Rubriken Stadtpolitik, Politik, KI & Stadt (André, 15.11.2026)
**Gewählt:** Eigener Menüpunkt „Blog“ (`blog.html`, Daten `data/blog.json`). Stadtpolitik bündelt „Aus dem Römer“, „Aus dem Ortsbeirat 10“, „Bürgerdialog“ (REDAKTION.md); Politik = Land/Bund/Europa aus Frankfurter Sicht; KI & Stadt = Beispiele aus anderen Städten nach festem Muster (Beispiel mit Quelle · Funktionsweise · Kosten laut Quelle · Stand in Frankfurt · was Frankfurt bräuchte). Alle Rubriken parteiunabhängig; Parteipositionen nur unter Standpunkte. Rubrik-Chips als Sprungmarken (ohne JS). Geplante Themen stehen als Fragen ohne Tatsachenbehauptung da.
**Navigation:** Damit es bei höchstens 7 Hauptpunkten bleibt (R2), ist „Standpunkte“ in den Footer gewandert (deutlich als „gekennzeichneter Partei-Bereich“). Alternative: „Für Vereine & Firmen“ in den Footer – verworfen, weil die neutralen Bereiche und das Angebot sichtbar bleiben sollen und der Partei-Bereich nicht im Hauptmenü neben dem Verein stehen muss. Umkehrbar in `NAV` (build.py).

## E21 · Blog-Beiträge als Markdown, Seiten in Unterordnern (R1, schlanke Fassung, 15.11.2026)
**Abgelöst am 17.11.2026 durch E10** (Nutzerentscheidung auf `main`): Beiträge liegen unter `frankfurt/<slug>.html`, Entwürfe werden nie gebaut. Aus E21 übernommen und in `tools/beitraege.py` ergänzt: `[[link:x|Text]]`, `[[seite:pfad|Text]]`, `[[bild:img/…]]` (Nachweis-Pflicht E13), Hinweiskasten `> `, optionale Kopf-Felder `rubrik`, `bild`, `beschreibung`; `links` wird als Quellenliste angezeigt. Der folgende Text beschreibt den alten Stand.
**Gewählt:** `data/beitraege/*.md` mit Kopf (titel, beschreibung, rubrik, slug, stand, freigegeben, bild, quellen) und kleinem Markdown; `tools/beitraege.py` (ohne Fremdpakete) wandelt um, build.py schreibt `/<rubrik>/<slug>/index.html`. `page()` setzt für Unterordner `../` vor alle relativen Links. Externe Links im Text nur als `[Text](link:schluessel)` aus `links.json` (bestätigt), sonst bricht der Build ab; HTML im Text ist verboten. Entwürfe (`freigegeben: nein`) zeigen einen Hinweis; check.py warnt, bei `--launch` Fehler.
| Alternative | Nutzen | Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Python-Paket `markdown` | vollständiges Markdown | Fremdpaket, auf Termux zusätzliche Installation, erlaubt Roh-HTML | verworfen |
| Beiträge als JSON | einfach zu prüfen | schlecht zu schreiben | verworfen |
| Flache Dateien `blog-slug.html` | keine `../`-Logik | widerspricht R1 (`/<rubrik>/<slug>/`), spätere URL-Änderung kostet Suchmaschinen-Ranking | verworfen |
Abweichung von REDAKTION.md: `quellen` als Komma-Liste von `links.json`-Schlüsseln statt YAML-Liste mit URL – so gibt es nur eine Link-Liste. JSON-LD (`Article`) folgt mit S2; dafür muss check.py `<script type="application/ld+json">` gezielt erlauben (wird nicht ausgeführt, CSP bleibt `script-src 'none'`).

## E22 · Schaubild „Wer entscheidet in Frankfurt?“ (Phase 2, Aufgabe 5)
**Gewählt:** Inline-SVG hochkant (viewBox 360 × 660, Schrift ab 390 px lesbar), Farben aus CSS-Variablen (hell/dunkel), `role="img"` mit Kurzbeschreibung + vollständige Tabelle als Text-Alternative. Inhalte in `data/schaubild.json`. Ersetzt die alten Karten „Stadtverordnetenversammlung“ und „Ortsbeiräte“, deren Angaben teils unbelegt waren.
**Belege:** HGO (Bürgerservice Hessenrecht, abgerufen 15.11.2026): § 9 Abs. 1/2 (oberstes Organ; Bezeichnungen Stadtverordnetenversammlung/Magistrat), § 38 Abs. 1 (93 bei 500 001–1 000 000 Einwohnern), § 39 (Direktwahl), § 82 Abs. 1/3 (Wahl und Vorschlagsrecht der Ortsbeiräte). Broschüre „Kommunalpolitik einfach erklärt“, Büro der StVV, Stand Mai 2025: 93 Mitglieder, 16 Ortsbeiräte mit 284 Mitgliedern, Wahlzeiten 5/6 Jahre, Stadträte von der StVV gewählt, Ortsbezirk 10 = Berkersheim, Bonames, Eckenheim, Frankfurter Berg, Preungesheim.
**Abweichungen von der Chat-Recherche:** Bezeichnungen stehen in **§ 9** HGO (nicht § 49). Keine Stadtrats-Zahlen im Schaubild – die Broschüre nennt an verschiedenen Stellen unterschiedliche Zahlen hauptamtlicher Mitglieder. Ausländerbeirat/KAV nicht im Schaubild: Die HGO lässt statt eines Ausländerbeirats auch eine Integrations-Kommission zu (§ 84 Satz 3); welche Form Frankfurt hat, ist noch nicht an einer Primärquelle geprüft.
| Alternative | Nutzen | Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Querformat-Schaubild | übersichtlich am Desktop | auf 390 px Schrift unter 10 px | verworfen |
| Nur Tabelle | barrierefrei | kein „Bild vor Text“ (UX-Prinzip 2) | ergänzt, nicht ersetzt |
| Grafik als Bilddatei | einfacher | Farben fix, kein Dunkelmodus, Text nicht durchsuchbar | verworfen |

## E23 · Suche ja, KI-Chat nein, Glossar viersprachig (André, 15.11.2026)
**Gewählt:** Lokale Seitensuche mit einfacher Interaktion im Repo-Stil (`/`, Live-Treffer, Pfeiltasten, Filter-Chips); E15 gilt damit auch für die Suche: Skript nur aus `assets/`, ohne Bibliothek, speichert nichts, CSP `script-src 'self'` nur auf den Seiten mit Suchfeld, ohne Skript A–Z-Verzeichnis. Kein KI-Chat. Glossar in Deutsch (Referenz), Englisch, Spanisch, Französisch; Übersetzungen nur mit Prüfvermerk.
| Alternative | Nutzen | Nachteil | Ergebnis |
| --- | --- | --- | --- |
| KI-Chat aus eigenen Inhalten | Fragen in Alltagssprache | Server, laufende Kosten, Art.-9-Daten, Vertrag mit KI-Anbieter | verworfen (André) |
| Suche über externe Suchmaschine | kein eigener Code | jede Suchanfrage geht an Dritte | verworfen |
| Nur A–Z-Verzeichnis | null Skript | langsam bei vielen Beiträgen | bleibt als Fallback |
Umsetzung nach Abschluss aller Inhaltsaufgaben (TODO-MASTER G1–G3).

## E24 · Zusammenführung ux-phase2 + main, Menüpunkt „Ortsbezirke & Blog“ (Nutzer, 17.11.2026)
**Gewählt:** Alles zusammenführen auf Basis `main`. E10–E12 (main) bleiben, ux-phase2-Entscheidungen heißen E13–E23. Ein Menüpunkt „Ortsbezirke & Blog“ (`ortsbezirke/index.html`): oben Blog mit Rubrik-Chips (E20), darunter die 16 Ortsbezirke (E11/E12). `blog.html` entfällt; `frankfurt/index.html` bleibt als „Alle Beiträge“. Standpunkte bleibt im Footer (E20) → 7 Menüpunkte (R2).
| Alternative | Nutzen | Nachteil | Ergebnis |
| --- | --- | --- | --- |
| Standpunkte in den Footer, Blog und Ortsbezirke getrennt | klare Trennung | 8 Menüpunkte | verworfen (Nutzer) |
| Agentur in den Footer | Partei-Bereich sichtbar | Angebot verschwindet aus dem Menü | verworfen (Nutzer) |
| **Ein Punkt „Ortsbezirke & Blog“** | Blog und Stadtteile gehören inhaltlich zusammen (Beiträge haben Pflichtfeld `ortsbezirk`) | längerer Menütext | **gewählt** |
