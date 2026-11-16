---
origen: 5e561d3fee2c
---

# Comment activer le prélèvement automatique par carte

Si un client a une carte enregistrée, vous pouvez activer le prélèvement automatique sur sa cotisation : à la date d'échéance, la cotisation est débitée automatiquement sur cette carte. Vous pouvez l'activer en ajoutant le client à la cotisation ou plus tard, depuis la liste des clients de la cotisation.

> **Important :** le prélèvement automatique ne peut être activé que si le client a une carte enregistrée. Si un prélèvement automatique échoue, la cotisation reste comme dette en attente de paiement dans [Ventes › Dettes](../deudas/README.md).

### Avant de commencer : comment le client enregistre sa carte

Le client peut enregistrer sa carte depuis son espace client de deux façons :

*   **En payant une cotisation en ligne.** Si la cotisation est en attente de paiement, elle apparaît dans **Mon Compte › Ventes en attente** pour qu'il la paie. S'il y souscrit en ligne, elle est ajoutée au panier. Dans les deux cas, en payant par carte, le système l'oblige à l'enregistrer.<br>

    <figure><img src="../../.gitbook/assets/cuotas-tarjeta-ventas-pendientes.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/cuotas-tarjeta-guardar.png" alt=""><figcaption></figcaption></figure>
*   **Depuis son profil, sans rien payer.** Dans **Mon Compte › Mon profil › Méthodes de paiement**, avec le bouton **Ajouter une carte de crédit**. Rien ne lui est débité à ce moment-là.<br>

    <figure><img src="../../.gitbook/assets/cuotas-tarjeta-mi-perfil.png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/cuotas-tarjeta-anadir-tarjeta.png" alt=""><figcaption></figcaption></figure>

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès à la cotisation

* Allez dans le menu latéral gauche et sélectionnez **Ventes**.
* Dans le menu déroulant, choisissez **ventes périodiques**.
* Cliquez sur l'**ID** de la cotisation.
* Ouvrez l'onglet **Clients**.
{% endstep %}

{% step %}
### L'activer en ajoutant un client

* Cliquez sur **+** pour ajouter un client à la cotisation.
* Remplissez les données : **Acheteur**, **Début**, **Fin**, **Jour d'échéance** et **Description**.
*   Cochez la case **Prélèvement automatique par carte**.<br>

    <figure><img src="../../.gitbook/assets/cuotas-cobro-tarjeta-anadir.png" alt=""><figcaption></figcaption></figure>
* Cliquez sur **Sauvegarder**.
*   Si le client n'a aucune carte enregistrée, un avertissement en rouge apparaît et vous ne pouvez pas activer le prélèvement automatique :<br>

    <figure><img src="../../.gitbook/assets/cuotas-cobro-tarjeta-sin-tarjeta.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### L'activer pour un client déjà inscrit à la cotisation

*   Dans la liste des clients de la cotisation, la colonne **Card** indique si le client a une carte enregistrée et la colonne **Prélèvement automatique par carte** s'il a le prélèvement automatique activé.<br>

    <figure><img src="../../.gitbook/assets/cuotas-cobro-tarjeta-listado.png" alt=""><figcaption></figcaption></figure>
*   Si le client a une carte, cliquez sur sa cellule dans la colonne **Prélèvement automatique par carte** et cochez la case. L'enregistrement est automatique.<br>

    <figure><img src="../../.gitbook/assets/cuotas-cobro-tarjeta-activar.png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
