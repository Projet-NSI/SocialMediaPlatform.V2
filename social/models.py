from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    contenu = models.TextField(max_length=1500)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    sendingTime = models.DateTimeField(default=timezone.now)
    

    
