from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Cargar el DataFrame desde el archivo Parquet
def load_data():
    return pd.read_parquet('streaming_functions.parquet')


@app.get("/")
def read_root():
    return {"Mensaje": "Welcome to the Movie API"}

read_root()

# Cantidad de filmaciones por mes

@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    df = load_data()
    # Convertir mes a número
    month_map = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
        "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    month_num = month_map.get(mes.lower())
    if month_num is None:
        return {"error": "Mes inválido"}
    count = df[df['release_date'].dt.month == month_num].shape[0]
    return {"mes": mes, "cantidad": count}


# Cantidad de filmaciones por día

@app.get("/cantidad_filmaciones_dia/{dia}")
def cantidad_filmaciones_dia(dia: str):
    df = load_data()
    # Convertir día a número
    day_map = {
        "lunes": 0, "martes": 1, "miércoles": 2, "jueves": 3, "viernes": 4, "sábado": 5, "domingo": 6
    }
    day_num = day_map.get(dia.lower())
    if day_num is None:
        return {"error": "Día inválido"}
    count = df[df['release_date'].dt.dayofweek == day_num].shape[0]
    return {"dia": dia, "cantidad": count}


# Puntaje según titulo

@app.get("/score_titulo/{titulo}")
def score_titulo(titulo: str):
    df = load_data()
    film = df[df['title'].str.lower() == titulo.lower()]
    if film.empty:
        return {"error": "Título no encontrado"}
    film_info = film.iloc[0]
    return {
        "titulo": film_info['title'],
        "año": film_info['release_year'],
        "score": film_info['vote_average']
    }

# Votos según título 

@app.get("/votos_titulo/{titulo}")
def votos_titulo(titulo: str):
    df = load_data()
    film = df[df['title'].str.lower() == titulo.lower()]
    if film.empty:
        return {"error": "Título no encontrado"}
    film_info = film.iloc[0]
    if film_info['vote_count'] < 2000:
        return {"mensaje": "La película no cumple con los requisitos mínimos de votos"}
    return {
        "titulo": film_info['title'],
        "año": film_info['release_year'],
        "votos": film_info['vote_count'],
        "promedio_votos": film_info['vote_average']
    }

# Obtener información de actores 

@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    df = load_data()
    films = df[df['actors'].apply(lambda lista_actores: nombre_actor in lista_actores)]
    if films.empty:
        return {"error": "Actor no encontrado"}
    total_ret = films['return'].sum()
    count_films = films.shape[0]
    avg_ret = total_ret / count_films
    return {
        "actor": nombre_actor,
        "cantidad_filmaciones": count_films,
        "retorno_total": total_ret,
        "retorno_promedio": avg_ret
    }

# Éxito del director

@app.get("/get_director/{nombre_director}")
def get_director(nombre_director: str):
    df = load_data()
    films = df[df['director'].str.contains(nombre_director, case=False, na=False)]
    if films.empty:
        return {"error": "Director no encontrado"}
    film_details = films[['title', 'release_date', 'return', 'budget', 'revenue']].to_dict(orient='records')
    return {
        "director": nombre_director,
        "peliculas": film_details
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

