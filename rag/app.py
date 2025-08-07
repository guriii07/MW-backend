from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ Allows frontend to access from other ports

# Load GPT-2 using pipeline
generator = pipeline("text-generation", model="gpt2")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    try:
        result = generator(query, max_length=100, num_return_sequences=1, do_sample=True)
        response = result[0]["generated_text"]
        return jsonify({"answer": response})
    except Exception as e:
        print("❌ Error during generation:", e)
        return jsonify({"answer": "Sorry, something went wrong."}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
CORS(app)
