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

![1](/Mod%C3%A8les/S'abonner_%C3%A0.png)
![2](/Mod%C3%A8les/Etre_Suivi_Par.png)
![3](/Mod%C3%A8les/Commenter_Sur.png)
![4](/Mod%C3%A8les/Envoyer_%C3%A0.png)
![5](/Mod%C3%A8les/Recevoir.png)
![6](/Mod%C3%A8les/Profile-User-C.png)
![7](/Mod%C3%A8les/Profile-Post-C.png)

## Modèles relationnels

![1](/Mod%C3%A8les/User-Profile-Rel.png)
![2](/Mod%C3%A8les/Message-Destinataire-Rel.png)
>Remarque:
un message peut être destiné à plusieurs utilisateurs, donc il faut créer une table de liaison

![3](/Mod%C3%A8les/Post-Comment-Rel.png)
![4](/Mod%C3%A8les/Post-Profile-Rel.png)
![5](/Mod%C3%A8les/User-Notif-Rel.png)
![6](/Mod%C3%A8les/User-Subscriber-Rel.png)
![7](/Mod%C3%A8les/User-Subscription-Rel.png)

## Fonctionnalités

- [ ] Obtention des données de l'utilisateur
- [ ] Création de comptes utilisateur (Profil) 
- [ ] Publication de messages
- [ ] Publication de posts
- [ ] Commentaires sur les posts
- [ ] Gestion des abonnements
- [ ] Réception de notifications
- [ ] Liker des posts (et commentaires)
- [ ] Recherche d'autres utilisateurs à suivre


## Points importants

- [ ] Sécurité des données utilisateur
- [ ] Optimisation de la vitesse pour prendre en charge les volumes élevés de trafic
- [ ] Mise en place d'une interface utilisateur conviviale
- [ ] Gestion des erreurs

## Difficultés rencontrées


# Obtention de données de l'utilisateur