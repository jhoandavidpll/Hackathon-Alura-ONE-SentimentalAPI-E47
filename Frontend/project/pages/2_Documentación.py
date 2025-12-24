import streamlit as st
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menu import generar_menu

st.set_page_config(page_title="Documentación", layout="wide")

generar_menu()

st.title("Documentación")
# ... resto de tu código