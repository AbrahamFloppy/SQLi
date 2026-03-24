import os
import psycopg2
from flask import Flask, request, render_template
from dotenv import load_dotenv
import bcrypt

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL)
conn.autocommit = True

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        if bcrypt.checkpw(password.encode(), result[0].encode()):
            return "login correcto"

    return "credenciales incorrectas"

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    cursor = conn.cursor()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, hashed)
    )

    return "usuario registrado"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))