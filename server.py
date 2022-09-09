from flask import Flask, render_template, request,redirect
from flask_socketio import SocketIO, send

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

@socketio.on("sign")
def signin(name,pswd):
    with open("users/"+name,"w") as f:
        f.write(name+"\n"+pswd)

@socketio.on("login")
def login(name,pswd):
    global temp
    try:
        with open("users/"+name,"r") as f:
            txt = f.read()
    except (FileNotFoundError, TypeError):
        return
    ps = ""
    for i in txt:
        ps += i
    if ps == pswd:
        temp = name
        print("redir")
        return "redir"

@app.route("/chat")
def message():
    if temp != "":
        datae = {'name':temp}
        temp = ""
    else:
        return redirect("/")
    return render_template("client.html",data=datae)


if __name__ == "__main__":
    app.run(debug=True)