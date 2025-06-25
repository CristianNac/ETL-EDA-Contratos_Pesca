"""

"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine

class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',
                                      extra='ignore')
    
    postgres_user:str
    postgres_password:str
    postgres_host:str
    postgres_db:str

# Inicializar DbSettings
dbsettings = DbSettings()

# Crear database engine

engine = create_engine(f"postgresql://{dbsettings.postgres_user}:"
                       f"{dbsettings.postgres_password}@" 
                       f"{dbsettings.postgres_host}/"
                       f"{dbsettings.postgres_db}"
                       )



