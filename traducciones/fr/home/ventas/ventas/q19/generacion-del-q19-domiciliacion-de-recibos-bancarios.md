---
icon: money-bill-transfer
origen: fdf667ab9773
---
# Génération du Q19 (prélèvement des échéances bancaires)

Dans cet article, nous voyons comment créer un fichier **Q19** pour gérer les remises de cotisations, comment ajouter les lignes correspondantes et quelles vérifications faire avant de le fermer et de le télécharger.

Voici une vidéo explicative avec toutes les étapes :

### Vidéo explicative

{% embed url="https://youtu.be/IA2_rz0yjHM" %}

Dans cet article, nous détaillons comment faire :

### Avant de commencer

Avant de générer un Q19, vérifiez que ces données sont créées dans :

* **Paramètres > Ventes > Entreprises**

Pour savoir comment faire, consultez cet article :

<a href="antes-de-empezar-a-remesar.md" class="button primary">Avant de commencer les remises</a>

{% stepper %}
{% step %}
### Accès à la section Q19

* Allez dans le menu de gauche et sélectionnez **Ventes.**
* Cliquez sur **Q19**.
*   Depuis cette section, vous pouvez consulter les remises déjà créées ou en générer une nouvelle.<br>

    <figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Créer un nouveau fichier Q19

Une fois dans **Q19**, cliquez sur le bouton **ajouter** pour créer un nouveau fichier.

Remplissez ensuite les champs principaux :

* **Description** : saisissez un nom qui identifie la remise.\
  Exemple : **REMISE COTISATIONS MEMBRES AVRIL 2026**
* **ID d'émetteur** : sélectionnez l'émetteur correspondant.
*   **Commentaires des clients** : ce champ est facultatif.<br>

    <figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

Une fois les informations remplies, cliquez sur **Sauvegarder**.
{% endstep %}

{% step %}
### Ajouter les lignes au Q19

*   Une fois le fichier enregistré, ouvrez la section **Lignes Q19** et cliquez sur le bouton **+** pour ajouter les lignes à inclure dans la remise.<br>

    <figure><img src="../../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>
*   Une fenêtre s'ouvre avec les **Articles de vente**, à partir de laquelle vous pouvez facilement trouver les cotisations à inclure dans le fichier.<br>

    <figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Bien filtrer les lignes

Pour ne trouver que les lignes qui doivent faire partie de la remise, il est important d'appliquer les bons filtres.

* #### État du ticket
  * Filtrez par **En attente**, pour n'afficher que les lignes pas encore traitées.
* #### Due date
  * Utilisez ce filtre pour trouver les cotisations de la période à remettre.
* #### Type de produit
  * Filtrez par **Cotisations Membres**, pour que n'apparaissent que les lignes de cotisations de membres et pas d'autres produits ou réservations.

Une fois les filtres appliqués, cochez les lignes à inclure et cliquez sur **Sélectionner**.
{% endstep %}

{% step %}
### Vérifier s'il y a des erreurs

En sélectionnant les lignes, un avertissement **Erreur** peut apparaître. Si c'est le cas, cliquez sur **OK** et vérifiez les erreurs comme expliqué ci-dessous.

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

*   Dans le même fichier Q19, vous trouverez aussi l'onglet **Erreurs**.<br>

    <figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>
* Depuis cet onglet, vous pouvez repérer les problèmes avant de fermer la remise. Si une ligne ne doit pas être incluse ou présente un problème, vérifiez-la avant de continuer et sélectionnez écarter.
* Vous pouvez aussi supprimer des lignes ajoutées depuis le Q19 si vous devez corriger la sélection.
{% endstep %}

{% step %}
### Vérifier les lignes ajoutées

*   En revenant au fichier Q19, vous verrez les lignes incluses dans la section **lignes**.<br>

    <figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
* Vous pouvez y vérifier des informations comme :
  * **Client**
  * **Nom du titulaire du compte**
  * **Concept**
  * **Montant**
* Il est important de vérifier que les lignes incluses sont correctes avant de continuer.
{% endstep %}

{% step %}
### Fermer le fichier Q19

* Quand vous avez vérifié que toutes les lignes sont correctes, cliquez sur fermer.
* Le logiciel affiche un avertissement avec le montant total et le nombre de paiements.\
  ![](<../../.gitbook/assets/image (19).png>)
* Cliquez sur **OK.**
* Le fichier passe alors à l'état **Fermé.**
* Cette étape est indispensable pour que le fichier soit correctement préparé.
{% endstep %}

{% step %}
### Télécharger le fichier

*   Quand l'état du Q19 est **Fermé**, vous pouvez utiliser l'option **Télécharger** pour obtenir le fichier généré.<br>

    <figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
* C'est ce fichier que vous pourrez utiliser pour gérer la remise et envoyer à la banque.
{% endstep %}
{% endstepper %}

Avant de fermer et télécharger le fichier, pensez à vérifier que les lignes incluses correspondent à la bonne période, qu'elles appartiennent au type de produit **Cotisations Membres** et qu'il n'y a aucun problème dans l'onglet des erreurs.

Vous pourrez ainsi générer correctement le fichier Q19 avec les lignes à inclure dans la remise.
