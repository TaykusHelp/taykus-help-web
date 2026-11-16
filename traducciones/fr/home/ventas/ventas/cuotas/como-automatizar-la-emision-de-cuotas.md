---
origen: cfbd15adbd85
---

# Comment automatiser l'émission des cotisations

Si vous activez l'émission automatique sur une cotisation, vous n'avez plus besoin de l'émettre à la main chaque mois depuis le calendrier des cotisations : le logiciel l'émet tout seul.

> **Important :** la cotisation est émise automatiquement **le lendemain de son échéance, à 00:00**. Par exemple, si elle arrive à échéance le 1er, elle est émise le 2 à 00:00.

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
### Activer l'émission automatique

*   Dans le bloc **Ventes périodiques automatiques**, cochez **Émission automatique**.

    <figure><img src="../../.gitbook/assets/cuotas-emision-automatica.png" alt=""><figcaption></figcaption></figure>
* Cliquez sur **Sauvegarder**.
{% endstep %}
{% endstepper %}

Une fois émise, la cotisation est en attente de paiement et le client la voit dans son espace client. Pour l'encaisser aussi automatiquement, consultez [Comment activer le prélèvement automatique par carte](como-activar-el-cobro-automatico-con-tarjeta.md).
