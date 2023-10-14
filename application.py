import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

MAX_MESSAGES = 5
CHANNELS = {}
USUARIOS = {}

@app.route("/")
def canales():
    return render_template("canales.html")

# SOCKETS
@socketio.on("connect")
def conecciones():
    print("cliente conectado")

@socketio.on("ingreso_usuario")
def usuarios(usuarios):
    print(f'Usuario ingresado: {usuarios}')
    USUARIOS[usuarios] = request.sid

@socketio.on("nuevo_mensaje")
def mensajes(mensajes):
    print(f"mensaje {mensajes}")
    usuarios = None
    for usuario in USUARIOS:
        if(USUARIOS[usuario] == request.sid):
            usuarios = usuario
    emit("chat", {"mensajes": mensajes, "usuario": usuarios} , broadcast = True)