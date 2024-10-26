# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia el resto del proyecto al contenedor
COPY . /app/

# Ejecuta Gunicorn en el servidor

CMD ["gunicorn", "monolito.wsgi:application", "--bind", "0.0.0.0:8000"]
