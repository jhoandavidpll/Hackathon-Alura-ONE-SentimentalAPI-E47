from menu import generar_menu
from datetime import datetime
from funciones import *
import streamlit as st
import pandas as pd
import requests
import json
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os

# Inicializa la sesion
def init_session():
    if "actual_page" not in st.session_state:
        st.session_state.actual_page = 0
    if "total_page" not in st.session_state:
        st.session_state.total_page = None
    if "primero" not in st.session_state:
        st.session_state.primero = True
    if "ultimo" not in st.session_state:
        st.session_state.ultimo = False
    if "tabla" not in st.session_state:
        st.session_state.tabla = pd.DataFrame()
    if "actualizado" not in st.session_state:
        st.session_state.actualizado = True

def obtener_datos():
    try:
        response = requests.get(
            f"http://localhost:8080/predict?page={st.session_state.actual_page}"
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Actualiza la sesion
            st.session_state.total_page = int(data['totalPages'])
            st.session_state.primero = data['first']
            st.session_state.ultimo = data['last']
            
            # Crear y guardar DataFrame
            if data['content']:
                df = pd.DataFrame(data['content'])
                
                # Añadir transformaciones si es necesario
                if 'probabilidad' in df.columns:
                    df['probabilidad_%'] = [str(i)+"%" for i in (df['probabilidad'] * 100).round(2)]
                if 'fecha' in df.columns:
                    df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime("%d/%m/%Y")

                new_df = df.drop('probabilidad', axis=1)
                st.session_state.tabla = new_df[["id", "comentario", "prevision", "probabilidad_%", "idioma", "fecha"]]
            else:
                st.session_state.tabla = pd.DataFrame()
                
        else:
            st.error(f"Error al obtener datos: {response.status_code}")
            st.session_state.tabla = pd.DataFrame()
            
    except Exception as e:
        st.error(f"Error de conexión: {str(e)}")
        st.session_state.tabla = pd.DataFrame()

def manejo_page():
    seleccion = st.session_state.control_pag
    primera = st.session_state.primero
    ultima = st.session_state.ultimo
    total = st.session_state.total_page - 1

    pagina_anterior = st.session_state.actual_page

    # Manejo de paginas
    if seleccion == "<" and not(primera):
        st.session_state.actual_page -= 1
    elif seleccion == "\>" and not(ultima):
        st.session_state.actual_page += 1
    elif seleccion == "<<":
        st.session_state.actual_page = 0
    elif seleccion == "\>>":
        st.session_state.actual_page = total
    
    if pagina_anterior != st.session_state.actual_page:
        obtener_datos()
        st.session_state.actualizado = True
    else:
        st.session_state.actualizado = False

def mostar_historial():
    # Muesta la tabla
    df = st.session_state.tabla
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay datos disponibles")

    st.markdown(
        """
        <style>
            .stButtonGroup {
                display: flex; 
                justify-content: center; 
                align-items: center;
            }
        </style>
        """, unsafe_allow_html=True
    )
    # Paginacion en pantalla
    st.segmented_control(label=" ", options=["<<", "<", str(st.session_state.actual_page+1), "\>", "\>>"], key="control_pag", on_change=manejo_page)
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            Página {st.session_state.actual_page+1} de {st.session_state.total_page}
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    init_session()

    st.set_page_config(page_title="Histórico", layout="wide")

    generar_menu()

    # --- ESTILOS CSS PERSONALIZADOS ---
    estilo()

    st.title("Datos Históricos")
    with st.container():
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:

            st.write("# Histórico")

            if st.session_state.tabla.empty:
                obtener_datos()

            if st.session_state.actualizado:
                mostar_historial()

if __name__ == "__main__":
    main()