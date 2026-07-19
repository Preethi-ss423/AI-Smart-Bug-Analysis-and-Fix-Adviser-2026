import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


class DuplicateAgent:

    def __init__(self):
        print("Loading Duplicate Detection Agent...")

        # Load embedding model
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

        # Load FAISS index
        self.faiss_index = faiss.read_index("faiss_index.index")

        # Load structured bug data
        with open("structured_bug_data.pkl", "rb") as f:
            self.bug_data = pickle.load(f)

        print("Duplicate Detection Agent Ready!")

    def find_similar_bugs(self, query_text, top_k=3):

        # Generate embedding for input query
        query_embedding = self.embedding_model.encode([query_text])

        # Search FAISS
        distances, indices = self.faiss_index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        results = []

        for idx in indices[0]:

            if 0 <= idx < len(self.bug_data):

                bug = self.bug_data[idx]

                results.append({
                    "bug_id": bug["bug_id"],
                    "product": bug["product"],
                    "component": bug["component"],
                    "title": bug["title"],
                    "description": bug["description"],
                    "severity": bug["severity"],
                    "resolution": bug["resolution"]
                })

        return results