---
origen: d16af3650c7f
---

# Come automatizzare l'annullamento per mancato pagamento

Puoi fare in modo che una quota si annulli da sola quando il cliente non la paga. Così non gli vengono più emesse le rate dei mesi successivi.

Si considera mancato pagamento uno qualsiasi di questi casi:

* Una rata domiciliata che la banca restituisce.
* Un addebito automatico su carta che non va a buon fine.
* Una quota emessa che nessuno paga.

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Aprire la quota

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
* Clicca su **Vendite**. Si apre direttamente la scheda **Prodotti**.
* Nella colonna **Categoria**, seleziona **Periodic sale** e clicca sull'**Id** della quota.
* Clicca sull'icona <i class="fa-pen">:pen:</i> per modificarla.

> Se la quota non esiste ancora, puoi compilare questi campi quando la crei. Consulta [Come creare un prodotto di tipo Quota](../../../configuracion/configuracion/ventas/productos/como-crear-un-producto-tipo-cuota.md).
{% endstep %}

{% step %}
### Configurare l'annullamento

*   Nel blocco **Vendite periodiche automatiche**, compila questi campi:

    <figure><img src="../../.gitbook/assets/cuotas-cancelar-impago.png" alt=""><figcaption></figcaption></figure>

    * **Giorni di tolleranza mancato pagamento:** i giorni di attesa, dalla scadenza della quota, prima di annullarla.
    * **Annulla per mancato pagamento:** selezionalo perché la quota si annulli quando passano quei giorni senza pagamento.
* Clicca su **Salva**.
{% endstep %}
{% endstepper %}

## Cosa succede quando viene annullata

Quando passano i giorni di tolleranza e la quota non è ancora stata pagata:

* Smettono di essere emesse le quote dei mesi successivi.
* Il debito che aveva già **non viene cancellato**: resta emesso e in attesa di pagamento in [Vendite › Debiti](../deudas/README.md).
* Se la quota è un abbonamento, il cliente passa al tipo di cliente di disdetta (per esempio, da **Socio** a **Non socio**). Consulta [Che cos'è un abbonamento e come funziona](que-es-una-membresia-y-como-funciona.md).
* Il cliente riceve un'e-mail che lo avvisa che il suo abbonamento è stato annullato. È il modello **Notifica di abbonamento annullato**, che puoi controllare in [Modelli di e-mail](../../../comunicaciones/comunicaciones/plantillas-de-emails.md).

> **Importante:** annullare la quota non disiscrive il cliente dall'attività né dal gruppo dell'accademia a cui è iscritto.
