from agents.triage_agent import TriageAgent

agent = TriageAgent()

result = agent.process_bug(
    "NullPointerException in Login",
    "Application crashes when username is empty.",
    "java.lang.NullPointerException"
)

print(result)