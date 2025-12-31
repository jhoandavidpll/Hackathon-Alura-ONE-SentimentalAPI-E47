import streamlit as st
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menu import generar_menu

st.set_page_config(page_title="Acerca", layout="wide")

generar_menu()

st.title("Sobre el Proyecto")
st.header("\"Detectamos problemas y promovemos oportunidades de mejora\"")

    #Seccion: Presentacion del Proyecto
st.markdown("""
    SentimentAPI es una aplicación de análisis de sentimientos que convierte comentarios de texto en insights claros y accionables, de forma rápida, sencilla y accesible.
    Permite:
    - Identificar sentimientos positivos, negativos y neutrales
    - Detectar debilidades recurrentes en productos o servicios
    - Resaltar feedback relevante para la toma de decisiones
    - Priorizar acciones basadas en datos reales
    """)#Posicionar y colocar imagen referente al proyecto

    #Seccion: Funcionamiento
st.subheader("Como funciona")
st.markdown("""
        1. El usuario envía comentarios (reviews, mensajes, encuestas)
        2. La API procesa el texto usando modelos de NLP
        3. Se devuelve:
            - Sentimiento general
            - Probabilidad
            - Métricas agregadas
            - Tendencias clave
        4. Los resultados se integran fácilmente en dashboards o flujos existentes
    """)

st.video("https://www.youtube.com/watch?v=VIDEO_ID")#Por indicar el video y cambiar posicion

    #Seccion: Publico objetivo
st.subheader("Dirigido a")
st.markdown("""
        - Dueños de pequeños negocios.
        - Community Managers.
        - Agentes y supervisores de centros de contacto.
        - Gerentes de Experiencia del Cliente y Marketing en empresas medianas.
    """)

    #Seccion: Vision
st.subheader("Vision")
st.markdown("""
        Transformar grandes volúmenes de texto en claridad, ayudando a los equipos a escuchar mejor a sus usuarios y tomar 
        decisiones basadas en datos.
    """)

    #Seccion: Cronograma de Desarrollo
st.subheader("Roadmap")
st.markdown("""
        
    """)

    #Seccion: Presentacion del Equipo
st.subheader("Equipo")
st.markdown("""
        - Jhoan David Pillapa Llerena (Data Engineer)
        - Mitchel David Poblete Santibañez (Backend Developer)
        - Andres Felipe Cubillos Hurtado (Data Scientist)
        - Brandon Omar Ortiz Gutierrez (Backend Developer)
        - David Avila (Data Scientist)
        - Nydia Olmos (Backend Developer)
        - Andrés Huerta Salgado (Data Scientist)
        - Cristian Armando Larios Bravo (Backend Developer)
    """)#Por agregar (linkedin, github, correos, fotos)

st.html("""
<div style="display: flex; align-items: center; background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #31333f; font-family: sans-serif;">
  <img src="https://avatars.githubusercontent.com/u/66537133?s=400&u=82d981fa4f723616d5809b2fc3f84999b8d29fbe&v=4" 
       alt="Jhoan David Pillapa Llerena" 
       style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; margin-right: 20px; border: 2px solid #31333f;">
  
  <div>
    <h3 style="margin: 0; color: white;">Jhoan David Pillapa Llerena</h3>
    <h4 style="margin: 5px 0; color: #ff4b4b;">Data Engineer</h4>
    <p style="margin: 0 0 10px 0; color: #fafafa; font-size: 0.9rem;">
      Experto en transformar grandes volúmenes de datos en insights accionables para acelerar el crecimiento del negocio. Especialista en automatización de reportes (Power BI/Python).
    </p>
    
    <!-- Contenedor de Redes Sociales -->
    <div style="display: flex; gap: 12px; align-items: center;">
      <!-- LinkedIn -->
      <a href="https://www.linkedin.com/in/jhoandavidpll/" target="_blank" style="text-decoration: none;">
        <img alt="Jhoan Pillapa | Linkedin" width="28px" src="https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/linkedin-svgrepo-com.svg" style="display: block;">
      </a>
      <a href="https://github.com/jhoandavidpll" target="_blank" style="text-decoration: none;">
        <img alt="Jhoan Pillapa | Github" width="28px" src="https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/github-color-svgrepo-com.svg" style="display: block;">
      </a>
    </div>
  </div>
</div>
""")

    #Herramientas
st.subheader("Stack Tecnologico")
st.markdown("""
    <style>
    .tech-grid {
        display:grid;
        grid-template-columns: repeat(5, 1fr);
        gap:30px;
        text-align:center;
    }
    .tech-grid img {
        width:64px;
    }
    .tech-grid p {
        margin-top:8px;
        font-weight:600;
    }
    </style>
    <div class="tech-grid">
        <div>
            <a href="https://www.java.com/es/">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg">
                <p>Java 21</p>
            </a>
        </div>
        <div>
            <a href="https://www.python.org">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
                <p>Python 3.13</p>
            </a>
        </div>
        <div>
            <a href="https://www.docker.com">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg">
                <p>Docker</p>
            </a>
        </div>
        <div>
            <a href="https://www.canva.com">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/canva/canva-original.svg">
                <p>Canva</p>
            </a>
        </div>
        <div>
            <a href="https://www.oracle.com/cloud/">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/oracle/oracle-original.svg">
                <p>Oracle Cloud</p>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    #Anexos
st.subheader("Enlaces")
st.markdown("""
        - [Video Demo](https://www.youtube.com)
        - [Canva](https://www.canva.com/design/DAG8qnGYp1c/-nmKgA5yGP5BC8sAsg2SAA/edit)
        - [Github](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/tree/DS)
        - [Readme](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/DS/README.md)
    """)
    