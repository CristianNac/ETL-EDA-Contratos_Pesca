# Análisis de Contratos de Pesca

Proyecto de análisis de datos sobre empleo en plantas de procesamiento pesquero en Chile (2005-2011).

## 📋 Descripción

Este proyecto analiza los datos históricos de empleo en plantas de procesamiento pesquero, proporcionando insights sobre la evolución del sector pesquero chileno durante el período 2005-2011.

## 🏗️ Estructura del Proyecto

```
analisis-contratos-pesca/
├── src/                          # Código fuente
│   ├── config/                   # Configuraciones
│   │   ├── data.py              # Configuración de datos
│   │   └── db.py                # Configuración de base de datos
│   └── ETL/                     # Pipeline de datos
│       ├── data/                # Archivos CSV (2005-2011)
│       ├── extract.py           # Extracción de datos
│       ├── transform.py         # Transformación de datos
│       └── persist.py           # Persistencia de datos
├── notebooks-eda/              # Análisis exploratorio
│   └── eda_modelado_contratos.ipynb
├── docker-compose.yml          # Configuración Docker
├── Makefile                    # Comandos automatizados
└── pyproject.toml             # Dependencias y configuración
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.11+
- Poetry
- Docker (opcional)

### Configuración del entorno

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd analisis-contratos-pesca
   ```

2. **Instalar dependencias**
   ```bash
   poetry install
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

## 🔧 Uso

### Comandos disponibles (Makefile)

```bash
# Ver ayuda
make help

# Limpiar cache
make clean

# Revisar código con ruff
make lint

# Extraer datos desde CSV
make extract

# Transformar datos
make transform

# Ejecutar pipeline ETL completo
make etl
```

### Pipeline de datos

1. **Extracción**: Carga datos desde archivos CSV (2005-2011)
2. **Transformación**: Limpia y procesa los datos
3. **Persistencia**: Guarda en base de datos PostgreSQL

**Ejecutar pipeline completo:**
```bash
make etl  # Ejecuta todo el proceso ETL de una vez
```

## 📊 Datos

El proyecto trabaja con datos de empleo en plantas de procesamiento pesquero:
- **Período**: 2005-2011
- **Formato**: CSV con encoding latin-1
- **Separador**: punto y coma (;)

### Archivos de datos
- `empleoPlantasDeProceso2005.csv`
- `empleoPlantasDeProceso2006.csv`
- `empleoPlantasDeProceso2007.csv`
- `empleoPlantasDeProceso2008.csv`
- `empleoPlantasDeProceso2009.csv`
- `empleoPlantasDeProceso2010.csv`
- `empleoPlantasDeProceso2011.csv`

## 🛠️ Tecnologías

- **Python 3.11**: Lenguaje principal
- **Pandas**: Manipulación de datos
- **SQLAlchemy**: ORM para base de datos
- **Pydantic**: Validación de configuraciones
- **PostgreSQL**: Base de datos (psycopg2-binary)
- **Ruff**: Linting y formateo
- **Poetry**: Gestión de dependencias
- **Docker**: Containerización

## 📈 Análisis

El notebook `eda_modelado_contratos.ipynb` contiene:
- Análisis exploratorio de datos
- Visualizaciones
- Modelado estadístico
- Insights del sector pesquero

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 👤 Autor

**Cristian Orellana**

---
