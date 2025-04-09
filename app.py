from flask import Flask, jsonify

# Criação do app Flask
app = Flask(__name__)

# Rota inicial
@app.route("/")
def home():
    return jsonify({"message": "Olá, bem-vindo ao meu app Flask no Render!"})

# Configuração para rodar no Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
