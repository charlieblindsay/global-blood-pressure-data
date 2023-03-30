import pandas as pd

from utilities.file_paths import processed_data_path

df_population = pd.read_csv(processed_data_path / 'population_data.csv')
df_gdp = pd.read_csv(processed_data_path / 'GDP_data.csv')
df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')
df_BMI = pd.read_csv(processed_data_path / 'BMI_data.csv')

years = df_BMI.Year.values
countries = df_BMI.columns[1:]

df_dict = {'Population': df_population, 'GDP_per_capita': df_gdp, 'Alcohol_Consumption': df_alcohol, 'BMI': df_BMI}

dict = {'Country': [], 'Year': [], 'Population': [], 'GDP_per_capita': [], 'Alcohol_Consumption': [], 'BMI': []}

for country in countries:
    for year in years:
        dict['Country'].append(country)
        dict['Year'].append(year)

        for column_name in df_dict:
            df = df_dict[column_name]
            dict[column_name].append(df[df.Year == year][country].iloc[0])

df_population_SQL = pd.DataFrame(dict)
df_population_SQL.to_csv(processed_data_path / 'data_SQL.csv', index=False)