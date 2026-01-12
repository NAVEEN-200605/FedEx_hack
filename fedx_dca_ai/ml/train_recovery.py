import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("data/raw_cases.csv")

# Create target (simulated)
df["recovered"] = (df["days_overdue"] < 90).astype(int)

X = df[["amount_due", "days_overdue", "past_payment_delay", "previous_escalations"]]
y = df["recovered"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "models/recovery_model.pkl")
print("Recovery model saved")
