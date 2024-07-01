import pandas as pd
import os

def run():
    price_matrix = pd.read_excel('../src/price_matrix.xlsx')
    residental_complex = pd.read_excel('../src/residential_complex_transposed.xlsx')

    price_matrix_df = pd.DataFrame(price_matrix)

    price_matrix_df['ЖК'] = [price_matrix_df['Проект'][i] + ' ' + str(price_matrix_df['Корпус'][i]) for i in range(len(price_matrix_df['Проект']))]
    price_matrix_df.to_excel('../src/price_matrix_m.xlsx')

    price_matrix = pd.read_excel('../src/price_matrix_m.xlsx')

    # left join
    merged_df = price_matrix.merge(residental_complex, how='left', on='ЖК')
    merged_df.to_excel('../src/data_set.xlsx')

    # inner join
    merged_inner_df = price_matrix.merge(residental_complex, how='inner', on='ЖК')
    merged_inner_df.to_excel('../src/merged_inner.xlsx')

    os.remove('../src/price_matrix_m.xlsx')


run()