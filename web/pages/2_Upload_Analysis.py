import sys
import os

# Add root dir to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

import streamlit as st
from PIL import Image
import time
from cv2 import imwrite

from src.predict import predict_image
from src.unet_segmenter import run_unet_segmentation
from src.visualize_segmentation import create_segmentation_overlay
from src.report_generator import generate_report
from web.theme import load_custom_css

# Page Configuration
st.set_page_config(
    page_title="Neural Shield AI - Run Analysis",
    layout="wide",
    page_icon="📤"
)

# Load global CSS styling
load_custom_css()

# Sidebar branding
from web.theme import apply_sidebar_branding
apply_sidebar_branding()

# Header Section
st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #6366f1; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;">Diagnostic Lab Module</span>
    <h1 style="margin: 5px 0 15px 0; font-size: 2.5rem;">Patient Upload & AI Analysis</h1>
    <p style="font-size: 1rem; color: #94a3b8; max-width: 800px;">
        Perform deep learning-based diagnostics on patient imagery. Fill in client information, upload a frontal facial photo, and execute neural profiling.
    </p>
</div>
""", unsafe_allow_html=True)

# Form wrapped in premium card container styling
st.markdown('<div class="premium-card">', unsafe_allow_html=True)
with st.form("patient_form"):
    st.markdown("<h4 style='color:#f8fafc; margin-top:0;'>1. Patient Intake Record</h4>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)

    with col1:
        patient_name = st.text_input("Full Patient Name", placeholder="e.g. John Doe")
    with col2:
        age = st.text_input("Age (Years)", placeholder="e.g. 45")
    with col3:
        gender = st.selectbox("Gender at Birth", ["Male", "Female", "Other"])

    st.markdown("<h4 style='color:#f8fafc; margin-top:15px;'>2. Frontal Facial Photograph</h4>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload image (PNG, JPG, JPEG) in neutral expression", type=["jpg", "png", "jpeg"])
    
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    submit = st.form_submit_button("🧠 Run Diagnostics & Segmentations")
st.markdown('</div>', unsafe_allow_html=True)

if submit:
    if not patient_name:
        st.error("⚠️ Please specify patient name before executing diagnostics.")
    elif not age or not age.isdigit():
        st.error("⚠️ Please enter a valid numerical age.")
    elif not uploaded_file:
        st.error("⚠️ Please upload a patient photo image.")
    else:
        # Create output folders
        os.makedirs("reports/images", exist_ok=True)
        original_path = "reports/images/original.png"
        
        # Save original file
        image = Image.open(uploaded_file)
        image.save(original_path)

        # Set up dynamic progress bars
        st.markdown("<br><h3><i class='fa-solid fa-gears' style='color:#38bdf8;'></i> Analyzing Image...</h3>", unsafe_allow_html=True)
        progress_bar = st.progress(0)
        status_text = st.empty()

        # Step 1: CNN Predict
        status_text.text("Step 1/4: Querying CNN model for classification...")
        progress_bar.progress(25)
        time.sleep(0.4)
        diagnosis, score, severity, confidence = predict_image(original_path)

        # Step 2: U-Net segment
        status_text.text("Step 2/4: Computing U-Net facial segmentation masks...")
        progress_bar.progress(50)
        time.sleep(0.4)
        mask = run_unet_segmentation(original_path)

        # Step 3: Create overlays
        status_text.text("Step 3/4: Rendering asymmetry landmark coordinates & overlays...")
        progress_bar.progress(75)
        time.sleep(0.3)
        mask_path = "reports/images/segmentation_mask.png"
        overlay_path = "reports/images/segmentation.png"
        imwrite(mask_path, mask * 255)
        create_segmentation_overlay(original_path, mask_path, overlay_path)

        # Step 4: PDF Compilation
        status_text.text("Step 4/4: Compiling clinical PDF report...")
        progress_bar.progress(100)
        time.sleep(0.3)
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

        st.success("✅ Diagnostic processing completed. Results compiled.")

        # Display Results
        col_res1, col_res2 = st.columns([1, 1.2])

        with col_res1:
            st.markdown("### <i class='fa-solid fa-stethoscope' style='color:#6366f1;'></i> Diagnosis Summary", unsafe_allow_html=True)
            
            # Badge styles based on severity
            badge_color = "#22c55e"  # green
            bg_color = "rgba(34, 197, 94, 0.1)"
            
            if severity.lower() == "mild":
                badge_color = "#eab308"  # yellow
                bg_color = "rgba(234, 179, 8, 0.1)"
            elif severity.lower() in ["moderate", "severe"]:
                badge_color = "#ef4444"  # red
                bg_color = "rgba(239, 68, 68, 0.1)"

            st.markdown(f"""
            <div class="premium-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 20px;">
                    <span style="font-weight:600; color:#94a3b8;">DIAGNOSTIC VERDICT</span>
                    <div style="background:{bg_color}; color:{badge_color}; border: 1px solid {badge_color}; padding:6px 14px; border-radius:30px; font-size:0.85rem; font-weight:700; text-transform:uppercase;">
                        {diagnosis}
                    </div>
                </div>
                <table style="width:100%; border-collapse:collapse; margin-bottom:20px;">
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <td style="padding: 10px 0; color:#94a3b8;">Patient Name</td>
                        <td style="padding: 10px 0; text-align:right; font-weight:600; color:#f8fafc;">{patient_name}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <td style="padding: 10px 0; color:#94a3b8;">Age / Gender</td>
                        <td style="padding: 10px 0; text-align:right; font-weight:600; color:#f8fafc;">{age} yrs / {gender}</td>
                    </tr>
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                        <td style="padding: 10px 0; color:#94a3b8;">Asymmetry Score</td>
                        <td style="padding: 10px 0; text-align:right; font-weight:700; color:#38bdf8;">{score:.4f}</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 0; color:#94a3b8;">Severity Classification</td>
                        <td style="padding: 10px 0; text-align:right; font-weight:600; color:{badge_color};">{severity}</td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

            # Download Action Button
            if os.path.exists("reports/final_medical_report.pdf"):
                with open("reports/final_medical_report.pdf", "rb") as f:
                    st.download_button(
                        label="📄 Download Medical Report (PDF)",
                        data=f,
                        file_name=f"Report_{patient_name.replace(' ', '_')}.pdf",
                        mime="application/pdf"
                    )

        with col_res2:
    st.markdown("### <i class='fa-solid fa-eye' style='color:#38bdf8;'></i> Computer Vision Output", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["U-Net Segmentation Overlay", "Original Patient Photo"])

    with tab1:
        st.image(
            overlay_path,
            caption="U-Net Facial Muscle Segmentation Overlay",
            width=700
        )

    with tab2:
        st.image(
            original_path,
            caption="Uploaded Original Face Image",
            width=700
        )