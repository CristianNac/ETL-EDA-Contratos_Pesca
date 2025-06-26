"""
Configuración de datos para el proyecto de análisis de contratos de pesca.

Este módulo define la configuración para acceder a los archivos de datos
CSV que contienen información histórica de empleo en plantas de procesamiento
pesquero del período 2005-2011.
"""

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataSettings(BaseSettings):
    """
    Configuración de rutas y nombres de archivos de datos.
    
    Esta clase maneja la configuración de acceso a los archivos CSV
    que contienen los datos de empleo en plantas de procesamiento pesquero.
    Las configuraciones se cargan desde variables de entorno definidas
    en el archivo .env.
    
    Attributes:
        data_directory (DirectoryPath): Directorio donde se encuentran los archivos CSV.
        data_2005 (str): Nombre del archivo CSV para el año 2005.
        data_2006 (str): Nombre del archivo CSV para el año 2006.
        data_2007 (str): Nombre del archivo CSV para el año 2007.
        data_2008 (str): Nombre del archivo CSV para el año 2008.
        data_2009 (str): Nombre del archivo CSV para el año 2009.
        data_2010 (str): Nombre del archivo CSV para el año 2010.
        data_2011 (str): Nombre del archivo CSV para el año 2011.
    """
    model_config =  SettingsConfigDict(env_file='.env',
                                       env_file_encoding='utf-8',
                                       extra='ignore')
    
    data_directory:DirectoryPath
    data_2005:str
    data_2006:str
    data_2007:str
    data_2008:str
    data_2009:str
    data_2010:str
    data_2011:str

# Instancia global de configuración de datos
datasettings = DataSettings()