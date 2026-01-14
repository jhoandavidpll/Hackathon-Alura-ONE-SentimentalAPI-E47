import streamlit as st
from menu import generar_menu # Importamos nuestra función
from langid import classify
from langdetect import detect, DetectorFactory

# Esto hace que el resultado sea siempre el mismo para el mismo texto
DetectorFactory.seed = 0

st.set_page_config(page_title="Inicio", layout="wide")

# Llamamos al menú antes de cualquier otra cosa
generar_menu()
# ... resto de tu código


st.write("# SentimentAPI")

seleccionar_idioma = st.radio("Seleccione el Idioma para la reseña", ["Español", "Portugues", "Automático"])


texto_ingresado = st.text_input("Ingrese texto")

def detectar_idioma(seleccionar_idioma, texto_ingresado):
    try:
        if seleccionar_idioma == "Automático":
            idioma = detect(texto_ingresado)
        elif seleccionar_idioma == "Español":
            idioma = "es"
        elif seleccionar_idioma == "Portugues":
            idioma = "pr"
        else:
            idioma = "Ingrese un texto"
    except:
        idioma = ""
    return idioma

salida = detectar_idioma(seleccionar_idioma, texto_ingresado)

st.write(f"El idioma detectado es: {salida}")

st.write(f"Texto ingresado: {texto_ingresado}")

boton = st.button("Clic aquí")



