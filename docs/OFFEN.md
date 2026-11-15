# Offene Punkte – unbelegt, darum nicht (oder noch nicht belegt) auf der Seite

Regel (CLAUDE-CODE-AUFTRAG.md, Punkt 4): Jede Zahl, Rechtsaussage und jeder Link braucht Primärquelle + Datum. Was hier steht, ist noch nicht belegt.

## Zahlen
| Punkt | Stand | Was fehlt |
| --- | --- | --- |
| „15.770 Einwohner Preungesheim“ (Beispiel in UX-KONZEPT) | **nicht verwendet** | Wert 31.12.2024, nur über citypopulation.de (Aggregator) gefunden. Auf der Seite steht stattdessen 15.896 (Ende 2025) direkt aus statistik.aktuell 04/2026 der Stadt. |
| Einwohner Ortsbezirk 10 (Nord-Ost) | offen | Keine amtliche Summe gefunden; selbst addieren nur mit Zuordnung der Stadtteile laut Stadt Frankfurt (kommt in Aufgabe 6). |
| Anteil Menschen ab 65 in Preungesheim | offen | Wäre für die Zielgruppe stark; in statistik.aktuell 04/2026 nur stadtweit (Ausgabe 04/2024: 15,8 % stadtweit, Stand 31.12.2023). Stadtteilwert im STATISTIK.ATLAS suchen. |

## Bestehende Aussagen ohne verlinkte Primärquelle (schon vor Phase 2 auf der Seite)
| Seite | Aussage | Was fehlt |
| --- | --- | --- |
| frankfurt.html | „Frankfurt hat 16 Ortsbeiräte“, „Preungesheim gehört zum Ortsbezirk 10“ | frankfurt.de blockt Skript-Abrufe (403) → im Browser prüfen und als Link in `links.json` eintragen. |
| frankfurt.html | Kommunalwahl „zuletzt am 15. März 2026, für fünf Jahre“ | Quelle: Wahlamt Frankfurt / HKWG § 2 im Browser prüfen. |

## Barrierefreiheit
Erledigt am 15.11.2026: Hellmodus-Kontrast von `--gold-soft` (siehe FEHLER-LOG, Aufgabe 3).

## Sicherheit / Datenschutz – Entscheidung André
**Öffentliches Repo + GitHub Pages veröffentlichen alles.** Abrufbar sind u. a. `data/dienste.json` (Feld `pruefen`: Arbeitgeber-Konflikt Hotel, Projekt STAFF, Status der Näherinnen, TeleSon-Vertragsform), `docs/*` (Vornamen möglicher Übersetzer in TODO-MASTER und FESTKALENDER-RECHERCHE), `FEHLER-LOG.md`, `CLAUDE.md`. Auch die Git-Historie bleibt öffentlich. Geprüft: keine Passwörter, Schlüssel, Telefonnummern in Dateien oder Historie.
Optionen:
1. Interne Notizen (`pruefen`, Personen-Vornamen) aus dem Repo nehmen → lokale Datei, per `.gitignore` ausgeschlossen. Bisheriger Stand bleibt in der Historie sichtbar.
2. Repo privat stellen – GitHub Pages aus privatem Repo braucht einen bezahlten Plan; ohne ihn geht die Vorschau offline.
3. Bei Umzug zum EU-Hoster (TODO P1) nur den Build-Ordner hochladen statt des ganzen Repos.
Empfehlung Claude Code: 1 sofort (Vornamen + `pruefen` entfernen), 3 beim Hoster-Umzug.
