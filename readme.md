# Social Media Platform - Projet NSI:

![home](https://i.ibb.co/2ZgswzL/Capture-d-e-cran-2023-04-03-a-21-07-43.png)

# Sommaire : 

- Cahier des charges
- Spécifications techniques
- Modalités de mise en œuvre
- Conclusion 
- Bibliographie

# I - Cahier des charges

## Présentation

*Social media website* avec Django est une application visant à créer un réseau social simpliste, à l'aide du framework Django[^1], ce projet comportera donc de la programmation objet et une base de données.

[^1]: Django peut être séparé en deux parties clés : les URLs et les vues. Ce sont deux concepts pour gérer les requêtes des utilisateurs. Les URLs sont des adresses web uniques qui identifient une vue dans votre application web. Les vues sont des fonctions Python qui répondent aux requêtes des utilisateurs et renvoient une réponse HTTP, généralement une page web.

### Langages 

Python avec Django / SQLite / HTML / CSS (Bootstrap5[^2])

[^2]: Bootstrap 5 est un framework front-end open-source qui permet de créer des interfaces utilisateur pour des sites web et des applications web. Il fournit des styles CSS pré-construits pour des éléments tels que des boutons, des formulaires, des tables, etc., ainsi que des composants JavaScript interactifs tels que des menus déroulants, des modales, des carrousels, etc. C’est très pratique pour notre projet car cela nous permet de créer rapidement et facilement des interfaces utilisateur attrayantes et cohérentes.

## Modèles

Les modèles de données comprennent les utilisateurs, les profils, les messages et les commentaires.

![Schema relationnel](https://i.ibb.co/bBVxFf0/modeles-social.png)

> Remarque : La table *User* est integrée dans Django, elle a pour clé primaire son id qui identifie l'utilisateur de manière unique, qui permet ici aux tables *Post* et *Comment* d'interagir.

### Fonctionnalités

- [x] Obtention des données de l'utilisateur
- [x] Deconnexion du compte utilisateur
- [x] Création de comptes utilisateur (Profil) 
- [x] Publication de posts
- [x] Publication de commentaires
- [x] Modification de posts/commentaires
- [x] Suppression de posts/commentaires
- [x] Commentaires sur les posts
- [x] Gestion des abonnements
- [x] Liker des posts (et commentaires)
- [ ] Recherche utilisateurs à suivre

## Points importants

- [ ] Sécurité des données utilisateur
- [x] Mise en place d'une interface utilisateur conviviale
- [ ] Gestion des erreurs

## Exemple 

Un utilisateur s'inscrit, crée son profil, publie et commente un post, suit d'autres utilisateurs pour voir leurs profils et communiquer avec eux par message et reçoit une notification lorsque ces utilisateurs publient de nouveaux messages.

# II - Spécifications techniques

## Architecture client-server
L'architecture client-server est composée de trois étapes : 

- détailler le routage des URL pour associer les vues adaptées aux requêtes HTTP que le site devra traiter (y compris avec des informations encodées dans les URL).
- définir les fonctions de visualisation et créer les pages HTML qui vont permettre de publier les informations à destination des utilisateurs du site.
- créer les gabarits qui vont permettre de publier les données dans les vues.

![2](media/uploads/models/basic-django.png)

## Pages web

Nous aurons à créer plusieurs pages web. Cela fait beaucoup d'éléments à maîtriser dans une seule section d'apprentissage de l'outil. Nous avons donc opté pour ne traiter dans cette section que de la page d'accueil et de traiter les autres pages dans une autre section du didacticiel. Cela permet, de mieux appréhender les composants comme le routage d'URL ou les vues et d'une manière générale le fonctionnement du modèle de Django.

## Types de fichiers

Notre programme traitera des fichiers PNG, JPG, GIF, MP4, MP3 et HTML.

## Arborescence

Grâce à Django, nos fichiers sont répartis de base dans plusieurs applications (ou modules) et un projet.

Notre début de structure se façonne ainsi 

- landing
    - templates
        - landing
            - base.html
            - index.html
            - navbar.html
    - admin.py
    - apps copy.py
    - tests.py
    - apps.py
    - models.py
    - urls.py
    - views.py
- social
    - templates
        - social
            - comment_delete.html
            ...
            (voir github)
    - admin.py
    - apps copy.py
    - tests.py
    - apps.py
    - models.py
    - urls.py
    - views.py
- socialmedia
    - settings.py
    ...
- media
    - uploads
        - logos
            ...
        - models
            ...
        - profile_pictures
            ...
- templates
    ...
- db.sqlite3
- manage.py
- readme.md
- requirements.txt

> Remarque : nous récupéré un module *templates* en dessous qui comprends toutes les pages pré construites pour les connexions et inscriptions à l’aide de django-allauth (plusieurs grandes entreprises comme google, instagram, twitter utilisent django-allauth, c’est l’une des bibliothèque les plus efficace.)
> *socialmedia* est le nom de notre projet Django. Il comprend notamment les settings.py et les urls. 
> *landing* et *social* sont des applications de notre projet Django


## Obtention de données de l'utilisateur

Nous utilisons django-allauth[^3] pour les récupérations des données. 

[^3]: Django-allauth est un package de Django qui fournit des fonctionnalités
d'authentification pour les utilisateurs. Il inclut des formulaires de création de compte, de
connexion, de récupération de mot de passe, et des pages HTML pour gérer les
comptes d'utilisateurs. Cela nous est très utile pour notre réseau social qui nécessite
des fonctionnalités d'authentification et de gestion des utilisateurs.

## Fonctionnement d'une application Django

Dans une application il y a des modules par défaut qui sont:

### Migrations.py:

Elle permet d'apporter des modifications à des modèles dans un schéma de base de donnés 
```
python3 manage.py
```
>manage.py django-admin est l'utilitaire en ligne de commande de Django pour les tâches administratives
```
python3 manage.py makemigrations
```
> responsable de la création de nouvelles migrations en fonction des modifications que vous avez apportées aux modèles.

```
python3 manage.py migrate
```
> responsable de l’exécution et de l’annulation des migrations (sauvegardes).

## Settings.py

C'est le fichier qui s'occupe des réglages de l'application
elle a par exemple une liste avec tout les adresses autorisés

Dans le fichier settings.py, il y a notamment les applications installées, dont ‘landing’ et les pages allauth, crispy_forms[^4]

```
INSTALLED_APPS = [
    'landing',
    'social',

    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
```

[^4]: crispy_forms est une API pour récupérer les données d’un formulaire
## Modules views.py

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

### Render

```
return render(request, 'social/post_detail.html', context)
```


Render est un module de django.shortcuts

Les moteurs de rendu personnalisés doivent implémenter une méthode render(template_name, context, request=None). Cette méthode doit renvoyer un modèle rendu (sous la forme d'une chaîne de caractères) ou soulever la question *TemplateDoesNotExist*.

## Views.py

C'est le module permettant de stocker les vues (fonctions) pour notre projet Django.

### View

```
class PostListView(View):
```

Le module *View* est une classe parent pour les vues, qui possède différentes méthodes utiles pour celles-ci.

https://docs.djangoproject.com/en/4.1/ref/class-based-views/base/

### UpdateView

UpdateView est un module de django.view.generic.edit

UpdateView est une vue qui affiche un formulaire de **modification d'un objet existant**.

### DeleteView

UpdateView est un module de django.view.generic.edit

DeleteView est une vue qui affiche une **page de confirmation** et supprime un fichier existant.

### UserPassesTestMixin

Module de Django permettant de faire passer des **tests de verifications** aux utilisateurs pour gérer leurs possibilités 

### LoginRequiredMixin

Module de Django vérifiant si l’utilisateur est connecté (ce mixin vérifie que les *AUTHENTICATION_BACKENDS* par défaut rejettent les utilisateurs inactifs.)

### Reverse_lazy()

```
def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
```

Fonction utile pour procéder à une résolution d’URL **avant le chargement** de la configuration des *URLs*.

Dans notre projet, nous l'utilisons pour les mises à jour et supression de posts et commentaires, ou encore dans la création d'un profil 

### Kwargs et Args

```
 def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
```
Les paramètres de la fonction *post* 'args' et 'kwargs' permettent de passer plusieurs arguments ou des arguments de mots-clés à une fonction
> *args permet de passer plusieurs arguments à une fonction. Si on ajoute print(args), cela va retourner un tuple contenant tous les arguments.
> **kwargs permet de passer des arguments de mots-clés à une fonction. Si on ajoute print(kwargs), cela va retourner un dictionnaire avec tous les arguments de mot clés

### Redirect

redirect(to, *args, permanent=False, **kwargs)¶

Renvoie une réponse HttpResponseRedirect à l’URL correspondant aux paramètres transmis.

Nous l'utilisons pour les fonctions d'ajouts et de retraits d'abonnements dans nos vues, en indiquant en paramètre l'URL du profil qui sera utilisée comme emplacement de redirection.

```
def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', profile.pk)
```

### HttpResponserRedirect()

HttpResponseRedirect() prend un seul paramètre : l’URL vers laquelle l’utilisateur va être redirigé (redirige vers une nouvelle URL).

Nous l'utilisons dans nos vues pour les likes et dislikes pour rediriger l'utilisateur vers l'URL de la page où il se trouve.

```
next = request.POST.get('next','/')
return HttpResponseRedirect(next)
```

### Crsf_token

Django est livré avec une protection simple d’emploi contre les attaques de type Cross Site Request Forgeries. Lors de l’envoi d’un formulaire par la méthode POST et la protection CSRF active, nous devons obligatoirement utiliser la balise de gabarit csrf_token

```
<form method="POST">
    {% csrf_token %}
    {{ form | crispy }}
    <div class="d-grid gap-2">
        <button class="btn btn-primary mt-3">Envoyer!</button>
    </div>
</form>
```
## Models.py

Les modèles de Django sont une façon de représenter les données dans une base de données relationnelle. Nous les utilisons pour stocker et récupérer des données dans la base de données SQLite3, fournie avec Django.

### User

Les objets utilisateurs sont au cœur du système d'authentification.

Les principaux attributs de l'utilisateur par défaut sont les suivants :

- nom d'utilisateur
- mot de passe
- email
- prenom
- nom

### Timezone

```
sendingTime = models.DateTimeField(default=timezone.now)
```

Django inclut un paramètre *TIME_ZONE* dont la valeur par défaut est l'horaire 'UTC'. Il se trouve dans le fichier de configuration 'settings.py':
```
TIME_ZONE = 'UTC'
```

## Urls.py

C'est le fichier qui permet de stocker les chemins à l'aide du module *path* qui sert à récuperer des chemins et de les transformer en variable:

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

## Forms.py

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

Django gère **trois parties** distinctes du travail induit par les formulaires dans forms.py:

- préparation et restructuration des données en vue de leur présentation
- création des formulaires HTML pour les données
- réception et traitement des formulaires et des données envoyés par le client

## Admin.py

```
from django.contrib import admin
from .models import Post, UserProfile
# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
```

Le fichier admin.py sert à **enregistrer** les modèles dans le projet Django (base de donnée)

# III - Modalités de mise en oeuvre 

On utilise le langage **Python** à l’aide de son framework **Django** pour le développement back-end, puis du SQLite pour la partie base de données du réseau social.

Pour la partie front-end nous utilisons du **HTML** et du CSS à l’aide du framework **Bootstrap 5**, pour simplifier la tâche.

Ce projet sera hébergé sur la plateforme **Github** sur le référentiel ici : 

https://github.com/Projet-NSI/SocialMediaPlatform.V2

Il y sera précisé à l’aide d’un fichier *README.md* toutes les **étapes clés** de notre projet, les objectifs et les fonctionnalités. Vous pourrez suivre à l’aide de notre référentiel **la configuration du projet et son évolution**.

Vous avez **accès** à l'application ici : 

https://socialmediaplatformv2-3.simonzeru.repl.co/

# Bibliographie 

### Doc de django allauth :

https://django-allauth.readthedocs.io/en/latest/installation.html

### Stack overflow pour les erreurs par exemple : 

https://stackoverflow.com/questions/65238459/templatedoesnotexist-at-users-register-bootstrap5-uni-form-html

### Doc de Django : 

https://docs.djangoproject.com/en/4.1/

### Doc bootstrap 5 : 

https://getbootstrap.com/docs/5.0/getting-started/introduction/


### Penners django-aullauth social media template : 

https://github.com/pennersr/django-allauth

### Tuto django app : 

https://www.youtube.com/watch?v=ns7cmSaiA9E&ab_channel=Docstring

### strftime() : 

https://www.programiz.com/python-programming/datetime/strftime

### Font awesome : 

https://fontawesome.com/


