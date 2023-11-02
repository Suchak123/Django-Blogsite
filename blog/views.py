from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


posts = [
    {
        'author': 'Suchak',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'RadheShyam',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {'posts' : posts}
    return render(request, 'blog/home.html', context)
# Create your views here.

def about(request):
    return HttpResponse('<h1>About here')