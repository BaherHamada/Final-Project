import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

from flask import Flask, request, jsonify
import vertexai
from vertexai.generative_models import GenerativeModel

# إعداد GCP
vertexai.init(project="final-chat-460420", location="us-central1")

# تحميل موديل Gemini
model = GenerativeModel("gemini-2.5-flash-preview-05-20")

# إعداد Flask
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    response = model.generate_content(user_message)

    return jsonify({
        "response": response.text
    })

if __name__ == '__main__':
    app.run(debug=True)
