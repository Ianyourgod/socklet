const socket = io();
var canvas = document.getElementById("canv");
var ctx = canvas.getContext("2d");
canvas.width  = window.innerWidth;
canvas.height = window.innerHeight;
socket.on("update", (li) => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    li.forEach(function(item) {
        ctx.fillStyle = "#eb4034";
        ctx.fillRect(item[0], item[1], 20, 20);
    })
})
socket.on("disconnect", () => {
    emit("diconnect", datae['name'])
})
document.addEventListener("keydown", (event) => {
    if (event.isComposing || event.keyCode === 229) {
      return;
    }
    if (event.key === "w") {
        socket.emit("move",  "up", dato['name'])
    }
    if (event.key === "s") {
        socket.emit("move","down", dato['name'])
    }
    if (event.key === "a") {
        socket.emit("move","left", dato['name'])
    }
    if (event.key === "d") {
        socket.emit("move","right",dato['name'])
    }
})
window.addEventListener('beforeunload', function (e) {
    socket.emit("discon", dato['name'])
    e.preventDefault();
    e.returnValue = '';
})