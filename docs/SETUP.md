# Guía de Configuración

## Instalación paso a paso

### 1. Prerrequisitos
- Python 3.11+
- Poetry
- PostgreSQL (opcional con Docker)

### 2. Configuración inicial

```bash
# Clonar repositorio
git clone <url-repositorio>
cd analisis-contratos-pesca

# Instalar dependencias
poetry install

# Copiar configuración
cp .env.example .env
```

### 3. Configurar variables de entorno

Editar `.env` con tus valores:

```env
DATA_DIRECTORY=src/ETL/data
DATA_2005=empleoPlantasDeProceso2005.csv
# ... otros archivos

DB_HOST=localhost
DB_PORT=5432
DB_NAME=contratos_pesca
DB_USER=tu_usuario
DB_PASSWORD=tu_password
```

### 4. Base de datos (con Docker)

```bash
# Levantar PostgreSQL
docker-compose up -d

# Verificar conexión
poetry run python -c "from config.db import engine; print('Conexión exitosa')"
```

### 5. Ejecutar pipeline

```bash
# Pipeline completo (recomendado)
make etl

# O paso a paso:
make extract    # Solo extraer
make transform  # Solo transformar
```

## Solución de problemas

### Error de encoding
Si encuentras errores de caracteres, verifica que los CSV usen encoding `latin-1`.

### Error de conexión DB
Verifica que PostgreSQL esté ejecutándose y las credenciales sean correctas.

### Error de dependencias
```bash
poetry install --no-dev  # Solo dependencias principales
```