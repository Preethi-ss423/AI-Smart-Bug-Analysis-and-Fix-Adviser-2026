from agents.remediation_agent import RemediationAgent


agent = RemediationAgent()


root_cause = {
    "root_cause":
    "LoginService contains an uninitialized object which is accessed without null validation."
}


result = agent.suggest_fix(root_cause)


print(result)