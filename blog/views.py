from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from blog.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adr = request.POST.get('adr')
        desc = request.POST.get('desc')
        contact = Contact(name=name , email=email, phone=phone, desc=desc, adr=adr)
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'contact.html')
    
# User Authenticate
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # check if user has entered corPOSTrect credentials

        user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('/')
        # else:
        #     return render(request, 'login.html')

        if username=='arpit':
            login(request, user)
            return redirect('/')
        else:
            login(request, user)
            return redirect('/contact')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
