from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(User)
    content = models.TextField()

    def __str__(self):
        return self.title