---
icon: clock-three
origen: c76a56afd4b8
---
# Come creare un orario

I campi e gli insegnanti compaiono nel calendario solo quando hanno un orario. L'orario indica in quali giorni e a che ore è aperta ogni risorsa, e come si può prenotare.

Taykus include due orari già creati. Puoi modificarli o eliminarli e crearne uno nuovo. In questo articolo ti spieghiamo come crearne uno da zero.

### Video esplicativo

{% embed url="https://youtu.be/0UDRdOUjr54" %}

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso agli orari

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
*   Clicca su **prenotazioni**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure></div>
*   Clicca sul blocco **Orari**.<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Creare l'orario

* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure></div>

    * **Nome:** un nome in base ai giorni che include (per esempio, _Feriali_ o _Fine settimana_).
    * **Priorità:** quale prevale se due orari coincidono: vince il **numero più alto**. Di solito si dà più priorità al fine settimana che ai giorni feriali: così, se vuoi che un festivo infrasettimanale funzioni come un sabato, quel giorno userà l'orario del fine settimana.
    * **Inizio/FINE:** date da cui e fino a cui si applica l'orario. Se le lasci vuote, si applica da quando lo salvi.
    * **Giorno della settimana:** seleziona i giorni inclusi in questo orario.
* Clicca su **Salva**.
{% endstep %}

{% step %}
### Aprire gli orari di apertura

* Quando salvi, l'orario si apre nella scheda **Date**.
*   Clicca sulla scheda **Orari di apertura**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure></div>

Qui configurerai due cose:

* **Apertura e chiusura:** quali strutture (padel, tennis, calcio…) seguono questo orario e a che ora aprono e chiudono.
* **Intervalli e durata delle prenotazioni online:** ogni quanto possono prenotare i clienti online (ogni 30, 60 o 90 minuti) e la durata minima e massima delle prenotazioni.

> **Importante:**
>
> * Se il club ha una scuola, aggiungi anche gli **insegnanti** all'orario.
> * Puoi creare tutti gli orari che ti servono. Se tutte le strutture aprono alla stessa ora, mettile in un solo orario; se ognuna ha il suo, creane uno per ciascuna.
{% endstep %}

{% step %}
### Aggiungere gli orari di apertura

* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:<br>

    <figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

    * **Risorsa:** tutti i campi o insegnanti a cui si applica questo orario.
    * **Inizio:** ora di apertura.
    * **FINE:** ora di chiusura.
    * **End is next day:** selezionala se l'orario termina alle 00:00 o più tardi.
    * **Intervalli in minuti:** ogni quanti minuti si divide il calendario. Per esempio, con 30 minuti vedrai fasce alle 09:00, 09:30, 10:00, 10:30…
    * **Durata minima:** la durata minima di una prenotazione. Non può essere inferiore all'intervallo e deve esserne un multiplo.
    * **Durata massima:** la durata massima di una prenotazione. Deve essere un multiplo dell'intervallo.
* Clicca su **Salva**.
{% endstep %}
{% endstepper %}

## Se qualcosa non funziona

* **Il campo non compare nel calendario:** verifica che sia stato aggiunto in **Orari di apertura** (passaggio 4). Creare l'orario senza aggiungere il campo non basta.
* **Ho ampliato l'orario e non mi lascia prenotare nelle nuove ore:** amplia anche la fascia nelle tariffe per calendario. L'orario e i prezzi devono coprire le stesse ore. Per farlo, consulta questo articolo:

  <a href="../precios-por-calendario/como-poner-precios-al-horario.md" class="button primary">Come assegnare i prezzi all'orario</a>
* **Non mi lascia salvare la durata:** la durata minima e quella massima devono essere multipli dell'intervallo. Con un intervallo di 30 minuti puoi mettere 60 o 90, ma non 45.
