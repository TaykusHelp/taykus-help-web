# Taykus Help Center (nuevo) — estado del proyecto

Actualizado: 21 oct 2026

## Cómo está montado
- Los artículos se escriben en GitBook (taykus-help-center.gitbook.io).
- Git Sync copia GitBook ↔ GitHub, repositorio `TaykusHelp/taykus-help-center` (rama main). Los cambios de Claude en GitHub vuelven a GitBook solos.
- La web vive en `TaykusHelp/taykus-help-web`: generador en Python (build.py + templates.py + static/), sin dependencias JS.
- Web publicada: https://taykushelp.github.io/taykus-help-web/ (GitHub Pages, repos públicos). Se publica cada hora, al cambiar el repo de la web y al pulsar Actions › Publicar centro de ayuda › Run workflow.
- Textos de portada, correo de soporte, descripciones e iconos de módulos: `config/site.yaml` (apartado `en` para inglés).
- Chat de claude.ai (desde 20 oct): instalado el "Claude Github MCP Connector" en la cuenta TaykusHelp, así que se puede leer y guardar texto en los dos repositorios. No puede subir imágenes (Valeria las sube en GitHub con "Add file › Upload files" en la rama), ni borrar ramas, ni lanzar la publicación de la web. Desde Claude Code sí se puede todo.

## Versión en inglés (publicada 16 oct)
- Selector ES / EN en la cabecera (también en móvil). Inglés en /en/ con las mismas direcciones que en español. La web recuerda si el visitante eligió inglés.
- Traducciones en `taykus-help-web/traducciones/en/` (no están en GitBook). Valeria sigue escribiendo solo en español.
- Cada traducción guarda la huella ("origen") del artículo en español. Si el original cambia, la web en inglés lo muestra en español con un aviso. El resumen de cada publicación en Actions lista las traducciones pendientes. Para ponerlas al día: `python traducciones/sellar.py --content ../taykus-help-center --pendientes en`, traducir y sellar con `python traducciones/sellar.py --content ../taykus-help-center <archivos>`.
- 194 archivos traducidos (159 artículos + portadas de sección). El panel de Taykus tiene inglés, así que botones y menús van con nombre en inglés (puestos por Claude, a falta de confirmar con el panel real).
- Glosario: reserva = booking, pista = court, bono = voucher (bono monedero = wallet voucher), recarga = top-up, cuota = fee, caja = cash register, TPV = POS, profesor/entrenador = coach, Configuración = Settings, Artículo/Servicio/Cuota = Item/Service/Fee, código promocional = promo code, cliente responsable = responsible customer, Asociados = Associates, Crear Nuevo = Create New (estos tres, a falta de confirmar con el panel en inglés).

## Diseño
- Manual de identidad Taykus: azul #055AE2, celeste #18BBEA, azul noche #011733, degradado Taykus. Poppins para textos, Montserrat solo en el logotipo.

## Hecho
- 17 módulos, 162 artículos, 27 con vídeo, ~390 imágenes importadas.
- Pasos numerados, pestañas (se ocultan las vacías), vídeos que cargan al pulsar, imágenes ampliables, índice del artículo, relacionados, "¿Te ha sido útil?".
- Buscador con tolerancia a faltas, fragmento resaltado y filtros por módulo y "con vídeo". En inglés tiene su propio índice.
- Artículos antiguos pasados a pasos (5 oct): cerrar una pista, Display, crear jugador, recargar bono, correo masivo, tipos de jugador.
- Redacción revisada y validada por Valeria: Calendario (16 artículos) y Configuración (46 artículos), 6 oct.
- Códigos promocionales (Marketing), 16 oct: "Cómo hacer" actualizado al formulario nuevo, "Cómo editar" con captura nueva, y artículo nuevo "Cómo limitar un código promocional a ciertos productos".
- Errata corregida (20 oct): Apple "Cómo crear una cuenta de desarrollador" decía "Google" en el D-U-N-S; ahora dice "Apple". Traducción al inglés resellada.
- Enlaces entre artículos pasados a botón (20 oct): 25 enlaces en 23 artículos, con el título real del artículo. Veri*FACTU con botón "Ir a la sede de la Agencia Tributaria". En "Cómo añadir a un profesor nuevo", botón también en el aviso inicial y botón final con el título real. Mismo cambio en las traducciones al inglés, reselladas. Las tarjetas de las portadas de sección no se tocaron.
- Cliente responsable (21 oct): 3 artículos nuevos: "Cómo asignar un cliente responsable a un jugador" y "Cómo ver los clientes asociados a un jugador" (Jugadores) y "Cómo cambiar entre tu cuenta y la de tus asociados en la zona de clientes" (Zona de clientes). Jugadores reorganizado en grupos: Fichas de jugador (crear, tipos, nivel, cliente responsable, asociados) y Bonos (recargar, transferir, restar); "Cómo enviar un correo masivo" queda suelto al final. Portada del módulo con la tarjeta de nivel, que faltaba. Cambian las direcciones web de los artículos movidos. Traducciones movidas y reselladas. En la captura de "Crear Nuevo" se difuminó la lista de clientes reales.

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
- Cliente responsable: se asigna desde la ficha del asociado (Jugadores › Id › lápiz › Información de Contacto Adicional › Cliente Responsable › Guardar). Buscador por cualquier dato de la ficha (nombre, apellido, DNI…); "Crear Nuevo" abre la ficha de crear jugador. Solo uno por jugador; un responsable puede tener varios asociados. Sirve para cualquier relación (no solo hijos y tutores).
- Si el asociado tiene vacíos correo o teléfono, se rellenan con los del responsable; al correo se le añade "+número" antes de la @ y lo enviado llega al responsable. Si ya los tiene, no se tocan. Solo hablar de correos (no de SMS ni notificaciones).
- Quitar la relación: vaciar el campo y Guardar. El correo generado se queda y no avisa.
- Pestaña Asociados: solo muestra jugadores en la ficha del responsable.
- Cobro con tarjeta guardada y bono monedero del responsable: en el TPV (al pasar el ratón sale "Propietario") y en la zona de clientes ("Pagable con bono" y la tarjeta con el nombre del responsable).
- Zona de clientes: el responsable entra con su usuario y cambia de cuenta en el desplegable de su nombre. El asociado solo entra por su cuenta si tiene correo propio.

## Criterios de redacción (acordados)
- Introducción de 1–2 frases, "A continuación, se detallan los pasos a seguir:", pasos con stepper.
- Tú/imperativo ("Clica", "Selecciona"), menú lateral izquierdo, botones en negrita.
- Acceso a configuración: "Clica en el icono ⚙ de la esquina superior derecha y entra en Configuración".
- Avisos como cita "> **Importante:**". No tocar imágenes ni vídeos (salvo capturas nuevas que mande Valeria).
- Enlaces a otros artículos: siempre como botón `<a href="ruta.md" class="button primary">Título real del artículo</a>`, sin icono. Si el enlace va en mitad de una frase (también en listas y avisos), la frase termina con "consulta este artículo:" y el botón va debajo. Nada de "léase/véase el siguiente artículo" ni "haz clic en el siguiente enlace". Las tarjetas de las portadas de sección no se tocan.
- Revisión de Valeria antes de publicar: página de antes/después con las dudas numeradas; ella responde por número en el chat. Números de dudas y pasos en azul, como en la web.
- Capturas: difuminar datos personales reales (nombres, teléfonos, correos) antes de publicarlas.
- Comprobar la web publicada: si Claude no puede abrirla, no se queda esperando; avisa a Valeria y lo comprueba ella.

## Pendiente
- Siguiente módulo a revisar (por decidir): Ventas, TPV, Academia, Jugadores…
- Confirmar con el panel en inglés los nombres de botones y menús de la traducción.
- Erratas en español: "Cómo recargar un bono desde el TPV" dice en la intro "venta con un producto abierto"; "Cómo modificar precio a una couta" solo tiene una nota interna; "Cómo hgacer un recuento de caja" en la pestaña de Cajas; el recuento dice "confirmar el cierre de caja"; "Cómo crear categorias" (Actividades) no lleva tilde en el título.
- Borrar las ramas `mejora-configuracion`, `mejora-codigos-promocionales`, `mejora-errata-apple`, `mejora-enlaces-botones`, `prueba-acceso`, `mejora-cliente-responsable` (help-center) e `ingles`, `mejora-enlaces-botones`, `prueba-acceso`, `mejora-cliente-responsable` (web) en GitHub.
- Dominio propio (ayuda.taykus.com): registro DNS por quien gestione el dominio.
- Unas 11 imágenes siguen alojadas en GitBook (pegadas como enlace); conviene resubirlas en GitBook.
- "¿Te ha sido útil?" aún no guarda las respuestas.
- Estructura en GitBook: portada con texto de plantilla, Pedidos/Reportes "Page" vacíos, Equipos vacío con descripción de Jugadores, "couta" en Ventas.
