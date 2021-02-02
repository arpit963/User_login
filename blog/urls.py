from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("register", views.register, name='register'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
]