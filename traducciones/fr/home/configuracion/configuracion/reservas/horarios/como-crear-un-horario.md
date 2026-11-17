---
icon: clock-three
origen: c76a56afd4b8
---
# Comment créer un horaire

Les terrains et les professeurs n'apparaissent dans le calendrier que lorsqu'ils ont un horaire. L'horaire indique quels jours et à quelles heures chaque ressource est ouverte, et comment elle peut être réservée.

Taykus fournit deux horaires déjà créés. Vous pouvez les modifier ou les supprimer et en créer un nouveau. Dans cet article, nous vous expliquons comment en créer un de zéro.

### Vidéo explicative

{% embed url="https://youtu.be/0UDRdOUjr54" %}

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux horaires

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
*   Cliquez sur **réservations**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure></div>
*   Cliquez sur le bloc **Horaires**.<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
### Créer l'horaire

* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :<br>

    <div align="left"><figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure></div>

    * **Nom :** un nom selon les jours inclus (par exemple, _Semaine_ ou _Week-end_).
    * **Priorité :** lequel l'emporte si deux horaires se chevauchent : c'est le **nombre le plus élevé** qui gagne. En général, on donne plus de priorité au week-end qu'à la semaine : ainsi, si vous voulez qu'un jour férié en semaine fonctionne comme un samedi, ce jour-là utilisera l'horaire du week-end.
    * **Début/Fin :** dates de début et de fin d'application de l'horaire. Si vous les laissez vides, il s'applique dès son enregistrement.
    * **Jour de la semaine :** cochez les jours inclus dans cet horaire.
* Cliquez sur **Sauvegarder**.
{% endstep %}

{% step %}
### Ouvrir les heures d'ouverture

* À l'enregistrement, l'horaire s'ouvre sur l'onglet **Dates**.
*   Cliquez sur l'onglet **Heures d'ouverture**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure></div>

Vous allez y configurer deux choses :

* **Ouverture et fermeture :** quelles installations (padel, tennis, football…) suivent cet horaire et à quelle heure elles ouvrent et ferment.
* **Intervalles et durée des réservations en ligne :** à quelle fréquence les clients peuvent réserver en ligne (toutes les 30, 60 ou 90 minutes) et la durée minimale et maximale des réservations.

> **Important :**
>
> * Si le club a une école, ajoutez aussi les **professeurs** à l'horaire.
> * Vous pouvez créer autant d'horaires que nécessaire. Si toutes les installations ouvrent à la même heure, mettez-les dans un seul horaire ; si chacune a le sien, créez-en un pour chacune.
{% endstep %}

{% step %}
### Ajouter les heures d'ouverture

* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :<br>

    <figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

    * **Ressource :** tous les terrains ou professeurs auxquels s'applique cet horaire.
    * **Début :** heure d'ouverture.
    * **Fin :** heure de fermeture.
    * **End is next day :** cochez-la si l'horaire se termine à 00:00 ou plus tard.
    * **Intervalles en minutes :** tous les combien de minutes le calendrier est découpé. Par exemple, avec 30 minutes, vous verrez des tranches à 09:00, 09:30, 10:00, 10:30…
    * **Durée minimale :** la durée minimale d'une réservation. Elle ne peut pas être inférieure à l'intervalle et doit en être un multiple.
    * **Durée maximale :** la durée maximale d'une réservation. Elle doit être un multiple de l'intervalle.
* Cliquez sur **Sauvegarder**.
{% endstep %}
{% endstepper %}

## Si quelque chose ne fonctionne pas

* **Le terrain n'apparaît pas dans le calendrier :** vérifiez qu'il a bien été ajouté dans **Heures d'ouverture** (étape 4). Créer l'horaire sans ajouter le terrain ne suffit pas.
* **J'ai élargi l'horaire et je ne peux pas réserver sur les nouvelles heures :** élargissez aussi la tranche dans les tarifs par calendrier. L'horaire et les prix doivent couvrir les mêmes heures. Pour cela, consultez cet article :

  <a href="../precios-por-calendario/como-poner-precios-al-horario.md" class="button primary">Comment mettre des prix sur l'horaire</a>
* **Je ne peux pas enregistrer la durée :** les durées minimale et maximale doivent être des multiples de l'intervalle. Avec un intervalle de 30 minutes, vous pouvez mettre 60 ou 90, mais pas 45.
