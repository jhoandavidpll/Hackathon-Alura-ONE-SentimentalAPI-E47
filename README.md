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

El proyecto presente ha sido desplegado en una instancia OCI para su consumo público, se puede acceder a través del badge o haciendo click [aquí](http://129.213.21.63:8501/).

[![BEEsionary](https://img.shields.io/badge/BEEsionary-gray?logo=google)](http://129.213.21.63:8501/)


**Repositorio**

Para acceder al repositorio en github y poner a prueba el proyecto de forma local puede hacerlo haciendo click en el badge o haciendo click [aquí](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/).

[![Repositorio](https://img.shields.io/badge/Repositorio-gray?logo=github)](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/)

**Video demostración**

Para evitar hace uso de la aplicación sin conocimientos previos o haber leído la documentación primero, acceda al link que el equipo a creado haciendo una demostración ejemplo con la aplicación. Puede acceder haciendo click en el badge o haciendo click [aquí](https://www.youtube.com/watch?v=-Fnpv2fOMsA).

[![Video presentación](https://img.shields.io/badge/Video-gray?logo=youtube)](https://www.youtube.com/watch?v=-Fnpv2fOMsA)

**Notebooks**

Para visualizar el proceso detallado que siguió el equipo de Data Science para entrenar los modelos puede visualizar las notebooks, en dónde se explora de manera profunda los datasets implementados, así como las diferentes pruebas realizadas para seleccionar el modelo con el mejor desempeño. Puede acceder a las notbooks a través de los badges o bien haciendo click [aquí para el modelo en español](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_Analisis_de_Sentimientos_Completo_Espa%C3%B1ol_15_Enero.ipynb) o [aquí para el modelo en portugués](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Data-Science/Notebooks/Proyecto_API_de_An%C3%A1lisis_de_Sentimientos_Completo_Portugues_15_Ene.ipynb).

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
    * [Diagrama de arquitectura del sistema](#Diagrama-de-arquitectura-del-sistema)
    * [Estructura del Proyecto](#Estructura-del-Proyecto)
* [Documentación Backend](#Backend)
    * [Tecnologías](#Tecnologías)
    * [Configuración del proyecto](#Configuración-del-proyecto)
    * [Ejecución del proyecto](#Ejecución-del-proyecto)
    * [Endpoints principales](#Endpoints-principales)
    * [Consumo de la API](#Consumo-de-la-API)
* [Documentación Frontend](#Front)
    * [Requerimientos](#Requerimientos)
    * [Configuración del entrono](#Configuración-del-entrono)
    * [Ejecución del proyecto Frontend](#Ejecución-del-proyecto-Frontend)
    * [Interfaces del usuario](#Interfaces-del-usuario)
* [Documentación Data Science](#Data-Science)
    * [Modelo PORTUGUÉS](#modelo-seleccionado-en-portugués-sgdclassifier-como-regresión-logística)
    * [Modelo ESPAÑOL](#modelo-seleccionado-en-español-sgdclassifier-como-regresión-logística)


## Organizadores
<p style="display: flex; justify-content: space-between;">
  <img src="https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Baner.png?raw=true   " width="100%" />
</p>

# Datos generales

## Integrantes del Proyecto
- Jhoan David Pillapa Llerena
- Mitchel David Poblete Santibañez
- Andres Felipe Cubillos Hurtado
- Brandon Omar Ortiz Gutierrez  
- David Abraham Avila Castro  
- Nydia Naomi Olmos Romero
- Andrés Huerta Salgado  
- Cristian Armando Larios Bravo
- Jeferson José Peña Curvelo

## Diagrama de arquitectura del sistema

![infraestructura](https://raw.githubusercontent.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/refs/heads/main/Frontend/img/Infraestrucura_sentimentAPI.png)

## Estructura del Proyecto

```text
REPO/
│
├── Backend/                 # (Squad Java Spring Boot)
│   ├── src/                 # Código fuente Java
│   │    └── main
│   │       └──java/equipo/_7/SentimentAPIAplication
│   │                             ├──/java  # Programa principal
│   │                             └──application.properties # Configuraciones generales
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

# Backend 

La API desarrollada con Java 21.0.8 con Spring Boot en su versión 3.3.9, implementa una base de datos PostgreSQL en su versión 17.5 contenerizada en Docker. Hace uso de Flyway para migraciones y manejo de la base de datos. Implementa el dos modelos capaces de clasificar sentimientos en base a comentarios extraídos de la red social Twitter a través de ONNX.

La API se basa en un CRUD básico en el cual permite hacer clasificaciones simples (un único comentario), clasificaciones en batch (a través de archivos csv), listar todas las clasificaciones existentes en la base de datos, eliminar comentario analizado de la base de datos, listar el top 5 palabras más repetidas según el idioma y el sentimiento, y la cantidad de comentarios negativos y positivos que existen según el idioma.

## Tecnologías

- Spring-boot
- Jakarta
- Flywaydb
- Opencsv
- Postgresql
- Spring-boot-docker-compose
- Springframework ai
- Spring-boot-starter-validation
- Lombok

## Configuración del proyecto

Para poder compilar y ejecutar el proyecto sin muchas complicaciones es necesario ya sea o bien definir las variables de entorno, agregando un archivo .env o bien modificar los archivos application.properties y compose.yaml. Las variables de entrono implementadas son:

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

# Frontend

Esta aplicación frontend fue desarrollada con streamlit como una forma visual de consumir la API REST desarrollada en Spring Boot, agregando diseño, validaciones y limpieza al uso de las diferentes funcionalidades que posee la aplicación.

Permite a los usuarios hacer clasificación de comentarios simples, clasificación de comentarios a través de archivos .csv, visualización de la base de datos, eliminación de clasificaciones, visualización gráfica de estadísticas con múltiples filtros, y finalmente conocer un poco más acerca del proyecto.

## Requerimientos
- Python 3.13.9
- Streamlit
- Pandas
- Nltk
- Plotly
- Seaborn
- Matplotlib
- Numpy
- Scikit-learn
- Sklearn
- Textblob
- Requests

## Configuración del entrono

El proyecto está previamente configurado para ejecutarse sin ningún problema a través del localhost, pero en caso de que se desee usar una ip o dominio diferente será necesario modificar los archivos de Inicio.py, 1_Batching.py, 2_Histótico.py y 3_Estadísticas.py, cambiando la url a la que se consumirá la API, solo cambie el localhost por su nuevo host.

Ejemplo:

**DE**
```
response = requests.post(
    "http://localhost:8080/predict",
    json=st.session_state.data_formulario,
    headers={"Content-Type":"application/json"}
)
```
**A**
```
response = requests.post(
    "http://{NUEVO HOST}:8080/predict",
    json=st.session_state.data_formulario,
    headers={"Content-Type":"application/json"}
)
```

## Ejecución del proyecto Frontend

Para el correcto funcionamiento del proyecto es necesario tener el servicio de la API ([Ejecución del proyecto Backend](#Ejecución-del-proyecto)) ejecutándose en segundo plano para poder enviar los request.

1. Crear entorno virtual dentro del directorio Frontend:

    ```cd /Frontend```

    ([¿Cómo se crea un entorno virtual?](#Cómo-se-crea-un-entorno-virtual?))
2. Instalar dependencias dentro del entorno virtual:

   ```pip install -r requirements.txt```
3. Entra a la carpeta /project:

    ```cd /project```
3. Ejecutar aplicación:

    ```streamlit run Inicio.py```

### ¿Cómo se crea un entorno virtual?

1. Crear entorno virtual ```python -m venv nombre_entorno```
2. Activa el entorno virtual
    - Windows: ```nombre_entorno\Scripts\activat```
    - Linux/Mac: ```source nombre_entorno/bin/activate```

>*Nota:*
> El "nombre_entorno" lo puedes remplazar por el nombre que desees ponerle a tu entorno virtual.

## Interfaces del usuario

### Inicio

Esta primera vista corresponde a la clasificación simple de nuestra API. Aquí elegiremos entre los dos idiomas disponibles, escribiremos un comentario y lo enviaremos a nuestra API a ser clasificado por el modelo. Se pueden añadir emojis, hashtags, arrobas, entre otros signos especiales. Ambos modelos fueron entrenados con datos extraídos de la red social Twitter, por lo que tiende a tener mayor precisión en contextos similares.

Las posibilidades de respuestas en la clasificación son de Negativos o Positivos, además de añadir el porcentaje de precisión obtenido, y el idioma seleccionado.

![Inicio](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Inicio.gif?raw=true)

### Batching

La clasificación por batching permite clasificar múltiples comentarios escritos en el mismo idioma de forma simultánea. En esta vista es posible descargar un archivo csv base el cual sirve cómo referencia respecto al acomodo y formato que deben de tener los archivos para ser considerados válidos.

Archivo ejemplo.csv:
```
comentarios
Este es el mejor analizador de sentimientos!!! 🎉
"Gracias a AluraLatam, Oracle, a los patrocinadores y a todo el equipo de organización por esta oportunidad 😍❤️ "
"La primavera es la estación que más me desespera, esta alergia no me deja respirar."
```

Los comentarios pueden ser delimitados por comillas dobles o directamente por enters. Es importante mantener un comentario por renglón o se tomará como un solo comentario, siempre respetando el hecho de que están acomodados en una columna.

Se puedo borrar o modificar el contenido base del ejemplo.csv, lo importante es mantener y respetar el título de la columna (comentarios) y el formato. Solo se aceptan archivos .csv.

Asegúrese de que el idioma seleccionado coincida con el idioma en el que se escribieron los comentarios del archivo para su correcta clasificación.

![Batching](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Batching.gif?raw=true)

### Histórico

El histórico presenta todos los registros existentes en la base de datos. Adicionalmente, existe la posibilidad de eliminar los registros seleccionados. Tome en cuenta que es necesario seleccionar por lo menos un registro para habilitar el botón de eliminado.

>El eliminado es permanente, no es posible recuperar los registros eliminados.

![Histórico](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Historico.gif?raw=true)

### Estadísticas

En esta vista podemos ver las estadísticas generales de todos los análisis realizados. El primer gráfico representa las top 5 palabras que más se repiten según el sentimiento, idioma y periodo de tiempo. En caso de dejar el periodo de tiempo en blanco se tomarán todos los registros que existen en la base de datos. Por su parte, el segundo gráfico representa la cantidad de comentarios positivos y negativos de los que se tienen registro según el idioma y la fecha. Cabe resaltar que el filtro del sentimiento no afecta al gráfico.

Nótese que no se envía una nueva petición a menos que se pongan ambas fechas. En caso de colocar una fecha de inicio posterior a la fecha fin, internamente se invierten para evitar romper la API. En caso de que no existan registros en el periodo especificado se indicará y no se mostrará ningún gráfico.

![Estadísticas](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Estadisticas.gif?raw=true)

### Acerca de nosotros

Esta vista es para información adicional referente al proyecto así cómo información de los colaboradores que participaron en el desarrollo del mismo.

![Acerca](https://github.com/jhoandavidpll/Hackathon-Alura-ONE-SentimentalAPI-E47/blob/main/Frontend/img/Acerca.gif?raw=true)

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
