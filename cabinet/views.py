from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(redirect_field_name="after", login_url="auth:login")
def cabinet(request, user):
    
    if request.POST:
        deleteAccount = request.POST["deleteAccount"]
        if deleteAccount:
            User.objects.get(username=user).delete()
            messages.success(request, "Account successfully deleted!")
            return redirect("auth:login")
    else:
        pass
    
    data = {
    }
    return render(request, "cabinet/cabinet.html", context=data)