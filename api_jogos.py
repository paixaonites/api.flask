from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "nome": "GTA"},
    {"id": 2, "nome": "Minecraft"},
    {"id": 3, "nome": "FIFA"}
]

@app.route("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de jogos - Acesse/jogos"})

@app.route("/jogos", methods=["GET"])
def listar_jogos(): 
    return jsonify (jogos)

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host="0.0.0.0", port=port)