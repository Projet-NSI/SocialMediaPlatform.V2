# Social Media Platform



# Présentation

"Social media website avec Django" est une application visant à créer un réseau social simpliste, à l'aide du framework Django

## Langages 

Python avec Django / SQLite / HTML / CSS (Bootstrap5)

## Relation avec le programme terminale

Bases de données / Python / Programmation objet

# Modèles

Les modèles de données comprennent les utilisateurs, les profils, les messages, les commentaires.

![1](/media/uploads/models/modeles.png)

## Fonctionnalités

- [x] Obtention des données de l'utilisateur
- [x] Deconnexion du compte utilisateur
- [x] Création de comptes utilisateur (Profil) 
- [x] Publication de posts
- [x] Publication de commentaires
- [x] Modification de posts/commentaires
- [x] Suppression de posts/commentaires
- [x] Commentaires sur les posts
- [ ] Gestion des abonnements
- [ ] Liker des posts (et commentaires)
- [ ] Recherche d'autres utilisateurs à suivre


## Points importants

- [ ] Sécurité des données utilisateur
- [x] Mise en place d'une interface utilisateur conviviale
- [ ] Gestion des erreurs

## Difficultés rencontrées


# Obtention de données de l'utilisateur

Nous utilisons django-allauth[^1] pour les récupérations des données. 


[^1]: Django-allauth est un package de Django qui fournit des fonctionnalités
d'authentification pour les utilisateurs. Il inclut des formulaires de création de compte, de
connexion, de récupération de mot de passe, et des pages HTML pour gérer les
comptes d'utilisateurs. Cela nous est très utile pour notre réseau social qui nécessite
des fonctionnalités d'authentification et de gestion des utilisateurs.


