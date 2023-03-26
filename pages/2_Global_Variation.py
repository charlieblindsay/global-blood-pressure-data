import streamlit as st
import pandas as pd
from utilities.file_paths import processed_data_path, raw_data_path
from utilities.plotting import plot_chloropleth

st.title('How does Alcohol consumption and Blood Pressure vary by country?')

df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
df_continents = df_continents[['alpha-3', 'region']]
df_continents.columns = ['Country_Code', 'region']

selected_continent = st.radio('Choose which continent\'s data will be shown', options=df_continents.region.unique()[:-1], index=0)
df_single_continent = df_continents[df_continents.region == selected_continent]

selected_data = st.radio('Choose to see blood pressure or alcohol data', options=['Alcohol', 'Blood Pressure'], index=0)

df_country_codes = pd.read_csv(processed_data_path / 'country_codes.csv')

if selected_data == 'Alcohol':
    plot_chloropleth(data_file_path=processed_data_path / 'alcohol_data.csv',
                    year_range=(1960, 2019), 
                    default_year=2002, 
                    chloropleth_subheader='Chloropleth showing how alcohol consumption per capita (in pure litres of alcohol consumed per year) varied across the globe',
                    df_country_codes=df_country_codes,
                    df_single_continent=df_single_continent)

if selected_data == 'Blood Pressure':
    plot_chloropleth(data_file_path=processed_data_path / 'BMI_data.csv',
                    year_range=(1975, 2015), 
                    default_year=2000, 
                    chloropleth_subheader="Chloropleth showing how average blood pressure varied across the globe",
                    df_country_codes=df_country_codes,
                    df_single_continent=df_single_continent)