import pandas as pd
from flask import Flask, jsonify

ratings = pd.read_csv('ratings.csv')
print(movies.head())

app = Flask(__name__)


@app.route("/")
def index():
    return "Mostrando Sistema de Recomendaciones"


@app.route("/api")
def api():
    rating_dict = ratings.to_dict(orient='records')
    return jsonify(rating_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
