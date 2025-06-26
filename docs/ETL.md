# Documentación del Pipeline ETL

## Descripción General

El pipeline ETL (Extract, Transform, Load) procesa los datos históricos de empleo en plantas de procesamiento pesquero desde archivos CSV hacia una base de datos estructurada.

## Módulos

### 1. Extract (`extract.py`)

**Propósito**: Extrae datos desde archivos CSV del período 2005-2011.

**Función principal**: `load_data()`
- Carga 7 archivos CSV correspondientes a cada año
- Utiliza encoding `latin-1` y separador `;`
- Retorna 7 DataFrames de pandas

### 2. Transform (`transform.py`)

**Propósito**: Limpia, valida y transforma los datos extraídos.

### 3. Persist (`persist.py`)

**Propósito**: Persiste los datos transformados en la base de datos.

## Uso

```bash
# Extraer datos
make extract

# Transformar datos
make transform

# Pipeline ETL completo
make etl
```

## Configuración

Variables de entorno requeridas en `.env`:
- `DATA_DIRECTORY`: Directorio de archivos CSV
- `DATA_2005` a `DATA_2011`: Nombres de archivos por año
- Configuración de base de datos PostgreSQL