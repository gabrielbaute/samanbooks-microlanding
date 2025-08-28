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
    useradd -r -u 1000 -g appuser appuser && \
    mkdir -p instance && \
    chown appuser:appuser instance && \
    chmod 755 instance

# 3. Instala dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

# 4. Copia el código
# COPY app/ ./app/
# COPY run.py .
COPY . .

# Exponer el puerto en el que corre la aplicación
EXPOSE ${PORT:-5000}

# 6. Cambia al usuario no-root
USER appuser

CMD ["python", "run.py"]