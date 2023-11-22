import pandas as pd
from flask import Flask, jsonify

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')

app = Flask(__name__)


@app.route("/")
def index():
    return "Mostrando Sistema de Recomendaciones"


@app.route("/api")
def api():
    movie_dict = movies.to_dict(orient='records')
    return jsonify(movie_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
