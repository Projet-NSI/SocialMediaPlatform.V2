from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

class PostListView(View):
    def get(self, request, *args, **kwargs): #permettent de passer plusieurs arguments ou des arguments de mots-clés à une fonction
        posts = Post.objects.all().order_by('-sendingTime')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-sendingTime')
        form = PostForm(request.POST, request.FILES) # réinitialiser le formulaire après l'enregistrement réussi
        

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.auteur = request.user
            new_post.contenu = form.cleaned_data.get('contenu')
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-sendingTime') #SELECT * FROM Comment ORDER BY sendingTime

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.auteur = request.user
            new_comment.post = post 
            new_comment.save() #Sauvegarde les attributs dans la base de données
        
        comments = Comment.objects.filter(post=post).order_by('-sendingTime')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['contenu']
    template_name = 'social/post_edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.auteur

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.auteur

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'social/comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.auteur

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(auteur=user).order_by('-sendingTime')
        abonnes = profile.followers.all()
        total_abonnes = len(abonnes)

        est_abonne = False

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

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user) #Fonction de Django déjà faite pour ajouter des abonnements

        return redirect('profile', profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user) #Fonction de Django déjà faite pour retirer des abonnements

        return redirect('profile', pk=profile.pk)

class Like(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        dislikes = post.dislikes.all()
        has_disliked = False

        for dislike in dislikes:
            if dislike == request.user:
                has_disliked = True
                break
        
        if has_disliked:
            post.dislikes.remove(request.user)

        likes = post.likes.all()
        has_liked = False

        for like in likes:
            if like == request.user:
                has_liked = True
                break
        
        if not has_liked:
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)

class Dislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        likes = post.likes.all()
        has_liked = False
        for like in likes:
            if like == request.user:
                has_liked = False
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

class CommentLike(LoginRequiredMixin, View):
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

class CommentDislike(LoginRequiredMixin, View):
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