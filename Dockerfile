FROM python:3.13-rc-slim-bookworm

# Configuración de entorno seguro
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# 1. Instala dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl3 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 2. Crea usuario y directorio de instance ANTES de cambiar de usuario
RUN groupadd -r appuser -g 1000 && \
    useradd -r -u 1000 -g appuser appuser

# 3. Crear directorio para archivos de instancia
#RUN mkdir -p /app/instance && \
#    chown appuser:appuser /app/instance && \
#    chmod 755 /app/instance

# 4. Instala dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# 5. Copia el código
COPY . .

# 6. Exponer el puerto en el que corre la aplicación
EXPOSE ${PORT:-5000}

# 7. Cambia al usuario no-root
USER appuser

CMD ["python", "run.py"]