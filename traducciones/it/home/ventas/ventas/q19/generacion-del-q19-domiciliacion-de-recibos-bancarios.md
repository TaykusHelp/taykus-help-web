---
icon: money-bill-transfer
origen: fdf667ab9773
---
# Generazione del Q19 (addebito diretto delle rate bancarie)

In questo articolo vediamo come creare un file **Q19** per gestire le rimesse delle quote, come aggiungere le righe corrispondenti e quali verifiche fare prima di chiuderlo e scaricarlo.

Qui sotto trovi un video esplicativo con tutti i passaggi:

### Video esplicativo

{% embed url="https://youtu.be/IA2_rz0yjHM" %}

In questo articolo vediamo come fare:

### Prima di iniziare

Prima di generare un Q19, controlla che questi dati siano stati creati in:

* **Impostazioni > Vendite > Aziende**

Per sapere come fare, consulta questo articolo:

<a href="antes-de-empezar-a-remesar.md" class="button primary">Prima di iniziare a fare rimesse</a>

{% stepper %}
{% step %}
### Accesso alla sezione Q19

* Vai al menu a sinistra e seleziona **Vendite.**
* Clicca su **Q19**.
*   Da questa sezione puoi consultare le rimesse già create o generarne una nuova.<br>

    <figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Creare un nuovo file Q19

Una volta dentro **Q19**, premi il pulsante **aggiungi** per creare un nuovo file.

Poi compila i campi principali:

* **Descrizione**: inserisci un nome che identifichi la rimessa.\
  Esempio: **RIMESSA QUOTE SOCI APRILE 2026**
* **ID emittente**: seleziona l'emittente corrispondente.
*   **Commenti dei clienti**: questo campo è facoltativo.<br>

    <figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

Quando hai completato i dati, premi **Salva**.
{% endstep %}

{% step %}
### Aggiungere le righe al Q19

*   Una volta salvato il file, entra nella sezione **Righe Q19** e premi il pulsante **+** per aggiungere le righe da includere nella rimessa.<br>

    <figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
*   Si apre una finestra con gli **Articoli in vendita**, dalla quale puoi trovare facilmente le quote da includere nel file.<br>

    <figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Filtrare correttamente le righe

Per trovare solo le righe che devono far parte della rimessa, è importante applicare i filtri giusti.

* #### Stato dello scontrino
  * Filtra per **In attesa di**, per mostrare solo le righe non ancora elaborate.
* #### Due date
  * Usa questo filtro per trovare le quote del periodo che vuoi includere nella rimessa.
* #### Tipo di prodotto
  * Filtra per **Quote Soci**, così compaiono solo le righe delle quote dei soci e non altri prodotti o prenotazioni.

Una volta applicati i filtri, seleziona le righe che vuoi includere e premi **Selezionare**.
{% endstep %}

{% step %}
### Verificare se ci sono errori

Quando selezioni le righe, può comparire un avviso di **Errore**. Se compare, clicca su **OK** e controlla gli errori come spiegato qui sotto.

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

*   Nello stesso file Q19 trovi anche la scheda **Errori**.<br>

    <figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
* Da questa scheda puoi individuare i problemi prima di chiudere la rimessa. Se una riga non va inclusa o presenta qualche problema, controllala prima di continuare e seleziona scarta.
* Inoltre, dallo stesso Q19 puoi eliminare le righe aggiunte se devi correggere la selezione.
{% endstep %}

{% step %}
### Controllare le righe aggiunte

*   Tornando al file Q19, vedrai le righe incluse nella sezione **linee**.<br>

    <figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
* Da qui puoi controllare informazioni come:
  * **Cliente**
  * **Nome del titolare**
  * **Concetto**
  * **Quantità**
* È importante controllare che le righe incluse siano corrette prima di continuare.
{% endstep %}

{% step %}
### Chiudere il file Q19

* Quando hai verificato che tutte le righe sono corrette, clicca su chiudere.
* Il programma mostra un avviso con l'importo totale e il numero di pagamenti.\
  ![](<../../.gitbook/assets/image (19).png>)
* Clicca su **OK.**
* Fatto questo, il file cambia stato in **Chiuso.**
* Questo passaggio è indispensabile per preparare correttamente il file.
{% endstep %}

{% step %}
### Scaricare il file

*   Quando lo stato del Q19 è **Chiuso**, puoi usare l'opzione **Scaricamento** per ottenere il file generato.<br>

    <figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
* Questo è il file che potrai usare per gestire la rimessa e caricare in banca.
{% endstep %}
{% endstepper %}

Prima di chiudere e scaricare il file, ricorda di verificare che le righe incluse corrispondano al periodo corretto, che appartengano al tipo di prodotto **Quote Soci** e che non ci siano problemi nella scheda degli errori.

Così potrai generare correttamente il file Q19 con le righe da includere nella rimessa.
