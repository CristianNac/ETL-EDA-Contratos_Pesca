"""
Módulo de extracción de datos para el análisis de contratos de pesca.

Este módulo se encarga de cargar los datos históricos de empleo en plantas
de procesamiento pesquero desde archivos CSV del período 2005-2011.
"""

import pandas as pd

from config import datasettings


def load_data() -> tuple[pd.DataFrame, ...]:
    """
    Carga los datos de empleo en plantas de procesamiento pesquero.
    
    Lee los archivos CSV correspondientes a los años 2005-2011 con datos
    de empleo en plantas de procesamiento pesquero. Cada archivo utiliza
    encoding latin-1 y separador punto y coma.
    
    Returns:
        tuple: Tupla con 7 DataFrames correspondientes a los años 2005-2011.
               Cada DataFrame contiene los datos de empleo de un año específico.
    
    Raises:
        FileNotFoundError: Si algún archivo CSV no se encuentra.
        pd.errors.EmptyDataError: Si algún archivo está vacío.
        UnicodeDecodeError: Si hay problemas con el encoding latin-1.
    
    Example:
        >>> df_2005, df_2006, *otros = load_data()
        >>> print(f"Registros 2005: {len(df_2005)}")
    """

    df = pd.read_csv(f'{datasettings.data_directory}/'
                     f'{datasettings.data_2005}',
                     encoding='latin-1',
                     sep=';',)
    
    df2 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2006}',
                      encoding='latin-1',
                      sep=';',)
    
    df3 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2007}',
                      encoding='latin-1',
                      sep=';',)
    
    df4 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2008}',
                      encoding='latin-1',
                      sep=';',)
    
    df5 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2009}',
                      encoding='latin-1',
                      sep=';',)
    
    df6 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2010}',
                      encoding='latin-1',
                      sep=';',)
    
    df7 = pd.read_csv(f'{datasettings.data_directory}/'
                      f'{datasettings.data_2011}',
                      encoding='latin-1',
                      sep=';',)
    
    
    
    return df, df2, df3, df4, df5, df6, df7

