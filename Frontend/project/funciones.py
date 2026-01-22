import streamlit as st
import nltk
from nltk.corpus import stopwords
from pathlib import Path
import emoji
import re

# --- ESTILOS CSS PERSONALIZADOS ---
def estilo():
    return st.markdown("""
        <style>
        /* Cambiar el fondo de la aplicación */
        .stApp {
            background: linear-gradient(135deg, #1E293B 0%, #1E293B 100%);
        }

        /* Contenedor principal tipo 'Isla' */
        .main-card {
            background-color: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            margin-top: 20px;
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
        }
        
        div.stButton > button:focus, div.stButton > button:active {
            background-color: transparent;
            border-radius: 10px;
            border: 2px solid #c50707;
        }

        div.stButton > button:hover {
            background-color: #9e0505;   /* rojo más oscuro */
            transform: translateY(-2px);
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.25);
            color: white;
        }
        
        /* Títulos dentro de la isla */
        .card-title {
            color: #4a4a4a;
            font-family: 'sans-serif';
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
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