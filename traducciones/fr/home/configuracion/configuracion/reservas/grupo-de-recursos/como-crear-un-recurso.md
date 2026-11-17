---
icon: tennis-ball
origen: 0e5d3f307582
---
# Comment créer une ressource

Une **ressource** est tout ce qui peut être réservé ou attribué à une activité : un terrain ou un professeur. Les ressources sont regroupées par sport (padel, tennis, football…) et, grâce à elles, le système sait ce qui est disponible et à quels horaires, pour organiser les réservations sans chevauchements.

En général, les installations du club sont déjà créées lors de la configuration initiale. Si vous devez en ajouter une nouvelle, suivez ces étapes.

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès à Groupe de ressources

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **réservations**. Le bloc **Groupe de ressources** s'ouvre directement.
{% endstep %}

{% step %}
### Créer le sport (groupe de ressources)

Si le sport existe déjà, passez directement à l'étape 4.

* Cliquez sur <i class="fa-plus-large">:plus-large:</i> pour créer un nouveau sport ou non-sport.
* Cette fenêtre s'ouvre. Dans l'exemple, nous créons le tennis :

<figure><img src="../../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

Voici les champs obligatoires :

* **Nom :** le nom du sport.
*   **Commande :** la position à laquelle il apparaîtra dans le calendrier.

    <figure><img src="../../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>
* **Sport :** le sport. Si vous créez des professeurs, choisissez **Pas de sport**.
* **Catégorie :** le type de ressource.
* **Intervalles en minutes :** tous les combien de minutes le calendrier est découpé.
* **Durée minimale :** la durée minimale d'une réservation.
* **Durée maximale :** la durée maximale d'une réservation.
{% endstep %}

{% step %}
### Champs facultatifs du sport

* **Modifie le niveau :** cochez-la si les résultats de ce sport font monter ou descendre le niveau du joueur.
* **Hauteur de cellule du calendrier :** la hauteur des cases du calendrier. Par défaut, 35. Pour voir 4 joueurs dans une réservation d'1 heure avec des tranches de 30 minutes, nous recommandons 90.
* **Afficher les joueurs :** cochez-la pour voir les joueurs directement dans la réservation du calendrier.
* **Abandonné :** cochez-la pour ne plus utiliser ce sport.
* **Afficher les initiales des participants :** cochez-la pour que l'affichage montre les initiales au lieu du nom complet.
* **Temps maximum entre réservations en ligne :** le plus petit créneau libre autorisé entre deux réservations en ligne. Cela évite de laisser des créneaux si courts que personne ne pourra les réserver.
* **Espace entre réservations à l'ouverture/fermeture :** comme le précédent, mais en tenant compte aussi des créneaux avec l'heure d'ouverture et de fermeture.
* **Temps min. entre réservations admin :** l'espace libre minimum entre une réservation faite depuis l'administration et une autre.
* **Heure de début de journée :** l'heure à laquelle commence la journée, avec un nombre entier entre 0 et 23.
{% endstep %}

{% step %}
### Ajouter les terrains (ressources)

* Cliquez sur l'**ID** du sport ou non-sport.
*   Allez dans le bloc **Ressources**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure></div>
* Cliquez sur <i class="fa-plus-large">:plus-large:</i>.
* Une autre fenêtre s'ouvre :
  * **Nom :** le nom du terrain. L'idéal est le sport et son numéro (par exemple, _Padel 1_). Si le terrain est sponsorisé, vous pouvez utiliser le nom du sponsor.
  * **Commande :** la position du terrain dans le calendrier.
  * **Type de terrain :** intérieur, extérieur, couvert, etc.
  * **Sol/mur :** dépend du sport. Au tennis ou au football, on choisit le type de sol ; au padel ou au squash, le type de mur.
*   **Sauvegarder & Nouveau :** si vous créez plusieurs terrains, utilisez cette option. Le terrain est enregistré et un autre s'ouvre presque entièrement rempli, sauf le nom et l'ordre.

    <figure><img src="../../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

> **Important :** le terrain n'apparaîtra pas encore dans le calendrier. Vous devez d'abord lui donner un horaire :

<a href="../horarios/como-crear-un-horario.md" class="button primary">Comment créer un horaire</a>
