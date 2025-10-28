from django.db import models

# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=25, unique=True)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=99)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self) -> str:   
        return (f"Post[ID:{self.pk}]: {self.name}")