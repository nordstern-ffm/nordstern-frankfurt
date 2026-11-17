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
- **frankfurt.de und ffm.de trotz Freigabe nicht abrufbar (HTTP 403)** · Domains in der Umgebung freigegeben, Proxy lässt durch, aber die Seiten selbst blocken Rechenzentrums-Zugriffe (frankfurt.de: Cloudflare-Bot-Schutz „Just a moment…“, ffm.de: 403) – auch mit echtem Browser · nicht umgehen; Prüfpunkte zu städtischen Seiten im eigenen Browser erledigen, Gesetzestexte über gesetze-im-internet.de (funktioniert) · Lehre: Nach einer Freigabe jede Domain einzeln testen; 403 mit „Connection Established“ = Sperre der Seite, nicht der Umgebung.
