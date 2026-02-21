From https://genai.owasp.org/llm-top-10/
| ID | Risk Category | GRC / Analyst Focus |
| :--- | :--- | :--- |
| **LLM01** | Prompt Injection | **Control:** Implement robust input sanitization and use "System Messages" that cannot be overridden by user data. |
| **LLM02** | Sensitive Info Disclosure | **Control:** Use Data Loss Prevention (DLP) tools to scrub PII/PHI from training data and user prompts. |
| **LLM03** | Supply Chain Vulnerabilities | **Control:** Third-party vetting of base models (e.g., OpenAI, Anthropic) and auditing of Python libraries used. |
| **LLM04** | Data and Model Poisoning | **Control:** Verify the integrity of data used for Fine-Tuning or RAG (Retrieval-Augmented Generation). |
| **LLM05** | Improper Output Handling | **Control:** Treat LLM output as "untrusted." Ensure it is sanitized before it hits a web browser or a database. |
| **LLM06** | Excessive Agency | **Control:** Limit the "tools" an AI can use. (e.g., An AI should not have permission to delete a user account). |
| **LLM07** | System Prompt Leakage | **Control:** Design system prompts with the assumption they will be public. Never put secrets in the "Instructions." |
| **LLM08** | Vector & Embedding Weaknesses | **Control:** Secure the Vector Database (e.g., Pinecone, Milvus) with strict RBAC (Role-Based Access Control). |
| **LLM09** | Misinformation (Hallucinations) | **Control:** Implement "Grounding." The AI must cite a specific internal document for every claim it makes. |
| **LLM10** | Unbounded Consumption | **Control:** Set API rate limits and "Spend Caps" to prevent a DoS attack or a massive bill. |
