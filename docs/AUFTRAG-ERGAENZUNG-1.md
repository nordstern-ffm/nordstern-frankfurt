# Ergänzung zum Claude-Code-Auftrag (15.11.2026) – nach Phase-2-Aufgaben einreihen

Lies: `docs/INHALTE-PRIORITAET.md`, `docs/REDAKTION.md`, `docs/SEO-RICHTLINIE.md`. Alle Arbeitsregeln aus `CLAUDE-CODE-AUFTRAG.md` gelten weiter.

| # | Aufgabe | Fertig, wenn |
| --- | --- | --- |
| S1 | SEO-Prüfungen in `check.py` (alle ✔-Punkte aus SEO-RICHTLINIE) + Testfälle in `tools/test_check.py` | jeder Punkt hat mindestens einen Fehl- und einen Gut-Test |
| S2 | `build.py`: Meta/OG/JSON-LD (`WebSite`, `Organization`, `BreadcrumbList`) je Seite aus `data/site.json`; `sitemap.xml` nur bei Launch | check grün, JSON-LD valide (Struktur per Python geprüft) |
| R1 | Beitragssystem: `data/beitraege/*.md` (Vorlage in REDAKTION) → `/<rubrik>/<slug>/index.html`, Übersicht je Rubrik, `Article`-JSON-LD | Testbeitrag baut; Beitrag ohne Quelle oder `stand` → check-Fehler |
| R2 | Rubriken-Startseiten aus REDAKTION anlegen, Leerzustand freundlich („Erster Beitrag kommt bald“) | Navigation übersichtlich (max. 7 Hauptpunkte, Rest im Footer) |
| R3 | Baustein „Kurz durchatmen“ (ruhige Karte, `prefers-reduced-motion` beachten) am Seitenende | auf allen Hauptseiten, ohne JS |
| R4 | Erste Ratgeber aus Stufe A (INHALTE-PRIORITAET) **neu schreiben**, je Fakt Primärquelle; unbelegte Zahlen → `docs/OFFEN.md` | André gibt jeden Beitrag frei, bevor er auf `main` geht |

**Nicht erlaubt:** Inhalte aus den Ausschluss-Repos (siehe INHALTE-PRIORITAET), Texte aus Zeitungen übernehmen, Beiträge ohne Freigabe von André veröffentlichen.
