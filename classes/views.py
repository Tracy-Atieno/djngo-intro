from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# this is where all functions are created


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'pages/contact.html')
