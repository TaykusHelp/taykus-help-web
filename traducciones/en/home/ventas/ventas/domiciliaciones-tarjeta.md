---
origen: cddafebcf6fb
---
# How to run a card direct debit

From **Sales › Card Direct Debits** you can collect, in one go, everything pending payment from customers who have a saved card. It works like a Q19 remittance, but the payment is taken from the card instead of the bank account.

> **Important:** automatic card payment doesn't need to be turned on in the fees. It's enough for the customer to have a saved card. To see how customers save it, see [How to turn on automatic card payment](cuotas/como-activar-el-cobro-automatico-con-tarjeta.md).

Below are the steps to follow:

{% stepper %}
{% step %}
### Go to Card Direct Debits

* Go to the left-hand menu and select **Sales**.
*   In the drop-down, choose **Card Direct Debits**. From here you can view the files already created or create a new one.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-listado.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Create or open a file

*   To create a new file, click **+** and fill in the fields:
    * **Description**: a name that identifies the file. It's required.
    * **Comments**: optional.

    <figure><img src="../.gitbook/assets/domtarjeta-crear-archivo.png" alt=""><figcaption></figcaption></figure>
* Click **Save**.
* If you already have an open file that hasn't been collected yet, click its **ID** to open it.
{% endstep %}

{% step %}
### Add the lines

*   Inside the file, in the **Direct Debit Lines** section, click **+**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-archivo-nuevo.png" alt=""><figcaption></figcaption></figure>
* The **Select Lines** window opens, with everything pending payment.
* Filter by the columns you need and scroll through the list to find the lines you want to collect.
*   Tick the lines and click **Select**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-seleccionar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Remove customers without a card

* Back in the file, you'll see the lines grouped by player.
*   Lines for customers who don't have a saved card appear in red, with the message **The customer has no card** in the **Error** column.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-sin-tarjeta.png" alt=""><figcaption></figcaption></figure>
* Tick those lines and delete them with the bin icon in **Direct Debit Lines**.
*   Click **OK** to confirm.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-eliminar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Collect the file

*   When the lines are correct, click **Collect File**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-cobrar-archivo.png" alt=""><figcaption></figcaption></figure>
*   A window opens with the number of customers who will be charged and the total. Click **OK** to start the collection.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-confirmar-cobro.png" alt=""><figcaption></figcaption></figure>

> **Important:** the collection can't be undone. Check the lines carefully before confirming.
{% endstep %}

{% step %}
### Check the result

* Click the refresh icon in **Direct Debit Lines** to see how the process is going.
*   The **Paid** column shows what has been collected. Lines that couldn't be collected stay as **(Pending)** and the reason appears in the **Error** column.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-resultado.png" alt=""><figcaption></figcaption></figure>
* Anything that couldn't be collected stays as a debt pending payment.
{% endstep %}
{% endstepper %}

You can also check the payments in **Sales › Lines**, in **Sales › Payments** or in the player's profile.
