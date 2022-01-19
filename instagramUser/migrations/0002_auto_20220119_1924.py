# Generated by Django 3.2.11 on 2022-01-19 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagramUser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='following',
            name='user_from',
        ),
        migrations.RemoveField(
            model_name='following',
            name='user_to',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.AddField(
            model_name='following',
            name='followed',
            field=models.ManyToManyField(default=False, related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='following',
            name='follower',
            field=models.ManyToManyField(default=False, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='following',
            name='user',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]