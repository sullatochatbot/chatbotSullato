from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Chatbot Sullato online com Flask!"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == "sullatotoken123":
            return challenge
        return "Token inválido", 403

    if request.method == "POST":
        data = request.get_json()
        print("Mensagem recebida:", json.dumps(data, indent=2))

        # Verifica se há uma mensagem de texto
        if data.get("entry"):
            for entry in data["entry"]:
                if entry.get("changes"):
                    for change in entry["changes"]:
                        value = change.get("value")
                        messages = value.get("messages")
                        if messages:
                            for message in messages:
                                sender_id = message["from"]
                                text = message["text"]["body"]
                                print(f"Mensagem de {sender_id}: {text}")
        return "Evento recebido", 200
