from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# La clé API est lue depuis les variables d'environnement (configurées sur Render)
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/api/rag/chat', methods=['POST', 'GET'])
def rag_chat():
    try:
        if request.method == 'GET':
            message = request.args.get('message', 'Test GET')
        else:
            if request.is_json:
                data = request.get_json()
            else:
                data = request.form.to_dict()
            message = data.get('message', 'Test POST')

        print(f"Message reçu: '{message}'")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=100
        )

        content = response.choices[0].message.content
        return jsonify({"content": content, "status": "success"})
    except Exception as e:
        print(f"Erreur: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)
