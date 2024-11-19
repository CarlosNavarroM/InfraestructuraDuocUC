# Usa una imagen base con Python
FROM python:3.9-slim

# Instalar dependencias necesarias para `mysqlclient`
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia todo el código al contenedor
COPY . .

# Ejecuta el comando para recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# (Opcional) Ejecuta las migraciones de base de datos
RUN python manage.py migrate --noinput

# Exponer el puerto 8000 para el servidor de desarrollo
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "monolito.wsgi:application", "--bind", "0.0.0.0:8000"]
