# pipeline/embedding.py
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
# 2. Function to embed patient text on the fly
# -------------------------------
def embed_patient_text(patient_txt_path: str):
    with open(patient_txt_path, "r", encoding="utf-8") as f:
        text = f.read()
    embedding = embed_model.get_text_embedding(text)
    return embedding

# -------------------------------
# 3. Example usage
# -------------------------------
if __name__ == "__main__":
    txt_path = "./data/dummy_patient.txt"
    embedding = embed_patient_text(txt_path)
    print(f"Patient embedding (first 10 values): {embedding[:10]}")
