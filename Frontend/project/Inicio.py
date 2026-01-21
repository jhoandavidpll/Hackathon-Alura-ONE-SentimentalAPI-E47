
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


import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Analizador de Sentimiento", layout="centered")

# --- ESTILOS CSS PERSONALIZADOS ---
from funciones import *
estilo()

# --- CONTENIDO ---
# Usamos un div para envolver los widgets de Streamlit
st.write("Selecciona el Idioma")

tipo = st.selectbox("Primero, selecciona el tipo:", ["Simple", "Batch"])

comentario = st.text_area("Segundo, ingresa el comentario:", 
                          placeholder="Ej: Este es el mejor PITCH...",
                          height=150)

with st.expander("⚙️ Opciones "):
    st.checkbox("")
    st.checkbox("Detectar idioma")

if st.button("ENVIAR COMENTARIO"):
    st.success("Procesando...")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; color: white; margin-top: 30px; font-size: 0.8em;">
        Desarrollado por E47 | 
    </div>
    """, unsafe_allow_html=True)



