from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm


def signup(request):
    form = RegistrationForm()
    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:home")
    else:
        messages.error(request, "Data is incorrect!")
    
    data = {
        'form': form,
    }
    return render(request, 'authentication/registration.html', context=data)