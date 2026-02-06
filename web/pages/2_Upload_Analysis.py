import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(ROOT_DIR)

import streamlit as st
from PIL import Image


from src.predict import predict_image
from src.unet_segmenter import run_unet_segmentation
from src.visualize_segmentation import create_segmentation_overlay
from src.report_generator import generate_report

st.title("📤 Patient Upload & AI Analysis")

with st.form("patient_form"):
    col1, col2 = st.columns(2)

    with col1:
        patient_name = st.text_input("Patient Name")
        age = st.text_input("Age")

    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    uploaded_file = st.file_uploader("Upload Face Image", type=["jpg","png","jpeg"])
    submit = st.form_submit_button("🧠 Run Analysis")

if submit and uploaded_file:

    os.makedirs("reports/images", exist_ok=True)

    original_path = "reports/images/original.png"
    image = Image.open(uploaded_file)
    image.save(original_path)

    st.image(image, caption="Uploaded Image", width=250)

    with st.spinner("Running AI models..."):

        diagnosis, score, severity = predict_image(original_path)

        mask = run_unet_segmentation(original_path)

        mask_path = "reports/images/segmentation_mask.png"
        overlay_path = "reports/images/segmentation.png"

        from cv2 import imwrite
        imwrite(mask_path, mask * 255)

        create_segmentation_overlay(
            original_path,
            mask_path,
            overlay_path
        )

        generate_report(
            patient_name,
            age,
            gender,
            diagnosis,
            score,
            severity,
            original_path,
            overlay_path
        )

    st.success("✅ Medical Report Generated")

    st.image(overlay_path, caption="Segmentation Result", width=300)

    with open("reports/final_medical_report.pdf","rb") as f:
        st.download_button(
            "📄 Download Report",
            f,
            file_name="Facial_Paralysis_Report.pdf",
            mime="application/pdf"
        )
