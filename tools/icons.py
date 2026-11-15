#!/usr/bin/env python3
"""Baut assets/icons.svg (ein <symbol> je Icon) aus heruntergeladenen Lucide-SVGs.

Nur bei neuen Icons nötig – nicht Teil des normalen Builds.
1. Lucide-Version festlegen (VERSION) und Namen in ICONS ergänzen.
2. SVGs in einen eigenen, leeren Ordner laden, z. B. in Git Bash:
     for n in house mail; do curl -sf -o "$n.svg" "https://unpkg.com/lucide-static@1.73.0/icons/$n.svg"; done
3. python3 -I tools/icons.py ORDNER
Aus den Downloads werden nur Geometrie-Elemente mit Geometrie-Attributen übernommen
(keine Skripte, Links, Stile) – fremde Dateien gelten als nicht vertrauenswürdig.
"""
import os, sys, xml.etree.ElementTree as ET

VERSION = "1.73.0"
ICONS = [
    # Navigation und Säulen
    "house", "hand-heart", "landmark", "megaphone", "handshake", "flag", "briefcase",
    # Familie, Nachbarschaft, Frankfurt
    "languages", "route", "users", "shopping-basket", "user-search", "building-2", "map-pinned", "laptop",
    # Vermittlung (data/dienste.json → icon)
    "bed-double", "car-taxi-front", "sparkles", "scissors", "zap", "shopping-bag",
    # Agentur, Kontakt
    "layout-template", "pen-line", "wrench", "package", "mail",
    # Abläufe (data/ablaeufe.json → icon)
    "eye", "message-circle", "send", "search",
]
ERLAUBT = {
    "path": {"d"}, "circle": {"cx", "cy", "r"}, "ellipse": {"cx", "cy", "rx", "ry"},
    "line": {"x1", "y1", "x2", "y2"}, "polyline": {"points"}, "polygon": {"points"},
    "rect": {"x", "y", "width", "height", "rx", "ry"},
}
NS = "{http://www.w3.org/2000/svg}"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def symbol(ordner, name):
    svg = ET.parse(os.path.join(ordner, name + ".svg")).getroot()
    if svg.get("viewBox") != "0 0 24 24":
        raise SystemExit(f"{name}: unerwartete viewBox {svg.get('viewBox')}")
    teile = []
    for el in svg.iter():
        tag = el.tag.replace(NS, "")
        if el is svg:
            continue
        if tag not in ERLAUBT:
            raise SystemExit(f"{name}: Element <{tag}> nicht erlaubt")
        attr = " ".join(f'{k}="{v}"' for k, v in el.attrib.items() if k in ERLAUBT[tag])
        teile.append(f"<{tag} {attr}/>")
    return f'<symbol id="{name}" viewBox="0 0 24 24">{"".join(teile)}</symbol>'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    syms = "\n".join(symbol(sys.argv[1], n) for n in ICONS)
    out = os.path.join(ROOT, "assets", "icons.svg")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg">\n<!-- Lucide v{VERSION}, ISC-Lizenz, '
                f'siehe assets/LICENSE-icons.txt · https://lucide.dev -->\n{syms}\n</svg>\n')
    print(f"{len(ICONS)} Icons -> assets/icons.svg ({os.path.getsize(out)} Bytes)")
