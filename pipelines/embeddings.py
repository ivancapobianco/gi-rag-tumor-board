import json
import pandas as pd
import os
from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# -------------------------------
# 1. Load embedding model
# -------------------------------
embed_model = Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-m3"
)
print("Embedding model loaded!")

# -------------------------------
# 2. Load guidelines JSON
# -------------------------------
def load_guidelines_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# -------------------------------
# 3. Load patient TXT
# -------------------------------
def load_patient_txt(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# -------------------------------
# 4. Embed documents
# -------------------------------
def embed_documents(documents: list):
    docs = [Document(text=d) for d in documents]
    embeddings = [embed_model.get_text_embedding(doc.text) for doc in docs]
    return docs, embeddings

# -------------------------------
# 5. Save embeddings to JSON
# -------------------------------
def save_embeddings(output_path, docs, embeddings):
    saved = []
    for doc, emb in zip(docs, embeddings):
        saved.append({"text": doc.text, "embedding": emb})
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(saved, f, ensure_ascii=False, indent=2)
    print(f"Saved embeddings to {output_path}")

# -------------------------------
# 6. Main pipeline
# -------------------------------
if __name__ == "__main__":
    # Corpora JSON
    corpora_json_path = "./data/dummy_guidelines.json"
    corpora_data = load_guidelines_json(corpora_json_path)
    corpora_chunks = [chunk["text"] for chunk in corpora_data]

    docs, embeddings = embed_documents(corpora_chunks)
    save_embeddings("./data/corpora_embeddings.json", docs, embeddings)

    # Patient dummy TXT
    patient_txt_path = "./data/dummy_patient.txt"
    patient_text = load_patient_txt(patient_txt_path)
    patient_docs, patient_embeddings = embed_documents([patient_text])
    save_embeddings("./data/patient_embeddings.json", patient_docs, patient_embeddings)
