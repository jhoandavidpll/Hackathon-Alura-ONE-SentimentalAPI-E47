import streamlit as st
import pandas as pd
from datetime import datetime
from textblob import TextBlob
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Startup - Análisis de Sentimientos",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INICIALIZAR ESTADO (Base de datos temporal en memoria) ---
# Esto sustituye temporalmente a la DB. Los datos se pierden al refrescar la página.
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- COLORES Y ESTILOS (CSS) ---
COLOR_PRIMARY = "#D12E2E" 
COLOR_BG = "#F0F2F6"
COLOR_TEXT = "#333333"

st.markdown(f"""
    <style>
    .stApp {{ background-color: {COLOR_BG}; }}
    
    /* Contenedor Flotante de Navegación */
    .nav-container {{
        background-color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        justify_content: space-between;
    }}
    
    /* Menú (Radio Buttons modificados) */
    div.row-widget.stRadio > div {{
        flex-direction: row;
        align-items: center;
        background-color: white;
        border: none;
    }}
    div.row-widget.stRadio > div[role='radiogroup'] > label {{
        background-color: white;
        border: none;
        color: {COLOR_TEXT};
        margin-right: 15px;
        padding: 5px 10px;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s;
    }}
    div.row-widget.stRadio > div[role='radiogroup'] > label:hover {{
        color: {COLOR_PRIMARY};
    }}
    div.row-widget.stRadio div[role='radiogroup'] > label > div:first-child {{
        display: none;
    }}

    /* Botones */
    div.stButton > button {{
        background-color: {COLOR_PRIMARY};
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        width: 100%;
        transition: background-color 0.3s;
    }}
    div.stButton > button:hover {{
        background-color: #B01E1E;
        color: white;
        border: none;
    }}

    /* Estilos Generales */
    .logo-text {{
        font-family: sans-serif;
        font-weight: bold;
        font-size: 24px;
        color: {COLOR_PRIMARY};
        display: flex;
        align-items: center;
    }}
    .result-card {{
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-top: 20px;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONES ---

def analyze_sentiment(text):
    """Simulación de análisis de sentimientos"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.05:
        label = "Positivo"
        prob = 0.5 + (polarity / 2)
    elif polarity < -0.05:
        label = "Negativo"
        prob = 0.5 + (abs(polarity) / 2)
    else:
        label = "Neutro"
        prob = 1.0 - abs(polarity)
        
    return label, round(prob * 100, 2)

def save_to_temp_memory(texto, sentimiento, probabilidad):
    """Guarda en session_state (Aquí conectarás PostgreSQL después)"""
    nuevo_registro = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "texto": texto,
        "sentimiento": sentimiento,
        "probabilidad": probabilidad
    }
    # Insertamos al principio de la lista para ver el más reciente primero
    st.session_state['history'].insert(0, nuevo_registro)

# --- UI: BARRA DE NAVEGACIÓN ---
with st.container():
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    col_logo, col_menu = st.columns([1, 3])
    
    with col_logo:
        st.markdown(f'''
            <div class="logo-text">
                <span style="color:{COLOR_PRIMARY}; font-size: 1.5rem;">Startup</span>
                <span style="color:#E85D64; margin-left:5px; font-size: 1.5rem;">sentimientosAPI</span>
            </div>
        ''', unsafe_allow_html=True)
    
    with col_menu:
        menu_options = ["Inicio", "Histórico", "Documentación", "Para empresas", "Acerca de"]
        selection = st.radio("Nav", menu_options, horizontal=True, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# --- UI: PÁGINAS ---

if selection == "Inicio":
    st.markdown(f"<h2 style='text-align: center; color: {COLOR_TEXT};'>Análisis de Sentimientos</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Introduce un comentario abajo para detectar si es positivo, negativo o neutro.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user_input = st.text_area("Comentario", placeholder="Escribe aquí tu experiencia con la Startup...", height=150)
        
        analyze_btn = st.button("Analizar Texto")
        
        if analyze_btn and user_input:
            with st.spinner("Procesando..."):
                time.sleep(0.5)
                label, prob = analyze_sentiment(user_input)
                
                # GUARDAR RESULTADO (En memoria por ahora)
                save_to_temp_memory(user_input, label, prob)
            
            # Mostrar tarjeta de resultados
            st.markdown(f"""
                <div class="result-card">
                    <h3 style="color: {'green' if label == 'Positivo' else 'red' if label == 'Negativo' else 'gray'};">{label}</h3>
                    <div style="font-size: 40px; font-weight: bold; color: {COLOR_TEXT};">{prob}%</div>
                    <p style="color: gray;">Probabilidad de certeza</p>
                </div>
            """, unsafe_allow_html=True)
            st.success("¡Análisis realizado correctamente!")

        elif analyze_btn and not user_input:
            st.warning("El campo de texto está vacío.")

elif selection == "Histórico":
    st.markdown(f"<h2 style='color: {COLOR_TEXT};'>Historial de Análisis (Sesión Actual)</h2>", unsafe_allow_html=True)
    
    # Recuperamos los datos de la memoria temporal
    data = st.session_state['history']
    
    if len(data) > 0:
        df = pd.DataFrame(data)
        
        # Métricas
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Registros", len(df))
        m2.metric("Positivos", len(df[df['sentimiento']=='Positivo']))
        m3.metric("Negativos", len(df[df['sentimiento']=='Negativo']))
        
        # Tabla interactiva
        st.dataframe(
            df,
            column_config={
                "probabilidad": st.column_config.ProgressColumn(
                    "Certeza (%)",
                    format="%.2f%%",
                    min_value=0,
                    max_value=100,
                ),
                "sentimiento": st.column_config.TextColumn("Clasificación"),
            },
            use_container_width=True,
            hide_index=True
        )
        st.caption("Nota: Estos datos son temporales. Se perderán al reiniciar la aplicación hasta que se conecte PostgreSQL.")
    else:
        st.info("No hay datos en esta sesión. Realiza un análisis en 'Inicio' para ver resultados aquí.")

elif selection == "Documentación":
    st.header("Documentación Técnica")
    st.write("Estructura futura para conexión PostgreSQL:")
    st.code("""
    import psycopg2

    # TODO: Implementar conexión
    def connect_postgres():
        conn = psycopg2.connect(
            host="localhost",
            database="sentimientosAPI_db",
            user="user",
            password="password"
        )
        return conn
    """, language="python")

elif selection == "Para empresas":
    st.header("Soluciones Corporativas")
    st.write("Contáctanos para integraciones API a gran escala.")

elif selection == "Acerca de":
    st.header("Sobre el Proyecto")
    st.write("Plataforma de análisis de sentimientos desarrollada para Startup.")