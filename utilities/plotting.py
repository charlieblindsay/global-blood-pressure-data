#TODO: Add docstrings to all functions

import pandas as pd
import streamlit as st
import plotly.express as px

def plot_chloropleth(data_file_path: str, 
                     year_range: tuple, 
                     default_year: int, 
                     chloropleth_subheader: str, 
                     df_single_continent: pd.DataFrame, 
                     df_country_codes: pd.DataFrame) -> None:
    
    min_year, max_year = year_range
    
    df = pd.read_csv(data_file_path)
    
    year = st.slider('Choose year', min_value=min_year, max_value=max_year, value=default_year, step=1)

    df = df.set_index('Year')
    df_single_year = pd.DataFrame({'Level': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'Level']

    df_merge = pd.merge(df_single_year, df_country_codes, on='Country', how='left')
    df_merge = pd.merge(df_single_continent, df_merge, on='Country_Code', how='left')

    chloropleth_subheader = chloropleth_subheader + f' in {year}'
    st.subheader(chloropleth_subheader)
    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="Level",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        center={'lat': 50, 'lon': 14})

    st.plotly_chart(fig)