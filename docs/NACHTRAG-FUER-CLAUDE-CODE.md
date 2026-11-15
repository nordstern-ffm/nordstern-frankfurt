# Nachtrag 15.11.2026 – bitte in die Stammdateien übertragen, dann diese Datei löschen

(Als eigene Datei geliefert, damit der Patch nicht mit deinen Änderungen an FEHLER-LOG.md und ENTSCHEIDUNGEN.md kollidiert.)

## → docs/ENTSCHEIDUNGEN.md
**E12 · Lückentext-Sofortprüfung im Sprachraum** – entschieden von André am 15.11.2026: **JA**.
Eine kleine lokale Datei `assets/uebung.js`, nur auf Sprachraum-Seiten, ohne Bibliotheken, ohne Datenspeicherung; Seite funktioniert vollständig ohne Skript (Lösungen per `<details>`). Alternative „nur `<details>`“ verworfen: weniger motivierend. In `PHASE3B-VISUELL-LINKS-ANZEIGEN.md` steht dafür „E11“ – gemeint ist E12 (E10/E11 hast du bereits vergeben).

## → FEHLER-LOG.md
- **Festtermine aus Reiseseiten sind unzuverlässig** · Recherche Weihnachten: eine Seite listet Bulgarien beim 7. Januar, richtig ist der 25. Dezember (revidierter Kalender) · Regel in `docs/FESTKALENDER-RECHERCHE.md`: nur Quellen der Religionsgemeinschaft oder Fachmedien.
- **Nummernkonflikt Entscheidungen** · Phase-3b-Dokument nannte die JS-Entscheidung E11, obwohl E11 schon vergeben war · Lehre: Nummern nur in `docs/ENTSCHEIDUNGEN.md` vergeben, in anderen Dokumenten „E-neu“ schreiben.

## Neu
- `data/kultur.json`: 3 geprüfte Beispiel-Einträge (Weihnachten 24.–26.12., orthodoxes Weihnachten 6./7.1., Ukraine-Hinweis). Quellen-Links vor Nutzung in `data/links.json` bestätigen.
- `docs/FESTKALENDER-RECHERCHE.md`: Recherche-Plan je Religion/Kultur mit Primärquellen.
