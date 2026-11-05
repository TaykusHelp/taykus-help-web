---
origen: dcea7bf35b5b
---
# What a membership is and how it works

A membership is a fee that, as well as being charged regularly, changes the customer type of whoever has it. It works like a gym membership: while the customer pays it they're a **Member** and enjoy its benefits, such as special prices, and when they leave they go back to being a **Non-member**.

## How to turn a fee into a membership

In the fee's form, in the **Recurring sale** block, fill in these two fields:

<figure><img src="../../.gitbook/assets/cuotas-automaticas-campos.png" alt=""><figcaption></figcaption></figure>

* **Membership Customer Type:** the customer type they'll have while they're on the fee. For example, **Member**.
* **Membership Cancellation Customer Type:** the customer type they'll have when they leave. For example, **Non-member**.

The customer types have to be created first. To find out how, see [How to create different player types](../../../jugadores/jugadores/fichas-de-jugador/como-crear-diferentes-tipos-de-jugadores.md). To give them special prices, see [Customise prices by player type](../../../configuracion/configuracion/ventas/personalizacion-de-precios/personalizar-precios-por-tipo-de-jugador.md).

To find out where these fields are, see [How to create a Fee product](../../../configuracion/configuracion/ventas/productos/como-crear-un-producto-tipo-cuota.md).

## How a customer joins the membership

* **The club adds them:** from **Sales › Fees**, in the fee's **Players** tab, with **+**.
* **The customer signs up online:** if the fee has **Online sale** ticked, they can buy it from the club's Customer Area.

When they join, they automatically get the **Membership Customer Type**.

## When they stop being a member

The customer moves to the **Membership Cancellation Customer Type** in any of these cases:

* When their fee's **End** date arrives.
* When the fee is cancelled for non-payment. See [How to automate cancellation for non-payment](como-automatizar-la-cancelacion-por-impago.md).
* When the club removes them from the fee by changing their **End** date. See [How to remove a customer from a fee](como-dar-de-baja-a-un-cliente-de-una-cuota.md).
