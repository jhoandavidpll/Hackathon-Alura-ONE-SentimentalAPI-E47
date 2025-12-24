import streamlit as st

st.write("Hola")

texto_ingresado = st.text_input("Ingrese texto")

st.write(f"Texto ingresado: {texto_ingresado}")

boton = st.button("Clic aquí")

st.write("## Este un título H2")

# importar datos
import pandas as pd
import numpy as np

data = pd.read_csv("/home/jhoan/Documentos/portfolio/Hackathon-Alura-ONE-SentimentalAPI-E47/Data-Science/data/spanish/train.csv")

st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)

