# Weltstadt · Lesbarkeit · Verweilen & Interaktion (Ergänzung 15.11.2026)

## 1 · Faktencheck „190 Nationen“
Die Stadt Frankfurt nennt für den 31.12.2023: **Menschen aus 179 Ländern** leben in Frankfurt, Ausländeranteil **31,7 %** (244.401 Personen mit Hauptwohnung).
Quelle: Stadt Frankfurt, Bürgeramt Statistik und Wahlen, *statistik.aktuell* 05/2024 – https://statistikportal.frankfurt.de/download/FSA/2024/FSA_2024_05_Ausländer_Ende2023.pdf
→ Auf der Seite **„Menschen aus 179 Ländern“ (Stand Ende 2023)** schreiben, nicht „190 Nationen“. Jährlich mit der neuesten Ausgabe aktualisieren (`data/zahlen.json`).
Hinweis: Staatsangehörigkeit ≠ gesprochene Sprache. Für Sprach-Artikel nie „X Menschen sprechen Y“ ohne Quelle behaupten.

## 2 · Lesbarkeit – automatisch prüfen (Ergänzung zur SEO-RICHTLINIE)
`tools/check.py` bekommt eine Lesbarkeitsprüfung für deutschen Fließtext (Warnungen, keine harten Fehler – Heuristik):
| Prüfung | Grenze | Gilt für |
| --- | --- | --- |
| Flesch-Lesbarkeit (deutsche Formel nach Amstad: 180 − Satzlänge − 58,5 × Silben je Wort) | ≥ 60 (Ratgeber), ≥ 70 („Kurz gesagt“, Sprachraum A1/A2) | `lang="de"` |
| Ø Satzlänge | ≤ 15 Wörter | alle deutschen Texte |
| Einzelsatz | Warnung ab 25 Wörtern | alle |
| Absatzlänge | Warnung ab 5 Sätzen | Beiträge |
| Abkürzungen/Fachwörter | beim ersten Vorkommen erklärt oder `<abbr title>` / Glossar-Link | alle |
| „Kurz gesagt“ | vorhanden, ≤ 3 Sätze | jeder Beitrag (Fehler, wenn fehlt) |
Ausgabe als Liste „Seite · Wert · schwierigster Satz“, damit André gezielt kürzen kann.
Andere Sprachen: keine automatische Formel → **Muttersprachler-Prüfung Pflicht** (Feld `geprueft_von` im Beitragskopf, ohne Kontaktdaten).
Leichte Sprache (geregelte Form) nur mit Prüfung durch die Zielgruppe anbieten; bis dahin „Einfache Sprache“ nennen.

## 3 · Rubrik „Frankfurt spricht“ – die Welt in der Stadt
Ein Beitrag pro Sprache, Reihenfolge nach den größten Herkunftsgruppen laut Stadtstatistik, dazu die Sprachen unserer Familie (Bangla, Tigrinya, Thai, Lao).
**Vorlage je Sprache:**
1. „Kurz gesagt“: wo die Sprache gesprochen wird, eine überraschende Tatsache (mit Quelle)
2. 5 Wörter für den Frankfurter Alltag (z. B. Hallo, Danke, Nachbar, Willkommen, Guten Appetit) mit Umschrift + Audio (eigene Aufnahme, Sprecher-Einwilligung)
3. Ein Sprichwort mit Übersetzung und Bedeutung
4. Ein Fest (Verknüpfung zu `data/kultur.json`)
5. Ein Frankfurt-Bezug (Verein, Gemeinde, Kulturzentrum – nur Organisationen, Link bestätigt)
6. Bild mit Nachweis (`data/bilder.json`) – Schrift/Alphabet als eigene SVG-Grafik ist oft besser als ein Foto
7. Weiterlesen: Sprachraum-Lektion, passender Ratgeber
**Regeln:** feiernd und neugierig, keine Klischees, Muttersprachler prüft, Humor nur über Sprache/Missverständnisse, nie über Menschen.

## 4 · Verweilen – entspannte Atmosphäre
- Ruhige Gestaltung: viel Weißraum, langsame dezente Bewegung (abschaltbar), warme Gold-Akzente, kein Pop-up, kein Cookie-Banner (weil keine Cookies).
- **Fortsetzungsgeschichten** mit Nisha, Rashed und neuen Figuren aus aller Welt (Sprachraum + Frankfurt-Alltag) → Grund zum Wiederkommen.
- „Kurz durchatmen“ auch als Audio (60 Sek., eigene Stimme).
- Lesezeit und „Weiter, wenn du magst“-Hinweise statt Druck.
- Druckbare Extras: Frankfurt-Ausmalbilder (eigene SVG), Wortkarten, Postkarten „Ei Gude in 10 Sprachen“.

## 5 · Interaktion – ohne Tracking, ohne Konten
| Element | Technik | Datenschutz |
| --- | --- | --- |
| Quiz „Wie gut kennst du Frankfurt?“ (aus `Frankfurt_FW/…/quiz.json`) und „Welche Sprache ist das?“ | lokales Skript wie E12 (gleiche Datei-Regeln) | nichts gespeichert |
| Wort-Memory / Zuordnen im Sprachraum | lokales Skript | nichts gespeichert |
| „Dein Wort für Frankfurt“ – Leser schicken ein Wort aus ihrer Sprache | `mailto:` mit vorbereitetem Betreff | Veröffentlichung nur mit ausdrücklicher Zustimmung, Vorname optional |
| Leserbriefe statt Kommentarspalte | E-Mail, kuratiert | keine Moderationshaftung für Kommentare |
| Sprachcafé / Spaziergänge | Termine (offline treffen) | — |
| Newsletter (später) | EU-Anbieter, Double-Opt-in | eigene Datenschutz-Ergänzung |
Für Quiz/Memory gilt eine **neue Entscheidung (E-neu)**: E12 erweitern auf „Lern- und Spiel-Elemente“, gleiche Bedingungen (lokal, ohne Bibliotheken, ohne Speicherung, funktioniert ohne JS mit Lösungsansicht). André entscheidet.

## Aufgaben für Claude Code
| # | Aufgabe | Fertig, wenn |
| --- | --- | --- |
| W1 | Lesbarkeitsprüfung (Abschnitt 2) in check.py + Tests (leichter Text besteht, Schachtelsatz warnt) | Bericht pro Seite |
| W2 | `data/zahlen.json`: „179 Länder · 31,7 % (Ende 2023)“ mit Quelle als Kennzahl-Kachel auf Start und Frankfurt-Info | Quelle sichtbar |
| W3 | Rubrik „Frankfurt spricht“ mit Vorlage, 1 Beispielbeitrag als Entwurf (nicht veröffentlicht, `entwurf: true`) | Muttersprachler-Feld vorhanden |
| W4 | Quiz-Baustein aus `quiz.json` (nach Andrés Entscheidung) | funktioniert ohne JS mit Lösungen |
| W5 | „Dein Wort für Frankfurt“ (mailto-Vorlage + Zustimmungstext) | Datenschutzerklärung ergänzt |
| W6 | Druck-Extras (Ausmalbild Skyline, Postkarte „Ei Gude“) als eigene SVG | in bilder.json als „eigen“ nachgewiesen |
