"""

"""

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataSettings(BaseSettings):
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

datasettings = DataSettings()