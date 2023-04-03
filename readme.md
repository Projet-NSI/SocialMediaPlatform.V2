# Social Media Platform



# Présentation

"Social media website avec Django" est une application visant à créer un réseau social simpliste, à l'aide du framework Django

## Langages 

Python avec Django / SQLite / HTML / CSS (Bootstrap5)

## Relation avec le programme terminale

Bases de données / Python / Programmation objet

# Modèles

Les modèles de données comprennent les utilisateurs, les profils, les messages, les commentaires.

![1](/media/uploads/models/modeles_social.png)

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

# Fonctionnement d'une application Django
Dans une application il y a fichiers par defaut qui sont:

## migrations:

Elle permet d'apporter des modifications à des modèles dans un schéma de base de donnés 
```
python3 manage.py
```
>manage.py django-admin est l'utilitaire en ligne de commande de Django pour les tâches administratives
```
python3 manage.py makemigrations
```
> résponsable de la création de nouvelles migrations en fonction des modifications que vous avez apportées aux modèles.

```
python3 manage.py migrate
```
> résponsable de l’exécution et de l’annulation des migrations (sauvegardes).

## settings:
c'est le fichier qui s'occupe des réglages de l'application
elle a par exemple une liste avec tout les adresses autorisés


# Modules views.py

Nous utilisons différents modules:

```
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
```

## Render

```
return render(request, 'social/post_detail.html', context)
```


Render est un module de django.shortcuts

Les moteurs de rendu personnalisés doivent implémenter une méthode render(template_name, context, request=None). Cette méthode doit renvoyer un modèle rendu (sous la forme d'une chaîne de caractères) ou soulever la question TemplateDoesNotExist.

# Views.py

## View

```
class PostListView(View):
```

## UpdateView

UpdateView est un module de django.view.generic.edit

UpdateView est une vue qui affiche un formulaire de modification d'un objet existant.

## DeleteView

UpdateView est un module de django.view.generic.edit

DeleteView est une vue qui affiche une page de confirmation et supprime un fichier existant.

## UserPassesTestMixin

Module de Django permettant de faire passer des tests de verifications aux utilisateurs pour gérer leurs possibilités 

## LoginRequiredMixin

Module de Django vérifiant si l’utilisateur est connecté (ce mixin vérifie que les AUTHENTICATION_BACKENDS par défaut rejettent les utilisateurs inactifs.)

## Reverse_lazy()

```
def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
```

Fonction utile pour procéder à une résolution d’URL avant le chargement de la configuration des URLs.

Dans notre projet, nous l'utilisons pour les mises à jour et supression de posts et commentaires, ou encore dans la création d'un profil 

## Kwargs et Args

```
 def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
```
> *args permet de passer un nombre arbitraire d'arguments positionnels à votre fonction.
> 
> **kwargs permet de gérer les arguments nommés que vous n'avez pas définis à l'avance.

# Models.py

## User

Les objets utilisateurs sont au cœur du système d'authentification.

Les principaux attributs de l'utilisateur par défaut sont les suivants :

- nom d'utilisateur
- mot de passe
- email
- prenom
- nom

## Timezone

```
sendingTime = models.DateTimeField(default=timezone.now)
```

Django inclut un paramètre TIME_ZONE dont la valeur par défaut est l'horaire 'UTC'. Il se trouve dans le fichier de configuration 'settings.py':
```
TIME_ZONE = 'UTC'
```

# Urls.py

C'est le fichier qui permet de stocker les chemins à l'aide du module path qui sert à récuperer des chemins et de les transformer en variable:
```
from django.urls import path
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
]
```

# Forms.py

```
class PostForm(forms.ModelForm):
    contenu = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Dites quelque chose...'
            }))

    class Meta:
        model = Post
        fields = ['contenu']
```

Django gère trois parties distinctes du travail induit par les formulaires dans forms.py:

- préparation et restructuration des données en vue de leur présentation
- création des formulaires HTML pour les données
- réception et traitement des formulaires et des données envoyés par le client

# Admin.py





