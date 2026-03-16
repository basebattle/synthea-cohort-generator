import streamlit as st
import time
import pandas as pd
from utils.fhir_parser import load_bundles

st.title("Generate Synthetic Cohort")

profile = st.selectbox("Select Cohort Profile", ["oncology", "high_risk_readmission", "hospital_at_home"])

if st.button("Generate"):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    
    st.success("Cohort Generated Successfully!")
    
    bundles = load_bundles(profile)
    st.write(f"**Patient Count:** {len(bundles)}")
    
    if bundles:
        df = pd.DataFrame([{"ID": b["entry"][0]["resource"]["id"], "Gender": b["entry"][0]["resource"]["gender"], "BirthDate": b["entry"][0]["resource"]["birthDate"]} for b in bundles])
        st.dataframe(df)

