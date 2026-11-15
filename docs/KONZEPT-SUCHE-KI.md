# Konzept: Glossar, Suche und KI-Chat (Stand 15.11.2026)

Auftrag André: KI-Such- und Chatbot mit ausführlichem Glossar – **erst nach Abschluss aller inhaltlichen Aufgaben**.
Leitlinie: Die Seite bleibt ohne Skript vollständig nutzbar (E4, E12, E15). Jede Stufe ist für sich nützlich.

## Stufe 1 · Glossar (ohne JavaScript, sofort machbar)
- `data/glossar.json`: Begriff, Kurz-Erklärung (1–2 Sätze, einfache Sprache), ausführliche Erklärung, Quelle (Schlüssel in `links.json`), Stand, verwandte Begriffe, Sprachen (de, später en/bn/ti/th/lo).
- `glossar.html` mit A–Z-Sprungleiste (wie Blog-Chips), jeder Begriff mit eigener Sprungmarke `#begriff`.
- build.py verlinkt den **ersten** Treffer eines Begriffs in Beiträgen automatisch auf das Glossar.
- check.py: jeder Eintrag mit Quelle und Stand, keine doppelten Begriffe, jeder Querverweis existiert.
- Startbestand aus vorhandenen Inhalten: Ortsbeirat, Magistrat, Stadtverordnetenversammlung, Entlastungsbetrag, Chancenkarte, Vermittlungsgutschein, AZAV, Arbeitnehmerüberlassung, Gewerbeanzeige, Bürgerfragestunde …
- Später (S2): `DefinedTermSet` als JSON-LD – gut für Suchmaschinen und KI-Antwortdienste.

## Stufe 2 · Suche auf der Seite (kleines lokales Skript)
- build.py erzeugt `assets/suche.json` (Titel, Kurztext, Adresse aller Seiten, Beiträge, Glossar).
- `assets/suche.js` (wenige KB, ohne Bibliothek) sucht nur in dieser Datei – keine Anfrage verlässt den Browser, nichts wird gespeichert.
- Ohne Skript: Seite `suche.html` zeigt das vollständige A–Z-Verzeichnis.
- **Braucht eine Entscheidung (E-neu):** E12 auf die Suche erweitern; CSP auf `suche.html` `script-src 'self'`; check.py-Liste der Seiten mit Skript.
- Alternative: Pagefind (fertige statische Suche) – verworfen, solange es ein Fremdwerkzeug im Build bräuchte.

## Stufe 3 · „KI-lesbar“ (ohne eigenen Bot)
- `llms.txt` und saubere Zusammenfassungen („Kurz gesagt“) je Seite, damit KI-Assistenten Nordstern korrekt finden und zitieren.
- Kostet nichts, keine Daten, kein Risiko.

## Stufe 4 · KI-Chat (erst nach Umzug zum EU-Hoster, TODO P1)
- **Antwortet nur aus eigenen Inhalten** (Seiten, Beiträge, Glossar, `zahlen.json`) und nennt immer die Quelle mit Link; sonst: „Dazu haben wir nichts – hier ist die zuständige Stelle.“
- Technik: kleine Serverfunktion beim EU-Hoster, die die Frage mit passenden Textstellen an ein KI-Modell schickt (Claude über die Anthropic-API oder EU-Anbieter). Schlüssel nur auf dem Server, nie im Browser.
- Schutz: Ratenbegrenzung, kein Speichern der Fragen, Hinweis „Keine Gesundheits-, Rechts- oder Finanzdaten eingeben“, keine Rechts-/Steuer-/Medizinberatung, Parteipositionen nur mit Verweis auf „Standpunkte“.
- **Datenschutz (Recht/Datenschutz-Abwägung, großes Modell + Fachprüfung):** Fragen können Gesundheit oder politische Meinung enthalten (Art. 9 DSGVO); Auftragsverarbeitungsvertrag mit dem KI-Anbieter, Drittland-Prüfung, Datenschutzerklärung ergänzen, ggf. Datenschutz-Folgenabschätzung.
- Kosten: Modell und Preise erst zum Zeitpunkt des Baus aktuell prüfen; Obergrenze pro Monat festlegen.
- Fallback: ohne Skript oder bei Ausfall führt der Chat-Platz zur Suche und zum Glossar.

## Entscheidungen André (15.11.2026) → E20
1. **Kein KI-Chat.** Stufe 4 entfällt (kein Server, kein KI-Anbieter, keine Datenschutz-Folgenabschätzung nötig).
2. **Suche: ja**, als lokale Seitensuche mit einfacher Interaktion „wie in einem Repo“ (GitHub-Stil):
   - Taste `/` springt ins Suchfeld, Ergebnisse erscheinen beim Tippen, Pfeiltasten + Enter wählen aus, `Esc` leert.
   - Filter-Chips: Alle · Seiten · Blog · Glossar; Treffer zeigen Titel, Bereich und Kurztext mit hervorgehobenem Suchwort.
   - Ohne Skript: `suche.html` zeigt das vollständige A–Z-Verzeichnis (gleiche Daten).
3. **Glossar viersprachig: Deutsch, Englisch, Spanisch, Französisch.**
   - Deutsch ist Referenz (mit Quelle + Stand); jede Übersetzung trägt `geprueft_von` (Rolle, kein Name ohne Einwilligung) und Datum – ungeprüfte Übersetzungen werden nicht gebaut.
   - Fachbegriffe ohne Entsprechung bleiben deutsch und werden erklärt (z. B. „Ortsbeirat – local district council“).
   - Seiten: `glossar.html` (de) mit Sprachumschalter zu `en/glossary.html`, `es/glosario.html`, `fr/glossaire.html`; `lang`/`hreflang` je Sprache (P1).
   - Die Suche findet Begriffe in allen vier Sprachen.
