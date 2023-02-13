from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('profile_update', views.profile_update, name='profile_update'),
]