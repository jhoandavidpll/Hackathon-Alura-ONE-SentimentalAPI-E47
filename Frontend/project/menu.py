import streamlit as st

def generar_menu():
### Contenido para el header
    header = st.container()
    header.write("""
    <style>
    /*Mantener header fijo*/
    /* 1. Ocultar la barra superior (Header) donde está el botón Deploy */
        [data-testid="stHeader"] {
            display: none;
        }

        [data-testid="stMarkdownContainer"] {
            margin-top: 0;
            padding-top: 0;
        }

    /* 2. Subir el contenido principal para eliminar el espacio vacío de arriba */
    /* Streamlit añade mucho padding por defecto, aquí lo reducimos a 0 o 1rem */
        .block-container {
            padding-top: 5.5rem; 
            padding-bottom: 0rem;
        }

        div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: white;
            z-index: 1000;
            border-bottom: 1px solid #ddd;
        }

        .fixed-header h1 {
            margin: 0;
        }

        .header1{
            display: flex;
            flex-direction: row;
            align-items: center;
        }
        .header2{
            display: flex;
            flex: 2;
            flex-direction: row;
            align-items: center;
            justify-content: space-around;
            margin: 0;
        }
        .header2 li{
            list-style-type: none;
            padding-left: 0;
        }

    /*Borrar formato de hipervinculo*/
        a {
            text-decoration: none !important; /* Quita el subrayado */
            color: inherit !important;       /* Mantiene el color del texto circundante */
        }
    </style>

    <div class='fixed-header'>
        <div class='header1'>
            <h1>🏅SentimentAPI</h1>
            <ul class='header2'>
                <li><a href='/' target='_self'>Inicio</a></li>
                <li><a href='/Histórico' target='_self'>Histórico</a></li>
                <li><a href='/Documentación' target='_self'>Documentación</a></li>
                <li><a href='/Acerca' target='_self'>Acerca</a></li>
            </ul>
        </div>
    <div/>
    """, unsafe_allow_html=True)