import faiss
import numpy as np

print("Loading embeddings...")

# Load embeddings
embeddings = np.load("embeddings.npy").astype("float32")

print("Embeddings Shape:", embeddings.shape)

# Get embedding dimension
dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

print("Adding vectors to FAISS...")

# Add embeddings
index.add(embeddings)

# Save index
faiss.write_index(index, "faiss_index.index")

print("\n✅ FAISS Index Created Successfully!")
print("Total Vectors:", index.ntotal)