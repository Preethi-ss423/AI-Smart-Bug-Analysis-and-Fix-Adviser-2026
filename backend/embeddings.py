import pandas as pd
from sentence_transformers import SentenceTransformer
import pickle

# Load cleaned knowledge base
knowledge_base = pd.read_csv("../datasets/knowledge_base.csv")

# Convert each bug report into a text chunk
chunks = []

for _, row in knowledge_base.iterrows():

    chunk = f"""
Bug ID: {row['bug_id']}
Product: {row['product_name']}
Component: {row['component_name']}

Title:
{row['short_description']}

Description:
{row['long_description']}

Severity:
{row['severity_category']}

Resolution:
{row['resolution_category']}
"""

    chunks.append(chunk.strip())

print("Loading embedding model...")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

# Generate embeddings
embeddings = model.encode(
    chunks,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Embeddings generated successfully!")

print("Total Chunks :", len(chunks))
print("Embedding Shape :", embeddings.shape)

# Save embeddings
with open("../datasets/embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("Embeddings saved as embeddings.pkl")