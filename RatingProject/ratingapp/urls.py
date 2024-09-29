from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.home, name='home'),
    path('loginpage/', views.loginfunction, name='loginpage'),  
    path('signuppage/', views.signupfunction, name='signuppage'),
    path('index/', views.index, name='index'),
    path('save_rating/', views.save_rating, name='save_rating'),
    path('sort_table/', views.sort_table, name='sort_table'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    path('signuppage/', views.signupfunction),
    path('loginpage/', views.loginfunction),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
