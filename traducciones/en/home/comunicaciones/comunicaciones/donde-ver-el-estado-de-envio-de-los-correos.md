---
origen: b5c1c01b5e8c
---
# Where to see the delivery status of emails

Taykus lets you check the status of the emails sent to customers and see whether the system has processed each communication correctly.

Below are the steps to follow:

{% stepper %}
{% step %}
### Go to the sent emails

* Go to the left-hand menu and select **Communications**.
* In the drop-down, choose **Emails**. You'll see the list of emails sent by the system.
{% endstep %}

{% step %}
### Check the status

* Find the email you want to check. You can use the filters in each column, for example **Customer** or **Subject**.
* Look at the **Delivery status** column. These are the statuses you'll see:
  * **Inserted:** the email has been created and is waiting to go out.
  * **Sent:** the email has gone out.
  * **Failed:** the email couldn't be sent. Taykus tries up to three times before marking it as failed; the **Attempts** column shows how many times it has been tried.
  * **Cancelled:** the sending has been cancelled.

> The column filter shows more statuses (**Sending**, **Delivered**, **Read**), but they aren't used.

<figure><img src="../.gitbook/assets/estados-envio-correo.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Important:** the **Sent** status means the email has been processed by Taykus, but it doesn't guarantee that the recipient's email provider has delivered it to their inbox.

If an email hasn't reached the customer, you can send it again. See [How to resend an email](como-reenviar-un-mail.md).
