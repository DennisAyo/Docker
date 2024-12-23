# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y la aplicación
COPY requirements.txt requirements.txt 

# Instala las dependencias
RUN pip install -r requirements.txt
COPY . .
# Expone el puerto en el que la app correrá
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
