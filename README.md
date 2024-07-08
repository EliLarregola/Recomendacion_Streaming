# SISTEMA DE RECOMENDACIÓN DE PELICULAS - MACHINE LEARNING OPERATIONS

## Descripción del proyecto
En este proyecto se busca desarrollar una API para consultas con un sistema de recomendación de películas utilizando datos de plataformas de Streaming proporcionados por Henry. La API proporciona varios endpoints que permiten consultar información entre otras acerca de películas, directores y actores, pero lo más importante es la implementación de un sistema de recomendación de películas a través de un modelo de Machine Learning.

## Rol a desarrollar y desafíos iniciales
En un primer momento se asume el rol de **Data Engineer** con el objetivo de crear un MVP (*Minimum Viable Product*) desde cero. En primer lugar, llevar a cabo un proceso de ETL (*Extract, Transform, Load*) para realizar las transformaciones necesarias en el dataset para poder acceder a la información precisa de manera fácil y eficiente. Como por ejemplo desanidar datos en diversas columnas y una serie de transformaciones propuestas:

•	Algunos campos, como **belongs_to_collection**, **production_companies** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila. La propuesta es desanidar los datos e incluir los necesarios en el dataset.

•	Los valores nulos de los campos **revenue**, **budget** deben ser rellenados por el número 0.

•	Los valores nulos del campo **release_date** deben eliminarse.

•	De haber fechas, deberán tener el formato **AAAA-mm-dd**, además deberán crear la columna **release_year** donde extraerán el año de la fecha de estreno.

•	Crear la columna con el retorno de inversión, llamada **return** con los campos **revenue** y **budget**, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

•	Eliminar las columnas que no serán utilizadas, **video**, **imdb_id**, **adult**, **original_title**, **poster_path** y **homepage**.

Por otro lado, se asume el rol de Data Scientist en una hipotética *start-up* que provee servicios de agregación de plataformas de *streaming*. Esto implica principalmente realizar un Análisis Exploratorio de los Datos (**EDA**), lo cual es indispensable para la creación de un modelo de *Machine Learning* que soluciona un problema de negocio: un sistema de recomendación de películas.

## Tecnologías utilizadas
Se utilizó Visual Studio Code, Jupyter Notebook y Python con las siguientes librerías:

•	Pandas

•	Numpy

•	Scikit-Learn

•	FastAPI

•	Matplotlib

•	Seaborn

•	Uvicorn

•	Wordcloud

•	SciPy.stats

•	Re

•	Ast

