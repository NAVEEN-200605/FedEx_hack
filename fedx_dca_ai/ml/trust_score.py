import pandas as pd

def calculate_trust_scores():
    dca = pd.read_csv("data/dca_performance.csv")

    dca["trust_score"] = (
        dca["recovery_rate"] * 100
        - dca["sla_violations"] * 5
        - dca["escalation_rate"] * 50
        - dca["update_delay_days"] * 3
    )

    return dca[["dca_id", "trust_score"]]
