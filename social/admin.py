from django.contrib import admin
from .models import Post, UserProfile, Comment

# On enregistre les objets des tables pour que l'admin puisse modifier la base de donnée comme bon lui semble

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)