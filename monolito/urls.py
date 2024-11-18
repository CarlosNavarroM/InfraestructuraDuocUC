from django.urls import path

from django.contrib import admin  # Importa el admin correcto
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', views.home, name='home'),  # Página principal
    path('registro/', views.registro, name='registro'),  # Registro de usuarios
    path('productos/', views.listar_productos, name='productos'),  # Listar productos
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),  # Agregar al carrito
    path('carrito/', views.ver_carrito, name='carrito'),  # Ver carrito
]
