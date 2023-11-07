from django.contrib import admin
from django.urls import path, include
from blog import views
from account.views import (
    register_view,
    
)

urlpatterns = [

    path('', views.home, name='blog-home'),
    path('register/', register_view, name='register'),
    path('about/', views.about, name='blog-about'),

]