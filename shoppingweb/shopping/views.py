# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth import logout
from .models import Product

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('signin')  # Redirect to login page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')  # Redirect to welcome page after successful login
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def welcome(request):
    products = Product.objects.all()
    return render(request, 'welcome.html', {'products': products})

def logout_view(request):
    logout(request)
    return redirect('home')