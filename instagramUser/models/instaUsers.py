from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    bio = models.TextField(max_length=100,blank=True, null=True)
    img = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length = 20, blank=True, null=True)
    followers = models.IntegerField(default=0)
    followings = models.IntegerField(default=0)
    like_count  = models.IntegerField(default=0)

    def __str__(self):
        return self.username