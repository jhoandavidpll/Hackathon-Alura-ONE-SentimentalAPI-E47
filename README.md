# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimientos 
# Stack
![Java](https://img.shields.io/badge/java-21.0.8-white?logo=java)
![Python](https://img.shields.io/badge/python-3.13.9-blue?logo=python)
![Docker](https://img.shields.io/badge/docker-29.1.3-0db7ed?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.5-gray?logo=postgresql)
![Colab](https://img.shields.io/badge/Colab-gray?logo=googlecolab)

## Notebooks
[![Colab Español](https://img.shields.io/badge/Colab_Español-gray?logo=googlecolab)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_Analisis_de_Sentimientos_Completo_Espa%C3%B1ol_15_Enero.ipynb)
[![Colab](https://img.shields.io/badge/Colab_Portugués-gray?logo=googlecolab)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_An%C3%A1lisis_de_Sentimientos_Completo_Portugues_15_Ene.ipynb)


## Organizadores
<p>
  <img src="https://nocountry.tech/one.png" width="20%" />
  <img src="https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/alura_latam.png" width="20%" />
  <img src="https://nocountry.tech/images/oracle-logo.webp" width="20%" />
</p>

![Logo BEEsionary](https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/logo_BEE.png)

# Startup SentimentalAPI
![infraestructura](https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/Infraestrucura_sentimentAPI.png)
# Integrantes del Proyecto
- Jhoan David Pillapa Llerena
- Mitchel David Poblete Santibañez
- Andres Felipe Cubillos Hurtado
- Brandon Omar Ortiz Gutierrez  
- David Avila  
- Nydia Olmos  
- Andrés Huerta Salgado  
- Cristian Armando Larios Bravo


# Estructura del Proyecto

```text
REPO/
│
├── Backend/                 # (Squad Java Spring Boot)
│   ├── src/                 # Código fuente Java
│   │    └── main
│   │       └──java/equipo/_7/SentimentAPIAplication.java  #programa principal
│   └── pom.xml              # Dependencias Maven
│
│
├── Frontend/                # (Squad Presentación - Streamlit)
│   ├── projecct              # Interfaz gráfica (Python)
│   │    ├── Inicio.py        # Primera página para anpalisis individuales
│   │    └── pages/
│   │          ├── 1.Batching.py       # Análisis colectivo
│   │          ├── 2.Histórico.py      # Histórico de análisis
│   │          ├── 3.Estadísticas.py   # Estadísticas de los análisis
│   │          └── 4.Acerca.py         # Acerca de Nosotros
│   └── requirements.txt     # streamlit, requests
│
├── Data-Science/            # (Squad Entrenamiento & Exploración)
│   ├── Notebooks/           # Jupyter Notebooks (Zona de pruebas)
│   ├── data/                # CSVs crudos (Raw data)
│   │    ├── / spanish
│   │    ├── / portuges      
│   └── models/              # Serialización de los modelos
│   │   ├── model_es.onnx    # Modelo en Español
│   │   └── model_pt.onnx    # Modelo en Portugues
│
├── .gitignore               # Ignora __pycache__, .class, .ipynb_checkpoints
└── README.md                # Documentación general
```

# Requerimientos
- streamlit
- pandas
- scikit-learn
- nltk
- emoji

# Modelo Seleccionado en PORTUGUES : SGDClassifier como Regresión Logística 

## Modelo SGD
<img src="https://i.imgur.com/nHfsHRh.png" alt="Modelo SGD" width="300">

## Distribución de negativos y positivos
<img src="https://i.imgur.com/nHfsHRh.png](https://i.imgur.com/SYL6oqZ.png" alt="Modelo SGD" width="300">

## Porcentajes de predicción
<img src="https://i.imgur.com/nHfsHRh.png](https://i.imgur.com/JGKb6lj.png" alt="Modelo SGD" width="300">


## Falsos positivos y negativos
<img src="https://i.imgur.com/YYHpSqH.png" alt="Modelo SGD" width="300">

# Modelo Seleccionado en ESPAÑOL: SGDClassifier como Regresión Logística 

## Modelo SGD
<img src="https://i.imgur.com/pKarVla.png" alt="Modelo SGD" width="300">


## Distribución de negativos y positivos
<img src="https://i.imgur.com/ma7pg0u.png" alt="Modelo SGD" width="300">

## Porcentajes de predicción
<img src="[h](https://i.imgur.com/foWGLrS.png)" alt="Modelo SGD" width="300">


## falsos positivos y negativos
<img src="https://i.imgur.com/MYb6tFD.png" alt="Modelo SGD" width="300">

