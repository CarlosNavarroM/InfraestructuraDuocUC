from django.contrib import admin
from .models import Producto, Carrito, CarritoProducto

# Configuración del modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'valoracion_promedio')
    search_fields = ('nombre',)
    list_filter = ('precio', 'stock')
    ordering = ('nombre',)

# Configuración del modelo Carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario',)
    search_fields = ('usuario__username',)

# Configuración del modelo CarritoProducto
@admin.register(CarritoProducto)
class CarritoProductoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'producto', 'cantidad', 'total')
    search_fields = ('carrito__usuario__username', 'producto__nombre')
