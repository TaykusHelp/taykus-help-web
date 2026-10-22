# Taykus Help Center (nuevo) — estado del proyecto

Actualizado: 22 oct 2026

## Cómo está montado
- Los artículos se escriben en GitBook (taykus-help-center.gitbook.io).
- Git Sync copia GitBook ↔ GitHub, repositorio `TaykusHelp/taykus-help-center` (rama main). Los cambios de Claude en GitHub vuelven a GitBook solos.
- La web vive en `TaykusHelp/taykus-help-web`: generador en Python (build.py + templates.py + static/), sin dependencias JS.
- Web publicada: https://taykushelp.github.io/taykus-help-web/ (GitHub Pages, repos públicos). Se publica cada hora, al cambiar el repo de la web y al pulsar Actions › Publicar centro de ayuda › Run workflow.
- Textos de portada, correo de soporte, descripciones e iconos de módulos: `config/site.yaml` (apartado `en` para inglés).
- Chat de claude.ai (desde 20 oct): instalado el "Claude Github MCP Connector" en la cuenta TaykusHelp, así que se puede leer y guardar texto en los dos repositorios. No puede subir imágenes (Valeria las sube en GitHub con "Add file › Upload files" en la rama), ni borrar ramas, ni lanzar la publicación de la web. Desde Claude Code sí se puede todo.
- Publicar desde el chat: Claude crea la rama y guarda (si son muchos archivos, Valeria los sube arrastrando la carpeta en GitHub y Claude comprueba que todo coincide); Valeria crea la petición en GitHub (Compare & pull request › Create pull request, porque el formulario del chat no le aparece) y Claude la pasa a main. Primero artículos, después web.

## Versión en inglés (publicada 16 oct)
- Selector ES / EN en la cabecera (también en móvil). Inglés en /en/ con las mismas direcciones que en español. La web recuerda si el visitante eligió inglés.
- Traducciones en `taykus-help-web/traducciones/en/` (no están en GitBook). Valeria sigue escribiendo solo en español.
- Cada traducción guarda la huella ("origen") del artículo en español. Si el original cambia, la web en inglés lo muestra en español con un aviso. El resumen de cada publicación en Actions lista las traducciones pendientes. Para ponerlas al día: `python traducciones/sellar.py --content ../taykus-help-center --pendientes en`, traducir y sellar con `python traducciones/sellar.py --content ../taykus-help-center <archivos>`.
- 194 archivos traducidos (159 artículos + portadas de sección). El panel de Taykus tiene inglés, así que botones y menús van con nombre en inglés (puestos por Claude, a falta de confirmar con el panel real).
- Glosario: reserva = booking, pista = court, bono = voucher (bono monedero = wallet voucher), recarga = top-up, cuota = fee, caja = cash register, TPV = POS, profesor/entrenador = coach, Configuración = Settings, Artículo/Servicio/Cuota = Item/Service/Fee, código promocional = promo code, cliente responsable = responsible customer, Asociados = Associates, Crear Nuevo = Create New (estos tres, a falta de confirmar con el panel en inglés).

## Diseño
- Manual de identidad Taykus: azul #055AE2, celeste #18BBEA, azul noche #011733, degradado Taykus. Poppins para textos, Montserrat solo en el logotipo.

## Hecho
- 17 módulos, 166 artículos, 27 con vídeo, ~390 imágenes importadas.
- Pasos numerados, pestañas (se ocultan las vacías), vídeos que cargan al pulsar, imágenes ampliables, índice del artículo, relacionados, "¿Te ha sido útil?".
- Buscador con tolerancia a faltas, fragmento resaltado y filtros por módulo y "con vídeo". En inglés tiene su propio índice.
- Artículos antiguos pasados a pasos (5 oct): cerrar una pista, Display, crear jugador, recargar bono, correo masivo, tipos de jugador.
- Redacción revisada y validada por Valeria: Calendario (16 artículos) y Configuración (46 artículos), 6 oct.
- Códigos promocionales (Marketing), 16 oct: "Cómo hacer" actualizado al formulario nuevo, "Cómo editar" con captura nueva, y artículo nuevo "Cómo limitar un código promocional a ciertos productos".
- Errata corregida (20 oct): Apple "Cómo crear una cuenta de desarrollador" decía "Google" en el D-U-N-S; ahora dice "Apple". Traducción al inglés resellada.
- Enlaces entre artículos pasados a botón (20 oct): 25 enlaces en 23 artículos, con el título real del artículo. Veri*FACTU con botón "Ir a la sede de la Agencia Tributaria". En "Cómo añadir a un profesor nuevo", botón también en el aviso inicial y botón final con el título real. Mismo cambio en las traducciones al inglés, reselladas. Las tarjetas de las portadas de sección no se tocaron.
- Cliente responsable (21 oct): 3 artículos nuevos: "Cómo asignar un cliente responsable a un jugador" y "Cómo ver los clientes asociados a un jugador" (Jugadores) y "Cómo cambiar entre tu cuenta y la de tus asociados en la zona de clientes" (Zona de clientes). Jugadores reorganizado en grupos: Fichas de jugador (crear, tipos, nivel, cliente responsable, asociados) y Bonos (recargar, transferir, restar); "Cómo enviar un correo masivo" queda suelto al final. Portada del módulo con la tarjeta de nivel, que faltaba. Cambian las direcciones web de los artículos movidos. Traducciones movidas y reselladas. En la captura de "Crear Nuevo" se difuminó la lista de clientes reales.
- Cliente responsable dividido (21 oct): "Cómo asignar…" queda solo con los pasos (y un aviso en Guardar sobre el correo y el teléfono) y el artículo nuevo "Qué cambia cuando un jugador tiene cliente responsable" recoge correo y teléfono, cobros en el TPV, zona de clientes y cómo quitar la relación. Criterio: separar el "cómo se hace" del "qué implica" cuando las dudas llegan en momentos distintos.
- Revisión de claridad (21 oct): leídos como club todos los módulos sin revisar (todos menos Calendario y Configuración). 31 artículos corregidos: recuento de caja (decía que cerraba la caja), abrir caja desde el TPV (orden de pasos, falta "Abrir"), crear actividad (textos copiados de Academia), restar stock (no hay campo motivo), Comunicaciones (cómo llegar a cada pantalla), Q19 (aviso de error y prefijo del banco), "Participantes" y "Número máximo de participantes" (sirven para lo mismo), "Dónde ver el estado de envío de los correos" completado, títulos "Vídeo explicativo" sin vídeo quitados en Cajas, y erratas.
- Cuotas (21 oct): escritos los 5 artículos vacíos y 2 nuevos ("Cómo ver las cuotas" y "Cómo restablecer una cuota"). "Cómo modificar precio a una couta" pasa a "Cómo modificar el precio de una cuota" y "Cómo cambiar día de vencimiento" a "Cómo cambiar el día de vencimiento de una cuota". Academia › Cuotas enlaza a "Cómo ver las cuotas". "Cómo crear un producto tipo Cuota" actualizado al formulario nuevo (membresías, impagos, emisión automática; ya no hay Marca ni Venta en TPV).
- Aviso de reservas (22 oct): artículo nuevo "Cómo recibir un email cuando alguien reserva o cancela" (Configuración › Reservas › Grupo de recursos), a petición de un club.

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
- Cuotas: se ven en Ventas › Cuotas › Id › pestaña Calendario (todas las personas), en la ficha del jugador › Facturación › Cuotas (todas las suyas) o desde el grupo de academia. Se marca el círculo del mes y se usa el botón Acciones. Sin emitir: Pagar, Emitir, Modificar Precio, Omitir, Cambiar Día Vencimiento. Emitida: Pagar o Restablecer. El círculo del jugador marca su fila; el del mes, la columna. Los cambios solo afectan a las cuotas marcadas.
- Cuotas: emitir = línea de venta pendiente que el cliente ve en su zona de clientes. Pagar lleva al TPV y emite las no emitidas. Omitir = no se cobra ni se remesa (queda en gris). Restablecer = deshace la emisión y quita la línea pendiente. Colores: azul sin emitir, naranja emitida, verde pagada, gris omitida.
- Producto tipo Cuota: emisión automática en el apartado Cuotas Automáticas (también hay un check por jugador en la lista de jugadores de la cuota). Tipo Cliente Membresía / Baja Membresía = tipo de cliente al suscribirse / al terminar (como la cuota de un gimnasio). Días Cortesía Impago = días tras un impago antes de dar de baja la membresía. Cancelar con Impago = cancela la cuota y su origen (actividad, grupo de escuela…). Tipo de impuestos se elige siempre en el desplegable. El apartado Visibilidad sale vacío.
- Aviso de reservas: campo "Email Notificación Reserva" de cada pista (Configuración › Reservas › Id del deporte › Recursos). Pista por pista, un solo correo por pista. Llega con cualquier reserva (club, web o app) y al cancelar; los jugadores no pueden modificar sus reservas. No hay otro tipo de aviso, solo correo. Desde el listado se escribe en la columna y se guarda con Enter; desde la ficha, con Guardar.
- Actividades y preinscripciones: "Participantes" y "Número máximo de participantes" sirven para lo mismo. Restar stock no tiene campo de motivo. No hay vídeos de Cajas. "Calendario de alumnos" se llama así en el programa.

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
- Comunicaciones: escribir "Cómo cancelar envíos" y "Cómo reenviar un mail" (faltan datos de Valeria).
- Siguiente módulo a revisar (por decidir): Ventas, TPV, Academia, Jugadores…
- Confirmar con el panel en inglés los nombres de botones y menús de la traducción.
- Erratas en español: "Cómo crear categorias" (Actividades) no lleva tilde en el título.
- Artículos vacíos por escribir con Valeria: Ventas › Pagos, Bonos y Deudas; Configuración › Campos personalizados y Registro.
- Incompletos: Configuración › Zona de Jugadores (5 de 6 pestañas vacías: Principal, Detalles, Testimonios, Nuestro Equipo, Patrocinadores); pestaña "Ventas" vacía en las portadas de Academia y Preinscripciones; pestañas "Cuotas" y "Ventas" de crear actividad y crear preinscripción sin explicar.
- Borrar las ramas `mejora-cliente-responsable-dividir`, `mejora-claridad-cuotas` y `mejora-aviso-reservas` en los dos repositorios.
- Dominio propio (ayuda.taykus.com): registro DNS por quien gestione el dominio.
- Unas 11 imágenes siguen alojadas en GitBook (pegadas como enlace); conviene resubirlas en GitBook.
- "¿Te ha sido útil?" aún no guarda las respuestas.
- Estructura en GitBook: portada con texto de plantilla, Pedidos/Reportes "Page" vacíos, Equipos vacío con descripción de Jugadores.
