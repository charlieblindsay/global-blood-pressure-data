# TODO: Write Comments

import pandas as pd
from utilities.data_cleaning import change_dataframe_structure, remove_range
from utilities.file_paths import raw_data_path, processed_data_path

df = pd.read_csv(raw_data_path / 'BMI_data.csv')

df = df[['Period', 'Location', 'Dim1', 'SpatialDimValueCode', 'Value']]
df.columns = ['Year', 'Country', 'Gender', 'Country_Code', 'BMI']

df = df[df.Gender == 'Both sexes']
df = df.drop('Gender', axis=1)

df = df[df.BMI != 'No data']

df.BMI = df.BMI.apply(remove_range)

df.BMI = pd.to_numeric(df.BMI)

countries = df.Country.unique()
years = df.Year.unique()
years.sort()

df = change_dataframe_structure(df)

df.to_csv(processed_data_path / 'BMI_data.csv', index=False)