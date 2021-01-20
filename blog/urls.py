from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),

]