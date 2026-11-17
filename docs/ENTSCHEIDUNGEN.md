# Entscheidungen – Alternativen doppelt geprüft (Nutzen / Sicherheit / neuer Weg)

## E1 · Eine Marke, getrennte Verantwortung
**Gewählt:** Nordstern als Dach, betrieben von André / Copy & Code Agency. Verein, Partei und Vermittlung je in eigenem, gekennzeichnetem Bereich.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Alles als Vereinsseite | ein Absender | **Gemeinnützigkeit in Gefahr**: Ein gemeinnütziger Verein darf keine Partei fördern (§ 55 Abs. 1 Nr. 1 AO) und keine gewerbliche Vermittlung im Vordergrund haben | verworfen |
| Alles gemischt ohne Kennzeichnung | einfach | Glaubwürdigkeit leidet; Senioren, die Hilfe suchen, landen bei Parteiwerbung | verworfen |
| **Dach + Bereiche** | Reichweite wird geteilt, Risiken getrennt | Verein verlinkt nicht zurück auf Partei/Geschäft | **gewählt** – vor Gründung mit Steuerberatung bestätigen |

## E2 · Mängelmelder
**Gewählt:** Verlinken auf den städtischen Mängelmelder (ffm.de). Eigener Melder hätte Fotos mit Standort/Personen (DSGVO), Moderation und keine Weiterleitung an die Verwaltung bedeutet. **Neuer Weg später:** Monatlicher Blogbeitrag „Was im Norden gemeldet wurde“ – Mehrwert ohne Datenhaltung.

## E3 · Petitionen „220 Bürger“
**Gewählt:** Anliegen hier vorstellen und Fortschritt zeigen; Unterschriften extern (ffm.de-Ideenplattform oder openPetition). Eigene Unterschriftenliste = politische Meinung = besondere Kategorie (Art. 9 DSGVO) → zu riskant für eine statische Seite. Zahl 220 steht nur in `data/petitionen.json`.
**Zu prüfen:** Gilt für ffm.de-Ideen wirklich eine 200er-Schwelle? (laut Bürgerplattform-FEHLER-LOG unbestätigt). Für ein Bürgerbegehren gelten andere, viel höhere Quoren (HGO § 8b).

## E4 · Technik
**Gewählt:** Statisches HTML aus Python-Skript, kein JS, kein npm. Läuft in Termux.
| Alternative | Warum nicht |
| --- | --- |
| React (wie Frankfurt_FW-Wurzel) | Build-Kette, auf Termux fehleranfällig, für Infoseite unnötig |
| Tailwind-CDN | Besucher-IP an Dritte; laut eigenem FEHLER-LOG bereits einmal ersetzt |
| WordPress | Hosting-Kosten, Updates, Angriffsfläche |
| **Neuer Weg geprüft:** Eleventy/Hugo | sinnvoll ab ~30 Seiten/Blog; bis dahin reicht build.py |

## E5 · Hosting & Domain
**Gewählt (Start):** GitHub Pages + eigene Domain (kostenlos, HTTPS automatisch).
**Später:** EU-Hoster (z. B. ein deutscher Anbieter mit statischem Hosting), weil Pages in den USA liegt – steht ehrlich in der Datenschutzerklärung.

## E6 · Kontakt
**Gewählt:** `mailto:`-Link. Formspree (früher in copy-code-agency genutzt) = US-Dienst, Formulardaten außerhalb der EU → verworfen. Später EU-Formulardienst prüfen.

## E7 · Vermittlung – Risiken je Dienst (nicht öffentlich, steht in `data/dienste.json` → `pruefen`)
- Personal: private Arbeitsvermittlung ist erlaubnisfrei, Gewerbeanmeldung genügt; Zeitarbeit braucht AÜG-Erlaubnis, Vermittlungsgutscheine eine AZAV-Zulassung.
- Hotel: Interessenkonflikt mit eigenem Arbeitgeber vorab klären.
- Taxi: nur vermitteln, nicht befördern (Personenbeförderungsgesetz).
- Massage: nur Fachpersonal, keine Heilversprechen, strikt getrennt vom Projekt STAFF.
- Nähen: Status der Näherinnen klären (Scheinselbstständigkeit).
- Strom & Gas (TeleSon): vorbereitet, `aktiv: false`. Vertragsform (Handelsvertreter?), Provision offen nennen, Markenname nur mit Freigabe.
- Amway: vorbereitet, `aktiv: false`. Website-/Social-Media-Regeln von Amway für Geschäftspartner vorher lesen; keine Einkommens- oder Heilversprechen; Kennzeichnung „unabhängiger Geschäftspartner“.

## E8 · Bezahlen (Gumroad oder Stripe)
**Gewählt:** Gehostete Zahlungsseite per Link (Stripe Payment Link oder Gumroad) in `data/zahlung.json`. Kein eigener Checkout-Code, keine Kartendaten, kein Server.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Eigenes Stripe-Backend (wie mindful7777/stripe-api auf Vercel) | Abos, Kundenportal | Secrets, Webhooks, Server – dort schon Fehler „STRIPE_SECRET_KEY is not set“ | erst wenn Abos nötig |
| Gumroad | sofort startklar, übernimmt Steuern als Händler | höhere Gebühr, eher für digitale Produkte | gut für Vorlagen/E-Books |
| **Stripe Payment Link** | Dienstleistungen mit Festpreis, eigenes Branding | gehostet von Stripe | **gewählt für Agentur-Pakete** |
Wichtig: eigenes Stripe-Konto für die Agentur (nicht das von Gumroad verwaltete bangla-hilfe-Konto, nicht das mindful7777-Konto). Pakete erscheinen erst mit `aktiv`, Preis und Link. Preise legen André und Sam fest.

## E9 · Verknüpfung mit BanglaHilfe und wege-nach-frankfurt
**Gewählt:** Nordstern verlinkt beide auf Start („Nordstern-Familie“) und Frankfurt-Info; Links am 15.11.2026 erreichbar geprüft (HTTP 200). **Rückverlinkung** aus beiden Repos erst nach Domain-Start (sonst zeigen sie auf eine `noindex`-Vorschau). Repos bleiben eigenständig – kein Zusammenlegen, damit sie einzeln verkaufbar bleiben (Repo-Verkauf).

## E11 · Umfang: Variante A, entschieden 17.11.2026 (Nutzer)
**Gewählt:** Start mit Ortsbezirk 10 (Berkersheim, Bonames, Eckenheim, Frankfurter Berg, Preungesheim). Die Struktur (Pflichtfeld `ortsbezirk` 1–16 in Beiträgen, Tabelle in `docs/BETREUUNG.md`) ist für alle 16 Ortsbezirke angelegt. Weitere Bezirke gehen erst online, wenn jemand sie dauerhaft betreut.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| **A · OBR 10 zuerst, Struktur für alle 16** | Qualität dort, wo wir uns auskennen; Ausbau ohne Umbau | jede Angabe hat eine verantwortliche Person, die Quellen prüft | **gewählt** |
| B · ganze Stadt sofort | große Reichweite ab Tag 1 | 16 Bezirke ohne Betreuung → veraltete Termine, ungeprüfte Angaben, Glaubwürdigkeit leidet; Rechercheaufwand vervielfacht sich, solange PARLIS/frankfurt.de in der Cloud-Umgebung gesperrt sind | verworfen |
| C · nur Frankfurter Norden, keine Struktur für mehr | am einfachsten | spätere Erweiterung braucht Umbau (Datenmodell, Navigation); Name „Frankfurt“ verspricht mehr, als die Seite hält | verworfen |
