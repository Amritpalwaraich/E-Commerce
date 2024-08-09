from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import  CommentForm, SignUpForm

# Create your views here.

def category(request, foo):
    #Replace hyphens with space 
    foo = foo.replace('-',' ')
    #Grab the cartgory from the url 
    try:
        # loop Up the category 
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category': category})
    except:
        messages.success(request,("That Category doesn't exists....")) 
        return redirect('home')
    
def comment(request):
    form = CommentForm
    return render(request, 'comment.html',{'form':form})

def product(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print("form")
    else:
        form = CommentForm
    product = Product.objects.get(id = pk)
    return render(request, 'product.html',{'product': product, 'form': form}) 

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', )

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Logged In! "))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again."))
            return redirect('login')
    else:      
        return render(request, 'login.html', {})

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Great, your account is successfully registered. Please complete your personal information.")
            return redirect("login")
        else:
            messages.error(request, "Oops something went wrong with your registration, please try again.")
            return redirect("register")
    else:
        context = {'form': form}
        return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out... Thanks for stopping by..."))
    return redirect('home')

