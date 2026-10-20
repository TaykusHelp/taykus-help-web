# Taykus Help Center (nuevo) — estado del proyecto

Actualizado: 20 oct 2026

## Cómo está montado
- Los artículos se escriben en GitBook (taykus-help-center.gitbook.io).
- Git Sync copia GitBook ↔ GitHub, repositorio `TaykusHelp/taykus-help-center` (rama main). Los cambios de Claude en GitHub vuelven a GitBook solos.
- La web vive en `TaykusHelp/taykus-help-web`: generador en Python (build.py + templates.py + static/), sin dependencias JS.
- Web publicada: https://taykushelp.github.io/taykus-help-web/ (GitHub Pages, repos públicos). Se publica cada hora, al cambiar el repo de la web y al pulsar Actions › Publicar centro de ayuda › Run workflow.
- Textos de portada, correo de soporte, descripciones e iconos de módulos: `config/site.yaml` (apartado `en` para inglés).

## Versión en inglés (publicada 16 oct)
- Selector ES / EN en la cabecera (también en móvil). Inglés en /en/ con las mismas direcciones que en español. La web recuerda si el visitante eligió inglés.
- Traducciones en `taykus-help-web/traducciones/en/` (no están en GitBook). Valeria sigue escribiendo solo en español.
- Cada traducción guarda la huella ("origen") del artículo en español. Si el original cambia, la web en inglés lo muestra en español con un aviso. El resumen de cada publicación en Actions lista las traducciones pendientes. Para ponerlas al día: `python traducciones/sellar.py --content ../taykus-help-center --pendientes en`, traducir y sellar con `python traducciones/sellar.py --content ../taykus-help-center <archivos>`.
- 194 archivos traducidos (159 artículos + portadas de sección). El panel de Taykus tiene inglés, así que botones y menús van con nombre en inglés (puestos por Claude, a falta de confirmar con el panel real).
- Glosario: reserva = booking, pista = court, bono = voucher (bono monedero = wallet voucher), recarga = top-up, cuota = fee, caja = cash register, TPV = POS, profesor/entrenador = coach, Configuración = Settings, Artículo/Servicio/Cuota = Item/Service/Fee, código promocional = promo code.

## Diseño
- Manual de identidad Taykus: azul #055AE2, celeste #18BBEA, azul noche #011733, degradado Taykus. Poppins para textos, Montserrat solo en el logotipo.

## Hecho
- 17 módulos, 159 artículos, 27 con vídeo, ~380 imágenes importadas.
- Pasos numerados, pestañas (se ocultan las vacías), vídeos que cargan al pulsar, imágenes ampliables, índice del artículo, relacionados, "¿Te ha sido útil?".
- Buscador con tolerancia a faltas, fragmento resaltado y filtros por módulo y "con vídeo". En inglés tiene su propio índice.
- Artículos antiguos pasados a pasos (5 oct): cerrar una pista, Display, crear jugador, recargar bono, correo masivo, tipos de jugador.
- Redacción revisada y validada por Valeria: Calendario (16 artículos) y Configuración (46 artículos), 6 oct.
- Códigos promocionales (Marketing), 16 oct: "Cómo hacer" actualizado al formulario nuevo, "Cómo editar" con captura nueva, y artículo nuevo "Cómo limitar un código promocional a ciertos productos".
- Errata corregida (20 oct): Apple "Cómo crear una cuenta de desarrollador" decía "Google" en el D-U-N-S; ahora dice "Apple". Traducción al inglés resellada.

## Datos confirmados por Valeria (para no volver a preguntar)
- Prioridad de horarios y precios por calendario: gana el número más alto. Entre semana el más bajo, fin de semana mayor, festivo/cerrado el más alto (100).
- Marcas: etiquetas libres para filtrar (normalmente el fabricante, pero el nombre es libre).
- Bono de horas: Tipo de cantidad = Unidades. Los bonos se guardan con Guardar.
- Recursos: "No Deporte" se elige en el campo Deporte. "Máximo tiempo entre reservas online" = hueco libre mínimo permitido entre reservas online.
- Usuarios: sale directamente en el desplegable del engranaje (no dentro de Configuración).
- Acceso de profesores: https://<club>.taykus…/teachers/login
- Ventanas de empresa del club y empresa cliente son prácticamente idénticas.
- Códigos promocionales: Cantidad = el mismo código se crea N veces (= N usos), máximo 1000. Empieza por (prefijo) o Texto exacto (código fijo), solo uno. Fechas vacías = activo ya / no caduca. Límite por cliente: no se menciona. Productos permitidos: se añaden después de crear, dentro de la promoción (clic en id › scroll › + › Producto › Guardar); sin productos = vale para todos. "Copiar productos a…" = desde la promoción que los tiene hacia otra; "Copiar productos desde…" = desde la nueva, traerlos de otra.
- El panel de Taykus tiene versión en inglés.

## Criterios de redacción (acordados)
- Introducción de 1–2 frases, "A continuación, se detallan los pasos a seguir:", pasos con stepper.
- Tú/imperativo ("Clica", "Selecciona"), menú lateral izquierdo, botones en negrita.
- Acceso a configuración: "Clica en el icono ⚙ de la esquina superior derecha y entra en Configuración".
- Avisos como cita "> **Importante:**". No tocar imágenes ni vídeos (salvo capturas nuevas que mande Valeria).
- Revisión de Valeria antes de publicar: página de antes/después con las dudas numeradas; ella responde por número en el chat.

## Pendiente
- Siguiente módulo a revisar (por decidir): Ventas, TPV, Academia, Jugadores…
- Confirmar con el panel en inglés los nombres de botones y menús de la traducción.
- Erratas en español: "Cómo recargar un bono desde el TPV" dice en la intro "venta con un producto abierto"; "Cómo modificar precio a una couta" solo tiene una nota interna; "Cómo hgacer un recuento de caja" en la pestaña de Cajas; el recuento dice "confirmar el cierre de caja".
- Borrar las ramas `mejora-configuracion`, `mejora-codigos-promocionales`, `mejora-errata-apple` (help-center) e `ingles` (web) en GitHub.
- Dominio propio (ayuda.taykus.com): registro DNS por quien gestione el dominio.
- Unas 11 imágenes siguen alojadas en GitBook (pegadas como enlace); conviene resubirlas en GitBook.
- "¿Te ha sido útil?" aún no guarda las respuestas.
- Estructura en GitBook: portada con texto de plantilla, Pedidos/Reportes "Page" vacíos, Equipos vacío con descripción de Jugadores, "couta" en Ventas.
