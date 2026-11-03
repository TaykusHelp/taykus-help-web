---
origen: 0579304bd989
---
# How to issue an invoice from Sales > Payments

From **Sales › Payments** you can issue the invoice for a sale from its payment. It works the same as from **Sales › Lines**, but in this list you click the number in the **Sale** column.

> **Important:** before issuing the invoice, check that you have created your company details in **Settings › Sales › Companies** and, if you invoice companies, their details in **Settings › Sales › Customer companies**. To find out how, see these articles:

<a href="https://app.gitbook.com/s/V0h7jTfpeuZY1RmPEtNK/configuracion/ventas/empresas/como-configurar-los-datos-de-empresa" class="button primary">How to set up your company details</a>

<a href="https://app.gitbook.com/s/V0h7jTfpeuZY1RmPEtNK/configuracion/ventas/empresas-clientes/como-crear-empresas-cliente-en-el-sistema" class="button primary">How to create customer companies in the system</a>

Below are the steps to follow:

{% stepper %}
{% step %}
### Go to Payments

* Go to the left-hand menu and select **Sales**.
* In the drop-down, choose **Payments**.
*   Find the payment for the sale you want to invoice. You can use the filters in each column.<br>

    <figure><img src="../../.gitbook/assets/pagos-listado.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Open the sale

* Click the number in the **Sale** column (not the **ID**).
*   In the sale, click **Issue invoice**.<br>

    <figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
* A window with the billing details opens.
{% endstep %}

{% step %}
### Invoice details

In the **Issuer** block:

* Select the **issuing company** in the **Company** field.
* The system automatically fills in the linked details, such as:
  * Name
  * Tax ID (CIF)
  * Email
  * Phone

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

In the **Customer** block, you can choose between two options:

**Individual**

If the invoice is for a private individual:

* Leave the **Individual** option ticked.
* Check or fill in the customer's details:
  * Full name
  * ID number (DNI)
  * Email
  * Phone
  * Address

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

**Company**

If the invoice is for a company:

* Tick the **Company** option.
* In the **Customer company** field, select the company.
* The system automatically fills in that company's tax details.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>


{% endstep %}

{% step %}
### Save

* Check the details and click the save icon.
* The invoice for that sale is generated and sent automatically to the customer.
{% endstep %}
{% endstepper %}

> **Important:** in **Sales › Voucher Payments** it works exactly the same way: click the number in the **Sale** column and follow the same steps.

If you need to send it again or download it, see [How to resend or download an invoice](como-reenviar-o-descargar-una-factura.md).
