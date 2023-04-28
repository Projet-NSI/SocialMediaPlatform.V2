"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# URLS du projet
urlpatterns = [
    path('admin/', admin.site.urls), # Sur le chemin localhost:8000/admin, l'admin aura accès aux paramètres de l'application
    path('', include('landing.urls')), # On a créer un fichier urls.py dans l'application landing pour faciliter les chemins relatifs, et include permet de relier les urls
    path('accounts/', include('allauth.urls')), # On a créer un fichier urls.py dans l'application allauth pour faciliter les chemins relatifs, et include permet de relier les urls
    path('social/', include('social.urls')), # On a créer un fichier urls.py dans l'application social pour faciliter les chemins relatifs, et include permet de relier les urls
]

# Debogage
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)