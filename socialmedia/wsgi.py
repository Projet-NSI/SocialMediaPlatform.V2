"""
WSGI config for socialmedia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Déterminez si nous sommes sur la branche gh-pages
on_ghpages_branch = 'gh-pages' in os.environ.get('GITHUB_REF', '')

# Si nous sommes sur la branche gh-pages, utilisez les paramètres spécifiques à gh-pages
if on_ghpages_branch:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings_ghpages')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialmedia.settings')

application = get_wsgi_application()


