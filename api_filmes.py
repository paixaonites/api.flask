from flask import Flask, jsonify

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
 app.run(port=5001)