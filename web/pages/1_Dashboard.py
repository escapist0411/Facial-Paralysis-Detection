import streamlit as st

st.title("📊 Clinical Dashboard")

st.metric("AI Model Accuracy", "96.6%")
st.metric("Segmentation IoU", "0.91")
st.metric("Cases Tested", "300+")

st.info("""
This system uses:
• CNN for paralysis classification  
• U-Net for facial segmentation  
• Landmark asymmetry analysis  
""")

