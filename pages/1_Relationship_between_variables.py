import streamlit as st
import plotly.express as px
import pandas as pd
from utilities.file_paths import raw_data_path, processed_data_path

st.title('What is the relationship between BMI and alcohol consumption?')

df_alcohol = pd.read_csv(processed_data_path / 'alcohol_data.csv')
df_bmi = pd.read_csv(processed_data_path / 'BMI_data.csv')
df_country_code = pd.read_csv(processed_data_path / 'country_codes.csv')

df_alcohol = df_alcohol.set_index('Year')
df_bmi = df_bmi.set_index('Year')

year = st.slider('Choose year', min_value=1975, max_value=2015, value=2015, step=1)

df_a_single_year = pd.DataFrame({'Alcohol': df_alcohol.loc[year]})
df_bmi_single_year = pd.DataFrame({'BMI': df_bmi.loc[year]})

df_a_single_year = df_a_single_year.reset_index()
df_a_single_year.columns = ['Country', 'Alcohol Consumption per Capita (in pure litres of alcohol per year)']

df_bmi_single_year = df_bmi_single_year.reset_index()
df_bmi_single_year.columns = ['Country', 'Average BMI']

df_a_single_year = pd.merge(df_a_single_year, df_country_code, on='Country', how='left')

df_merge = pd.merge(df_a_single_year, df_bmi_single_year, on='Country')

df_merge = df_merge.dropna()

df_continents = pd.read_csv(raw_data_path / 'continent_data.csv')
df_continents = df_continents[['alpha-3', 'sub-region', 'region']]
df_continents.columns = ['Country_Code', 'sub-region', 'Continent']

df_merge = pd.merge(df_merge, df_continents, how='left', on='Country_Code')

if year == 2015:
    st.subheader('Try to analyse the data! Click below to see if you got the same analysis points as me')
    with st.expander("See my analysis of the 2015 data"):
        st.write("""
            - There are 7 countries with an average BMI of 30 kg/m^2 or more; they are all from Micronesia or Polynesia, which are islands in Oceania! This makes the average person there obese.
            - Countries in Europe have widely varied alcohol consumption, but similar average BMI.
            - Estonians drink the most alcohol.
            - The data points of Africa and Asia, as well as Europe and Americas are clustered together.
        """)

st.subheader(f'Relationship between BMI and Alcohol Consumption for countries across the globe in {year}')
fig = px.scatter(df_merge, x="Alcohol Consumption per Capita (in pure litres of alcohol per year)", y="Average BMI",
                 hover_data=['Country', 'sub-region'], color='Continent')

st.plotly_chart(fig)