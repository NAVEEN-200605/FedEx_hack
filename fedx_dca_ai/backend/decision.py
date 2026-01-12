import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
import pandas as pd
from ml.trust_score import calculate_trust_scores

recovery_model = joblib.load("models/recovery_model.pkl")
escalation_model = joblib.load("models/escalation_model.pkl")

def assign_dca(case):
    X_recovery = [[
        case["amount_due"],
        case["days_overdue"],
        case["past_payment_delay"],
        case["previous_escalations"]
    ]]

    recovery_prob = recovery_model.predict_proba(X_recovery)[0][1]

    X_esc = [[case["days_overdue"], case["past_payment_delay"]]]
    escalation_risk = escalation_model.predict(X_esc)[0]

    trust_df = calculate_trust_scores()
    best_dca = trust_df.sort_values("trust_score", ascending=False).iloc[0]

    return {
        "recommended_dca": best_dca["dca_id"],
        "recovery_probability": round(recovery_prob, 2),
        "escalation_risk": "High" if escalation_risk else "Low",
        "reason": "Best trust score with high recovery probability"
    }
