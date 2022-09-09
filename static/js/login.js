const socket = io();
function submit() {
    socket.emit("login",document.getElementById("uinp").value,document.getElementById("pinp").value)
    
}