const socket = io();
function submit() {
    socket.emit("login",document.getElementById("uinp").value)
    
}