# Generated by Django 4.1.7 on 2023-02-23 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='auteur',
        ),
        migrations.RemoveField(
            model_name='message',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='post_comment',
            name='idComment',
        ),
        migrations.RemoveField(
            model_name='post_comment',
            name='idPost',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='recipient_message',
            name='idMessage',
        ),
        migrations.RemoveField(
            model_name='recipient_message',
            name='idRecipient',
        ),
        migrations.RemoveField(
            model_name='user_subscriber',
            name='idSubscriber',
        ),
        migrations.RemoveField(
            model_name='user_subscriber',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='user_subscription',
            name='idSubscription',
        ),
        migrations.RemoveField(
            model_name='user_subscription',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='auteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='idPost',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='sendingTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Abonne',
        ),
        migrations.DeleteModel(
            name='Abonnement',
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Post_Comment',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Recipient_Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_Subscriber',
        ),
        migrations.DeleteModel(
            name='User_Subscription',
        ),
    ]
