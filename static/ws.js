console.log("ws.js loaded ✅");
var ws = new WebSocket("wss://ominous-system-j6xgq9vq65vhqg6r-8000.app.github.dev/ws");
ws.onmessage = function(event) {
   var messages = document.getElementById('messages')
   var message = document.createElement('li')
   var content = document.createTextNode(event.data)
   message.appendChild(content)
   messages.appendChild(message)
};
function sendMessage(event) {
   var input = document.getElementById("messageText")
   ws.send(input.value)
   input.value = ''
   event.preventDefault()
}