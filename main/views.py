from django.shortcuts import render, redirect
from django.db.models import F
from .models import Post, Comment, Category
from .forms import CommentForm

def index(request):
    
    posts = Post.objects.all().order_by('-date')[:3]
    categories = Category.objects.all()
    message = ""

    data = {
        'posts':posts,
        'categories': categories,
        'message': message,
    }
    
    if request.GET:
        
        query = request.GET.get("search-query")
        
        if query:
            result = Post.objects.filter(name__contains=query) | Post.objects.filter(text__contains=query)
            data["message"] = "Nothing here ... :)"
            data["searchResult"] = result
        
    return render(request, 'main/index.html', context=data)

def post(request, slug):
    
    if request.user.is_authenticated:
        Post.objects.filter(slug = slug).update(views=F('views')+1)
        
    post = Post.objects.get(slug = slug)
    form = CommentForm()
    
    message = "" # Just learning different ways to show messages, by myself and from django contrib messages
    
    if request.POST:
        
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            print(comment)
            return redirect("main:post", slug)
        else:
            message = "something went wrong :("
    
    else:
        form = CommentForm()
    
    comments = Comment.objects.filter(post=post).order_by('-date')
    
    if request.POST:
        
        delete_comment = request.POST["delete-comment"]
        
        try:
            if delete_comment:
                delete_comment = delete_comment.split("|")
                comment = Comment.objects.get(pk = delete_comment[0], author=request.user)
                comment.delete()
        except Exception:
            message = "Comment haven't founded"
    
    else:
        pass
    
    data = {
        'post':post,
        'comments':comments,
        'form':form,
    }
    
    return render(request, 'main/post.html', context=data)

def category(request, cat_pk):
    
    category = Category.objects.get(pk=cat_pk)
    posts = Post.objects.filter(category=cat_pk)
    
    data = {
        'cat': category,
        'posts': posts,
    }
    
    return render(request, 'main/category.html', context=data)

def search(request):
    
    if request.GET:
        query = request.GET['search_query']
        result = Post.objects.filter(name__contains=query) | Post.objects.filter(text__contains=query)
        
    data = {
        'searchResult': result,
    }
    
    return render(request, 'main/search.html', context=data)