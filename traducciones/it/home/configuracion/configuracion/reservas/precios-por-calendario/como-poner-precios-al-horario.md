---
icon: display-chart-up-circle-dollar
origen: d2d1d0d733e4
---
# Come assegnare i prezzi all'orario

In **Tariffe per calendario** si decide quale prezzo ha ogni prenotazione in base al giorno e all'ora. Per esempio, puoi far pagare diversamente nell'ora di punta e nell'ora di bassa affluenza. Ogni fascia usa un prodotto di tipo **Service**, che è quello che stabilisce il prezzo.

> **Importante:** qui si cambiano solo i **prezzi**. Non cambiano l'apertura né la disponibilità dei campi. Per questo, consulta questo articolo:
>
> <a href="../horarios/como-crear-un-horario.md" class="button primary">Come creare un orario</a>

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso a Tariffe per calendario

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
*   Clicca su **prenotazioni**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure></div>
*   Clicca sul blocco **Tariffe per calendario**.<br>

    <figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Creare il calendario dei prezzi

* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:

    <div align="left"><figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure></div>

    * **Nome:** ti consigliamo di indicare i giorni della settimana che include.
    * **Priorità:** un numero che decide quale prezzo prevale se due coincidono. Si applica prima quello con il **numero più alto**. Di solito si mette il numero più basso ai giorni feriali, uno maggiore al fine settimana (così puoi applicare il prezzo del fine settimana a un giorno feriale) e il più alto ai festivi o alla chiusura.
    * **Inizio:** data da cui si applicano questi prezzi. Se è da subito, lascialo vuoto.
    * **FINE:** data fino a cui si applicano. Se non è prevista una data di fine, lascialo vuoto.
    * **Giorno della settimana:** seleziona i giorni in cui si applicano questi prezzi.
* Clicca su **Salva**.
{% endstep %}

{% step %}
### Aggiungere le fasce di prezzo

All'interno dello stesso giorno puoi avere più fasce con prezzi diversi (per esempio, ora di punta e ora di bassa affluenza).

* Clicca sull'**Id** del calendario dei prezzi.
*   Vai al blocco **Tariffe**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure></div>
* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:

    <figure><img src="../../../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

    * **Risorsa:** i campi o insegnanti a cui si applica il prezzo.
    * **Inizio:** ora in cui inizia la fascia.
    * **FINE:** ora in cui termina la fascia.
    * **End is next day:** selezionala se la fascia termina alle 00:00 o più tardi.
    * **Applica questo prezzo nelle sovrapposizioni:** se una prenotazione occupa due fasce, si farà pagare tutta con questo prezzo invece di ripartirla tra le due.
    * **Prodotto:** il prodotto di tipo **Service** che stabilisce il prezzo di questa fascia.
* Clicca su <i class="fa-floppy-disk" style="color:green;">:floppy-disk:</i> per salvare.
{% endstep %}
{% endstepper %}

> Se ci sono più fasce con prezzi diversi, ripeti l'ultimo passaggio per ciascuna.

## Se qualcosa non funziona

* **La prenotazione risulta a 0 €:** controlla che il campo sia aggiunto nella fascia, che la fascia copra l'ora della prenotazione e, se termina alle 00:00 o più tardi, che sia selezionato **End is next day**.
* **Ho ampliato l'orario di apertura e non mi lascia prenotare nelle nuove ore:** amplia anche qui la fascia di prezzo. L'orario e i prezzi devono coprire le stesse ore.
* **Un festivo fa pagare il prezzo normale:** controlla che il calendario dei prezzi dei festivi abbia una priorità più alta di quello dei giorni feriali.
