from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)
    # send() function will emit a message vent by default

@app.route("/chat")
def message():
    data = {'name':request.args['name']}
    return render_template("client.html",data=data)


if __name__ == "__main__":
    app.run(debug=True)