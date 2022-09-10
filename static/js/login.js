const socket = io();
function submit() {
    console.log("RANNNNNNN")
    socket.emit("login",document.getElementById("uinp").value)
    
}