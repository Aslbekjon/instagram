from django.db import models
from .instaUsers import Profile

class Following(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, default=False)
    followed = models.ManyToManyField(Profile, related_name="followed")
    follower = models.ManyToManyField(Profile, related_name="follower")

    @classmethod
    def follow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user = user)
        obj.followed.add(another_account)
        print("followed")

    @classmethod
    def unfollow(cls, user, another_account):
        obj, create = cls.objects.get_or_create(user = user)
        obj.followed.remove(another_account)
        print("unfollowed")

    def __str__(self):
        return f'{self.user.username} Profile'
