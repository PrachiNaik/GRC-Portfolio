### 🛡️ 2026 AI Risk Register

| Risk ID | Risk Scenario | Framework | Inherent Risk | Mitigation Control | Residual Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AI-01** | **Memory Poisoning:** Attacker implants instructions in Agent memory. | ISO A.8.2 | 🔴 Critical | **Stateful Sanitization:** Scrub memory of commands. | 🟢 Low |
| **AI-02** | **Excessive Agency:** Agent deletes database due to prompt trickery. | ISO A.6.3 | 🟠 High | **HITL:** Require Digital Signature for deletes. | 🟡 Medium |
| **AI-03** | **Prompt Injection:** Agent exfiltrates secrets from external data. | ISO A.5.4 | 🔴 Critical | **Sandboxing:** Remove 'write' access for external tasks. | 🟡 Medium |
