from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from main.forms import PostAddingForm


@login_required(redirect_field_name="after", login_url="auth:login")
def cabinet(request, user):
    form = PostAddingForm()
    
    if request.POST:
        form = PostAddingForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("main:home")
        else:
            messages.error(request, "Smth went wrong")
    else:
        pass
    
    if request.POST:
        deleteAccount = request.POST["deleteAccount"]
        if deleteAccount:
            User.objects.get(username=user).delete()
            messages.success(request, "Account successfully deleted!")
            return redirect("auth:login")
    else:
        pass
    
    data = {
        "form":form
    }
    return render(request, "cabinet/cabinet.html", context=data)