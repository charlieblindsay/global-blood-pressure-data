#TODO: Add docstrings to all functions

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

from utilities.file_paths import processed_data_path

def plot_variation_against_time(df: pd.DataFrame, 
                                variable_name: str, 
                                selected_countries: list,
                                xticklabels: list,
                                ylabel: str = None):
    
    fig = sns.lineplot(data=df[selected_countries])
    st.header(f'How has {variable_name} varied over time?')
    plt.xlabel('Year')
    if ylabel != None:
        plt.ylabel(ylabel)
    else:
        plt.ylabel(variable_name.capitalize())
    fig.set_xticklabels(xticklabels)

def plot_chloropleth(data_file_path: str, 
                     year_range: tuple, 
                     default_year: int, 
                     chloropleth_subheader: str) -> None:
    
    df_country_codes_who = pd.read_csv(processed_data_path / 'country_codes_who.csv')
    
    min_year, max_year = year_range
    
    df = pd.read_csv(data_file_path)
    
    year = st.slider('Choose year', min_value=min_year, max_value=max_year, value=default_year, step=1)

    df = df.set_index('Year')
    df_single_year = pd.DataFrame({'Level': df.loc[year]})
    df_single_year = df_single_year.reset_index()
    df_single_year.columns = ['Country', 'Level']

    df_merge = pd.merge(df_single_year, df_country_codes_who, on='Country', how='left')

    chloropleth_subheader = chloropleth_subheader + f' in {year}'
    st.subheader(chloropleth_subheader)
    fig = px.choropleth(df_merge, locations="Country_Code",
                        color="Level",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        center={'lat': 50, 'lon': 14})

    st.plotly_chart(fig)