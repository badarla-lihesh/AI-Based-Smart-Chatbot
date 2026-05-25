from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__) 

# Load intents (DO NOT CHANGE FILE)
with open("intents.json", "r") as file:
    data = json.load(file)


def get_response(user_input):
    user_input = user_input.lower() 

    best_intent = None
    best_score = 0

    for intent_name in data:
        keywords = data[intent_name]["keywords"]

        for word in keywords:

            # EXACT MATCH (highest priority)
            if word == user_input:
                return random.choice(data[intent_name]["responses"])

            # SAFE MATCH: only whole-word match
            if word in user_input.split():
                if len(word) > best_score:
                    best_score = len(word)
                    best_intent = intent_name

    if best_intent:
        return random.choice(data[best_intent]["responses"])

    return "Sorry, I did not understand."
    
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    msg = request.json["message"]
    reply = get_response(msg)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)