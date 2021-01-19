
import streamlit as st
from vega_datasets import data
import altair as alt
import time 


@st.cache #se pone delante de una función. Si no cambian los parámetros de entrada la función la cachea
def get_cars():
    time.sleep(3) #estamos simulando la carga del dataset
    return data.cars()


@st.cache
def get_subset(origin, df):
    time.sleep(5)
    return df[df['Origin']==country]

name = st.text_input('¿Cómo te llamas')
country = st.selectbox('¿De qué país quieres ver datos', ['USA', 'Europe', 'Japan'])

st.write('# Bienvenidos a mi app')

cars = get_cars()
subset = get_subset(country, cars)

my_chart = alt.Chart(subset).mark_point().encode(x='Displacement', y='Horsepower')

st.altair_chart(my_chart)

st.write('Gracias por visitarnos, %s' % name)
