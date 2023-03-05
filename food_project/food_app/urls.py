from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up,name='sign_up'),
    path('sign-in/', views.sign_in,name='sign_in'),
]