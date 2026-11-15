# Phase 3 – Bereich „Ankommen“ + großer Sprachraum (Deutsch A1–B1)

Auftrag von André (15.11.2026): **Alles, was auf bangla-hilfe und wege-nach-frankfurt angedacht ist, wird in Nordstern neu gebaut**, mit einem **bewusst großzügig angelegten Raum für die Sprachschule** (Deutsch lernen A1, A2, B1).
Namen sind noch offen (siehe Abschnitt 6). Arbeitstitel: Bereich `/ankommen/`, Sprachschule `/sprachraum/`.

## 1 · Bestand, der übernommen und neu geschrieben wird
| Herkunft | Inhalt | Neuer Ort |
| --- | --- | --- |
| bangla-hilfe `wissen.html` | Chancenkarte, Visum-Checkliste, Familiennachzug, häufige Antragsfehler, Aufenthaltstitel verlängern, Ausländerbehörde, EU Blue Card, Jobcenter/Agentur, Arbeitsvertrag verstehen, FSJ/BFD, IT-Jobs, Zeugnisse/Anabin/ZAB, Pflegekraft-Anerkennung | `/ankommen/wissen/<thema>/` |
| bangla-hilfe `ratgeber/` | Anmeldung, Steuer-ID, Krankenversicherung, Deutsch lernen in Dhaka | `/ankommen/wissen/…` bzw. `/sprachraum/` |
| bangla-hilfe `lektionen.html` | Geschichten-Lektionen „Nisha im Bus“, „Rashed beim Bäcker“ (erfundene Figuren) | Grundstock des Sprachraums, Figuren beibehalten |
| bangla-hilfe `glossar.html`, `faq.html` | Glossar Deutsch–Bangla, FAQ | `/ankommen/glossar/` (mehrsprachig erweiterbar), FAQ je Thema |
| bangla-hilfe `pakete.html`, `bestellen.html` | bezahlte Hilfepakete | erst nach Umzug zum EU-Hoster, über `data/zahlung.json` |
| wege-nach-frankfurt | Länder Eritrea/Thailand/Laos, Geschichten, Termine, Mitreden, Untertitel DE/Lao, Werkzeug `ja2de` | `/ankommen/geschichten/`, `/ankommen/laender/`, Termine → Sprachcafé |

Sprachen: de, en, bn, ti, th, lo. **Übersetzungen erst online, wenn ein Muttersprachler sie geprüft hat** (Regel aus wege-nach-frankfurt). Jede Seite oben „Kurz gesagt“ in Einfacher Sprache (max. 3 Sätze).

## 2 · Sprachraum – Aufbau (großzügig, ruhig, motivierend)
```
/sprachraum/                Start: „Wo stehst du?“ → A1 · A2 · B1 (große Karten mit Kann-Sätzen)
  /a1/ /a2/ /b1/            Niveau-Seite: Lernweg als Zeitleiste, 10–12 Alltagsszenen
    /a1/beim-baecker/       Lektion (Vorlage unten)
  /wortschatz/              Wortkarten nach Themen, druckbar
  /grammatik/               kurze Erklärkarten, je eine Regel, viele Beispiele
  /pruefung/                Prüfungen erklärt (Goethe, telc, ÖSD, DTZ im Integrationskurs) – nur erklären + offiziell verlinken
  /kurs-finden/             Integrationskurs (BAMF-Kurssuche), VHS Frankfurt, kostenlose Online-Angebote (vhs-Lernportal, DW „Nicos Weg“) – nur verlinken
  /sprachcafe/              Termine zum Sprechen üben (aus wege-Termine)
  /fuer-lehrkraefte/        Material zum Ausdrucken, Kontakt für Ehrenamtliche
```
**Alltagsszenen A1–B1 (Vorschlag):** Bus & Bahn · Bäcker & Einkauf · Wohnung & Nachbarn · Anmeldung im Bürgeramt · Arzt & Apotheke · Kita & Schule · Jobsuche · erster Arbeitstag · Telefonieren · Formulare · Feste in Frankfurt (Wäldchestag, Ebbelwoi) · Gefühle & Small Talk.

**Lektions-Vorlage** (`data/lektionen/<niveau>-<slug>.md`):
1. Szenen-Illustration (eigenes SVG, Figuren Nisha, Rashed, neue Figuren aus Eritrea, Thailand, Laos)
2. Kann-Satz („Ich kann beim Bäcker bestellen.“)
3. Dialog Deutsch, darunter umschaltbar die Übersetzung (`<details>` je Sprache, kein JS)
4. Audio (eigene Aufnahme, Muttersprachler Deutsch) + Transkript – Audiodateien mit Nachweis in `data/bilder.json` bzw. `data/medien.json`
5. 8–12 Wortkarten (Artikel farbig: der/die/das)
6. Eine Grammatik-Box
7. Übungen mit Lösung in `<details>` (Lückentext, Zuordnen) – druckbar
8. „Kurz durchatmen“: 10 Minuten reichen für heute
9. Weiter zur nächsten Szene

**Didaktik-Regeln:** Niveaus nach dem Gemeinsamen Europäischen Referenzrahmen (GER) – Kann-Beschreibungen in eigenen Worten, nicht abgeschrieben. Keine Zertifikate, keine „Prüfung garantiert bestanden“-Versprechen. Eine Lehrkraft (DaF/DaZ) prüft jede Lektion vor Freigabe. Ruhiger Ton, kein Druck, Fortschritt zum Abhaken (druckbare Liste, keine Konten, keine Datenspeicherung).

## 3 · Interaktivität
Phase 3a ohne JavaScript (`<details>`, Druckansicht). Ob später kleine lokale Skripte für Übungen erlaubt werden, wird als Entscheidung mit Alternativen in `docs/ENTSCHEIDUNGEN.md` getroffen (Nutzen: Lernmotivation · Risiko: Wartung, Barrierefreiheit).

## 4 · Monetarisierung (später, nach EU-Hosting)
Grundlernstoff kostenlos (Reichweite, SEO, Vertrauen). Bezahlt: Lernpakete als PDF/Audio (Gumroad), Einzelstunden und Kleingruppen (Stripe Payment Link), Hilfepakete aus bangla-hilfe. Alles über `data/zahlung.json`.

## 5 · SEO
Eigene Suchabsicht je Seite („Deutsch lernen A1 Bäcker Dialog“, „Anmeldung Frankfurt Schritt für Schritt“), `hreflang` für alle Sprachfassungen, `Course`/`LearningResource`-Strukturdaten nur wo zutreffend. Alte URLs von bangla-hilfe und wege-nach-frankfurt erhalten Weiterleitungsseiten auf die neuen Adressen.

## 6 · Offene Entscheidungen (André)
- Name des Bereichs (z. B. „Ankommen in Frankfurt“) und der Sprachschule (z. B. „Sprachraum“, „Deutsch-Raum Nordstern“)
- Bleibt „BanglaHilfe“ als Unter-Marke für bengalische Leser erhalten?
- Wer prüft Übersetzungen (bn, ti, th, lo) und wer ist Lehrkraft?

## Aufgaben für Claude Code (nach Phase 2 und Ergänzung 1)
| # | Aufgabe | Fertig, wenn |
| --- | --- | --- |
| P1 | Mehrsprachigkeit im Build: `lang`, `hreflang`, Sprachumschalter, lokale Noto-Schriften (bn, ti/Ethiopic, th, lo) nur bei Bedarf geladen | check prüft hreflang-Paare |
| P2 | Lektions-System aus `data/lektionen/*.md` nach Vorlage | 2 Beispiel-Lektionen (Bus, Bäcker) bauen fehlerfrei |
| P3 | Sprachraum-Startseite + Niveau-Seiten A1/A2/B1 mit Lernweg | auf 390 px großzügig, Touch ≥ 48 px |
| P4 | Wissen-Hub `/ankommen/wissen/` – Themen neu geschrieben mit Primärquelle und Stand | jeder Beitrag von André freigegeben |
| P5 | Geschichten/Länder aus wege-nach-frankfurt | Einwilligung je Person dokumentiert (`docs/EINWILLIGUNGEN.md`, ohne Kontaktdaten) |
| P6 | Weiterleitungsseiten für alte URLs vorbereiten (erst nach Domain-Start aktiv) | Liste alt → neu vollständig |
