# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimeintos

# Estructura del Proyecto 

# Estructura del Proyecto

```text
REPO-ROOT/
│
├── Backend-Main/            # (Squad Java Spring Boot)
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
│   └── requirements.txt     # fastapi, uvicorn, scikit-learn, joblib
│
├── Frontend/                # (Squad Presentación - Streamlit)
│   ├── app.py               # Interfaz gráfica (Python)
│   ├── assets/              # Logos, imágenes estáticas
│   ├── Dockerfile           # Expone puerto 8501
│   └── requirements.txt     # streamlit, requests
│
├── Data-Science/            # (Squad Entrenamiento & Exploración)
│   ├── notebooks/           # Jupyter Notebooks (Zona de pruebas)
│   ├── dataset/             # CSVs crudos (Raw data)
│   └── training/            # Scripts limpios (.py) que generan los modelos
│
├── docker-compose.yml       # El "Director de Orquesta"
├── .gitignore               # Ignora __pycache__, .class, .ipynb_checkpoints
└── README.md                # Documentación general