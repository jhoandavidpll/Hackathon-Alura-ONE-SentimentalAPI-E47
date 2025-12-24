import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página (Debe ser lo primero)
st.set_page_config(page_title="Fundación Favorita - Sentiment Analysis", layout="wide")

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 5%;
        background-color: white;
        border-bottom: 1px solid #f0f0f0;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }
    .logo-img {
        height: 50px;
    }
    .nav-item {
        margin: 0 15px;
        text-decoration: none;
        color: #555;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN (Simulando el Header de la imagen) ---
def render_header():
    # Usamos columnas de Streamlit para replicar el layout
    col_logo, col_nav = st.columns([1, 3])
    
    with col_logo:
        # Aquí pondrías el path a tu imagen de logo
        st.image("https://via.placeholder.com/200x60?text=Fundacion+Favorita", width=200)

    with col_nav:
        # Botones de navegación horizontales
        selected = st.radio("", 
            ["Inicio", "Histórico", "Documentación", "Para Empresas", "Acerca de"], 
            horizontal=True, label_visibility="collapsed")
        return selected

# --- LÓGICA DE BASE DE DATOS (Simulada con un CSV para este ejemplo) ---
def get_history():
    try:
        return pd.read_csv("historial_sentimientos.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Fecha", "Comentario", "Sentimiento", "Probabilidad"])

def save_analysis(comentario, sentimiento, probabilidad):
    df = get_history()
    nueva_fila = {
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Comentario": comentario,
        "Sentimiento": sentimiento,
        "Probabilidad": f"{probabilidad:.2%}"
    }
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_csv("historial_sentimientos.csv", index=False)

# --- RENDERIZADO DE PÁGINAS ---
page = render_header()
st.divider()

if page == "Inicio":
    st.title("Análisis de Sentimientos")
    st.write("Introduce un texto para determinar si su connotación es Positiva, Negativa o Neutra.")