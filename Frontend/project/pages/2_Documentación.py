import streamlit as st
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menu import generar_menu
from funciones import estilo

st.set_page_config(page_title="Documentación", layout="wide")

generar_menu()

# --- ESTILOS CSS PERSONALIZADOS ---
estilo()

st.title("Documentación")
# ... resto de tu código

st.write("## Este un título H2")

# importar datos
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)