"""
Módulo de persistencia de datos para el análisis de contratos de pesca.

Este módulo se encarga de guardar los datos transformados en la base de datos
PostgreSQL, manejando la creación de tablas y la inserción de registros.
"""

import pandas as pd
from sqlalchemy import text

from config.db import engine
from ETL.transform import transform_data


def save_to_database(df: pd.DataFrame, table_name: str = "empleo_plantas_procesamiento") -> None:
    """
    Guarda el DataFrame transformado en la base de datos PostgreSQL.
    
    Inserta los datos limpios y transformados en la tabla especificada.
    Si la tabla no existe, la crea automáticamente basándose en el esquema
    del DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos transformados a guardar.
        table_name (str): Nombre de la tabla donde guardar los datos.
                         Por defecto 'empleo_plantas_procesamiento'.
    
    Raises:
        sqlalchemy.exc.SQLAlchemyError: Si hay problemas de conexión o SQL.
        ValueError: Si el DataFrame está vacío.
    
    Example:
        >>> data_clean = transform_data()
        >>> save_to_database(data_clean)
        >>> print("Datos guardados exitosamente")
    """
    if df.empty:
        raise ValueError("El DataFrame está vacío, no hay datos para guardar")
    
    # Guardar datos en PostgreSQL
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',  # Reemplaza la tabla si existe
        index=False,
        method='multi'  # Inserción optimizada por lotes
    )


def create_indexes(table_name: str = "empleo_plantas_procesamiento") -> None:
    """
    Crea índices en la tabla para optimizar las consultas.
    
    Crea índices en las columnas más utilizadas para mejorar el rendimiento
    de las consultas de análisis.
    
    Args:
        table_name (str): Nombre de la tabla donde crear los índices.
    
    Raises:
        sqlalchemy.exc.SQLAlchemyError: Si hay problemas ejecutando el SQL.
    """
    with engine.connect() as conn:
        # Índice por año para consultas temporales
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_año ON {table_name} (\"Año\")"))
        
        # Índice por región para análisis geográfico
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_region ON {table_name} (\"Región\")"))
        
        # Índice por categoría para análisis de tipos de empleo
        conn.execute(text(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_categoria ON {table_name} (\"Categoría\")"))
        
        conn.commit()


def persist_data() -> None:
    """
    Ejecuta el proceso completo de persistencia de datos.
    
    Transforma los datos y los guarda en la base de datos, creando
    también los índices necesarios para optimizar las consultas.
    
    Raises:
        Exception: Si hay algún error en el proceso de persistencia.
    
    Example:
        >>> persist_data()
        >>> print("Pipeline de persistencia completado")
    """
    try:
        # Transformar datos
        data_clean = transform_data()
        
        # Guardar en base de datos
        save_to_database(data_clean)
        
        # Crear índices
        create_indexes()
        
        print(f"Datos persistidos exitosamente: {len(data_clean)} registros")
        
    except Exception as e:
        print(f"Error en el proceso de persistencia: {e}")
        raise


if __name__ == "__main__":
    persist_data()