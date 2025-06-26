"""
Módulo de transformación de datos para el análisis de contratos de pesca.

Este módulo se encarga de limpiar, normalizar y transformar los datos
cargados desde los archivos CSV para prepararlos para el análisis y
almacenamiento en la base de datos.
"""

import pandas as pd

from ETL.extract import load_data

def transform_data() -> pd.DataFrame:
    """
    Transforma y limpia los datos de empleo en plantas de procesamiento pesquero.
    
    Aplica una serie de transformaciones a los datos cargados desde los archivos CSV:
    - Corrige el formato numérico de la columna 'Ocupados' para el año 2010
    - Concatena todos los DataFrames en uno solo
    - Normaliza la categoría 'SUB-CONTRATO' a 'SUBCONTRATO'
    - Limpia y normaliza la columna 'Función'
    - Elimina columnas con más del 50% de valores nulos
    
    Returns:
        pd.DataFrame: DataFrame consolidado y limpio con todos los datos
                     del período 2005-2011.
    
    Raises:
        ValueError: Si hay problemas en la conversión de tipos de datos.
        KeyError: Si alguna columna esperada no existe en los datos.
    
    Example:
        >>> data_clean = transform_data()
        >>> print(f"Registros totales: {len(data_clean)}")
        >>> print(f"Años disponibles: {data_clean['Año'].unique()}")
    """
    df, df2, df3, df4, df5, df6, df7 = load_data()

    # Transformación para la data del año 2010
    df6['Ocupados'] = df6['Ocupados'].str.replace(',','.')
    df6['Ocupados'] = df6['Ocupados'].astype('float')
    df6['Ocupados'] = df6['Ocupados'].astype('int')

    # Unión de tablas
    lista_df = [df, df2, df3, df4, df5, df6,df7]
    data = pd.concat(lista_df)

    # Transformación para corregir error en el nombre de la categoría Sub-contrato
    data['Categoría'] = data['Categoría'].str.replace('SUB-CONTRATO','SUBCONTRATO')

    # Transformación de la columna Función

    data['Función'] = data['Función'].str.strip()
    data['Función'] = data['Función'].str.lower()
    data['Función'] = data['Función'].str.capitalize()
    data['Función'] = data['Función'].str.replace('_',' ')

    # Eliminación de columnas con más del 50% de nulos

    data = data.drop(columns = ['EXPLICACIÓN_CLASE_INDUSTRIA','COMEN'])

    return data

