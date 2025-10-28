from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="home"),
    path('post/<slug:slug>', views.post, name="post"),
    path('results', views.search, name="search"),
]
