---
icon: file-check
origen: beb346012d5d
---
# Avant de commencer les remises

Avant de faire un Q19, il est important de prendre en compte certains paramétrages et vérifications préalables dans le logiciel.\
Ces étapes vous permettent de vous assurer que les données fiscales sont correctement préparées pour générer le fichier correctement.

{% stepper %}
{% step %}
### Accès aux paramètres des entreprises

* Cliquez sur l'icône ⚙ en haut à droite et ouvrez **Paramètres**.
* Cliquez sur **Ventes**.
*   Sélectionnez l'onglet **Entreprises.**<br>

    <figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Créer les données de l'entreprise

*   Cliquez sur ➕<br>

    <figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
* Remplissez les données fiscales de l'entreprise. Le seul champ obligatoire est l'e-mail.
  * **REMARQUE IMPORTANTE :** ne touchez pas à l'Invoice Number Format.
* Remplissez la section des prélèvements avec l'IBAN du compte, le CIF/VAT, le préfixe de l'émetteur bancaire et le préfixe de la banque créancière.
  * <mark style="background-color:$warning;">**REMARQUE IMPORTANTE :**</mark> <mark style="background-color:$warning;">le préfixe de l'émetteur bancaire et le préfixe de la banque créancière vous sont donnés par votre banque (elle l'appelle parfois « suffixe »). C'est généralement un nombre à 3 chiffres, souvent 000 ou 001.</mark>
* Cliquez sur enregistrer pour terminer.
{% endstep %}
{% endstepper %}

Une fois ce paramétrage terminé, l'entreprise est correctement préparée sur le plan fiscal pour générer le fichier Q19 dans le logiciel.

Pensez à vérifier en particulier que les données bancaires et fiscales sont bien renseignées et à ne pas modifier le champ **Invoice Number Format**, car cela pourrait empêcher le processus de fonctionner correctement.

Une fois ces vérifications faites, vous pouvez poursuivre la génération du Q19 en toute sécurité.

Pour savoir comment, consultez cet article :

<a href="generacion-del-q19-domiciliacion-de-recibos-bancarios.md" class="button primary">Génération du Q19 (prélèvement des échéances bancaires)</a>
