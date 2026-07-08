import pandas as pd
import pickle

# Load Mozilla dataset
df = pd.read_csv("../datasets/mozilla/mozilla_bug_report_data.csv")
structured_bugs = []

for _, row in df.iterrows():

    bug = {
        "bug_id": str(row["bug_id"]),
        "product": str(row["product_name"]),
        "component": str(row["component_name"]),
        "title": str(row["short_description"]),
        "description": str(row["long_description"]),
        "severity": str(row["severity_category"]),
        "resolution": str(row["resolution_category"])
    }

    # Text used ONLY for embedding
    bug["embedding_text"] = (
        bug["title"] + " " +
        bug["description"] + " " +
        bug["product"] + " " +
        bug["component"]
    )

    structured_bugs.append(bug)

# Save structured data
with open("structured_bug_data.pkl", "wb") as f:
    pickle.dump(structured_bugs, f)

print("✅ Structured dataset created successfully!")
print("Total Bug Reports:", len(structured_bugs))