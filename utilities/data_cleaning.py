#TODO: Add docstrings to all functions

import pandas as pd

def change_dataframe_structure(df: pd.DataFrame) -> pd.DataFrame:
    countries = df.Country.unique()
    years = df.Year.unique()
    years.sort()
    dict = {country: [] for country in countries}
    for country in countries:
        for year in years:
            value = df[df.Country == country][df.Year == year].Alcohol_consumption_per_capita
            if value.empty == True:
                dict[country].append(float('NaN'))
            else:
                dict[country].append(float(df[df.Country == country][df.Year == year].Alcohol_consumption_per_capita))
    df = pd.DataFrame(dict)
    df['Year'] = [i for i in range(years[0], years[-1]+1)]
    
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