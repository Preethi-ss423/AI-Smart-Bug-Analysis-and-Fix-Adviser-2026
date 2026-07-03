# Technology Stack

## Overview

The AI Smart Bug Analysis and Fix Adviser project uses web technologies, Python, and AI frameworks to analyze software bugs and recommend possible fixes.

---

## Frontend

### HTML
Used to create the structure of the web pages.

### CSS
Used to design the user interface and improve the appearance of the application.

### JavaScript
Used to add interactivity such as file upload, form validation, and communication with the backend.

---

## Backend

### Python
Used as the main programming language because it has strong support for Artificial Intelligence and Machine Learning libraries.

### Flask
Used to build REST APIs and connect the frontend with AI modules.

---

## Artificial Intelligence

### LangChain
Used to build the RAG pipeline and coordinate the interaction between the language model and the knowledge base.

### Sentence Transformers
Used to convert bug reports into vector embeddings for semantic similarity search.

### FAISS
Used as the vector database to store embeddings and retrieve similar historical bug reports efficiently.

---

## Knowledge Base

Public bug datasets from Mozilla, Apache, and Eclipse will be used to build the historical defect knowledge base.

---

## Version Control

### Git
Used to track project changes.

### GitHub
Used to store the project repository and enable collaboration.

---

## Why This Tech Stack?

- HTML, CSS, and JavaScript provide a simple and responsive user interface.
- Python and Flask make backend development straightforward and integrate well with AI libraries.
- LangChain simplifies the implementation of Retrieval-Augmented Generation (RAG).
- Sentence Transformers generate meaningful embeddings for bug reports.
- FAISS performs fast semantic similarity search on large collections of historical bugs.
- Git and GitHub help manage the project efficiently.