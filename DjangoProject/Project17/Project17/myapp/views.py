from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from django.template.context_processors import request


def home(request):
    #return HttpResponse("Hello,django!")
    #return render(request,'')
    #return render(request, 'myapp/about.html')  # Update this line
    return render(request, 'myapp/home.html')

def about(request):
    #return HttpResponse("< h1>About Us</h1><p>This is the about page.</p>")

    return render(request, 'myapp/about.html')  # Update this line

def contact(request):
    return render(request, 'myapp/contact.html')  # Contact page

def services(request):
    return render(request, 'myapp/services.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'myapp/login.html')