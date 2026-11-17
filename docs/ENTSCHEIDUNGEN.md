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

## E13 · Lernseiten mit JavaScript als Ausnahme (`lernen/`) – entschieden 18.11.2026 (Nutzer)
**Gewählt:** Neuer Bereich `lernen/` (Menüpunkt „Lernen“). `lernen/index.html` wird von `build.py` gebaut (ohne JS). Die Lernseiten selbst (`lernen/deutsch-lao.html`, Quelle: Claude-Artefakt „Deutsch selbst lernen – für Lao-Sprechende“) sind handgepflegt und dürfen **als einzige Ausnahme** Inline-JavaScript enthalten. `check.py` schlägt Alarm, sobald `<script` irgendwo sonst steht. Schriften lokal (Noto Sans Lao neu, SIL OFL), kein CDN, Fortschritt nur im localStorage des Browsers, Hinweis in Datenschutz und Seitenfuß.
| Alternative | Nutzen | Sicherheit / Regeln | Ergebnis |
| --- | --- | --- | --- |
| **A · Ausnahme `lernen/` mit Inline-JS** | Quiz, Fehlerwiederholung, Vorlesen und Fortschritt bleiben erhalten | keine Fremdabrufe, keine Daten verlassen das Gerät; Ausnahme technisch auf einen Ordner begrenzt | **gewählt** |
| B · statisch ohne JS (`<details>` mit Lösungen) | erfüllt Regel „kein JS“ vollständig | kein Zähler, keine Selbstkontrolle, kein Vorlesen → Lernwert deutlich geringer | Rückfall, falls JS je Probleme macht |
| C · nur auf das Claude-Artefakt verlinken | null Aufwand | Inhalt liegt außerhalb des Repos, nicht verkaufbar/versionierbar, fremde Plattform | verworfen |
**Offen:** Laotische Texte von einer Muttersprachlerin gegenlesen lassen. **Neuer Weg später:** Lerninhalte als JSON in `data/lernen/` und eine gemeinsame Lern-Engine für Lao, Französisch, Englisch (Folgeauftrag „Fortsetzung“).
