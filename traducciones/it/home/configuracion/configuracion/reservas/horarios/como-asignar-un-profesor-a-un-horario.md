---
icon: circle-user-clock
origen: 62c01ad14b11
---
# Come assegnare un insegnante a un orario

Perché un insegnante si possa prenotare, deve essere in un orario, proprio come i campi. Prima di assegnarlo, l'insegnante deve essere stato creato come risorsa. Se non l'hai ancora fatto, consulta prima questo articolo:

<a href="../grupo-de-recursos/como-anadir-a-un-profesor-nuevo.md" class="button primary">Come aggiungere un nuovo insegnante</a>

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso agli orari

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
*   Clicca su **prenotazioni**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure></div>
*   Clicca sul blocco **Orari**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Aprire l'orario

*   Clicca sull'**Id** dell'orario.<br>

    <figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
*   Apri la scheda **Orari di apertura**.<br>

    <figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Aggiungere l'insegnante

* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:<br>

    <figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

    * **Risorsa:** cerca e aggiungi l'insegnante.
    * **Inizio:** ora in cui l'insegnante inizia a lavorare.
    * **FINE:** ora in cui finisce.
    * **End is next day:** selezionala se l'orario termina alle 00:00 o più tardi.
    * **Intervalli in minuti:** ogni quanti minuti si divide il calendario. Per esempio, con 30 minuti vedrai fasce alle 09:00, 09:30, 10:00, 10:30…
    * **Durata minima:** la durata minima di una prenotazione con l'insegnante. Non può essere inferiore all'intervallo e deve esserne un multiplo.
    * **Durata massima:** la durata massima di una prenotazione con l'insegnante. Deve essere un multiplo dell'intervallo.
* Clicca su **Salva**.
{% endstep %}

{% step %}
### Verificare che funzioni

Ci sono due modi per verificare che l'insegnante sia assegnato correttamente:

**Opzione 1: facendo una prenotazione**

*   Nel calendario, crea una prenotazione in cui devi scegliere l'insegnante.

    <figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
*   Verifica che l'insegnante compaia nell'elenco e che tu possa selezionarlo.

    <figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
* Prova a completare la prenotazione. Se il sistema te lo permette, l'insegnante è configurato correttamente.\
  ![](<../../../.gitbook/assets/image (22).png>)

**Opzione 2: nella vista degli insegnanti**

*   Nel calendario, clicca sulla scheda **Teachers**.<br>

    <figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
*   Verifica che l'insegnante compaia nella griglia.

    <figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
