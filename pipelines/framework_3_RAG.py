"""
Run a CUSTOM RAG pipeline using:
- Embedding of the patient case
- Precomputed dummy guideline embeddings (JSON)
- Local similarity search
- Prompt-based RAG inference via ChatCompletion

IMPORTANT:
- Guideline embeddings are fully synthetic and for demonstration only
- No copyrighted guideline text is included
"""

import os
import sys
import json
import numpy as np

# ------------------------------------------------------------------
# Path setup: allow imports from parallel folders
# ------------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))

prompts_dir = os.path.abspath(os.path.join(current_dir, '..', 'prompts'))
processing_dir = os.path.abspath(os.path.join(current_dir, '..', 'processing'))

sys.path.append(prompts_dir)
sys.path.append(processing_dir)

# ------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------
from prompts_templates import get_prompt_for_configuration
from chatgpt import chatgpt_chat_completion
from embedding import embed_text

# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------
MODEL_NAME = "gpt-4o-mini"
TOP_K = 5

CASE_PATH = os.path.abspath(
    os.path.join(current_dir, '..', 'data', 'dummy_patients', 'example_case_de.txt')
)

CORPORA_PATH = os.path.abspath(
    os.path.join(current_dir, '..', 'data', 'dummy_corpora', 'dummy_guidelines_with_embeddings.json')
)

# ------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------
def load_case_text(path: str) -> str:
    """Load patient case text from file."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()


def load_guideline_corpora(path: str) -> list[dict]:
    """Load guideline chunks with embeddings from JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def dot_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """Compute dot product similarity between two vectors."""
    return float(np.dot(vec1, vec2))


def retrieve_top_k_chunks(
    query_embedding: np.ndarray,
    corpora: list[dict],
    top_k: int = 5
) -> list[dict]:
    """
    Retrieve top-k guideline chunks by embedding similarity.
    """
    scored_chunks = []

    for chunk in corpora:
        chunk_embedding = np.array(chunk["embedding"], dtype=float)
        score = dot_similarity(chunk_embedding, query_embedding)

        scored_chunks.append({
            "chunk_id": chunk.get("chunk_id"),
            "source": chunk.get("source"),
            "text": chunk.get("text"),
            "score": score
        })

    scored_chunks.sort(key=lambda x: x["score"], reverse=True)
    return scored_chunks[:top_k]

# ------------------------------------------------------------------
# Main pipeline
# ------------------------------------------------------------------
if __name__ == "__main__":

    print("Running local RAG pipeline with dummy guideline embeddings\n")

    # --------------------------------------------------------------
    # Step 1: Load patient case
    # --------------------------------------------------------------
    case_text = load_case_text(CASE_PATH)

    # --------------------------------------------------------------
    # Step 2: Embed patient case (on the run)
    # --------------------------------------------------------------
    query_embedding = np.array(embed_text(case_text), dtype=float)

    # --------------------------------------------------------------
    # Step 3: Load guideline corpora with embeddings
    # --------------------------------------------------------------
    corpora = load_guideline_corpora(CORPORA_PATH)

    # --------------------------------------------------------------
    # Step 4: Retrieve top-k guideline chunks
    # --------------------------------------------------------------
    retrieved_chunks = retrieve_top_k_chunks(
        query_embedding=query_embedding,
        corpora=corpora,
        top_k=TOP_K
    )

    # --------------------------------------------------------------
    # Step 5: Build RAG prompt
    # --------------------------------------------------------------
    prompt = get_prompt_for_configuration(
        case_text=case_text,
        config_type="rag_full",
        retrieved_chunks=retrieved_chunks
    )

    # --------------------------------------------------------------
    # Step 6: Run ChatCompletion
    # --------------------------------------------------------------
    response = chatgpt_chat_completion(prompt, model=MODEL_NAME)

    # --------------------------------------------------------------
    # Output
    # --------------------------------------------------------------
    print("=== Patient Case ===")
    print(case_text)

    print("\n=== Retrieved Guideline Chunks ===")
    for chunk in retrieved_chunks:
        print(f"- Chunk {chunk['chunk_id']} | Score: {chunk['score']:.4f}")

    print("\n=== RAG Output ===")
    print(response)

