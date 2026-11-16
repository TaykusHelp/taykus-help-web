---
origen: d81b4ae3af17
---

# Come creare un prodotto di tipo Quota

I prodotti di tipo **Periodic sale** (quota) sono quelli che si incassano periodicamente, come una mensilità, una quota trimestrale o un abbonamento annuale. Nella loro scheda si definisce ogni quanto e come si incassano, così il sistema gestisce gli incassi ricorrenti.

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso ai prodotti

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
* Clicca su **Vendite**. Si apre direttamente la scheda **Prodotti**.
{% endstep %}

{% step %}
### Creare il prodotto

* Clicca su :heavy\_plus\_sign:.
* Si apre la scheda del prodotto.
{% endstep %}

{% step %}
### Generale

<figure><img src="../../../.gitbook/assets/producto-cuota-general.png" alt=""><figcaption></figcaption></figure>

* **Logo:** facoltativo. Aiuta a riconoscere il prodotto nel POS. Puoi caricare un'immagine con **Navigare** o sceglierne una dalla **Galleria**.
* **Nome:** nome descrittivo della quota. Campo obbligatorio.
* **Categoria:** è impostata su **Article** di default. Cambiala in **Periodic sale**.
* **Prezzo lordo:** prezzo di vendita al pubblico, tasse incluse. Campo obbligatorio.
* **Prezzo netto:** prezzo senza tasse. Si calcola automaticamente in base al tipo di imposta.
* **Tipo di tasse:** scegli nel menu a tendina l'imposta che si applica alla quota. Campo obbligatorio.
* **Tipo di prodotto:** scegli uno dei tipi di prodotto che hai già creato.
* **Punti fedeltà:** importo che viene ricaricato nel buono di denaro del cliente per ogni unità acquistata, nell'unità minima della tua valuta (in euro, centesimi). Per esempio, se scrivi 2, il cliente riceve 2 centesimi per ogni unità acquistata.
{% endstep %}

{% step %}
### Vendita online

* **Dettaglio:** testo facoltativo per spiegare le condizioni della quota.
* **Vendita online:** selezionala se si può acquistare online.
* **Tendenza:** mette in evidenza la quota nella vendita online come opzione consigliata.
* **Popolare:** segna la quota come opzione popolare.
{% endstep %}

{% step %}
### Vendita periodica

<figure><img src="../../../.gitbook/assets/producto-cuota-venta-periodica.png" alt=""><figcaption></figcaption></figure>

* **Periodicità:** scegli nel menu a tendina ogni quanto si incassa la quota.
* **Ripartisci il primo:** selezionala perché, se ci si iscrive a metà periodo, il primo incasso sia proporzionale.
* **Inscription:** per incassare una quota di iscrizione. Scegli un prodotto di tipo **Article** (crealo prima se non ce l'hai). Consulta [Come creare un prodotto di tipo Article](como-crear-un-producto-tipo-articulo.md).
* **Tipo cliente abbonamento:** quando si iscrive alla quota, il cliente passa automaticamente a questo tipo di cliente.
* **Tipo cliente disdetta abbonamento:** quando la quota termina, il cliente passa automaticamente a questo tipo di cliente.
* **Fatturazione bancaria:** selezionala se la quota si incassa tramite addebito bancario.

> **Abbonamenti:** con i due campi del tipo di cliente, una quota funziona come quella di una palestra. Finché il cliente ce l'ha, diventa del tipo che scegli (per esempio, **Socio**) e gode dei suoi vantaggi, come prezzi speciali. Quando si disiscrive, passa al tipo di disdetta che hai indicato. Consulta [Che cos'è un abbonamento e come funziona](../../../../ventas/ventas/cuotas/que-es-una-membresia-y-como-funciona.md).
{% endstep %}

{% step %}
### Vendite periodiche automatiche

* **Giorni di tolleranza mancato pagamento:** i giorni di attesa, dalla scadenza, prima di annullare la quota per mancato pagamento.
* **Emissione automatica:** selezionala perché le quote si emettano da sole il giorno dopo la scadenza, senza doverlo fare a mano. Consulta [Come automatizzare l'emissione delle quote](../../../../ventas/ventas/cuotas/como-automatizar-la-emision-de-cuotas.md).
* **Annulla per mancato pagamento:** se la quota non viene pagata nei giorni di tolleranza, smette di essere emessa e, se è un abbonamento, il cliente passa al tipo di disdetta. Consulta [Come automatizzare l'annullamento per mancato pagamento](../../../../ventas/ventas/cuotas/como-automatizar-la-cancelacion-por-impago.md).

> Nei menu a tendina compaiono solo cinque opzioni. Se non vedi quella che cerchi, inizia a scriverne il nome.
{% endstep %}

{% step %}
### Salvare

* Clicca su **Salva**.
{% endstep %}
{% endstepper %}

Una volta creata, puoi gestire le quote di ogni cliente. Per sapere come, consulta questo articolo:

<a href="../../../../ventas/ventas/cuotas/como-ver-las-cuotas.md" class="button primary">Come vedere le quote</a>
