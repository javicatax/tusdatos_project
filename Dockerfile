# Selecciona la imagen base de Python
FROM python:3.12.3

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos locales en el contenedor (del directorio actual al contenedor)
COPY . .

# Instala las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto donde se ejecutará la app (esto es opcional, pero útil para aplicaciones web)
EXPOSE 8000

# Comando para ejecutar la aplicación (ajusta según la configuración de tu proyecto)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
