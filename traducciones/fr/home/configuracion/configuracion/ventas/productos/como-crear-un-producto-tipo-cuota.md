---
origen: d81b4ae3af17
---

# Comment créer un produit de type Cotisation

Les produits de type **Periodic sale** (cotisation) sont ceux qui s'encaissent périodiquement, comme une mensualité, une cotisation trimestrielle ou un abonnement annuel. Leur fiche définit à quelle fréquence et comment ils s'encaissent, pour que le système gère les encaissements récurrents.

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux produits

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **Ventes**. L'onglet **Produits** s'ouvre directement.
{% endstep %}

{% step %}
### Créer le produit

* Cliquez sur :heavy\_plus\_sign:.
* La fiche du produit s'ouvre.
{% endstep %}

{% step %}
### Général

<figure><img src="../../../.gitbook/assets/producto-cuota-general.png" alt=""><figcaption></figcaption></figure>

* **Logo :** facultatif. Aide à reconnaître le produit au point de vente. Vous pouvez téléverser une image avec **Parcourir** ou en choisir une dans la **Galerie**.
* **Nom :** nom descriptif de la cotisation. Champ obligatoire.
* **Catégorie :** elle est réglée sur **Article** par défaut. Changez-la en **Periodic sale**.
* **Prix brut :** prix de vente au public, taxes comprises. Champ obligatoire.
* **Prix net :** prix hors taxes. Il est calculé automatiquement selon le type de taxe.
* **Type de taxe :** choisissez dans le menu déroulant la taxe qui s'applique à la cotisation. Champ obligatoire.
* **Type de produit :** choisissez l'un des types de produits déjà créés.
* **Points de fidélité :** montant rechargé sur le bon monétaire du client pour chaque unité achetée, dans la plus petite unité de votre monnaie (en euros, les centimes). Par exemple, si vous écrivez 2, le client reçoit 2 centimes pour chaque unité achetée.
{% endstep %}

{% step %}
### Vente en ligne

* **Détail :** texte facultatif pour expliquer les conditions de la cotisation.
* **Vente en ligne :** cochez-la si elle peut être achetée en ligne.
* **Tendance :** met en avant la cotisation dans la vente en ligne comme option recommandée.
* **Populaire :** marque la cotisation comme option populaire.
{% endstep %}

{% step %}
### Vente périodique

<figure><img src="../../../.gitbook/assets/producto-cuota-venta-periodica.png" alt=""><figcaption></figcaption></figure>

* **Périodicité :** choisissez dans le menu déroulant à quelle fréquence la cotisation est encaissée.
* **Proratiser le premier :** cochez-la pour que, en cas d'inscription en milieu de période, le premier encaissement soit proportionnel.
* **Inscription :** pour encaisser des frais d'inscription. Choisissez un produit de type **Article** (créez-le avant si vous ne l'avez pas). Consultez [Comment créer un produit de type Article](como-crear-un-producto-tipo-articulo.md).
* **Type de client adhésion :** en souscrivant à la cotisation, le client passe automatiquement à ce type de client.
* **Type de client fin d'adhésion :** à la fin de la cotisation, le client passe automatiquement à ce type de client.
* **Facturation bancaire :** cochez-la si la cotisation est encaissée par prélèvement bancaire.

> **Adhésions :** avec les deux champs de type de client, une cotisation fonctionne comme l'abonnement d'une salle de sport. Tant que le client l'a, il passe au type que vous choisissez (par exemple, **Membre**) et profite de ses avantages, comme des prix spéciaux. Quand il se désinscrit, il passe au type de résiliation indiqué. Consultez [Qu'est-ce qu'une adhésion et comment fonctionne-t-elle](../../../../ventas/ventas/cuotas/que-es-una-membresia-y-como-funciona.md).
{% endstep %}

{% step %}
### Ventes périodiques automatiques

* **Jours de grâce impayé :** nombre de jours d'attente, à partir de l'échéance, avant d'annuler la cotisation pour impayé.
* **Émission automatique :** cochez-la pour que les cotisations s'émettent toutes seules le lendemain de leur échéance, sans avoir à le faire à la main. Consultez [Comment automatiser l'émission des cotisations](../../../../ventas/ventas/cuotas/como-automatizar-la-emision-de-cuotas.md).
* **Annuler en cas d'impayé :** si la cotisation n'est pas payée pendant les jours de grâce, elle n'est plus émise et, s'il s'agit d'une adhésion, le client passe au type de résiliation. Consultez [Comment automatiser l'annulation pour impayé](../../../../ventas/ventas/cuotas/como-automatizar-la-cancelacion-por-impago.md).

> Les menus déroulants n'affichent que cinq options. Si vous ne voyez pas celle que vous cherchez, commencez à taper son nom.
{% endstep %}

{% step %}
### Enregistrer

* Cliquez sur **Sauvegarder**.
{% endstep %}
{% endstepper %}

Une fois créée, vous pouvez gérer les cotisations de chaque client. Pour savoir comment, consultez cet article :

<a href="../../../../ventas/ventas/cuotas/como-ver-las-cuotas.md" class="button primary">Comment voir les cotisations</a>
