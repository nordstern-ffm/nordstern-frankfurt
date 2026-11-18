# Nordstern Frankfurt

GitHub-Konto: **nordstern-ffm** (eigenes Konto, getrennt von intelligentresponder-max). Repo: nordstern-ffm/nordstern-frankfurt.

Sozial. Informiert. Vernetzt. – Dachseite für den Frankfurter Norden.
Briefing: [CLAUDE.md](CLAUDE.md) · Entscheidungen: [docs/ENTSCHEIDUNGEN.md](docs/ENTSCHEIDUNGEN.md) · Domain: [docs/DOMAIN-SETUP.md](docs/DOMAIN-SETUP.md) · Fehler: [FEHLER-LOG.md](FEHLER-LOG.md)

## Bauen (Termux oder Git Bash)
```bash
python3 tools/build.py      # erzeugt alle .html aus data/*.json
python3 tools/check.py      # 0 Fehler = darf gepusht werden
python3 tools/test_check.py # nur nach Änderung an check.py: Bildrechte-Prüfung testen
```
Lokal ansehen: `python3 -m http.server 8000` → http://localhost:8000

## Struktur
| Pfad | Inhalt |
| --- | --- |
| `data/site.json` | Marke, Betreiber, Domain, **Launch-Schalter** |
| `data/dienste.json` | Vermittlungsangebote (+ interne Prüfpunkte) |
| `data/petitionen.json` | Anliegen, Ziel 220 Unterstützer |
| `data/standpunkte.json` | FW-Positionen, nur `freigegeben: true` wird gezeigt |
| `data/zahlung.json` | Agentur-Pakete mit Stripe-/Gumroad-Zahlungslink (erst sichtbar mit Preis + Link) |
| `data/links.json` | Nur im Browser bestätigte externe Links |
| `data/zahlen.json` | Kennzahlen nur mit Primärquelle, Fundstelle und Stand (Unbelegtes → `docs/OFFEN.md`) |
| `data/bilder.json` | Pflicht-Nachweis für jedes Bild (Urheber, Lizenz, Quelle, Prüfdatum, Alt-Text) → `bildnachweise.html` |
| `tools/build.py`, `tools/check.py`, `tools/test_check.py` | Generator, Prüfung, Test der Prüfung |
| `css/`, `fonts/` | Gestaltung, lokale Schriften (SIL OFL) |

Status: **Vorschau** (`noindex`, kein CNAME), bis Impressumsdaten und Domain eingetragen sind.
