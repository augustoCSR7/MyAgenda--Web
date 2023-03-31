from flask import Flask, render_template, request, flash, redirect
import json
import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE user (nome text, username text not null unique, password text)")

cursor.execute("INSERT INTO user VALUES('Augusto César', 'augustocadasr', 'dada323')")

banco.commit()

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())

app = Flask(__name__)
app.secret_key = "dkjhdhfbshjfb64f38fj dhfbgdgu8"

@app.route('/')
def home():
	return render_template('login.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	nome = request.form.get('username')
	senha = request.form.get('senha')

	with open('usuarios.json') as usuariosTemp:
		usuarios = json.load(usuariosTemp)
		cont = 0
		for usuario in usuarios:
			cont += 1
			if usuario['nome'] == nome and usuario['senha'] == senha:
				return render_template ("index.html")
			
			if cont >= len(usuarios):
				return redirect ('/')


@app.route("/cadastro.html")
def cadastro():
	return render_template("cadastro.html")

@app.route("/app")
def index():
	flash("Nenhum lembrete criado")
	return render_template("index.html")

@app.route("/lembrete", methods=['POST', 'GET'])
def greeter():
	flash("Lembrete: " + str(request.form['title_input']) + " às " + str(request.form['time_input']) + ", " + str(request.form['date_input']) + " criado com sucesso!")
	return render_template("index.html")

if __name__ in "__main__":
	app.run(debug=True)