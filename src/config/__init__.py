"""
Paquete de configuración para el proyecto de análisis de contratos de pesca.

Este paquete centraliza todas las configuraciones necesarias para el proyecto,
incluyendo configuraciones de base de datos y acceso a archivos de datos.
"""

from .db import dbsettings, engine
from .data import datasettings

__all__ = ['dbsettings', 'engine', 'datasettings']