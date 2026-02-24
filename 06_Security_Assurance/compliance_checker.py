import pandas as pd
from datetime import datetime

# SIMULATED DATA: In a real environment, this would be a live API call to AWS/Azure
# As a GRC Analyst, you use this to verify "Control Effectiveness"
infrastructure_assets = [
    {"bucket_name": "atc-public-assets", "is_encrypted": True, "public_access": "Blocked", "status": "Compliant"},
    {"bucket_name": "atc-client-data-01", "is_encrypted": True, "public_access": "OPEN", "status": "NON-COMPLIANT"},
    {"bucket_name": "atc-agent-logs-2026", "is_encrypted": False, "public_access": "Blocked", "status": "NON-COMPLIANT"},
    {"bucket_name": "atc-internal-wiki", "is_encrypted": True, "public_access": "Blocked", "status": "Compliant"}
]

def run_compliance_audit(data):
    print(f"--- Agentic Trust Corp: Automated Compliance Scan ({datetime.now().strftime('%Y-%m-%d')}) ---")
    df = pd.DataFrame(data)
    
    # Logic: Find assets that violate the 'Blocked' public access policy
    violations = df[df['public_access'] == 'OPEN']
    
    if not violations.empty:
        print(f"⚠️ ALERT: {len(violations)} Security Policy Violations Found!")
        for index, row in violations.iterrows():
            print(f"🔴 ACTION REQUIRED: System '{row['bucket_name']}' is EXPOSED to the public internet.")
    else:
        print("✅ All systems meet the Public Access Block policy.")

    # Exporting for Audit Evidence (The GRC "Paper Trail")
    df.to_csv("compliance_audit_report.csv", index=False)
    print("\n[Audit Evidence Generated: compliance_audit_report.csv]")

if __name__ == "__main__":
    run_compliance_audit(infrastructure_assets)
