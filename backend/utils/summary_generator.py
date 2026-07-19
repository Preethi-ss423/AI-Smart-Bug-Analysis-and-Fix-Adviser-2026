class SummaryGenerator:

    def generate_summary(
        self,
        triage,
        log_analysis,
        duplicate_results,
        root_cause,
        remediation
    ):

        duplicate_count = len(duplicate_results)

        summary = {

            "overall_status": "Analysis Completed",

            "severity": triage.get("severity"),

            "priority": triage.get("priority"),

            "bug_category": triage.get("bug_category"),

            "affected_module": triage.get("affected_module"),

            "exception": log_analysis.get("exception"),

            "language": log_analysis.get("language"),

            "duplicate_bugs_found": duplicate_count,

            "root_cause": root_cause.get("root_cause"),

            "impact": root_cause.get("impact"),

            "top_recommendation":
                remediation.get("recommendations")[0]
                if remediation.get("recommendations")
                else "No recommendation"

        }

        return summary