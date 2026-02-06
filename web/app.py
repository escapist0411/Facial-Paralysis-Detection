import streamlit as st

st.set_page_config(
    page_title="AI Facial Paralysis System",
    layout="wide",
    page_icon="🧠"
)

st.sidebar.title("🏥 AI Medical Portal")
st.sidebar.markdown("Facial Paralysis Detection")

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #f0f6ff;
}
</style>
""", unsafe_allow_html=True)

st.title("Welcome Doctor 👨‍⚕️")
st.write("Use the sidebar to navigate through the system.")
