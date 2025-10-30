from django.db import models
from django.contrib.auth.models import User

default_author = User.objects.get(username='TemporaryAuthor')

# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=25, unique=True)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=99)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=default_author.pk)
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self) -> str:   
        return (f"Post[ID:{self.pk}]: {self.name}")