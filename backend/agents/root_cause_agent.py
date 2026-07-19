class RootCauseAgent:

    def __init__(self):
        self.name = "Root Cause Analysis Agent"

    def analyze_root_cause(self, log_data):

        exception = log_data.get("exception", "")
        module = log_data.get("module", "Unknown")

        if exception == "NullPointerException":

            root_cause = (
                f"{module} contains an uninitialized object "
                "that is accessed without performing a null check."
            )

            impact = (
                "Application execution stops, preventing users from "
                "completing the requested operation."
            )

        elif exception == "ArrayIndexOutOfBoundsException":

            root_cause = (
                f"{module} is attempting to access an array index "
                "outside its valid range."
            )

            impact = (
                "The application crashes while processing array data."
            )

        elif exception == "ArithmeticException":

            root_cause = (
                f"{module} performs an invalid arithmetic operation, "
                "such as division by zero."
            )

            impact = (
                "The requested calculation fails and interrupts execution."
            )

        elif exception == "FileNotFoundException":

            root_cause = (
                f"{module} cannot locate the required file."
            )

            impact = (
                "The application cannot continue because required data is unavailable."
            )

        elif exception == "ClassNotFoundException":

            root_cause = (
                f"{module} references a class that is missing from the application."
            )

            impact = (
                "The application cannot load the required component."
            )

        else:

            root_cause = (
                "The exact root cause could not be determined from the available log."
            )

            impact = (
                "Further debugging and log analysis are required."
            )

        return {
            "agent": self.name,
            "exception": exception,
            "module": module,
            "root_cause": root_cause,
            "impact": impact
        }