import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load structured bug data
with open("structured_bug_data.pkl", "rb") as f:
    bug_data = pickle.load(f)

print(f"Loaded {len(bug_data)} bug reports.")

# Get text for embedding
texts = [bug["embedding_text"] for bug in bug_data]

print("Generating embeddings...")

# Generate embeddings
embeddings = model.encode(
    texts,
    batch_size=32,
    show_progress_bar=True,
    convert_to_numpy=True
)

# Save embeddings
np.save("embeddings.npy", embeddings)

print("✅ Embeddings created successfully!")
print("Shape:", embeddings.shape)