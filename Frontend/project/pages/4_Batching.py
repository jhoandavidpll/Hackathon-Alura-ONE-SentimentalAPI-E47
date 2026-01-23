from menu import generar_menu 
from funciones import *
import streamlit as st
import pandas as pd
import requests
import sys
import os
import io

# Inicializa la sesion mostrando el formulario
def init_session():
    if "file" not in st.session_state:
        st.session_state.file = {}
    if "datos" not in st.session_state:
        st.session_state.datos = {}
    if "mostrar_form" not in st.session_state:
        st.session_state.mostrar_form = True
    if "respuesta" not in st.session_state:
        st.session_state.respuesta = pd.DataFrame()
    if "mensaje_error" not in st.session_state:
        st.session_state.mensaje_error = None
    if "limpieza_realizada" not in st.session_state:
        st.session_state.limpieza_realizada = False

def reset_formulario():
    st.session_state.file.clear()
    st.session_state.datos.clear()
    st.session_state.mostrar_form = True
    st.session_state.respuesta = pd.DataFrame()
    st.session_state.mensaje_error = None
    st.session_state.limpieza_realizada = False
    st.cache_data.clear()

def generar_ejemplo():
    ejemplo = {
        "comentarios" : [
            "Este es el mejor analizador de sentimientos!!! 🎉",
            "Gracias a AluraLatam, Oracle, a los patrocinadores y a todo el equipo de organización por esta oportunidad 😍❤️ ",
            "La primavera es la estación que más me desespera, esta alergia no me deja respirar."
        ]
    }

    df = pd.DataFrame(ejemplo)

    return df.to_csv(index=False)

def envio_archivo():
    try:
        if st.session_state.file["archivo"]:
            response = requests.post(
                "http://localhost:8080/predict/csv",
                files=st.session_state.file,
                data=st.session_state.datos
            )

            st.session_state.respuesta  = pd.DataFrame(response.json())

            if response.status_code == 200:
                st.session_state.mostrar_form = False

                if not st.session_state.respuesta.empty:
                    df = st.session_state.respuesta
                    # Añadir transformaciones si es necesario
                    if 'probabilidad' in df.columns:
                        df['probabilidad_%'] = [str(i)+"%" for i in (df['probabilidad'] * 100).round(2)]
                    if 'fecha' in df.columns:
                        df['fecha'] = pd.to_datetime(df['fecha']).dt.strftime("%d/%m/%Y")

                    new_df = df.drop('probabilidad', axis=1)
                    st.session_state.respuesta = new_df[["id", "comentario", "prevision", "probabilidad_%", "idioma", "fecha"]]
            else:
                st.session_state.mensaje_error = f"Error: {response.status_code} - \"{response.json()[0]['error']}\""
    except Exception as e:
        st.session_state.mensaje_error = f"Error: {str(e)}"

def formulario():
    st.title("Batchig")
    st.markdown("""
        Puede realizar un análisis de sentimientos de forma masiva a través de un archivo csv, 
        descargue el archivo ejemplo para rellenarlo, evite el uso de comillas dobles (“ ”). 
        Una vez que rellene el archivo, asegúrese que tenga el formato “.csv” y súbalo para analizarlo y 
        seleccione el idioma en el que están escritos los comentarios. 
        No combine mensajes en diferentes idiomas para el correcto funcionamiento del analizador.
    """)

    # Archivo ejemplo
    st.download_button(
        label=":inbox_tray: Archivo ejemplo",
        data=generar_ejemplo(),
        file_name="ejemplo.csv",
        mime="text/csv"
    )

    # Input del idioma del modelo
    st.segmented_control("Seleccione el Idioma de la reseña", ["Español", "Portugués"], default="Español", key="idioma")

    # Input del archivo
    file = st.file_uploader(
        "Arrastra tu archivo aquí o haz clic para subirlo",
        accept_multiple_files=False,
        type=["csv"]
    )

    if file is not None:
        idioma = "ES" if st.session_state.idioma == "Español" else "PT"
        archivo_new = limpieza_df(file, idioma)
        csv = archivo_new.to_csv(index=False)
        # st.session_state.file = {"archivo" : (file.name, file.getvalue(), file.type)}
        st.session_state.file = {"archivo" : ("file.csv", csv, "application/vnd.ms-excel")}
        st.session_state.datos = {"modelo" : idioma}     

    st.button("ENVIAR COMENTARIO", on_click=envio_archivo)

    # Muestra el error en caso de existir
    if st.session_state.mensaje_error:
        st.error(st.session_state.mensaje_error)

def mostrar_resultado():
    st.title(":trophy: Resultados")

    st.balloons()

    # Muestra las respuestas
    df = st.session_state.respuesta
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No hay datos disponibles")

    # Boton para regresar al formulario
    if st.button("Analizar otro archivo", use_container_width=True):
        reset_formulario()
        st.rerun()

def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    # Inicio sesion 
    init_session()

    # Configuracion de la pagina
    st.set_page_config(page_title="Batching", layout="centered", page_icon=":brain:")
    # Estilos personalizados
    estilo()
    generar_menu()

    # Muestra el formulario
    with st.container():
        # Mostramos el contenido segun el estado
        if st.session_state.mostrar_form:
            formulario()
        else:
            mostrar_resultado()

if __name__ == "__main__":
    main()