from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="after", login_url="auth:login")
def cabinet(request, user):
    data = {
    }
    return render(request, "cabinet/cabinet.html", context=data)