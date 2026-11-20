---
origen: e2ddd803a16d
---

# Dove vedere lo stato di invio delle e-mail

Taykus permette di consultare lo stato delle e-mail inviate ai clienti e di verificare se il sistema ha elaborato correttamente ogni comunicazione.

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso alle e-mail inviate

* Vai al menu laterale a sinistra e seleziona **Comunicazioni**.
*   Nel menu a tendina, scegli **E-mail**. Vedrai l'elenco delle e-mail inviate dal sistema.

    <figure><img src="../.gitbook/assets/reenviar-acceso-emails.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Consultare lo stato

* Trova l'e-mail che vuoi controllare. Puoi usare i filtri di ogni colonna, per esempio **Acquirente** o **Soggetto**.
* Guarda la colonna **Stato di invio**. Questi sono gli stati che vedrai:
  * **Inserito:** l'e-mail è stata creata ed è in attesa di partire.
  * **Inviato:** l'e-mail è partita.
  * **Fallito:** non è stato possibile inviare l'e-mail. Taykus ci prova fino a tre volte prima di segnarla come fallita; la colonna **Tentativi** indica quante volte ci ha provato.
  * **Annullato:** l'invio è stato annullato.

> Nel filtro della colonna compaiono altri stati (**Invio in corso**, **Consegnato**, **Letto**), ma non si usano.

<figure><img src="../.gitbook/assets/estados-envio-correo.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Importante:** lo stato **Inviato** indica che l'e-mail è stata elaborata da Taykus, ma non garantisce che il provider di posta del destinatario l'abbia consegnata nella sua casella.

Se un'e-mail non è arrivata al cliente, puoi inviarla di nuovo. Consulta [Come inviare di nuovo un'e-mail](como-reenviar-un-mail.md).
