from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm


def signup(request):
    form = RegistrationForm()
    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("auth:login")
        else:
            messages.error(request, "Data is incorrect!")
    else:
        pass
    
    data = {
        'form': form,
    }
    return render(request, 'authentication/registration.html', context=data)

def log_in(request):
    form = LoginForm()
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:home")
        else:
            messages.error(request, "User isn'f founded!")
    else:
        pass
    
    data = {
        'form': form,
    }
    return render(request, 'authentication/login.html', context=data)

def log_out(request):
    logout(request)
    messages.success("You are successfully logged out.")
    return redirect("auth:login")