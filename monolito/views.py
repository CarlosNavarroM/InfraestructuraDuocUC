from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, CarritoProducto


# Página principal
def home(request):
    return render(request, 'frontend/home.html')


# Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'frontend/registro.html', {'form': form})


# Iniciar sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'frontend/login.html', {'form': form})


# Cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# Listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'frontend/listar_productos.html', {'productos': productos})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if producto.stock <= 0:
        return redirect('listar_productos')  # Redirigir si no hay stock disponible

    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, created = CarritoProducto.objects.get_or_create(
        carrito=carrito, producto=producto
    )
    if not created:
        if carrito_producto.cantidad < producto.stock:
            carrito_producto.cantidad += 1
        else:
            return redirect('listar_productos')  # Redirigir si ya alcanzó el stock
    else:
        carrito_producto.cantidad = 1
    carrito_producto.save()
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    # Obtener o crear el carrito del usuario
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    # Obtener los productos del carrito
    productos = carrito.productos.all()

    # Crear una lista de productos con sus totales calculados
    productos_con_totales = []
    for item in productos:
        total = item.cantidad * item.producto.precio
        productos_con_totales.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'total': total,
        })

    # Enviar los productos al contexto
    return render(request, 'frontend/carrito.html', {'productos': productos_con_totales})





@login_required
def eliminar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto_id=producto_id)
    carrito_producto.delete()
    return redirect('ver_carrito')