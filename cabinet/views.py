from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import Post
from main.forms import PostAddingForm


special_symbols = " !@#$%^&*()_+-=\'\";:./,<>|"

def checkingForSpecialCharacters(comingString):
    
    f = 0
            
    for i in comingString:
        if i in special_symbols: f = 1
        
    return f == 0


@login_required(redirect_field_name="after", login_url="auth:login")
def cabinet(request, user):
    form = PostAddingForm()
    user_posts = Post.objects.filter(author=request.user.pk)
    
    if request.POST:
        
        postCreatingForm = request.POST.get("postCreatingForm")
        
        if postCreatingForm:
            
            form = PostAddingForm(request.POST, request.FILES)
            
            if form.is_valid() and checkingForSpecialCharacters(request.POST['slug']):
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "Post created successfully!")
                return redirect("main:home")
            elif not checkingForSpecialCharacters(request.POST['slug']):
                messages.error(request, "You can not type special symbols and spaces in slug!")
            else:
                messages.error(request, "Smth went wrong")
            
            return redirect("cabinet:studio", request.user)
    
    if request.POST:
        
        editPost = request.POST.get("editPost")
        
        try:
            if editPost:
                p = Post.objects.get(pk=editPost)
                editPostForm = PostAddingForm(instance=p)
                editPost = int(editPost)
        except Exception:
            messages.error(request, "Post not found!")
            return redirect("cabinet:studio", request.user)
    else:
        editPost = 0
        editPostForm = ""
        
    if request.POST:
        
        postUpdatingForm = request.POST.get("postUpdatingForm")
        
        if postUpdatingForm:
            post = Post.objects.get(pk=postUpdatingForm)
            form = PostAddingForm(request.POST, request.FILES, instance=post)
            
            if form.is_valid() and checkingForSpecialCharacters(request.POST['slug']):
                post = form.save()
            elif not checkingForSpecialCharacters(request.POST['slug']):
                messages.error(request, "You can not type special symbols and spaces in slug!")
            else:
                messages.error(request, "Smth went wrong")

            return redirect("cabinet:studio", request.user)

    if request.POST:
        
        deletePost = request.POST.get("deletePost")
        
        try:
            if deletePost:
                Post.objects.get(pk=deletePost).delete()
                messages.success(request, "Post successfully deleted!")
                return redirect("cabinet:studio", request.user)
        except Exception:
            messages.error(request, "Post not found!")
            return redirect("cabinet:studio", request.user)
    
    if request.POST:
        
        deleteAccount = request.POST.get("deleteAccount")
        
        try:
            if deleteAccount:
                User.objects.get(pk=request.user.pk, username=request.user.username).delete()
                messages.success(request, "Account successfully deleted!")
                return redirect("auth:login")
        except Exception:
            messages.error(request, "Account not found!")
            return redirect("auth:login")
    
    data = {
        "form": form,
        "posts": user_posts,
        "editPostid": editPost,
        "editPostForm": editPostForm,
    }
    return render(request, "cabinet/cabinet.html", context=data)