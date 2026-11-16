---
origen: 0579304bd989
---

# Comment émettre une facture depuis Ventes > Paiements

Depuis **Ventes › Paiements**, vous pouvez émettre la facture d'une vente à partir de son paiement. Cela se fait comme depuis **Ventes › lignes**, mais dans cette liste il faut cliquer sur le numéro de la colonne **Vente**.

> **Important :** avant d'émettre la facture, vérifiez que vous avez créé les données de votre entreprise dans **Paramètres › Ventes › Entreprises** et, si vous facturez des entreprises, leurs données dans **Paramètres › Ventes › Sociétés clientes**. Pour savoir comment, consultez ces articles :

<a href="https://app.gitbook.com/s/V0h7jTfpeuZY1RmPEtNK/configuracion/ventas/empresas/como-configurar-los-datos-de-empresa" class="button primary">Comment configurer les données de l'entreprise</a>

<a href="https://app.gitbook.com/s/V0h7jTfpeuZY1RmPEtNK/configuracion/ventas/empresas-clientes/como-crear-empresas-cliente-en-el-sistema" class="button primary">Comment créer des sociétés clientes dans le système</a>

Voici les étapes à suivre :

{% stepper %}
{% step %}
### Accès aux paiements

* Allez dans le menu latéral gauche et sélectionnez **Ventes**.
* Dans le menu déroulant, choisissez **Paiements**.
*   Cherchez le paiement de la vente à facturer. Vous pouvez utiliser les filtres de chaque colonne.<br>

    <figure><img src="../../.gitbook/assets/pagos-listado.png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
### Ouvrir la vente

* Cliquez sur le numéro de la colonne **Vente** (pas sur l'**ID**).
*   Dans la vente, cliquez sur **Émettre une facture**.<br>

    <figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>
* Une fenêtre s'ouvre avec les données de facturation.
{% endstep %}

{% step %}
### Données de la facture

Dans le bloc **Émetteur** :

* Sélectionnez l'**entreprise émettrice** dans le champ **Entreprise**.
* Le système remplit automatiquement les données associées, par exemple :
  * Nom
  * CIF
  * E-mail
  * Téléphone

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

Dans le bloc **Acheteur**, vous pouvez choisir entre deux options :

**Personne physique**

Si la facture est pour un particulier :

* Laissez cochée l'option **Personne physique**.
* Vérifiez ou complétez les données du client :
  * Nom complet
  * DNI
  * E-mail
  * Téléphone
  * Adresse

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

**Entreprise**

Si la facture est pour une entreprise :

* Cochez l'option **Entreprise**.
* Dans le champ **Société cliente**, sélectionnez l'entreprise correspondante.
* Le système complète automatiquement les données fiscales de cette entreprise.

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>


{% endstep %}

{% step %}
### Enregistrer

* Vérifiez les données et cliquez sur l'icône d'enregistrement.
* La facture de cette vente est générée et envoyée automatiquement au client.
{% endstep %}
{% endstepper %}

> **Important :** dans **Ventes › Paiements par chèque**, cela se fait exactement de la même façon : cliquez sur le numéro de la colonne **Vente** et suivez les mêmes étapes.

Si vous devez la renvoyer ou la télécharger, consultez [Comment renvoyer ou télécharger une facture](como-reenviar-o-descargar-una-factura.md).
