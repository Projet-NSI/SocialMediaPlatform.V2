from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm
# Create your views here.

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-sendingTime')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'social/post_list.html', context)
    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-sendingTime')
        form = PostForm(request.POST) # réinitialiser le formulaire après l'enregistrement réussi

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


