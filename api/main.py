import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import redis
import json
import os

app = Flask(__name__)

movies = pd.read_csv('movies.csv')

redis_conn = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


@app.route('/api/movies')
def movie_api():
    pelicula = movies.sort_values(by="title", ascending=False)
    return jsonify(pelicula.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
