from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-date')
    data = {
        'posts':posts
    }
    return render(request, 'main/index.html', context=data)

def post(request, slug):
    post = Post.objects.get(slug = slug)
    data = {
        'post':post
    }
    return render(request, 'main/post.html', context=data)