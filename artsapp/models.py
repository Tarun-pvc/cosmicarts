from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    # art = models.ImageField()
    # if the user is deleted, all his blog posts will be deleted with CASCADE.
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    art_image = models.ImageField(null=True, blank=True, upload_to='')
    # likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title + ' by ' + str(self.artist)
