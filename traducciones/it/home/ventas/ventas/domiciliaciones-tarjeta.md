---
origen: cddafebcf6fb
---

# Come fare un addebito diretto su carta

Da **Vendite › Addebiti diretti su carta** puoi incassare in un colpo solo tutto ciò che è in attesa di pagamento dai clienti che hanno una carta salvata. Funziona come una rimessa del Q19, ma l'addebito avviene sulla carta invece che sul conto bancario.

> **Importante:** non serve avere attivato l'addebito automatico su carta nelle quote. Basta che il cliente abbia una carta salvata. Per sapere come la salva, consulta [Come attivare l'addebito automatico su carta](cuotas/como-activar-el-cobro-automatico-con-tarjeta.md).

Ecco i passaggi da seguire:

{% stepper %}
{% step %}
### Accesso agli addebiti diretti su carta

* Vai al menu laterale a sinistra e seleziona **Vendite**.
*   Nel menu a tendina, scegli **Addebiti diretti su carta**. Da qui puoi consultare i file già creati o crearne uno nuovo.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-listado.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Creare o aprire un file

*   Per creare un nuovo file, clicca su **+** e compila i campi:
    * **Descrizione**: un nome che identifichi il file. È obbligatorio.
    * **Commenti dei clienti**: è facoltativo.

    <figure><img src="../.gitbook/assets/domtarjeta-crear-archivo.png" alt=""><figcaption></figcaption></figure>
* Clicca su **Salva**.
* Se hai già un file aperto che non hai ancora incassato, clicca sul suo **Id** per entrare.
{% endstep %}

{% step %}
### Aggiungere le righe

*   Dentro il file, nella sezione **Linee di addebito diretto della carta**, clicca su **+**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-archivo-nuevo.png" alt=""><figcaption></figcaption></figure>
* Si apre la finestra **Seleziona linee**, con tutto ciò che è in attesa di pagamento.
* Filtra per le colonne che ti servono e scorri l'elenco per trovare le righe che vuoi incassare.
*   Seleziona le righe e clicca su **Selezionare**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-seleccionar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Togliere i clienti senza carta

* Tornando al file, vedrai le righe raggruppate per cliente.
*   Quelle dei clienti che non hanno una carta salvata compaiono in rosso, con l'avviso **Il cliente non ha una carta** nella colonna **Errore**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-sin-tarjeta.png" alt=""><figcaption></figcaption></figure>
* Seleziona quelle righe ed eliminale con l'icona del cestino di **Linee di addebito diretto della carta**.
*   Clicca su **OK** per confermare.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-eliminar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Incassare il file

*   Quando le righe sono corrette, clicca su **File di addebito**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-cobrar-archivo.png" alt=""><figcaption></figcaption></figure>
*   Si apre una finestra con il numero di clienti a cui verrà addebitato e il totale. Clicca su **OK** per avviare l'addebito.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-confirmar-cobro.png" alt=""><figcaption></figcaption></figure>

> **Importante:** l'addebito non si può annullare. Controlla bene le righe prima di confermare.
{% endstep %}

{% step %}
### Controllare il risultato

* Clicca sull'icona di aggiornamento di **Linee di addebito diretto della carta** per vedere l'avanzamento.
*   Nella colonna **Pagato** vedrai ciò che è stato incassato. Le righe che non è stato possibile incassare restano **(In attesa di)** e nella colonna **Errore** compare il motivo.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-resultado.png" alt=""><figcaption></figcaption></figure>
* Ciò che non è stato possibile incassare resta come debito in attesa di pagamento.
{% endstep %}
{% endstepper %}

Puoi consultare gli incassi anche in **Vendite › linee**, in **Vendite › Pagamenti** o nella scheda del cliente.
