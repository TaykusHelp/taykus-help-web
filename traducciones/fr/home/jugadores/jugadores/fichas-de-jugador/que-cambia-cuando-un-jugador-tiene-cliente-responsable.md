---
icon: circle-info
origen: b97623bce639
---
# Ce qui change quand un client a un client responsable

Quand vous attribuez un client responsable à un client, la fiche associée peut utiliser l'e-mail, le téléphone et les moyens de paiement du responsable. Voici ce qui change dans chaque cas et comment supprimer la relation.

## E-mail et téléphone

Si les champs **Email** ou **N° de téléphone** de la fiche associée sont vides, ils sont complétés à l'enregistrement avec ceux du client responsable.

Comme une adresse e-mail ne peut pas apparaître sur deux fiches, le logiciel ajoute automatiquement un **+** et un numéro avant le @. Par exemple, si l'e-mail du responsable est `unoperez@yopmail.com`, celui de la fiche associée devient `unoperez+239@yopmail.com`. C'est une adresse qui fonctionne : tout ce qui est envoyé à la fiche associée arrive à l'e-mail du client responsable.

<figure><img src="../../.gitbook/assets/cliente-responsable-correo-generado.png" alt=""><figcaption></figcaption></figure>

> **Important :** si la fiche associée a déjà son propre e-mail ou téléphone, ils ne sont pas modifiés, et ce qui est envoyé à cette fiche continue d'arriver à sa propre adresse.

## Encaissements au point de vente

Quand vous encaissez au **point de vente** une vente de la fiche associée, la carte enregistrée et le **Bon monétaire** du client responsable apparaissent comme moyens de paiement. En passant la souris sur l'un des deux, vous verrez le nom de son propriétaire.

<figure><img src="../../.gitbook/assets/tpv-cobro-cliente-responsable.png" alt=""><figcaption></figcaption></figure>

## Espace client

Le client responsable peut se connecter à l'espace client avec son identifiant et son mot de passe et passer aux comptes de ses associés, par exemple pour payer avec son bon ou sa carte enregistrée. Pour savoir comment, consultez cet article :

<a href="../../../zona-de-clientes/zona-de-clientes/como-cambiar-entre-tu-cuenta-y-la-de-tus-asociados-en-la-zona-de-clientes.md" class="button primary">Comment passer de votre compte à celui de vos associés dans l'espace client</a>

La personne associée ne peut se connecter seule que si elle a son propre e-mail. Sinon, elle doit passer par le compte du client responsable.

## Supprimer la relation

Pour supprimer la relation, modifiez la fiche associée, videz le champ **Client responsable** et cliquez sur **Sauvegarder**.

> **Important :** en supprimant la relation, l'e-mail généré (avec le **+** et le numéro) reste sur la fiche et le logiciel ne prévient pas. Si vous voulez que ce qui est envoyé à cette fiche n'arrive plus à l'ancien responsable, remplacez l'e-mail par celui de la personne elle-même.

Pour attribuer un client responsable à un client, consultez cet article :

<a href="como-asignar-un-cliente-responsable-a-un-jugador.md" class="button primary">Comment attribuer un client responsable à un client</a>
