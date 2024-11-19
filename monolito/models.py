from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio en CLP
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Imagen del producto
    stock = models.PositiveIntegerField(default=0)  # Cantidad disponible
    valoracion_promedio = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )  # Valoración promedio (0 a 5)
    total_valoraciones = models.PositiveIntegerField(default=0)  # Número de valoraciones acumuladas

    def __str__(self):
        return self.nombre

    def agregar_valoracion(self, valor):
        """
        Método para actualizar la valoración promedio del producto.
        """
        self.total_valoraciones += 1
        self.valoracion_promedio = (
            (self.valoracion_promedio * (self.total_valoraciones - 1)) + valor
        ) / self.total_valoraciones
        self.save()


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def total(self):
        """
        Calcula el precio total del producto en el carrito.
        """
        return self.cantidad * self.producto.precio
