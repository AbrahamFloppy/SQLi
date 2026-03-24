import os
import psycopg2
from flask import Flask, request, render_template, redirect, url_for
from dotenv import load_dotenv
import bcrypt

load_dotenv()

app = Flask(__name__)

url_bd = os.getenv("DATABASE_URL")
conexion = psycopg2.connect(url_bd)
conexion.autocommit = True

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    nombre = request.form['username']
    clave = request.form['password']

    cursor = conexion.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (nombre,))
    resultado = cursor.fetchone()

    if resultado != None:
        contra_guardada = resultado[0]

        if type(contra_guardada) == str:
            contra_guardada = contra_guardada.encode()

        if bcrypt.checkpw(clave.encode(), contra_guardada):
            return redirect(url_for('bienvenida', usuario=nombre))

    return "credenciales incorrectas"

@app.route('/bienvenida/<usuario>')
def bienvenida(usuario):
    return render_template("success.html", usuario=usuario)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)