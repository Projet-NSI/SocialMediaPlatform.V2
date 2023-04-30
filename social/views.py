from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


# Vue de la liste des posts qui hérite de la classe View
class PostListView(View): 
    
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
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-sendingTime') # SELECT * FROM Post ORDER BY sendingTime
        # récupère le formulaire soumis
        form = PostForm(request.POST, request.FILES)
        
        #valide le formulaire
        if form.is_valid():
            new_post = form.save(commit=False) # crée un nouvel objet Post avec les données soumises
            new_post.auteur = request.user # associe à l'utilisateur qui a soumis le formulaire
            new_post.contenu = form.cleaned_data.get('contenu')
            new_post.save() #enregistre le Post dans la base de données
        
        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)

# Vue pour les détails des posts qui hérite de la classe View et LoginRequiredMixin
class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        # récupère l'objet Post avec l'ID spécifié dans l'URL
        post = Post.objects.get(pk=pk) # SELECT * FROM Post WHERE idPost = pk
        # initialise un formulaire vide pour créer un nouveau post
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-sendingTime') #SELECT * FROM Comment ORDER BY sendingTime

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk) # SELECT * FROM Post WHERE idPost = pk
        # récupère le formulaire soumis
        form = CommentForm(request.POST)
        # on valide le formulaire
        if form.is_valid():
            new_comment = form.save(commit=False) # crée un nouvel objet Comment avec les données soumises
            new_comment.auteur = request.user #on l'associe à l'utilisateur qui a soumis le formulaire
            new_comment.post = post #on l'associe également à l'objet Post correspondant
            new_comment.save() #Sauvegarde le commentaire dans la base de données
        
        comments = Comment.objects.filter(post=post).order_by('-sendingTime') 
        # SELECT post FROM Comment where post = post ORDER BY sendingTime

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

# Vue pour les modifications de posts qui hérite des classes Django UpdateView, LoginRequiredMixin et UserPassesTestMixin

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post # On défini le modèle de l'objet modifié
    fields = ['contenu', 'image'] # On défini l'attribut du modèle de l'objet modifié
    template_name = 'social/post_edit.html' 
    # template_name sert à spécifier le nom de la page modèle à utiliser pour afficher la page d'édition des publications (Post). 
    
    # méthode de la classe UpdateView appelée lorsque la mise à jour d'un objet est réussie. 
    # Dans ce cas, elle redirige l'utilisateur vers la vue de détail de l'objet mis à jour, ici post_detail.
    def get_success_url(self):
         # Clé primaire du post mis à jour
        pk = self.kwargs['pk']

        # génére (ou retourne) l'URL de redirection en utilisant le nom relatif de l'URL
        return reverse_lazy('post-detail', kwargs={'pk': pk})
        # L'identifiant du post doit être inclus dans l'URL de redirection, 
        # car la vue de détail du post est la page à laquelle l'utilisateur sera redirigé après avoir mis à jour son post.
        # Cela garantit que l'utilisateur sera redirigé vers la bonne page après la mise à jour du post.

    def test_func(self): # Vérifie si l'utilisateur est autorisé à effectuer l'action à l'aide de la méthode test_func
        post = self.get_object() # récupère le post
        return self.request.user == post.auteur # vérifie si l'auteur est bien l'utilisateur

# Vue pour supprimer un post qui hérite des classes Django DeleteView, LoginRequiredMixin et UserPassesTestMixin
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
# Vue pour supprimer un commentaire, qui hérite des mêmes classes Django que la vue pour supprimer un post
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        # récupére l'identifiant du post à partir duquel l'utilisateur a supprimé un commentaire.
        pk = self.kwargs['post_pk'] 
        
        # nous créons une URL en utilisant la fonction reverse_lazy. Cette URL est générée à partir du nom relatif de l'URL (post-detail)
        return reverse_lazy('post-detail', kwargs={'pk': pk}) 
        # L'identifiant du post doit être inclus dans l'URL de redirection, car la vue de détail du post est la page à laquelle l'utilisateur sera redirigé après avoir supprimé le commentaire.
        
        # Cela garantit que l'utilisateur sera redirigé vers la bonne page après la suppression du commentaire.
    
    def test_func(self): # test de vérification
        comment = self.get_object()
        return self.request.user == comment.auteur

# Vue pour les profils des utilisateurs qui hérite de la classe Django View
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

# Vue pour éditer les profils qui hérite des memes classes Django que les modifications et supression de posts
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

# Vue pour ajouter un abonnement qui hérite des classes Django View et LoginRequiredMixin
class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk) # SELECT * FROM UserProfile WHERE user = pk

        # La méthode add() est une méthode de l'objet ManyToManyField utilisée pour ajouter un objet à une relation Many-to-Many. 
        profile.followers.add(request.user) #ajout de l'utilisateur qui a fait la requête dans les abonnés du profil
        
        # Dans ce cas, profile.followers représente la relation ManyToManyField définie dans le modèle Profile, qui relie un profil à plusieurs utilisateurs qui le suivent.
        
        return redirect('profile', profile.pk)
        # redirige l'utilisateur vers la page du profil de l'utilisateur qu'il vient de suivre.

# Vue pour retirer un abonnement qui hérite des classes Django View et LoginRequiredMixin
class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk) # SELECT * FROM UserProfile WHERE user = pk
        profile.followers.remove(request.user) #Fonction de Django déjà faite pour retirer des abonnements

        return redirect('profile', pk=profile.pk)

# Vue pour ajouter un J'aime sur un post
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

# Vue pour ajouter un dislike sur un post
class Dislike(LoginRequiredMixin, View):
    # même principe que la vue Like
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        likes = post.likes.all()
        has_liked = False
        for like in likes:
            if like == request.user:
                has_liked = True
                break

        if has_liked:
            post.likes.remove(request.user)

        dislikes = post.dislikes.all()
        has_disliked = False

        for dislike in dislikes:
            if dislike == request.user:
                has_disliked = True
                break

        if not has_disliked:
            post.dislikes.add(request.user)
        else:
            post.dislikes.remove(request.user)
        
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

# Vue pour ajouter un J'aime sur un commentaire
class CommentLike(LoginRequiredMixin, View):
    # même principe que la vue Like
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        dislikes = comment.dislikes.all()
        has_disliked = False

        for dislike in dislikes:
            if dislike == request.user:
                has_disliked = True
                break
        
        if has_disliked:
            comment.dislikes.remove(request.user)

        likes = comment.likes.all()
        has_liked = False

        for like in likes:
            if like == request.user:
                has_liked = True
                break
        
        if not has_liked:
            comment.likes.add(request.user)
        else:
            comment.likes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

# Vue pour ajouter un dislike sur un commentaire
class CommentDislike(LoginRequiredMixin, View):
    # même principe que la vue Like
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        likes = comment.likes.all()
        has_liked = False
        for like in likes:
            if like == request.user:
                has_liked = False
                break

        if has_liked:
            comment.likes.remove(request.user)

        dislikes = comment.dislikes.all()
        has_disliked = False

        for dislike in dislikes:
            if dislike == request.user:
                has_disliked = True
                break

        if not has_disliked:
            comment.dislikes.add(request.user)
        else:
            comment.dislikes.remove(request.user)
        
        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)