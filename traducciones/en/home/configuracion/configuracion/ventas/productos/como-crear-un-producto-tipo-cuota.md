---
origen: 2663c13483eb
---
# How to create a Fee product

**Fee** products are charged regularly, such as a monthly fee, a quarterly fee or an annual subscription. Their form sets how often and how they're charged, so the system can manage recurring payments.

Below are the steps to follow:

{% stepper %}
{% step %}
### Go to Products

* Click the <i class="fa-gear" style="color:blue;">:gear:</i> icon in the top right corner and go to **Settings**.
* Click **Sales**. The **Products** tab opens directly.
{% endstep %}

{% step %}
### Create the product

* Click :heavy\_plus\_sign:.
* The product form opens.
{% endstep %}

{% step %}
### General

<figure><img src="../../../.gitbook/assets/producto-cuota-general.png" alt=""><figcaption></figcaption></figure>

* **Logo:** optional. Helps you recognise the product at the POS. You can upload an image with **Browse…** or choose one from the **Gallery**.
* **Name:** a descriptive name for the fee. Required field.
* **Category:** set to **Item** by default. Change it to **Fee**.
* **Gross price:** retail price, including taxes. Required field.
* **Net price:** price without taxes. It's calculated automatically from the tax type.
* **Tax type:** choose from the drop-down the tax that applies to the fee. Required field.
* **Product type:** choose one of the product types you've already created.
* **Loyalty points:** the amount topped up to the customer's wallet voucher for each unit bought, in the smallest unit of your currency (for euros, cents). For example, if you enter 2, the customer gets 2 cents for each unit they buy.
{% endstep %}

{% step %}
### Online sale

* **Detail:** optional text to explain the fee's conditions.
* **Online sale:** tick it if it can be bought online.
* **Trending:** highlights the fee in online sales as a recommended option.
* **Popular:** marks the fee as a popular option.
{% endstep %}

{% step %}
### Recurring sale

<figure><img src="../../../.gitbook/assets/producto-cuota-venta-periodica.png" alt=""><figcaption></figcaption></figure>

* **Frequency:** choose from the drop-down how often the fee is charged.
* **Prorate first:** tick it so that, when someone signs up mid-period, the first charge is proportional.
* **Registration:** to charge an enrolment or registration fee. Choose an **Item**-type product (create it first if you don't have one). See [How to create an Item-type product](como-crear-un-producto-tipo-articulo.md).
* **Membership Customer Type:** when they subscribe to the fee, the customer automatically gets this customer type.
* **Membership Cancellation Customer Type:** when the fee ends, the customer automatically gets this customer type.
* **Bank billing:** tick it if the fee is paid by direct debit.

> **Memberships:** with the two customer type fields, a fee works like a gym membership. While the customer has it, they're the type you choose (for example, **Member**) and enjoy its benefits, such as special prices. When the fee ends, they move to the cancellation type you've set.
{% endstep %}

{% step %}
### Automatic fees

* **Non-payment Grace Days:** number of days to wait after a non-payment before cancelling the membership.
* **Automatic Issue:** tick it so the fees are issued by themselves, without having to do it by hand from the fees calendar.
* **Cancel on Non-payment:** if a non-payment occurs, cancels the fee and what it came from (for example, the registration for an activity or a school group).

> Drop-downs only show five options. If you can't see the one you're looking for, start typing its name.
{% endstep %}

{% step %}
### Save

* Click **Save**.
{% endstep %}
{% endstepper %}

Once it's created, you can manage each player's fees. To find out how, see this article:

<a href="../../../../ventas/ventas/cuotas/como-ver-las-cuotas.md" class="button primary">How to view fees</a>
