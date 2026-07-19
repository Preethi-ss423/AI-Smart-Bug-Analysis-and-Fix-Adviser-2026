import re


class LogAnalysisAgent:

    def analyze(self, stack_trace):

        result = {
            "language": "Unknown",
            "exception": "Unknown",
            "module": "Unknown",
            "file": "Unknown",
            "line": "Unknown",
            "method": "Unknown",
            "package": "Unknown",
            "error_type": "Unknown",
            "stack_depth": 0
        }

        # ---------------- Programming Language ----------------

        if "java" in stack_trace.lower():
            result["language"] = "Java"

        # ---------------- Exception ----------------

        exception_match = re.search(r'([A-Za-z]+Exception|[A-Za-z]+Error)', stack_trace)

        if exception_match:
            result["exception"] = exception_match.group(1)

        # ---------------- Java File ----------------

        file_match = re.search(r'([A-Za-z0-9_]+\.java)', stack_trace)

        if file_match:
            result["file"] = file_match.group(1)

        # ---------------- Line Number ----------------

        line_match = re.search(r':(\d+)', stack_trace)

        if line_match:
            result["line"] = line_match.group(1)

        # ---------------- Package, Class & Method ----------------

        method_match = re.search(
            r'at\s+([\w\.]+)\.([A-Za-z0-9_]+)\(([\w\.]+):(\d+)\)',
            stack_trace
        )

        if method_match:

            full_path = method_match.group(1)

            result["method"] = method_match.group(2)

            parts = full_path.split(".")

            if len(parts) > 1:

                result["package"] = ".".join(parts[:-1])

                result["module"] = parts[-1]

            else:

                result["module"] = full_path

        # ---------------- Error Type ----------------

        runtime_errors = [
            "NullPointerException",
            "ArrayIndexOutOfBoundsException",
            "ArithmeticException",
            "ClassNotFoundException",
            "FileNotFoundException"
        ]

        if result["exception"] in runtime_errors:
            result["error_type"] = "Runtime Error"

        elif "Error" in result["exception"]:
            result["error_type"] = "System Error"

        else:
            result["error_type"] = "General Error"

        # ---------------- Stack Depth ----------------

        result["stack_depth"] = len(
            re.findall(r'^\s*at\s+', stack_trace, re.MULTILINE)
        )

    # ---------------- Failure Point ----------------

        if result["file"] != "Unknown":
         result["failure_point"] = (
         f'{result["module"]}.{result["method"]}() '
         f'at {result["file"]}:{result["line"]}'
    )
        else:
         result["failure_point"] = "Unknown"
         
         # ---------------- Affected Code Path ----------------

        code_path = []

        matches = re.findall(
            r'at\s+([\w\.]+)\.([A-Za-z0-9_]+)\(',
            stack_trace
        )

        for full_path, method in matches:
            class_name = full_path.split(".")[-1]
            code_path.append(f"{class_name}.{method}()")

        result["affected_code_path"] = code_path
                
                
        return result