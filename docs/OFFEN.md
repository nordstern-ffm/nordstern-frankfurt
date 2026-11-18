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
| frankfurt.html | ~~16 Ortsbeiräte, Ortsbezirk 10~~ | **erledigt** (Aufgabe 5): Broschüre StVV, Stand Mai 2025 |
| frankfurt.html | Kommunalwahl „zuletzt am 15. März 2026“ | Satz entfernt (Aufgabe 5); Wahltermin erst mit Quelle (Wahlamt) wieder nennen. Wahlzeit 5 Jahre ist über die StVV-Broschüre belegt. |

## Barrierefreiheit
Erledigt am 15.11.2026: Hellmodus-Kontrast von `--gold-soft` (siehe FEHLER-LOG, Aufgabe 3).

## Sicherheit / Datenschutz – Entscheidung André
Erledigt am 15.11.2026 (E20): interne Prüfnotizen, Vornamen Dritter und das Repo-Audit liegen nur noch lokal in `docs/intern/` und `data/intern/` (per `.gitignore` ausgeschlossen).
**Offen:** Die Git-Historie (bis Commit 147d551) und damit GitHub enthält die alten Fassungen weiterhin. Entfernen ginge nur durch Umschreiben der Historie und erzwungenen Push (`git filter-repo`, danach `--force`) – nicht umkehrbar, Forks/Kopien bleiben. Alternative: Repo privat stellen (Pages braucht dann einen bezahlten Plan) oder neues, sauberes Repo nur mit dem aktuellen Stand anlegen. Entscheidung André.

## Blog / Artikel Personalvermittlung (15.11.2026)
- Beitrag `data/beitraege/2026-11-15-personalvermittlung-gruenden.md` ist **Entwurf** – Freigabe durch André vor Merge auf `main` (R4).
- § 299 SGB III (Informationspflichten bei grenzüberschreitender Vermittlung) noch nicht gelesen → vor Ausbau des Auslands-Abschnitts prüfen.
- Ob die Gewerbeanzeige in Frankfurt beim Ordnungsamt/Gewerbeamt liegt und online geht: auf frankfurt.de im Browser prüfen (Skript-Abruf 403).
- Bundesagentur: offizielle Seite zum Programm für Pflegekräfte aus dem Ausland suchen und als Link ergänzen (Leser sollen sich direkt informieren können).
- BanglaHilfe (anderes Repo): Google Fonts lokal einbinden; Mindestlohn 12,82 €/h und Finanznachweis 11.904 € auf Stand 2026 prüfen; `bangla-hilfe.de` nicht erreichbar.

## Aufgabe 5 – Schaubild (15.11.2026)
- **Zahlen nach der Kommunalwahl 2026:** 93 Stadtverordnete folgt aus § 38 Abs. 1 HGO (Frankfurt > 500 000 Einwohner) – gilt weiter, solange die Hauptsatzung die Zahl nicht senkt (§ 38 Abs. 2). 284 Ortsbeiratsmitglieder: Stand Mai 2025, nach der Wahl am 15.03.2026 auf stvv.frankfurt.de prüfen.
- **Ausländerbeirat / KAV:** Hat Frankfurt eine Kommunale Ausländer- und Ausländerinnenvertretung (Ausländerbeirat nach § 84 HGO) oder eine Integrations-Kommission (§ 89)? Primärquelle (stvv.frankfurt.de / Wahlamt) suchen, dann ins Schaubild.
- **Zahl der Stadträtinnen und Stadträte:** Broschüre widersprüchlich (OB + 11 / 12 hauptamtliche / OB + Bürgermeister + 9) → nicht verwenden, bis die Magistratsseite der Stadt geprüft ist.

## Aus Chat 2 übernommen (17.11.2026)
- Gesperrte Quellen in der Cloud-Umgebung: www.stvv.frankfurt.de (PARLIS), frankfurt.de (inkl. Amtsblatt), www.frankfurt-gestalten.de → im eigenen Browser prüfen.
- Mängelmelder-Beitrag (veröffentlicht): Ablauf auf ffm.de (Pflichtfelder, Foto, Rückmeldung), Bürgerfragestunde OBR 10 (Ablauf/Anmeldung), Antragsnummern OF 63/10, 64/10, 69/10 – noch unbelegt.
- OBR-Termine im Claude-Doc vom 16.11. stammen aus einem früheren Lauf; mit `data/termine.json` (PARLIS-Export) abgleichen.
- Ungeprüfte Recherche (Wohngeld, Mietpreisbremse, Haushalt, Glasfaser, Weihnachtsmärkte): `docs/recherche/2026-11-uebergabe-chat2.md`.
- **Datenschutz, Entscheidung André:** Die Verbindung der Konten `intelligentresponder-max` ↔ `nordstern-ffm` ist öffentlich sichtbar (Fork, PR #1, Collaborator, Fehler-Log); Commits enthalten Links zu claude.ai-Sitzungen; das Claude-Doc „Ortsbeiräte Frankfurt – Recherche Nov/Dez 2026“ ist für alle mit Link lesbar. Bewusst so lassen oder ändern?

## Aus Chat 3 „nh-preungesheim“ (Stand 18.11.2026) – Übergabe
- Gearbeitet wurde **nicht** in diesem Repo, sondern im lokalen Ordner `C:/Users/Holy New/Desktop/nh-preungesheim` (kein Git, nichts committet): Prototyp `app/index.html` (Rollen, Matching, Einsatznachweis), `app/config.json`, `vorlagen/strassen_beispiel.csv` (fiktive Daten).
- Offen dort: Prototyp im echten Browser prüfen · Ordner versionieren (eigenes Repo oder Übernahme) · Löschfristen und Zugriffsprotokoll · Konfiguration (Logo, Farben, Tätigkeiten) · Adressprüfung · später PWA mit Datenbank, EU-Hosting, echte Rollen mit Zwei-Faktor (Rollen sind nur im Browser simuliert).
- Ungeprüfte Fakten (aus dem alten Briefing übernommen): BGW-Unfallversicherung, Freibeträge 960 € / 3.300 €, Abtretung durch Pflegekassen, Entlastungsbetrag 131 € (am 15.11. an § 45b SGB XI geprüft), Hessen-Höchstsätze 25 €/30 €, Führungszeugnis 13 €, IPot-Studie (Hochschule Kempten).
- **Sicherheit:** Im Projekt `Frankfurt_FW` steht ein GitHub-Zugangstoken im Klartext in der Remote-URL → bei GitHub widerrufen, Remote-URL ohne Token setzen (Befehl in der Antwort an André).
