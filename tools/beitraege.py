"""Blog-Beiträge aus data/beitraege/*.md – eigener Mini-Parser (Entscheidung E10, Variante 1).

Nur Standardbibliothek, kein PyYAML, kein markdown-Paket. Läuft auch auf älterem Python (Termux):
keine f-Strings mit Backslash im Ausdruck (siehe FEHLER-LOG).

Unterstützt genau das, was die Beiträge nutzen:
  # / ## / ###, Absätze, "- " Listen, "1. " Listen, **fett**, *kursiv*, `code`, ---,
  einfache Tabellen (| Kopf | … | + Trennzeile | --- | … |)
  Links nur als Platzhalter [[link:schluessel]] → Eintrag aus data/links.json,
  mit eigenem Text: [[link:schluessel|Text]] · interne Seite: [[seite:pfad.html|Text]] (Pfad ab Hauptordner).
  Zeile nur aus [[bild:img/…]] → Bild mit Nachweis aus data/bilder.json (E14) · Zeilen mit "> " → Hinweiskasten.
Alles andere wird als Text ausgegeben (HTML-escaped). Rohe URLs werden nie zu Links.
"""
import glob, html, os, re

E = html.escape
STATUS = ("entwurf", "veroeffentlicht")
LINK_RE = re.compile(r"\[\[link:([a-z0-9_]+)(?:\|([^\]]+))?\]\]")
SEITE_RE = re.compile(r"\[\[seite:([a-z0-9_\-/.#]+)\|([^\]]+)\]\]")
BILD_RE = re.compile(r"\[\[bild:([a-z0-9_\-/.]+)\]\]")
CODE_RE = re.compile(r"`([^`\n]+)`")
TOKEN_RE = re.compile(r"\[\[link:[a-z0-9_]+(?:\|[^\]]+)?\]\]|\[\[seite:[^\]]+\]\]|`[^`\n]+`")
BOLD_RE = re.compile(r"\*\*([^*\n]+)\*\*")
ITAL_RE = re.compile(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])")
OL_RE = re.compile(r"^\d+\.\s+")


def _wert(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def frontmatter(text):
    """Gibt (meta, body) zurück. Erlaubt: key: wert · key: [a, b] · key: + Zeilen '  - eintrag'."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    meta, key = {}, None
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return meta, "\n".join(lines[i + 1:])
        if not line.strip():
            continue
        if line.lstrip().startswith("- ") and key is not None and line[:1] in " \t":
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(_wert(line.lstrip()[2:]))
            continue
        if ":" not in line:
            raise ValueError("Frontmatter-Zeile ohne Doppelpunkt: " + line)
        key, v = line.split(":", 1)
        key, v = key.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            meta[key] = [_wert(x) for x in v[1:-1].split(",") if x.strip()]
        else:
            meta[key] = _wert(v)
    raise ValueError("Frontmatter nicht mit --- abgeschlossen")


def laden(root):
    """Alle Beiträge als Liste von dicts: datei, meta, body."""
    out = []
    for p in sorted(glob.glob(os.path.join(root, "data", "beitraege", "*.md"))):
        with open(p, encoding="utf-8") as f:
            meta, body = frontmatter(f.read())
        out.append({"datei": os.path.relpath(p, root), "meta": meta, "body": body})
    return out


def link_keys(text):
    return [k for k, _ in LINK_RE.findall(text)]


def seiten(text):
    """Interne Ziele aus [[seite:…]] (ohne #Sprungmarke) – für check.py."""
    return [z.split("#")[0] for z, _ in SEITE_RE.findall(text)]


def bilder(text):
    return BILD_RE.findall(text)


def inline(text, link):
    """Escaped Text; [[link:x]] / [[link:x|Text]] über link(x[, Text]), [[seite:…|Text]], `code`, **fett**, *kursiv*."""
    parts, pos = [], 0
    for m in TOKEN_RE.finditer(text):
        parts.append(_fmt(E(text[pos:m.start()], quote=False)))
        tok = m.group(0)
        lm = LINK_RE.fullmatch(tok)
        sm = SEITE_RE.fullmatch(tok)
        if lm:
            parts.append(link(lm.group(1), E(lm.group(2), quote=False)) if lm.group(2) else link(lm.group(1)))
        elif sm:
            parts.append('<a href="' + E(sm.group(1)) + '">' + E(sm.group(2), quote=False) + "</a>")
        else:
            parts.append("<code>" + E(tok[1:-1], quote=False) + "</code>")
        pos = m.end()
    parts.append(_fmt(E(text[pos:], quote=False)))
    return "".join(parts)


def _fmt(s):
    s = BOLD_RE.sub(r"<strong>\1</strong>", s)
    return ITAL_RE.sub(r"<em>\1</em>", s)


TRENN_RE = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?$")


def _zellen(zeile):
    return [z.strip() for z in zeile.strip().strip("|").split("|")]


def _tabelle(zeilen, link):
    kopf, rumpf = _zellen(zeilen[0]), [_zellen(z) for z in zeilen[2:]]
    th = "".join('<th scope="col">' + inline(z, link) + "</th>" for z in kopf)
    tr = "".join("<tr>" + "".join(
        ('<th scope="row">' if i == 0 else "<td>") + inline(z, link) + ("</th>" if i == 0 else "</td>")
        for i, z in enumerate(r)) + "</tr>" for r in rumpf)
    return '<div class="tabelle"><table><thead><tr>' + th + "</tr></thead><tbody>" + tr + "</tbody></table></div>"


def markdown(body, link, bild=None):
    """Block-Parser: Überschriften, Trennlinie, Listen, Tabellen, Absätze, Hinweiskasten, Bilder (bild(datei) → <figure>)."""
    out, para, liste, kasten = [], [], None, []  # liste = ("ul"|"ol", [items])
    tab = []

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), link) + "</p>")
            del para[:]
        if kasten:
            out.append('<div class="callout">' + "".join("<p>" + inline(k, link) + "</p>" for k in kasten) + "</div>")
            del kasten[:]

    def flush_list():
        nonlocal liste
        if liste:
            tag, items = liste
            li = "".join("<li>" + inline(x, link) + "</li>" for x in items)
            out.append("<" + tag + ">" + li + "</" + tag + ">")
            liste = None

    def flush_tab():
        if tab:
            if len(tab) >= 2 and TRENN_RE.match(tab[1]):
                out.append(_tabelle(tab, link))
            else:  # keine gültige Tabelle → als Absatz
                out.append("<p>" + inline(" ".join(tab), link) + "</p>")
            del tab[:]

    for raw in body.split("\n"):
        line = raw.rstrip()
        s = line.strip()
        if s.startswith("|"):
            flush(); flush_list(); tab.append(s); continue
        flush_tab()
        if not s:
            flush(); flush_list(); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            flush(); flush_list()
            n = str(len(m.group(1)))
            out.append("<h" + n + ">" + inline(m.group(2), link) + "</h" + n + ">")
            continue
        if s == "---":
            flush(); flush_list(); out.append("<hr>"); continue
        bm = BILD_RE.fullmatch(s)
        if bm:
            flush(); flush_list()
            if bild is None:
                raise ValueError("[[bild:…]] ohne Bild-Funktion")
            out.append(bild(bm.group(1))); continue
        if s.startswith("> "):
            if para:
                flush()
            flush_list()
            kasten.append(s[2:]); continue
        if kasten:
            flush()
        if s.startswith("- "):
            flush()
            if not liste or liste[0] != "ul":
                flush_list(); liste = ("ul", [])
            liste[1].append(s[2:]); continue
        if OL_RE.match(s):
            flush()
            if not liste or liste[0] != "ol":
                flush_list(); liste = ("ol", [])
            liste[1].append(OL_RE.sub("", s, count=1)); continue
        flush_list()
        para.append(s)
    flush(); flush_list(); flush_tab()
    return "\n".join(out)
