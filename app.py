from flask import Flask, request

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
        return "Token inválido"

    if request.method == "POST":
        data = request.get_json()
        print("Mensagem recebida:", data)
        return "Evento recebido", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

