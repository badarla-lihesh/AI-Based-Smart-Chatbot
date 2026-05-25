document.addEventListener("DOMContentLoaded", function () {

    console.log("SCRIPT LOADED ✔");

    const inputBox = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const sendBtn = document.getElementById("sendBtn");

    sendBtn.addEventListener("click", function () {

        console.log("BUTTON CLICKED ✔");

        let message = inputBox.value;
        console.log("MESSAGE:", message);

        chatBox.innerHTML += "<div>You: " + message + "</div>";

        fetch("/get", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        })
        .then(res => res.json())
        .then(data => {
            console.log("BOT RESPONSE:", data);
            chatBox.innerHTML += "<div>Bot: " + data.reply + "</div>";
        });

        inputBox.value = "";
    });

});