from flask import Flask, request, render_template, redirect, url_for
import json
import os

app = Flask(__name__)

# Carregar os dados do JSON
with open('user_data.json', 'r') as file:
    users = json.load(file)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Verificar as credenciais no formato atual do JSON
    if username in users and users[username]['password'] == password:
        dashboard_html = users[username]['dashboard']
        return render_template('dashboard.html', dashboard_html=dashboard_html)
    else:
        return render_template('login.html', error="Credenciais inválidas!")

if __name__ == '__main__':
    # Ajuste para funcionar no Render ou localmente
    port = int(os.environ.get("PORT", 5000))  # Porta padrão do Render é 10000
    app.run(host="0.0.0.0", port=port)
