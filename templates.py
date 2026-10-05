"""Plantillas HTML del Centro de ayuda Taykus."""
from __future__ import annotations

import html
import re
from pathlib import Path

E = lambda s: html.escape(str(s or ""), quote=True)  # noqa: E731

# Iconos de trazo (24x24) usados en módulos y artículos.
ICONS = {
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "medal": '<circle cx="12" cy="15" r="6"/><path d="M8 3l4 6 4-6"/>',
    "team": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c1-3.5 3.5-5.5 6.5-5.5s5.5 2 6.5 5.5M16 4.5a3.5 3.5 0 0 1 0 7M18 14.8c1.8.8 3 2.6 3.5 5.2"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    "flag": '<path d="M5 21V4h12l-2 4 2 4H5"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/>',
    "euro": '<path d="M17 6.5A7 7 0 1 0 17 17.5M4 10h9M4 14h9"/>',
    "megaphone": '<path d="M3 10v4h4l9 5V5L7 10H3zM19 9a3 3 0 0 1 0 6"/>',
    "truck": '<path d="M2 6h12v10H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4zM3 7l9 4 9-4M12 11v10"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "invoice": '<path d="M6 2h9l4 4v16H6zM14 2v5h5M9 12h7M9 16h7"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "monitor": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "pen": '<path d="M4 20h4L19 9l-4-4L4 16v4zM13.5 6.5l4 4"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "save": '<path d="M4 4h13l3 3v13H4z"/><path d="M8 4v5h8V4M8 20v-6h8v6"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
    "ban": '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
    "trash": '<path d="M4 7h16M10 11v6M14 11v6M5 7l1 13h12l1-13M9 7V4h6v3"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.6 7.6L20 18M8.6 16.4L20 6"/>',
    "arrowdown": '<path d="M12 5v14M6 13l6 6 6-6"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    "play": '<path d="M7 4v16l13-8z" fill="currentColor" stroke="none"/>',
    "download": '<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.01"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "chevron": '<path d="M9 6l6 6-6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v6H4V6h6"/>',
}


def svg(name: str, size: int = 22, cls: str = "") -> str:
    body = ICONS.get(name, ICONS["info"])
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


LOGO = ('<svg class="tk-logo-mark" viewBox="0 0 96 136" aria-hidden="true"><defs><linearGradient id="tkg{n}" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0" stop-color="#18BBEA"/><stop offset="1" stop-color="#055AE2"/></linearGradient></defs>'
        '<path d="M42 4 L54 4 L82 40 L92 104 L48 130 L4 104 L14 40 Z M14 40 L48 124 L82 40" fill="none" stroke="url(#tkg{n})" '
        'stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/></svg>')


# ---------------------------------------------------------------------------
# Piezas que usa build.py dentro del contenido
# ---------------------------------------------------------------------------

def inline_icon(name: str) -> str:
    return f'<span class="tk-ico">{svg(name, 16)}</span>'


def video(vid: str, short: bool) -> str:
    cls = "tk-video tk-video-short" if short else "tk-video"
    return (f'<div class="{cls}"><a class="tk-video-btn" href="https://www.youtube.com/watch?v={E(vid)}" data-yt="{E(vid)}" '
            f'aria-label="Reproducir el vídeo tutorial"><img src="https://i.ytimg.com/vi/{E(vid)}/hqdefault.jpg" alt="" loading="lazy">'
            f'<span class="tk-play" aria-hidden="true">{svg("play", 26)}</span><span class="tk-video-label">Vídeo tutorial</span></a></div>')


def ref_card(href: str, title: str, meta: str, external: bool = False) -> str:
    tgt = ' target="_blank" rel="noopener"' if external else ""
    meta_html = f'<span class="tk-ref-meta">{E(meta)}</span>' if meta else ""
    return (f'<a class="tk-ref" href="{E(href)}"{tgt}><span class="tk-ref-body">{meta_html}<span class="tk-ref-title">{E(title)}</span></span>'
            f'{svg("external" if external else "arrow", 18)}</a>')


def file_card(href: str, name: str) -> str:
    return (f'<a class="tk-file" href="{E(href)}" download>{svg("download", 20)}<span><span class="tk-file-name">{E(name)}</span>'
            f'<span class="tk-file-meta">Descargar archivo</span></span></a>')


# ---------------------------------------------------------------------------
# Estructura común
# ---------------------------------------------------------------------------

class Context:
    def __init__(self, site, version: str):
        self.site = site
        self.version = version
        self.cfg = site.config.get("site", {})
        self.players = set(site.config.get("players", []))
        self._logo_n = 0

    def url(self, path: str) -> str:
        return self.site.url(path)

    def logo(self) -> str:
        self._logo_n += 1
        return LOGO.replace("{n}", str(self._logo_n))

    def static(self, name: str) -> str:
        return self.url(f"/static/{name}?v={self.version}")


def head(ctx: Context, title: str, description: str = "", path: str = "/") -> str:
    full = f"{title} · {ctx.cfg.get('title', 'Centro de ayuda Taykus')}" if title else ctx.cfg.get("title", "Centro de ayuda Taykus")
    desc = description or ctx.cfg.get("tagline", "")
    canonical = f'<link rel="canonical" href="{E(ctx.site.site_url + ctx.url(path))}">' if ctx.site.site_url else ""
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full)}</title>
<meta name="description" content="{E(desc[:300])}">
<meta name="tk-base" content="{E(ctx.site.base)}">
<meta property="og:title" content="{E(full)}">
<meta property="og:description" content="{E(desc[:300])}">
<meta name="theme-color" content="#011733">
{canonical}
<link rel="icon" href="{ctx.static('favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Poppins:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{ctx.static('styles.css')}">
<script defer src="{ctx.static('app.js')}"></script>
</head>"""


def brand(ctx: Context) -> str:
    return (f'<a class="tk-brand" href="{ctx.url("/")}" aria-label="Centro de ayuda Taykus, inicio">{ctx.logo()}'
            f'<span class="tk-wordmark">TAYKUS</span><span class="tk-brand-sep"></span><span class="tk-brand-sub">Centro de ayuda</span></a>')


def header_search(ctx: Context, value: str = "", big: bool = False, autofocus: bool = False) -> str:
    cls = "tk-search tk-search-big" if big else "tk-search"
    af = " autofocus" if autofocus else ""
    placeholder = "Ej.: cómo cerrar un día, cobrar una reserva…" if big else "Buscar en el centro de ayuda…"
    btn = '<button type="submit" class="tk-search-submit">Buscar</button>' if big else ""
    return (f'<form class="{cls}" action="{ctx.url("/buscar/")}" role="search" autocomplete="off">'
            f'<label class="tk-sr" for="q{"b" if big else "h"}">Busca tu pregunta</label>'
            f'{svg("search", 20, "tk-search-ico")}'
            f'<input id="q{"b" if big else "h"}" name="q" type="search" value="{E(value)}" placeholder="{E(placeholder)}"{af} '
            f'aria-autocomplete="list" aria-controls="pop{"b" if big else "h"}" aria-expanded="false">{btn}'
            f'<div class="tk-search-pop" id="pop{"b" if big else "h"}" role="listbox" hidden></div></form>')


def header(ctx: Context, variant: str = "dark", search: bool = True) -> str:
    app = ctx.cfg.get("app_url")
    app_btn = f'<a class="tk-btn tk-btn-sm" href="{E(app)}">Entrar en Taykus</a>' if app else ""
    nav = (f'<nav class="tk-topnav" aria-label="Principal"><a href="{ctx.url("/")}#modulos">Guías</a>'
           f'<a href="{ctx.url("/videos/")}">Vídeos</a><a href="#contacto">Contacto</a>{app_btn}</nav>')
    s = header_search(ctx) if search else ""
    return f'<header class="tk-header tk-header-{variant}"><div class="tk-wrap tk-header-in">{brand(ctx)}{s}{nav}</div></header>'


def contact(ctx: Context, compact: bool = False) -> str:
    email = ctx.cfg.get("support_email", "soporte@taykus.com")
    cls = "tk-contact tk-contact-compact" if compact else "tk-contact"
    return (f'<section class="{cls}" id="contacto"><div><h2>¿No encuentras lo que buscas?</h2>'
            f'<p>El equipo de soporte de Taykus te ayuda encantado.</p></div>'
            f'<a class="tk-btn tk-btn-light" href="mailto:{E(email)}">Escribir a soporte</a></section>')


def footer(ctx: Context) -> str:
    email = ctx.cfg.get("support_email", "soporte@taykus.com")
    return (f'<footer class="tk-footer"><div class="tk-wrap tk-footer-in"><span>© Taykus · Centro de ayuda</span>'
            f'<a href="mailto:{E(email)}">{E(email)}</a></div></footer>')


def page(ctx: Context, title: str, body: str, description: str = "", path: str = "/", variant: str = "dark", search: bool = True, cls: str = "") -> str:
    return (f'{head(ctx, title, description, path)}\n<body class="{cls}"><a class="tk-skip" href="#main">Saltar al contenido</a>'
            f'{header(ctx, variant, search)}{body}{footer(ctx)}<div class="tk-lightbox" hidden></div></body></html>')


# ---------------------------------------------------------------------------
# Ayudas
# ---------------------------------------------------------------------------

def short_label(title: str) -> str:
    t = re.sub(r"^[¿¡]\s*", "", title).rstrip("?").strip()
    t = re.sub(r"^c[oó]mo\s+", "", t, flags=re.I)
    return t[:1].upper() + t[1:]


def video_pages(ctx: Context):
    return [p for m in ctx.site.modules for p in m.pages() if p.videos and p.kind == "article"]


def popular_pages(ctx: Context):
    site = ctx.site
    readme = site.content / "home" / "README.md"
    out = []
    if readme.exists():
        for m in re.finditer(r"\{%\s*content-ref[^%]*%\}\s*\n\s*\[[^\]]*\]\(([^)]+)\)", readme.read_text(encoding="utf-8")):
            path = re.sub(r"^/?taykushelpcenter/", "", m.group(1)).strip("/")
            path = re.sub(r"^home/", "", path)
            parts = path.split("/", 1)
            if len(parts) == 2:
                p = site.find_by_rel(parts[0], parts[1])
                if p and p not in out:
                    out.append(p)
    return out


def crumbs(ctx: Context, p) -> str:
    items = [f'<a href="{ctx.url("/")}">Inicio</a>', f'<a href="{ctx.url(p.module.root.url)}">{E(p.module.title)}</a>']
    for a in p.ancestors()[1:]:
        items.append(f'<a href="{ctx.url(a.url)}">{E(a.title)}</a>')
    sep = '<span aria-hidden="true">›</span>'
    return f'<nav class="tk-crumbs" aria-label="Estás en">{sep.join(items)}</nav>'


def tree(ctx: Context, node, current) -> str:
    out = []
    for c in node.children:
        is_cur = c is current
        if c.children:
            opened = any(x is current for x in c.walk())
            inner = ""
            if c.kind == "article":
                cur = ' aria-current="page"' if is_cur else ""
                inner += f'<a href="{ctx.url(c.url)}"{cur}>{E(c.title)}</a>'
            inner += tree(ctx, c, current)
            link = f'<a class="tk-tree-sec" href="{ctx.url(c.url)}"{" aria-current=page" if is_cur and c.kind=="section" else ""}>{E(c.title)}</a>' if c.kind == "section" else f"<span>{E(c.title)}</span>"
            out.append(f'<details{" open" if opened else ""}><summary>{link}{svg("chevron", 16, "tk-chev")}</summary><div class="tk-tree-sub">{inner}</div></details>')
        else:
            cur = ' aria-current="page"' if is_cur else ""
            out.append(f'<a href="{ctx.url(c.url)}"{cur}>{E(c.title)}</a>')
    return "".join(out)


def sidebar(ctx: Context, p) -> str:
    m = p.module
    return (f'<aside class="tk-side"><button class="tk-side-toggle" type="button" aria-expanded="false">{svg("menu", 18)}'
            f'Índice de {E(m.title)}</button><nav class="tk-tree" aria-label="{E(m.title)}">'
            f'<a class="tk-tree-back" href="{ctx.url("/")}#modulos">← Todos los módulos</a>'
            f'<a class="tk-tree-mod" href="{ctx.url(m.root.url)}">{svg(m.icon, 18)}{E(m.title)}</a>'
            f'{tree(ctx, m.root, p)}</nav></aside>')


def related(ctx: Context, p) -> list:
    sibs = [s for s in (p.parent.children if p.parent else []) if s is not p and s.kind == "article"]
    if len(sibs) < 3 and p.parent and p.parent.parent:
        sibs += [s for s in p.parent.parent.children if s is not p and s is not p.parent and s.kind == "article" and s not in sibs]
    return sibs[:4]


def article_card(ctx: Context, p) -> str:
    vid = f'<span class="tk-tag">{svg("play", 12)}Vídeo</span>' if p.videos else ""
    return (f'<a class="tk-link-row" href="{ctx.url(p.url)}"><span>{E(p.title)}</span>'
            f'<span class="tk-link-meta">{vid}{svg("chevron", 18)}</span></a>')


# ---------------------------------------------------------------------------
# Páginas
# ---------------------------------------------------------------------------

def home(ctx: Context) -> str:
    site = ctx.site
    pop = popular_pages(ctx)
    featured = next((p for p in pop if "inicio r" in p.title.lower()), None)
    others = [p for p in pop if p is not featured]
    if not others:
        others = [a for m in site.modules for a in m.articles()][:5]
    chips = "".join(f'<a href="{ctx.url(p.url)}">{E(short_label(p.title))}</a>' for p in others[:4])

    feat_html = ""
    if featured:
        feat_html = (f'<a class="tk-feature" href="{ctx.url(featured.url)}"><span class="tk-eyebrow">Empieza aquí</span>'
                     f'<span class="tk-feature-title">{E(featured.title)}</span>'
                     f'<span class="tk-feature-text">Lo imprescindible para dejar tu club listo para empezar con Taykus.</span>'
                     f'<span class="tk-feature-cta">Ver la guía {svg("arrow", 18)}</span></a>')
    pop_rows = "".join(
        f'<a class="tk-link-row" href="{ctx.url(p.url)}"><span>{E(p.title)}</span><span class="tk-link-meta">{E(p.module.title)}</span></a>'
        for p in others[:6])

    club_mods = [m for m in site.modules if m.slug not in ctx.players and m.root]
    active = [m for m in club_mods if m.articles()]
    soon = [m for m in club_mods if not m.articles()]
    cards = "".join(
        f'<a class="tk-mod" href="{ctx.url(m.root.url)}"><span class="tk-mod-ico">{svg(m.icon)}</span><span class="tk-mod-body">'
        f'<span class="tk-mod-title">{E(m.title)}</span><span class="tk-mod-desc">{E(m.description)}</span>'
        f'<span class="tk-mod-count">{len(m.articles())} guías</span></span></a>' for m in active)
    soon_html = ""
    if soon:
        soon_html = '<div class="tk-soon"><span>Próximamente:</span>' + "".join(f'<span class="tk-pill">{E(m.title)}</span>' for m in soon) + "</div>"

    players = [m for m in site.modules if m.slug in ctx.players and m.root]
    player_cards = "".join(
        f'<a class="tk-player" href="{ctx.url(m.root.url)}"><span class="tk-player-ico">{svg(m.icon, 24)}</span><span>'
        f'<span class="tk-mod-title">{E(m.title)}</span><span class="tk-mod-desc">{E(m.description)}</span></span></a>' for m in players)

    vids = video_pages(ctx)
    vid_cards = "".join(video_card(ctx, p) for p in vids[:3])
    vid_section = ""
    if vids:
        vid_section = (f'<section class="tk-section" id="videos"><div class="tk-section-head"><div><h2>Vídeos tutoriales</h2>'
                       f'<p>Aprende viendo cómo se hace, en pocos minutos.</p></div><a class="tk-more" href="{ctx.url("/videos/")}">Ver los {len(vids)} vídeos {svg("arrow", 16)}</a></div>'
                       f'<div class="tk-vgrid">{vid_cards}</div></section>')

    body = f"""
<section class="tk-hero"><div class="tk-hero-in">
<h1>¿En qué podemos ayudarte?</h1>
<p>{E(ctx.cfg.get('tagline', ''))}</p>
{header_search(ctx, big=True)}
<div class="tk-chips"><span>Lo más buscado:</span>{chips}</div>
</div></section>
<main id="main" class="tk-wrap tk-home">
<section class="tk-start">{feat_html}<div class="tk-popular"><h2>Artículos más consultados</h2>{pop_rows}</div></section>
<section class="tk-section" id="modulos"><div class="tk-section-head"><div><h2>Guías para tu club</h2><p>Elige el módulo de Taykus sobre el que tienes la duda.</p></div></div>
<div class="tk-mods">{cards}</div>{soon_html}</section>
<section class="tk-section"><div class="tk-section-head"><div><h2>Para tus jugadores</h2><p>Guías que puedes enviar a tus clientes para que reserven solos.</p></div></div>
<div class="tk-players">{player_cards}</div></section>
{vid_section}
{contact(ctx)}
</main>"""
    return page(ctx, "", body, path="/", variant="light", search=False, cls="tk-page-home")


def video_card(ctx: Context, p) -> str:
    vid, short = p.videos[0]
    return (f'<a class="tk-vcard" href="{ctx.url(p.url)}"><span class="tk-vthumb"><img src="https://i.ytimg.com/vi/{E(vid)}/hqdefault.jpg" alt="" loading="lazy">'
            f'<span class="tk-play" aria-hidden="true">{svg("play", 20)}</span></span><span class="tk-vbody"><span class="tk-eyebrow-sm">{E(p.module.title)}</span>'
            f'<span class="tk-vtitle">{E(p.title)}</span></span></a>')


def module_page(ctx: Context, m) -> str:
    groups = []
    loose = []

    def flush():
        if loose:
            groups.append(("Guías", None, list(loose)))
            loose.clear()

    for c in m.root.children:
        if c.children:
            flush()
            items = [c] if c.kind == "article" else []
            items += [x for x in c.walk() if x is not c and x.kind == "article"]
            groups.append((c.title, c, items))
        elif c.kind == "article":
            loose.append(c)
    flush()
    if groups:
        blocks = "".join(
            f'<section class="tk-group"><h2>{E(t) if not g or g.kind != "section" else f"<a href={chr(34)}{ctx.url(g.url)}{chr(34)}>{E(t)}</a>"}</h2>'
            f'{"".join(article_card(ctx, p) for p in items)}</section>' for t, g, items in groups)
    else:
        blocks = ('<div class="tk-empty"><h2>Estamos preparando estas guías</h2><p>Mientras tanto, escríbenos y te ayudamos con lo que necesites.</p></div>')
    n = len(m.articles())
    body = f"""
<section class="tk-band"><div class="tk-wrap tk-band-in">
{crumbs_simple(ctx, m)}
<div class="tk-band-title"><span class="tk-band-ico">{svg(m.icon, 28)}</span><div><h1>{E(m.title)}</h1><p>{E(m.description)}{f' · {n} guías' if n else ''}</p></div></div>
</div></section>
<main id="main" class="tk-wrap tk-module"><div class="tk-groups">{blocks}</div>{contact(ctx, compact=True)}</main>"""
    return page(ctx, m.title, body, m.description, m.root.url)


def crumbs_simple(ctx: Context, m) -> str:
    return f'<nav class="tk-crumbs tk-crumbs-light" aria-label="Estás en"><a href="{ctx.url("/")}">Inicio</a><span aria-hidden="true">›</span><span>{E(m.title)}</span></nav>'


def doc_layout(ctx: Context, p, main_html: str, toc_html: str = "") -> str:
    return (f'<div class="tk-wrap tk-doc">{sidebar(ctx, p)}<main id="main" class="tk-main">{main_html}</main>'
            f'{toc_html}</div>')


def section_page(ctx: Context, p) -> str:
    items = "".join(article_card(ctx, c) if c.kind == "article" else
                    f'<a class="tk-link-row" href="{ctx.url(c.url)}"><span>{E(c.title)}</span><span class="tk-link-meta">{len([x for x in c.walk() if x.kind=="article"])} guías{svg("chevron", 18)}</span></a>'
                    for c in p.children)
    main = (f'{crumbs(ctx, p)}<h1 class="tk-title">{E(p.title)}</h1>'
            f'<p class="tk-lead">Guías de {E(p.title.lower())} en el módulo {E(p.module.title)}.</p><div class="tk-list">{items}</div>'
            f'{contact(ctx, compact=True)}')
    return page(ctx, p.title, doc_layout(ctx, p, main), path=p.url)


def article_page(ctx: Context, p) -> str:
    meta = [f"{p.minutes} min de lectura"]
    if p.videos:
        meta.append("Con vídeo")
    lead = f'<p class="tk-lead">{E(p.description)}</p>' if p.description else ""
    children = ""
    subs = [c for c in p.children]
    if subs:
        children = '<h2 class="tk-h-sub">En esta sección</h2><div class="tk-list">' + "".join(article_card(ctx, c) for c in subs) + "</div>"
    rel = related(ctx, p)
    rel_html = ""
    if rel:
        rel_html = '<h2 class="tk-h-sub">Artículos relacionados</h2><div class="tk-rel">' + "".join(
            f'<a href="{ctx.url(r.url)}">{E(r.title)}{svg("arrow", 16)}</a>' for r in rel) + "</div>"
    feedback = ('<section class="tk-feedback" aria-label="Valoración"><span class="tk-fb-q">¿Te ha sido útil este artículo?</span>'
                '<div class="tk-fb-btns"><button type="button" data-fb="si">Sí</button><button type="button" data-fb="no">No</button></div>'
                '<p class="tk-fb-thanks" hidden>¡Gracias por tu respuesta!</p></section>')
    main = (f'{crumbs(ctx, p)}<h1 class="tk-title">{E(p.title)}</h1><div class="tk-meta">{" · ".join(meta)}</div>{lead}'
            f'<article class="tk-content">{p.html}</article>{children}{feedback}{rel_html}{contact(ctx, compact=True)}')
    toc_html = ""
    if len(p.toc) >= 2:
        links = "".join(f'<a class="tk-toc-l{lvl}" href="#{E(hid)}">{E(text)}</a>' for lvl, hid, text in p.toc[:14])
        toc_html = f'<aside class="tk-toc" aria-label="En este artículo"><div class="tk-toc-title">En este artículo</div><nav>{links}</nav></aside>'
    return page(ctx, p.title, doc_layout(ctx, p, main, toc_html), p.description or f"{p.title} · {p.module.title}", p.url)


def search_page(ctx: Context) -> str:
    body = f"""
<section class="tk-band tk-band-search"><div class="tk-wrap-narrow">
<h1 class="tk-sr">Buscar en el centro de ayuda</h1>
{header_search(ctx, big=True, autofocus=True).replace('class="tk-search tk-search-big"', 'class="tk-search tk-search-big tk-search-page"')}
</div></section>
<main id="main" class="tk-wrap-narrow tk-results-page">
<p class="tk-results-info" aria-live="polite"></p>
<div class="tk-filters" role="group" aria-label="Filtrar resultados"></div>
<div class="tk-results"></div>
<noscript><p>Activa JavaScript para usar el buscador.</p></noscript>
{contact(ctx, compact=True)}
</main>"""
    return page(ctx, "Buscar", body, path="/buscar/", search=False, cls="tk-page-search")


def videos_page(ctx: Context) -> str:
    vids = video_pages(ctx)
    cards = "".join(video_card(ctx, p) for p in vids)
    body = f"""
<section class="tk-band"><div class="tk-wrap tk-band-in">
<nav class="tk-crumbs tk-crumbs-light" aria-label="Estás en"><a href="{ctx.url('/')}">Inicio</a><span aria-hidden="true">›</span><span>Vídeos</span></nav>
<div class="tk-band-title"><span class="tk-band-ico">{svg('play', 26)}</span><div><h1>Vídeos tutoriales</h1><p>{len(vids)} vídeos paso a paso. Cada uno va con su guía escrita.</p></div></div>
</div></section>
<main id="main" class="tk-wrap tk-videos"><div class="tk-vgrid">{cards}</div>{contact(ctx, compact=True)}</main>"""
    return page(ctx, "Vídeos tutoriales", body, path="/videos/")


def not_found(ctx: Context) -> str:
    body = f"""
<main id="main" class="tk-wrap-narrow tk-404">
<h1>No encontramos esta página</h1>
<p>Puede que el artículo haya cambiado de sitio. Prueba a buscarlo:</p>
{header_search(ctx, big=True)}
<p><a href="{ctx.url('/')}">Volver al inicio</a></p>
</main>"""
    return page(ctx, "Página no encontrada", body, path="/404.html", search=False)
