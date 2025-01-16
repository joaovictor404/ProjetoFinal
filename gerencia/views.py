from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gerencia/index.html')

def inicio(request):
    return render(request, 'gerencia/inicio.html')