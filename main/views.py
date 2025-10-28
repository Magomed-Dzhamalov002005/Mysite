from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-date')[:3]

    data = {
        'posts':posts,
    }
    
    query = request.GET.get("search")
    if query:
        result = Post.objects.filter(name__contains=query) | Post.objects.filter(text__contains=query)
        data["searchResult"] = result
        
    return render(request, 'main/index.html', context=data)

def post(request, slug):
    post = Post.objects.get(slug = slug)
    data = {
        'post':post
    }
    return render(request, 'main/post.html', context=data)

def search(request):
    if request.GET:
        query = request.GET['search_query']
        result = Post.objects.filter(name__contains=query) | Post.objects.filter(text__contains=query)
        
    data = {
        'searchResult': result,
    }
    return render(request, 'main/search.html', context=data)