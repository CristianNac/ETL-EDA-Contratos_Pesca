"""
Paquete ETL para el análisis de contratos de pesca.

Este paquete contiene todos los módulos necesarios para el pipeline ETL
(Extract, Transform, Load) que procesa los datos históricos de empleo
en plantas de procesamiento pesquero del período 2005-2011.

Módulos:
    extract: Extracción de datos desde archivos CSV
    transform: Transformación y limpieza de datos
    persist: Persistencia de datos en base de datos PostgreSQL
"""

from .extract import load_data
from .transform import transform_data
from .persist import persist_data, save_to_database

__all__ = ['load_data', 'transform_data', 'persist_data', 'save_to_database']