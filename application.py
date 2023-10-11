import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.run(debug=True)
MAX_MESSAGES = 5
CHANNELS = {}

@app.route("/")
def canales():
    return render_template("canales.html")

# SOCKETS
@socketio.on('connect')
def conecciones():
    return 'cliente conectado'