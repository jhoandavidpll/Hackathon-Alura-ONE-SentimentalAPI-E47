import streamlit as st
from menu import generar_menu # Importamos nuestra función

st.set_page_config(page_title="Inicio", layout="wide")

# Llamamos al menú antes de cualquier otra cosa
generar_menu()

st.title("Bienvenido a la página de Inicio")
# ... resto de tu código


st.write("# Inicio")

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
