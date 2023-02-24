from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    idPost = models.AutoField(primary_key=True)
    contenu = models.TextField(max_length=1500)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sendingTime = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    comment = models.TextField()
    contenu = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sendingTime = models.DateTimeField(default=timezone.now)

    
