from agents.root_cause_agent import RootCauseAgent

agent = RootCauseAgent()

query = {
    "title": "NullPointerException in Login",
    "description": "Application crashes during login"
}

log_analysis = {
    "exception": "NullPointerException"
}

similar_bugs = []

result = agent.analyze(query, log_analysis, similar_bugs)

print(result["root_cause"])