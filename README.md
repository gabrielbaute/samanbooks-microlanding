
## 🚀 Guía de Deploy para SamanBooks Microlanding

### 📁 1. Preparar entorno local

```bash
cp .env.example .env
```

- Edita `.env` con tus variables personalizadas (puerto, claves, rutas, etc).
- Asegúrate de que la carpeta `instance/` exista en la raíz del proyecto.

---

### 🐳 2. Construir el contenedor

```bash
docker compose build
```

Esto compila la imagen usando el `Dockerfile` y prepara el entorno para ejecución.

---

### 🔐 3. Ajustar permisos de la carpeta `instance/`

El contenedor corre como usuario no-root (`UID 1000`), por lo tanto necesitas:

```bash
sudo chown -R 1000:1000 ./instance
sudo chmod -R 755 ./instance
```

Esto asegura que la base de datos SQLite pueda escribirse correctamente.

---

### ▶️ 4. Levantar el servicio

```bash
docker compose up
```

- La aplicación estará disponible en `http://localhost:5000` (o el puerto definido en `.env`)
- Puedes usar `docker compose up -d` para ejecutarlo en segundo plano.
- Checa los logs con `docker compose logs -f`

---

### 🧪 5. Verificar estado

```bash
docker exec -it samanbooks ls /app/instance
```

Deberías ver el archivo `app.db` o los archivos de estado si todo está funcionando.

---

### 🧼 6. Apagar el servicio

```bash
docker compose down
```

Esto detiene y elimina los contenedores sin borrar volúmenes persistentes.

---

### 📦 Extras opcionales

- Para reconstruir desde cero:  
  ```bash
  docker compose build --no-cache
  ```

- Para ver logs en tiempo real:  
  ```bash
  docker compose logs -f
  ```

- Para probar escritura manual:  
  ```bash
  docker exec -it samanbooks touch /app/instance/test.txt
  ```
