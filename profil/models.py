from django.db import models


class User(models.Model):
    idUser = models.PositiveIntegerField(primary_key=True)
    nom = models.CharField(max_length=26)
    prenom = models.CharField(max_length=26)
    mail = models.EmailField()
    mdp = models.CharField(max_length=100)
    dateInscription = models.DateTimeField()
    dateNaissance = models.DateField()

class Profile(models.Model):
    pseudo = models.CharField(max_length=40)
    pdp = models.ImageField()
    description = models.TextField(max_length=300)
    abonnements = models.PositiveBigIntegerField()
    abonnes = models.PositiveBigIntegerField()
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

class Abonnement(models.Model):
    idSubscription = models.PositiveIntegerField()
    pseudo = models.CharField(max_length=40)

class User_Subscription(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idSubscription = models.ForeignKey(Abonnement, on_delete=models.CASCADE)

class Abonne(models.Model):
    idSubscriber = models.PositiveIntegerField()
    pseudo = models.CharField(max_length=40)

class User_Subscriber(models.Model):
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idSubscriber = models.ForeignKey(Abonne, on_delete=models.CASCADE)

class Post(models.Model):
    idPost = models.PositiveIntegerField()
    contenu = models.TextField(max_length=1500)
    lienExterne = models.AutoField(default=None)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveBigIntegerField()
    comments = models.PositiveBigIntegerField()
    sendTime = models.DateTimeField()
    
class Commentaire(models.Model):
    idComment = models.PositiveIntegerField()
    contenu = models.TextField(max_length=1000)
    likes = models.PositiveBigIntegerField()
    sendTime = models.DateTimeField()
    idAuteur = models.ForeignKey(User, on_delete=models.CASCADE)

class Post_Comment(models.Model):
    idComment = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    idPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class Message(models.Model):
    idPost = models.PositiveIntegerField()
    contenu = models.TextField(max_length=1500)
    lienExterne = models.AutoField(default=None)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idRecipient = models.PositiveBigIntegerField()
    sendTime = models.DateTimeField()

class Recipient_Message(models.Model):
    idMessage = models.ForeignKey(Message, on_delete=models.CASCADE)
    idRecipient = models.ForeignKey(User, on_delete=models.CASCADE)