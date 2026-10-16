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

## Versión en inglés

La web tiene un selector **ES / EN** arriba a la derecha. La versión en inglés está en `/en/`.

- Los artículos se siguen escribiendo **solo en español**, en GitBook.
- Las traducciones están en `traducciones/en/`, con la misma ruta que el artículo original.
- Cada traducción guarda la huella del artículo en español del que sale. Si cambias un artículo en GitBook, la web en inglés muestra ese artículo en español con un aviso hasta que se actualice la traducción.
- Para ver qué traducciones faltan: Actions › la última publicación › resumen (apartado "Traducciones al inglés").
- Nombres de módulos y textos de portada en inglés: `config/site.yaml`, apartado `en`.

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
- `traducciones/sellar.py`: marca traducciones como al día (`python traducciones/sellar.py --content ../taykus-help-center <archivos>`) y lista las pendientes (`--pendientes en`).
