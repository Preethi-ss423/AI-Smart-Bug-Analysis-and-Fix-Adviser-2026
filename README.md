# 🤖 AI Smart Bug Analysis and Fix Adviser

## 📌 Project Overview

AI Smart Bug Analysis and Fix Adviser is an AI-powered web application that assists developers in analyzing software defects efficiently. The system accepts bug reports, descriptions, stack traces, and log files, performs intelligent bug triaging, analyzes stack traces, retrieves similar historical bugs using semantic search (FAISS), identifies possible root causes, and recommends appropriate fixes.

The project follows a **Multi-Agent AI Architecture**, where specialized agents collaborate to analyze software bugs and generate a structured AI bug analysis report.

---

# 🚀 Problem Statement

Software developers spend significant time manually analyzing bug reports, searching historical issues, identifying root causes, and recommending fixes. This process increases software maintenance time and debugging effort.

This project aims to automate software bug analysis using Artificial Intelligence, semantic search, Retrieval-Augmented Generation (RAG), and a Multi-Agent System.

---

# 🎯 Objectives

- Accept bug reports, descriptions, stack traces, and log files.
- Automatically classify bug severity and priority.
- Identify the affected software component.
- Analyze stack traces to detect failure points.
- Retrieve similar historical bugs using semantic search.
- Detect duplicate bug reports.
- Identify possible root causes.
- Recommend suitable fixes.
- Generate a structured AI bug analysis report.

---

# ✨ Features Implemented (Milestone 2)

## ✅ Bug Submission Module

- Submit Bug Title
- Bug Description
- Stack Trace
- Log File Upload

---

## ✅ Triage Agent

The Triage Agent automatically predicts:

- Bug Category
- Severity (Critical / High / Medium / Low)
- Priority (P1 / P2 / P3 / P4)
- Affected Module
- Confidence Score
- Reasoning for Prediction

---

## ✅ Log Analysis Agent

The Log Analysis Agent extracts:

- Programming Language
- Exception Type
- Source File
- Method Name
- Line Number
- Failure Point
- Affected Code Path
- Error Type
- Stack Depth

---

## ✅ Duplicate Detection

- Semantic Similarity Search using FAISS
- Retrieves similar historical bug reports
- Displays relevant bug information

---

## ✅ Root Cause Analysis

Identifies:

- Possible root cause
- Impact of the bug

---

## ✅ Remediation Agent

Provides:

- Recommended fixes
- Best practices
- Overall recommendation

---

## ✅ AI Bug Analysis Report

The generated report includes:

- Submitted Bug
- Triage Analysis
- Log Analysis
- Similar Historical Bugs
- Root Cause Analysis
- Recommended Fixes
- Overall Recommendation

---

# 🏗️ System Architecture

```
                    Bug Submission
                           │
                           ▼
                   Triage Agent
                           │
                           ▼
                 Log Analysis Agent
                           │
                           ▼
                 Combined Analysis
                           │
         ┌─────────────────┼──────────────────┐
         ▼                 ▼                  ▼
Duplicate Detection   Root Cause Agent   Remediation Agent
         │                 │                  │
         └─────────────────┼──────────────────┘
                           ▼
              AI Bug Analysis Report
```

---

# 🛠️ Technology Stack

## Frontend

- HTML
- CSS
- JavaScript

## Backend

- Python
- Flask

## AI / Machine Learning

- Sentence Transformers
- FAISS (Vector Database)
- LangChain
- Retrieval-Augmented Generation (RAG)

## Datasets

- Mozilla Bug Reports
- Apache Bug Reports
- Eclipse Bug Reports

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
AI-Smart-Bug-Analysis-and-Fix-Adviser/
│
├── backend/
│   ├── agents/
│   ├── utils/
│   ├── app.py
│
├── frontend/
│   ├── static/
│   ├── templates/
│
├── datasets/
│
├── vector_db/
│
├── uploads/
│
├── docs/
│
├── README.md
│
└── .gitignore
```

---

# 🔄 Project Workflow

1. User submits a bug report.
2. Triage Agent predicts severity, priority, and affected module.
3. Log Analysis Agent extracts exception details and failure points.
4. Duplicate Detection Agent retrieves similar historical bugs.
5. Root Cause Agent identifies the probable cause.
6. Remediation Agent suggests appropriate fixes.
7. The system generates a structured AI Bug Analysis Report.

---

# 📊 Current Progress

## ✅ Milestone 1 – Completed

- Project Repository Setup
- System Architecture Design
- Module Design
- Knowledge Base Design
- Workflow Documentation
- Technology Stack Documentation

---

## ✅ Milestone 2 – Completed

- Bug Submission Module
- Triage Agent
- Log Analysis Agent
- Multi-Agent Orchestration
- Duplicate Detection
- Root Cause Analysis
- Remediation Agent
- Validation with Multiple Bug Reports

---

# 🚀 Upcoming Enhancements

- Improve Duplicate Detection using combined analysis
- Enhance Root Cause Analysis
- Improve Remediation Suggestions
- Bug Analytics Dashboard
- PDF Report Generation
- LLM-based Root Cause Explanation
- Advanced Semantic Search

---

# ▶️ How to Run the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd AI-Smart-Bug-Analysis-and-Fix-Adviser
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the Flask server

```bash
python app.py
```

5. Open the application in your browser.

---

# 📌 Sample Output

The application generates a structured report containing:

- Analysis Status
- Submitted Bug
- Triage Analysis
- Log Analysis
- Similar Historical Bugs
- Root Cause Analysis
- Recommended Fixes
- Overall Recommendation

---

# 👩‍💻 Developed By

**Preethi S S**

Computer Science Engineering Student

---

## ⭐ Future Scope

- Support multiple programming languages
- Integration with GitHub Issues
- Real-time Bug Prediction
- Cloud Deployment
- AI-powered Bug Resolution Suggestions
- Interactive Analytics Dashboard


