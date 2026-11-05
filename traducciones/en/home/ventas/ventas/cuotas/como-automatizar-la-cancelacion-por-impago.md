---
origen: eaf969b4aab0
---
# How to automate cancellation for non-payment

You can make a fee cancel itself when the customer doesn't pay it. That way they don't keep getting charges for the following months.

Any of these counts as non-payment:

* A direct debit receipt returned by the bank.
* An automatic card payment that fails.
* An issued fee that nobody pays.

Below are the steps to follow:

{% stepper %}
{% step %}
### Open the fee

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
* Click **Sales**. The **Products** tab opens directly.
* In the **Category** column, select **Fee** and click the fee's **Id**.
* Click the <i class="fa-pen">:pen:</i> icon to edit it.

> If the fee doesn't exist yet, you can fill in these fields when you create it. See [How to create a Fee product](../../../configuracion/configuracion/ventas/productos/como-crear-un-producto-tipo-cuota.md).
{% endstep %}

{% step %}
### Set up the cancellation

*   In the **Automatic Fees** block, fill in these fields:

    <figure><img src="../../.gitbook/assets/cuotas-automaticas-campos.png" alt=""><figcaption></figcaption></figure>

    * **Non-payment Grace Days:** the days to wait, from the fee's due date, before cancelling it.
    * **Cancel on Non-payment:** tick it so the fee is cancelled when those days pass without payment.
* Click **Save**.
{% endstep %}
{% endstepper %}

## What happens when it's cancelled

When the grace days have passed and the fee is still unpaid:

* The fees for the following months stop being issued.
* The debt they already had **isn't deleted**: it stays issued and pending payment in [Sales › Debts](../deudas/README.md).
* If the fee is a membership, the customer moves to the cancellation customer type (for example, from **Member** to **Non-member**). See [What a membership is and how it works](que-es-una-membresia-y-como-funciona.md).
* The customer receives an email telling them their subscription has been cancelled. It's the **Subscription cancelled notification** template, which you can check in [Email templates](../../../comunicaciones/comunicaciones/plantillas-de-emails.md).

> **Important:** cancelling the fee doesn't remove them from the activity or academy group they're enrolled in.
