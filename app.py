from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "dkjhdhfbshjfb64f38fj dhfbgdgu8"

@app.route("/")
def home():
	return render_template("login.html")

@app.route("/login.html")
def login():
	return render_template("login.html")

@app.route("/cadastro.html")
def cadastro():
	return render_template("cadastro.html")

@app.route("/app")
def index():
	flash("Nenhum lembrete criado")
	return render_template("index.html")

@app.route("/lembrete", methods=['POST', 'GET'])
def greeter():
	flash("Lembrete na data: " + str(request.form['time_input']) + ", " + str(request.form['date_input']) + " criado com sucesso!")
	return render_template("index.html")