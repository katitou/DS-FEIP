import pandas as pd


class ResidentialDataSource:
    __data_set_path = 'src/data_set.xlsx'

    def write(self, df: pd.DataFrame, sheet_name: str):
        with pd.ExcelWriter(self.__data_set_path, engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, index=False, sheet_name=sheet_name)

    def fetch_data_set(self) -> pd.DataFrame:
        table = pd.read_excel(self.__data_set_path)

        data_frame = pd.DataFrame(table)

        return data_frame