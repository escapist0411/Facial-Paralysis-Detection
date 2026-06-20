import streamlit as st
import os
import sys
import json
from datetime import datetime

# Add root dir to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from web.theme import load_custom_css

# Page Configuration
st.set_page_config(
    page_title="Neural Shield AI - Contact Us",
    layout="wide",
    page_icon="📞"
)

# Load global CSS styling
load_custom_css()

# Sidebar branding
from web.theme import apply_sidebar_branding
apply_sidebar_branding()

# Header Section
st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #6366f1; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;">Direct Assistance Hotline</span>
    <h1 style="margin: 5px 0 15px 0; font-size: 2.5rem;">Contact Clinical Operations</h1>
    <p style="font-size: 1rem; color: #94a3b8; max-width: 800px;">
        Reach out to our clinical technology team, research integration desk, or submit feedback regarding our diagnostic models.
    </p>
</div>
""", unsafe_allow_html=True)

# Main Grid layout
col_form, col_details = st.columns([1.5, 1])

with col_form:
    st.markdown("### <i class='fa-solid fa-paper-plane' style='color:#6366f1; margin-right:10px;'></i> Submit Integration Inquiry", unsafe_allow_html=True)
    
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Clinician Name", placeholder="e.g. Dr. Robert Chen")
        email = st.text_input("Professional Email Address", placeholder="e.g. r.chen@hospital.org")
        category = st.selectbox(
            "Department / Reason for Inquiry",
            [
                "Clinical Support & Troubleshooting",
                "EHR Integration Request",
                "Model Calibration & Research",
                "Reporting Anomalies / Bug Report",
                "General Partnership Inquiry"
            ]
        )
        message = st.text_area("Message Detail", height=150, placeholder="Explain your inquiry in detail...")
        
        st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Send Secure Message")
    st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        if not name or not email or not message:
            st.error("⚠️ Please fill in all fields (Name, Email, and Message) before sending.")
        elif "@" not in email:
            st.error("⚠️ Please enter a valid email address.")
        else:
            # Create a simple JSON log of inquiries for clinical audibility
            os.makedirs("reports/inquiries", exist_ok=True)
            inquiry_data = {
                "name": name,
                "email": email,
                "category": category,
                "message": message,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            log_filename = f"reports/inquiries/inquiry_{int(datetime.now().timestamp())}.json"
            with open(log_filename, "w") as f:
                json.dump(inquiry_data, f, indent=4)
                
            st.success("🎉 Secure message dispatched! Our integration representatives will contact you at your provided clinic address in 24 hours.")

with col_details:
    st.markdown("### <i class='fa-solid fa-hospital' style='color:#38bdf8; margin-right:10px;'></i> Medical Center Coordinates", unsafe_allow_html=True)
    
    st.markdown("""
<div class="premium-card">
<h4 style="margin-top:0; color:#f8fafc; font-size:1.15rem;"><i class="fa-solid fa-map-location-dot" style="color:#6366f1; margin-right:8px;"></i> Primary Facility</h4>
<p style="color:#94a3b8; font-size:0.9rem; line-height:1.5; margin-bottom:15px;">
Eastern Medical Diagnostic Center<br>
Neural Diagnostics Wing, Suite 500<br>
750 Medical Plaza Parkway<br>
Boston, MA 02111
</p>

<h4 style="color:#f8fafc; font-size:1.15rem; margin-top:20px;"><i class="fa-solid fa-phone" style="color:#38bdf8; margin-right:8px;"></i> Communication Directs</h4>
<p style="color:#94a3b8; font-size:0.9rem; line-height:1.5; margin-bottom:15px;">
<strong>Clinical Support Desk:</strong> +1 (555) 492-9010<br>
<strong>EHR Integration Hotline:</strong> +1 (555) 492-9012<br>
<strong>Research Inquiries:</strong> <a href="mailto:integrations@neuralshield.ai" style="color:#38bdf8; text-decoration:none;">integrations@neuralshield.ai</a>
</p>

<h4 style="color:#f8fafc; font-size:1.15rem; margin-top:20px;"><i class="fa-solid fa-clock" style="color:#22c55e; margin-right:8px;"></i> Service Availability</h4>
<p style="color:#94a3b8; font-size:0.9rem; line-height:1.5; margin-bottom:0;">
Monday - Friday: 08:00 AM - 06:00 PM EST<br>
Saturday - Sunday: Emergency On-Call Specialists Only
</p>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("""
<div class="premium-card" style="background: rgba(99, 102, 241, 0.05); border-color: rgba(99, 102, 241, 0.15);">
<h5 style="color:#f8fafc; margin-top:0; font-size:1rem;"><i class="fa-solid fa-shield-halved" style="color:#6366f1; margin-right:6px;"></i> HIPAA Data Protection Notice</h5>
<p style="color:#94a3b8; font-size:0.8rem; line-height:1.4; margin-bottom:0;">
All contact forms and communication vectors are TLS 1.3 encrypted. Do not send Patient Protected Health Information (PHI) 
directly through this form. Use our HL7/FHIR compliant secure channels for patient-specific data exchange.
</p>
</div>
""", unsafe_allow_html=True)
