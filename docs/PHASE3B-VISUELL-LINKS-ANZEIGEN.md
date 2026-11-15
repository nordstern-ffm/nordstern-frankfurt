# Phase 3b – Visuelle Vorlagen, interne Verlinkung, Anzeigen, Kultur-Momente

Vorlagen (im Browser öffnen, `noindex`): `docs/mockups/seitenanatomie.html`, `docs/mockups/sprachraum-diktatweg.html`.
Gestrichelte Rahmen + Nummern = Zonen. Claude Code baut daraus wiederverwendbare Bausteine in `tools/build.py`.

## 1 · Seitenanatomie (jede Inhaltsseite)
| Zone | Baustein | Zweck |
| --- | --- | --- |
| 1 | Breadcrumb + H1 + Pills (Stand, Lesezeit, Sprachen) + Hero-Illustration | Orientierung, `BreadcrumbList`-JSON-LD |
| 2 | „Kurz gesagt“ (max. 3 Sätze, mit Zahl/Datum) | Schnellleser, Einfache Sprache, KI-Zitierfähigkeit |
| 3 | Inhalt: Grafik/Icon/Zahl vor Text, Diagramm + Tabelle | „In Bildern erklären“ |
| 4 | Kontext-Links im Fließtext | interne Verlinkung mit beschreibendem Linktext |
| 5 | „Weiterlesen“ – 3 Karten aus demselben Themen-Cluster + 1 Querverbindung | Relevanz, Verweildauer |
| 6 | Anzeige (rechte Spalte / mobil nach Zone 5) | Einnahmen, seriös |
| 7 | Kultur-Moment | Frankfurt-Leben, Feste, Religionen – unaufdringlich |
| 8 | Kurz durchatmen | Entspannung (mindful7777-Ton) |
| 9 | Quellen + Autor + Prüfdatum | E-E-A-T, Vertrauen |

## 2 · Interne Verlinkung (Regeln, von check.py geprüft)
- **Themen-Cluster** (Hub & Spoke): Ankommen · Sprachraum · Nachbarschaft · Frankfurt verstehen · Melden & Bewegen · Vermittlung. Jede Rubrik-Startseite = Hub, verlinkt alle Beiträge; jeder Beitrag verlinkt zurück zum Hub.
- Jeder Beitrag: **3–5 interne Kontext-Links** + „Weiterlesen“-Block. Mindestens **eine Querverbindung** zwischen Clustern (z. B. Ratgeber „Anmeldung“ ↔ Lektion „Im Bürgeramt“ ↔ Meldung „Aus dem Römer“).
- Linktext beschreibt das Ziel (kein „hier“, „mehr“). Keine verwaisten Seiten (jede Seite hat ≥ 2 eingehende interne Links).
- Verknüpfung über Felder im Beitragskopf: `cluster`, `tags`, `verwandt: [slug, slug]` → Build erzeugt „Weiterlesen“ automatisch.
- `check.py`: verwaiste Seiten, tote Links, Beiträge mit < 3 internen Links, generische Linktexte → Fehler.

**Wo Blog-Bereiche verlinkt werden:** Startseite (Block „Neu im Norden“: 3 neueste Beiträge), jede Hauptseite (Zone 5), Sprachraum-Lektionen (Zone H „Weiter lernen“ → passender Ratgeber), Vermittlung (passender Ratgeber je Dienst, z. B. Energie → „Erste Wohnung: Strom anmelden“), 404-Seite, Footer (Rubriken).

## 3 · Anzeigen – nur seriöse Direktlinks
- Daten: `data/anzeigen.json` → `{id, partner, titel, text, url, bild (mit bilder.json-Eintrag), seiten: [...], von, bis, aktiv}`.
- Darstellung: Label **„Anzeige“** gut sichtbar (Kennzeichnungspflicht für Werbung), Link mit `rel="sponsored noopener"`, optional UTM-Parameter in der URL (kein Skript, kein Pixel).
- **Max. 1 Anzeige pro Seite**, thematisch passend (Sprachschule → Sprachraum, Handwerk → Nachbarschaft nicht!).
- **Nie** auf: Nachbarschaft/Verein, Standpunkte, Melden & Petitionen, Impressum/Datenschutz.
- Ausschluss: Glücksspiel/Wetten, Kredite/Finanzprodukte mit Renditeversprechen, Heilversprechen, Parteiwerbung, Krypto-Spekulation, Escort.
- Abgelaufene Anzeigen (`bis` < heute) baut der Build nicht mehr ein; `check.py` warnt.
- Erlaubte Plätze: Zone 6 auf Ratgeber-, Sprachraum-, Frankfurt-Info- und Vermittlungsseiten; Sprachraum-Startseite als „Partner-Sprachschulen“-Liste (gekennzeichnet).

## 4 · Kultur-Momente (Leben in Frankfurt · Kultur · Religion)
- `data/kultur.json`: `{datum_von, datum_bis, titel, satz, kategorie: [fest|religion|frankfurt|wort], quelle, geprueft}` – **jedes Jahr neu prüfen** (bewegliche Feste wie Ramadan, Ostern, Diwali, Pi Mai, Pohela Boishakh, Meskel).
- Gleichberechtigt: christliche, muslimische, jüdische, hinduistische, buddhistische und weltliche Feste; Frankfurter Termine (Museumsuferfest, Dippemess, Wäldchestag, Weihnachtsmarkt). Ein Satz, respektvoll, ohne Wertung, mit Quelle.
- „Ein Wort Hessisch“ / „Wusstest du?“ – Humor über Frankfurt, nie über Menschen.
- Visuell: Main-Linie (Wellenmotiv, Türkis), Sterne, Skyline – dezent, `prefers-reduced-motion` respektieren.

## 5 · Sprachraum: Diktat-Weg (Prinzip aus Sousse, Inhalte Deutsch)
Pro Niveau 10 Diktate als Lernweg (Zone A). Je Diktat: Szene + Kann-Satz (B), Audio + Transkript (C), Lückentext mit Selbstprüfung und Fehlererklärung + Link zur passenden Grammatik-Karte (D), Wortkarten mit Artikel-Farben **plus** Text (E), druckbare QR-Karte für den Kursraum, lokal erzeugt (F), Frankfurt-Moment (G), interne Links (H), Lehrkraft-Ecke mit Kursplan 10 Sitzungen + Einstiegs-/Abschlusstest (I).
Material aus Sousse (Französisch) wird **nicht** übernommen – nur Ablauf und Didaktik.

### Entscheidung E11 (vorgeschlagen, André bestätigt)
Sofort-Prüfung im Lückentext braucht JavaScript. Vorschlag: **eine** kleine lokale Datei `assets/uebung.js` nur auf Sprachraum-Seiten, ohne Bibliotheken, ohne Datenspeicherung, Seite funktioniert vollständig ohne (Lösungen per `<details>`). Alternative „nur `<details>`“: sicherer, aber weniger motivierend. → in `docs/ENTSCHEIDUNGEN.md` mit Ergebnis eintragen.

## 6 · SEO + KI-Lesbarkeit (Ergänzung zu SEO-RICHTLINIE)
- Semantisches HTML (`main`, `article`, `nav`, `aside`, `figure/figcaption`), Inhalte nie nur in Bildern oder Skripten.
- „Kurz gesagt“ + Frage-Antwort-Abschnitte; Zahlen mit Einheit und Datum; Quellen verlinkt.
- JSON-LD je Seitentyp: `Article`, `BreadcrumbList`, Sprachraum `LearningResource` (mit `educationalLevel` A1/A2/B1, `inLanguage`).
- Optional `llms.txt` (Übersicht der wichtigsten Seiten für KI-Systeme) – ist ein Vorschlag, kein Standard; geringer Aufwand, schadet nicht.
- Bild-Alt-Texte beschreiben den Inhalt, SVG-Grafiken mit `aria-label` bzw. Text-Alternative.

## Aufgaben für Claude Code (nach Phase 3)
| # | Aufgabe | Fertig, wenn |
| --- | --- | --- |
| V1 | Bausteine aus `seitenanatomie.html` als Funktionen in build.py (`kurz_gesagt`, `weiterlesen`, `anzeige`, `kultur_moment`, `durchatmen`, `quellen_autor`) | alle Hauptseiten nutzen sie; Mockup und Ergebnis per Screenshot verglichen |
| V2 | Verlinkungs-Prüfungen aus Abschnitt 2 in check.py + Tests | verwaiste Seite → Fehler (Testfall) |
| V3 | `data/anzeigen.json` + Regeln Abschnitt 3 (Seiten-Ausschluss, Ablaufdatum, Kennzeichnung) | Anzeige auf Vereinsseite → check-Fehler (Testfall) |
| V4 | `data/kultur.json` + Kultur-Moment je Woche (Build wählt nach Datum) | jeder Eintrag mit Quelle + Prüfdatum |
| V5 | Sprachraum-Diktatweg nach `sprachraum-diktatweg.html`, E11 nach Andrés Entscheidung | 2 Beispiel-Diktate A1 vollständig, Lehrkraft prüft |
