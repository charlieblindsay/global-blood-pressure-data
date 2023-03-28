import streamlit as st
import pandas as pd
from utilities.file_paths import processed_data_path, raw_data_path
from utilities.plotting import plot_chloropleth

st.title('How does Alcohol Consumption, BMI and GDP per capita vary by country?')

df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
df_continents = df_continents[['alpha-3', 'region']]
df_continents.columns = ['Country_Code', 'region']

selected_data = st.radio('Choose which data you want to see', options=['Alcohol Consumption', 'BMI', 'Population', 'GDP per capita' ], index=0)

if selected_data == 'Alcohol Consumption':
    plot_chloropleth(data_file_path=processed_data_path / 'alcohol_data.csv',
                    year_range=(1960, 2019), 
                    default_year=2002, 
                    chloropleth_subheader='Chloropleth showing how alcohol consumption per capita (in pure litres of alcohol consumed per year) varied across the globe')

if selected_data == 'BMI':
    plot_chloropleth(data_file_path=processed_data_path / 'BMI_data.csv',
                    year_range=(1975, 2015), 
                    default_year=2000, 
                    chloropleth_subheader="Chloropleth showing how average blood pressure varied across the globe")
    
if selected_data == 'Population':
    plot_chloropleth(data_file_path=processed_data_path / 'population_data.csv',
                    year_range=(1960, 2021), 
                    default_year=2021, 
                    chloropleth_subheader="Chloropleth showing population variation by country")
    
if selected_data == 'GDP per capita':
    plot_chloropleth(data_file_path=processed_data_path / 'GDP_data.csv',
                    year_range=(1960, 2021), 
                    default_year=2021, 
                    chloropleth_subheader="Chloropleth showing GDP per capita variation by country")





