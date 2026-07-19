from agents.log_analysis_agent import LogAnalysisAgent

agent = LogAnalysisAgent()

stack_trace = """
java.lang.NullPointerException
at com.example.login.LoginService.authenticate(LoginService.java:54)
at com.example.login.LoginController.login(LoginController.java:28)
"""

result = agent.analyze(stack_trace)

print("========== LOG ANALYSIS AGENT ==========\n")

print("Language :", result["language"])
print("Exception:", result["exception"])
print("Module   :", result["module"])
print("File     :", result["file"])
print("Line No. :", result["line"])