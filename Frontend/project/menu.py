import streamlit as st

def generar_menu():
    # 1. Definimos el estilo CSS para que parezca una barra de navegación
    # Esto pone el fondo gris claro y ajusta padding
    # CSS PARA ELIMINAR LA BARRA NATIVA Y EL ESPACIO VACÍO
    estilo_limpieza = """
    <style>
        /* 1. Ocultar la barra superior (Header) donde está el botón Deploy */
        [data-testid="stHeader"] {
            visibility: hidden;
            height: 0px; /* Forzamos a que no ocupe altura */
        }

        /* 2. Subir el contenido principal para eliminar el espacio vacío de arriba */
        /* Streamlit añade mucho padding por defecto, aquí lo reducimos a 0 o 1rem */
        .block-container {
            padding-top: 0rem; 
            padding-bottom: 0rem;
        }
        
        /* Opcional: Si quieres ocultar el footer "Made with Streamlit" */
        footer {visibility: hidden;}
    </style>
    """
    st.markdown(estilo_limpieza, unsafe_allow_html=True)

    # 2. Creamos columnas: Una pequeña para el logo/título y otra para los enlaces
    with st.container():
        # Ajusta las proporciones: col1 (logo) pequeña, col2 (espacio), col3 (menú)
        col1, col2 = st.columns([1, 3]) 
        
        with col1:
            # Puedes usar st.image("tu_logo.png", width=150) aquí
            st.markdown("### 🏅Startup") # Simulación de tu logo

        with col2:
            # Usamos una columna dentro de la columna para alinear a la derecha o centro
            # Streamlit pone los botones verticales por defecto, así que usamos cols internas
            m1, m2, m3, m4 = st.columns(4)
            
            with m1:
                st.page_link("Inicio.py", label="Inicio", icon="🏠")
            with m2:
                st.page_link("pages/1_Histórico.py", label="Histórico", icon="📈")
            with m3:
                st.page_link("pages/2_Documentación.py", label="Documentación", icon="📚")
            with m4:
                st.page_link("pages/3_Acerca.py", label="Acerca", icon="ℹ️")
        
        st.write("---") # Una línea separadora opcional