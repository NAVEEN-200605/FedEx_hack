import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/raw_cases.csv")

df["escalated"] = (df["previous_escalations"] > 0).astype(int)

X = df[["days_overdue", "past_payment_delay"]]
y = df["escalated"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "models/escalation_model.pkl")
print("Escalation model saved")
