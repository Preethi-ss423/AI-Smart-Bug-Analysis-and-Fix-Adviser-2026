import pandas as pd

# Load datasets
mozilla_df = pd.read_csv("../datasets/mozilla/mozilla_bug_report_data.csv")
eclipse_df = pd.read_csv("../datasets/eclipse/eclipse_bug_report_data.csv")

# Keep only useful columns
columns_to_keep = [
    "bug_id",
    "product_name",
    "component_name",
    "short_description",
    "long_description",
    "severity_category",
    "resolution_category"
]

mozilla_clean = mozilla_df[columns_to_keep]
eclipse_clean = eclipse_df[columns_to_keep]

# Remove rows with missing title or description
mozilla_clean = mozilla_clean.dropna(
    subset=["short_description", "long_description"]
)

eclipse_clean = eclipse_clean.dropna(
    subset=["short_description", "long_description"]
)

# Merge both datasets
knowledge_base = pd.concat(
    [mozilla_clean, eclipse_clean],
    ignore_index=True
)

# Remove duplicate bug reports
knowledge_base = knowledge_base.drop_duplicates()

# Save cleaned dataset
knowledge_base.to_csv(
    "../datasets/knowledge_base.csv",
    index=False
)

print("Knowledge Base Created Successfully!")
print("Total Bug Reports:", len(knowledge_base))

print("\nSample Data:\n")
print(knowledge_base.head())