from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from POS_1.settings import LOGIN_REDIRECT_URL
from .forms import UserRegisterForm
from django.contrib import messages
from django.views.generic import TemplateView 
from .models import Product

# Create your views here.
def homePage(request):
    return render(request, 'user/sidebar.html',{'title':'POS System'})

@login_required
def Shop(request):
    prods = Product.get_all_products
    return render(request, 'user/shop.html', { 'products': prods })

def Furniture(request):
    prods = Product.objects.filter(category=1)
    return render(request, 'user/shop.html', { 'products': prods })

def Men_clothes(request):
    prods = Product.objects.filter(category=3)
    return render(request, 'user/shop.html', { 'products': prods })

def Women_clothes(request):
    prods = Product.objects.filter(category=2)
    return render(request, 'user/shop.html', { 'products': prods })

def Kids_clothes(request):
    prods = Product.objects.filter(category=4)
    return render(request, 'user/shop.html', { 'products': prods })

def Grocery(request):
    prods = Product.objects.filter(category=7)
    return render(request, 'user/shop.html', { 'products': prods })

def Laptops(request):
    prods = Product.objects.filter(category=6)
    return render(request, 'user/shop.html', { 'products': prods })

def Mobiles(request):
    prods = Product.objects.filter(category=5)
    return render(request, 'user/shop.html', { 'products': prods })

def signUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('user-signin')
    else:
        form = UserRegisterForm()
    return render(request, 'user/signup.html', {'form': form})

def SideBar(request):
    return render(request, 'user/sidebar.html')

class SignInView(TemplateView):
    template_name = 'signin.html'

class SignOutView(TemplateView):
    template_name = 'signout.html'

#def signIn(request):
    #return render(request, 'user/signup.html')

#def signOut(request):
    #return render(request, 'user/signup.html')