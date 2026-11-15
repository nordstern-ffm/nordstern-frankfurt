# Nordstern Frankfurt – Briefing für Claude Code

## Aktueller Auftrag
**Phase 2 (visuelles Redesign): siehe `CLAUDE-CODE-AUFTRAG.md` und `docs/UX-KONZEPT.md`.**
Stand und Übergabe: `docs/STAND.md` · Reihenfolge: `docs/TODO-MASTER.md` · Tests: `python tools/test_check.py`.
Umgebung des Nutzers: Windows + Git Bash (dort `python` statt `python3`), unterwegs Termux.

## Ziel
Dachseite für den Frankfurter Norden: Nachbarschaftshilfe (Verlinkung zum Verein), neutrale Frankfurt-Infos, Mängelmelder (Link zur Stadt), Petitionen (Ziel 220 Unterstützer, extern gesammelt), gewerbliche Vermittlung, gekennzeichnete Standpunkte FREIE WÄHLER, Schaufenster der Copy & Code Agency (André und Partner/in).

## Arbeitsweise (sparsam = wenige Tokens, keine teuren Modelle für Routine)
1. **Inhalte ändern = nur `data/*.json` ändern.** Nie HTML direkt editieren – es wird überschrieben.
2. `python3 tools/build.py && python3 tools/check.py` – erst bei 0 Fehlern committen.
3. Neue Seite = ein `page(...)`-Aufruf in `tools/build.py` + Eintrag in `NAV`.
4. Fixes zuerst per `sed`/`python3` im Repo (SED-MAGIC-Regel aus dem tools-Repo).
5. Routine (Texte, JSON-Einträge, Tippfehler) mit dem günstigsten Modell; großes Modell nur für Architektur, Recht/Datenschutz-Abwägungen und Reviews.
6. Jeder Fehler → `FEHLER-LOG.md`. Jede Richtungsentscheidung → `docs/ENTSCHEIDUNGEN.md` mit Alternativen.

## Muss-Regeln
- Bilder/Grafiken nur mit vollständigem Eintrag in `data/bilder.json` (Lizenz am Original geprüft).
- Kein JavaScript, kein CDN, keine Tracker, keine Formulare mit personenbezogenen Daten.
- Externe Links nur aus `data/links.json` mit Datum `bestaetigt`.
- Verein-Bereich parteipolitisch neutral; Partei-Inhalte nur unter `standpunkte.html`, nur `freigegeben: true`.
- `launch`/`domain_bestaetigt` in `data/site.json` nur umstellen, wenn `check.py --launch` 0 Fehler meldet.
- Keine echten Personendaten Dritter, keine Telefonnummern von Privatpersonen. Repo ist öffentlich: Interna, Vornamen Dritter, Prüfnotizen nur in `docs/intern/` bzw. `data/intern/` (per .gitignore ausgeschlossen).
- WCAG 2.1 AA: Kontrast 4,5:1, Touch-Ziele ≥ 44 px, beide Farbschemata testen.
- Design: Nachtblau #0B1630, Gold #E0B84A, Schriften Fraunces + Atkinson Hyperlegible (lokal).

## Nächste Aufgaben
1. Betreiberdaten + Domain eintragen (docs/DOMAIN-SETUP.md).
2. Blog `frankfurt/` (Python-Build erweitern: `data/beitraege/*.md` → HTML), erster Beitrag „Ortsbeirat 10 in 5 Minuten“.
3. Erste echte Petition mit externer URL in `data/petitionen.json`.
4. Vermittlung: interne Prüfpunkte je Dienst (`data/intern/`, nicht im Repo) abarbeiten, dann Kontakt freischalten.
5. Agenturseite: Preise/Pakete von André und Agentur-Partner/in in `data/zahlung.json`, Stripe Payment Links anlegen (eigenes Konto).
6. Strom & Gas (TeleSon) und Amway: interne Prüfpunkte klären, dann `aktiv: true`.
7. Nach Domain-Start: Rückverlinkung „Teil der Nordstern-Familie“ in bangla-hilfe und wege-nach-frankfurt.
