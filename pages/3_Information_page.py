import streamlit as st
from PIL import Image

st.title('Want to see my code? Click below:')
st.subheader('[GitHub Repo](https://github.com/charlieblindsay/World-Health-Data)')

st.subheader('Purpose of the app')
st.write('It allows users to interactively explore data from the World Health Organisation')

st.subheader('Purpose of different pages')
st.write('1. Time Variation: For the countries selected, the selected dependent variable is plotted against time')
st.write('2. Relationship between Variables: For the year selected, the 2 selected dependent variables are plotted against each other')
st.write('3. Global Variation: A chloropleth shows how alcohol consumption varied across the globe in the year 2000')

st.subheader('What does BMI mean?')
st.write('Body Mass Index (BMI) gives an indication of whether a person\'s weight is healthy. It is a person\'s weight (in kilograms) divided by their height (in metres) squared.')
img = Image.open('images/bmi.png')
st.image(img)

st.subheader('What are healthy levels of alcohol consumption?')
st.write('According to the [NHS](https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units/), the maximum amount people should drink is 14 units per week, which equates to around 8 litres of pure alcohol per year.')

st.subheader('Data Sources')
st.write('Both datasets are from the WHO website:')
st.write("- [BMI data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/mean-bmi-(kg-m-)-(age-standardized-estimate))")
st.write("- [Alcohol data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol))")

st.write('I originally used this data as part of a \'Data Visuzalization\' section in a [Python course](https://icsm-python-course.netlify.app/) I created.')