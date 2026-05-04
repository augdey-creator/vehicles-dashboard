import pandas as pd
import plotly.express as px
import streamlit as st

# Título
st.header("Dashboard de Autos en Venta")

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón histograma
# hist_button = st.button('Construir histograma')

# if hist_button:
if st.checkbox('Mostrar histograma'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón scatter
# scatter_button = st.button('Construir gráfico de dispersión')

# if scatter_button:
if st.checkbox('Mostrar scatter'):
    st.write('Relación entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
