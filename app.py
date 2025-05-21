from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Dental Chat API is live!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Placeholder response (هنبدله بجيميني بعدين)
    return jsonify({
        "reply": f"You said: {user_message}"
    })

if __name__ == "__main__":
    app.run(debug=True)
