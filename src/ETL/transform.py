import pandas as pd

from ETL.extract import load_data

def transform_data():
    df, df2, df3, df4, df5, df6, df7 = load_data()

    #Transformación para la data del año 2010
    df6['Ocupados'] = df6['Ocupados'].str.replace(',','.')
    df6['Ocupados'] = df6['Ocupados'].astype('float')
    df6['Ocupados'] = df6['Ocupados'].astype('int')

    #Unión de tablas
    lista_df = [df, df2, df3, df4, df5, df6,df7]
    data = pd.concat(lista_df)

    #Transformación para corregir error en el nombre de la categoría Sub-contrato
    data['Categoría'] = data['Categoría'].str.replace('SUB-CONTRATO','SUBCONTRATO')

    #Transformación de la columna Función

    data['Función'] = data['Función'].str.strip()
    data['Función'] = data['Función'].str.lower()
    data['Función'] = data['Función'].str.capitalize()
    data['Función'] = data['Función'].str.replace('_',' ')

    #Eliminación de columnas con más del 50% de nulos

    data = data.drop(columns = ['EXPLICACIÓN_CLASE_INDUSTRIA','COMEN'])

    return data

