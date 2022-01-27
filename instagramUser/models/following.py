from django.db import models
from .instaUsers import Profile

class Following(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return self.follower.username + ' ' + self.following.username + 'ga follow bosdi'

