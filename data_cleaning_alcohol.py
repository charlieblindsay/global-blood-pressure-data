# TODO: Finish Comments

import pandas as pd
from utilities.data_cleaning import change_dataframe_structure, check_if_consumption_is_zero, convert_consumption_values_to_floats
from utilities.file_paths import raw_data_path, processed_data_path

df=pd.read_csv(raw_data_path / 'alcohol_data.csv')

# Selecting columns of interest
df = df[['Period', 'Location', 'Dim1', 'SpatialDimValueCode', 'Value']]

# Renaming columns
df.columns = ['Year', 'Country', 'Alcohol_Type', 'Country_Code', 'Alcohol_consumption_per_capita']

df_country_codes_who = df[['Country', 'Country_Code']]
df_country_codes_who = df_country_codes_who.drop_duplicates()

df = df.drop('Country_Code', axis=1)

# Selecting only rows which have alcohol type equal to 'all types'
df = df[df.Alcohol_Type == 'All types']

# Remving 'Alcohol_Type' column as it now contains no information
df = df.drop('Alcohol_Type', axis=1)

df = df[df.Alcohol_consumption_per_capita.apply(check_if_consumption_is_zero)]
    
df.Alcohol_consumption_per_capita = df.Alcohol_consumption_per_capita.apply(convert_consumption_values_to_floats)

df = df.sort_values(by=['Country', 'Year'])

df = change_dataframe_structure(df)

df.to_csv(processed_data_path / 'alcohol_data.csv', index=False)
df_country_codes_who.to_csv(processed_data_path / 'country_codes_who.csv', index=False)