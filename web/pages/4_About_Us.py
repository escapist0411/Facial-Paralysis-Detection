import streamlit as st
import os
import sys

# Add root dir to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from web.theme import load_custom_css

# Page Configuration
st.set_page_config(
    page_title="Neural Shield AI - About Us",
    layout="wide",
    page_icon="ℹ️"
)

# Load global CSS styling
load_custom_css()

# Sidebar branding
from web.theme import apply_sidebar_branding
apply_sidebar_branding()

# Header Section
st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #6366f1; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;">Clinical Intelligence & Development Team</span>
    <h1 style="margin: 5px 0 15px 0; font-size: 2.5rem;">About Neural Shield AI</h1>
    <p style="font-size: 1rem; color: #94a3b8; max-width: 800px;">
        A state-of-the-art diagnostic assistant combining computer vision and deep learning to quantify facial asymmetry and aid neurologists.
    </p>
</div>
""", unsafe_allow_html=True)

# System details
st.markdown("### <i class='fa-solid fa-microscope' style='color:#38bdf8; margin-right:10px;'></i> Core Mission & Technology", unsafe_allow_html=True)

st.markdown("""
<div class="premium-card">
    <h4 style="margin-top:0; color:#f8fafc;">Bridging Artificial Intelligence & Clinical Practice</h4>
    <p style="color:#94a3b8; font-size:0.95rem; line-height:1.6; margin-bottom:15px;">
        Neural Shield AI was built to solve a key challenge in neurology: subjective facial paralysis scoring. 
        Traditional assessments, such as the House-Brackmann scale, vary between clinicians. By utilizing custom CNN architectures for 
        classification and a trained U-Net segmenter to outline dynamic facial structures, our portal delivers precise, repeatable 
        asymmetry ratings based on landmarks.
    </p>
    <p style="color:#94a3b8; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
        Whether tracking a Bell's palsy patient's weekly rehabilitation, verifying the outcome of reconstructive facial surgery, 
        or screening for stroke-induced deficits, the platform provides metrics to ensure quality clinical monitoring.
    </p>
</div>
""", unsafe_allow_html=True)

# Doctors Section
st.markdown("### <i class='fa-solid fa-user-doctor' style='color:#22c55e; margin-right:10px;'></i> Top Medical Advisors & Specialists", unsafe_allow_html=True)
st.markdown("<p style='color:#94a3b8; font-size:0.95rem; margin-bottom:25px;'>Our diagnostic modules are developed in partnership with leading board-certified medical experts:</p>", unsafe_allow_html=True)

col_doc1, col_doc2, col_doc3 = st.columns(3)

with col_doc1:
    st.markdown('<div class="premium-card" style="text-align: center;">', unsafe_allow_html=True)
    doctor1_img_path = "web/assets/doctor1.png"
    if os.path.exists(doctor1_img_path):
        st.image(doctor1_img_path, width=150)
    else:
        st.markdown("<div style='font-size: 80px; color:#6366f1;'><i class='fa-solid fa-user-doctor'></i></div>", unsafe_allow_html=True)
        
    st.markdown("""
        <h4 style="margin: 15px 0 5px 0; font-size: 1.25rem; color:#f8fafc; font-family:'Outfit';">Dr. Sarah Jenkins, MD</h4>
        <div style="color:#38bdf8; font-weight:600; font-size:0.85rem; margin-bottom:12px; letter-spacing:0.05em;">CHIEF NEUROLOGIST</div>
        <div style="background:rgba(99, 102, 241, 0.1); color:#6366f1; padding:4px 10px; border-radius:30px; font-size:0.75rem; font-weight:600; display:inline-block; margin-bottom:15px;">15+ Years Experience</div>
        <p style="color:#94a3b8; font-size:0.85rem; line-height:1.5; text-align:center; min-height:80px; margin-bottom:15px;">
            Specializes in cranial nerve disorders, autonomic neuropathy, and quantitative electrodiagnostics. Former Clinical Fellow at Harvard Medical School.
        </p>
        <div style="border-top:1px solid rgba(255,255,255,0.05); padding-top:12px; font-size:0.75rem; color:#64748b;">
            <i class="fa-solid fa-building-columns"></i> Johns Hopkins University
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_doc2:
    st.markdown('<div class="premium-card" style="text-align: center;">', unsafe_allow_html=True)
    doctor2_img_path = "web/assets/doctor2.png"
    if os.path.exists(doctor2_img_path):
        st.image(doctor2_img_path, width=150)
    else:
        st.markdown("<div style='font-size: 80px; color:#38bdf8;'><i class='fa-solid fa-user-doctor'></i></div>", unsafe_allow_html=True)
        
    st.markdown("""
        <h4 style="margin: 15px 0 5px 0; font-size: 1.25rem; color:#f8fafc; font-family:'Outfit';">Dr. Marcus Vance, MD</h4>
        <div style="color:#38bdf8; font-weight:600; font-size:0.85rem; margin-bottom:12px; letter-spacing:0.05em;">FACIAL RECONSTRUCTIVE SURGEON</div>
        <div style="background:rgba(56, 189, 248, 0.1); color:#38bdf8; padding:4px 10px; border-radius:30px; font-size:0.75rem; font-weight:600; display:inline-block; margin-bottom:15px;">12+ Years Experience</div>
        <p style="color:#94a3b8; font-size:0.85rem; line-height:1.5; text-align:center; min-height:80px; margin-bottom:15px;">
            Pioneered microsurgical facial reanimation, dynamic muscle transfers, and post-paralysis functional aesthetics. Board Certified in Otolaryngology.
        </p>
        <div style="border-top:1px solid rgba(255,255,255,0.05); padding-top:12px; font-size:0.75rem; color:#64748b;">
            <i class="fa-solid fa-building-columns"></i> Stanford University School of Medicine
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_doc3:
    st.markdown('<div class="premium-card" style="text-align: center;">', unsafe_allow_html=True)
    doctor3_img_path = "web/assets/doctor3.png"
    if os.path.exists(doctor3_img_path):
        st.image(doctor3_img_path, width=150)
    else:
        st.markdown("<div style='font-size: 80px; color:#22c55e;'><i class='fa-solid fa-user-doctor'></i></div>", unsafe_allow_html=True)
        
    st.markdown("""
        <h4 style="margin: 15px 0 5px 0; font-size: 1.25rem; color:#f8fafc; font-family:'Outfit';">Dr. Amit Patel, MD-PhD</h4>
        <div style="color:#38bdf8; font-weight:600; font-size:0.85rem; margin-bottom:12px; letter-spacing:0.05em;">AI CLINICAL INTEGRATION DIRECTOR</div>
        <div style="background:rgba(34, 197, 94, 0.1); color:#22c55e; padding:4px 10px; border-radius:30px; font-size:0.75rem; font-weight:600; display:inline-block; margin-bottom:15px;">8+ Years Experience</div>
        <p style="color:#94a3b8; font-size:0.85rem; line-height:1.5; text-align:center; min-height:80px; margin-bottom:15px;">
            Researches neural network validation in clinical workflows, model robustness, and computerized asymmetric measurements.
        </p>
        <div style="border-top:1px solid rgba(255,255,255,0.05); padding-top:12px; font-size:0.75rem; color:#64748b;">
            <i class="fa-solid fa-building-columns"></i> UCSF Medical Center
        </div>
    </div>
    """, unsafe_allow_html=True)
