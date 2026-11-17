---
icon: lock
origen: 2a9d48b9d301
---
# Comment créer, modifier ou supprimer un rôle

Les **rôles** déterminent ce que chaque employé peut voir et faire dans Taykus. Chaque utilisateur a un rôle, et ce rôle définit ses autorisations dans chaque partie du logiciel.

### Vidéo explicative

{% embed url="https://youtu.be/Vk6PSU2hFQU" %}

## Où se trouvent les rôles

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **Rôles**.

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Vous verrez la liste des rôles et pourrez ouvrir chacun pour voir ses autorisations.

## Rôles créés par défaut

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

* **Admin Centro :** accès complet à tout le logiciel.
* **Recepción :** accès complet aux réservations, à l'académie et aux communications, et partiel aux paramètres.
* **Profesor :** accès partiel au calendrier, à l'académie et aux clients.
* **Soporte Taykus :** accès complet, pour que l'équipe d'assistance puisse vous aider en cas de question ou d'incident.

> Si vous ne voulez pas que les professeurs entrent dans le logiciel comme administrateurs, vous pouvez leur donner une adresse d'accès réservée aux professeurs, où ils ne verront que leurs cours, leurs élèves et leur calendrier. Par exemple : `https://mariademo.taykusdemo.com/teachers/login`

## Niveaux d'autorisation

Chaque rôle a plusieurs blocs d'autorisations. À côté de chaque autorisation, vous pouvez activer ou désactiver ces niveaux :

![](<../../.gitbook/assets/image (10).png>)

* **Voir :** l'utilisateur peut voir les informations.
* **Modifier :** l'utilisateur peut changer les informations. Selon l'autorisation, il peut aussi créer, supprimer ou exporter.

## Modifier les autorisations d'un rôle

{% stepper %}
{% step %}
### Ouvrir le rôle

* Allez dans **Paramètres › Rôles**.
* Cliquez sur l'**ID** du rôle.
{% endstep %}

{% step %}
### Activer ou désactiver des autorisations

* Vérifiez les blocs d'autorisations.
* Cliquez sur le niveau à modifier :
  * En **vert**, l'autorisation est activée.    ![](<../../.gitbook/assets/image (11).png>)
  * En **rouge**, elle est désactivée.    ![](<../../.gitbook/assets/image (12).png>)
* Les modifications s'enregistrent toutes seules ; inutile de cliquer sur Sauvegarder.
{% endstep %}
{% endstepper %}

## Créer un nouveau rôle

{% stepper %}
{% step %}
### Créer le rôle

* Allez dans **Paramètres › Rôles**.
* Cliquez sur l'option pour créer un nouveau rôle.
* Écrivez le nom du rôle et enregistrez.
{% endstep %}

{% step %}
### Configurer ses autorisations

* Ouvrez le rôle depuis son **ID**.
* Activez ou désactivez les autorisations comme expliqué dans la section précédente.
{% endstep %}
{% endstepper %}

## Supprimer un rôle

{% stepper %}
{% step %}
### Vérifier que personne ne l'utilise

* Avant de supprimer un rôle, vérifiez qu'aucun utilisateur ne l'a. Sinon, cet employé pourrait se retrouver sans accès.
{% endstep %}

{% step %}
### Supprimer le rôle

* Allez dans **Paramètres › Rôles**.
* Ouvrez le rôle depuis son **ID**.
* Utilisez l'option de suppression.
{% endstep %}
{% endstepper %}
