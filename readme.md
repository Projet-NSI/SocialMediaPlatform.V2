# Social Media Platform



# Présentation

"Social media website avec Django" est une application visant à créer un réseau social simpliste, à l'aide du framework Django

## Langages 

Python avec Django / SQLite / HTML / CSS

## Relation avec le programme terminale

Bases de données / Python / Programmation objet

# Modèles

Les modèles de données comprennent des objets pour les utilisateurs, les messages, les abonnements et les notifications.

## Modèles conceptuels

![1](/media/uploads/models/S'abonner_%C3%A0.png)
![2](/media/uploads/models/Etre_Suivi_Par.png)
![3](/media/uploads/models/Commenter_Sur.png)
![4](/media/uploads/models/Envoyer_%C3%A0.png)
![5](/media/uploads/models/Recevoir.png)
![6](/media/uploads/models/Profile-User-C.png)
![7](/media/uploads/models/Profile-Post-C.png)

## Modèles relationnels

![1](/media/uploads/models/User-Profile-Rel.png)
![2](/media/uploads/models/Message-Destinataire-Rel.png)
>Remarque:
un message peut être destiné à plusieurs utilisateurs, donc il faut créer une table de liaison

![3](/media/uploads/models/Post-Comment-Rel.png)
![4](/media/uploads/models/Post-Profile-Rel.png)
![5](/media/uploads/models/User-Notif-Rel.png)
![6](/media/uploads/models/User-Subscriber-Rel.png)
![7](/media/uploads/models/User-Subscription-Rel.png)

## Fonctionnalités

- [x] Obtention des données de l'utilisateur
- [ ] Création de comptes utilisateur (Profil) 
- [ ] Publication de messages
- [x] Publication de posts
- [x] Commentaires sur les posts
- [ ] Gestion des abonnements
- [ ] Réception de notifications
- [ ] Liker des posts (et commentaires)
- [ ] Recherche d'autres utilisateurs à suivre


## Points importants

- [x] Sécurité des données utilisateur
- [ ] Optimisation de la vitesse pour prendre en charge les volumes élevés de trafic
- [ ] Mise en place d'une interface utilisateur conviviale
- [ ] Gestion des erreurs

## Difficultés rencontrées


# Obtention de données de l'utilisateur


# Messages et Commentaires

Nous allons voir les fonctionnalité des messages et des commentaires en ajoutant la possibilité de modifier un message, de supprimer un message, d'ajouter un commentaire et de supprimer un commentaire.  Nous allons également restreindre les différentes vues que nous avons créées afin que seuls les utilisateurs qui doivent y avoir accès puissent le faire.

## Envoyer des messages