# Standard "Acceptable Use Policies" are outdated. You need a policy that defines levels of autonomy.

## Key sections:

1. The "Stop-Button" Clause: All autonomous agents must have a centralized "Kill Switch" accessible by the Security Operations Center (SOC).

2. Identity Governance: Every AI Agent must have a unique Workload Identity (e.g., Azure Entra ID or AWS IAM Role). No "Shared Service Accounts" for agents.

## Action Tiers:

# Tier 1 (Read-Only): Agent can summarize data. (No approval needed).

# Tier 2 (Internal Action): Agent can move files. (Audit log required).

# Tier 3 (External/Financial): Agent can pay vendors. (MFA-style human approval required).
