import streamlit as st
import nltk
import pandas as pd
from nltk.corpus import stopwords
from pathlib import Path
import emoji
import re

# --- ESTILOS CSS PERSONALIZADOS ---
import streamlit as st

def estilo():
    return st.markdown("""
        <style>
        /* 1. Fondo principal - Oscuro y profundo */
        .stApp {
            background: #283241; /* Un negro muy oscuro para el espacio profundo */
            overflow-x: hidden; /* Evitar scroll horizontal si las estrellas se mueven */
        }

        /* 2. Capa de estrellas #1 (fondo, movimiento lento) */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 200%; /* El doble de alto para que haya scroll de estrellas */
            background: 
                radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.08) 1px, transparent 15px),
                radial-gradient(circle at 30% 70%, rgba(255, 255, 255, 0.06) 1px, transparent 12px),
                radial-gradient(circle at 60% 10%, rgba(255, 255, 255, 0.07) 1px, transparent 18px),
                radial-gradient(circle at 80% 50%, rgba(255, 255, 255, 0.09) 1px, transparent 10px);
            background-size: 300px 300px, 400px 400px, 350px 350px, 250px 250px;
            animation: moveStarsBg 180s linear infinite; /* Movimiento muy lento */
            z-index: -3; /* La capa más lejana */
            opacity: 0.9;
        }

        /* 3. Capa de estrellas #2 (medio, movimiento medio) */
        .stApp::after {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 200%; /* También el doble de alto */
            background: 
                radial-gradient(circle at 50% 30%, rgba(255, 255, 255, 0.15) 1px, transparent 10px),
                radial-gradient(circle at 20% 80%, rgba(255, 255, 255, 0.12) 1px, transparent 8px),
                radial-gradient(circle at 70% 60%, rgba(255, 255, 255, 0.13) 1px, transparent 11px);
            background-size: 200px 200px, 250px 250px, 180px 180px;
            animation: moveStarsMd 120s linear infinite; /* Movimiento medio */
            z-index: -2; /* Capa intermedia */
            opacity: 0.8;
        }

        /* 4. Capa de constelaciones brillantes (primer plano, movimiento más rápido y color) */
        body { /* Inyectamos aquí una capa extra de estrellas más grandes */
            background-image: 
                radial-gradient(circle at 80% 20%, rgba(255, 200, 25, 0.2) 2px, transparent 25px), /* Dorada */
                radial-gradient(circle at 30% 90%, rgba(100, 200, 255, 0.25) 2px, transparent 20px), /* Azul brillante */
                radial-gradient(circle at 10% 10%, rgba(255, 100, 100, 0.2) 2px, transparent 30px); /* Roja */
            background-size: 400px 400px, 500px 500px, 350px 350px;
            background-repeat: repeat;
            animation: moveStarsFg 60s linear infinite; /* Movimiento más rápido */
            z-index: -1; /* Capa más cercana */
            opacity: 0.7;
        }

        /* Animaciones de movimiento vertical */
        @keyframes moveStarsBg { from { background-position: 0 0; } to { background-position: 0 1000px; } }
        @keyframes moveStarsMd { from { background-position: 0 0; } to { background-position: 0 1500px; } }
        @keyframes moveStarsFg { from { background-position: 0 0; } to { background-position: 0 2000px; } }


        /* --- TUS ESTILOS BASE Y DE CARD MANTENIDOS --- */
        .stDownloadButton {
            display: flex; 
            justify-content: center; 
            align-items: center;
        }

        /* Contenedor principal tipo 'Isla' con fondo translúcido */
        .main-card {
            background-color: rgba(255, 255, 255, 0.08); /* Fondo muy sutilmente visible */
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.6); /* Sombra intensa para que flote */
            margin-top: 20px;
            backdrop-filter: blur(8px); /* Efecto cristal */
            border: 1px solid rgba(255, 255, 255, 0.1); /* Borde sutil brillante */
            position: relative; /* Asegura que la tarjeta esté encima de las estrellas */
            z-index: 10;
        }

        /* Personalización del botón */
        div.stButton > button {
            width: 100%;
            background-color: #c50707;
            color: white;
            border-radius: 10px;
            border: none;
            height: 3em;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(197, 7, 7, 0.4);
        }
        
        /* 5. Botón tipo "Power-up" */
        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #c50707 0%, #9e0505 100%);
            color: white;
            border: none;
            padding: 15px;
            border-radius: 12px;
            font-weight: bold;
            transition: 0.3s;
            box-shadow: 0 4px 15px rgba(197, 7, 7, 0.4);
        }

        div.stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 0 20px rgba(255, 193, 7, 0.6);
            background: #FFC107;
            color: #121212;
        }
        
        /* Títulos dentro de la isla - con gradiente sutil y contraste */
        .card-title {
            color: #E0E7FF; /* Color de texto más brillante */
            font-family: 'sans-serif';
            font-weight: bold;
            font-size: 28px; /* Un poco más grande */
            margin-bottom: 20px;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3); /* Ligero resplandor */
            text-align: center;
        }

        /* Asegurarse de que el resto del texto sea legible */
        .stMarkdown, .stText, .stLabel, .stSlider label {
            color: #E0E7FF;
        }
        </style>
        """, unsafe_allow_html=True)


def estilo_resulado(): 
    return st.markdown(
    """
    <style>
    .card {
        background-color: rgba(95,100,120,0.7);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .comentario {
        background-color: rgba(29,31,54,0.8);
        padding: 16px;
        border-radius: 12px;
        font-style: italic;
        margin-bottom: 8px;
    }
    .resultado {
        display: flex;
        gap: 20px;
        align-items: center;
    }
    .badge-positivo {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        color: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        min-width: 180px;
        font-size: 20px;
        font-weight: bold;
    }
    .badge-negativo {
        background: linear-gradient(135deg, #e74c3c, #9E0808);
        color: white;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        min-width: 180px;
        font-size: 20px;
        font-weight: bold;
    }
    .barra-container {
        width: 100%;
    }
    .barra {
        height: 16px;
        border-radius: 10px;
        background-color: #e0e0e0;
        margin-bottom: 10px;
        overflow: hidden;
    }
    .barra-positiva {
        height: 100%;
        background-color: #2ecc71;
    }
    .barra-negativa {
        height: 100%;
        background-color: #e74c3c;
    }
    .label {
        font-size: 16px;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# FUNCIONES DE TRATAMIENTO DE COMENTARIOS
def descarga_stopwords():
    try:
        stopwords_path = Path(nltk.data.find('corpora/stopwords'))

        if stopwords_path.exists():
            return True
        else:
            nltk.download('stopwords')
            return True
        
    except LookupError:
        nltk.download('stopwords')
        return True
    except Exception as e:
        return False

def limpieza_pt(texto):
    stop_words = set(stopwords.words('portuguese'))
    stop_words = {
    w.replace("á","a").replace("é","e").replace("í","i")
        .replace("ó","o").replace("ú","u")
        for w in stop_words
    }
    negaciones = {"não", "nem", "nunca", "jamais"}
    stop_words = stop_words - negaciones

    texto = str(texto)

    texto = texto.lower()

    texto = emoji.demojize(texto, delimiters=(" ", " "), language='pt').lower()

    # Normalizar alargamientos
    texto = re.sub(r'(.)\1{2,}', r'\1\1', texto)

    # Elimina urls
    texto = re.sub(r'https?:///\S+|www\.\S+', '', texto)
    # Elimia los @
    texto = re.sub(r'@\w+', '', texto)
    # Elimina el #
    texto = texto.replace("#", "")

    # Eliminar caracteres no alfabéticos - INCLUIR CARACTERES PORTUGUESES
    # áàâãéèêíïóôõöúçñ
    texto = re.sub(r'[^a-záàâãéèêíïóôõöúçñ0-9\s]', ' ', texto)

    # Unir negaciones EN PORTUGUÉS
    texto = re.sub(r'\b(não|nem|nunca|jamais)\s+(\w+)', r'\1_\2', texto)

    palabras = texto.split()
    palabras = [p for p in palabras if p not in stop_words]

    return ' '.join(palabras)

def limpieza_es(texto):
    stop_words = set(stopwords.words('spanish'))
    stop_words = {
        w.replace("á","a").replace("é","e").replace("í","i")
        .replace("ó","o").replace("ú","u")
        for w in stop_words
    }
    negaciones = {"no", "ni", "nunca", "jamas"}
    stop_words = stop_words - negaciones

    texto = emoji.demojize(texto, delimiters=(" ", " "), language='es').lower()

    # Normalizar repeticiones
    texto = re.sub(r'(.)\1{2,}', r'\1\1', texto)

    # Normalización de jergas
    diccionario = {
        'lol': 'reirse_mucho',
        'lmao': 'reirse_mucho',
        'wtf': 'que_demonios',
        'nmm': 'no_mames',
        'nmms': 'no_mames',
        'tqm': 'te_quiero_mucho',
        'rip': 'descanse_en_paz',
        'omg': 'oh_dios_mio',
        'sierto': 'cierto',
        'alv': 'a_la_verg',
        'gg': 'buen_juego',
        'wp': 'bien_jugado',
        'rofl': 'revolcarse_de_risa',
        'npn': 'no_pasa_nada',
        'ntp': 'no_pasa_nada',
    }

    items_ordenados = sorted(diccionario.items(),
                            key=lambda x: len(x[0]),
                            reverse=True)
    for abrev, expansion in items_ordenados:
        patron = r'\b' + re.escape(abrev.strip()) + r'\b'
        texto = re.sub(patron, expansion.strip(), texto, flags=re.IGNORECASE)

    # Quitar tildes
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")

    # Elimina numeros
    texto = re.sub(r'\d+', '', texto)
    # Elimina urls
    texto = re.sub(r'https?:///\S+|www\.\S+', '', texto)
    # Elimia los @
    texto = re.sub(r'@\w+', '', texto)
    # Elimina el #
    texto = texto.replace("#", "")

    # Normaliza los espacios
    texto = re.sub(r'\s+', ' ', texto)

    # Filtrar stopwords
    palabras = texto.split()
    palabras = [p for p in palabras if p not in stop_words and len(p) > 1]
    return ' '.join(palabras)

def limpieza_df(file, idioma):
    df = pd.read_csv(file)

    if "comentarios" not in df.columns:
        return None

    # Aplica la limpieza segun el idioma
    df_limpio = df.copy()
    if idioma == "ES":
        df_limpio["limpios"] = df_limpio["comentarios"].apply(limpieza_es)
    else:
        df_limpio["limpios"] = df_limpio["comentarios"].apply(limpieza_pt)

    # Retorna el archivo a enviar
    return df_limpio[['comentarios', 'limpios']]