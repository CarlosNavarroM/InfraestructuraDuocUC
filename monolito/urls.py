from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    # Ruta para el admin
    path('admin/', admin.site.urls),

    # Rutas principales
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Productos
    path('productos/', views.listar_productos, name='listar_productos'),

    # Carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    # Pago con Transbank
    path('pago/proceder/', views.proceder_pago, name='proceder_pago'),
    path('pago/respuesta/', views.pago_respuesta, name='pago_respuesta'),
]
