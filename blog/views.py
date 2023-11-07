from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post

def home(request):
    context = {'posts' : Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return HttpResponse('<h1>About here')


# Create your views here.