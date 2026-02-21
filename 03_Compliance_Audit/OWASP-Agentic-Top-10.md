# OWASP Top 10 for Agentic Applications (2026)
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

This framework addresses the security and governance risks associated with autonomous AI agents that have the ability to plan, use tools, and execute workflows.

| ID | Risk Category | GRC & Analyst Mitigation Strategy |
| :--- | :--- | :--- |
| **ASI-01** | **Agent Goal Hijack** | Implement "Mandate Validation": The agent's core mission must be cryptographically signed and verified before execution of sub-tasks. |
| **ASI-02** | **Tool Misuse & Exploitation** | Apply the "Principle of Least Privilege" to AI toolsets. Use sandboxed environments for execution of agent-generated code. |
| **ASI-03** | **Identity & Privilege Abuse** | Assign unique **Machine Identities** to agents. Avoid sharing user session tokens; use "On-Behalf-Of" tokens with scoped permissions. |
| **ASI-04** | **Agentic Supply Chain** | Maintain an **AIBOM (AI Bill of Materials)**. Vet third-party Model Context Protocol (MCP) servers and orchestrators for security posture. |
| **ASI-05** | **Unexpected Code Execution** | Enforce "Static Analysis" on agent-generated scripts before execution. Block access to system-level APIs and sensitive environment variables. |
| **ASI-06** | **Memory & Context Poisoning** | Implement "Contextual Scrubbing": Periodically purge agent long-term memory and sanitize RAG inputs to prevent persistent instruction injection. |
| **ASI-07** | **Insecure Inter-Agent Comm** | Require Mutual TLS (mTLS) or signed messaging for Multi-Agent Systems (MAS) to prevent "Agent Spoofing" or unauthorized task handoffs. |
| **ASI-08** | **Cascading Failures** | Establish "Circuit Breakers": Automated limits on API calls, financial spend, or recursive loops to stop runaway autonomous processes. |
| **ASI-09** | **Human-Agent Trust Exploitation** | Conduct "Authority Bias" training for human reviewers. Mandate "Reasoning Traces" (Chain-of-Thought) for all high-impact AI decisions. |
| **ASI-10** | **Rogue Agent Persistence** | Implement "Agent TTL (Time-to-Live)": Automatically de-provision agent identities and compute resources after task completion to prevent persistence. |
