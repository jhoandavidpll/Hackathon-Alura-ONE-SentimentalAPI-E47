import streamlit as st
from menu import generar_menu # Importamos nuestra función

st.set_page_config(page_title="Inicio", layout="wide")

# Llamamos al menú antes de cualquier otra cosa
generar_menu()

st.title("Bienvenido a ..")
# ... resto de tu código


st.write("# Inicio")

st.write("SentimentAPI")

idioma = st.radio("Seleccione el Idioma para la reseña", ["Español", "Portuguese"])

texto_ingresado = st.text_input("Ingrese texto")

st.write(f"Texto ingresado: {texto_ingresado}")

boton = st.button("Clic aquí")




