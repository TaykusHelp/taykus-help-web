#!/usr/bin/env python3
"""Genera el Centro de ayuda Taykus (web estática) a partir del contenido de GitBook.

Uso:
    python build.py --content ../taykus-help-center --out dist

El contenido llega al repositorio taykus-help-center mediante Git Sync de GitBook.
Este script lo lee tal cual (no lo modifica) y produce una web en la carpeta --out.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml
from markdown_it import MarkdownIt

import templates as T

ROOT = Path(__file__).resolve().parent

# Espacios de GitBook cuyo identificador aparece en enlaces del tipo app.gitbook.com/s/<id>/
KNOWN_SPACE_IDS = {
    "V0h7jTfpeuZY1RmPEtNK": "configuracion",
    "hSQoRJmdDmzxYVh7vpFW": "calendario",
    "7f6wmhmmi292HcDQR5ok": "academia",
    "QFNRYl4MHLCMNIVqCXJJ": "ventas",
    "4z8F8SJQ4eSsPYRArwWe": "marketing",
}

WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)


# ---------------------------------------------------------------------------
# Utilidades de texto
# ---------------------------------------------------------------------------

EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿️‍⬀-⯿⌀-⏿]+"
)


def clean_title(t: str) -> str:
    t = EMOJI_RE.sub("", t or "")
    t = re.sub(r"\*\*|__", "", t)
    return re.sub(r"\s+", " ", t).strip()


def slugify(text: str) -> str:
    t = unicodedata.normalize("NFD", text.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "seccion"


def strip_tags(s: str) -> str:
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def split_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        m = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n?", text)
        if m:
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError:
                fm = {}
            return (fm if isinstance(fm, dict) else {}), text[m.end():]
    return {}, text


def youtube_id(url: str) -> tuple[str | None, bool]:
    u = urlparse(url)
    host = (u.netloc or "").lower()
    short = "/shorts/" in u.path
    if "youtu.be" in host:
        return u.path.strip("/").split("/")[0] or None, short
    if "youtube" in host:
        m = re.search(r"(?:[?&]v=)([\w-]{6,})", url)
        if m:
            return m.group(1), short
        m = re.search(r"/(?:shorts|embed|live)/([\w-]{6,})", u.path)
        if m:
            return m.group(1), short
    return None, False


# ---------------------------------------------------------------------------
# Modelo de páginas
# ---------------------------------------------------------------------------


class Page:
    def __init__(self, module: "Module", src: Path, rel: str, title: str, parent: "Page | None"):
        self.module = module
        self.src = src
        self.rel = rel  # ruta dentro del espacio, p. ej. calendario/reservas/x.md
        self.summary_title = title
        self.parent = parent
        self.children: list[Page] = []
        self.url = module.page_url(rel)
        self.title = clean_title(title)
        self.description = ""
        self.html = ""
        self.text = ""
        self.toc: list[tuple[int, str, str]] = []
        self.videos: list[tuple[str, bool]] = []
        self.has_body = False
        self.minutes = 1

    @property
    def is_readme(self) -> bool:
        return self.src.name.lower() == "readme.md"

    @property
    def kind(self) -> str:
        if self.parent is None:
            return "module"
        if self.children and not self.has_body:
            return "section"
        return "article"

    def ancestors(self) -> list["Page"]:
        out, p = [], self.parent
        while p is not None:
            out.append(p)
            p = p.parent
        return list(reversed(out))

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


class Module:
    def __init__(self, slug: str, title: str, directory: Path, meta: dict):
        self.slug = slug
        self.dir = directory
        self.title = clean_title(meta.get("title") or title)
        self.description = meta.get("description", "")
        self.icon = meta.get("icon", "gear")
        self.root: Page | None = None

    def page_url(self, rel: str) -> str:
        parts = rel[:-3].split("/") if rel.endswith(".md") else rel.strip("/").split("/")
        if parts and parts[-1].lower() == "readme":
            parts = parts[:-1]
        if len(parts) > 0 and parts[0] == self.slug:
            parts = parts[1:]
        path = "/".join(p for p in parts if p)
        return f"/{self.slug}/{path}/" if path else f"/{self.slug}/"

    def pages(self):
        return list(self.root.walk()) if self.root else []

    def articles(self):
        return [p for p in self.pages() if p.kind == "article"]


SUMMARY_RE = re.compile(r"^(\s*)[*-]\s+\[(.*)\]\((.*)\)\s*$")


def parse_summary(module: Module) -> None:
    summary = module.dir / "SUMMARY.md"
    if not summary.exists():
        warn(f"{module.slug}: falta SUMMARY.md")
        return
    stack: list[tuple[int, Page]] = []
    for line in summary.read_text(encoding="utf-8").splitlines():
        m = SUMMARY_RE.match(line)
        if not m:
            continue
        indent = len(m.group(1).replace("\t", "  "))
        title, rel = m.group(2), unquote(m.group(3)).strip()
        if re.match(r"^https?://", rel):  # acceso directo a otro módulo dentro del índice
            continue
        src = module.dir / rel
        if not src.exists():
            warn(f"{module.slug}: el índice apunta a un archivo que no existe: {rel}")
            continue
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack else None
        page = Page(module, src, rel, title, parent)
        if parent is None:
            if module.root is None:
                module.root = page
            else:  # varios elementos de primer nivel: cuelgan de la raíz
                page.parent = module.root
                module.root.children.append(page)
        else:
            parent.children.append(page)
        stack.append((indent, page))


# ---------------------------------------------------------------------------
# Conversión de contenido
# ---------------------------------------------------------------------------

ICON_NAMES = {
    "pen": "pen", "pencil": "pen", "pen-to-square": "pen", "plus": "plus", "plus-large": "plus",
    "floppy-disk": "save", "gear": "gear", "user": "user", "truck": "truck", "trophy": "medal",
    "mobile": "phone", "memo": "invoice", "megaphone": "megaphone", "medal": "medal",
    "flag-pennant": "flag", "file-invoice": "invoice", "envelope": "mail", "dollar-sign": "euro",
    "credit-card": "card", "clock-three": "clock", "chart-simple": "chart", "cart-shopping": "cart",
    "briefcase": "box", "bolt": "bolt", "ban": "ban", "trash": "trash", "eye": "eye",
}

EMOJI_ICONS = {
    "heavy_plus_sign": "plus", "plus": "plus", "gear": "gear", "scissors": "scissors",
    "floppy_disk": "save", "arrow_down": "arrowdown", "pencil": "pen", "pencil2": "pen",
    "wastebasket": "trash", "eye": "eye", "no_entry_sign": "ban", "zap": "bolt",
}

MARK_COLORS = {
    "$danger": "danger", "red": "danger", "$warning": "warning", "orange": "warning",
    "yellow": "yellow", "blue": "info", "$info": "info", "$primary": "info", "$tint": "info",
    "$success": "success", "green": "success",
}


class Site:
    def __init__(self, content: Path, out: Path, base: str, site_url: str, config: dict):
        self.content = content
        self.out = out
        self.base = base.rstrip("/")
        self.site_url = site_url.rstrip("/")
        self.config = config
        self.modules: list[Module] = []
        self.by_src: dict[Path, Page] = {}
        self.assets: dict[Path, str] = {}
        self.asset_names: set[str] = set()
        md = MarkdownIt("commonmark", {"html": True, "typographer": False})
        md.enable(["table", "strikethrough"])
        self.md = md

    # -- carga ---------------------------------------------------------------
    def load(self) -> None:
        cfg = yaml.safe_load((self.content / "gitbook-docs.yaml").read_text(encoding="utf-8"))
        meta = self.config.get("modules", {})

        def walk(nodes):
            for n in nodes:
                if n.get("type") == "space":
                    d = (n.get("content") or {}).get("directory")
                    slug = n.get("path")
                    if d and slug and slug != "home":
                        directory = (self.content / d).resolve()
                        if directory.exists():
                            self.modules.append(Module(slug, n.get("title", slug), directory, meta.get(slug, {})))
                walk(n.get("children", []))

        walk(cfg["site"]["structure"])
        for m in self.modules:
            parse_summary(m)
            for p in m.pages():
                self.by_src[p.src.resolve()] = p

    def url(self, path: str) -> str:
        return self.base + path

    # -- resolución de enlaces ------------------------------------------------
    def find_by_rel(self, module_slug: str | None, rel: str) -> Page | None:
        rel = rel.strip("/")
        rel = re.sub(r"\.md$", "", rel)
        rel = re.sub(r"(^|/)README$", "", rel, flags=re.I)
        mods = [m for m in self.modules if module_slug is None or m.slug == module_slug]
        for m in mods:
            for p in m.pages():
                key = re.sub(r"\.md$", "", p.rel)
                key = re.sub(r"(^|/)README$", "", key, flags=re.I).strip("/")
                if key == rel or (rel and key.endswith("/" + rel)):
                    return p
        # Último recurso: mismo nombre de archivo en todo el centro de ayuda
        last = rel.split("/")[-1] if rel else ""
        if last:
            cands = [p for m in self.modules for p in m.pages()
                     if re.sub(r"\.md$", "", p.src.name) == last or (p.is_readme and p.src.parent.name == last)]
            if len(cands) == 1:
                return cands[0]
        return None

    def resolve_href(self, href: str, page: Page) -> tuple[str, bool]:
        """Devuelve (href nuevo, es_externo)."""
        raw = html.unescape(href).strip()
        if not raw or raw.startswith(("#", "mailto:", "tel:", "/")):
            return href, False
        u = urlparse(raw)
        if u.scheme in ("http", "https"):
            host = u.netloc.lower()
            if host == "app.gitbook.com":
                m = re.match(r"^(?:/o/[^/]+)?/s/([^/]+)/?(.*)$", u.path)
                if m:
                    space_id, rest = m.group(1), m.group(2)
                    frag = f"#{u.fragment}" if u.fragment else ""
                    target = self.find_by_rel(None, rest) if rest else None
                    if target:
                        return self.url(target.url) + frag, False
                    mod = KNOWN_SPACE_IDS.get(space_id)
                    if mod and not rest:
                        return self.url(f"/{mod}/"), False
                    warn(f"{page.rel}: enlace de GitBook sin destino claro: {raw}")
                    return self.url("/"), False
            if host.endswith("gitbook.io") and "/~gitbook/image" not in u.path:
                path = re.sub(r"^/taykushelpcenter/?", "", u.path).strip("/")
                path = re.sub(r"^home/", "", path)
                parts = path.split("/", 1)
                target = None
                if len(parts) == 2:
                    target = self.find_by_rel(parts[0], parts[1]) or self.find_by_rel(None, parts[1])
                if target:
                    return self.url(target.url), False
                if not path:
                    return self.url("/"), False
                warn(f"{page.rel}: enlace antiguo de GitBook sin destino: {raw}")
            return raw, True
        if u.scheme:
            return raw, True
        # Ruta relativa
        path_part = unquote(u.path)
        frag = f"#{u.fragment}" if u.fragment else ""
        target_path = (page.src.parent / path_part).resolve()
        if target_path.is_dir():
            target_path = target_path / "README.md"
        p = self.by_src.get(target_path)
        if p is None and target_path.suffix == "" and target_path.with_suffix(".md").exists():
            p = self.by_src.get(target_path.with_suffix(".md"))
        if p is not None:
            return self.url(p.url) + frag, False
        if target_path.suffix.lower() == ".md":
            alt = self.find_by_rel(page.module.slug, os.path.relpath(target_path, page.module.dir))
            if alt:
                return self.url(alt.url) + frag, False
            warn(f"{page.rel}: enlace a un artículo que no está en el índice: {path_part}")
            return self.url(f"/{page.module.slug}/"), False
        if target_path.exists() and target_path.is_file():
            return self.asset_url(target_path, page.module.slug), False
        warn(f"{page.rel}: no se encuentra el archivo: {path_part}")
        return raw, False

    def asset_url(self, path: Path, module_slug: str) -> str:
        path = path.resolve()
        if path in self.assets:
            return self.assets[path]
        stem = slugify(path.stem)[:80]
        ext = path.suffix.lower()
        name = f"{module_slug}/{stem}{ext}"
        i = 2
        while name in self.asset_names:
            name = f"{module_slug}/{stem}-{i}{ext}"
            i += 1
        self.asset_names.add(name)
        dest = self.out / "media" / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        url = self.url(f"/media/{name}")
        self.assets[path] = url
        return url

    # -- bloques de GitBook ---------------------------------------------------
    def convert_blocks(self, md: str, page: Page) -> str:
        out: list[str] = []
        lines = md.split("\n")
        i = 0
        while i < len(lines):
            line = lines[i]
            m = re.fullmatch(r"\s*\{%\s*([\w-]+)(.*?)%\}\s*", line)
            if not m:
                out.append(self.convert_inline(line))
                i += 1
                continue
            tag, args = m.group(1), m.group(2)
            attrs = dict(re.findall(r'(\w+)="([^"]*)"', args))

            def block(h: str) -> None:
                out.extend(["", h, ""])

            if tag == "stepper":
                block('<div class="tk-steps">')
            elif tag == "step":
                block('<div class="tk-step">')
            elif tag == "tabs":
                block('<div class="tk-tabs">')
            elif tag == "tab":
                block(f'<div class="tk-tab" data-title="{html.escape(attrs.get("title", ""))}">')
            elif tag == "columns":
                block('<div class="tk-cols">')
            elif tag == "column":
                block('<div class="tk-col">')
            elif tag == "hint":
                style = re.sub(r"[^a-z]", "", attrs.get("style", "info"))
                block(f'<div class="tk-hint tk-hint-{style}">')
            elif tag in ("endstepper", "endstep", "endtabs", "endtab", "endcolumns", "endcolumn", "endhint"):
                block("</div>")
            elif tag == "embed":
                block(self.embed_html(attrs.get("url", ""), page))
            elif tag == "file":
                src = attrs.get("src", "")
                target = (page.src.parent / unquote(src)).resolve()
                name = target.name
                if target.exists():
                    href = self.asset_url(target, page.module.slug)
                else:
                    warn(f"{page.rel}: falta el archivo adjunto {src}")
                    href = "#"
                block(T.file_card(href, name))
            elif tag == "content-ref":
                j = i + 1
                text = ""
                while j < len(lines) and not re.fullmatch(r"\s*\{%\s*endcontent-ref\s*%\}\s*", lines[j]):
                    mm = re.search(r"\[(.*?)\]\((.*?)\)", lines[j])
                    if mm:
                        text = mm.group(1)
                    j += 1
                href, ext = self.resolve_href(attrs.get("url", ""), page)
                title = text
                target = self.page_for_url(href)
                if target:
                    title = target.title
                title = clean_title(re.sub(r"\.md$", "", title).replace("-", " ") if title.endswith(".md") else title)
                block(T.ref_card(href, title, target.module.title if target else ""))
                i = j + 1
                continue
            else:
                warn(f"{page.rel}: bloque de GitBook no reconocido: {tag}")
            i += 1
        return "\n".join(out)

    def page_for_url(self, href: str) -> Page | None:
        path = href[len(self.base):] if self.base and href.startswith(self.base) else href
        path = path.split("#")[0]
        for m in self.modules:
            for p in m.pages():
                if p.url == path:
                    return p
        return None

    def embed_html(self, url: str, page: Page) -> str:
        vid, short = youtube_id(url)
        if vid:
            page.videos.append((vid, short))
            return T.video(vid, short)
        if url:
            return T.ref_card(url, url, "Enlace externo", external=True)
        return ""

    def convert_inline(self, line: str) -> str:
        def icon(m):
            name = ICON_NAMES.get(m.group(1), "")
            return T.inline_icon(name) if name else ""

        line = re.sub(r'<i class="fa-([\w-]+)"[^>]*>(?::[\w-]+:)?</i>', icon, line)

        # Emojis escritos como :nombre: en GitBook (p. ej. :heavy_plus_sign:)
        def shortcode(m):
            name = m.group(2).replace("\\", "")
            ico = EMOJI_ICONS.get(name)
            return m.group(1) + T.inline_icon(ico) if ico else m.group(0)

        line = re.sub(r'(^|[^\w/:"\']):([a-z][a-z0-9_\\+-]*):', shortcode, line)

        def mark(m):
            style = m.group(1)
            cm = re.search(r"(background-color|color)\s*:\s*([^;\"]+)", style)
            kind = "yellow"
            if cm:
                kind = MARK_COLORS.get(cm.group(2).strip(), "yellow")
                if cm.group(1) == "color":
                    return f'<mark class="tk-mark-text tk-mark-{kind}">'
            return f'<mark class="tk-mark tk-mark-{kind}">'

        line = re.sub(r'<mark style="([^"]*)">', mark, line)
        return line

    # -- render de una página -------------------------------------------------
    def render_page(self, page: Page) -> None:
        raw = page.src.read_text(encoding="utf-8")
        fm, body = split_frontmatter(raw)
        desc = str(fm.get("description") or "").strip()
        if desc and not re.match(r"^gu[ií]as? del m[oó]dulo", desc, re.I) and "developer platform" not in desc:
            page.description = desc
        m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
        if m and not body[: m.start()].strip():
            h1 = clean_title(m.group(1))
            if h1 and h1.lower() != "page":
                page.title = h1
            body = body[m.end():]
        if page.title.lower() == "page":
            page.title = page.module.title
        if page.parent is None:  # la portada de cada módulo la generamos nosotros
            page.has_body = False
            return
        body = body.strip("\n")
        # Una página que solo enlaza a otras (índices con pestañas de enlaces) cuenta como sección
        bare = re.sub(r"\{%\s*content-ref[\s\S]*?\{%\s*endcontent-ref\s*%\}", "", body)
        bare = re.sub(r"\{%[^%]*%\}", "", bare)
        bare = re.sub(r"^\s*#{1,6}\s.*$", "", bare, flags=re.M)
        page.has_body = bool(strip_tags(bare).strip()) or "{% embed" in body or "<img" in bare or "![" in bare
        if not page.has_body:
            return
        md = self.convert_blocks(body, page)
        out = self.md.render(md)
        out = self.post_html(out, page)
        page.html = out
        page.text = strip_tags(re.sub(r'<a class="tk-ref"[\s\S]*?</a>', " ", out))
        words = len(page.text.split())
        page.minutes = max(1, math.ceil(words / 180))

    def post_html(self, out: str, page: Page) -> str:
        def attr(m):
            name, val = m.group(1), m.group(2)
            new, external = self.resolve_href(val, page)
            extra = ' target="_blank" rel="noopener"' if external and name == "href" else ""
            return f'{name}="{html.escape(new, quote=True)}"{extra}'

        out = re.sub(r'\b(src|href)="([^"]*)"', attr, out)
        out = out.replace("<figcaption></figcaption>", "")
        out = re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy"', out)
        # Imágenes marcadas en GitBook como "tamaño de línea" (iconos dentro del texto)
        out = re.sub(r'<img([^>]*?)\sdata-size="line"([^>]*)>', r'<img class="tk-img-inline"\1\2>', out)
        out = re.sub(r"<table", '<div class="tk-table"><table', out)
        out = out.replace("</table>", "</table></div>")
        # GitBook: <a class="button primary" data-icon="..."> -> botón Taykus
        out = re.sub(r'<a ([^>]*?)class="button[^"]*"', r'<a \1class="tk-btn"', out)
        out = re.sub(r'\sdata-icon="[^"]*"', "", out)
        # Anclas e índice del artículo
        used: set[str] = set()
        toc: list[tuple[int, str, str]] = []

        def head(m):
            lvl, attrs_, inner = m.group(1), m.group(2), m.group(3)
            text = strip_tags(inner)
            if not text:
                return m.group(0)
            idm = re.search(r'id="([^"]+)"', attrs_)
            hid = idm.group(1) if idm else slugify(text)[:60]
            base, k = hid, 2
            while hid in used:
                hid, k = f"{base}-{k}", k + 1
            used.add(hid)
            if lvl in ("2", "3"):
                toc.append((int(lvl), hid, text))
            if not idm:
                attrs_ = f'{attrs_} id="{hid}"'
            return f"<h{lvl}{attrs_}>{inner}</h{lvl}>"

        out = re.sub(r"<h([2-4])([^>]*)>([\s\S]*?)</h\1>", head, out)
        page.toc = toc

        # Enlaces "mention" de GitBook: el texto es el nombre del archivo; se cambia por el título del artículo
        def mention(m):
            target = self.page_for_url(html.unescape(m.group(2)))
            return f'{m.group(1)}{html.escape(target.title) if target else m.group(3)}</a>'

        out = re.sub(r'(<a href="([^"]+)"[^>]*>)([^<]*?\.md)</a>', mention, out)
        return out

    # -- salida ---------------------------------------------------------------
    def build(self) -> None:
        if self.out.exists():
            shutil.rmtree(self.out)
        (self.out / "media").mkdir(parents=True)
        self.load()
        for m in self.modules:
            for p in m.pages():
                self.render_page(p)

        static_src = ROOT / "static"
        shutil.copytree(static_src, self.out / "static")
        version = hashlib.sha1(
            b"".join((static_src / f).read_bytes() for f in sorted(os.listdir(static_src)) if (static_src / f).is_file())
        ).hexdigest()[:8]
        ctx = T.Context(self, version)

        def write(path: str, content: str) -> None:
            dest = self.out / path.strip("/") / "index.html" if not path.endswith(".html") else self.out / path.strip("/")
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")

        write("/", T.home(ctx))
        write("/buscar/", T.search_page(ctx))
        write("/videos/", T.videos_page(ctx))
        write("/404.html", T.not_found(ctx))
        for m in self.modules:
            if not m.root:
                continue
            write(m.root.url, T.module_page(ctx, m))
            for p in m.pages()[1:]:
                write(p.url, T.section_page(ctx, p) if p.kind == "section" else T.article_page(ctx, p))

        # Índice de búsqueda
        index = []
        for m in self.modules:
            for p in m.pages():
                if p.kind != "article":
                    continue
                crumbs = " › ".join([m.title] + [a.title for a in p.ancestors()[1:]])
                index.append({
                    "t": p.title, "u": self.url(p.url), "m": m.title, "s": m.slug, "b": crumbs,
                    "h": " · ".join(t for _, _, t in p.toc), "x": p.text[:8000], "v": 1 if p.videos else 0,
                })
        (self.out / "search-index.json").write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

        # Sitemap y robots
        if self.site_url:
            urls = ["/", "/videos/"] + [p.url for m in self.modules for p in m.pages()]
            sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
            sm += [f"<url><loc>{html.escape(self.site_url + self.base + u)}</loc></url>" for u in urls]
            sm.append("</urlset>")
            (self.out / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
            (self.out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {self.site_url}{self.base}/sitemap.xml\n", encoding="utf-8")
        else:
            (self.out / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
        (self.out / ".nojekyll").write_text("", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", default=os.environ.get("CONTENT_DIR", str(ROOT.parent / "taykus-help-center")))
    ap.add_argument("--out", default=str(ROOT / "dist"))
    ap.add_argument("--base", default=os.environ.get("BASE_PATH", ""), help="Subcarpeta si la web no va en la raíz del dominio, p. ej. /ayuda")
    ap.add_argument("--site-url", default=os.environ.get("SITE_URL", ""), help="Dirección pública, p. ej. https://ayuda.taykus.com")
    args = ap.parse_args()

    config = yaml.safe_load((ROOT / "config" / "site.yaml").read_text(encoding="utf-8"))
    site = Site(Path(args.content).resolve(), Path(args.out).resolve(), args.base, args.site_url, config)
    site.build()
    n_art = sum(len(m.articles()) for m in site.modules)
    n_vid = sum(1 for m in site.modules for p in m.pages() if p.videos)
    print(f"Web generada en {args.out}: {len(site.modules)} módulos, {n_art} artículos, {n_vid} con vídeo, {len(site.assets)} archivos.")
    if WARNINGS:
        print(f"\n{len(WARNINGS)} avisos:")
        for w in WARNINGS:
            print("  -", w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
