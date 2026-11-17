---
icon: tennis-ball
origen: 0e5d3f307582
---
# Come creare una risorsa

Una **risorsa** è tutto ciò che si può prenotare o assegnare a un'attività: un campo o un insegnante. Le risorse si raggruppano per sport (padel, tennis, calcio…) e, grazie a loro, il sistema sa cosa è disponibile e in quale orario, per organizzare le prenotazioni senza sovrapposizioni.

Di solito le strutture del club vengono già create nella configurazione iniziale. Se devi aggiungerne una nuova, segui questi passaggi.

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso a Gruppo risorse

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
* Clicca su **prenotazioni**. Si apre direttamente il blocco **Gruppo risorse**.
{% endstep %}

{% step %}
### Creare lo sport (gruppo di risorse)

Se lo sport esiste già, passa direttamente al passaggio 4.

* Clicca su <i class="fa-plus-large">:plus-large:</i> per creare un nuovo sport o non sport.
* Si apre questa finestra. Nell'esempio creiamo il tennis:

<figure><img src="../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

Questi sono i campi obbligatori:

* **Nome:** il nome dello sport.
*   **Ordine:** la posizione in cui si vedrà nel calendario.

    <figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>
* **Sport:** lo sport. Se stai creando insegnanti, scegli **Non sport**.
* **Categoria:** il tipo di risorsa.
* **Intervalli in minuti:** ogni quanti minuti si divide il calendario.
* **Durata minima:** la durata minima di una prenotazione.
* **Durata massima:** la durata massima di una prenotazione.
{% endstep %}

{% step %}
### Campi facoltativi dello sport

* **Modifica livello:** selezionala se i risultati di questo sport fanno salire o scendere il livello del giocatore.
* **Altezza cella calendario:** l'altezza delle caselle del calendario. Di default è 35. Per vedere 4 giocatori in una prenotazione di 1 ora con fasce di 30 minuti, si consiglia 90.
* **Mostra giocatori:** selezionala per vedere i giocatori direttamente nella prenotazione del calendario.
* **Dismesso:** selezionala per smettere di usare questo sport.
* **Mostra iniziali partecipanti:** selezionala perché nel display compaiano le iniziali invece del nome completo.
* **Tempo massimo tra prenotazioni online:** lo spazio libero più piccolo che si può lasciare tra una prenotazione online e l'altra. Serve a evitare spazi così brevi che poi nessuno possa prenotarli.
* **Spazio tra prenotazioni in apertura/chiusura:** come il precedente, ma tenendo conto anche degli spazi con l'ora di apertura e di chiusura.
* **Tempo min. tra prenotazioni admin:** lo spazio libero minimo tra una prenotazione fatta dall'amministrazione e un'altra.
* **Ora inizio giornata:** l'ora in cui inizia la giornata, con un numero intero tra 0 e 23.
{% endstep %}

{% step %}
### Aggiungere i campi (risorse)

* Clicca sull'**Id** dello sport o non sport.
*   Vai al blocco **Risorse**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure></div>
* Clicca su <i class="fa-plus-large">:plus-large:</i>.
* Si apre un'altra finestra:
  * **Nome:** il nome del campo. L'ideale è lo sport e il suo numero (per esempio, _Padel 1_). Se il campo è sponsorizzato, puoi usare il nome dello sponsor.
  * **Ordine:** la posizione in cui comparirà il campo nel calendario.
  * **Tipo di campo:** interno, esterno, coperto, ecc.
  * **Fondo/parete:** dipende dallo sport. Nel tennis o nel calcio si sceglie il tipo di fondo; nel padel o nello squash, il tipo di parete.
*   **Salva e nuovo:** se crei più campi, usa questa opzione. Il campo viene salvato e se ne apre un altro con quasi tutto compilato, tranne il nome e l'ordine.

    <figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Importante:** il campo non comparirà ancora nel calendario. Prima devi assegnargli un orario:

<a href="../horarios/como-crear-un-horario.md" class="button primary">Come creare un orario</a>
