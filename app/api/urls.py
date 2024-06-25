from django.urls import path
from . import views

urlpatterns = [
    path('UserRegister', views.user_register),
]