---
origen: e2ddd803a16d
---

# Où voir l'état d'envoi des e-mails

Taykus permet de consulter l'état des e-mails envoyés aux clients et de vérifier si le système a bien traité chaque communication.

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux e-mails envoyés

* Allez dans le menu latéral gauche et sélectionnez **Communications**.
*   Dans le menu déroulant, choisissez **Emails**. Vous verrez la liste des e-mails envoyés par le système.

    <figure><img src="../.gitbook/assets/reenviar-acceso-emails.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Consulter l'état

* Trouvez l'e-mail à vérifier. Vous pouvez utiliser les filtres de chaque colonne, par exemple **Acheteur** ou **Sujet**.
* Regardez la colonne **Statut d'envoi**. Voici les états que vous verrez :
  * **Inséré :** l'e-mail a été créé et attend de partir.
  * **Envoyé :** l'e-mail est parti.
  * **Échoué :** l'e-mail n'a pas pu être envoyé. Taykus essaie jusqu'à trois fois avant de le marquer comme échoué ; la colonne **Tentatives** indique combien de fois il a essayé.
  * **Annulé :** l'envoi a été annulé.

> D'autres états apparaissent dans le filtre de la colonne (**En cours d'envoi**, **Livré**, **Lu**), mais ils ne sont pas utilisés.

<figure><img src="../.gitbook/assets/estados-envio-correo.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Important :** l'état **Envoyé** indique que l'e-mail a été traité par Taykus, mais ne garantit pas que le fournisseur de messagerie du destinataire l'a remis dans sa boîte de réception.

Si un e-mail n'est pas arrivé au client, vous pouvez le renvoyer. Consultez [Comment renvoyer un e-mail](como-reenviar-un-mail.md).
