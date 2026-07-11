import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
sources = []

# Knowledge Base Folder
kb_folder = "knowledge_base"

print("Loading Knowledge Base...")

for file in os.listdir(kb_folder):

    if file.endswith(".txt"):

        path = os.path.join(kb_folder, file)

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

            # Split into paragraphs
            chunks = text.split("\n\n")

            for chunk in chunks:

                chunk = chunk.strip()

                if len(chunk) > 20:

                    documents.append(chunk)

                    sources.append(file)

print(f"Loaded {len(documents)} chunks")

# Generate embeddings
print("Generating Embeddings...")

embeddings = model.encode(
    documents,
    convert_to_numpy=True,
    normalize_embeddings=True
)

embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

# Save Index
faiss.write_index(index, "rag/faiss_index.bin")

# Save Documents
with open("rag/documents.pkl", "wb") as f:

    pickle.dump((documents, sources), f)

print("===================================")
print("✅ FAISS Index Created Successfully!")
print("===================================")
print(f"Documents : {len(documents)}")
print(f"Dimension : {dimension}")