"""
Configuración de base de datos para el proyecto de análisis de contratos de pesca.

Este módulo maneja la configuración y conexión a la base de datos PostgreSQL
utilizada para almacenar los datos procesados del análisis de empleo en
plantas de procesamiento pesquero.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine

class DbSettings(BaseSettings):
    """
    Configuración de conexión a la base de datos PostgreSQL.
    
    Esta clase maneja los parámetros de conexión a la base de datos
    PostgreSQL donde se almacenan los datos procesados. Las configuraciones
    se cargan desde variables de entorno definidas en el archivo .env.
    
    Attributes:
        postgres_user (str): Usuario de PostgreSQL.
        postgres_password (str): Contraseña de PostgreSQL.
        postgres_host (str): Host del servidor PostgreSQL.
        postgres_db (str): Nombre de la base de datos.
    """
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')
    
    postgres_user:str
    postgres_password:str
    postgres_host:str
    postgres_db:str

# Instancia global de configuración de base de datos
dbsettings = DbSettings()

# Motor de base de datos SQLAlchemy para PostgreSQL
engine = create_engine(
    f"postgresql://{dbsettings.postgres_user}:"
    f"{dbsettings.postgres_password}@"
    f"{dbsettings.postgres_host}/"
    f"{dbsettings.postgres_db}"
)



