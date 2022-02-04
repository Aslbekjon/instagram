from django.db import models
from instagramUser.models import Profile
from .post import Post


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")
