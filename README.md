# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimientos 

## Organizadores
<p>
  <img src="https://nocountry.tech/one.png" width="20%" />
  <img src="https://nocountry.tech/images/alura-latam-logo.1750260032.png" width="20%" />
  <img src="https://nocountry.tech/images/oracle-logo.webp" width="20%" />
</p>

![Logo BEEsionary](https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/logo_BEE.png)

# Startup SentimentalAPI
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
REPO-ROOT/
│
├── Backend/                 # (Squad Java Spring Boot)
│   ├── src/                 # Código fuente Java
│   ├── pom.xml              # Dependencias Maven
│   └── Dockerfile           # Expone puerto 8080
│
├── Model-Service/           # (Squad FastAPI - Microservicio de IA)
│   ├── app/
│   │   ├── main.py          # Lógica de predicción y carga de modelos
│   │   └── schemas.py       # Definición de datos
│   ├── models/              # [CRÍTICO] Aquí se guardan los .joblib finales
│   │   ├── model_es.joblib  # (Generado por Squad Data Science)
│   │   └── model_pt.joblib  # (Generado por Squad Data Science)
│   ├── Dockerfile           # Expone puerto 5000 (interno)
│   └── requirements.txt     # scikit-learn, joblib
│
├── Frontend/                # (Squad Presentación - Streamlit)
│   ├── app.py               # Interfaz gráfica (Python)
│   ├── assets/              # Logos, imágenes estáticas
│   ├── Dockerfile           # Expone puerto 8501
│   └── requirements.txt     # streamlit, requests
│
├── Data-Science/            # (Squad Entrenamiento & Exploración)
│   ├── Notebooks/           # Jupyter Notebooks (Zona de pruebas)
│   ├── data/                # CSVs crudos (Raw data)
│   └── training/            # Scripts limpios (.py) que generan los modelos
│
├── docker-compose.yml       # El "Director de Orquesta"
├── .gitignore               # Ignora __pycache__, .class, .ipynb_checkpoints
└── README.md                # Documentación general
```

![Java](https://img.shields.io/badge/java-21.0.8-white?logo=java)
![Python](https://img.shields.io/badge/python-3.13.9-blue?logo=python)
![Docker](https://img.shields.io/badge/docker-29.1.3-0db7ed?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.5-gray?logo=postgresql)
![Colab](https://img.shields.io/badge/Colab-gray?logo=googlecolab)

# Requerimientos
- streamlit
- pandas
- scikit-learn
- nltk
- emoji

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

# falsos positivos y negativos
![Curva ROC AUC 0.834](https://i.imgur.com/MYb6tFD.png)
