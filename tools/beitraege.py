"""Blog-Beiträge aus data/beitraege/*.md – gemeinsam genutzt von build.py und check.py.

Kopf (zwischen ---):  titel, beschreibung, rubrik, slug, stand (JJJJ-MM-TT), freigegeben (ja/nein),
                      bild (Datei aus data/bilder.json), quellen (Schlüssel aus data/links.json, mit Komma).
Text (kleines Markdown):  ## / ### Überschriften · Absätze · "- " und "1. " Listen · "> " Hinweiskasten ·
                      ![](img/…) Bild mit Nachweis · **fett** · [Text](link:schluessel) extern über links.json ·
                      [Text](seite.html) intern (vom Hauptordner aus gedacht).
Kein HTML im Text: alles wird maskiert.
"""
import html, os, re

E = html.escape
PFLICHT = ("titel", "beschreibung", "rubrik", "slug", "stand", "freigegeben", "bild", "quellen")


def lesen(pfad):
    """Gibt (kopf: dict, text: str) zurück."""
    roh = open(pfad, encoding="utf-8").read().replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n(.*)", roh, re.S)
    if not m:
        return {}, roh
    kopf = {}
    for zeile in m.group(1).splitlines():
        if ":" in zeile:
            k, v = zeile.split(":", 1)
            kopf[k.strip()] = v.strip()
    kopf["quellen"] = [q.strip() for q in kopf.get("quellen", "").split(",") if q.strip()]
    return kopf, m.group(2)


def alle(root):
    ordner = os.path.join(root, "data", "beitraege")
    if not os.path.isdir(ordner):
        return []
    return [(d, *lesen(os.path.join(ordner, d))) for d in sorted(os.listdir(ordner)) if d.endswith(".md")]


def ziel(kopf):
    return f'{kopf["rubrik"]}/{kopf["slug"]}/index.html'


def _inline(s, link_fn):
    s = E(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

    def lnk(m):
        text, z = m.group(1), m.group(2)
        if z.startswith("link:"):
            return link_fn(z[5:], text)
        return f'<a href="{z}">{text}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lnk, s)


def html_aus(text, link_fn, bild_fn):
    """Markdown-Teilmenge → HTML. link_fn(schluessel, text), bild_fn(datei)."""
    aus, absatz, liste, kasten = [], [], None, []

    def flush():
        nonlocal absatz, liste, kasten
        if absatz:
            aus.append(f'<p>{_inline(" ".join(absatz), link_fn)}</p>')
            absatz = []
        if liste:
            tag, punkte = liste
            aus.append(f"<{tag}>" + "".join(f"<li>{_inline(p, link_fn)}</li>" for p in punkte) + f"</{tag}>")
            liste = None
        if kasten:
            aus.append('<div class="callout">' + "".join(f"<p>{_inline(k, link_fn)}</p>" for k in kasten) + "</div>")
            kasten = []

    for z in text.split("\n"):
        s = z.strip()
        if not s:
            flush()
        elif s.startswith("### "):
            flush(); aus.append(f"<h3>{_inline(s[4:], link_fn)}</h3>")
        elif s.startswith("## "):
            flush(); aus.append(f"<h2>{_inline(s[3:], link_fn)}</h2>")
        elif m := re.fullmatch(r"!\[\]\(([^)]+)\)", s):
            flush(); aus.append(bild_fn(m.group(1)))
        elif s.startswith("> "):
            if absatz or liste:
                flush()
            kasten.append(s[2:])
        elif m := re.match(r"(- |\d+\. )(.*)", s):
            tag = "ul" if m.group(1) == "- " else "ol"
            if absatz or kasten or (liste and liste[0] != tag):
                flush()
            liste = liste or (tag, [])
            liste[1].append(m.group(2))
        else:
            if liste or kasten:
                flush()
            absatz.append(s)
    flush()
    return "\n".join(aus)
