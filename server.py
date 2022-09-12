from flask import Flask, render_template, request,redirect
from flask_socketio import SocketIO, send, emit
from time import sleep

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
temp = ""
temp = []

@app.route("/")
def login():
    return render_template("login.html")

@socketio.on("connected")
def conn(user):
    print("connect")
    sids[request.sid] = user

players = {}
sids = {}
@app.route("/game", methods=['POST'])
def game():
    user = request.form['user']
    if user == "":
        return redirect("/")
    try:
        players[user]
        return redirect("/")
    except KeyError:
        pass
    datae = {'name':user}
    players[user] = [0,0]
    return render_template("game.html", data=datae)

def update():
    sendi = []
    for key in players:
        sendi.append(players[key])
    emit('update',sendi, broadcast=True)

@socketio.on("move")
def move(dir, name):
    if dir == "up":
        players[name][1] -= 5
    elif dir == "down":
        players[name][1] += 5
    elif dir == "left":
        players[name][0] -= 5
    else:
        players[name][0] += 5
    # list that will be sent to all of the clients
    update()

@socketio.on('disconnect')
def disconnect():
    print("del")
    name = sids[request.sid]
    try:
        del players[name]
        del sids[request.sid]
    except KeyError:
        print(sids)
    update()
    

if __name__ == "__main__":
    app.run(debug=True)