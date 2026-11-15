# FEHLER-LOG – Nordstern Frankfurt

Format: Symptom · Ursache · Fix · Lehre · Datum. Einmal gemachte Fehler hier festhalten.

## Übernommene Lehren aus anderen Repos (gelten hier von Anfang an)
- **Pages vom Hauptzweig = jeder Merge ist eine Veröffentlichung** (Frankfurt_FW) → `noindex`, `robots.txt Disallow` und Vorschau-Banner schon im ersten Commit; Launch nur über `data/site.json`.
- **Keine ungeprüfte URL ins Repo** (Frankfurt_FW) → `data/links.json` mit Datum `bestaetigt`; unbestätigte Links werden nur als Text gezeigt.
- **ffm.de blockt automatische Abrufe (HTTP 403)** → Links im Browser prüfen, nicht per Skript.
- **Tailwind-/Google-CDN überträgt Besucher-IP** (Frankfurt_FW, nachbarschaftshilfe-preungesheim M1) → nur lokale Schriften, kein CDN.
- **Branch-Schutz auf main lehnt Direkt-Push ab (GH013)** (copy-code-agency-website) → Arbeit auf `dev`, Merge per PR.
- **„IPAT-Studie Uni Augsburg“ war falsch** → richtig: IPot-Studie, Hochschule Kempten.
- **Ungenutztes Hosting-Paket lief weiter** (frankfurt-energie.online) → nur Domain buchen, Fristen notieren.

## 15.11.2026 – Aufbau
- **check.py meldete Platzhalter im Impressum** · Regex mit `re.I` traf die CSS-Klasse `class="todo"` · nur Großschreibung `\bTODO\b` prüfen · Lehre: Prüfmuster an echten Seiten testen, nicht nur ausdenken.
- **Hellmodus: dunkle Schrift auf Gold #8A6A10 ≈ 3,6:1** (WCAG verlangt 4,5:1) · Vorschau-Banner und aktiver Menüpunkt im Hellmodus auf Navy/Weiß · Lehre: beide Farbschemata per Screenshot prüfen.
- **Python-f-String mit Backslash im Ausdruck** (`\"page\"`) bricht vor Python 3.12 (Termux kann älter sein) · Wert vorher in Variable · Lehre: Skripte so schreiben, dass sie auch auf älterem Python laufen.
- **Bundle ohne HEAD** · `git clone` des Bundles meldete „remote HEAD refers to nonexistent ref“, Branch `master` leer · Bundle nur mit `main` erstellt, ohne `HEAD` · Workaround beim Nutzer: `git checkout main` · Lehre: Bundles immer mit `git bundle create X.bundle HEAD main` erzeugen und vorher `git clone X.bundle test` testen.
- **Befehle beim Einfügen in Git Bash verstümmelt** · `~` und `@` gingen verloren (`~/Downloads` → `/Downloads` = `C:/Program Files/Git/Downloads`) · Anleitungen mit `"$HOME/..."` und `git config credential.username` statt `user@host` · Lehre: Für den Nutzer keine `~`/`@` in Kopier-Befehlen, jede Zeile einzeln.
- **Neues GitHub-Konto (nordstern-ffm)** · Gefahr, dass Git die gespeicherte Anmeldung des alten Kontos nutzt · `git config credential.username nordstern-ffm` vor dem ersten Push · Push am 15.11.2026 erfolgreich.

## 15.11.2026 – Phase 2, Aufgabe 1 (Bildrechte-Prüfung)
- **test_check.py brach mit UnicodeDecodeError ab** · check.py als Unterprozess schreibt unter Windows in cp1252 („geprüft“ → Byte 0xFC), Test las UTF-8 · `PYTHONIOENCODING=utf-8` für den Unterprozess setzen · Lehre: Unterprozess-Ausgabe auf Windows immer mit fester Kodierung lesen.

## 15.11.2026 – Phase 2, Aufgabe 2 (Icons)
- **tools/icons.py brach bei der Ausgabe ab (UnicodeEncodeError „→“)** · `python -I` ignoriert `PYTHONIOENCODING`, Windows-Konsole ist cp1252 · Ausgabe nur ASCII · Lehre: Konsolen-Ausgaben von Werkzeugen ohne Sonderzeichen außerhalb Latin-1.
- **Edge headless hing beim dritten Screenshot** (Befehl lief in den 2-Minuten-Timeout) · vermutlich Kopplung an das laufende Edge-Profil · bei Screenshots eigenes `--user-data-dir` und Zeitlimit je Aufruf verwenden · 390-px-Aufnahmen von Edge headless wirken rechts abgeschnitten (Mindest-Fensterbreite) → für die Abnahme (Aufgabe 10) Gerätemodus/Emulation nutzen, nicht `--window-size`.
