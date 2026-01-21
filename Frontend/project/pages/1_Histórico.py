import streamlit as st
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menu import generar_menu
from funciones import *

st.set_page_config(page_title="Histórico", layout="wide")

generar_menu()

# --- ESTILOS CSS PERSONALIZADOS ---
estilo()

st.title("Datos Históricos")
# ... resto de tu código

st.write("# Histórico")

# importar datos
import pandas as pd
import numpy as np

data = pd.read_csv("/home/jhoan/Documentos/portfolio/Hackathon-Alura-ONE-SentimentalAPI-E47/Data-Science/data/spanish/train.csv")

st.write(data)