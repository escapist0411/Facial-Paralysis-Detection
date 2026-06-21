import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Add root dir to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from web.theme import load_custom_css

# Page Configuration
st.set_page_config(
    page_title="Neural Shield AI - Clinical Dashboard",
    layout="wide",
    page_icon="📊"
)

# Load global CSS styling
load_custom_css()

# Sidebar branding
from web.theme import apply_sidebar_branding
apply_sidebar_branding()

# Header Section
st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #38bdf8; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;">Realtime Statistics & Metrics</span>
    <h1 style="margin: 5px 0 15px 0; font-size: 2.5rem;">Clinical Analytics Dashboard</h1>
    <p style="font-size: 1rem; color: #94a3b8; max-width: 800px;">
        Monitor AI performance indices, segmentation quality, and patient queue metrics in real-time.
    </p>
</div>
""", unsafe_allow_html=True)

# Metric Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Classifier Accuracy", "96.6%", delta="0.4%")

with col2:
    st.metric("U-Net Mean IoU", "0.912", delta="0.015")

with col3:
    st.metric("Total Cases Run", "342", delta="12 today")

with col4:
    st.metric("Avg. Scan Time", "1.4s", delta="-0.2s")

st.markdown("<br>", unsafe_allow_html=True)

# Main Grid: Charts & Performance
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### <i class=\"fa-solid fa-chart-simple\" style=\"color: #6366f1; margin-right: 10px;\"></i> Case Severity Distribution", unsafe_allow_html=True)
    
    # Generate dummy data for chart
    severity_data = pd.DataFrame({
        'Severity Level': ['Normal / Symm.', 'Mild Asymm.', 'Moderate Palsy', 'Severe Palsy'],
        'Cases': [112, 145, 63, 22]
    }).set_index('Severity Level')
    
    st.bar_chart(severity_data, color="#6366f1")
    
    st.markdown("""
    <div style="font-size:0.8rem; color:#64748b; margin-top:-10px; text-align:center;">
        Fig 1: Number of scanned patients grouped by House-Brackmann equivalence.
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("### <i class=\"fa-solid fa-square-poll-vertical\" style=\"color: #38bdf8; margin-right: 10px;\"></i> AI Confidence & Calibration", unsafe_allow_html=True)
    
    # Generate line chart data
    chart_data = pd.DataFrame(
        np.random.normal(0.966, 0.012, size=(30, 2)),
        columns=['CNN Classif.', 'U-Net Segm.']
    )
    
    st.line_chart(chart_data, color=["#6366f1", "#38bdf8"])
    
    st.markdown("""
    <div style="font-size:0.8rem; color:#64748b; margin-top:-10px; text-align:center;">
        Fig 2: Rolling 30-day confidence tracking for clinical segmentation and classification models.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Patient Queue Table
st.markdown("### <i class=\"fa-solid fa-users-viewfinder\" style=\"color: #22c55e; margin-right: 10px;\"></i> Recent Patient Queue", unsafe_allow_html=True)

# Create dummy table data
patient_queue = pd.DataFrame([
    {"ID": "FP-8490", "Name": "Alice Johnson", "Age": 42, "Gender": "Female", "Asymmetry Score": "0.14", "Diagnosis": "Normal", "Severity": "None", "Status": "Completed"},
    {"ID": "FP-3211", "Name": "Marcus Sterling", "Age": 58, "Gender": "Male", "Asymmetry Score": "0.38", "Diagnosis": "Facial Paralysis", "Severity": "Moderate", "Status": "Completed"},
    {"ID": "FP-1289", "Name": "Elena Rostova", "Age": 29, "Gender": "Female", "Asymmetry Score": "0.62", "Diagnosis": "Facial Paralysis", "Severity": "Severe", "Status": "Completed"},
    {"ID": "FP-7422", "Name": "Devon Miller", "Age": 63, "Gender": "Male", "Asymmetry Score": "0.08", "Diagnosis": "Normal", "Severity": "None", "Status": "Completed"},
    {"ID": "FP-4122", "Name": "Siddharth Rao", "Age": 37, "Gender": "Male", "Asymmetry Score": "0.22", "Diagnosis": "Facial Paralysis", "Severity": "Mild", "Status": "Completed"},
    {"ID": "FP-9304", "Name": "Sofia Martinez", "Age": 51, "Gender": "Female", "Asymmetry Score": "0.41", "Diagnosis": "Facial Paralysis", "Severity": "Moderate", "Status": "Completed"}
])

# Search bar
search_query = st.text_input("🔍 Search patient queue by Name or ID:")
if search_query:
    filtered_df = patient_queue[
        patient_queue['Name'].str.contains(search_query, case=False) | 
        patient_queue['ID'].str.contains(search_query, case=False)
    ]
else:
    filtered_df = patient_queue

# Style table
st.dataframe(

    filtered_df,

    hide_index=True

)

st.markdown("""
<div style="background: rgba(31, 41, 55, 0.3); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 15px; margin-top:20px;">
    <h5 style="color:#f8fafc; margin-top:0;"><i class="fa-solid fa-circle-info" style="color:#38bdf8; margin-right:8px;"></i> Clinical Interpretation Protocol</h5>
    <ul style="color:#94a3b8; font-size:0.9rem; margin-bottom:0; line-height:1.5;">
        <li><strong>Asymmetry Score < 0.15:</strong> Indicative of physiological baseline symmetry. Classified as Normal.</li>
        <li><strong>Asymmetry Score 0.15 - 0.30:</strong> Mild palsy. Often represents recovering bell's palsy or minor facial asymmetry.</li>
        <li><strong>Asymmetry Score 0.30 - 0.50:</strong> Moderate facial paralysis. Evident resting asymmetry with functional limitation.</li>
        <li><strong>Asymmetry Score > 0.50:</strong> Severe facial paralysis. Pronounced resting asymmetry with complete loss of muscular tone on one side.</li>
    </ul>
</div>
""", unsafe_allow_html=True)
