---
icon: money-check-dollar-pen
origen: f11565308974
---
# Comment modifier les prix

Les prix des réservations dépendent des tranches configurées dans **Tarifs par calendrier**. Pour changer un prix, vous changez le produit utilisé par cette tranche. Avant de commencer, assurez-vous de modifier le bon calendrier, les bonnes installations et les bonnes tranches.

### Vidéo explicative

{% embed url="https://youtu.be/Ra_LiCtxGUY" %}

> **Avant de commencer :** le nouveau prix doit exister comme produit de type Service. Si vous ne l'avez pas encore créé, consultez :
>
> <a href="../../ventas/productos/como-crear-un-producto-tipo-servicio.md" class="button primary" data-icon="box">Comment créer un produit de type Service</a>

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès à Tarifs par calendrier

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
*   Cliquez sur **réservations**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure></div>
*   Cliquez sur le bloc **Tarifs par calendrier**.<br>

    <figure><img src="../../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Ouvrir le calendrier de prix

* Cherchez le calendrier de prix à modifier et cliquez sur son **ID**.
*   Allez dans le bloc **Tarifs**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure></div>
* Vous verrez la liste des tranches avec leur prix :

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Option 1 : changer le produit d'une tranche

* Élargissez la colonne **Produits** en faisant glisser son bord vers la droite.
*   Cliquez dans l'espace blanc indiqué.<br>

    <figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
*   Cliquez sur la **X** pour retirer le produit actuel.<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure></div>
* Cherchez le produit avec le nouveau prix.  ![](<../../../.gitbook/assets/image (5).png>)
* Sélectionnez-le et appuyez sur **Entrée**. La tranche est mise à jour.
{% endstep %}

{% step %}
### Option 2 : créer une nouvelle tranche

Vous pouvez aussi supprimer les tranches actuelles et en créer de nouvelles.

* Cliquez sur :heavy\_plus\_sign:.
*   La fenêtre **Ajouter une heure** s'ouvre :<br>

    <figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

    * **Ressource :** le terrain ou la ressource précise, si le prix ne concerne qu'un seul.
    * **Groupederessources :** le groupe, si le prix concerne plusieurs installations du même type.
    * **Début :** heure à laquelle le prix commence à s'appliquer.
    * **Fin :** heure à laquelle il cesse de s'appliquer.
    * **End is next day :** cochez-la si la tranche se termine le lendemain.
    * **Appliquer ce prix en cas de chevauchement :** cochez-la si ce prix doit s'appliquer quand deux tranches se chevauchent.
    * **Produit :** le produit qui fixe le prix des réservations sur cette tranche.
* Cliquez sur **Sauvegarder**.
{% endstep %}

{% step %}
### Vérifier les changements

Vérifiez dans la liste des prix que la tranche est correcte. Vérifiez surtout :

* Que la ressource ou le groupe de ressources est le bon.
* Que les heures de début et de fin sont correctes.
* Que le produit est le bon et que son prix est celui que vous voulez facturer.
* Que l'option de chevauchement n'est cochée que si nécessaire.
{% endstep %}
{% endstepper %}
