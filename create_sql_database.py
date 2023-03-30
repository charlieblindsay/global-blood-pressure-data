from utilities.file_paths import sql_path, processed_data_path
import sqlite3
import pandas as pd

conn = sqlite3.connect(sql_path / 'database')
c = conn.cursor()

c.execute(f'CREATE TABLE IF NOT EXISTS Country_Table (Country text, Year number, Population number, GDP_per_capita number, Alcohol_Consumption number, BMI number)')

df_all_variables = pd.read_csv(processed_data_path / 'data_SQL.csv')

df_all_variables.to_sql('Country_Table', conn, if_exists='replace', index = False)
conn.commit()

