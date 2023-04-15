from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def buy(request):
    return HttpResponse('<h1>buebue</h1>')

