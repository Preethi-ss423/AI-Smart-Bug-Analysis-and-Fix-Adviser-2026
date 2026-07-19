class RemediationAgent:

    def __init__(self):
        self.name = "Remediation Agent"

    def suggest_fix(self, root_cause_data):

        exception = root_cause_data.get("exception", "")

        if exception == "NullPointerException":

            recommendations = [
                "Initialize objects before accessing their properties.",
                "Add null validation checks before object usage.",
                "Use Objects.requireNonNull() where appropriate.",
                "Write unit tests for null input scenarios."
            ]

        elif exception == "ArrayIndexOutOfBoundsException":

            recommendations = [
                "Validate array indices before accessing elements.",
                "Use array.length to prevent invalid indexing.",
                "Add boundary condition test cases.",
                "Handle invalid index values gracefully."
            ]

        elif exception == "ArithmeticException":

            recommendations = [
                "Check for division by zero before calculations.",
                "Validate numeric inputs.",
                "Use exception handling around arithmetic operations.",
                "Add test cases for edge conditions."
            ]

        elif exception == "FileNotFoundException":

            recommendations = [
                "Verify that the file path is correct.",
                "Check whether the file exists before opening it.",
                "Handle missing files using try-catch blocks.",
                "Provide a meaningful error message to the user."
            ]

        elif exception == "ClassNotFoundException":

            recommendations = [
                "Verify project dependencies.",
                "Ensure the required JAR files are included.",
                "Check package names and class paths.",
                "Rebuild the project after fixing dependencies."
            ]

        else:

            recommendations = [
                "Review the complete stack trace.",
                "Analyze the affected module.",
                "Improve exception handling.",
                "Add additional logging for debugging."
            ]

        return {
            "agent": self.name,
            "exception": exception,
            "recommendations": recommendations
        }