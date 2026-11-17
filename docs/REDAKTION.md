# Redaktionsplan – viel Inhalt, übersichtlich, entspannt

## Ziel (Andrés Vorgabe, 15.11.2026)
So viel guten Inhalt übersichtlich anhäufen, dass die **Relevanz der Seite steigt** – für Frankfurter, für Menschen, die nach Frankfurt kommen, und für Interessierte im Ausland. Die Seite soll informieren **und erheitern**. Grundgefühl: **entspannt** (Ton wie mindful7777).

## Wichtigste Regel: Qualität skaliert, Masse nicht
Google stuft massenhaft erzeugte, dünne Seiten als Spam ein („scaled content abuse“). Also: **jeder Beitrag mit eigenem Mehrwert** – eigene Erfahrung, lokale Einordnung, geprüfte Quelle. Lieber 2 starke Beiträge pro Woche als 20 schwache. Kein Beitrag ohne menschliche Endkontrolle durch André.

## Rubriken
| Rubrik | Inhalt | Rhythmus | Zielgruppe |
| --- | --- | --- | --- |
| **Aus dem Römer** | Was Stadtverordnetenversammlung und Magistrat beschlossen haben, in 5 Sätzen + „Was heißt das für den Norden?“ | wöchentlich | Frankfurter |
| **Aus dem Ortsbeirat 10** | Anträge, Termine, Ergebnisse | nach Sitzung | Nachbarschaft |
| **Bürgerdialog** | Was Bürger auf ffm.de vorschlagen und melden, gebündelt nach Themen (keine Personendaten) | monatlich | Frankfurter |
| **Standpunkt-Check** | Eine Stadt-Meldung neben die passende FW-Position stellen: „Das wurde beschlossen – das sagen die FREIEN WÄHLER dazu“ (klar gekennzeichnet, nur freigegebene Positionen) | bei Anlass | politisch Interessierte |
| **Ratgeber** | Behörde, Pflege, Energie, Wohnen – Schritt für Schritt | 1–2 pro Woche | alle |
| **Ankommen in Frankfurt** | für Neue aus dem Ausland (DE/EN, später bn, ti, th, lo) | 2 pro Monat | international |
| **Frankfurt zum Schmunzeln** | Mundart-Wörterbuch („Ei Gude“), Kuriositäten, Ebbelwoi-Kultur, Stadtteil-Anekdoten, Rätsel/Quiz | wöchentlich | alle, auch Ausland |
| **Kurz durchatmen** | 60–90 Sekunden Ruhe: Lieblingsorte im Grünen (Nidda, Grüngürtel), Atempause, ein Satz zum Tag | wöchentlich | alle |

## Quellen (nur Primärquellen, Link vor Nutzung im Browser bestätigen → `data/links.json`)
- Pressemitteilungen der Stadt Frankfurt (frankfurt.de) · Parlamentsinformationssystem PARLIS (Beschlüsse, Anträge, Ortsbeiräte) · ffm.de (Mängelmelder, Ideenplattform, Bürgerdialog) · Statistik der Stadt Frankfurt · Gesetzestexte (gesetze-im-internet.de, rv.hessenrecht.hessen.de)
- Zeitungen (FR, FNP, hessenschau): **nur verlinken und in eigenen Worten einordnen**, nie Absätze übernehmen; Zitate unter 15 Wörtern, eines pro Quelle.

## Neutralitäts-Regel
„Aus dem Römer“, „Ortsbeirat“, „Bürgerdialog“ = **neutral berichten**, alle Fraktionen gleich behandeln. Wertung nur im gekennzeichneten „Standpunkt-Check“. Der Verein Nachbarschaftshilfe wird nie mit Parteiinhalten verknüpft.

## Ton (entspannt, nach mindful7777)
- Kurze Sätze. Ein Gedanke pro Absatz. Viel Weißraum.
- Freundlich, nie alarmistisch: keine „Letzte Chance!“, keine Ausrufezeichen-Ketten, keine Angstbilder.
- Humor über Frankfurt, nie über Menschen oder Gruppen.
- Jede Seite hat einen ruhigen Abschluss (z. B. „Kurz durchatmen“-Karte).

## Beitrags-Vorlage (`data/beitraege/JJJJ-MM-TT-slug.md`)
```
---
titel: (50–60 Zeichen, Keyword vorne)
beschreibung: (150–160 Zeichen)
rubrik: aus-dem-roemer
stand: 2026-11-15
quellen:
  - titel: … | url: … | abgerufen: 2026-11-15
sprachen: [de]
---
Kurzfassung in 3 Sätzen (zitierfähig, mit Zahl/Datum).
## Was ist passiert?
## Was heißt das für den Frankfurter Norden?
## Mehr dazu (Quellen)
```
