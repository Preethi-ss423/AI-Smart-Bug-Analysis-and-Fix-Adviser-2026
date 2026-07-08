import pandas as pd

# Load cleaned knowledge base
knowledge_base = pd.read_csv("../datasets/knowledge_base.csv")

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

print("\n========== SAMPLE CHUNKS ==========\n")

for i in range(3):
    print(f"\nChunk {i+1}\n")
    print(chunks[i])
    print("-" * 70)

print("\nTotal Chunks Created:", len(chunks))
import pickle

# Save chunks
with open("bug_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("\nChunks saved successfully as bug_chunks.pkl")