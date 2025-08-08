
This is the **backend** for MindWhisper, an AI-powered mental wellness chatbot using **Retrieval-Augmented Generation (RAG)**, **FAISS vector search**, and **Hugging Face Transformers**.

Built with **Flask** in Python, it serves as the API layer between the frontend and the AI model.

---

## 🧠 Tech Stack
- **Python 3.10+**
- **Flask** (API framework)
- **Flask-CORS** (Cross-Origin Resource Sharing)
- **FAISS** (Vector search engine)
- **Hugging Face Transformers** (Language model inference)

---

## 📂 Project Structure
mindwhisper-backend/
│── backend/ # (If present) Core backend files
│── rag/
│ ├── app.py # Main Flask app
│ ├── rag_engine.py # RAG logic (FAISS + model)
│ ├── data/ # Knowledge base / mock documents
│── requirements.txt

**RAG Workflow:-
User query comes from the frontend.

FAISS searches the knowledge base for relevant context.

Hugging Face model generates an emotionally supportive response.

Response is sent back to the frontend in real time.**

yaml
Copy code
