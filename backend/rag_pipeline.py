import faiss
import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load knowledge base
knowledge_base = pd.read_csv("../datasets/knowledge_base.csv")

# Load FAISS index
index = faiss.read_index("../datasets/faiss_index.index")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("RAG Pipeline Ready!")

while True:

    query = input("\nEnter Bug Description (or type exit): ")

    if query.lower() == "exit":
        break

    # Convert query to embedding
    query_embedding = model.encode([query])

    # Search top 5 similar bugs
    distances, indices = index.search(query_embedding, 5)

    print("\n========== TOP 5 SIMILAR BUGS ==========\n")

    for i in indices[0]:

        bug = knowledge_base.iloc[i]

        print("Bug ID:", bug["bug_id"])
        print("Title:", bug["short_description"])
        print("Severity:", bug["severity_category"])
        print("Resolution:", bug["resolution_category"])
        print("-" * 60)