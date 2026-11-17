# Bild-Prompts für KI-Bildgeneratoren (z. B. Nano Banana / Gemini)

Stand 15.11.2026. Für Szenen, zu denen es kein freies Foto gibt. Fotos echter Orte kommen weiter von Wikimedia Commons (Lizenz am Original prüfen, `data/bilder.json`).

## Regeln (UX-KONZEPT Abschnitt 4 + Datenschutz)
1. **Nie als Foto eines echten Ortes ausgeben.** KI-Bilder zeigen typische Szenen, keine erkennbaren Frankfurter Gebäude, keine Wahrzeichen, keine Straßenschilder mit echten Namen.
2. **Keine echten Personen**, keine Ähnlichkeit mit bekannten Menschen, keine Kinder im Vordergrund.
3. **Keine Logos, Marken, Behördenwappen, Parteifarben** (Neutralität, Markenrecht). Keine echten Ausweise oder Formulare mit lesbarem Text.
4. **Kennzeichnung:** In `data/bilder.json` mit `"ki": true`, `autor`: „KI-generiert (Modellname), Prompt: Nordstern“, `quelle_url`: Nutzungsbedingungen des Anbieters, `geaendert`: „KI-generiert“. Die Bildunterschrift zeigt dann „KI-Illustration“. (Feld `ki` wird beim ersten KI-Bild in build.py/check.py eingebaut.)
5. **Nutzungsrechte** des Anbieters vor dem ersten Einsatz lesen (kommerzielle Nutzung auf einer Seite mit gewerblichem Bereich).
6. Export als WebP, 1000 px breit, ≤ 150 KB, Metadaten entfernen.

## Stil-Baustein (an jeden Prompt anhängen)
> Photorealistic, modern editorial photography style, natural soft daylight, calm and warm atmosphere, muted colour palette with deep navy blue (#0B1630) and warm gold (#E0B84A) accents, shallow depth of field, 3:2 landscape, no text, no logos, no brand names, no recognizable real people, no famous landmarks.

## Beitrag „Personalvermittlung gründen“ (Ratgeber)
| Stelle | Szene (Prompt, englisch für bessere Ergebnisse) | Alt-Text (deutsch) |
| --- | --- | --- |
| Abschnitt „Was ist was?“ | A small bright office desk with two coffee cups, a laptop showing an abstract blank screen, a printed CV with unreadable text and a pen, seen from above, two hands about to shake in the background, faces not visible | Schreibtisch mit Laptop, Lebenslauf und zwei Kaffeetassen, im Hintergrund ein Handschlag |
| „In fünf Schritten“ | A neat flat-lay of a notebook with five hand-drawn empty checkboxes, a fountain pen, a calculator and a small potted plant on a light oak table | Notizbuch mit fünf Kästchen zum Abhaken, Stift und Taschenrechner |
| „Was Vermittler verlangen dürfen“ | Close-up of a signed paper contract on a table next to reading glasses, no readable text, a gold paperclip, soft window light | Unterschriebener Vertrag auf einem Tisch, daneben eine Lesebrille |
| „Vermittlungsgutschein“ | A friendly consultation in a modern public office, seen from behind the shoulder of a person, a counsellor’s hands pointing at a paper, faces out of frame | Beratungsgespräch an einem Schreibtisch, Hände zeigen auf ein Blatt Papier |
| „Vermittlung aus dem Ausland“ | A traveller’s backpack and a suitcase standing on a platform of a large generic European train station with an arched glass roof, early morning light, no signs | Rucksack und Koffer auf einem Bahnsteig unter einem Glasdach am Morgen |
| „Checkliste“ | A clipboard with a simple five-item checklist (unreadable placeholder lines, five gold tick marks) on a navy blue background | Klemmbrett mit fünf goldenen Haken |

## Blog-Rubriken (Titelbilder)
| Rubrik | Szene | Alt-Text |
| --- | --- | --- |
| Ratgeber | An open notebook with a hand-drawn step-by-step path of five stars, gold ink on cream paper, on a desk by a window | Notizbuch mit einem gezeichneten Weg aus fünf Sternen |
| Stadtpolitik | A generic historic council chamber with empty wooden seats arranged in a semicircle, warm light, no flags, no coats of arms | Leerer Sitzungssaal mit Holzbänken im Halbkreis |
| Politik | A neutral scale of justice made of brass on a stack of books, navy background, no flags | Messingwaage auf einem Bücherstapel |
| KI & Stadt | A generic modern city intersection at dusk with traffic lights and soft light trails, a subtle abstract network of thin gold lines in the sky, no recognizable buildings, no text | Kreuzung in der Abenddämmerung mit Ampeln und feinen goldenen Linien wie ein Netz |

## Geplante KI-&-Stadt-Beiträge
| Thema | Szene | Alt-Text |
| --- | --- | --- |
| Ampeln mit KI | Close-up of a modern traffic light with a small generic camera sensor on the pole, evening, blurred cars, abstract data dots in gold | Ampel mit kleinem Sensor am Mast, dahinter unscharfe Autos |
| Digitales Rathaus | A person’s hands holding a smartphone showing a generic form with abstract fields, sitting on a park bench, city greenery in the background | Hände halten ein Smartphone mit einem Online-Formular, im Hintergrund Grün |
| Mängel mit KI sortieren | A cracked pavement with a small pothole, a smartphone held above it taking a picture, the screen shows a generic map pin | Smartphone fotografiert ein Schlagloch, auf dem Bildschirm eine Kartennadel |
