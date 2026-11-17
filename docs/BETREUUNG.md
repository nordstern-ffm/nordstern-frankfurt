# Betreuung der Ortsbezirke

Umfang laut `docs/ENTSCHEIDUNGEN.md`, Eintrag „Umfang: Variante A“: Start mit Ortsbezirk 10, Struktur für alle 16. Ein Ortsbezirk wird erst **aktiv** (Beiträge mit diesem `ortsbezirk` werden veröffentlicht), wenn er eine Betreuung hat.

Stadtteilzuordnung vor Veröffentlichung auf frankfurt.de prüfen (frankfurt.de blockt Zugriffe aus der Cloud-Umgebung).

Die Webseite liest die Bezirke aus `data/ortsbezirke.json` – Änderungen an Betreuung/Status dort **und** in dieser Tabelle eintragen. Jeder Bezirk hat eine eigene Seite `ortsbezirke/ortsbezirk-<Nr>.html` mit Sitzungsterminen (aus PARLIS) und Beiträgen mit passendem `ortsbezirk`.

| Nr. | Ortsbezirk | Stadtteile | Betreuung | Status | Rhythmus |
| --- | --- | --- | --- | --- | --- |
| 1 | Innenstadt I | Altstadt, Bahnhofsviertel, Gallus, Gutleutviertel, Innenstadt | offen | nicht aktiv | – |
| 2 | Innenstadt II | Bockenheim, Kuhwald, Westend-Nord, Westend-Süd | offen | nicht aktiv | – |
| 3 | Innenstadt III | Nordend-Ost, Nordend-West | offen | nicht aktiv | – |
| 4 | Bornheim/Ostend | Bornheim, Ostend | offen | nicht aktiv | – |
| 5 | Süd | Flughafen, Niederrad, Oberrad, Sachsenhausen-Nord, Sachsenhausen-Süd | offen | nicht aktiv | – |
| 6 | West | Goldstein, Griesheim, Höchst, Nied, Schwanheim, Sindlingen, Sossenheim, Unterliederbach, Zeilsheim | offen | nicht aktiv | – |
| 7 | Mitte-West | Hausen, Industriehof, Praunheim, Rödelheim, Westhausen | offen | nicht aktiv | – |
| 8 | Nord-West | Heddernheim, Niederursel, Nordweststadt | offen | nicht aktiv | – |
| 9 | Mitte-Nord | Dornbusch, Eschersheim, Ginnheim | offen | nicht aktiv | – |
| 10 | Nord-Ost | Berkersheim, Bonames, Eckenheim, Frankfurter Berg, Preungesheim | André | aktiv | monatlich |
| 11 | Ost | Fechenheim, Riederwald, Seckbach | offen | nicht aktiv | – |
| 12 | Kalbach-Riedberg | Kalbach, Riedberg | offen | nicht aktiv | – |
| 13 | Nieder-Erlenbach | Nieder-Erlenbach | offen | nicht aktiv | – |
| 14 | Harheim | Harheim | offen | nicht aktiv | – |
| 15 | Nieder-Eschbach | Nieder-Eschbach | offen | nicht aktiv | – |
| 16 | Bergen-Enkheim | Bergen-Enkheim | offen | nicht aktiv | – |

## Was Betreuung bedeutet

Wer einen Ortsbezirk betreut, macht im vereinbarten Rhythmus:

1. **Monatsrecherche:** PARLIS-Kalender (.ics) herunterladen und mit `python3 tools/ics_import.py` einlesen; Sitzungstermine und Tagesordnung des Ortsbeirats, neue Anträge, Termine im Stadtteil. Ablage als `docs/recherche/JJJJ-MM-<thema>.md` mit Status-Legende (✅ / ⚠️ / ❓).
2. **Quellenprüfung:** Jede Angabe an der Originalquelle prüfen (PARLIS, frankfurt.de, Veranstalter). Externe Links nur über `data/links.json` mit Datum `bestaetigt`. Widersprüche als ❓ markieren und nicht als Fakt übernehmen.
3. **Blogentwurf:** mindestens ein Beitrag in `data/beitraege/` mit `ortsbezirk: <Nr.>` und `status: entwurf`, offene Punkte im Feld `pruefen`. Veröffentlicht wird erst, wenn `pruefen` leer ist und `check.py` 0 Fehler meldet.
4. **Fehler-Log:** Jeder Fehler (falsche Angabe, gesperrte Quelle, Werkzeugproblem) kommt mit Ursache, Fix und Lehre in `FEHLER-LOG.md`.

Neutralität wie überall: Infos parteipolitisch neutral, Bewertungen nur unter `standpunkte.html` mit `freigegeben: true`. Keine Daten von Privatpersonen.

## Checkliste „Übergabe eines Ortsbezirks“

- [ ] Neue Betreuung ist namentlich benannt (nur Vorname oder Pseudonym, keine Kontaktdaten Dritter im Repo).
- [ ] Rhythmus vereinbart (z. B. monatlich) und in der Tabelle oben eingetragen.
- [ ] Zugang geklärt: GitHub-Konto als Collaborator eingeladen, `CLAUDE.md`, `FEHLER-LOG.md` und `docs/ENTSCHEIDUNGEN.md` gelesen.
- [ ] Stadtteilzuordnung des Bezirks auf frankfurt.de geprüft und in der Tabelle korrigiert.
- [ ] Quellen des Bezirks getestet (PARLIS-Seite des Ortsbeirats, Sitzungsort); gesperrte Domains im Fehler-Log vermerkt.
- [ ] Erste Monatsrecherche abgelegt, erster Blogentwurf mit `ortsbezirk: <Nr.>` angelegt.
- [ ] `python3 tools/build.py && python3 tools/check.py` → 0 Fehler.
- [ ] Erst danach Status in der Tabelle auf **aktiv** setzen (eigener PR) und Richtungsentscheidung in `docs/ENTSCHEIDUNGEN.md` vermerken.
- [ ] Bei Abgabe: Betreuung auf „offen“, Status auf „nicht aktiv“; veröffentlichte Beiträge bleiben, neue Entwürfe werden nicht mehr veröffentlicht.
