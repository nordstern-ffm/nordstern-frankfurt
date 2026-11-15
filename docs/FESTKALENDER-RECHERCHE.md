# Festkalender – Recherche-Plan (Kultur-Momente)

Ziel: Für jedes Jahr ein geprüfter Kalender in `data/kultur.json` – alle Kulturen und Religionen gleichberechtigt, Frankfurter Termine, „ein Wort Hessisch“.

## Lehre aus dem Beispiel Weihnachten (15.11.2026)
Quellen widersprechen sich: Eine Reiseseite nennt Bulgarien beim 7. Januar, tatsächlich feiern die bulgarische, rumänische und griechische Kirche am 25. Dezember (revidierter Kalender). Die Orthodoxe Kirche der Ukraine wechselte 2023 zum 25. Dezember, die Ukrainische Orthodoxe Kirche (früher Moskau) blieb laut Berichten beim 7. Januar. → **Regel: Termine nur aus Quellen der Religionsgemeinschaft selbst oder seriösen Kirchen-/Fachmedien; Reise- und Ratgeberseiten nie als alleinige Quelle.** (Eintrag auch im FEHLER-LOG.)

## Recherche je Bereich (jährlich, im Oktober für das Folgejahr)
| Bereich | Feste (Auswahl) | Primärquelle |
| --- | --- | --- |
| Christlich (kath./ev.) | Advent, Heiligabend, Ostern, Pfingsten | Bistum Limburg (Frankfurt gehört dazu), EKD, Ev. Kirche in Hessen und Nassau |
| Christlich-orthodox | Weihnachten 7. Januar (julianisch), orthodoxes Ostern | Orthodoxe Bischofskonferenz in Deutschland, jeweilige Gemeinde in Frankfurt |
| Eritreisch/äthiopisch-orthodox | Genna (Weihnachten), Timkat, Meskel | Eritreisch-orthodoxe Gemeinde – Kontakt über wege-nach-frankfurt |
| Jüdisch | Pessach, Rosch ha-Schana, Jom Kippur, Chanukka | Jüdische Gemeinde Frankfurt, Zentralrat der Juden |
| Muslimisch | Ramadan, Eid al-Fitr, Eid al-Adha | Moscheegemeinden/Verbände; **Datum hängt vom Mond ab → „voraussichtlich“** |
| Hinduistisch / bengalisch | Diwali, Durga Puja, Pohela Boishakh (bengal. Neujahr) | Gemeinden in Frankfurt, BanglaHilfe-Kontakte |
| Buddhistisch / Laos, Thailand | Pi Mai Lao, Songkran, Vesakh | Tempel/Vereine in Rhein-Main, Monis Kontakte |
| Frankfurt | Dippemess, Wäldchestag, Museumsuferfest, Weihnachtsmarkt, Lichter Filmfest | frankfurt.de, Veranstalter |
| Ein Wort Hessisch | „Ei Gude“, „Bembel“, „Stöffche“ | eigene Erfahrung + Mundart-Wörterbuch |

## Ablauf
1. Liste der Feste fürs Folgejahr anlegen (Tabelle oben).
2. Je Fest: Datum + ein Satz + Quelle + `geprueft` → `data/kultur.json`.
3. Bewegliche/mondabhängige Feste mit „voraussichtlich“ kennzeichnen und eine Woche vorher nachprüfen.
4. Bei Unsicherheit: Gemeinde fragen statt raten. Unbestätigtes → `docs/OFFEN.md`.

Vorschlag: Diese Jahresrecherche als **Deep Research** im Claude-Chat laufen lassen (ein Bericht pro Jahr mit allen Quellen), danach überträgt Claude Code die bestätigten Einträge.
