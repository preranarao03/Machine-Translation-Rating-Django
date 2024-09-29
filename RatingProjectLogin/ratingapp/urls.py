from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_rating/', views.save_rating, name='save_rating'),
    path('sort_table/', views.sort_table, name='sort_table'),
    path('add_sentence/', views.add_sentence, name='add_sentence'),
    path('signuppage/', views.signupfunction),
    path('loginpage/', views.loginfunction),
]
