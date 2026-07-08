import faiss
import pickle

# Load embeddings
with open("../datasets/embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

print("Embeddings Loaded Successfully!")
print("Shape:", embeddings.shape)

# Get embedding dimension
dimension = embeddings.shape[1]

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Add embeddings to index
index.add(embeddings)

print("FAISS Index Created Successfully!")
print("Total Vectors:", index.ntotal)

# Save FAISS index
faiss.write_index(index, "../datasets/faiss_index.index")

print("FAISS Index Saved Successfully!")