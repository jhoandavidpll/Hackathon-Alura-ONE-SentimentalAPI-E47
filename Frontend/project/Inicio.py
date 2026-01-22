
import streamlit as st
from menu import generar_menu # Importamos nuestra función
import requests
from funciones import *

# Inicializa la sesion mostrando el formulario
def init_session():
    if "mostrar_form" not in st.session_state:
        st.session_state.mostrar_form = True
    if "respuesta_api" not in st.session_state:
        st.session_state.respuesta_api = None
    if "data_formulario" not in st.session_state:
        st.session_state.data_formulario = {}
    if "mensaje_error" not in st.session_state:
        st.session_state.mensaje_error = None

def reset_formulario():
    st.session_state.mostrar_form = True
    st.session_state.respuesta_api = None
    st.session_state.mensaje_error = None
    st.session_state.data_formulario.clear()
    st.cache_data.clear()

def envio_peticion():
    try:
        # Limpieza del comentario
        if (st.session_state.data_formulario["modelo"] == "ES"):
            comentario_limpio = limpieza_es(st.session_state.data_formulario["comentario_original"])
        else:
            comentario_limpio = limpieza_pt(st.session_state.data_formulario["comentario_original"])

        st.session_state.data_formulario["comentario"] = comentario_limpio

        # Llamada a la api
        response = requests.post(
            "http://localhost:8080/predict",
            json=st.session_state.data_formulario,
            headers={"Content-Type":"application/json"}
        )

        # Guarda la respuesta 
        st.session_state.respuesta_api = {
            "status_code" : response.status_code,
            "data" : response.json() if response.status_code == 201 else None
        }

        # Cambia la vista al resultado en caso de que la prediccion se realice correctamente
        if response.status_code == 201:
            st.session_state.mostrar_form = False
        else:
            error = response.json()
            st.session_state.mensaje_error = f"Error: {response.status_code} - \"{error[0]['error']}\""
    except Exception as e:
        st.session_state.mensaje_error = f"Error: {str(e)}"

def mostrar_formulario(): 
    st.write("# SentimentAPI")
    # --- CONTENIDO ---
    seleccionar_idioma = st.segmented_control("Seleccione el Idioma de la reseña", ["Español", "Portugués"], default="Español")

    comentario = st.text_area("Ingresa el comentario:", 
                            placeholder="Ej: Este es el mejor PITCH...",
                            height=150)
    
    # Guarda los datos del formulario
    st.session_state.data_formulario = {
        "comentario_original": comentario,
        "comentario": None,
        "modelo" : "ES" if seleccionar_idioma == "Español" else "PT"
    }

    envio_comentario = st.button("ENVIAR COMENTARIO", on_click=envio_peticion)

    # Muestra el error en caso de existir
    if st.session_state.mensaje_error:
        st.error(st.session_state.mensaje_error)

def mostrar_resultado():
    st.title(":trophy: Resultados")

    # Muestra la respuesta de la peticion
    if st.session_state.respuesta_api:
        respuesta = st.session_state.respuesta_api
        # st.json(respuesta["data"])
        estilo_resulado()
        st.markdown(
            f"""
            <div class="card">
                <div class="resultado">
                    <div class="{"badge-positivo" if respuesta["data"]["prevision"] == "Positivo" else "badge-negativo"}">
                        {"😊" if respuesta["data"]["prevision"] == "Positivo" else "😫"}<br>Sentimiento<br>
                        {respuesta["data"]["prevision"]}
                    </div>
                    <div class="barra-container">
                        <div class="comentario">
                            “{st.session_state.data_formulario["comentario_original"]}”
                        </div>
                        <div class="label">Idioma: {"Español" if respuesta["data"]["idioma"] == "ES" else "Portugués"}</div>
                        <div class="label">Probabilidad: {respuesta["data"]["probabilidad"]*100:.0f}%</div>
                        <div class="barra">
                            <div class="{"barra-positiva" if respuesta["data"]["prevision"] == "Positivo" else "barra-negativa"}" style="width:{respuesta["data"]["probabilidad"]*100}%"></div>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Boton para regresar al formulario
    if st.button("Analizar otro comentario", use_container_width=True):
        reset_formulario()
        st.rerun()

def main():
    # Inicializa la sesion
    init_session()

    # --- CONFIGURACIÓN DE PÁGINA ---
    st.set_page_config(page_title="Analizador de Sentimiento", layout="centered", page_icon="🏅")

    # Llamamos al menú antes de cualquier otra cosa
    generar_menu()

    # --- ESTILOS CSS PERSONALIZADOS ---
    estilo()

    with st.container():
        # Mostramos el contenido segun el estado
        if st.session_state.mostrar_form:
            mostrar_formulario()
        else:
            mostrar_resultado()

    # --- FOOTER ---
    st.markdown("""
        <div style="text-align: center; color: white; margin-top: 30px; font-size: 0.8em;">
            Desarrollado por E47 
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
