
# Proyecto Django con Integración de Transbank

Este proyecto implementa un sistema de pagos en Django utilizando **Transbank Webpay Plus** en el ambiente de integración. Además, cuenta con un sistema de carrito de compras.

---

## Requisitos Previos

1. **Docker y Docker Compose** instalados.
2. Credenciales de prueba para Transbank Webpay Plus.
3. Superusuario configurado para acceder al panel de administración.

---

## Configuración del Proyecto

### 1. Clonar el Repositorio
```bash
git clone https://github.com/CarlosNavarroM/InfraestructuraDuocUC
cd monolito
```

### 2. Configuración en `settings.py`

Asegúrate de que las siguientes configuraciones estén presentes en tu archivo `settings.py`:

```python
# Credenciales para Transbank
TRANSBANK_COMMERCE_CODE = "597055555532"
TRANSBANK_API_KEY = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
TRANSBANK_ENVIRONMENT = "integration"

# Configuración de Django
SECRET_KEY = "tu_secreto_aqui"
DEBUG = False

# Configuración de Archivos Estáticos y de Medios
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Construcción y Ejecución del Proyecto

### 1. Construir y Ejecutar los Contenedores
```bash
docker-compose up --build
```

---

## Acceso al Panel de Administración

### Credenciales de Superusuario
- **Usuario:** admin
- **Contraseña:** admin

Accede al panel en [http://localhost/admin](http://localhost/admin).

---

## Uso de Transbank Webpay Plus

### Datos de Tarjeta de Prueba
- **Número de tarjeta (VISA):** `4051 8856 0044 6623`
- **CVV:** `123`
- **Fecha de vencimiento:** Cualquier fecha futura válida (por ejemplo, `12/30`).
- **RUT:** `11.111.111-1`
- **Correo electrónico:** Puedes usar cualquier correo válido (por ejemplo, `test@test.com`).

---

## Archivos Clave

### `docker-compose.yml`
Configura los servicios de Django, Nginx y MySQL.

### `nginx/nginx.conf`
Define cómo Nginx sirve los archivos estáticos y de medios, y redirige solicitudes a Django.

---

## Pruebas

1. Accede al carrito de compras y selecciona "Proceder al Pago".
2. Completa el formulario de prueba de Transbank con los datos mencionados arriba.
3. Verifica el estado de la transacción en la página de resultados.

---

## Solución de Problemas

1. **Error con Nginx:**
   Asegúrate de que el archivo `nginx.conf` esté correctamente configurado y que los contenedores estén reiniciados.

2. **Archivos estáticos o de medios no se cargan:**
   Asegúrate de haber ejecutado:
   ```bash
   docker exec -it django_app python manage.py collectstatic
   ```

---

## Créditos
Proyecto desarrollado con Django, Docker, Nginx y MySQL, integrado con Transbank Webpay Plus.
