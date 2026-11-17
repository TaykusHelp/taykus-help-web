---
icon: display-chart-up-circle-dollar
origen: d2d1d0d733e4
---
# Comment mettre des prix sur l'horaire

Dans **Tarifs par calendrier**, on décide du prix de chaque réservation selon le jour et l'heure. Par exemple, vous pouvez facturer différemment en heure de pointe et en heure creuse. Chaque tranche utilise un produit de type **Service**, qui fixe le prix.

> **Important :** ici, on ne change que les **prix**. L'ouverture et la disponibilité des terrains ne changent pas. Pour cela, consultez cet article :
>
> <a href="../horarios/como-crear-un-horario.md" class="button primary">Comment créer un horaire</a>

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
### Créer le calendrier de prix

* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :

    <div align="left"><figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure></div>

    * **Nom :** nous vous conseillons d'indiquer les jours de la semaine inclus.
    * **Priorité :** un nombre qui décide quel prix l'emporte si deux se chevauchent. Celui au **nombre le plus élevé** s'applique en premier. En général, on met le nombre le plus bas à la semaine, un plus élevé au week-end (vous pourrez ainsi appliquer le prix du week-end à un jour de semaine) et le plus élevé aux jours fériés ou à la fermeture.
    * **Début :** date à partir de laquelle ces prix s'appliquent. Si c'est dès maintenant, laissez vide.
    * **Fin :** date jusqu'à laquelle ils s'appliquent. S'il n'y a pas de date de fin prévue, laissez vide.
    * **Jour de la semaine :** cochez les jours où ces prix s'appliquent.
* Cliquez sur **Sauvegarder**.
{% endstep %}

{% step %}
### Ajouter les tranches de prix

Dans une même journée, vous pouvez avoir plusieurs tranches à des prix différents (par exemple, heure de pointe et heure creuse).

* Cliquez sur l'**ID** du calendrier de prix.
*   Allez dans le bloc **Tarifs**.

    <div align="left"><figure><img src="../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure></div>
* Cliquez sur :heavy\_plus\_sign:.
*   Cette fenêtre s'ouvre :

    <figure><img src="../../../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

    * **Ressource :** les terrains ou professeurs auxquels s'applique le prix.
    * **Début :** heure de début de la tranche.
    * **Fin :** heure de fin de la tranche.
    * **End is next day :** cochez-la si la tranche se termine à 00:00 ou plus tard.
    * **Appliquer ce prix en cas de chevauchement :** si une réservation couvre deux tranches, elle sera entièrement facturée à ce prix au lieu d'être répartie entre les deux.
    * **Produit :** le produit de type **Service** qui fixe le prix de cette tranche.
* Cliquez sur <i class="fa-floppy-disk" style="color:green;">:floppy-disk:</i> pour enregistrer.
{% endstep %}
{% endstepper %}

> S'il y a plusieurs tranches à des prix différents, répétez la dernière étape pour chacune.

## Si quelque chose ne fonctionne pas

* **La réservation est à 0 € :** vérifiez que le terrain est ajouté à la tranche, que la tranche couvre l'heure de la réservation et, si elle se termine à 00:00 ou plus tard, que **End is next day** est coché.
* **J'ai élargi l'horaire d'ouverture et je ne peux pas réserver sur les nouvelles heures :** élargissez aussi ici la tranche de prix. L'horaire et les prix doivent couvrir les mêmes heures.
* **Un jour férié est facturé au prix normal :** vérifiez que le calendrier de prix des jours fériés a une priorité plus élevée que celui de la semaine.
