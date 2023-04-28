"""
WSGI config for socialmedia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings')

application = get_wsgi_application()

# Le fichier wsgi.py est utilisé pour déployer l'application Django sur des serveurs web traditionnels,
# tels que Apache ou Nginx, qui supportent l'interface WSGI (Web Server Gateway Interface). 
# Lorsque l'application est exécutée, le serveur WSGI importe le fichier wsgi.py, 
# qui charge l'application Django et la configure. 
# Ce fichier initialise également le processus de démarrage de l'application en appelant la fonction get_wsgi_application().

# Ce fichier est un point d'entrée pour les serveurs web qui permettent de déployer une application Django 

