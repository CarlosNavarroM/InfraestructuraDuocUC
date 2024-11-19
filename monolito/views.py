from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, CarritoProducto
from transbank.webpay.webpay_plus.transaction import Transaction
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

#tranksbank 

@login_required
def proceder_pago(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    productos = carrito.productos.all()

    if not productos:
        return redirect('ver_carrito')  # Si no hay productos, redirige al carrito

    # Calcula el total del carrito
    total = sum([item.cantidad * item.producto.precio for item in productos])

    # Configura la transacción de Transbank
    transaction = Transaction()
    buy_order = f"ORDER-{carrito.id}"  # Orden única basada en el ID del carrito
    session_id = f"SESSION-{request.user.id}"
    return_url = request.build_absolute_uri(reverse('pago_respuesta'))  # URL para manejar la respuesta

    response = transaction.create(buy_order, session_id, total, return_url)

    # Redirige al usuario al formulario de pago de Transbank
    return HttpResponseRedirect(response["url"] + "?token_ws=" + response["token"])

@login_required
def pago_respuesta(request):
    token = request.GET.get("token_ws")

    if not token:
        return redirect('ver_carrito')  # Redirige si no hay token

    transaction = Transaction()
    response = transaction.commit(token)

    if response["status"] == "AUTHORIZED":
        # Vaciar el carrito después de una transacción exitosa
        carrito = get_object_or_404(Carrito, usuario=request.user)
        carrito.productos.all().delete()
        mensaje = "Pago exitoso. Gracias por tu compra."
    else:
        mensaje = "El pago no fue exitoso. Por favor, intenta nuevamente."

    return render(request, "frontend/pago_resultado.html", {"mensaje": mensaje, "response": response})
 
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
    print(f"Producto encontrado: {producto.nombre} (Stock: {producto.stock})")

    if producto.stock <= 0:
        print("El producto no tiene stock.")
        return redirect('listar_productos')

    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    print(f"Carrito del usuario: {carrito}")

    carrito_producto, created = CarritoProducto.objects.get_or_create(
        carrito=carrito, producto=producto
    )
    print(f"Producto agregado al carrito: {carrito_producto}, creado: {created}")

    if not created:
        if carrito_producto.cantidad < producto.stock:
            carrito_producto.cantidad += 1
        else:
            print("No se puede agregar más cantidad, se alcanzó el stock.")
            return redirect('listar_productos')
    else:
        carrito_producto.cantidad = 1

    carrito_producto.save()
    print(f"Cantidad actualizada: {carrito_producto.cantidad}")
    return redirect('ver_carrito')


@login_required
def ver_carrito(request):
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

    print(f"Productos en el carrito: {productos_con_totales}")  # Debug
    return render(request, 'frontend/carrito.html', {'productos': productos_con_totales})







@login_required
def eliminar_del_carrito(request, producto_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito_producto = get_object_or_404(CarritoProducto, carrito=carrito, producto_id=producto_id)
    carrito_producto.delete()
    return redirect('ver_carrito')