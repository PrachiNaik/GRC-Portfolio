# AI Vendor Security Questionnaire (GRC-01)

**Vendor Name:** ____________________  
**AI Product/Service:** ____________________  
**Date of Assessment:** 2026-02-21

## Section 1: Data Governance & Privacy
*These questions ensure our company data isn't being "leaked" or used to help our competitors.*

1. **Training Data Use:** Will our company data (prompts, uploaded files, or API data) be used to train or improve your base AI models?
   - [ ] Yes  - [ ] No
2. **Data Isolation:** How do you technically ensure that our data never "bleeds" into another customer's AI session? 
3. **Data Deletion:** Do you provide a "Right to be Forgotten" for AI? If we delete a document, is it also removed from the AI's "long-term memory" (Vector Database)?

## Section 2: Accountability & Human Oversight
*These questions ensure the AI doesn't make major mistakes without a human being responsible.*

4. **Human-in-the-Loop (HITL):** Does your AI system perform high-impact actions (like moving money or deleting accounts) autonomously, or is human approval required by default?
5. **Explainability:** If the AI makes a decision (e.g., rejecting a loan or flagging a user), can the system provide a "Reasoning Trace" explaining **why** it made that choice?

## Section 3: Reliability & "The Kill Switch"
*These questions ensure the business stays running even if the AI fails.*

6. **Accuracy Monitoring:** How do you measure "Hallucinations" (the AI making things up)? Do you provide a monthly report on model accuracy?
7. **Business Continuity:** If your AI provider (e.g., OpenAI or Anthropic) has an outage, does your system have a "fallback" mode, or does the service stop entirely?
8. **The Kill Switch:** Is there a manual "Panic Button" our admins can press to immediately disconnect the AI from our internal databases?

---
**Reviewer Note (GRC Analyst):** *This questionnaire is mapped to ISO 42001 (AI Management System) and the EU AI Act requirements for high-risk AI systems.*
