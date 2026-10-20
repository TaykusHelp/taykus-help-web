# Instrucciones para Claude

Trabajas con Valeria, de soporte en Taykus (software de gestión para clubes deportivos). No es programadora: háblale en español, con pasos sencillos y sin jerga técnica.

Este repositorio es la web del Help Center. Los artículos están en `TaykusHelp/taykus-help-center` (sincronizado con GitBook). Para trabajar necesitas los dos repositorios en la sesión.

- **Antes de empezar, lee `docs/estado-help-center.md`**: datos que Valeria ya ha confirmado (no se los vuelvas a preguntar), criterios de redacción y pendientes. Al terminar, actualízalo con lo hecho y lo nuevo que te confirme, y guárdalo en main.
- Para crear o cambiar artículos sigue el método de abajo (es el mismo que la skill help-center-taykus).


# Artículos del Help Center de Taykus

Valeria es de soporte en Taykus (software de gestión para clubes deportivos) y no es programadora. Háblale en español, con pasos sencillos, sin jerga técnica. Ella decide el contenido; tú redactas, preparas la revisión y publicas.

## Antes de empezar

1. Lee **`docs/estado-help-center.md`** (en este repositorio). Tiene los datos que Valeria ya ha confirmado (no se los vuelvas a preguntar), los criterios de redacción y lo pendiente.
2. Necesitas los dos repositorios de GitHub. Si no están en la sesión, añádelos:
   - `TaykusHelp/taykus-help-center` → los artículos. Se sincroniza solo con GitBook en los dos sentidos.
   - `TaykusHelp/taykus-help-web` → la web (Python) y las traducciones al inglés.
3. Busca el artículo existente (grep por palabras clave en `home/`) antes de crear uno nuevo, por si ya existe.

## Dónde está cada cosa (taykus-help-center)

- Cada módulo es una carpeta: `home/<modulo>/` (calendario, jugadores, academia, configuracion, tpv, ventas, marketing…).
- Artículos: `home/<modulo>/<modulo>/[subcarpeta/]nombre-del-articulo.md` (nombre en minúsculas, sin tildes, con guiones).
- Índice del módulo: `home/<modulo>/SUMMARY.md`. **Un artículo nuevo no aparece si no lo añades aquí**, en el sitio que le toca: `* [Título](<modulo>/ruta/archivo.md)`.
- Imágenes: `home/<modulo>/.gitbook/assets/`. Desde un artículo se enlazan con ruta relativa (`../.gitbook/assets/...` o `../../.gitbook/assets/...` según la profundidad). Las capturas que mande Valeria se copian ahí con un nombre descriptivo (por ejemplo `anadir-promocion.png`).

## Formato de un artículo (sintaxis de GitBook)

```markdown
---
icon: percent
---

# Cómo hacer un código promocional

Introducción de 1–2 frases: qué es y para qué sirve.

A continuación, se detallan los pasos a seguir:

{% stepper %}
{% step %}
### Acceso a Códigos promocionales

* Dirígete al menú lateral izquierdo y selecciona **Marketing**.
*   En el desplegable, haz clic en **Códigos Promocionales**.<br>

    <figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Crear código promocional

* Clica en :heavy\_plus\_sign:
*   Se abre esta ventana:

    <figure><img src="../.gitbook/assets/anadir-promocion.png" alt=""><figcaption></figcaption></figure>

    * **Nombre:** qué es y cómo se rellena.
    * **Cantidad:** …

    > **Importante:** aviso que el club no debe pasar por alto.
* Clica en **Guardar**.
{% endstep %}
{% endstepper %}

Cierre de 1–2 frases (opcional). Enlace a artículos relacionados:
[Cómo limitar un código promocional a ciertos productos](como-limitar-un-codigo-promocional-a-ciertos-productos.md)
```

Otros bloques que ya se usan: `{% tabs %}{% tab title="…" %}…{% endtab %}{% endtabs %}`, `{% embed url="https://youtu.be/…" %}` para vídeos (sección `### Vídeo explicativo`), `{% content-ref url="otro.md" %}` para tarjetas de enlace, `{% file src="…" %}` para descargas. Iconos dentro del texto: `:heavy_plus_sign:`, `<i class="fa-pen">:pen:</i>`, `<i class="fa-gear">:gear:</i>`, `<i class="fa-floppy-disk">:floppy-disk:</i>`.

## Criterios de redacción (acordados con Valeria)

- Tú e imperativo: "Clica", "Selecciona", "Escribe". Nada de "se debe" ni "nos redirige".
- Botones, pestañas, menús y campos en **negrita**, con el nombre exacto que sale en pantalla.
- Acceso a configuración siempre así: "Clica en el icono ⚙ de la esquina superior derecha y entra en **Configuración**."
- Menú lateral izquierdo para los módulos.
- Un paso del stepper = una pantalla o acción. Título del paso corto ("Acceso a…", "Crear…", "Guardar").
- Campos de un formulario: lista con `**Campo:** explicación` (qué es y qué poner, con ejemplo si ayuda).
- Avisos como cita: `> **Importante:** …`.
- No toques imágenes ni vídeos existentes, salvo que Valeria mande capturas nuevas para sustituirlas.
- Frases cortas y claras. Sin relleno de marketing.

## Cómo trabajar un cambio

1. **No inventes cómo funciona el programa.** Si falta un dato (qué hace un campo, qué pasa si se deja vacío, dónde está un botón), pregúntalo. Agrupa las dudas y numéralas.
2. **Recomienda la estructura** cuando haga falta (por ejemplo, si algo opcional merece un artículo aparte para que se encuentre en el buscador).
3. Haz los cambios en una **rama nueva** (`mejora-<tema>`), nunca directamente en main.
4. Prepara una **página de revisión** (artifact) con:
   - Arriba, las **dudas numeradas** (si quedan).
   - El **antes y el después** de cada artículo, lado a lado, con las capturas incrustadas.
   - Para artículos nuevos, el artículo completo tal como se verá.
5. Valeria responde **por número** en el chat. Aplica sus respuestas y, si no quedan dudas, publica.
6. **Publicar**: pasa la rama a main (`git fetch origin main`, `git rebase origin/main`, `git push origin HEAD:main`). GitBook lo recibe solo.
7. **Web**: se publica cada hora. Para que se vea ya: `gh workflow run publicar.yml -R TaykusHelp/taykus-help-web --ref main`, espera a que termine y comprueba la página publicada en https://taykushelp.github.io/taykus-help-web/
8. **Inglés**: actualiza la traducción del artículo (ver abajo).
9. Actualiza **`docs/estado-help-center.md`** y guárdalo en main: lo hecho, los datos nuevos que confirme Valeria y lo pendiente.
10. Recuérdale a Valeria que borre en GitHub las ramas ya publicadas (tú no puedes borrarlas).

## Versión en inglés

- Las traducciones están en `taykus-help-web/traducciones/en/`, con la misma ruta que el artículo original (`traducciones/en/home/<modulo>/...`). Valeria solo escribe en español.
- Cada traducción guarda en su cabecera `origen:` la huella del original. Si el original cambia y no se actualiza la traducción, la web en inglés muestra el artículo en español con un aviso.
- Ver qué falta: `python traducciones/sellar.py --content ../taykus-help-center --pendientes en`
- Tras traducir, sellar: `python traducciones/sellar.py --content ../taykus-help-center traducciones/en/home/...md`
- La traducción conserva exactamente la misma estructura: bloques `{% %}`, imágenes, enlaces (que siguen apuntando a los `.md` en español), vídeos y número de pasos. Solo cambia el texto.
- El panel de Taykus tiene inglés: botones y menús con su nombre en inglés.
- Glosario: reserva = booking, pista = court, bono = voucher (bono monedero = wallet voucher), recarga = top-up, cuota = fee, caja = cash register, TPV = POS, profesor/entrenador = coach, Configuración = Settings, Artículo/Servicio/Cuota = Item/Service/Fee, código promocional = promo code, Guardar = Save.
- Nombres de módulos y textos de la portada en inglés: `taykus-help-web/config/site.yaml`, apartado `en`.

## Comprobar antes de decir que está hecho

- El artículo nuevo está en el `SUMMARY.md` de su módulo.
- Las imágenes que enlaza existen en `.gitbook/assets`.
- `python build.py --content ../taykus-help-center --out /tmp/dist` en taykus-help-web no da avisos nuevos sobre ese artículo e indica "todas las traducciones están al día".
- La página se ve en la web publicada.

Al terminar, cuéntale a Valeria en pocas líneas qué ha cambiado y si queda algo que tenga que hacer ella.
