from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, CarritoProducto

# Home
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

# Listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'frontend/listar_productos.html', {'productos': productos})

# Agregar al carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    carrito_producto, created = CarritoProducto.objects.get_or_create(
        carrito=carrito, producto=producto
    )
    if not created:
        carrito_producto.cantidad += 1
    carrito_producto.save()
    return redirect('listar_productos')

# Ver carrito
@login_required
def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    productos = carrito.carritoproducto_set.all()
    return render(request, 'frontend/carrito.html', {'productos': productos})
