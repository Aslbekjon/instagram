from django.db import models
from .instaUsers import Profile

class Following(models.Model):
    user_from = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rel_to_set')

    def __str__(self):
        return '{} dan {} ga'.format(self.user_from.username, self.user_to.username)

Profile.add_to_class('following',
                    models.ManyToManyField('self',
                    through = Following,
                    related_name = 'followers',
                    symmetrical=False
                    ))