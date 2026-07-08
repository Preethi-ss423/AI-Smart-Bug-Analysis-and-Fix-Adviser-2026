from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------------- APP SETUP ----------------
app = Flask(__name__, static_folder="../frontend")
CORS(app)

# ---------------- LOAD MODEL ----------------
print("⏳ Loading AI model...")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- LOAD FAISS INDEX ----------------
faiss_index = faiss.read_index("faiss_index.index")

# ---------------- LOAD BUG DATA ----------------
with open("structured_bug_data.pkl", "rb") as f:
    bug_data = pickle.load(f)

print("✅ All models loaded successfully!")

# ---------------- UPLOAD FOLDER ----------------
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- FRONTEND ROUTE ----------------
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/test")
def test():
    return "Backend working"

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

# ---------------- MAIN API ----------------
@app.route("/analyze_bug", methods=["POST"])
def analyze_bug():

    data = request.get_json()

    title = data.get("title", "")
    description = data.get("description", "")
    stack_trace = data.get("stack_trace", "")

    uploaded_file = None
    file_name = None

    file_name = None
    if uploaded_file and uploaded_file.filename != "":
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)
        file_name = uploaded_file.filename

    # ✅ FIXED LINE
    query_text = f"{title} {description} {stack_trace}"

    if query_text.strip() == "":
        return jsonify({"error": "No bug input provided"}), 400

    # embedding
    query_embedding = embedding_model.encode([query_text])

    # FAISS search
    k = 3
    distances, indices = faiss_index.search(
        np.array(query_embedding).astype("float32"), k
    )

    results = []

    for idx in indices[0]:

             if 0 <= idx < len(bug_data):

                bug = bug_data[idx]

                results.append({
                        "bug_id": bug["bug_id"],
                        "product": bug["product"],
                        "component": bug["component"],
                        "title": bug["title"],
                        "description": bug["description"],
                        "severity": bug["severity"],
                        "resolution": bug["resolution"]
        })

    return jsonify({
        "query": {
            "title": title,
            "description": description,
            "stack_trace": stack_trace
        },
        "top_matches": results,
        "uploaded_file": file_name
    })

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)