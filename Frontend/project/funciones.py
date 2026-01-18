import streamlit as st

# --- ESTILOS CSS PERSONALIZADOS ---
def estilo():
    return st.markdown("""
        <style>
        /* Cambiar el fondo de la aplicación */
        .stApp {
            background: linear-gradient(135deg, #018790 0%, #018790 100%);
        }

        /* Contenedor principal tipo 'Isla' */
        .main-card {
            background-color: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            margin-top: 20px;
        }

        /* Personalización del botón */
        div.stButton > button {
            width: 100%;
            background-color: #9EC6F3;
            color: white;
            border-radius: 10px;
            border: none;
            height: 3em;
            font-weight: bold;
        }
        
        /* Títulos dentro de la isla */
        .card-title {
            color: #4a4a4a;
            font-family: 'sans-serif';
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)