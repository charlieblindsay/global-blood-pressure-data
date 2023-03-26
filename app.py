import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from utilities.file_paths import processed_data_path

st.title('How have Alcohol consumption and BMI varied in the last 50 years?')

df_blood_pressure = pd.read_csv(processed_data_path / 'BMI_data.csv')
df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')

countries = list(df_blood_pressure.columns[1:])

selected_countries = st.multiselect('Select Countries', countries)

try:
    selected_data = st.radio('Choose to see BMI or Alcohol consumption data', options=['BMI', 'Alcohol Consumption'], index=0)

    if selected_data == 'BMI':
        fig = sns.lineplot(data=df_blood_pressure[selected_countries])
        st.header("How has BMI varied over time?")
        plt.xlabel('Year')
        plt.ylabel('BMI')
        fig.set_xticklabels(['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015'])
    
    if selected_data == 'Alcohol Consumption':
        fig = sns.lineplot(data=df_alcohol[selected_countries])
        st.header("How has Alcohol Consumption varied over time?")
        plt.xlabel('Year')
        plt.ylabel('Alcohol consumption per capita (in litres of pure alcohol per year)')
        fig.set_xticklabels(['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020'])

    st.pyplot(plt.gcf())

except TypeError:
    st.warning('No countries selected. Click on \'Choose an option\' above to search for them')