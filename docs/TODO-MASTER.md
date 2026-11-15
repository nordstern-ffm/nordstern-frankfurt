# TODO-Master Nordstern – nach Wichtigkeit (Stand 15.11.2026)

Wer: **A** = André · **CC** = Claude Code · **Chat** = Claude im Chat (Recherche, Texte, Prüfung).
P0 = vor dem öffentlichen Start · P1 = vor dem ersten Geld · P2 = Ausbau · P3 = später.

## Reihenfolge Claude Code (festgelegt von André, 15.11.2026)
Abarbeitung strikt von oben nach unten. Details und „Fertig, wenn“ stehen im jeweiligen Dokument.
| # | Block | Aufgabe | Quelle | Status |
| --- | --- | --- | --- | --- |
| 1 | Phase 2 | Aufgaben 1–3: Bildrechte, Icons, Kennzahlen (+ Kontrast Hellmodus) | CLAUDE-CODE-AUFTRAG.md | ✓ erledigt (Branch ux-phase2) |
| 2 | Phase 2 | **4** Ablauf-Diagramme + Zeitleiste (`steps()`/`timeline()`) | CLAUDE-CODE-AUFTRAG.md | ✓ erledigt |
| 3 | Phase 2 | **5** Schaubild „Wer entscheidet in Frankfurt?“ (Inline-SVG + Text-Alternative, Quellen HGO/frankfurt.de) | CLAUDE-CODE-AUFTRAG.md | ✓ erledigt (E19), KAV offen |
| 4 | Phase 2 | **6** Schema-Karte Ortsbezirk 10 (eigenes SVG, ODbL-Hinweis) | CLAUDE-CODE-AUFTRAG.md | ☐ |
| 5 | Phase 2 | **7** Hero-Illustrationen je Seite (eigene SVG) | CLAUDE-CODE-AUFTRAG.md | ☐ |
| 6 | Phase 2 | **8** 3–6 Fotos Wikimedia Commons (WebP ≤ 150 KB, Lizenz am Original) | CLAUDE-CODE-AUFTRAG.md | ☐ |
| 7 | Phase 2 | **9** Vermittlung: Filter-Chips ohne JS, Dienst-Karten mit Icon | CLAUDE-CODE-AUFTRAG.md | ☐ |
| 8 | Phase 2 | **10** Abnahme: Screenshots 390/1280 hell/dunkel (Emulation, nicht `--window-size`), Kontrast, Lighthouse → `docs/ABNAHME-PHASE2.md` | CLAUDE-CODE-AUFTRAG.md | ☐ |
| 9 | Ergänzung 1 | **S1** SEO-Prüfungen in check.py + Fehl-/Gut-Tests | AUFTRAG-ERGAENZUNG-1.md | ☐ |
| 10 | Ergänzung 1 | **S2** Meta/OG/JSON-LD je Seite, `sitemap.xml` nur bei Launch | AUFTRAG-ERGAENZUNG-1.md | ☐ |
| 11 | Ergänzung 1 | **R1** Beitragssystem `data/beitraege/*.md` → Rubrik-Seiten, `Article`-JSON-LD | AUFTRAG-ERGAENZUNG-1.md | ◐ Grundsystem steht (E18), JSON-LD folgt mit S2 |
| 12 | Ergänzung 1 | **R2** Rubriken-Startseiten, Leerzustand, max. 7 Hauptpunkte | AUFTRAG-ERGAENZUNG-1.md | ☐ |
| 13 | Ergänzung 1 | **R3** Baustein „Kurz durchatmen“ ohne JS | AUFTRAG-ERGAENZUNG-1.md | ☐ |
| 14 | Ergänzung 1 | **R4** Erste Ratgeber Stufe A neu schreiben, je Fakt Primärquelle; Freigabe durch André | AUFTRAG-ERGAENZUNG-1.md | ☐ |
| 15 | Phase 3 | **P1** Mehrsprachigkeit: `lang`, `hreflang`, Sprachumschalter, Noto-Schriften lokal | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 16 | Phase 3 | **P2** Lektions-System `data/lektionen/*.md`, 2 Beispiel-Lektionen | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 17 | Phase 3 | **P3** Sprachraum-Start + Niveau-Seiten A1/A2/B1 (hier: E12-Freigabe in check.py bauen) | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 18 | Phase 3 | **P4** Wissen-Hub `/ankommen/wissen/`, Freigabe durch André | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 19 | Phase 3 | **P5** Geschichten/Länder aus wege-nach-frankfurt, Einwilligung je Person | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 20 | Phase 3 | **P6** Weiterleitungsseiten alte URLs (aktiv erst nach Domain-Start) | PHASE3-ANKOMMEN-SPRACHRAUM.md | ☐ |
| 21 | Phase 3b | **V1** Bausteine aus `seitenanatomie.html` als build.py-Funktionen | PHASE3B-VISUELL-LINKS-ANZEIGEN.md | ☐ |
| 22 | Phase 3b | **V2** Verlinkungs-Prüfungen + Tests (verwaiste Seite → Fehler) | PHASE3B-VISUELL-LINKS-ANZEIGEN.md | ☐ |
| 23 | Phase 3b | **V3** `data/anzeigen.json` + Regeln (Anzeige auf Vereinsseite → Fehler) | PHASE3B-VISUELL-LINKS-ANZEIGEN.md | ☐ |
| 24 | Phase 3b | **V4** `data/kultur.json` + Kultur-Moment je Woche; Quellen-Links vorher in `links.json` bestätigen | PHASE3B-VISUELL-LINKS-ANZEIGEN.md | ☐ |
| 25 | Phase 3b | **V5** Sprachraum-Diktatweg, E12 (freigegeben), 2 Beispiel-Diktate A1 | PHASE3B-VISUELL-LINKS-ANZEIGEN.md | ☐ |
| 26 | Weltstadt | **W1** Lesbarkeitsprüfung in check.py + Tests | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 27 | Weltstadt | **W2** Kennzahl „179 Länder · 31,7 % (Ende 2023)“ – Zahlen vor Einbau an der Primärquelle prüfen (Stand Ende 2025 vorhanden?) | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 28 | Weltstadt | **W3** Rubrik „Frankfurt spricht“, Beispielbeitrag als Entwurf | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 29 | Weltstadt | **W4** Quiz-Baustein aus `quiz.json` – **jetzt freigegeben (E12 erweitert, André 15.11.2026)**; Quiz-Fragen vor Übernahme auf Quellen prüfen | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 30 | Weltstadt | **W5** „Dein Wort für Frankfurt“ (mailto + Zustimmungstext), Datenschutzerklärung ergänzen | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 31 | Weltstadt | **W6** Druck-Extras als eigene SVG, in `bilder.json` als „eigen“ | WELTSTADT-LESBARKEIT-VERWEILEN.md | ☐ |
| 32 | Suche & KI | **G1** Glossar `data/glossar.json` → `glossar.html`, Auto-Links in Beiträgen | KONZEPT-SUCHE-KI.md | ☐ nach allen Inhaltsaufgaben |
| 33 | Suche & KI | **G2** Seitensuche mit lokalem Index (Entscheidung E12-Erweiterung) | KONZEPT-SUCHE-KI.md | ☐ |
| 34 | Suche & KI | **G3** `llms.txt` + Kurzfassungen für KI-Assistenten | KONZEPT-SUCHE-KI.md | ☐ |
| 35 | Suche & KI | **G4** KI-Chat nur aus eigenen Inhalten, erst nach EU-Hoster + Datenschutzprüfung | KONZEPT-SUCHE-KI.md | ☐ |

## Neu (André, 15.11.2026)
| ✓ | Aufgabe | Wer |
| --- | --- | --- |
| ✓ | Blog-Reiter mit Stadtpolitik, Politik, KI & Stadt, Ratgeber (E17) | CC |
| ◐ | Artikel „Personalvermittlung gründen“ – Entwurf, Freigabe offen | A |
| ☐ | KI-Bilder nach `docs/BILD-PROMPTS.md` erzeugen, dann Feld `ki` in build/check einbauen | A erzeugt, CC baut ein |
| ☐ | KI & Stadt: erste Recherche (KI-Ampeln, digitales Rathaus) – was hat Frankfurt schon? | Chat recherchiert, CC prüft Quellen |

## P0 – vor dem Start (Domain, noindex weg)
| ✓ | Aufgabe | Wer |
| --- | --- | --- |
| ☐ | **Zwei-Faktor-Anmeldung** für GitHub-Konto nordstern-ffm aktivieren (neues Konto, Hauptschutz des Projekts) | A |
| ✓ | Interne Notizen und Vornamen Dritter aus dem Repo genommen (15.11.2026, E16) – offen: Git-Historie bereinigen (siehe `docs/OFFEN.md`) | A entscheidet |
| ☐ | Impressum-Daten: Anschrift, E-Mail, Telefon → `data/site.json` | A |
| ☐ | Domain kaufen (nur Domain), DNS nach `docs/DOMAIN-SETUP.md`, Zwei-Faktor beim Registrar | A |
| ☐ | Phase 2 (Aufgaben 1–10) abnehmen, PR `ux-phase2 → main` prüfen und mergen (1–3 erledigt, siehe Reihenfolge oben) | A + CC |
| ☐ | Datenschutzerklärung an alle neuen Funktionen anpassen (Audio, lokale Skripte E12, E-Mail-Einsendungen, Anzeigen/UTM, externe Links) | CC + Chat prüft |
| ☐ | Erklärung zur Barrierefreiheit (Seite) + Prüfung, ob das Barrierefreiheitsstärkungsgesetz für die bezahlten Angebote gilt (Ausnahme für Kleinstunternehmen prüfen) | Chat recherchiert, CC baut |
| ☐ | Link-Check aller externen Links im Browser, Ergebnis in `data/links.json` | A + CC |
| ✓ | Mobilansicht 390 px: geklärt – Messfehler von Edge headless, per iframe 390 px nichts abgeschnitten (FEHLER-LOG, Aufgabe 4) | CC |
| ☐ | Wahlprogramm-Text FW schicken + Vorstandsfreigabe der Positionen | A |
| ☐ | Klären: „220 Bürger“ = Ziel 220 Unterstützer je Projekt? | A |

## P1 – vor dem ersten Geld (Anzeigen, Pakete, Vermittlung)
| ✓ | Aufgabe | Wer |
| --- | --- | --- |
| ☐ | Umzug zu EU-Hoster (GitHub-Regeln verbieten Pages als Geschäftsseite) + Deploy per Push | A + CC |
| ☐ | Gewerbeanmeldung (Agentur, Vermittlung), steuerliche Einordnung (Kleinunternehmer?) mit Steuerberatung | A |
| ☐ | AGB + Widerrufsbelehrung für bezahlte Pakete/Lernpakete, Preisangaben korrekt (Endpreise) | Chat Entwurf, Fachanwalt/IHK prüfen |
| ☐ | Eigenes Stripe-Konto Agentur, Zahlungslinks, ggf. Krypto (USDC) erst wenn im Konto verfügbar | A |
| ☐ | Agentur-Partner/in: Rolle, Pakete, Preise (Name nur mit Einwilligung veröffentlichen) | A |
| ☐ | Vermittlung: interne Prüfpunkte je Dienst abarbeiten (lokal in `data/intern/`) | A |
| ☐ | TeleSon-Vertragsform + Amway-Website-Richtlinien lesen, dann `aktiv: true` | A |
| ☐ | Anzeigenpartner-Vertrag (Mustervorlage: Laufzeit, Preis, Kennzeichnung, Ausschlüsse) | Chat |
| ☐ | Webador-Abo kündigen (Entwurf liegt im Chat), Domain-Code sichern | A |

## P2 – Ausbau (Phasen 3, 3b, Weltstadt)
| ✓ | Aufgabe | Wer |
| --- | --- | --- |
| ☐ | Ergänzung 1 (SEO S1–S2, Redaktion R1–R4) | CC |
| ☐ | Phase 3 Ankommen + Sprachraum (P1–P6), Namen festlegen | A entscheidet, CC baut |
| ☐ | Phase 3b Bausteine, Verlinkung, Anzeigen, Kultur (V1–V5) | CC |
| ☐ | Weltstadt/Lesbarkeit/Interaktion (W1–W6) – Entscheidung Quiz-Skripte ✓ (E12 erweitert, 15.11.2026) | CC |
| ☐ | **Prüfer-Netzwerk** Übersetzungen: Lao, Bangla, Tigrinya, Thai, Englisch – schriftliche Zusage + Nutzungsrechte | A |
| ☐ | **Einwilligungen** dokumentieren: Personen in Geschichten/Fotos, Sprecher für Audio, Gastautoren, Übersetzer (`docs/EINWILLIGUNGEN.md`, ohne Kontaktdaten) | A |
| ☐ | Festkalender 2027 per Deep Research (Oktober) | Chat |
| ☐ | Redaktionsrhythmus festlegen (z. B. 2 Beiträge/Woche) + Freigabeweg | A |
| ☐ | Fachliche Prüfung der Sprachraum-Lektionen (DaF/DaZ-Lehrkraft) | A |

## P3 – später
| ✓ | Aufgabe | Wer |
| --- | --- | --- |
| ☐ | Search Console + Bing Webmaster nach Launch, Sitemap einreichen | A + CC |
| ☐ | Weiterleitungen alte Seiten (bangla-hilfe, wege-nach-frankfurt) auf neue Domain | CC |
| ☐ | Newsletter (EU-Anbieter, Double-Opt-in) | A + CC |
| ☐ | Monatlicher automatischer Link-Check (Skript am PC), Bericht ins Repo | CC |
| ☐ | Sicherung: zweites Remote oder lokales Backup des Repos | A |
| ☐ | Altes Konto intelligentresponder-max: Impressum für 16 öffentliche Seiten ergänzen oder Pages abschalten, Duplikate archivieren (Audit lokal in `docs/intern/`) | A + CC |
| ☐ | Lernpakete (PDF/Audio) über Gumroad, Kleingruppen über Zahlungslink | A + CC |
