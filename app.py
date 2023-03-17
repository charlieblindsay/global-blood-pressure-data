import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('processed_data.csv')

plt.figure(figsize=(10,6))
plt.title("How blood pressure has varied in different countries between 1975 and 2015")
plt.xlabel('Year')
plt.ylabel('Average blood pressure (age-standardized)')

countries = list(df.columns[1:-3]) # Choose the first 188 countries so is divisible by 4

st.title('How does Blood Pressure vary by country?')
st.write('Find GitHub repository here: https://github.com/charlieblindsay/global-blood-pressure-data')
st.subheader('Steps to use this app:')
st.write('1. Select countries below.')
st.write('2. Click \'See blood pressure plots\' tab on the left to see how the average blood pressure of citizens in each country has varied against time.')
st.subheader('Country selection')

num_cols = 4
cols = st.columns(num_cols)

num_countries = len(countries)
num_countries_per_column = int(num_countries / num_cols)
countries_array = np.array(countries).reshape(num_cols,num_countries_per_column).transpose()
n,m = countries_array.shape

for i in range(n):
    for j in range(m):
        cols[j].checkbox(countries_array[i, j], key='dynamic_checkbox_' + countries_array[i, j])

