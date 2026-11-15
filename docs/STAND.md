# Stand für die nächste Claude-Code-Sitzung (15.11.2026)

Kurzfassung dessen, was erledigt ist und worauf man achten muss. Details: `docs/ENTSCHEIDUNGEN.md` (E10–E15), `FEHLER-LOG.md`, Reihenfolge der offenen Aufgaben: `docs/TODO-MASTER.md`, Unbelegtes: `docs/OFFEN.md`.

## Branch und Arbeitsweise
- Arbeit auf `ux-phase2`, nicht auf `main` (main = live auf GitHub Pages). **Nicht gepusht** – Push und PR macht André.
- Vor jedem Commit: `python tools/build.py && python tools/check.py && python tools/test_check.py` → 0 Fehler.
- Lokal ansehen: `python -m http.server 8000` im Repo-Ordner, dann http://localhost:8000/ (Icons laden nicht per Doppelklick/`file://`).

## Erledigt (Phase 2, Aufgaben 1–4 + Härtung)
| Was | Wo | Entscheidung |
| --- | --- | --- |
| Bildrechte: jedes Bild nur mit vollständigem Eintrag, Seite `bildnachweise.html` | `data/bilder.json`, `bild()` in build.py | E10 |
| Icon-System: 30 Lucide-Symbole lokal, Lizenzdatei, `icon()` | `assets/icons.svg`, `tools/icons.py` | E11 |
| Lokale Skripte für Lern-/Spiel-Elemente erlaubt (noch nicht gebaut) | – | E12 (André) |
| Kennzahl-Kacheln mit Primärquelle + Stand (15.896 Preungesheim, 781.337 Frankfurt, bis 131 €) | `data/zahlen.json`, `kacheln()` | E13 |
| Ablauf-Diagramme + Zeitleiste, Screenreader-Reihenfolge geprüft | `data/ablaeufe.json`, `steps()`, `timeline()` | E14 |
| Content-Security-Policy + Referrer-Policy, Sicherheitsprüfung über alle HTML/CSS im Repo | build.py-Kopf, check.py Abschnitte 8–10 | E15 |
| Kontrast Hellmodus (Gold #8A6A10), fehlende h2 auf 4 Seiten ergänzt | `css/style.css`, build.py | – |
| Andrés Patches (Ergänzung 1, Phase 3, 3b, Kultur, Weltstadt) eingespielt, Nachtrag übertragen | `docs/*` | – |

## Was `check.py` heute erzwingt (24 Testfälle in `tools/test_check.py`)
Bilder mit Nachweis und Alt-Text · Icons vorhanden und korrekt versteckt · Kennzahlen mit Quelle/Stand · **in allen HTML-Dateien des Repos** kein `<script>`, keine `on…=`-Handler, keine `javascript:`-Links, kein `<form>/<iframe>/<object>/<embed>/<base>`, keine Fremdabrufe, `target=_blank` nur mit `noopener` · CSS ohne `@import`/externe `url()` · Hauptseiten mit CSP, Referrer-Policy, `lang`, `<title>`, genau einer h1, ohne Überschriften-Sprünge, ohne doppelte IDs, Sprungmarken mit Ziel · alle `data/*.json` gültig, alle Links https · noindex im Vorschau-Modus.

## Achtung
- **Repo ist öffentlich und Pages veröffentlicht das ganze Repo** (`.nojekyll`). Interna nur in `docs/intern/` und `data/intern/` (ignoriert). Alte Fassungen stecken noch in der Git-Historie (siehe `docs/OFFEN.md`).
- E12-Freigabe für Skripte erst mit der ersten Sprachraum-/Quiz-Seite in check.py einbauen (Seitenliste + CSP `script-src 'self'` nur dort).
- frankfurt.de / ffm.de blocken Skript-Abrufe (403) → solche Quellen im Browser prüfen.
- Nächste Aufgabe: Phase 2 / 6 Schema-Karte Ortsbezirk 10 (Stadtteile laut StVV-Broschüre, ODbL-Hinweis).
- Erledigt seit Erststand: Datenschutz-Bereinigung (E16), Blog-Reiter (E17), Beitragssystem + Artikel Personalvermittlung als Entwurf (E18), Schaubild (E19).
