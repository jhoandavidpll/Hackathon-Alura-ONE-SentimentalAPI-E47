<img src="https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/logo_BEE.png?raw=true" width="100%" />

# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimientos 

## Organizadores
<p style="display: flex; justify-content: space-between;">
  <img src="https://nocountry.tech/one.png" width="20%" />
  <img src="https://nocountry.tech/nocountry-logo.png" width="20%" />
  <img src="https://nocountry.tech/images/oracle-logo.webp" width="20%" />
</p>

# Datos generales
## Integrantes del Proyecto
- Jhoan David Pillapa Llerena
- Mitchel David Poblete Santibañez
- Andres Felipe Cubillos Hurtado
- Brandon Omar Ortiz Gutierrez  
- David Avila  
- Nydia Naomi Olmos Romero
- Andrés Huerta Salgado  
- Cristian Armando Larios Bravo
- Jeferson Peña


## Estructura del Proyecto

```text
REPO-ROOT/
│
├── Backend/                 # (Squad Java Spring Boot)
│   ├── src/                 # Código fuente Java
│   ├── pom.xml              # Dependencias Maven
│   └── compose.yaml         # Contenedor de la base de datos
│
├── Frontend/                # (Squad Presentación - Streamlit)
│   ├── app.py               # Interfaz gráfica (Python)
│   ├── img/                 # Logos, imágenes estáticas
│   └── requirements.txt     # streamlit, requests
│
├── Data-Science/            # (Squad Entrenamiento & Exploración)
│   ├── Notebooks/           # Jupyter Notebooks (Zona de pruebas)
│   ├── data/                # CSVs crudos (Raw data)
│   └── models/              # Modelos a implementar
│
├── .gitignore               # Ignora __pycache__, .class, .ipynb_checkpoints
└── README.md                # Documentación general
```

## Herramientas y versiones

[![Java](https://img.shields.io/badge/java-21.0.8-white?logo=java)]
[![Python](https://img.shields.io/badge/python-3.13.9-blue?logo=python)]
[![Docker](https://img.shields.io/badge/docker-29.1.3-0db7ed?logo=docker)]
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.5-gray?logo=postgresql)]
[![Colab](https://img.shields.io/badge/Colab-gray?logo=googlecolab)]

## Requerimientos
- streamlit
- pandas
- nltk
- plotly
- seaborn
- matplotlib
- numpy
- scikit-learn
- sklearn
- textblob
- requests


# Modelo Seleccionado en PORTUGUES : SGDClassifier como Regresión Logística 

# Modelo SGD
![Modelo SGD](https://i.imgur.com/nHfsHRh.png)

# Distribución de negativos y positivos
![Distribución Positivos y negativos](https://i.imgur.com/SYL6oqZ.png)

# Porcentajes de predicción
![Porcentaje de Predicción ](https://i.imgur.com/JGKb6lj.png) 

# falsos positivos y negativos
![Curva ROC AUC 0.834](https://i.imgur.com/YYHpSqH.png)


# Modelo Seleccionado en ESPAÑOL: SGDClassifier como Regresión Logística 

# Modelo SGD
![Modelo SGD](https://i.imgur.com/pKarVla.png)

# Distribución de negativos y positivos
![Distribución Positivos y negativos](https://i.imgur.com/ma7pg0u.png)

# Porcentajes de predicción
![Porcentaje de Predicción ](https://i.imgur.com/foWGLrS.png) 

# Falsos positivos y negativos
![Curva ROC AUC 0.834](https://i.imgur.com/MYb6tFD.png)
