---
icon: circle-user-clock
origen: 62c01ad14b11
---
# Comment attribuer un professeur à un horaire

Pour qu'un professeur puisse être réservé, il doit figurer dans un horaire, comme les terrains. Avant de l'attribuer, le professeur doit être créé comme ressource. Si ce n'est pas encore fait, consultez d'abord cet article :

<a href="../grupo-de-recursos/como-anadir-a-un-profesor-nuevo.md" class="button primary">Comment ajouter un nouveau professeur</a>

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux horaires

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
*   Cliquez sur **réservations**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure></div>
*   Cliquez sur le bloc **Horaires**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Ouvrir l'horaire

*   Cliquez sur l'**ID** de l'horaire.<br>

    <figure><img src="../../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
*   Ouvrez l'onglet **Heures d'ouverture**.<br>

    <figure><img src="../../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Ajouter le professeur

* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :<br>

    <figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

    * **Ressource :** cherchez et ajoutez le professeur.
    * **Début :** heure à laquelle le professeur commence à travailler.
    * **Fin :** heure à laquelle il termine.
    * **End is next day :** cochez-la si l'horaire se termine à 00:00 ou plus tard.
    * **Intervalles en minutes :** tous les combien de minutes le calendrier est découpé. Par exemple, avec 30 minutes, vous verrez des tranches à 09:00, 09:30, 10:00, 10:30…
    * **Durée minimale :** la durée minimale d'une réservation avec le professeur. Elle ne peut pas être inférieure à l'intervalle et doit en être un multiple.
    * **Durée maximale :** la durée maximale d'une réservation avec le professeur. Elle doit être un multiple de l'intervalle.
* Cliquez sur **Sauvegarder**.
{% endstep %}

{% step %}
### Vérifier que cela fonctionne

Il y a deux façons de vérifier que le professeur est bien attribué :

**Option 1 : en faisant une réservation**

*   Dans le calendrier, créez une réservation où vous devez choisir un professeur.

    <figure><img src="../../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>
*   Vérifiez que le professeur apparaît dans la liste et que vous pouvez le sélectionner.

    <figure><img src="../../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
* Essayez de terminer la réservation. Si le système vous le permet, le professeur est bien configuré.\
  ![](<../../../.gitbook/assets/image (22).png>)

**Option 2 : dans la vue des professeurs**

*   Dans le calendrier, cliquez sur l'onglet **Teachers**.<br>

    <figure><img src="../../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
*   Vérifiez que le professeur apparaît dans la grille.

    <figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}
