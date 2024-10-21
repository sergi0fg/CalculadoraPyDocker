# Usar una imagen base de Alpine
FROM python:3.11-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de la calculadora al contenedor
COPY calculadora.py .

# Instalar cualquier dependencia necesaria (en este caso, no hay ninguna)
# RUN pip install -r requirements.txt

# Comando por defecto para ejecutar la calculadora
CMD ["python", "calculadora.py"]
