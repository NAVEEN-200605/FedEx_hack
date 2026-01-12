import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from backend.decision import assign_dca

st.title("FedEx AI DCA Management")

df = pd.read_csv("data/raw_cases.csv")
case_id = st.selectbox("Select Case", df["case_id"])

case = df[df["case_id"] == case_id].iloc[0].to_dict()

if st.button("Assign DCA"):
    result = assign_dca(case)

    st.success(f"Recommended DCA: {result['recommended_dca']}")
    st.write("Recovery Probability:", result["recovery_probability"])
    st.write("Escalation Risk:", result["escalation_risk"])
    st.info(result["reason"])
