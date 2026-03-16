import streamlit as st

st.set_page_config(
    page_title="Synthetic Patient Cohort Generator",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Synthetic Patient Cohort Generator")
st.markdown("""
Welcome to the Pre-configured Cohort Generator. 
Use the sidebar to:
- **Generate**: Select and build a purpose-built synthetic cohort.
- **Data Passport**: View statistical validations for generated cohorts.
- **Export**: Download FHIR Bundles and JSON definitions.
""")
