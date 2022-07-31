from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name = 'user-main'),
    path('home/', views.homePage, name = 'user-home'),
    path('pos/', views.homePage, name = 'pos'),
    path('shop/', views.Shop, name = 'user-shop'),
    path('furniture/', views.Furniture, name = 'furniture'),
    path('men-clothes/', views.Men_clothes, name = 'men-clothes'),
    path('women-clothes/', views.Women_clothes, name = 'women-clothes'),
    path('kids-clothes/', views.Kids_clothes, name = 'kids-clothes'),
    path('grocery/', views.Grocery, name = 'grocery'),
    path('laptops/', views.Laptops, name = 'laptops'),
    path('mobiles/', views.Mobiles, name = 'mobiles'),
    path('sidebar/', views.SideBar, name='sidebar'),
    path('signup/', views.signUp, name = 'user-signup'),
    path('signin/', auth_views.LoginView.as_view(template_name="user/signin.html"), name='user-signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name="user/signout.html"), name='user-signout'),
]