from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from instagramUser.models import Profile, Following
from .post import Post

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Stream(models.Model):
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stream_following')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField()
    
    def add_post(sender, instance, *args, **kwargs):
        post = instance
        user = post.profile
        followers = Following.objects.all().filter(following=user)
        for follower in followers:
            stream = Stream()
            stream.following=user
            stream.user = follower.follower
            stream.post = post
            stream.date = post.created_at
            stream.save()
    
    def __str__(self):
        return self.following.username + ' ' + self.user.username
post_save.connect(Stream.add_post, sender=Post)





