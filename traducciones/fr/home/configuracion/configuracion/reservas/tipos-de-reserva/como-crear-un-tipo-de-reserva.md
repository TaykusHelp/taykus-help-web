---
icon: business-time
origen: a25bf8ff2abf
---
# Comment créer un type de réservation

Les **types de réservation** sont des catégories (école, cours particulier, match…) qui donnent à chaque réservation ses propres règles : couleur, prix, durée, qui peut réserver et comment. Grâce à eux :

* Vous distinguez d'un coup d'œil chaque réservation dans le calendrier par sa couleur.
* Vous voyez dans les rapports combien de réservations il y a de chaque type.
* Vous pouvez facturer un prix différent de l'habituel selon le type de réservation.

<div align="left"><figure><img src="../../../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure></div>

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux types de réservation

* Cliquez sur l'icône <i class="fa-gear" style="color:blue;">:gear:</i> en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **réservations**.\
  ![](<../../../.gitbook/assets/image (97).png>)
*   Cliquez sur le bloc **TYPES DE RÉSERVATION**.<br>

    <figure><img src="../../../.gitbook/assets/image (98).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Créer le type de réservation

* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :<br>

    <figure><img src="../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (101).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

> **Important :** les champs marqués d'un astérisque (\*) sont obligatoires.

#### Données générales

* **Description (\*) :** le nom du type de réservation.
* **Catégorie :** facultative. Une sous-famille pour ce type.
* **Commande :** la position à laquelle il apparaît dans le calendrier.
* **Description détaillée :** facultative. Des détails sur ce type de réservation.
* **Images :** facultative. Aide à reconnaître le type de réservation.

#### Prix

* **Type de prix (\*) :** choisissez dans le menu déroulant :
  * **Par ressource :** on facture le prix configuré dans les horaires.
  * **Par personne :** on facture le prix des horaires à chaque participant.
  * **Gratuit :** rien n'est facturé.
* **Prix :** un prix fixe pour ce type de réservation, sans tenir compte des tarifs par calendrier.
* **Réservation par lieu :** cochez-la seulement si le type de prix est **Par personne**.

#### Réservation et annulation en ligne

* **Est public :** cochez-la pour pouvoir réserver en ligne.
* **Permet d'annuler en ligne :** si elle est activée, les clients peuvent annuler en ligne. Sinon, seul le club peut annuler.
* **Minimum de minutes d'anticipation :** avec combien d'avance minimale on peut réserver.
* **Maximum de minutes d'anticipation :** avec combien d'avance maximale on peut réserver.
* **Minutes d'anticipation pour les annulations :** jusqu'à combien de minutes avant on peut annuler.
* **Minutes de pré-réservation :** les minutes pendant lesquelles le terrain reste bloqué pendant que le client termine sa réservation.
* **Heures avant expiration :** combien d'heures avant la réservation celle-ci expire si elle n'est pas complétée.
* **Rembourser le paiement en cas d'annulation et d'expiration :** cochez-la pour que le client récupère son argent si la réservation est annulée ou expire sans être complétée.

#### Participants et niveau

* **Nombre minimum de participants (\*) :** le minimum de personnes pour ce type de réservation.
* **Nombre maximum de participants (\*) :** le maximum de personnes.
* **Min. Niveau** et **Max. Niveau :** le niveau de jeu autorisé.
* **Genre :**
  * **Homme :** seuls les utilisateurs de genre masculin peuvent réserver.
  * **Femme :** seules les utilisatrices de genre féminin peuvent réserver.
  * **Ouvert :** tout le monde peut réserver.

#### Limites

* **Permettre de personnaliser la durée :** permet de changer l'heure de fin en créant la réservation depuis l'administration.
* **Nombre maximum de réservations par jour :** combien de réservations de ce type peuvent être faites par jour.
* **Nombre maximum de réservations :** s'il y a une anticipation maximale, compte les réservations d'aujourd'hui jusqu'à cette anticipation. Sinon, compte toutes les réservations à partir d'aujourd'hui.
* **Restrictions du maximum de réservations en ligne et admin :** les limites s'appliquent aussi bien aux réservations en ligne qu'à celles du club.

#### Apparence

* **Couleurs :** la couleur de ce type de réservation dans le calendrier. Elle peut être fixe ou changer selon l'état de la réservation.
{% endstep %}

{% step %}
### Ajouter les ressources

* Dans **Types de réservation**, cliquez sur l'**ID** du type que vous venez de créer.
*   Ouvrez l'onglet **Ressources**.

    <figure><img src="../../../.gitbook/assets/image (103).png" alt=""><figcaption></figcaption></figure>
* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :<br>

    <figure><img src="../../../.gitbook/assets/image (104).png" alt=""><figcaption></figcaption></figure>

    * **Groupe de ressources :** la ressource occupée par ce type de réservation.
    * **Minutes bloquées avant la réservation :** combien de minutes avant la ressource est bloquée pour la préparer. Par exemple, si la réservation commence à 10:00 et que vous mettez 10 minutes, le terrain est bloqué dès 9:50.
    * **Durée :** la durée par défaut de la réservation.
    * **Durées autorisées :** les durées pouvant être choisies, en minutes et séparées par des espaces (par exemple : `30 60 120`). Si vous laissez vide, elles sont calculées selon la configuration du groupe de ressources.
    * **Ressource principale :** la ressource choisie en premier.
    * **Sélectionnable en ligne :** cochez-la pour que le client puisse choisir cette ressource en réservant en ligne.
* Cliquez sur **Sauvegarder**.

> Si le type de réservation occupe deux ressources (par exemple, terrain et professeur), répétez cette étape pour chacune.
{% endstep %}
{% endstepper %}

## Si quelque chose ne fonctionne pas

* **Le type de réservation n'apparaît pas en réservant un terrain :** ajoutez ce terrain dans l'onglet **Ressources** du type de réservation (étape 3).
