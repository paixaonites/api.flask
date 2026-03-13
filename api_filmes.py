from flask import Flask, jsonify
import os

app = Flask(__name__)

filmes = [
    {"id": 1, "nome": "Vingadores"},
    {"id": 2, "nome": "Como Eu era Antes De Voce"},
    {"id": 3, "nome": "Minions"}
]

@app.route("/filmes", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de filmes - Acesse/filmes"})

@app.route("/filmes", methods=["GET"])
def listar_filmes(): 
    return jsonify (filmes)

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host="0.0.0.0", port=port)