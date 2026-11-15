# SEO-Richtlinie Nordstern (erweitert aus tools/SEO-ROUTINE.md)

Grundsatz: E-E-A-T + hilfreicher Inhalt + Suchabsicht. Für Menschen schreiben, Technik sauber.
`tools/check.py` prüft jeden Punkt mit ✔ automatisch – **Claude Code baut diese Prüfungen ein (Aufgabe S1)**.

## Pro Seite (automatisch geprüft)
- ✔ `<title>` 50–60 Zeichen, eindeutig, Keyword vorne
- ✔ `meta description` 150–160 Zeichen, eindeutig
- ✔ genau **ein** `<h1>`; Überschriften ohne Sprünge (h2 → h3)
- ✔ `canonical` (nach Launch), `og:title`, `og:description`, `og:image` (eigenes Bild mit Nachweis), `og:locale`
- ✔ `lang` korrekt; bei Übersetzungen `hreflang` gegenseitig + `x-default`
- ✔ jedes Bild: Alt-Text, sprechender Dateiname, `width`/`height`, ≤ 150 KB, WebP/AVIF
- ✔ interne Links mit beschreibendem Text (kein „hier klicken“), keine toten Links
- ✔ URLs: klein, Bindestriche, keine Umlaute, kurz (`/nachbarschaft/entlastungsbetrag/`)

## Seitenweit
- ✔ `sitemap.xml` (alle indexierbaren Seiten, `lastmod` aus `stand`) – erst nach Launch in `robots.txt` eintragen
- ✔ `robots.txt`: Vorschau `Disallow: /`, nach Launch `Allow` + Sitemap-Zeile
- ✔ `404.html` mit Links zu den Hauptbereichen
- Strukturierte Daten (JSON-LD), nur was wahr ist:
  - `WebSite` + `Organization` (Name, Logo, Kontakt nach Impressum)
  - `BreadcrumbList` auf Unterseiten
  - `Article` für Beiträge (`datePublished`, `dateModified`, `author` = echte Person)
  - `FAQPage` darf genutzt werden, bringt aber laut Google seit 2023 für normale Websites meist **keine** Sonderanzeige mehr → kein Muss
  - **kein** `LocalBusiness` ohne echte Geschäftsadresse
- Core Web Vitals: LCP < 2,5 s, CLS < 0,1, INP < 200 ms (mobil, Lighthouse)

## Inhalt (Redaktion prüft)
- Suchabsicht vor dem Schreiben festlegen (Info / Navigation / Handlung)
- Erster Absatz beantwortet die Frage direkt (auch für KI-Suche zitierfähig: kurz, mit Zahl und Datum)
- Quellen am Ende, „Stand“ sichtbar, bei Änderung `dateModified` aktualisieren
- Autorenbox mit echter Person und Erfahrung (E-E-A-T)
- Keine Keyword-Häufung, keine Doppelseiten (gleiche Frage = eine Seite), keine automatisch vervielfältigten Stadtteil-Seiten mit Austauschtext
- Mehrsprachig nur mit echter Übersetzung (Muttersprachler gegenlesen), nie maschinell ungeprüft

## Nach Launch (Domain)
- Google Search Console + Bing Webmaster Tools anmelden (Verifizierung per DNS-TXT, keine Tracking-Skripte)
- Sitemap einreichen, Indexierung/Fehler wöchentlich prüfen
- Alte Seiten (bangla-hilfe, wege-nach-frankfurt) mit `canonical`/Weiterleitungsseite auf die neue Domain zeigen lassen
