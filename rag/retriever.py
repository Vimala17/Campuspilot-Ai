import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("rag/faiss_index.bin")

with open("rag/documents.pkl", "rb") as f:
    documents, sources = pickle.load(f)


def retrieve(query, k=2):
    embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype(np.float32)

    distances, indices = index.search(embedding, k)

    context = []
    selected_sources = []

    for idx in indices[0]:
        if idx != -1:
            context.append(documents[idx])
            selected_sources.append(sources[idx])

    return "\n\n".join(context), selected_sources