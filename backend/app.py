from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from utils.report_generator import ReportGenerator
import os
from flask import Flask, send_from_directory, send_file
from utils.pdf_generator import generate_pdf

from agents.triage_agent import TriageAgent
from agents.log_analysis_agent import LogAnalysisAgent
from agents.duplicate_detection_agent import DuplicateAgent
from agents.root_cause_agent import RootCauseAgent
from agents.remediation_agent import RemediationAgent


# ---------------- APP SETUP ----------------

app = Flask(__name__, static_folder="../frontend")
CORS(app)
latest_report = {}

# ---------------- LOAD AGENTS ----------------

print("⏳ Loading AI Agents...")

triage_agent = TriageAgent()

log_agent = LogAnalysisAgent()

duplicate_agent = DuplicateAgent()

root_agent = RootCauseAgent()

remediation_agent = RemediationAgent()

report_generator = ReportGenerator()

print("✅ All AI Agents Loaded Successfully!")


# ---------------- UPLOAD FOLDER ----------------

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# ---------------- FRONTEND ROUTE ----------------

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/download_report")
def download_report():

    global latest_report

    if not latest_report:
        return "No bug analysis available. Please analyze a bug first.", 400

    pdf = generate_pdf(latest_report)

    return send_file(
        pdf,
        as_attachment=True
    )

@app.route("/routes")
def routes():
    return str(app.url_map)

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


    uploaded_file = request.files.get("bugFile")

    file_name = None


    if uploaded_file and uploaded_file.filename != "":

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            uploaded_file.filename
        )

        uploaded_file.save(file_path)

        file_name = uploaded_file.filename



    # ---------------- TRIAGE AGENT ----------------

    triage_result = triage_agent.process_bug(
        title,
        description,
        stack_trace
    )
    print("========== TRIAGE RESULT ==========")
    print(triage_result)
    print("===================================")

    if not triage_result["success"]:

        return jsonify({
            "error": triage_result["message"]
        }), 400



    query_text = triage_result["query_text"]



    # ---------------- LOG ANALYSIS AGENT ----------------

    log_result = log_agent.analyze(stack_trace)

    # ---------------- COMBINED ANALYSIS ----------------

    combined_analysis = {

        "submitted_bug": {
            "title": title,
            "description": description,
            "stack_trace": stack_trace,
            "uploaded_file": file_name
        },

        "triage": triage_result,

        "log_analysis": log_result

}
    print("\n========== COMBINED ANALYSIS ==========")
    print(combined_analysis)
    print("=======================================\n")

    # ---------------- DUPLICATE DETECTION AGENT ----------------

    duplicate_result = duplicate_agent.find_similar_bugs(
        query_text
    )



    # ---------------- ROOT CAUSE AGENT ----------------

    root_cause_result = root_agent.analyze_root_cause(
        log_result
    )



    # ---------------- REMEDIATION AGENT ----------------

    remediation_result = remediation_agent.suggest_fix(
    root_cause_result
)
    report_result = report_generator.generate_report(

    {
        "title": title,
        "description": description,
        "stack_trace": stack_trace
    },

    triage_result,

    log_result,

    duplicate_result,

    root_cause_result,

    remediation_result
)
    global latest_report

    latest_report = {

    "bug_info": {
        "title": title,
        "description": description,
        "stack_trace": stack_trace,
        "uploaded_file": file_name
    },

    "triage": triage_result,

    "log_analysis": log_result,

    "duplicate": duplicate_result,

    "root_cause": root_cause_result,

    "fix": remediation_result

}

    # ---------------- FINAL RESPONSE ----------------

    return jsonify({
           "report": report_result,     
                 "query": {

            "title": title,

            "description": description,

            "stack_trace": stack_trace

        },


        "triage": triage_result,


        "log_analysis": log_result,


        "duplicate_detection": duplicate_result,


        "root_cause": root_cause_result,


        "remediation": remediation_result,


        "uploaded_file": file_name

    })



# ---------------- RUN SERVER ----------------

if __name__ == "__main__":

  app.run(debug=True, use_reloader=False)

