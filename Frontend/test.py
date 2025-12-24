import streamlit as st

st.write("Hola")

texto_ingresado = st.text_input("Ingrese texto")

st.write(f"Texto ingresado: {texto_ingresado}")

boton = st.button("Clic aquí")

st.write("## Este un título H2")

# importar datos
import pandas as pd

data = pd.read_csv()

