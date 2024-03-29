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

`LGMedia` avec Django est une application visant à créer un réseau social simpliste destiné aux lycéens du LGM, à l'aide du framework Django[^1], ce projet comportera donc de la programmation objet et une base de données.

[![Favicon-SM.png](https://i.postimg.cc/pXGLLPFH/Favicon-SM.png)](https://postimg.cc/SJ9hZFdT)

[^1]: Django peut être séparé en deux parties clés : les URLs et les vues. Ce sont deux concepts pour gérer les requêtes des utilisateurs. Les URLs sont des adresses web uniques qui identifient une vue dans votre application web. Les vues sont des fonctions Python qui répondent aux requêtes des utilisateurs et renvoient une réponse HTTP, généralement une page web.

### Langages 

Python avec Django / SQLite / HTML / CSS (Bootstrap5[^2])

[^2]: Bootstrap 5 est un framework front-end open-source qui permet de créer des interfaces utilisateur pour des sites web et des applications web. Il fournit des styles CSS pré-construits pour des éléments tels que des boutons, des formulaires, des tables, etc., ainsi que des composants JavaScript interactifs tels que des menus déroulants, des modales, des carrousels, etc. C’est très pratique pour notre projet car cela nous permet de créer rapidement et facilement des interfaces utilisateur attrayantes et cohérentes.

## Modèles

Les modèles de données comprennent les utilisateurs, les profils, les messages et les commentaires.

![Schema relationnel](https://i.ibb.co/bBVxFf0/modeles-social.png)

> Remarque : La table `User` est integrée dans Django, elle a pour clé primaire son id qui identifie l'utilisateur de manière unique, qui permet ici aux tables `Post` et `Comment` d'interagir.

### Fonctionnalités

- [x] Obtention des données de l'utilisateur
- [x] Deconnexion du compte utilisateur 
- [x] Publication de posts
- [x] Modification de posts
- [x] Suppression de posts
- [x] Création et modification de comptes utilisateur (Profil)
- [x] Commentaires sur les posts
- [x] Suppression de commentaires
- [x] Liker des posts et commentaires
- [x] Gestion des abonnements

## Points importants

- [ ] Sécurité des données utilisateur
- [x] Mise en place d'une interface utilisateur conviviale
- [x] Gestion des erreurs

## Exemple 

Un utilisateur **s'inscrit**, créé **son profil**, publie et commente un **post**, **like et dislike** des posts et commentaires et **suit d'autres utilisateurs** pour voir leurs profils.

## Pourquoi

Nous étions fascinés de voir comment marchait un réseau social et toutes les étapes à suivre pour en créer un facilement. L'idée de créer un réseau social local pour le lycée était une bonne idée. 

# II - Spécifications techniques

## Architecture client-server

L'architecture **client-server** est composée de **trois étapes** : 

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

- landing (dossier)
    - templates (dossier)
        - landing (dossier)
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
- social (dossier)
    - templates (dossier)
        - social (dossier)
            - comment_delete.html
            - post_delete.html
            - post_detail.html
            - post_edit.html
            - post_list.html
            - profile_edit.html
            - profile.html
    - admin.py
    - apps copy.py
    - tests.py
    - apps.py
    - models.py
    - urls.py
    - views.py
- socialmedia (dossier)
    - asgi.py
    - settings.py
    - urls.py
    - wsgi.py
- media (dossier)
    - uploads (dossier)
        - logos (dossier)
            ...
        - models (dossier)
            ...
        - profile_pictures (dossier)
            ...
        - post_photos (dossier)
            ...
- static (dossier)
    - style.css
- templates
    ... (django-allauth templates)
- db.sqlite3
- manage.py
- readme.md
- requirements.txt
- Procfile
- runtime.txt

> Remarque : nous avons récupéré un module `templates` en dessous qui comprends toutes les pages pré construites pour les connexions et inscriptions à l’aide de django-allauth (plusieurs grandes entreprises comme google, instagram, twitter utilisent django-allauth, c’est l’une des bibliothèque les plus efficace.)
> `socialmedia` est le nom de notre projet Django. Il comprend notamment les settings.py et les urls. 
> `landing` et `social` sont des applications de notre projet Django


# III - Modalités de mise en oeuvre 

On utilise le langage **Python** à l’aide de son framework **Django** pour le développement back-end

![Djangoproject](https://i0.wp.com/www.skysilk.com/blog/wp-content/uploads/2018/01/python-django-logo.jpg?fit=1280%2C720&ssl=1)

Puis, la base de donnée SQLite3

![SQLite3](https://sqlite.org/forum/logo?id=4ef9785e)

Pour la partie front-end nous utilisons du **HTML** et du CSS à l’aide du framework **Bootstrap 5**, pour simplifier la tâche.

![Bootstrap5](https://www.transycons.com/wp-content/uploads/2014/08/bootstrap-1.jpg)

Ce projet sera hébergé sur la plateforme **Github** sur le référentiel ici : 

https://github.com/Projet-NSI/SocialMediaPlatform.V2

Il y sera précisé à l’aide d’un fichier `README.md` toutes les **étapes clés** de notre projet, les objectifs et les fonctionnalités. Vous pourrez suivre à l’aide de notre référentiel **la configuration du projet et son évolution**.

Vous avez **accès** à l'application ici : 

https://web-production-9a97.up.railway.app/

## Démarrage du projet:

### Créer un projet Django:

Tout d'abord il fallait initialiser le projet django, créer un environnement virtuel (pour faciliter le transfert des modules), installer des modules (tels que *django allauth*, *Crispy Form* etc..) puis créer notre application `landing` ou on mettra nos pages HTML primaires (`base.html`, `index.html` et `navbar.html`) 

https://docs.djangoproject.com/en/4.2/

## Optemption des données de l'utilisateur :

### Django Allauth

Nous utilisons django-allauth[^3] pour les récupérations des données. 

[^3]: Django-allauth est un package de Django qui fournit des fonctionnalités
d'authentification pour les utilisateurs. Il inclut des formulaires de création de compte, de
connexion, de récupération de mot de passe, et des pages HTML pour gérer les
comptes d'utilisateurs. Cela nous est très utile pour notre réseau social qui nécessite des fonctionnalités d'authentification et de gestion des utilisateurs.


- Nous avons configuré les urls pour bien acheminer les pages
- Nous avons importé la classe User déjà existante dans Django 
- Nous avons migré les modèles dans la base de donnés
- Puis nous avions juste à styliser la page à l'aide de Boostrap5 et de CrispyForm

## Publication de posts:
 
C'est la fonctionnalité principale de notre application, c'est la page que l'on voit en premier après s'être authentifier

### Création de l'application social:

Pour des raisons d'organisation et de propreté, nous avons décidés de créer une application extérieure nommée `Social` sera mis toutes les autres fonctionnalités du réseau social. 

## Création du modèle Post

`Post` est un modèle Django pour stocker les publications.

```
class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    sendingTime = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
```

> Remarques : l'option `blank=True` est un paramètre que l'on peut ajouter aux champs de modèles pour spécifier que le champ peut être laissé vide dans le formulaire de création ou de modification d'objet.

> l'option `null=True` dans un champ de modèle indique que la valeur de ce champ peut être nulle dans la base de données.

### Pages HTML

Dans cette application, nous allons créer un dossier `Template` puis à l'interieur un dossier `social` pour gérer les pages HTML. Dans ce dossier, nous allons créer la page `post_list.html` qui comprendra le formulaire pour poster le message des utilisateurs puis la liste des posts triés par la date d'envoi.

Nous complèterons la page après avoir fini la création du formulaire et les fontions dans les vues. 

### Création du formulaire

Dans Django, nous avons la possibilité de créer des formulaires à l'aide du module forms, permettant de relier les attributs des tables (des modèles) aux formulaires. 

Nous l'utiliserons ensuite dans notre page HTML. 

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

La classe `Meta` defini le modèle et les attributs correspondants pour la base de donnée.

### Création de la vue

Il faut créer la `PostListView`, qui hérite de la classe générique de Django `View` permettant d'utiliser les méthodes `get` et `post`.

```
class PostListView(View): 
    ...
```

La classe `PostListView` est une vue qui gère l'affichage et l'envoi de messages (`Post`) sur la plateforme sociale.

La méthode `get` est utilisée pour récupérer tous les messages (`Post`) de la base de données et les afficher dans un contexte qui sera rendu dans le template `social/post_list.html`. Elle instancie également un formulaire vide `PostForm` pour permettre aux utilisateurs d'ajouter de nouveaux messages.

```
def get(self, request, *args, **kwargs): #args et kwargs permettent de passer plusieurs arguments ou des arguments de mots-clés à une fonction
        # récupère tous les objets Post dans la base de données, les trie par date d'envoi et les stocke dans la variable posts
        posts = Post.objects.all().order_by('-sendingTime') # SELECT * FROM Post ORDER BY sendingTime
        # initialise un formulaire vide pour créer un nouveau post
        form = PostForm() 
        #stocke les variables dans le dico 'contexte'
        context = {
            'post_list': posts,
            'form': form,
        }
        # retourne la requête client, la page modifiée et le contexte
        return render(request, 'social/post_list.html', context)
```

La méthode `post` est utilisée lorsque l'utilisateur envoie un formulaire pour ajouter un nouveau message (`Post`). Elle vérifie que le formulaire est valide, instancie un nouvel objet `Post` avec les données valides et l'associe à l'utilisateur connecté avant de l'enregistrer dans la base de données. Elle réaffiche ensuite la liste des messages avec le formulaire actualisé.

```
def post(self, request, `args, ``kwargs):
        posts = Post.objects.all().order_by('-sendingTime')
        form = PostForm(request.POST, request.FILES) # réinitialiser le formulaire après l'enregistrement réussi
        

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auteur = request.user
            new_post.contenu = form.cleaned_data.get('contenu')
            new_post.save()
```
> Remarque : la fonction `is_valid()` permet de verifier si le formulaire est propre.

Nous devons maintenant créer la page HTML `post_list` puis utiliser la fonction `render()` pour retourner la requête client, la page actuelle et le contexte (les variables utilisées).

```
return render(request, 'social/post_list.html', context)
```

Il nous reste plus qu'à configurer l'URL dans les `urls.py` pour indiquer le chemin à Django (sans oublier d'importer la vue): 

```
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    ...
]
```
> Remarque : le chemin n'a pas besoin d'être complété car ce sera la page d'accueil lorsque l'utilisateur se connecte.

## Commentaires sur les posts:

### Modèle

Le modèle `Comment` est utilisé pour stocker les commentaires dans l'application. 

```
class Comment(models.Model):
    comment = models.TextField()
    contenu = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sendingTime = models.DateTimeField(default=timezone.now)
```

### Formulaire

La classe `CommentForm` est un formulaire pour créer un commentaire, et elle contient un champ pour le texte du commentaire. Elle est liée au modèle `Comment`, de sorte que lorsque le formulaire est soumis, il crée un nouvel objet `Comment` avec le texte du commentaire entré par l'utilisateur.

```
class CommentForm(forms.ModelForm):
    '''Champs des commentaires'''
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '3',
                   'placeholder': 'Dites quelque chose...'}
        ))

    class Meta:
        '''Etabli le modèle du formulaire pour sauvegarder les champs dans la base de données'''
        model = Comment
        fields = ['comment']  
```

Nous utilisons la page `post_detail.html` pour afficher les détails d'une publication, y compris ses commentaires. Elle contiendra le formulaire `CommentForm`.

Il reste plus qu'à indiquer l'URL dans les urls.py :

```
urlpatterns = [
    ...
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
```

## Mise à jour des posts:

Nous héritons des classes de Django : UpdateView, LoginRequiredMixins et UserPassesTestMixin pour créer la vue. 

Dans Django, une vue est une fonction ou une classe qui prend une requête HTTP et renvoie une réponse HTTP. L'utilisation de la vue `UpdateView` permet de mettre à jour un modèle existant dans la base de données à travers un formulaire. Dans cet extrait de code, la vue PostEditView est utilisée pour mettre à jour le contenu de l'objet Post. Elle hérite des fonctionnalités de `LoginRequiredMixin` et `UserPassesTestMixin` pour vérifier que l'utilisateur est connecté et qu'il est bien l'auteur de la publication qu'il souhaite modifier. Les champs à mettre à jour sont spécifiés dans l'attribut `fields`, et la méthode `get_success_url()` redirige l'utilisateur vers la page de détails de la publication mise à jour.

```
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post # On défini le modèle de l'objet modifié
    fields = ['contenu'] # On défini l'attribut du modèle de l'objet modifié
    template_name = 'social/post_edit.html' # sert à spécifier le nom de la page modèle à utiliser pour afficher la page d'édition des publications (Post). 
    
    # méthode de la classe UpdateView appelée lorsque la mise à jour d'un objet est réussie. Dans ce cas, elle redirige l'utilisateur vers la vue de détail de l'objet mis à jour, ici post_detail.
    def get_success_url(self):
         # Clé primaire du post mis à jour
        pk = self.kwargs['pk']

        # génére (ou retourne) l'URL de redirection en utilisant le nom relatif de l'URL
        return reverse_lazy('post-detail', kwargs={'pk': pk})
        # L'identifiant du post doit être inclus dans l'URL de redirection, car la vue de détail du post est la page à laquelle l'utilisateur sera redirigé après avoir mis à jour son post.
        # Cela garantit que l'utilisateur sera redirigé vers la bonne page après la mise à jour du post.

    def test_func(self): # Vérifie si l'utilisateur est autorisé à effectuer l'action à l'aide de la méthode test_func
        post = self.get_object() # récupère le post
        return self.request.user == post.auteur # vérifie si l'auteur est bien l'utilisateur
```

> `UserPassesTextMixins` permet d'utiliser la méthode `test_func` pour verifier qu'uniquement l'utilisateur du post puisse le modifier. 

> la classe `LoginRequiredMixins` permet d'afficher une erreur si l'utilisater n'est pas connecté.

Nous utilisons la page HTML `post_edit.html` pour afficher le formulaire de mise à jour de publication.

Il nous reste plus qu'à configurer l'url :

```
urlpatterns = [
    ...
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    ...
]
```

## Suppression de posts/commentaires:

Les vues Django `DeleteView` sont utilisées pour supprimer des objets de la base de données. Dans ce cas, la classe `PostDeleteView` et la classe `CommentDeleteView` sont utilisées respectivement pour supprimer des publications et des commentaires. Le modèle associé à chaque vue est défini par la variable `model`. Les templates correspondants pour confirmer la suppression sont spécifiés par `template_name`. La redirection après la suppression réussie est spécifiée par `success_url` pour `PostDeleteView` et `get_success_url` pour `CommentDeleteView`. La fonction `test_func` permet de s'assurer que seuls les auteurs des publications et des commentaires peuvent les supprimer.

### Suppression de posts

La vue `PostDeleteView` est une vue basée sur une classe dans Django qui permet de supprimer un objet de type Post de la base de données. Cette vue nécessite que l'utilisateur soit authentifié et qu'il ait la permission de supprimer le `post` en question.
```
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # On défini le modèle de l'objet modifié
    model = Post
    # template_name sert à spécifier le nom de la page modèle à utiliser pour afficher la page d'édition des publications (Post). 
    template_name = 'social/post_delete.html'
    # après la suppression d'un Post, l'utilisateur sera redirigé vers la liste des Posts.
    success_url = reverse_lazy('post-list')
    # reverse_lazy() est utilisée pour obtenir l'URL à partir du nom relatif de l'URL.

    def test_func(self): #test de vérification
        post = self.get_object()
        return self.request.user == post.auteur
```

Elle utilise le modèle `Post` pour récupérer l'objet à supprimer à partir de son identifiant (`pk`), et affiche un formulaire de confirmation avant de supprimer définitivement le post de la base de données.

La vue redirige ensuite l'utilisateur vers la page d'accueil du site (`success_url = reverse_lazy('post-list')`). Si l'utilisateur annule la suppression, il est redirigé vers la page de détails du post (`get_success_url`).

Nous utilisons la page `post_delete.html` pour afficher la demande de suppresion du post.

Il nous reste plus qu'à configurer l'url :

```
urlpatterns = [
    ...
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    ...
]
```

### Suppression de commmentaires

La vue `CommentDeleteView` est une vue de suppression qui permet de supprimer un commentaire existant sur un `post`. Elle hérite de la classe générique Django `DeleteView`. Cette vue nécessite une connexion utilisateur pour être accessible grâce à l'utilisation de `LoginRequiredMixin`.

Dans la méthode `get_success_url()`, nous récupérons l'identifiant du `post` lié au commentaire supprimé grâce à `self.kwargs['post_pk']`. Puis, nous créons une URL pour afficher les détails de ce `post à l'aide de la fonction `reverse_lazy()` et nous passons l'identifiant du post en tant que paramètre.

```
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk'] # récupére l'identifiant du post à partir duquel l'utilisateur a supprimé un commentaire.
        
        # nous créons une URL en utilisant la fonction reverse_lazy. Cette URL est générée à partir du nom relatif de l'URL (post-detail)
        return reverse_lazy('post-detail', kwargs={'pk': pk}) 
        # L'identifiant du post doit être inclus dans l'URL de redirection, car la vue de détail du post est la page à laquelle l'utilisateur sera redirigé après avoir supprimé le commentaire.
        
        # Cela garantit que l'utilisateur sera redirigé vers la bonne page après la suppression du commentaire.
```

Lorsque l'utilisateur clique sur le bouton de suppression, la méthode `delete()` est appelée pour supprimer l'objet commentaire de la base de données. Enfin, l'utilisateur est redirigé vers la page des détails du post en question grâce à l'utilisation de la fonction `HttpResponseRedirect()`.

Nous utilisons la page `comment_delete.html` pour afficher la demande de suppression du commentaire.

Il nous reste plus qu'à configurer l'url :

```
urlpatterns = [
    ...
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    ...
]
```

## Création de Profil :

### Modèle

`UserProfile` est le modèle pour stocker les profils.

```
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date=models.DateField(null=True, blank=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
```

> Remarques : Les OneToOneFields() sont l'opposé des ManyToManyFields() puisqu'il ne peut y avoir qu'un profil pour chaques utilisateurs, soit une relation (1,1).

### Décorateurs 

Les décorateurs sont des fonctions qui prennent une autre fonction en argument et étendent le comportement de cette fonction sans la modifier explicitement. Dans cet exemple de modèle pour les profils des utilisateurs, les décorateurs sont utilisés pour définir des actions à effectuer avant ou après la création ou la mise à jour d'un objet User.

Le premier décorateur @receiver(post_save, sender=User) est appelé après la sauvegarde d'un objet User et crée un UserProfile associé à cet utilisateur s'il n'existe pas déjà.

Le deuxième décorateur @receiver(post_save, sender=User) est appelé après la sauvegarde d'un objet User et met à jour le profil associé à cet utilisateur.

```
@receiver(post_save, sender=User) #décorateur de Django
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User) #décorateur de Django
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
```

> Remarques : `sender` est le modèle envoyant le signal. Dans ce cas-ci, User est le modèle qui envoie le signal. Par conséquent, `sender=User`.

> `instance` est l'instance du modèle qui vient d'être sauvegardé. Par exemple, lorsqu'un nouvel utilisateur est créé, l'instance `User` nouvellement créée est passée à la fonction de rappel.

> `created` est un booléen qui indique si une nouvelle instance du modèle vient d'être créée (`created=True`) ou si une instance existante vient d'être mise à jour (`created=False`).

instance : l'instance du modèle qui vient d'être sauvegardé. Par exemple, lorsqu'un nouvel utilisateur est créé, l'instance User nouvellement créée est passée à la fonction de rappel.

created : un booléen qui indique si une nouvelle instance du modèle vient d'être créée (created=True) ou si une instance existante vient d'être mise à jour (created=False). Par exemple, lorsqu'un nouvel utilisateur est créé, created=True est passé à la fonction de rappel, tandis que lorsqu'un utilisateur existant est mis à jour, created=False est passé.

Ces décorateurs sont basés sur une fonction de réception, qui est appelée lorsque l'événement spécifié se produit. La fonction create_user_profile crée un nouveau profil d'utilisateur en utilisant l'objet User qui vient d'être créé, et la fonction save_user_profile enregistre les modifications apportées à l'objet User en mettant à jour le profil associé.

En utilisant ces décorateurs, l'application peut s'assurer que les profils des utilisateurs sont toujours créés et mis à jour correctement chaque fois qu'un objet User est créé ou modifié.

### Création de la vue

La vue `ProfileView` permet de récupérer et d'afficher les informations liées au profil d'un utilisateur en particulier.

```
class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk) # SELECT * FROM UserProfile WHERE user = pk
        user = profile.user # on récupère l''utilisateur du profil
        posts = Post.objects.filter(auteur=user).order_by('-sendingTime') # SELECT * FROM Post WHERE auteur = user ORDER BY sendingTime
        abonnes = profile.followers.all() # liste de tout les abonnés de du profil
        total_abonnes = len(abonnes) # nombre total d'abonnés, soit la longueur de la liste

        est_abonne = False 
        # On parcours la liste des abonnés pour savoir si l'utilisateur est abonné au profil
        for abonne in abonnes:
            if abonne == request.user:
                est_abonne =  True
                break

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'total_abonnes': total_abonnes,
            'est_abonne': est_abonne,
        }

        return render(request, 'social/profile.html', context)
```

Elle utilise l'objet `UserProfile` qui est lié à l'utilisateur grâce à la clé étrangère `user` pour récupérer le profil en question. Ensuite, elle récupère tous les posts écrits par cet utilisateur en les filtrant à l'aide de la méthode `filter` de l'objet `Post`. La vue récupère également la liste des abonnés du profil et calcule le nombre total d'abonnés. Enfin, elle vérifie si l'utilisateur connecté est abonné au profil en question et retourne toutes ces informations dans le contexte pour être utilisées dans le template `profile.html`.

Nous devons créer la page `profile.html` pour afficher le profil de l'utilisateur.

Il nous reste plus qu'à configurer l'url :

```
urlpatterns = [
    ...
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    ...
]
```

## Mise à jour de profils

Un utilisateur doit évidemment avoir la possibilité de modifier son profil (sa bio, photo de profil, etc.)

### Création de la vue 

La vue `ProfileEditView` prends le même principe que les modifications de posts et commentaires

```
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile 
    fields = ['name', 'bio', 'birth_date', 'location', 'picture'] 
    template_name = 'social/profile_edit.html'

    # méthode de la classe UpdateView appelée lorsque la mise à jour du profil est réussie. Dans ce cas, elle redirige l'utilisateur vers le profil.
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self): #test de vérification
        profile = self.get_object()
        return self.request.user == profile.user
```

Nous devons créer la page `profile_edit.html` pour afficher le profil de l'utilisateur.

Il nous reste plus qu'à configurer l'url :

```
urlpatterns = [
    ...
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    ...
]
```

## Liker/Disliker des posts et commentaires:

### Mise à jour des modèles `Post` et `Comment`

Nous devons rajouter les likes et les dislikes sous forme de clès étrangères `ManyToManyFields()`, qui peuvent contenir plusieurs tables `User`.

```
class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
    sendingTime = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

class Comment(models.Model):
    comment = models.TextField()
    contenu = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sendingTime = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
```

> Remarques : Les `ManyToManyFields()` sont un type de champ de modèle dans Django qui permettent de créer une relation many-to-many entre deux modèles. Cela signifie qu'un élément dans le premier modèle peut être lié à plusieurs éléments dans le deuxième modèle, et vice versa. C'est comme une relation (0,n) avec la table User. Les `OneToOneFields()` sont donc l'opposé des ManyToManyFields().

> Le paramètre `related_name='likes'` est utilisé pour spécifier le nom de l'attribut qui sera utilisé pour accéder à la liste des posts qui ont été 'likés' par un utilisateur spécifique. Ce paramètre est obligatoire car il y a plusieurs clés étrangères ManyToMany entre les modèles User et Comment.

### Création de la vue

Les vues permettent à un utilisateur connecté de "liker" ou "disliker" un post. La vue `Like` est appelée lorsqu'un utilisateur clique sur le bouton "Like" d'un post, et la vue `Dislike` est appelée lorsqu'il clique sur le bouton "Dislike". Dans chaque vue, la méthode `post` est utilisée pour traiter la demande POST envoyée par le formulaire.

```
class Like(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk) # SELECT * FROM Post WHERE idPost = pk

        dislikes = post.dislikes.all() # liste de tous id des utilisateurs qui ont dislike
        has_disliked = False
        # On vérifie si l'utilisateur actuel a disliker
        for dislike in dislikes:
            if dislike == request.user:
                has_disliked = True
                break
        # Si oui on le supprime de la liste car sinon il pourrait liker et disliker en même temps
        if has_disliked:
            post.dislikes.remove(request.user)

        # Même principe pour les likes
        likes = post.likes.all()
        has_liked = False

        for like in likes:
            if like == request.user:
                has_liked = True
                break
        # Si il n'a pas liker, on l'ajoute dans la liste sinon on le supprime de celle-ci
        if not has_liked:
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)

        # permet de récupérer l'URL de redirection (next) après que l'utilisateur ait effectué l'action de "like"
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next) # redirige l'utilisateur vers une autre page, si next est vide, on redirige l'utilisateur vers la page précédente (modifiée)

        # Plus précisément, cette ligne de code récupère la valeur associée à la clé "next" dans le dictionnaire de requête POST. 
        
        # Si la clé "next" n'est pas présente dans le dictionnaire de requête POST, la valeur par défaut "/" est retournée, qui est l'URL de la page d'accueil.

        # Par conséquent, si l'utilisateur est déjà sur une page spécifique (par exemple, la page de détails d'un post) et qu'il aime ce post, il sera redirigé vers la même page après avoir effectué l'action de "like".
```

Chacune de ces vues récupère le post correspondant en utilisant l'ID du post dans l'URL, puis vérifie si l'utilisateur connecté a déjà aimé ou non ce post. Si l'utilisateur a déjà aimé ou pas aimé, l'association entre l'utilisateur et le post est modifiée en conséquence en ajoutant ou en supprimant l'utilisateur de la liste des utilisateurs qui ont aimé ou n'ont pas aimé le post. La méthode `get_next()` est utilisée pour rediriger l'utilisateur vers la page d'origine.

Pour les likes et dislikes des Commentaires, le principe reste le même, il faut juste récuperer les commentaires et non les posts.

Il nous reste plus qu'à configurer les urls :

```
urlpatterns = [
    ...
    path('post/<int:post_pk>/comment/<int:pk>/like', CommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', CommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:pk>/like', Like.as_view(), name='like'),
    path('post/<int:pk>/dislike', Dislike.as_view(), name='dislike'),
    ...
]
```

## Gestion des abonnements:

### Mise à jour du modèle `UserProfile` 

Nous devons rajouter les followers sous forme de clès étrangères `ManyToManyFields()`, qui peuvent contenir plusieurs tables `User`.

```
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	birth_date=models.DateField(null=True, blank=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
	followers = models.ManyToManyField(User, blank=True, related_name='followers')
```

### Création des vues 

Les vues "AddFollower" et "RemoveFollower" sont des vues qui permettent d'ajouter ou de supprimer un abonnement à un utilisateur.

La vue "AddFollower" récupère le profil de l'utilisateur à partir de son identifiant, ajoute l'utilisateur connecté à la liste des abonnés du profil et redirige vers la page de profil. 

```
class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk) # SELECT * FROM UserProfile WHERE user = pk

        # La méthode add() est une méthode de l'objet ManyToManyField utilisée pour ajouter un objet à une relation Many-to-Many. 
        profile.followers.add(request.user) #ajout de l'utilisateur qui a fait la requête dans les abonnés du profil
        
        # Dans ce cas, profile.followers représente la relation ManyToManyField définie dans le modèle Profile, qui relie un profil à plusieurs utilisateurs qui le suivent.
        
        return redirect('profile', profile.pk)
        # redirige l'utilisateur vers la page du profil de l'utilisateur qu'il vient de suivre.
```

La vue "RemoveFollower" fonctionne de manière similaire, mais elle retire l'utilisateur connecté de la liste des abonnés du profil.

```
class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk) # SELECT * FROM UserProfile WHERE user = pk
        profile.followers.remove(request.user) #Fonction de Django déjà faite pour retirer des abonnements

        return redirect('profile', pk=profile.pk)
```

Il nous reste plus qu'à configurer les urls :

```
urlpatterns = [
    ...
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower')
]
```

## Syntaxe Django dans les pages HTML

Pour mettre des commandes python, il faut encadrer la ligne de code par `{% ... %}`
```
{% for post in post_list %}
...
{% endfor %}
```
> Remarque : Il faut toujours indiquer la fin des boucles ou conditions, comme en langage naturel

Il faut indiquer le placement du contenu au début et à la fin de chaques pages HTML:
```
<body>
    {% block content %}
    ...
    {% endblock content %}
</body>
```

### Extension et Inclusion des pages HTML 

#### Extension

Nous pouvons étendre notre fichier parent nommé `base.html` pour le séparer en plusieurs fichier 
```
{% extends 'landing/base.html' %}
```

#### Inclusion

Pour qu'un fichier reste affiché dans toutes nos pages html,
il faut l'inclure dans la base:
```
{% include 'landing/navbar.html' %}
```
> Remarque : Dans notre réseau social, il faut laisser la navbar affichée partout.

Pour le style, nous pouvons directement utiliser les classes *Bootstrap* : 
```
<div class="row justify-content-center mt-3">
```

Les classes css sont importées dans la `base.html` : 
```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" ...>
```

Pour les variables python, il faut encadrer par `{{ ... }}`
```
<p>{{ post.contenu }}</p>
```

Pour les urls, il faut écrire {% url 'nom_de_l'url' cle_primaire %}
```
<a href="{% url 'profile' post.auteur.profile.pk %}">
```

### Static

Pour les images et les fichier css, nous sommes obligé de charger `static` (module) au début de chaques pages HTML utilisant des images:
```
{% load static %}
```

### CrispyForms

Nous devons aussi charger le module de style pour les formulaires
```
{% load crispy_forms_tags %}
```

### Améliorations possibles 

- Notifications
- Recherche d'utilisitateurs à suivre
- Page d'accueil présentant uniquement les posts des abonnements de l'utilisateur
- Threads
- Algorithme de recommendation d'utilisateurs à suivre

**Nous vous enverrons par l'ent la partie d'explication des modules.**

# IV - Bibliographie 

### Doc Django Project Mozilla : 

https://developer.mozilla.org/fr/docs/Learn/Server-side/Django

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

### Railway:

https://railway.app/

https://alphasec.io/how-to-deploy-a-python-django-app-on-railway/

### Django redirects:

https://realpython.com/django-redirects/






