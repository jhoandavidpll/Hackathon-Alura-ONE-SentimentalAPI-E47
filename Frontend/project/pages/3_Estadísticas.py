import plotly.graph_objects as go
from menu import generar_menu
from funciones import estilo
import streamlit as st
import pandas as pd
import requests
import sys
import os

def init_session():
    if "data_stats" not in st.session_state:
        st.session_state.data_stats = {
            "clasificacion" : "Positivo",
            "idioma" : "ES"
        }
    if "data_frequency" not in st.session_state:
        st.session_state.data_frequency = {
            "idioma" : "ES"
        }
    if "top_palabras" not in st.session_state:
        st.session_state.top_palabras = pd.DataFrame()
    if "frequencias" not in st.session_state:
        st.session_state.frequencias = pd.DataFrame()

def obtener_top_palabras():
    try:
        response = requests.get(
            f"http://localhost:8080/predict/stats/words",
            json=st.session_state.data_stats,
            headers={"Content-Type":"application/json"}
        )

        data = response.json()

        if response.status_code == 200:
            # Crear y guardar DataFrame
            st.session_state.top_palabras = pd.DataFrame(data)
        else:
            st.error(f"Error: {response.status_code} - \"{data['error']}\"")
            st.session_state.top_palabras = pd.DataFrame()
    except Exception as e:
        st.error(f"Error de conexión: {str(e)}")
        st.session_state.top_palabras = pd.DataFrame()

def obtener_frequenias():
    try:
        response = requests.get(
            f"http://localhost:8080/predict/stats",
            json=st.session_state.data_frequency,
            headers={"Content-Type":"application/json"}
        )

        data = response.json()

        if response.status_code == 200:
            # Crear y guardar DataFrame
            st.session_state.frequencias = pd.DataFrame(data)
        else:
            st.error(f"Error: {response.status_code} - \"{data['error']}\"")
            st.session_state.frequencias = pd.DataFrame()
    except Exception as e:
        st.error(f"Error de conexión: {str(e)}")
        st.session_state.frequencias = pd.DataFrame()

def mostrar_formulario():
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns([1,2,2,2,2,1])
        with col2:
            seleccionar_sentimiento = st.segmented_control("Seleccione el Sentimiento", ["Positivo", "Negativo"], default="Positivo")
        with col3:
            seleccionar_idioma = st.segmented_control("Seleccione el Idioma", ["Español", "Portugués"], default="Español", key="idioma")
        with col4:
            selecciona_fecha_ini = st.date_input("Seleccione la Fecha de inicio", value=None)
        with col5:
            selecciona_fecha_fin = st.date_input("Seleccione la Fecha de fin", value=None)

        if selecciona_fecha_ini and selecciona_fecha_fin:
            if selecciona_fecha_ini > selecciona_fecha_fin:
                selecciona_fecha_ini, selecciona_fecha_fin = selecciona_fecha_fin, selecciona_fecha_ini
        if (selecciona_fecha_ini and selecciona_fecha_fin == None) or (selecciona_fecha_ini == None and selecciona_fecha_fin):
            selecciona_fecha_fin = None
            selecciona_fecha_ini = None

        st.session_state.data_stats = {
            "clasificacion" : seleccionar_sentimiento,
            "idioma" : "ES" if seleccionar_idioma == "Español" else "PT",
            "fecha_inicio" : str(selecciona_fecha_ini) if selecciona_fecha_ini else None,
            "fecha_fin" : str(selecciona_fecha_fin) if selecciona_fecha_fin else None
        }

        st.session_state.data_frequency = {
            "idioma" : "ES" if seleccionar_idioma == "Español" else "PT",
            "fecha_inicio" : str(selecciona_fecha_ini) if selecciona_fecha_ini else None,
            "fecha_fin" : str(selecciona_fecha_fin) if selecciona_fecha_fin else None
        }

def mostrar_graficos():
    with st.container():
        col1, col2, col3 = st.columns([0.5,9,0.5])
        with col2:
            # Obtenemos los datos a graficar
            obtener_top_palabras()
            obtener_frequenias()

            if st.session_state.top_palabras.empty or st.session_state.frequencias.empty:
                st.info("No hay información para mostrar")
            else:
                # Generamos los dataset
                df_top = st.session_state.top_palabras
                df_frequency = st.session_state.frequencias

                st.write("## Top 5 palabras más repetidas")
                col11, col12, col13 = st.columns([0.5,9,0.5])
                with col12:
                    fig = go.Figure(data=[
                        go.Bar(
                            x= df_top['palabra'],
                            y= df_top['frecuencia'],
                            text= df_top['frecuencia'],
                            textposition= 'auto'
                        )
                    ])
                    fig.update_layout(
                        title=f"Top 5 palabras {st.session_state.data_stats['clasificacion']}",
                        xaxis_title='Palabra',
                        yaxis_title='Frecuencia'
                    )
                    st.plotly_chart(fig)

                st.write("## Frequencia de sentimientos según el idioma")
                col11, col12, col13 = st.columns([0.5,9,0.5])
                with col12:
                    fig = go.Figure(data=[
                        go.Bar(
                            x= df_frequency['palabra'],
                            y= df_frequency['frecuencia'],
                            text= df_frequency['frecuencia'],
                            textposition= 'auto'
                        )
                    ])
                    fig.update_layout(
                        title=f"Frecuencia de sentimientos en el idioma {st.session_state.idioma}",
                        xaxis_title='Palabra',
                        yaxis_title='Frecuencia'
                    )
                    st.plotly_chart(fig)

def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    st.set_page_config(page_title="Estadísticas", layout="wide", page_icon=":bar_chart:")
    generar_menu()

    # --- ESTILOS CSS PERSONALIZADOS ---
    estilo()

    # Inicializa la sesion
    init_session()

    st.title("Estadísticas")

    mostrar_formulario()

    mostrar_graficos()

if __name__ == "__main__":
    main()