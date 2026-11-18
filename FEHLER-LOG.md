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

## 16.11.2026 – Recherche Ortsbeiräte
- **Recherche lieferte keine Ortsbeirats-Tagesordnungen (OBR 10) und keine Termine für OBR 2, 5, 8, 9, 13, 14** · Netzwerk der Claude-Code-Cloud-Umgebung blockiert `www.stvv.frankfurt.de`, `frankfurt.de`, `www.frankfurt-gestalten.de`; Websuche liefert nur alte Niederschriften · Domains in der Umgebung unter „Allowed domains“ freigeben, sonst Amtsblatt-PDFs nutzen · Lehre: Vor einer Recherche die Quell-Domains einmal per `curl` testen; ein leeres Ergebnis ist oft ein Netzwerkblock, keine fehlende Information.
- **Repo „nicht gefunden“** · Claude suchte nur unter `intelligentresponder-max`, das Repo liegt unter `nordstern-ffm` · `gh api search/repositories -f q='nordstern'` findet es · Lehre: Bei Repos des zweiten Kontos immer `nordstern-ffm/` als Besitzer nennen. Das in Claude Code verbundene GitHub-Konto hat keine Schreibrechte auf `nordstern-ffm` – Push nur durch den Nutzer oder nach Einladung von `intelligentresponder-max` als Collaborator.
- **Fork und Pull Request an `nordstern-ffm` aus Claude Code abgelehnt** · Sitzung darf nur ihr zugeordnete Repos anfassen; `nordstern-ffm` ist ein anderes Konto · Fork vom Handy als `intelligentresponder-max` angelegt, Branch in den Fork gepusht, PR per Compare-Link vom Nutzer geöffnet · Lehre: Ohne Passwort des Zweitkontos geht der Weg über Fork + Compare-Link; dauerhaft besser `intelligentresponder-max` als Collaborator einladen.
- **Leerzeile im Fehler-Log** · Patch endete mit Leerzeile, Anhang per heredoc dahinter · entfernt · Lehre: vor dem Anhängen an Markdown-Dateien Datei-Ende prüfen (`tail -c 2 | xxd`).
- **Gleichnamiger Fork blockiert Original in derselben Claude-Sitzung** · Claude Code checkt Repos als <cwd>/<name> aus, Fork und Original heißen beide nordstern-frankfurt · Arbeit am Original in eigener Sitzung · Lehre: Fork nach Collaborator-Einladung nicht mehr nutzen oder löschen.
- **Push aus Claude Code abgelehnt (403), obwohl Collaborator** · Claude GitHub App war auf dem Konto nordstern-ffm nicht installiert · App installiert · Lehre: Bei neuem GitHub-Konto immer zuerst die Claude GitHub App installieren, dann Collaborator.

## 17.11.2026 – Blog-Build (E10, Variante 1)
- **`frankfurt.html` änderte sich, obwohl kein Beitrag veröffentlicht war** · Platzhalter `{blog_hinweis}` stand auf eigener Zeile → leere Zeile im HTML · Platzhalter ohne Zeilenumbruch einsetzen, Umbruch nur mitliefern, wenn Inhalt da ist · Lehre: Nach jeder Build-Änderung `git status` prüfen – „keine HTML-Änderung“ ist der Test.
- **`tools/__pycache__/` tauchte im Repo auf** · `build.py`/`check.py` importieren jetzt `tools/beitraege.py`, Python legt Bytecode an · `sys.dont_write_bytecode = True` vor dem Import · Lehre: Bei neuem Python-Modul im Repo an Bytecode-Ordner denken (kein `.gitignore` nötig).

## 17.11.2026 – Netzwerk-Freigabe der Cloud-Umgebung
- **Freigabe von Domains (github.io, frankfurt.de, PARLIS, ffm.de) scheiterte** · Bestätigungskarte für die Umgebungsänderung lässt sich in der Handy-App nicht genehmigen („Prüfe sie auf deinem Computer“), Ablehnung kam dadurch automatisch · am Computer (claude.ai im Browser oder Desktop-App) genehmigen oder Domains selbst unter Umgebung → Bearbeiten → Netzwerkzugriff → Allowed domains eintragen · Lehre: Umgebungs- und Rechteänderungen nur am Computer anstoßen; vom Handy aus nur Aufgaben ohne Freigabe.
- **Städtische Termine nicht abrufbar, obwohl Nutzer sie braucht** · frankfurt.de/PARLIS blocken die Cloud-Umgebung · Nutzer lädt den PARLIS-Kalender (.ics) im eigenen Browser und lädt ihn hoch; `tools/ics_import.py` macht daraus `data/termine.json` · Lehre: Bei gesperrten Behördenseiten nach Export-Dateien (.ics, .csv, PDF) fragen statt aufzugeben; PARLIS liefert jeden Termin doppelt → beim Import entdoppeln; Kalender enthält keinen Ort → Ort nie aus dem Kalender behaupten.
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

## 16./17.11.2026 – nachgetragen aus Chat 2
- **Push/PR-Freigabe über eine Elternsitzung wirkte nicht** · Kind-Sitzungen pushen nur nach Bestätigung in der eigenen Sitzung · Lehre: Freigaben direkt in der arbeitenden Sitzung geben.
- **Parallele PRs hängten an dieselbe Stelle in ENTSCHEIDUNGEN.md an (#4/#6)** · Konflikt; Rebase + Force-Push hätte die PRs gekoppelt · besser `main` in den Branch mergen · Lehre: Nummern zentral vergeben, nur ein offener PR ändert ENTSCHEIDUNGEN.md (siehe E24).
- **Übergabedateien lagen im Arbeitsordner eines fremden Repos** · ein Stop-Hook verlangte einen Commit · Lehre: Übergabedateien nur im Scratchpad oder außerhalb jedes Repos.
- **„Claude GitHub App“ im Play Store gesucht** · Lehre: Das ist eine GitHub-Integration (github.com/apps/claude, im Browser), keine Handy-App.
- **Merge-Kasten im mobilen GitHub lud nicht** · Lehre: neu laden oder Desktop-Ansicht; notfalls am PC `git fetch origin pull/N/head` und Fast-Forward.
- **Repo nur unter dem verbundenen Konto gesucht** · Lehre: bei unbekanntem Repo zuerst die GitHub-Suche nutzen.

## 18.11.2026 – Blog-Beitrag Laab
- **`gh pr create` aus Claude Code abgelehnt (HTTP 403, GraphQL gesperrt)** · Claude-Code-Sitzungen erlauben nur die GitHub-REST-API · PR per `gh api repos/nordstern-ffm/nordstern-frankfurt/pulls -f base=main -f head=<branch> -f title=… -f body=…` angelegt (#12) · Lehre: In Claude Code PRs immer über `gh api …/pulls` erstellen, nicht über `gh pr create`.
- **`xxd` fehlt in der Cloud-Umgebung** · Datei-Ende-Prüfung aus dem Log (`tail -c 2 | xxd`) brach ab · `tail -c 2 Datei | od -c` nutzen · Lehre: Prüfbefehle mit Standardwerkzeugen (`od`) schreiben.

## 18.11.2026 – Lernseite Deutsch für Lao-Sprechende
- **„Repo Deutschlernen für Laos“ nicht gefunden** · Lernseite existierte nur als Claude-Artefakt, nie als Repo · über Chat-Suche gefunden und nach `lernen/deutsch-lao.html` übernommen · Lehre: Bei „Repo nicht gefunden“ zuerst Claude-Artefakte und frühere Chats prüfen; fertige Artefakte zeitnah in ein Repo übernehmen.
- **Artefakt verstieß gegen zwei Muss-Regeln** (JavaScript, Google Fonts per CDN) · Schriften lokal (Noto Sans Lao neu), JS als begrenzte Ausnahme E13, `check.py` erzwingt die Grenze · Lehre: Fremdes HTML vor dem Übernehmen gegen die Muss-Regeln prüfen, nicht nur `check.py` laufen lassen – `check.py` erkannte Inline-JS bis heute gar nicht.
- **Teil 2: leere Lücken landeten im Fehler-Training** · beim Prüfen wurden auch unausgefüllte Lücken als Fehler gespeichert (1 Fehler + 6 leere = 7) · nur falsch ausgefüllte Lücken zählen, leere nicht · gefunden per Klick-Test (puppeteer-core + Chrome) vor dem Commit · Lehre: Lernseiten nicht nur ansehen, sondern einmal durchklicken – Zähler an einem bekannten Fall nachrechnen.
- **`git checkout main` scheiterte an offenen Änderungen, Befehlskette lief trotzdem weiter** · neue Branch entstand vom alten (bereits gemergten) Branch statt von `main` · hier harmlos, PR zeigte nur die neuen Dateien · Lehre: Neue Branch immer vor dem Ändern anlegen, und Ketten mit `&&` statt `;` verbinden, damit ein Fehler alles stoppt.

## 18.11.2026 – zweite Zusammenführung (PR #12–#14)
- **Entscheidungsnummer E13 zum zweiten Mal doppelt** · ein vierter Chat arbeitete weiter auf `main` (Laab-Rezept, Lernseiten) und vergab E13 · meine Nummern erneut um 1 verschoben (jetzt E14–E26) · Lehre: Der Stopp-Text an alle anderen Chats muss vor dem Zusammenführen bestätigt sein; `git fetch` und Nummernkontrolle direkt vor jedem Merge.
- **Meine Sicherheitsregeln (E19) schlugen auf die Lernseiten an** (Skript, CSP, Sprungmarken per JS erzeugt) · Ausnahme genau für `lernen/deutsch-*.html`, dafür eigene CSP mit `connect-src 'none'` (E27) · Lehre: Ausnahmen immer mit einer Ersatzschranke beantworten, nicht nur mit einer Lockerung.
- **Seiten in Unterordnern bekamen doppelte `../`** (`lernen/index.html` verlinkte `../deutsch-lao.html`) · `page()` ergänzt `../` selbst, die Übersicht schrieb schon relative Pfade · Pfade ab Hauptordner (`lernen/…`) · Lehre: In `page()`-Texten immer Pfade ab Hauptordner schreiben.
- **Testgerüst löschte die echte `lernen/index.html` der Testkopie** (Testfall überschrieb und entfernte sie) · Originale werden jetzt gesichert und zurückgespielt · Lehre: Ein Testgerüst darf nur wegräumen, was es selbst angelegt hat.
- **Geprüft: Token im Klartext in `Frankfurt_FW`** (Hinweis aus Chat 3) · vorhanden, Wert nicht ausgegeben; André widerruft und setzt die Remote-URL ohne Token.

## 18.11.2026 – Optik-Paket 1
- **Vorschau zeigte altes CSS** · Browser-Cache des lokalen Servers (`python -m http.server` setzt keine Cache-Header) · beim Prüfen `fetch('/css/style.css', {cache:'reload'})` oder Strg+F5 · Lehre: Bei Optik-Änderungen immer hart neu laden, bevor man etwas „kaputt“ nennt.
- **Geöffneter Menü-Knopf im Hellmodus nur 2,4:1** (Gold #8A6A10 mit Marineblau) · im Hellmodus Marineblau mit Weiß wie beim aktiven Menüpunkt · Lehre: Jeden neuen Zustand (geöffnet, Fokus, aktiv) in beiden Farbschemata rechnen.
- **Externer Link ohne Eintrag in links.json** (lucide.dev auf der Bildnachweis-Seite) · von check.py gewarnt · bestätigt (HTTP 200) und über `link('lucide')` eingebunden.
