---
icon: circle-info
origen: b97623bce639
---
# What changes when a player has a responsible customer

When you assign a responsible customer to a player, the associated profile can use the responsible customer's email, phone and payment methods. Here's what changes in each case and how to remove the link.

## Email and phone

If the associated profile has the **Email** or **Phone No.** fields empty, they are filled in with the responsible customer's details when you save.

Since an email can't be repeated in two profiles, the system automatically adds a **+** and a number before the @. For example, if the responsible customer's email is `unoperez@yopmail.com`, the associated profile's becomes `unoperez+239@yopmail.com`. It's a working email: everything sent to the associated profile reaches the responsible customer's inbox.

<figure><img src="../../.gitbook/assets/cliente-responsable-correo-generado.png" alt=""><figcaption></figcaption></figure>

> **Important:** if the associated profile already has its own email or phone, they are not changed, and anything sent to that profile still reaches its own email.

## Payments at the POS

When you charge a sale for the associated profile at the **POS**, the responsible customer's saved card and **Wallet Voucher** appear as payment methods. If you hover over either of them, you'll see the owner's name.

<figure><img src="../../.gitbook/assets/tpv-cobro-cliente-responsable.png" alt=""><figcaption></figcaption></figure>

## Customer Area

The responsible customer can log in to the Customer Area with their username and password and switch to their associates' accounts, for example, to pay with their voucher or saved card. To learn how, see this article:

<a href="../../../zona-de-clientes/zona-de-clientes/como-cambiar-entre-tu-cuenta-y-la-de-tus-asociados-en-la-zona-de-clientes.md" class="button primary">How to switch between your account and your associates' in the Customer Area</a>

The associated person can only log in on their own if they have their own email. If not, they have to log in with the responsible customer's account.

## Removing the link

To remove the link, edit the associated profile, clear the **Responsible Customer** field and click **Save**.

> **Important:** when you remove the link, the generated email (with the **+** and the number) stays in the profile and the system doesn't warn you. If you want messages sent to that profile to stop reaching the former responsible customer, change the email to the person's own.

To assign a responsible customer to a player, see this article:

<a href="como-asignar-un-cliente-responsable-a-un-jugador.md" class="button primary">How to assign a responsible customer to a player</a>
