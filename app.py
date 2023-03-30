import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sqlite3

from utilities.file_paths import processed_data_path, sql_path
from utilities.plotting import plot_variation_against_time

st.title('How have Alcohol consumption, BMI and GDP per capita varied in the last 50 years?')

df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')
df_BMI = pd.read_csv(processed_data_path / 'BMI_data.csv')
df_population = pd.read_csv(processed_data_path / 'population_data.csv')
df_GDP = pd.read_csv(processed_data_path / 'GDP_data.csv')

countries = list(df_BMI.columns[1:])

selection_mode = st.radio('Choose your country selection mode', options=['Manual Selection', 'Selection with SQL query'], index=1)

if selection_mode == 'Manual Selection':
    selected_countries = st.multiselect('Select Countries', countries)

if selection_mode == 'Selection with SQL query':
    conn = sqlite3.connect(sql_path / 'database')
    c = conn.cursor()

    with st.expander("Tips for your writing an SQL query"):
        st.write('For your SQL query, the 5 columns in Country_Table are \'Country\', \'BMI\', \'Alcohol_Consumption\', \'Population\' and \'GDP_per_capita\'')
        st.write('You can substitute the \'BMI\' for any one of these.')
        st.write('Note: When you use \'Country\', since it has type = text, use operators such as \'[LIKE](https://www.w3schools.com/sql/sql_like.asp)\' instead of \'[BETWEEN](https://www.w3schools.com/sql/sql_between.asp)\'.')

    SQL_query = st.text_input('Enter your SQL query', value="""
    SELECT * FROM Country_Table WHERE BMI BETWEEN 30 AND 40
    """)
    
    c.execute(SQL_query)
    
    selected_countries = []

    for row in c.fetchall():
        country = row[0]
        if country not in selected_countries:
            selected_countries.append(country)

try:
    selected_data = st.radio('Choose which data you want to see', options=['BMI', 'Alcohol Consumption', 'Population', 'GDP per capita'], index=0)

    if selected_data == 'Alcohol Consumption':
        plot_variation_against_time(df = df_alcohol, 
                                    variable_name='Alcohol Consumption', 
                                    selected_countries=selected_countries, 
                                    ylabel='Alcohol consumption per capita \n (in litres of pure alcohol per year)',
                                    xticklabels=['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])

    if selected_data == 'BMI':
        plot_variation_against_time(df = df_BMI, 
                                    variable_name='BMI', 
                                    ylabel='Average BMI',
                                    selected_countries=selected_countries, 
                                    xticklabels=['1970', '1975', '1985', '1995', '2005', '2015'])
    
    if selected_data == 'Population':
        plot_variation_against_time(df = df_population, 
                                    variable_name='population', 
                                    selected_countries=selected_countries, 
                                    xticklabels=['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])      
    
    if selected_data == 'GDP per capita':
        plot_variation_against_time(df = df_GDP, 
                            variable_name='GDP per capita', 
                            ylabel='GDP per capita',
                            selected_countries=selected_countries, 
                            xticklabels=['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])      
    
    st.pyplot(plt.gcf())

except TypeError:
    st.warning('No countries selected. Click on \'Choose an option\' above to search for them')