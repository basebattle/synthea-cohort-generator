import streamlit as st
import os

st.title("Export Cohort Data")

profile = st.selectbox("Select Cohort to Export", ["oncology", "high_risk_readmission", "hospital_at_home"])

st.markdown("### FHIR R4 Bundle")
st.download_button(
    label="Download FHIR Bundles (ZIP)",
    data=b"Mock ZIP content",
    file_name=f"{profile}_fhir_bundle.zip",
    mime="application/zip"
)

st.markdown("### Cohort Definition")
config_file = os.path.join(os.path.dirname(__file__), f"../../generator/profiles/{profile}.json")
config_data = ""
if os.path.exists(config_file):
    with open(config_file, "r") as f:
        config_data = f.read()
        
st.download_button(
    label="Download JSON Config",
    data=config_data,
    file_name=f"{profile}_config.json",
    mime="application/json"
)

st.markdown("### Data Passport")
st.download_button(
    label="Download Passport (PDF)",
    data=b"Mock PDF Content",
    file_name=f"{profile}_passport.pdf",
    mime="application/pdf"
)
