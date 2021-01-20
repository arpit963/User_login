from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

# User Authenticate
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # check if user has entered correct credentials

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
            # A backend authenticated the credentials
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
