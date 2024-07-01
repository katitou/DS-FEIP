import pandas as pd
import os


class ResidentialDataSource:
    def __init__(self, data_set_path: str = 'stc/data_set.xlsx'):
        self.__data_set_path = data_set_path
    # __data_set_path = 'src/data_set.xlsx'

    def write(self, df: pd.DataFrame, sheet_name: str):
        with pd.ExcelWriter(self.__data_set_path, engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, index=False, sheet_name=sheet_name)

    def fetch_data_set(self) -> pd.DataFrame:
        if self.__data_set_path.endswith('.xlsx'):
            table = pd.read_excel(self.__data_set_path)
        elif self.__data_set_path.endswith('.csv'):
            table = pd.read_csv(self.__data_set_path)
            
        data_frame = pd.DataFrame(table)
        return data_frame
    
    @staticmethod
    def save_excel(df: pd.DataFrame, filename: str):
        file_path =  os.path.join('src', filename)
        df.to_excel(file_path, index=False)

    @staticmethod
    def save_csv(df:pd.DataFrame, filename: str):
        file_path = os.path.join('src', filename)
        df.to_csv(file_path, index=False)

