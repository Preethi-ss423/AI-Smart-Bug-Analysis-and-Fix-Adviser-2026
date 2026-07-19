import re


class TriageAgent:

    def process_bug(self, title, description, stack_trace):

        # Clean input
        title = title.strip()
        description = description.strip()
        stack_trace = stack_trace.strip()

        # Validate input
        if title == "" and description == "" and stack_trace == "":
            return {
                "success": False,
                "message": "No bug information provided."
            }

        # ---------------- Bug Category ----------------
        bug_category = "General Bug"

        if "Exception" in stack_trace:
            bug_category = "Runtime Exception"
        elif "error" in description.lower():
            bug_category = "Application Error"

        # ---------------- Severity ----------------
        severity = "Low"

        critical_exceptions = [
            "NullPointerException",
            "OutOfMemoryError",
            "StackOverflowError"
        ]

        high_exceptions = [
            "ArrayIndexOutOfBoundsException",
            "ClassNotFoundException",
            "FileNotFoundException"
        ]

        for exc in critical_exceptions:
            if exc in stack_trace:
                severity = "Critical"
                break

        if severity != "Critical":
            for exc in high_exceptions:
                if exc in stack_trace:
                    severity = "High"
                    break

        # ---------------- Priority ----------------
        priority_map = {
            "Critical": "P1",
            "High": "P2",
            "Medium": "P3",
            "Low": "P4"
        }

        priority = priority_map.get(severity, "P4")
        
        # ---------------- Confidence Score ----------------

        confidence_map = {
                "Critical": 98,
                "High": 90,
                "Medium": 80,
                "Low": 70
            }

        confidence_score = confidence_map.get(severity, 70)

        # ---------------- Affected Module ----------------
        module = "Unknown"

        module_match = re.search(r'at\s+([\w\.]+)\.', stack_trace)

        if module_match:
            module = module_match.group(1).split(".")[-1]
            
            # ---------------- Reasoning ----------------

        reasoning = []

        if severity == "Critical":
         reasoning.append("Critical exception detected in stack trace.")
         reasoning.append("Application execution is likely interrupted.")
        elif severity == "High":
         reasoning.append("High-impact exception detected.")
        elif severity == "Medium":
         reasoning.append("Issue affects functionality but is not critical.")
        else:
         reasoning.append("Minor issue with limited impact.")

        if module != "Unknown":
         reasoning.append(f"Affected module identified as '{module}'.")

        if "login" in title.lower() or "login" in description.lower():
         reasoning.append("Bug occurs during the login workflow, affecting user authentication.")
            
            

        # ---------------- Build Query ----------------
        query_text = f"{title}\n{description}\n{stack_trace}"

        return {

            "success": True,

            "title": title,

            "description": description,

            "stack_trace": stack_trace,

            "bug_category": bug_category,

            "severity": severity,

            "priority": priority,

            "affected_module": module,
            
            "confidence_score": confidence_score,

            "reasoning": reasoning,

            "query_text": query_text
        }