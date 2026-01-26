<img src="https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/logo_BEE.png?raw=true" width="100%" />

# Hackathon-Alura-ONE-SentimentalAPI-E47
Proyecto de Data Science y Backend sobre una API de Análisis de Sentimientos 

## Stack
![Java](https://img.shields.io/badge/java-21.0.8-white?logo=java)
![Python](https://img.shields.io/badge/python-3.13.9-blue?logo=python)
![Docker](https://img.shields.io/badge/docker-29.1.3-0db7ed?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17.5-gray?logo=postgresql)
![Colab](https://img.shields.io/badge/Colab-gray?logo=googlecolab)

## Links más importantes

**Proyecto funcional en la nube**

[![BEEsionary](https://img.shields.io/badge/BEEsionary-gray)](http://129.213.21.63:8501/)


**Repositorio**

[![Repositorio](https://img.shields.io/badge/Repositorio-gray?logo=github)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/)

**Video demostración**

[![Video presentación](https://img.shields.io/badge/Video-gray?logo=youtube)](https://www.youtube.com/watch?v=-Fnpv2fOMsA)

**Notebooks**

[![Colab Español](https://img.shields.io/badge/Colab_Español-gray?logo=googlecolab)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_Analisis_de_Sentimientos_Completo_Espa%C3%B1ol_15_Enero.ipynb)
[![Colab Portugués](https://img.shields.io/badge/Colab_Portugués-gray?logo=googlecolab)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_An%C3%A1lisis_de_Sentimientos_Completo_Portugues_15_Ene.ipynb)

## Índice

* [Título e imagen de portada](#Hackathon-Alura-ONE-SentimentalAPI-E47)
    * [Stack tecnológico](#Stack)
    * [Links más importantes](#Links-más-importantes)
    * [Índice](#Índice)
    * [Organizadores](#Organizadores)
* [Datos generales](#Datos-generales)
    * [Integrantes del Proyecto](#Integrantes-del-Proyecto)
    * [Estructura del Proyecto](#Estructura-del-Proyecto)
    * [Requerimientos](#Requerimientos)
* [Documentación Frontend](#Front)
* [Documentación Backend](#Backend)
    * [Tecnologías](#Tecnologías)
    * [Configuración del proyecto](#Configuración-del-proyecto)
    * [Ejecución del proyecto](#Ejecución-del-proyecto)
    * [Endpoints principales](#Endpoints-principales)
    * [Consumo de la API](#Consumo-de-la-API)
* [Documentación Data Science](#Data-Science)
    * [Modelo PORTUGUÉS](#Modelo-Seleccionado-en-PORTUGUÉS:-SGDClassifier-como-Regresión-Logística)
    * [Modelo ESPAÑOL](#Modelo-Seleccionado-en-ESPAÑOL:-SGDClassifier-como-Regresión-Logística)


## Organizadores
<p style="display: flex; justify-content: space-between;">
  <img src="https://nocountry.tech/one.png" width="20%" />
  <img src="https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/alura_latam.png" width="20%" />
  <img src="https://nocountry.tech/images/oracle-logo.webp" width="20%" />
  <img src="https://nocountry.tech/nocountry-logo.png" width="20%" />
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
REPO/
│
├── Backend/                 # (Squad Java Spring Boot)
│   ├── src/                 # Código fuente Java
│   │    └── main
│   │       └──java/equipo/_7/SentimentAPIAplication.java  # Programa principal
│   │── pom.xml              # Dependencias Maven
│   └── compose.yaml         # Contenedor de la base de datos
│
│
├── Frontend/                # (Squad Presentación - Streamlit)
│   ├── projecct              # Interfaz gráfica (Python)
│   │    ├── Inicio.py        # Primera página para análisis individuales
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

# Frontend

# Backend 

La API desarrollada con Java 21.0.8 con Spring Boot en su versión 3.3.9, implementa una base de datos PostgreSQL en su versión 17.5 contenerizada en Docker. Hace uso de Flyway para migraciones y manejo de la base de datos. Implementa el dos modelos capaces de clasificar sentimientos en base a comentarios extraídos de la red social Twitter a través de ONNX.

La API se basa en un CRUD básico en el cual permite hacer clasificaciones simples (un único comentario), clasificaciones en batch (a través de archivos csv), listar todas las clasificaciones existentes en la base de datos, eliminar comentario analizado de la base de datos, listar el top 5 palabras más repetidas según el idioma y el sentimiento, y la cantidad de comentarios negativos y positivos que existen según el idioma.

## Tecnologías

- spring-boot
- jakarta
- flywaydb
- opencsv
- postgresql
- spring-boot-docker-compose
- org.springframework.ai
- spring-boot-starter-validation
- lombok

## Configuración del proyecto

Para poder compilar y ejecutar el proyecto sin muchas complicaciones es necesario ya sea o bien definir las variables de entorno, agregando un archivo . envv o bien modificar los archivos application.properties y compose.yaml. Las variables de entrono implementadas son:

- DB_HOST
- DB_USER
- DB_PASSWORD

En caso de correr la API de forma local la variable de entorno DB_HOST se le debe de asignar el valor localhost, el resto de las variables dependen de la configuración que se tenga en el postgreSQL.

## Ejecución del proyecto

1. Clona el repositorio
  ```git clone https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47.git```
2. Entra al directorio del backend:
  ```cd Hackathon-Alura-ONE-SentimentalAPI-E47/Backend```
3. Compila el proyecto en la carpeta /target:
  ```mvn clean package -DskipTests```
4. Ejecuta la aplicación en la ruta raíz del backend:
  ```mvn spring-boot:run```

## Endpoints principales

| Método | Endpoint             | Descripción                                    |
|--------|----------------------|------------------------------------------------|
| POST   | /predict             | Clasificación simple (único comentario)        |
| POST   | /predict/csv         | Clasificación en batch (archivo csv)           |
| GET    | /predict/            | Listado de todas las clasificaciones           |
| GET    | /predict/{id}        | Obtiene la clasificación del id especificado   |
| GET    | /predict/stats       | Cantidad de comentarios por sentimiento        |
| GET    | /predict/stats/words | Top 5 palabras más repetidas                   |
| DELETE | /predict/{id}        | Elimina la clasificación con el id especificado|

## Consumo de la API

### Clasificación simple

- **Método:** POST

- **Endpoint:** /predict

#### Envía
```
{
	"comentario": "Odio trabajar en domingo",
	"comentario_limpio": "odio trabajar domingo",
	"modelo": "ES"
}
```
#### Recibe
```
{
	"id": 377,
	"comentario": "Odio trabajar en domingo",
	"prevision": "Negativo",
	"probabilidad": 0.3240935,
	"idioma": "ES",
	"fecha": "2026-01-25T15:33:47.2695179"
}
```

### Clasificación en batch

- **Método:** POST

- **Endpoint:** /predict/csv

#### Envía
<img width="538" height="233" alt="image" src="https://github.com/user-attachments/assets/e8aea7d3-144c-4b13-a1fd-4557b6fee29b" />

#### Recibe
```
[
	{
		"id": 378,
		"comentario": "Fico muito triste com a forma como a sociedade está hoje.",
		"prevision": "Negativo",
		"probabilidad": 0.8674735,
		"idioma": "PT",
		"fecha": "2026-01-25T17:41:15.2761158"
	},
	{
		"id": 379,
		"comentario": "A organização desta sociedade é terrível.",
		"prevision": "Negativo",
		"probabilidad": 0.73947096,
		"idioma": "PT",
		"fecha": "2026-01-25T17:41:15.2915533"
	},
	{
		"id": 380,
		"comentario": "Considero a série incrível, a melhor que já vi.",
		"prevision": "Positivo",
		"probabilidad": 0.91232455,
		"idioma": "PT",
		"fecha": "2026-01-25T17:41:15.297732"
	},
	{
		"id": 381,
		"comentario": "Eu amo como o cabelo dela brilha assim.",
		"prevision": "Positivo",
		"probabilidad": 0.81699395,
		"idioma": "PT",
		"fecha": "2026-01-25T17:41:15.3036343"
	}
]
```
#### Archivo
ejemplo.csv
```
comentarios, limpios
"Fico muito triste com a forma como a sociedade está hoje.", "fico muito triste forma sociedade esta hoje."
"A organização desta sociedade é terrível.","a organização desta sociedade terrivel."
"Considero a série incrível, a melhor que já vi.","considero serie incriveli melhori ja vi."
"Eu amo como o cabelo dela brilha assim.","eu amo cabelo dela brilha assim."
```

### Listado de clasificaciones

- **Método:** GET

- **Endpoint:** /predict

#### Recibe
```
{
	"content": [
		{
			"id": 333,
			"comentario": "Este es el mejor análizador de sentimientos!!! 🎉",
			"prevision": "Positivo",
			"probabilidad": 1.1294278,
			"idioma": "ES",
			"fecha": "2026-01-23T14:30:20.355075"
		},
		{
			"id": 334,
			"comentario": "Gracias a AluraLatam, Oracle, a los patrocinadores y a todo el equipo de organización por esta oportunidad 😍❤️ ",
			"prevision": "Positivo",
			"probabilidad": 0.1668056,
			"idioma": "ES",
			"fecha": "2026-01-23T14:30:20.369433"
		},
		{
			"id": 335,
			"comentario": "Primavera es la estación que más me desespera, esta alergía no me deja respirar.",
			"prevision": "Negativo",
			"probabilidad": 2.5198066,
			"idioma": "ES",
			"fecha": "2026-01-23T14:30:20.376229"
		},
		{
			"id": 352,
			"comentario": "Fico muito triste com a forma como a sociedade está hoje.",
			"prevision": "Negativo",
			"probabilidad": 0.8674735,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:23.953816"
		},
		{
			"id": 353,
			"comentario": "A organização desta sociedade é terrível.",
			"prevision": "Negativo",
			"probabilidad": 0.73947096,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:23.988173"
		},
		{
			"id": 354,
			"comentario": "Considero a série incrível, a melhor que já vi.",
			"prevision": "Positivo",
			"probabilidad": 0.91232455,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:23.995212"
		},
		{
			"id": 355,
			"comentario": "Eu amo como o cabelo dela brilha assim.",
			"prevision": "Positivo",
			"probabilidad": 0.81699395,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:24.000856"
		},
		{
			"id": 356,
			"comentario": "Fico muito triste com a forma como a sociedade está hoje.",
			"prevision": "Negativo",
			"probabilidad": 0.8674735,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:24.007202"
		},
		{
			"id": 357,
			"comentario": "A organização desta sociedade é terrível.",
			"prevision": "Negativo",
			"probabilidad": 0.73947096,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:24.013302"
		},
		{
			"id": 358,
			"comentario": "Considero a série incrível, a melhor que já vi.",
			"prevision": "Positivo",
			"probabilidad": 0.91232455,
			"idioma": "PT",
			"fecha": "2026-01-23T14:40:24.018659"
		}
	],
	"pageable": {
		"pageNumber": 0,
		"pageSize": 10,
		"sort": {
			"empty": false,
			"sorted": true,
			"unsorted": false
		},
		"offset": 0,
		"unpaged": false,
		"paged": true
	},
	"last": false,
	"totalElements": 29,
	"totalPages": 3,
	"size": 10,
	"number": 0,
	"sort": {
		"empty": false,
		"sorted": true,
		"unsorted": false
	},
	"numberOfElements": 10,
	"first": true,
	"empty": false
}
```

### Clasificación del id especificado

- **Método:** GET

- **Endpoint:** /predict/{id}

Ejemplo: /predict/334

#### Recibe
```
{
	"id": 334,
	"comentario": "Gracias a AluraLatam, Oracle, a los patrocinadores y a todo el equipo de organización por esta oportunidad 😍❤️ ",
	"prevision": "Positivo",
	"probabilidad": 0.1668056,
	"idioma": "ES",
	"fecha": "2026-01-23T14:30:20.369433"
}
```

### Cantidad de comentarios por sentimiento

- **Método:** GET

- **Endpoint:** /predict/stats

- **Parámetros:** El "idioma" es obligatorio, las fechas son opcionales, pero si se pone una de las dos es obligatorio que la otra exista, y la fecha de inicio sea antes que la fecha fin. Los idiomas disponibles son "ES" para español y "PT" para portugués. El formato de la fecha debe de ser aaaa-mm-dd.

#### Envía
```
{
	"idioma" : "ES",
	"fecha_inicio" : "2026-01-12",
	"fecha_fin" : "2026-01-26"
}
```
#### Recibe
```
[
	{
		"palabra": "Negativo",
		"frecuencia": 5
	},
	{
		"palabra": "Positivo",
		"frecuencia": 8
	}
]
```

### Top 5 palabras más repetidas

- **Método:** GET

- **Endpoint:** /predict/stats/words

- **Parámetros:** El "idioma" y la "clasificacion" son obligatorios, las fechas son opcionales, pero si se pone una de las dos es obligatorio que la otra exista, y la fecha de inicio sea antes que la fecha fin. Los idiomas disponibles son "ES" para español y "PT" para portugués. Las clasificaciones disponibles son "Positivo" y "Negativo". El formato de la fecha debe de ser aaaa-mm-dd.
#### Envía
```
{
	"clasificacion" : "Positivo",
	"idioma" : "ES",
	"fecha_inicio" : "2026-01-23",
	"fecha_fin" : "2026-01-23"
}
```
#### Recibe
```
[
	{
		"palabra": "corazon",
		"frecuencia": 4
	},
	{
		"palabra": "analizador",
		"frecuencia": 2
	},
	{
		"palabra": "aluralatam",
		"frecuencia": 2
	},
	{
		"palabra": "ojos",
		"frecuencia": 2
	},
	{
		"palabra": "sentimientos",
		"frecuencia": 2
	}
]
```

### Elimina la clasificación del id especificado

- **Método:** DELETE

- **Endpoint:** /predict/{id}

Ejemplo: /predict/352

Estatus respuesta: 204 No content

# Data Science
## Modelo Seleccionado en PORTUGUÉS: SGDClassifier como Regresión Logística 

### Modelo SGD
<img src="https://i.imgur.com/nHfsHRh.png" alt="Modelo SGD" width="300">

### Distribución de negativos y positivos
<img src="https://i.imgur.com/nHfsHRh.png](https://i.imgur.com/SYL6oqZ.png" alt="Modelo SGD" width="300">

### Porcentajes de predicción
<img src="https://i.imgur.com/nHfsHRh.png](https://i.imgur.com/JGKb6lj.png" alt="Modelo SGD" width="300">

### Falsos positivos y negativos
<img src="https://i.imgur.com/YYHpSqH.png" alt="Modelo SGD" width="300">


## Modelo Seleccionado en ESPAÑOL: SGDClassifier como Regresión Logística 

### Modelo SGD
<img src="https://i.imgur.com/pKarVla.png" alt="Modelo SGD" width="300">

### Distribución de negativos y positivos
<img src="https://i.imgur.com/ma7pg0u.png" alt="Modelo SGD" width="300">

### Porcentajes de predicción
<img src="https://i.imgur.com/foWGLrS.png" alt="Modelo SGD" width="300">

### Falsos positivos y negativos
<img src="https://i.imgur.com/MYb6tFD.png" alt="Modelo SGD" width="300">
