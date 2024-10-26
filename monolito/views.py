# monolito/views.py

from django.http import JsonResponse
from django.shortcuts import render

def home_view(request):
    return render(request, 'frontend/home.html')

def hola_mundo_api(request):
    return JsonResponse({"mensaje": "Hola, mundo"})
# monolito/views.py



