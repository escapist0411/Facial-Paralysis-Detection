import streamlit as st
import os

st.title("📄 Generated Reports")

if os.path.exists("reports/final_medical_report.pdf"):
    with open("reports/final_medical_report.pdf","rb") as f:
        st.download_button(
            "Download Latest Report",
            f,
            file_name="Facial_Paralysis_Report.pdf"
        )
else:
    st.warning("No reports generated yet.")
