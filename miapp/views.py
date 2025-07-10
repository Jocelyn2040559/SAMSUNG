from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')

def celulares(request):
    return render(request, 'miapp/celulares.html')

def soporte(request):
    return render(request, 'miapp/soporte.html')

def nosotros(request):
    return render(request, 'miapp/nosotros.html')

def contactanos(request):
    return render(request, 'miapp/contactanos.html')
