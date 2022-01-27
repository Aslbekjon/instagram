import profile
from statistics import mode
from django.db import models
from instagramUser.models import Profile
from .tags import Tag

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to = 'post/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='taglar')
    created_at = models.DateTimeField(auto_now_add = True)
    like = models.IntegerField(default = 0)
    location = models.CharField(max_length=200)


    def __str__(self):
        return '{}ning {}- rasmi'.format(self.profile.username, self.profile.post_set.count())
        