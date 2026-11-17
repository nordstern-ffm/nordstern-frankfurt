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

## 15.11.2026 – Phase 2, Aufgabe 4 (Abläufe, Zeitleiste)
- **Geklärt: „390 px abgeschnitten“ (Aufgabe 2) war ein Messfehler** · Edge headless erzwingt eine Mindest-Fensterbreite (~500 px), Screenshot schnitt rechts ab · Seite in einem `<iframe width="390">` rendern → echtes 390-px-Layout, nichts abgeschnitten · Lehre: Mobil-Screenshots per iframe oder Geräte-Emulation, nie per `--window-size` unter 500.
- **Entwurfstext behauptete mehr als belegt** · „Keine Pflege“ im Nachbarschafts-Ablauf stand nirgends auf der Seite; „220“ fest im Text widersprach E3 · ersetzt durch vorhandene Aussage (keine Strom-, Gas-, Wasserinstallation) und `{ziel}`-Platzhalter · Lehre: Ablauftexte Satz für Satz gegen bestehende Seiteninhalte prüfen.

## 15.11.2026 – Gesamtprüfung (Inhalt + Sicherheit)
- **check.py prüfte nur die 11 Hauptseiten** · `docs/mockups/*.html` (aus Andrés Patch) werden über Pages ebenfalls veröffentlicht, waren aber ungeprüft; außerdem fand die alte Regel nur `<script src>`, keine Inline-Skripte, Handler oder `javascript:`-Links · neue Abschnitte 8–10 in check.py für alle HTML/CSS + 12 Testfälle · Lehre: Prüfungen am Veröffentlichungsumfang ausrichten, nicht an der Build-Ausgabe.
- **Überschriften-Sprung h1 → h3 auf 4 Seiten** (Nachbarschaft, Frankfurt-Info, Vermittlung, Agentur) · Kartenraster direkt nach der h1 · je eine h2 ergänzt, check.py prüft Sprünge · Lehre: Struktur-Regeln (WCAG 1.3.1) automatisch prüfen, Screenshots zeigen das nicht.
- **Interne Notizen sind öffentlich** · Repo `nordstern-ffm/nordstern-frankfurt` ist öffentlich, Pages veröffentlicht mit `.nojekyll` alles (geprüft: `/data/dienste.json` und `/FEHLER-LOG.md` liefern HTTP 200) · E7 sagt „nicht öffentlich“ – stimmt nicht · Entscheidung bei André (docs/OFFEN.md) · Lehre: „intern“ heißt bei öffentlichem Repo: gar nicht ins Repo.
- **Mockup nannte noch „Entscheidung E11“** · auf E12 korrigiert.

## 15.11.2026 – Blog, Artikel Personalvermittlung
- **Commons-Treffer „Agentur für Arbeit Frankfurt“ zeigten Frankfurt (Oder)** · Suchbegriff ohne „am Main“ · Bilder verworfen · Lehre: Ort jedes Fotos in der Commons-Beschreibung prüfen, nicht im Dateinamen.
- **Gründerküche-Artikel ist Sekundärquelle (Stand 10/2023) ohne Gesetzesangaben** · alle Rechtsaussagen an gesetze-im-internet.de geprüft (§ 1, § 14 GewO, § 138 AO, § 2 IHKG, § 1 AÜG, §§ 45, 176, 296, 296a SGB III, § 38 BeschV + Anlage); „AZAV kostet mehrere tausend Euro“ nicht belegt → nicht übernommen.
- **Entwurfstext ging über die Quellen hinaus** („In Frankfurt ist das die Stadt“, „Provision meist vom Betrieb“, „Post vom Finanzamt“, „die Hälfte nach sechs Wochen“, „auch auf Bangla“) · auf belegte Aussagen gekürzt · Lehre: jeden Satz gegen die Fundstelle lesen, bevor gebaut wird.
- **Python-Ersetzungen mit Regex in Heredocs verloren Backslashes** (`\b` wurde zu Steuerzeichen, `"\n"` zu echtem Zeilenumbruch) · Änderungen mit Regex über den Editor statt per Skript · Lehre: Code mit Backslashes nie in normale Python-Strings einbetten.
- **test_check.py überschrieb bilder.json der Testkopie mit leerer Liste und löschte den ganzen img/-Ordner der Kopie** · echte Blog-Bilder fehlten → „0 Fehler“-Fälle schlugen fehl · Testbilder kommen jetzt zu den echten Einträgen dazu, gelöscht wird nur `img/test.webp` · Lehre: Testgerüste dürfen nur anfassen, was sie selbst anlegen.
- **check.py prüfte Seiten in Unterordnern nicht** (Beitrag wurde als „weitere HTML“ gezählt) · Seitenliste = alle HTML außer docs/, relative Links mit `../` werden aufgelöst.

## 17.11.2026 – Zusammenführen ux-phase2 ↔ main
- **Zwei Chats arbeiteten parallel auf verschiedenen Ständen** · `main` (anderer Chat, 10 PRs, live) und `ux-phase2` (20 Commits, nie gepusht) zweigten beide von 3e37dcd ab · doppelte Arbeit (zwei Blog-Systeme) und doppelte Entscheidungsnummern E10–E12; die Datenschutz-Bereinigung war nur auf ux-phase2, auf `main` waren interne Notizen weiter live · Zusammenführung auf `main`-Basis, ux-phase2-Entscheidungen E10–E20 → **E13–E23** (ältere Einträge in diesem Log nennen noch die alten Nummern) · Lehre: vor jeder Sitzung `git fetch` + Vergleich mit `origin/main`; nur ein Chat arbeitet gleichzeitig an einem Branch; Arbeitsstände früh als PR pushen.
