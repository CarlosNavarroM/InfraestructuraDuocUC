from django.contrib import admin
from .models import Producto, Carrito, CarritoProducto

# Registra los modelos en el administrador de Django
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)
