from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class CategoryType(models.TextChoices):
        COUNTRIES = 'GLC', ('Global countries')
        NEWS = 'NWS', ('Global news')
        OTHER = 'NO', ("Not in list")
    
    name = models.CharField(max_length=50, unique=True)
    categoryType = models.CharField(max_length=5, choices=CategoryType.choices, default=CategoryType.OTHER)

    def __str__(self) -> str:   
        return (f"Category[ID:{self.pk}]: {self.name}; {self.categoryType}")

default_author = User.objects.get(username='TemporaryAuthor')

class Post(models.Model):
    slug = models.CharField(max_length=25, unique=True)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=99)
    text = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=default_author.pk)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self) -> str:   
        return (f"Post[ID:{self.pk}]: {self.name}")


default_post = Post.objects.get(pk=1)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=default_post.pk)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    text = models.TextField(max_length=1000, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:   
        return (f"Comment[ID:{self.pk}]: Author: {self.author}; Date: {self.date}.")