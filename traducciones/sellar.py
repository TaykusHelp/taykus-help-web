#!/usr/bin/env python3
"""Marca traducciones como "al día" con la huella del artículo en español del que salen.

Uso:
    python traducciones/sellar.py --content ../taykus-help-center traducciones/en/home/marketing/marketing/x.md [...]
    python traducciones/sellar.py --content ../taykus-help-center --pendientes en

Sin archivos y con --pendientes, lista los artículos sin traducción o cuya traducción
es de una versión anterior del original.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def source_hash(path: Path) -> str:
    return hashlib.sha1(path.read_bytes()).hexdigest()[:12]


def stamp(tr_file: Path, content: Path) -> None:
    lang = tr_file.resolve().relative_to(ROOT).parts[0]
    rel = tr_file.resolve().relative_to(ROOT / lang)
    src = content / rel
    if not src.exists():
        sys.exit(f"No existe el original: {src}")
    text = tr_file.read_text(encoding="utf-8")
    h = source_hash(src)
    m = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n?", text)
    if m:
        fm = re.sub(r"^origen:.*\n?", "", m.group(1) + "\n", flags=re.M).rstrip("\n")
        fm = (fm + "\n" if fm.strip() else "") + f"origen: {h}"
        text = f"---\n{fm}\n---\n" + text[m.end():]
    else:
        text = f"---\norigen: {h}\n---\n\n" + text
    tr_file.write_text(text, encoding="utf-8")


def pending(content: Path, lang: str) -> list[tuple[str, str]]:
    out = []
    for src in sorted((content / "home").rglob("*.md")):
        if src.name == "SUMMARY.md" or src.parent == content / "home" or "/.gitbook/" in src.as_posix():
            continue
        rel = src.relative_to(content)
        if src.name == "README.md" and src.parent.parent == content / "home":
            continue  # portada del módulo: usa config/site.yaml
        tr = ROOT / lang / rel
        if not tr.exists():
            out.append((rel.as_posix(), "falta"))
            continue
        m = re.search(r"^origen:\s*(\S+)", tr.read_text(encoding="utf-8"), re.M)
        if not m or m.group(1) != source_hash(src):
            out.append((rel.as_posix(), "desactualizada"))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--content", default=str(ROOT.parent.parent / "taykus-help-center"))
    ap.add_argument("--pendientes", metavar="IDIOMA")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    content = Path(a.content).resolve()
    for f in a.files:
        stamp(Path(f), content)
    if a.pendientes:
        for rel, why in pending(content, a.pendientes):
            print(f"{why}\t{rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
