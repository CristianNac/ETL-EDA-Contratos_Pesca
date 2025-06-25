import pandas as pd

from config import datasettings


def load_data()->pd.DataFrame:

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

df, df2, df3, df4, df5, df6, df7 = load_data()
print(df7.head())   
