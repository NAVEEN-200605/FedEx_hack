import pandas as pd
from backend.decision import assign_dca

cases = pd.read_csv("data/raw_cases.csv")

results = []
for _, row in cases.iterrows():
    results.append(assign_dca(row.to_dict()))

output = pd.DataFrame(results)
output.to_csv("data/assigned_cases.csv", index=False)
print("Pipeline completed")
