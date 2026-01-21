
import streamlit as st
from menu import generar_menu # Importamos nuestra función
from langid import classify
from langdetect import detect, DetectorFactory

# Esto hace que el resultado sea siempre el mismo para el mismo texto
DetectorFactory.seed = 0

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Analizador de Sentimiento", layout="centered")

# Llamamos al menú antes de cualquier otra cosa
generar_menu()
# ... resto de tu código


st.write("# SentimentAPI")


# Aplicamos el estilo
st.markdown("""
    <style>
    input {
        background-color: white !important;
        color: #000000 !important;
    }
    /* Quitar el color gris cuando el input está enfocado */
    div[data-baseweb="text_area"]:focus-within {
        background-color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ESTILOS CSS PERSONALIZADOS ---
from funciones import *
estilo()

# --- CONTENIDO ---
# Usamos un div para envolver los widgets de Streamlit
st.write("Selecciona el Idioma")

seleccionar_idioma = st.segmented_control("Seleccione el Idioma para la reseña", ["Español", "Portugues", "Automático"])

#with st.expander("🪧 Idioma "):
#    st.checkbox("Español")
#    st.checkbox("Portugues")

#tipo = st.selectbox("Primero, selecciona el tipo:", ["Simple", "Batch"])

comentario = st.text_area("Ingresa el comentario:", 
                          placeholder="Ej: Este es el mejor PITCH...",
                          height=150)



if st.button("ENVIAR COMENTARIO"):
    st.success("Procesando...")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; color: white; margin-top: 30px; font-size: 0.8em;">
        Desarrollado por E47 | 
    </div>
    """, unsafe_allow_html=True)



