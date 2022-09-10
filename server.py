from flask import Flask, render_template, request,redirect
from flask_socketio import SocketIO, send
from time import sleep

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
temp = ""


@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)
    # send() function will emit a message vent by default

@app.route("/")
def loginPage():
    return render_template("login.html")

@socketio.on("login")
def login(user):
    global temp
    temp = user

@app.route("/chat", methods=['POST'])
def message():
    user = request.form['user']
    if user == "":
        return redirect("/")
    datae = {'name':user}
    return render_template("client.html",data=datae)


if __name__ == "__main__":
    app.run(debug=True)