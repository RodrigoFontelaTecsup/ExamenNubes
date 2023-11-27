import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import redis
import json
import os

app = Flask(__name__)
CORS(app)

movies = pd.read_csv('movies.csv')

# Conectar a Redis
redis_conn = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

# Clave para almacenar en Redis
REDIS_KEY = "movies_data"


def get_movies_from_redis():
    # Intentar obtener datos desde Redis
    cached_data = redis_conn.get(REDIS_KEY)

    if cached_data:
        # Si los datos están en caché, decodificar y devolver
        return json.loads(cached_data.decode('utf-8'))
    else:
        # Si no hay datos en caché, calcular y almacenar en Redis
        movies_data = movies.sort_values(
            by="title", ascending=False).to_dict(orient='records')
        redis_conn.set(REDIS_KEY, json.dumps(movies_data))
        return movies_data


@app.route('/api/movies')
def movie_api():
    # Obtener datos desde Redis o calcular si no está en caché
    pelicula = get_movies_from_redis()
    return jsonify(pelicula)


@app.route('/api/movies/<int:num_movies>')
def get_n_movies(num_movies):
    pelicula = movies.sort_values(by="title", ascending=False).head(num_movies)
    return jsonify(pelicula.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
