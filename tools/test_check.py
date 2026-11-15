#!/usr/bin/env python3
"""Testet Bildrechte-, Icon-, Kennzahl-, Sicherheits- und Struktur-Prüfung in check.py an einer Kopie des Repos.

Aufruf im Repo-Hauptordner:  python3 tools/test_check.py
Das echte Repo wird nicht verändert.
"""
import json, os, shutil, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEBP = b"RIFF\x1a\x00\x00\x00WEBPVP8L\x0d\x00\x00\x00\x2f\x00\x00\x00\x10\x07\x10\x11\x11\x88\x88\xfe\x07\x00"
EINTRAG = {"datei": "img/test.webp", "titel": "Testbild", "autor": "Testautor",
           "quelle_url": "https://commons.wikimedia.org/wiki/File:Test.webp", "lizenz": "CC0 1.0",
           "lizenz_url": "https://creativecommons.org/publicdomain/zero/1.0/deed.de",
           "geaendert": "nein", "geprueft": "2026-11-15", "alt": "Testbild"}
CSP = "default-src 'self'; script-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'"
SEITE = ('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">'
         '<meta http-equiv="Content-Security-Policy" content="' + CSP + '">'
         '<meta name="referrer" content="no-referrer"><title>Test</title>'
         '<meta name="robots" content="noindex, nofollow"></head><body><h1>Test</h1>{}</body></html>')


def lauf(tmp, bilder=None, datei=False, seite=None, roh=None, extra=None):
    """Setzt den Testzustand in der Kopie und gibt (Exit-Code, Ausgabe) von check.py zurück."""
    img = os.path.join(tmp, "img")
    shutil.rmtree(img, ignore_errors=True)
    if datei:
        os.makedirs(img)
        with open(os.path.join(img, "test.webp"), "wb") as f:
            f.write(WEBP)
    with open(os.path.join(tmp, "data", "bilder.json"), "w", encoding="utf-8") as f:
        json.dump({"bilder": bilder or []}, f)
    t = os.path.join(tmp, "zz-test.html")
    if seite or roh:
        with open(t, "w", encoding="utf-8") as f:
            f.write(roh or SEITE.format(seite))
    elif os.path.exists(t):
        os.remove(t)
    for pfad, inhalt in (extra or {}).items():  # weitere Dateien, nach dem Lauf wieder entfernt
        os.makedirs(os.path.dirname(os.path.join(tmp, pfad)), exist_ok=True)
        with open(os.path.join(tmp, pfad), "w", encoding="utf-8") as f:
            f.write(inhalt)
    r = subprocess.run([sys.executable, os.path.join(tmp, "tools", "check.py")],
                       capture_output=True, text=True, encoding="utf-8",
                       env=dict(os.environ, PYTHONIOENCODING="utf-8"))  # Windows-Konsole sonst cp1252
    for pfad in extra or {}:
        os.remove(os.path.join(tmp, pfad))
    return r.returncode, r.stdout


FAELLE = [
    # (Name, erwarteter Exit-Code, Textschnipsel in der Ausgabe, Zustand)
    ("ohne Bilder", 0, "0 Fehler", {}),
    ("Datei ohne Eintrag", 1, "img/test.webp: Bilddatei ohne vollständigen Eintrag", {"datei": True}),
    ("Eintrag ohne Autor", 1, "Pflichtfeld fehlt: autor", {"datei": True, "bilder": [dict(EINTRAG, autor="")]}),
    ("Eintrag ohne Datei", 1, "Datei existiert nicht", {"bilder": [EINTRAG]}),
    ("<img> ohne Eintrag", 1, 'zz-test.html: <img src="img/test.webp"> ohne vollständigen Eintrag',
     {"datei": True, "seite": '<img src="img/test.webp" alt="x">'}),
    ("<img> ohne Alt-Text", 1, "ohne Alt-Text",
     {"datei": True, "bilder": [EINTRAG], "seite": '<img src="img/test.webp">'}),
    ("externes Bild", 1, "externes Bild",
     {"bilder": [], "seite": '<img src="https://upload.wikimedia.org/x.jpg" alt="x">'}),
    ("Icon fehlt im Sprite", 1, "Icon „gibt-es-nicht“ fehlt",
     {"seite": '<svg class="icon" aria-hidden="true"><use href="assets/icons.svg#gibt-es-nicht"/></svg>'}),
    ("Deko-SVG ohne aria-hidden", 1, "<svg> ohne aria-hidden",
     {"seite": '<svg class="icon"><use href="assets/icons.svg#house"/></svg>'}),
    ("Karte ohne Icon", 1, "Karte ohne Icon", {"seite": '<article class="card"><h3>Test</h3></article>'}),
    ("Kennzahl ohne Stand", 1, "Kennzahl ohne Quelle/Stand",
     {"seite": '<li class="stat"><span class="stat-wert">1</span> Quelle: X</li>'}),
    # Sicherheit (alle HTML/CSS im Repo, auch Unterordner)
    ("Inline-Skript", 1, "<script> gefunden", {"seite": "<script>alert(1)</script>"}),
    ("Event-Handler", 1, "Inline-Event-Handler", {"seite": '<p onclick="x()">Text</p>'}),
    ("javascript:-Link", 1, "javascript:-Link", {"seite": '<a href="javascript:void(0)">x</a>'}),
    ("Formular", 1, "<form> nicht erlaubt", {"seite": '<form action="mailto:x"></form>'}),
    ("Fremdabruf im Mockup-Ordner", 1, "docs/mockups/zz.html: Fremdabruf",
     {"extra": {"docs/mockups/zz.html": '<link rel="stylesheet" href="https://fonts.example/x.css">'}}),
    ("CSS-Import extern", 1, "externer Abruf in CSS", {"extra": {"css/zz.css": "@import url(https://x.example/a.css);"}}),
    ("target=_blank ohne noopener", 1, "ohne rel=noopener", {"seite": '<a href="index.html" target="_blank">x</a>'}),
    # Struktur der Hauptseiten
    ("CSP fehlt", 1, "Content-Security-Policy fehlt",
     {"roh": '<!DOCTYPE html><html lang="de"><head><title>T</title><meta name="robots" content="noindex"></head><body><h1>T</h1></body></html>'}),
    ("Überschriften-Sprung", 1, "Überschriften-Sprung h1 → h3", {"seite": "<h3>Karte</h3>"}),
    ("zweite h1", 1, "2× <h1>", {"seite": "<h1>Noch eine</h1>"}),
    ("Sprungmarke ohne Ziel", 1, "Sprungmarke #fehlt ohne Ziel", {"seite": '<a href="#fehlt">x</a>'}),
    ("doppelte id", 1, "doppelte id", {"seite": '<p id="a">1</p><p id="a">2</p>'}),
    ("vollständig", 0, "0 Fehler",
     {"datei": True, "bilder": [EINTRAG], "seite": '<img src="img/test.webp" alt="Testbild">'}),
]

tmp = tempfile.mkdtemp(prefix="nordstern-test-")
try:
    shutil.copytree(ROOT, tmp, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".git"))
    falsch = 0
    for name, code, schnipsel, zustand in FAELLE:
        rc, out = lauf(tmp, **zustand)
        ok = rc == code and schnipsel in out
        falsch += not ok
        print(("OK    " if ok else "FALSCH"), name)
        if not ok:
            print(f"       erwartet Exit {code} + „{schnipsel}“, bekam Exit {rc}:\n{out}")
finally:
    shutil.rmtree(tmp, ignore_errors=True)
print(f"{len(FAELLE)} Testfälle · {falsch} falsch")
sys.exit(1 if falsch else 0)
