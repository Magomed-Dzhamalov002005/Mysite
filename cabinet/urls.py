from django.urls import path
from . import views

app_name = 'cabinet'
urlpatterns = [
    path('cabinet/<str:user>/', views.cabinet, name="studio"),
]
