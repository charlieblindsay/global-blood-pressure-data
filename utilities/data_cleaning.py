#TODO: Add docstrings to all functions

import pandas as pd
from utilities.file_paths import raw_data_path, processed_data_path

def produce_processed_world_bank_data(file_name: str) -> None:
    df = pd.read_csv(raw_data_path / file_name)
    df_country_codes_who = pd.read_csv(processed_data_path / 'country_codes_who.csv')

    # The World Bank data contains countries not present in WHO datasets.
    # This line removes these countries
    df_merge = pd.merge(df_country_codes_who, df, how='left', left_on='Country_Code', right_on='Country Code')

    df = df_merge.drop(['Country Name', 'Country Code', 'Country_Code', 'Indicator Name', 'Indicator Code'], axis=1)

    if 'Unnamed: 66' in df.columns:
        df = df.drop('Unnamed: 66', axis=1)
        
    df = df.transpose()

    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df.index = [i for i in range(1960, 2022)]

    df.index.name = 'Year'

    df.to_csv(processed_data_path / file_name)

def change_dataframe_structure(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    countries = df.Country.unique()
    years = df.Year.unique()
    years.sort()
    dict = {country: [] for country in countries}
    for country in countries:
        for year in years:
            value = df[df.Country == country][df.Year == year][column_name]
            if value.empty == True:
                dict[country].append(float('NaN'))
            else:
                dict[country].append(float(df[df.Country == country][df.Year == year][column_name]))
    df = pd.DataFrame(dict)
    df['Year'] = pd.Series([i for i in range(years[0], years[-1]+1)])
    
    return df

# Removing rows where alcohol consumption is zero
def check_if_consumption_is_zero(consumption_value) -> bool:
    if consumption_value in [0.0, '0', '0 [0 – 0]', '0.000\xa01']:
        return False
    else:
        return True
    
def convert_consumption_values_to_floats(consumption_value) -> float:
    if isinstance(consumption_value, float):
        return consumption_value
    else:
        if '\xa0' in consumption_value:
            consumption_value = consumption_value.replace('\xa0', '')
        return float(consumption_value.split(' ')[0])
    
def remove_range(cell: str) -> str:
    return cell.split(' ')[0]