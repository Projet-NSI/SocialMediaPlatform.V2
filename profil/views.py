from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View


class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
# def index(request):
#     return render(request, 'landing/index.html', context={})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connexion de l'utilisateur
            login(request, user)
            return redirect('home') # Redirection page d'accueil
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Connexion de l'utilisateur
            user = form.get_user()
            login(request, user)
            return redirect('home') # Redirection page d'accueil
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login') # Redirection page d'accueil
