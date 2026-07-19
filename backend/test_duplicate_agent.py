from agents.duplicate_detection_agent import DuplicateAgent

agent = DuplicateAgent()

query = """
NullPointerException in Login Module

Application crashes when username is empty.

java.lang.NullPointerException
"""

results = agent.find_similar_bugs(query)

print("\n========== DUPLICATE DETECTION AGENT ==========\n")

for i, bug in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 50)
    print("Bug ID      :", bug["bug_id"])
    print("Product     :", bug["product"])
    print("Component   :", bug["component"])
    print("Title       :", bug["title"])
    print("Severity    :", bug["severity"])
    print("Resolution  :", bug["resolution"])