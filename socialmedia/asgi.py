"""
ASGI config for socialmedia project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings')

application = get_asgi_application()

# Le fichier asgi.py est utilisé pour déployer l'application Django 
# sur des serveurs web qui supportent l'interface ASGI (Asynchronous Server Gateway Interface), 
# tels que Daphne ou Uvicorn, qui permettent une communication asynchrone entre le serveur web et l'application Django. 
# Lorsque l'application est exécutée, le serveur ASGI importe le fichier asgi.py, 
# qui charge l'application Django et la configure. 
# Ce fichier initialise également le processus de démarrage de l'application en appelant la fonction get_asgi_application().

# Ce fichier est un point d'entrée pour les serveurs web qui permettent de déployer une application Django 