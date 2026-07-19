class ReportGenerator:

    def generate_report(
        self,
        query,
        triage,
        log_analysis,
        duplicate_results,
        root_cause,
        remediation
    ):

        report = {

            "analysis_status": "Completed",

            "submitted_bug": {
                "title": query.get("title"),
                "description": query.get("description"),
                "stack_trace": query.get("stack_trace")
            },

            "triage": {
                "category": triage.get("bug_category"),
                "severity": triage.get("severity"),
                "priority": triage.get("priority"),
                "affected_module": triage.get("affected_module"),
                "confidence_score": triage.get("confidence_score"),
                "reasoning": triage.get("reasoning")
            },
            "log_analysis": {
                "language": log_analysis.get("language"),
                "exception": log_analysis.get("exception"),
                "file": log_analysis.get("file"),
                "method": log_analysis.get("method"),
                "line": log_analysis.get("line"),
                "failure_point": log_analysis.get("failure_point"),
                "affected_code_path": log_analysis.get("affected_code_path")
            },

            "duplicate_bugs": {
                "count": len(duplicate_results),
                "matches": duplicate_results
            },

            "root_cause": root_cause,

            "remediation": remediation,

            "overall_recommendation": (
                f"This is a {triage.get('severity')} "
                f"{triage.get('bug_category')} affecting "
                f"{triage.get('affected_module')}. "
                "Follow the remediation recommendations "
                "to resolve the issue."
            )

        }

        return report