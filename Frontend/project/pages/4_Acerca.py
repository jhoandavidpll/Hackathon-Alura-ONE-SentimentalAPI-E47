import streamlit as st
# Nota: Como 'pages' es una subcarpeta, necesitamos importar desde la raíz.
# A veces Python en Streamlit encuentra la raíz directamente:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from menu import generar_menu
from funciones import *

st.set_page_config(page_title="Acerca", layout="wide", page_icon=":busts_in_silhouette:")

generar_menu()
# --- ESTILOS CSS PERSONALIZADOS ---
estilo()

#Generando contenedores
titulo = st.container()
descripcion = st.container()
funcionamiento = st.container()
clientes = st.container()
vision = st.container()
mapa = st.container()
equipo = st.container()
herramientas = st.container()
enlaces = st.container()


### Contenido principal de la aplicación
# Contenido para el titulo
titulo.title("Sobre el Proyecto")
titulo.header("\"Detectamos problemas y promovemos oportunidades de mejora\"")
titulo.write("---")

#Seccion: Presentacion del Proyecto
descripcion.write("""
    <style>
        .description-box{
            display: flex;
            flex-direction: row;
            align-items: center;
            padding: 0 5%;
        }
        .description-text{
            flex: 1;
            font-size: 1.125rem;
            line-height: 1.6;   
        }
        .description-features{
            flex: 1;
            padding: 0 5%;
        }
        .description-image{
            flex: 1;
        }
        .description-box div ul{
            gap: 10px;
        }
        .description-box div ul li{
            box-sizing: border-box;
            list-style-type: none;
            padding: 15px;
            margin: 15px;
            border-radius: 8px;
            border: 1px solid #000000;
            min-height: 80px;
            width: 100%;
            display: flex; /* Para centrar el texto si es muy corto */
            align-items: center; /* Centra verticalmente */
            justify-content: center; /* Centra horizontalmente (opcional) */
            text-align: center;
        }
    </style>
    <div class='description-box'>
        <div class='description-text'>
            <p>SentimentAPI es una aplicación de análisis de sentimientos que convierte comentarios de texto en insights claros y accionables, de forma rápida, sencilla y accesible.</p>
        </div>
        <div class='description-features'>
            <ul>
                <li>Identifica sentimientos positivos, negativos y neutrales</li>
                <li>Detecta debilidades recurrentes en productos o servicios</li>
            </ul>
        </div>
        <div class='description-image'>
            <ul>
                <li>Resalta feedback relevante para la toma de decisiones</li>
                <li>Prioriza acciones basadas en datos reales</li>
            </ul>
        </div>
    </div>
""",unsafe_allow_html=True)

descripcion.write("---")

    #Seccion: Funcionamiento
funcionamiento.write("""
    <style>
        .funcionamiento-box{
            display: flex;
        }
        .funcionamiento-video{
            flex: 1;
        }
        .funcionamiento-pasos{
            flex: 1;
        }
        .funcionamiento-pasos ol li p{
            margin: 0;
        }
    </style>
    <div class='funcionamiento-box'>
        <div class='funcionamiento-video'>
            <iframe width="560" height="315" 
                src="www.youtube.com" 
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        </div>
        <div class='funcionamiento-pasos'>
            <h1>Como funciona</h1>
            <ol>
                <li>El usuario envía comentarios (reviews, mensajes, encuestas)</li>
                <li>La API procesa el texto usando modelos de NLP</li>
                <li>
                    <p>Se devuelve:</p>
                    <ul>
                        <li>Sentimiento general</li>
                        <li>Probabilidad</li>
                        <li>Métricas agregadas</li>
                        <li>Tendencias clave</li>
                    </ul>
                </li>
                <li>Los resultados se integran fácilmente en dashboards o flujos existentes</li>
            </ol>
        </div>
    </div>
""",unsafe_allow_html=True)

funcionamiento.write("---")

    #Seccion: Publico objetivo
clientes.write("""
    <style>
        .clientes-numerados ul{
            gap: 10px;
            display: flex;
            flex-direction: row;
        }
        .clientes-etiqueta{
            box-sizing: border-box;
            padding: 0;
            margin: 0;
            list-style-type: none;
            border-radius: 8px;
            border: 1px solid #000000;
            min-height: 14rem;
            width: 100%;
            display: flex;
            gap: 1em;
            flex-direction: column;
            text-align: center;
            justify-content: space-between;
        }
        .clientes-etiqueta h3{
            flex: 3;
            align-content: center;
            padding: 0.5rem;
            min-height: 7rem;
        }
        .clientes-etiqueta p{
            flex: 1.5;
            padding: 0.5rem;
            align-content: center;
        }
    </style>
    <div class = 'clientes-box'>
        <div class = 'clientes-titulo'>
            <h1>Dirigido a</h1>
        </div>
        <div class = 'clientes-numerados'>
            <ul>
                <li class='clientes-etiqueta'>
                    <h3>Dueños de pequeños negocios</h3>
                    <p>Vision resumida y rapida de las reseñas en Google y TripAdvisor</p>
                </li>
                <li class='clientes-etiqueta'>
                    <h3>Community Managers</h3>
                    <p>Facilitar monitorizacion cientos de menciones diarias.</p>
                </li>
                <li class='clientes-etiqueta'>
                    <h3>Agentes y supervisores de centros de contacto</h3>
                    <p>Herramientas prácticas que reducen la carga cognitiva y el estrés.</p>
                </li>
                <li class='clientes-etiqueta'>
                    <h3>Gerentes de Experiencia del Cliente y Marketing</h3>
                    <p>Brindar métricas claras para reportar a dirección.</p>
                </li>
            </ul>
        </div>
    </div>
""",unsafe_allow_html=True)
clientes.write("---")

    #Seccion: Vision

vision.write("""
    <style>
        .vision-box p{
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 1.25rem;

        }
    </style>
    <div class = 'vision-box'>
        <h1>Vision</h1>
        <p>Transformar grandes volúmenes de texto en claridad, ayudando a los equipos a escuchar mejor a sus usuarios y tomar 
        decisiones basadas en datos</p>
    </div>
""",unsafe_allow_html=True)

vision.write("---")

    #Seccion: Cronograma de Desarrollo
mapa.write("""
    <style>

    </style>
    <h1>Roadmap</h1>

""",unsafe_allow_html=True)

mapa.write("---")

    #Seccion: Presentacion del Equipo

personas = [
    {
        'nombre': 'David Abraham Avila Castro',
        'rol': 'Data Science',
        'linkedin': 'http://www.linkedin.com/in/david-abraham-avila-castro-a6631a158',
        'github': 'https://github.com/ADavid096',
        'foto': 'https://avatars.githubusercontent.com/u/163216805?s=400&u=bbb03385cf493f4f4f70dea2ac602b3c03d06be6&v=4',
        'descripcion': 'Dedicado al analisis de datos y con interes en la ciencia de datos debido a las posibilidades que brinda'
    },
    {
        'nombre': 'Mitchel David Poblete Satibáñez',
        'rol': 'Data Science',
        'linkedin': 'https://www.linkedin.com/in/mitchel-poblete/',
        'github': 'https://github.com/MiitchPs',
        'foto': 'https://avatars.githubusercontent.com/u/105990185?v=4',
        'descripcion': 'Analista Pogramador - Cert.DataScience - Cert.Oracle Cloud Infrastructure OCI '
    },
    {
        'nombre': 'Jhoan David Pillapa Llerena',
        'rol': 'Data Engineer',
        'linkedin': 'https://www.linkedin.com/in/jhoandavidpll/',
        'github': 'https://github.com/jhoandavidpll',
        'foto': 'https://avatars.githubusercontent.com/u/66537133?s=400&u=82d981fa4f723616d5809b2fc3f84999b8d29fbe&v=4',
        'descripcion': 'Ingeniero en Electrónica, Telecomunicaciones y Redes. Data Science, experto en transformar grandes volúmenes de datos en insights.'
    },
        {
        'nombre': 'Andres Felipe Cubillos Hurtado',
        'rol': 'Data Science',
        'linkedin': 'https://www.linkedin.com/in/andres-felipe-cubillos-hurtado-5a03a4189/',
        'github': 'https://github.com/andrewcubillos',
        'foto': 'https://avatars.githubusercontent.com/u/32993313?s=400&u=71f20d47c8bdce83b4cb965eb9f7d3d4b540c231&v=4',
        'descripcion': 'Ingeniero de Sistema. Análisis de datos con enfoqe en monitoreo y ciencia de datos.'
    },
        {
        'nombre': 'Andrés Huerta Salgado',
        'rol': 'Data Science',
        'linkedin': 'https://www.linkedin.com/in/andres-huerta-salgado-129474338/',
        'github': 'https://github.com/AHS30',
        'foto': 'https://avatars.githubusercontent.com/u/108943856?v=4',
        'descripcion': 'Estudiante de Sistemas Computacionales'
    },
        {
        'nombre': 'Jeferson José Peña Curvelo',
        'rol': 'Data Science',
        'linkedin': 'https://www.linkedin.com/in/jefersonjpc/',
        'github': 'https://github.com/JeffPeC',
        'foto': 'https://avatars.githubusercontent.com/u/201787396?s=400&u=ea59ecbe2fbb6456ff86fb04719bfdcd5f1636a4&v=4',
        'descripcion': 'Analista de Sistemas, Informático, actualmente enfocado en expandir mis conocimientos en Data Science.'
    },
        {
        'nombre': 'Nydia Naomi Olmos Romero',
        'rol': 'Backend',
        'linkedin': 'http://www.linkedin.com/in/nydia-olmos',
        'github': 'https://github.com/NydiaOlmos',
        'foto': 'https://avatars.githubusercontent.com/u/111654273?v=4',
        'descripcion': 'Ingeniera en Computación Inteligente, especializada en la ciencia de datos y aprendizaje de máquina, con alto interés en el computo en la nube y back end'
    },
        {
        'nombre': 'Brandon Omar Ortiz Gutierrez ',
        'rol': 'Backend',
        'linkedin': 'https://www.linkedin.com/in/brandon-ortiz-back',
        'github': 'https://github.com/brandon-informatico',
        'foto': 'https://avatars.githubusercontent.com/u/193290626?v=4',
        'descripcion': 'Ingeniero en Informática enfocado en back-end, BD relacionales, manejo de soluciones en la nube, con gran interes en la ingeniería de datos.'
    },
            {
        'nombre': 'Christian',
        'rol': 'Backend',
        'linkedin': 'http://www.linkedin.com/in/cristian-larios',
        'github': 'https://github.com/Fas5ter',
        'foto': 'https://avatars.githubusercontent.com/u/96441511?v=4',
        'descripcion': 'Ingeniero en Computación Inteligente, Arquitecto de Soluciones en la Nube, Científico de Datos y Desarrollador de Software Full Stack'
    }
]

#CSS para el equipo
equipo.write("""
    <style>
        [data-testid="stHeaderActionElements"] {
            display: none;
        }
        .equipos-box{
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .equipos-item{
            padding: 0;
            margin: 0;
            list-style-type: none;
            border-radius: 8px;
            border: 1px solid #000000;
            min-height: 24rem;
            width: 22%;
            display: flex;
            flex-direction: column;
            text-align: center;
        }
        .equipos-item h2, h3{
            margin:0;
            padding:0;
        }
        .equipos-detalle{
            display: flex;
            margin: 0;
            padding: 0;
            flex-direction: column;
            align-items: center;
            font-family: sans-serif;
        }
        .equipo-foto{
            width: 7rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: sans-serif;
            height: 8rem;

        }
        .equipo-foto img{
            border-radius: 64px;
        }
        .nombres {
            height: 2rem;
            align-content: center;
        }
        .equipos-detalle h2{
            font-size: 1.1rem;
        }
        .roles{
            height: 2rem;
            align-content: center;
        }
        .roles div h3{
            height: 2rem;
            padding: 0;
            align-content: center;
        }

        .equipos-detalle h3{
            color: #ff4b4b;
            font-size: 1rem;
        }
        .palabras{
           height: 8.5rem;
           padding: 0 1rem;
           text-align: justify;
        }
        .equipos-detalle p{
            font-size: 0.85rem;
        }
        .equipo-enlaces{
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-direction: row;
            width: 50%;
            height: 3rem;
           
        }
        .equipo-logos{
            width: 40px;
        }
        .equipo-logos img{
            width:100%;
            display: flex;
            align-items: center;
            gap: 15px;
        }
    </style>
""",unsafe_allow_html=True)

#Funcion para imprimir tarjetas
def tarjetas2(diccionario):
    inicio = f"""   <h1>Equipo</h1>
    <div>
        <ul class='equipos-box'>"""
    fin = f"""
        </ul>
    </div>"""
    tarjetas= ""
    for a in diccionario:
        tarjeta = f"""
            <li class='equipos-item'>
                <div class='equipos-detalle'>
                    <div class = 'equipo-foto'>
                        <img src={a['foto']}>
                    </div>
                    <div class = 'nombres'>
                        <h2>{a['nombre']}</h2>
                    </div>
                    <div class = 'roles'>
                        <h3>{a['rol']}</h3>
                    </div>
                    <div class= 'palabras'>
                        <p>{a['descripcion']}</p>
                    </div>
                    <div class='equipo-enlaces'>
                        <div class = 'equipo-logos'>
                            <a href={a['linkedin']}>
                                <img src='https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/linkedin-svgrepo-com.svg'>
                            </a>
                        </div>
                        <div class = 'equipo-logos'>
                            <a href={a['github']}>
                                <img src='https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/github-color-svgrepo-com.svg'>
                            </a>
                        </div>
                    </div>
                </div>
            </li>"""
        tarjetas = tarjetas + tarjeta
    tarjetas = inicio + tarjetas + fin
    return tarjetas

equipo.write(tarjetas2(personas),unsafe_allow_html=True)
equipo.write("---")

#Funcion para extraer la informacion del drive del equipo




#st.html("""
#<div style="display: flex; align-items: center; background-color: #0e1117; padding: 20px; border-radius: 10px; border: 1px solid #31333f; font-family: sans-serif;">
#  <img src="https://avatars.githubusercontent.com/u/66537133?s=400&u=82d981fa4f723616d5809b2fc3f84999b8d29fbe&v=4" 
#       alt="Jhoan David Pillapa Llerena" 
#       style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; margin-right: 20px; border: 2px solid #31333f;">
#  
#<div>
#    <h3 style="margin: 0; color: white;">Jhoan David Pillapa Llerena</h3>
#    <h4 style="margin: 5px 0; color: #ff4b4b;">Data Engineer</h4>
#    <p style="margin: 0 0 10px 0; color: #fafafa; font-size: 0.9rem;">
#      Experto en transformar grandes volúmenes de datos en insights accionables para acelerar el crecimiento del negocio. Especialista en automatización de reportes (Power BI/Python).
#    </p>
#    
#    <!-- Contenedor de Redes Sociales -->
#    <div style="display: flex; gap: 12px; align-items: center;">
#      <!-- LinkedIn -->
#      <a href="https://www.linkedin.com/in/jhoandavidpll/" target="_blank" style="text-decoration: none;">
#        <img alt="Jhoan Pillapa | Linkedin" width="28px" src="https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/linkedin-svgrepo-com.svg" style="display: block;">
#      </a>
#      <a href="https://github.com/jhoandavidpll" target="_blank" style="text-decoration: none;">
#        <img alt="Jhoan Pillapa | Github" width="28px" src="https://raw.githubusercontent.com/jhoandavidpll/jhoandavidpll/ef3b53d05731828b91f73ee7ef1fcedab18bd89b/img/github-color-svgrepo-com.svg" style="display: block;">
#      </a>
#    </div>
#  </div>
#</div>
#""")

    #Seccion: Herramientas
herramientas.write("""
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
    <h1>Stack Tecnologico</h1>
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

herramientas.write("---")

    #Anexos
enlaces.write("""
    <h1>Enlaces</h1>
    <ul>
        <li><a href='https://www.youtube.com'>Video Demo</a></li>
        <li><a href='https://www.canva.com/design/DAG8qnGYp1c/-nmKgA5yGP5BC8sAsg2SAA/edit'>Canva</a></li>
        <li><a href='https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/tree/DS'>Github</a></li>
        <li><a href='https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/DS/README.md'>Readme</a></li>
    </ul>
""", unsafe_allow_html=True)
    