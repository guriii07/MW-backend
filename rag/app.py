import sys
print("Python sys.path:", sys.path)

from flask import Flask, request, jsonify
from flask_cors import CORS
from rag.rag_engine import RAGEngine




app = Flask(__name__)
CORS(app)

# ✅ Initialize RAG engine once when the app starts
rag_engine = RAGEngine()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "Missing query"}), 400

    try:
        # ✅ Generate response using RAG + GPT-2
        response = rag_engine.generate_answer(query)
        return jsonify({"answer": response})
    except Exception as e:
        print("❌ Error during generation:", e)
        return jsonify({"answer": "Sorry, something went wrong."}), 500

if __name__ == "__main__":
    app.run(port=5001, debug=True)
