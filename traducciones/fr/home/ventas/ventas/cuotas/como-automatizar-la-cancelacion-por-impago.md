---
origen: d16af3650c7f
---

# Comment automatiser l'annulation pour impayé

Vous pouvez faire en sorte qu'une cotisation s'annule toute seule quand le client ne la paie pas. Ainsi, les échéances des mois suivants ne lui sont plus émises.

Est considéré comme impayé l'un de ces cas :

* Un prélèvement bancaire que la banque rejette.
* Un prélèvement automatique par carte qui échoue.
* Une cotisation émise que personne ne paie.

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Ouvrir la cotisation

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **Ventes**. L'onglet **Produits** s'ouvre directement.
* Dans la colonne **Catégorie**, sélectionnez **Periodic sale** et cliquez sur l'**ID** de la cotisation.
* Cliquez sur l'icône <i class="fa-pen">:pen:</i> pour la modifier.

> Si la cotisation n'existe pas encore, vous pouvez remplir ces champs en la créant. Consultez [Comment créer un produit de type Cotisation](../../../configuracion/configuracion/ventas/productos/como-crear-un-producto-tipo-cuota.md).
{% endstep %}

{% step %}
### Configurer l'annulation

*   Dans le bloc **Ventes périodiques automatiques**, remplissez ces champs :

    <figure><img src="../../.gitbook/assets/cuotas-cancelar-impago.png" alt=""><figcaption></figcaption></figure>

    * **Jours de grâce impayé :** le nombre de jours d'attente, à partir de l'échéance de la cotisation, avant de l'annuler.
    * **Annuler en cas d'impayé :** cochez-le pour que la cotisation s'annule une fois ces jours passés sans paiement.
* Cliquez sur **Sauvegarder**.
{% endstep %}
{% endstepper %}

## Ce qui se passe lors de l'annulation

Quand les jours de grâce sont passés et que la cotisation n'est toujours pas payée :

* Les cotisations des mois suivants ne sont plus émises.
* La dette existante **n'est pas supprimée** : elle reste émise et en attente de paiement dans [Ventes › Dettes](../deudas/README.md).
* Si la cotisation est une adhésion, le client passe au type de client de résiliation (par exemple, de **Membre** à **Non-membre**). Consultez [Qu'est-ce qu'une adhésion et comment fonctionne-t-elle](que-es-una-membresia-y-como-funciona.md).
* Le client reçoit un e-mail l'informant que son abonnement a été annulé. C'est le modèle **Notification d'abonnement annulé**, que vous pouvez consulter dans [Modèles d'e-mails](../../../comunicaciones/comunicaciones/plantillas-de-emails.md).

> **Important :** annuler la cotisation ne désinscrit pas le client de l'activité ni du groupe de l'académie auquel il est inscrit.
