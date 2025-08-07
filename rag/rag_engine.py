import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path
from transformers import pipeline


class RAGEngine:
    def __init__(self, docs_folder=None, model_name="all-MiniLM-L6-v2"):
        if docs_folder is None:
            current_dir = Path(__file__).parent
            docs_folder = current_dir / "mock_docs"

        self.model = SentenceTransformer(model_name)
        self.docs_folder = docs_folder
        self.documents = []
        self.doc_texts = []
        self.index = None
        self.generator = pipeline("text-generation", model="gpt2", max_new_tokens=60, temperature=0.7, top_p=0.95)

        


        self.load_documents()
        self.create_index()

    def load_documents(self):
        docs_path = Path(self.docs_folder).resolve()
        print("🔍 Looking in folder:", docs_path)

        txt_files = list(docs_path.glob("*.txt"))
        print("📄 Found files:", [str(f) for f in txt_files])

        for file in txt_files:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                print(f"✅ Loading {file.name} with {len(content)} characters")
                if content:
                    self.documents.append((file.name, content))
                    self.doc_texts.append(content)

    def create_index(self):
        embeddings = self.model.encode(self.doc_texts)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(np.array(embeddings))

    def retrieve_context(self, query, top_k=2):
        query_embedding = self.model.encode([query])
        D, I = self.index.search(np.array(query_embedding), top_k)
        return [self.doc_texts[i] for i in I[0]]

    def generate_answer(self, query):
        context_docs = self.retrieve_context(query)
        context = "\n\n".join(context_docs)

        prompt = f"""You are MindWhisper, a kind, emotionally intelligent, and understanding AI friend.

You speak like a gentle listener who wants the user to feel heard and supported. Your answers should be warm, non-judgmental, and emotionally comforting.

User: {query}

Some things you remember that might help:
{context}

MindWhisper:"""

        result = self.generator(prompt, max_length=200, do_sample=True, temperature=0.7)[0]['generated_text']
        return result.split("MindWhisper:")[-1].strip()
