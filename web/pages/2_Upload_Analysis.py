import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import streamlit as st
from PIL import Image
import time
import cv2

from src.predict import predict_image
from src.unet_segmenter import run_unet_segmentation
from src.visualize_segmentation import create_segmentation_overlay
from src.report_generator import generate_report
from web.theme import load_custom_css, apply_sidebar_branding

st.set_page_config(
    page_title="Neural Shield AI - Run Analysis",
    layout="wide",
    page_icon="📤"
)

load_custom_css()
apply_sidebar_branding()

st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #6366f1; font-weight: 600;">Diagnostic Lab Module</span>
    <h1>Patient Upload & AI Analysis</h1>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="premium-card">', unsafe_allow_html=True)

with st.form("patient_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        patient_name = st.text_input("Full Patient Name")
    with col2:
        age = st.text_input("Age")
    with col3:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg", "jpeg", "png"]
    )

    submit = st.form_submit_button("Run Analysis")

st.markdown("</div>", unsafe_allow_html=True)

if submit:
    if not patient_name:
        st.error("Enter patient name")
    elif not age.isdigit():
        st.error("Enter valid age")
    elif not uploaded_file:
        st.error("Upload image")
    else:
        os.makedirs("reports/images", exist_ok=True)

        original_path = "reports/images/original.png"
        image = Image.open(uploaded_file)
        image.save(original_path)

        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("Step 1/4: Prediction")
        progress_bar.progress(25)
        diagnosis, score, severity, confidence = predict_image(original_path)

        status_text.text("Step 2/4: Segmentation")
        progress_bar.progress(50)
        mask = run_unet_segmentation(original_path)

        status_text.text("Step 3/4: Overlay")
        progress_bar.progress(75)

        mask_path = "reports/images/segmentation_mask.png"
        overlay_path = "reports/images/segmentation.png"

        cv2.imwrite(mask_path, (mask * 255).astype("uint8"))
        create_segmentation_overlay(original_path, mask_path, overlay_path)

        status_text.text("Step 4/4: Report")
        progress_bar.progress(100)

        generate_report(
            patient_name,
            age,
            gender,
            diagnosis,
            score,
            severity,
            confidence,
            original_path,
            overlay_path
        )

        status_text.empty()
        progress_bar.empty()

        st.success("Analysis completed")

        col_res1, col_res2 = st.columns([1, 1.2])

        with col_res1:
            st.write("### Diagnosis Summary")
            st.write(f"Diagnosis: {diagnosis}")
            st.write(f"Score: {score:.4f}")
            st.write(f"Severity: {severity}")
            st.write(f"Confidence: {confidence}")

            if os.path.exists("reports/final_medical_report.pdf"):
                with open("reports/final_medical_report.pdf", "rb") as f:
                    st.download_button(
                        label="Download Report",
                        data=f,
                        file_name=f"{patient_name}_report.pdf",
                        mime="application/pdf"
                    )

        with col_res2:
            tab1, tab2 = st.tabs(["Segmentation", "Original"])

            with tab1:
                st.image(overlay_path, width=700)

            with tab2:
                st.image(original_path, width=700)