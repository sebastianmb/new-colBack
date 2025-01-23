# 1. Usar una imagen base de Python

FROM python:3

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Copiar los archivos de tu proyecto al contenedor
COPY requirements.txt . 

# 4. Instalar dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código del backend al contenedor
COPY . .

# 5. Exponer el puerto de Django (por defecto 8000)
EXPOSE 8000

# 6. Definir el comando de inicio del servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "noticias_api.wsgi:application"]