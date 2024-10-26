# monolito/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo_api, name='hola_mundo_api'),  # Mantiene la vista original
    path('home/', views.home_view, name='home_view'),       # Nueva vista para la plantilla
]
