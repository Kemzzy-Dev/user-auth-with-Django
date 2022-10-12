from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerUser, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.SignInUser, name='login'),
    path('signout/', views.SignOutUser, name='signout')
]