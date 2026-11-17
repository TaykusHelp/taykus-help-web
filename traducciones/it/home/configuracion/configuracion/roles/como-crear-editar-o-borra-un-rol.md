---
icon: lock
origen: 2a9d48b9d301
---
# Come creare, modificare o eliminare un ruolo

I **ruoli** decidono cosa può vedere e fare ogni dipendente in Taykus. Ogni utente ha un ruolo, e quel ruolo stabilisce i suoi permessi in ogni parte del programma.

### Video esplicativo

{% embed url="https://youtu.be/Vk6PSU2hFQU" %}

## Dove sono i ruoli

* Clicca sull'icona <i class="fa-gear" style="color:blue;">:gear:</i> nell'angolo in alto a destra ed entra in **Impostazioni**.
* Clicca su **Ruoli**.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Vedrai l'elenco dei ruoli e potrai aprire ciascuno per vederne i permessi.

## Ruoli già creati

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

* **Admin Centro:** accesso completo a tutto il programma.
* **Recepción:** accesso completo a prenotazioni, accademia e comunicazioni, e parziale alle impostazioni.
* **Profesor:** accesso parziale a calendario, accademia e clienti.
* **Soporte Taykus:** accesso completo, perché il team di supporto possa aiutarti con dubbi o problemi.

> Se non vuoi che gli insegnanti entrino nel programma come amministratori, puoi dar loro un indirizzo di accesso solo per insegnanti, dove vedranno solo le loro lezioni, i loro alunni e il loro calendario. Per esempio: `https://mariademo.taykusdemo.com/teachers/login`

## Livelli di permesso

Ogni ruolo ha diversi blocchi di permessi. Accanto a ogni permesso puoi attivare o disattivare questi livelli:

![](<../../.gitbook/assets/image (10).png>)

* **Vedere:** l'utente può vedere le informazioni.
* **Modifica:** l'utente può cambiare le informazioni. A seconda del permesso, può anche creare, eliminare o esportare.

## Modificare i permessi di un ruolo

{% stepper %}
{% step %}
### Aprire il ruolo

* Vai su **Impostazioni › Ruoli**.
* Clicca sull'**Id** del ruolo.
{% endstep %}

{% step %}
### Attivare o disattivare i permessi

* Controlla i blocchi di permessi.
* Clicca sul livello che vuoi cambiare:
  * In **verde**, il permesso è attivo.    ![](<../../.gitbook/assets/image (11).png>)
  * In **rosso**, è disattivato.    ![](<../../.gitbook/assets/image (12).png>)
* Le modifiche si salvano da sole; non serve premere Salva.
{% endstep %}
{% endstepper %}

## Creare un nuovo ruolo

{% stepper %}
{% step %}
### Creare il ruolo

* Vai su **Impostazioni › Ruoli**.
* Clicca sull'opzione per creare un nuovo ruolo.
* Scrivi il nome del ruolo e salva.
{% endstep %}

{% step %}
### Configurarne i permessi

* Apri il ruolo dal suo **Id**.
* Attiva o disattiva i permessi come spiegato nella sezione precedente.
{% endstep %}
{% endstepper %}

## Eliminare un ruolo

{% stepper %}
{% step %}
### Verificare che nessuno lo usi

* Prima di eliminare un ruolo, controlla che nessun utente lo abbia assegnato. Altrimenti quel dipendente potrebbe restare senza accesso.
{% endstep %}

{% step %}
### Eliminare il ruolo

* Vai su **Impostazioni › Ruoli**.
* Apri il ruolo dal suo **Id**.
* Usa l'opzione per eliminarlo.
{% endstep %}
{% endstepper %}
