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

## 15.11.2026 – Phase 2, Aufgabe 3 (Kennzahlen)
- **Beispielzahl im UX-Konzept war veraltet und nicht aus Primärquelle** · „15.770 Einwohner Preungesheim“ = Stand 31.12.2024 laut citypopulation.de · amtlich gefunden: 15.896 (Ende 2025, statistik.aktuell 04/2026) · Lehre: Zahlen aus Konzepten nie übernehmen, immer neu an der Primärquelle prüfen.
- **Statistik-Seiten der Stadt: WebFetch schneidet ab, PDF ist rechte-verschlüsselt** · Werte stecken als JSON in der Karte der HTML-Seite (7 MB) · Seite per curl laden und mit Python durchsuchen; `grep -o` mit langen Mustern auf einzeiligen 7-MB-Dateien hängt (2-Minuten-Timeout) · Lehre: große Einzeiler mit Python durchsuchen. Plausibilität geprüft: weiblich + männlich und deutsch + EU + Nicht-EU ergeben jeweils die Summe.
- **Kontrast: Gold-Soft im Hellmodus fällt durch (2,98:1 auf Weiß)** · neue Kennzahl nutzt im Hellmodus `--gold` (5,06:1) · bestehende Stellen in docs/OFFEN.md · Lehre: jede neue Farbe vor dem Einbau rechnen, nicht schätzen.
- **Behoben: Hellmodus-Kontrast `--gold-soft`** · `#B8901E` → `#8A6A10`: Karten-Überschriften 2,98 → 5,06:1, H1-Zeile 2 und Eyebrow 2,68 → 4,56:1 · Stern-Inneres im Hellmodus fest `#B8901E` (Deko, bleibt zweifarbig) · Lehre: Farb-Token im Hellmodus gegen jeden Hintergrund rechnen, auf dem es als Text vorkommt.

## 15.11.2026 – Nachtrag André (übertragen aus docs/NACHTRAG-FUER-CLAUDE-CODE.md)
- **Festtermine aus Reiseseiten sind unzuverlässig** · Recherche Weihnachten: eine Seite listet Bulgarien beim 7. Januar, richtig ist der 25. Dezember (revidierter Kalender) · Regel in `docs/FESTKALENDER-RECHERCHE.md`: nur Quellen der Religionsgemeinschaft oder Fachmedien.
- **Nummernkonflikt Entscheidungen** · Phase-3b-Dokument nannte die JS-Entscheidung E11, obwohl E11 schon vergeben war · Lehre: Nummern nur in `docs/ENTSCHEIDUNGEN.md` vergeben, in anderen Dokumenten „E-neu“ schreiben.
- **Nummernkonflikt, zweiter Fall** · Nachtrag vergab E12 für die Skript-Entscheidung, Claude Code hatte E12 am selben Tag für die Kennzahlen (Aufgabe 3) vergeben · Andrés Dokumente verweisen durchgehend auf E12 = Skripte → Kennzahlen auf E13 umnummeriert, PHASE3B „E11“ → E12 · Lehre: vor dem Vergeben einer Nummer `grep -rn "E1[0-9]" docs/` laufen lassen – auch in frisch eingespielten Patches.
