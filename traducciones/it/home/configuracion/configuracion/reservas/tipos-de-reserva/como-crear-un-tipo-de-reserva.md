---
icon: business-time
origen: a25bf8ff2abf
---
# Come creare un tipo di prenotazione

I **tipi di prenotazione** sono categorie (scuola, lezione privata, partita…) che danno a ogni prenotazione le sue regole: colore, prezzo, durata, chi può prenotare e come. Con loro:

* Distingui a colpo d'occhio ogni prenotazione nel calendario dal suo colore.
* Vedi nei report quante prenotazioni ci sono di ogni tipo.
* Puoi far pagare un prezzo diverso da quello abituale in base al tipo di prenotazione.

<div align="left"><figure><img src="../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure></div>

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso ai tipi di prenotazione

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
* Clicca su **prenotazioni**.\
  ![](<../../../.gitbook/assets/image (97).png>)
*   Clicca sul blocco **TIPOLOGIE DI PRENOTAZIONE**.<br>

    <figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Creare il tipo di prenotazione

* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:<br>

    <figure><img src="../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

> **Importante:** i campi contrassegnati da un asterisco (\*) sono obbligatori.

#### Dati generali

* **Descrizione (\*):** il nome del tipo di prenotazione.
* **Categoria:** facoltativa. Una sottofamiglia per questo tipo.
* **Ordine:** la posizione in cui compare nel calendario.
* **Descrizione estesa:** facoltativa. Dettagli su questo tipo di prenotazione.
* **immagini:** facoltativa. Aiuta a riconoscere il tipo di prenotazione.

#### Prezzo

* **Tipo di prezzo (\*):** scegli nel menu a tendina:
  * **Per risorsa:** si fa pagare il prezzo configurato negli orari.
  * **Per persona:** si fa pagare il prezzo degli orari a ogni partecipante.
  * **Gratis:** non si fa pagare nulla.
* **Prezzo:** un prezzo fisso per questo tipo di prenotazione, senza tener conto delle tariffe per calendario.
* **PrenotazionePerLuogo:** selezionala solo se il tipo di prezzo è **Per persona**.

#### Prenotazione e annullamento online

* **È pubblico:** selezionala perché si possa prenotare online.
* **Consenti annullamento online:** se è attiva, i clienti possono annullare online. Altrimenti può annullare solo il club.
* **Minimo di minuti di anticipo:** con quanto anticipo minimo si può prenotare.
* **Massimo di minuti di anticipo:** con quanto anticipo massimo si può prenotare.
* **Minuti di anticipo per gli annullamenti:** fino a quanti minuti prima si può annullare.
* **Minuti di pre-prenotazione:** i minuti per cui il campo resta bloccato mentre il cliente finisce di prenotare.
* **Ore prima della scadenza:** quante ore prima della prenotazione questa scade se non viene completata.
* **Rimborsa il pagamento in caso di annullamento e scadenza:** selezionala perché il cliente recuperi il denaro se la prenotazione viene annullata o scade senza essere completata.

#### Partecipanti e livello

* **Numero minimo di partecipanti (\*):** il numero minimo di persone per questo tipo di prenotazione.
* **Numero massimo di partecipanti (\*):** il numero massimo di persone.
* **Livello minimo** e **Livello massimo:** il livello di gioco consentito.
* **Genere:**
  * **Maschio:** possono prenotare solo utenti di genere maschile.
  * **Femmina:** possono prenotare solo utenti di genere femminile.
  * **Aperta:** può prenotare chiunque.

#### Limiti

* **Consenti di personalizzare la durata:** permette di cambiare l'ora di fine quando si crea la prenotazione dall'amministrazione.
* **Numero massimo di prenotazioni al giorno:** quante prenotazioni di questo tipo si possono fare al giorno.
* **Numero massimo di prenotazioni:** se c'è un anticipo massimo, conta le prenotazioni da oggi fino a quell'anticipo. Altrimenti conta tutte le prenotazioni da oggi.
* **Restrizioni sul massimo di prenotazioni online e admin:** i limiti si applicano sia alle prenotazioni online sia a quelle del club.

#### Aspetto

* **Colori:** il colore di questo tipo di prenotazione nel calendario. Può essere fisso o cambiare in base allo stato della prenotazione.
{% endstep %}

{% step %}
### Aggiungere le risorse

* In **Tipi di prenotazione**, clicca sull'**Id** del tipo che hai appena creato.
*   Apri la scheda **Risorse**.

    <figure><img src="../../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>
* Clicca su :heavy\_plus\_sign:.
*   Si apre questa finestra:<br>

    <figure><img src="../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

    * **Gruppo risorse:** la risorsa occupata da questo tipo di prenotazione.
    * **Minuti bloccati prima della prenotazione:** quanti minuti prima si blocca la risorsa per prepararla. Per esempio, se la prenotazione inizia alle 10:00 e metti 10 minuti, il campo viene bloccato dalle 9:50.
    * **Durata:** la durata predefinita della prenotazione.
    * **Durate consentite:** le durate che si possono scegliere, in minuti e separate da spazi (per esempio: `30 60 120`). Se lo lasci vuoto, si calcolano in base alla configurazione del gruppo di risorse.
    * **Risorsa principale:** la risorsa che si sceglie per prima.
    * **Selezionabile online:** selezionala perché il cliente possa scegliere questa risorsa quando prenota online.
* Clicca su **Salva**.

> Se il tipo di prenotazione occupa due risorse (per esempio, campo e insegnante), ripeti questo passaggio per ciascuna.
{% endstep %}
{% endstepper %}

## Se qualcosa non funziona

* **Il tipo di prenotazione non compare quando si prenota un campo:** aggiungi quel campo nella scheda **Risorse** del tipo di prenotazione (passaggio 3).
