from django.shortcuts import render 
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'JohnnyB',
        'title': 'Blog Post 1',
        'content': 'Bla Bla Bla Bla',
        'date_posted': '26 May 2019'
    },
    {
        'author': 'Angela',
        'title': 'Blog Post 2',
        'content': 'More Bla Bla Bla Bla',
        'date_posted': '31 May 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})