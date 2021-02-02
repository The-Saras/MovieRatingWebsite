from django.contrib import admin
from django.urls import path,include
from movie import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('<str:slug>',views.details,name='det'),
    path('signup',views.handleSignup,name='handleSignup')
]