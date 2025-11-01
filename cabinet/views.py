from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import Post
from main.forms import PostAddingForm


special_symbols = "!@#$%^&*()_+-=\|'\";:./,<>"

@login_required(redirect_field_name="after", login_url="auth:login")
def cabinet(request, user):
    form = PostAddingForm()
    user_posts = Post.objects.filter(author=request.user.pk)
    
    if request.POST:
        postCreatingForm = request.POST.get("postCreatingForm")
        if postCreatingForm:
            form = PostAddingForm(request.POST, request.FILES)
            
            f = 0    # checking special symbols in slug
            
            for i in request.POST['slug']:
                if i in special_symbols: f = 1
                    
            if form.is_valid() and f == 0:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect("main:home")
            elif f == 1:
                messages.error(request, "You can not type special symbols in slug!")
            else:
                messages.error(request, "Smth went wrong")
            
            return redirect("cabinet:studio", request.user)
    else:
        pass
    
    if request.POST:
        deleteAccount = request.POST.get("deleteAccount")
        if deleteAccount:
            User.objects.get(pk=request.user.pk, username=request.user.username).delete()
            messages.success(request, "Account successfully deleted!")
            return redirect("auth:login")
    else:
        pass
    
    data = {
        "form": form,
        "posts": user_posts,
    }
    return render(request, "cabinet/cabinet.html", context=data)