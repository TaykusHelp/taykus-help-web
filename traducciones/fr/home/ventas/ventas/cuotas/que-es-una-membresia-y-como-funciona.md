---
origen: dcea7bf35b5b
---

# Qu'est-ce qu'une adhésion et comment fonctionne-t-elle

Une adhésion est une cotisation qui, en plus d'être encaissée périodiquement, change le type de client de la personne qui l'a. Cela fonctionne comme l'abonnement d'une salle de sport : tant que le client paie, il est **Membre** et profite de ses avantages, comme des prix spéciaux, et quand il se désinscrit, il redevient **Non-membre**.

## Comment une cotisation devient une adhésion

Dans la fiche de la cotisation, dans le bloc **Vente périodique**, remplissez ces deux champs :

<figure><img src="../../.gitbook/assets/cuotas-automaticas-campos.png" alt=""><figcaption></figcaption></figure>

* **Type de client adhésion :** le type de client qu'il aura tant qu'il est inscrit à la cotisation. Par exemple, **Membre**.
* **Type de client fin d'adhésion :** le type de client qu'il aura quand il se désinscrit. Par exemple, **Non-membre**.

Les types de client doivent être créés au préalable. Pour savoir comment, consultez [Comment créer différents types de clients](../../../jugadores/jugadores/fichas-de-jugador/como-crear-diferentes-tipos-de-jugadores.md). Pour leur donner des prix spéciaux, consultez [Personnaliser les prix par type de client](../../../configuracion/configuracion/ventas/personalizacion-de-precios/personalizar-precios-por-tipo-de-jugador.md).

Pour savoir où se trouvent ces champs, consultez [Comment créer un produit de type Cotisation](../../../configuracion/configuracion/ventas/productos/como-crear-un-producto-tipo-cuota.md).

## Comment un client entre dans l'adhésion

* **Le club l'ajoute :** depuis **Ventes › ventes périodiques**, dans l'onglet **Clients** de la cotisation, avec **+**.
* **Le client y souscrit lui-même en ligne :** si la case **Vente en ligne** est cochée sur la cotisation, il peut l'acheter depuis l'espace client du club.

En entrant, il passe automatiquement au **Type de client adhésion**.

## Quand il cesse d'être membre

Le client passe au **Type de client fin d'adhésion** dans l'un de ces cas :

* Quand arrive la date de **Fin** de sa cotisation.
* Quand la cotisation est annulée pour impayé. Consultez [Comment automatiser l'annulation pour impayé](como-automatizar-la-cancelacion-por-impago.md).
* Quand le club le désinscrit de la cotisation, en changeant sa date de **Fin**. Consultez [Comment désinscrire un client d'une cotisation](como-dar-de-baja-a-un-cliente-de-una-cuota.md).
