from django.db import models
from instagramUser.models import Profile

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to = 'post/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    like = models.ManyToManyField(Profile, related_name='likes', blank=True)
    location = models.CharField(max_length=200)


    def __str__(self):
        return '{}ning {}- rasmi'.format(self.profile.username, self.id)
        