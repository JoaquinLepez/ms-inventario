FROM python:3.10-slim-bullseye

# Definimos variables de entorno
ENV FLASK_CONTEXT=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/ms-inventario/.local/bin

# Crear el usuario ms-inventario y su directorio home
RUN useradd --create-home --home-dir /home/ms-inventario ms-inventario

# Actualizamos los repositorios e instalamos las dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libpq-dev \
    python3-psycopg2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Definir el directorio de trabajo
WORKDIR /home/ms-inventario

# Cambiar al usuario ms-inventario
USER ms-inventario

# Crear la carpeta app
RUN mkdir app

# Copiar los archivos de la aplicación al contenedor
COPY ./app ./app
COPY ./app.py .

# Añadir el archivo requirements.txt e instalar las dependencias de Python
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000 para Flask
EXPOSE 3004

# Comando para ejecutar la aplicación Flask
CMD [ "python", "./app.py" ]