# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimientos 

## Organizadores
<p>
  <img src="https://nocountry.tech/one.png" width="20%" />
  <img src="https://nocountry.tech/success-cases/hackathon-one/logos/alura-logo.png" width="20%" />
  <img src="https://nocountry.tech/images/oracle-logo.webp" width="20%" />
</p>

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

# Herramientas y versiones
- Java 21.0.8
- Python 3.13.9
- Docker 29.1.3

![Java](https://img.shields.io/badge/java-21.0.8-white)
![Python](https://img.shields.io/badge/python-3.13.9-blue)
![Docker](https://img.shields.io/badge/docker-29.1.3-0db7ed)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.5-gray)

# Requerimientos
- streamlit
- pandas
- scikit-learn
- textblob
