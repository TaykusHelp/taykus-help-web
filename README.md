# Centro de ayuda Taykus

Web del Centro de ayuda de Taykus para clubes, con el diseño de la marca (Poppins y colores Taykus).

## Cómo funciona

1. Los artículos se escriben en **GitBook**, como siempre.
2. GitBook los copia al repositorio **taykus-help-center** (Git Sync).
3. Este repositorio coge esos artículos y genera la web. Se publica sola cada hora.

No hace falta tocar nada aquí para publicar un artículo nuevo: basta con escribirlo en GitBook.
Si quieres que salga al momento, entra en la pestaña **Actions**, elige **Publicar centro de ayuda** y pulsa **Run workflow**.

## Lo que se puede cambiar fácilmente

En `config/site.yaml`:

- El texto de la portada.
- El correo de soporte.
- El enlace del botón "Entrar en Taykus".
- La descripción y el icono de cada módulo.
- Qué módulos salen en "Para tus jugadores".

## Qué hace la web con los artículos de GitBook

- Los pasos (stepper) salen numerados con la línea de progreso.
- Los vídeos de YouTube se cargan solo al pulsar (la página va más rápida).
- Las imágenes se amplían al pulsarlas.
- Las pestañas vacías no se muestran.
- Las páginas que solo enlazan a otras se muestran como listado de guías.
- Los enlaces entre espacios de GitBook se convierten en enlaces de la web.

## Otros idiomas (inglés, italiano y francés)

La web tiene un selector de idioma (🌐) arriba a la derecha. Las versiones traducidas están en `/en/`, `/it/` y `/fr/`.

- Los artículos se siguen escribiendo **solo en español**, en GitBook.
- Las traducciones están en `traducciones/en/`, `traducciones/it/` y `traducciones/fr/`, con la misma ruta que el artículo original.
- Cada traducción guarda la huella del artículo en español del que sale. Si cambias un artículo en GitBook (o aún no está traducido), esa versión lo muestra en español con un aviso hasta que se actualice la traducción.
- Las capturas son del panel en español; los artículos traducidos con capturas lo avisan.
- Para ver qué traducciones faltan: Actions › la última publicación › resumen (un apartado por idioma).
- Nombres de módulos y textos de portada de cada idioma: `config/site.yaml`, apartados `en`, `it` y `fr`.

## Para técnicos

Generador estático en Python sin dependencias de JavaScript.

```bash
pip install -r requirements.txt
python build.py --content ../taykus-help-center --out dist
cd dist && python -m http.server 8000
```

- `build.py`: lee el contenido de GitBook y genera las páginas.
- `templates.py`: plantillas HTML.
- `static/`: estilos, buscador (con tolerancia a faltas) y favicon.
- `.github/workflows/publicar.yml`: publicación en GitHub Pages.
- `traducciones/sellar.py`: marca traducciones como al día (`python traducciones/sellar.py --content ../taykus-help-center <archivos>`) y lista las pendientes (`--pendientes en`, `it` o `fr`).
