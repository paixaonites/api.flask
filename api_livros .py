from flask import Flask, jsonify

app = Flask(__name__)

livros = [
    {"id": 1, "nome": "O Pequeno Príncipe"},
    {"id": 2, "nome": "O Menino Verde"},
    {"id": 3, "nome": "Dom Casmurro"}
]

@app.route("/livros", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse/livros"})

@app.route("/livros", methods=["GET"])
def livros(): 
    return jsonify (livros)

if __name__ == "__main__":
 app.run(port=5001)