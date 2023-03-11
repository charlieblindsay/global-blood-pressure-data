import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('processed_data.csv')

selected_countries = [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]

# lst = [int(df.index[i]) for i in range(0, 41, 5)]
# plt.xticks(lst)

try:
    fig = sns.lineplot(data=df[selected_countries])
    fig.set_xticklabels(['1970', '1975', '1980', '1985', '1990', '1995', '2000', '2005', '2010', '2015'])
    st.pyplot(plt.gcf())
except TypeError:
    st.warning('No countries selected. Please select countries by clicking on \'Country selection\' in the sidebar.')