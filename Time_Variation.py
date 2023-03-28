import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from utilities.file_paths import processed_data_path
from utilities.plotting import plot_variation_against_time

st.title('How have Alcohol consumption, BMI and GDP per capita varied in the last 50 years?')

df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')
df_BMI = pd.read_csv(processed_data_path / 'BMI_data.csv')
df_population = pd.read_csv(processed_data_path / 'population_data.csv')
df_GDP = pd.read_csv(processed_data_path / 'GDP_data.csv')

countries = list(df_BMI.columns[1:])

selected_countries = st.multiselect('Select Countries', countries)

try:
    selected_data = st.radio('Choose which data you want to see', options=['Alcohol Consumption', 'BMI', 'Population', 'GDP per capita'], index=0)

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
                                    xticklabels=['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015'])
    
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