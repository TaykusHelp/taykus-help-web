---
origen: cddafebcf6fb
---

# Comment faire un prélèvement par carte

Depuis **Ventes › Débits directs par carte**, vous pouvez encaisser en une seule fois tout ce qui est en attente de paiement auprès des clients qui ont une carte enregistrée. Cela fonctionne comme une remise Q19, mais le débit se fait sur la carte au lieu du compte bancaire.

> **Important :** il n'est pas nécessaire d'avoir activé le prélèvement automatique par carte sur les cotisations. Il suffit que le client ait une carte enregistrée. Pour savoir comment il l'enregistre, consultez [Comment activer le prélèvement automatique par carte](cuotas/como-activar-el-cobro-automatico-con-tarjeta.md).

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux débits directs par carte

* Allez dans le menu latéral gauche et sélectionnez **Ventes**.
*   Dans le menu déroulant, choisissez **Débits directs par carte**. Vous pouvez y consulter les fichiers déjà créés ou en créer un nouveau.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-listado.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Créer ou ouvrir un fichier

*   Pour créer un nouveau fichier, cliquez sur **+** et remplissez les champs :
    * **Description** : un nom qui identifie le fichier. Il est obligatoire.
    * **Commentaires des clients** : il est facultatif.

    <figure><img src="../.gitbook/assets/domtarjeta-crear-archivo.png" alt=""><figcaption></figcaption></figure>
* Cliquez sur **Sauvegarder**.
* Si vous avez déjà un fichier ouvert pas encore encaissé, cliquez sur son **ID** pour y entrer.
{% endstep %}

{% step %}
### Ajouter les lignes

*   Dans le fichier, dans la section **Lignes de débit direct de la carte**, cliquez sur **+**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-archivo-nuevo.png" alt=""><figcaption></figcaption></figure>
* La fenêtre **Sélectionner les lignes** s'ouvre, avec tout ce qui est en attente de paiement.
* Filtrez par les colonnes dont vous avez besoin et faites défiler la liste pour trouver les lignes à encaisser.
*   Cochez les lignes et cliquez sur **Sélectionner**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-seleccionar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Retirer les clients sans carte

* En revenant au fichier, vous verrez les lignes regroupées par client.
*   Celles des clients qui n'ont pas de carte enregistrée apparaissent en rouge, avec l'avertissement **Le client n'a pas de carte** dans la colonne **Erreur**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-sin-tarjeta.png" alt=""><figcaption></figcaption></figure>
* Cochez ces lignes et supprimez-les avec l'icône de corbeille de **Lignes de débit direct de la carte**.
*   Cliquez sur **OK** pour confirmer.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-eliminar-lineas.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Encaisser le fichier

*   Quand les lignes sont correctes, cliquez sur **Fichier de facturation**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-cobrar-archivo.png" alt=""><figcaption></figcaption></figure>
*   Une fenêtre s'ouvre avec le nombre de clients qui vont être débités et le total. Cliquez sur **OK** pour lancer le débit.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-confirmar-cobro.png" alt=""><figcaption></figcaption></figure>

> **Important :** le débit ne peut pas être annulé. Vérifiez bien les lignes avant de confirmer.
{% endstep %}

{% step %}
### Vérifier le résultat

* Cliquez sur l'icône d'actualisation de **Lignes de débit direct de la carte** pour suivre l'avancement.
*   Dans la colonne **Payé**, vous verrez ce qui a été encaissé. Les lignes qui n'ont pas pu être encaissées restent **(En attente)** et le motif apparaît dans la colonne **Erreur**.<br>

    <figure><img src="../.gitbook/assets/domtarjeta-resultado.png" alt=""><figcaption></figcaption></figure>
* Ce qui n'a pas pu être encaissé reste comme dette en attente de paiement.
{% endstep %}
{% endstepper %}

Vous pouvez aussi consulter les encaissements dans **Ventes › lignes**, dans **Ventes › Paiements** ou dans la fiche du client.
