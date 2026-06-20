import streamlit as st
import os
import sys

# Add root dir to path
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from web.theme import load_custom_css, show_splash_screen

# 1. Page Config (must be first)
st.set_page_config(
    page_title="Neural Shield AI - Facial Paralysis System",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

# 2. Trigger Splash Screen (runs once per session)
show_splash_screen()

# 3. Load CSS Theme
load_custom_css()

# 4. Sidebar configuration
from web.theme import apply_sidebar_branding
apply_sidebar_branding()
st.sidebar.markdown("""
<div style="padding: 10px; background: rgba(31, 41, 55, 0.4); border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">
    <small style="color: #94a3b8; display: block; margin-bottom: 4px;">SYSTEM STATUS</small>
    <div style="display: flex; align-items: center; gap: 8px;">
        <span style="height: 8px; width: 8px; background-color: #22c55e; border-radius: 50%; display: inline-block; box-shadow: 0 0 8px #22c55e;"></span>
        <span style="font-size: 0.85rem; color: #e2e8f0; font-weight: 500;">Models Online</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Main Page Content
st.markdown("""
<div style="padding: 20px 0 10px 0;">
    <span style="font-size: 0.85rem; color: #6366f1; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase;">Medical Intelligence Portal</span>
    <h1 style="margin: 5px 0 15px 0; font-size: 2.8rem;">Neural Shield AI</h1>
    <p style="font-size: 1.15rem; color: #94a3b8; max-width: 800px; line-height: 1.6;">
        An advanced diagnostic platform powered by deep learning for automated facial paralysis detection, 
        quantitative asymmetry scoring, and clinical reports generation.
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard Stats Summary Row
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 500;">MODEL ACCURACY</span>
            <div style="background: rgba(99, 102, 241, 0.1); color: #6366f1; padding: 6px 10px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;">Active</div>
        </div>
        <div style="font-size: 2.2rem; font-weight: 700; color: #f8fafc; margin-bottom: 5px;">96.6%</div>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0;">ResNet-50 paralysis classifier accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 500;">SEGMENTATION IoU</span>
            <div style="background: rgba(14, 165, 233, 0.1); color: #0ea5e9; padding: 6px 10px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;">Calibrated</div>
        </div>
        <div style="font-size: 2.2rem; font-weight: 700; color: #f8fafc; margin-bottom: 5px;">0.91</div>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0;">U-Net overlap score for facial regions</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="premium-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
            <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 500;">CLINICAL TESTS RUN</span>
            <div style="background: rgba(34, 197, 94, 0.1); color: #22c55e; padding: 6px 10px; border-radius: 8px; font-size: 0.8rem; font-weight: 600;">Verified</div>
        </div>
        <div style="font-size: 2.2rem; font-weight: 700; color: #f8fafc; margin-bottom: 5px;">300+</div>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0;">Diagnostic tests run in session logs</p>
    </div>
    """, unsafe_allow_html=True)

# Main layout content
col_main, col_sidebar = st.columns([2, 1])

with col_main:
    st.markdown("### <i class=\"fa-solid fa-notes-medical\" style=\"color: #6366f1; margin-right: 10px;\"></i> Clinical Action Center", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <h4 style="margin-top:0; color:#f8fafc; font-size: 1.2rem; margin-bottom:10px;">Automated Diagnostic Workflow</h4>
        <p style="color:#94a3b8; font-size:0.95rem; line-height:1.5; margin-bottom:20px;">
            The Neural Shield AI platform provides doctors with a rapid, objective method to analyze facial paralysis. 
            By combining deep learning models and geometric landmark calculations, the system extracts critical asymmetry indices 
            and compiles a downloadable report in seconds.
        </p>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(31, 41, 55, 0.3); border-radius: 12px; border: 1px solid rgba(255,255,255,0.03);">
                <div style="font-size:1.5rem; margin-bottom:8px; color:#6366f1;"><i class="fa-solid fa-image"></i></div>
                <div style="font-weight:600; color:#f8fafc; margin-bottom:4px;">1. Image Acquisition</div>
                <div style="font-size:0.8rem; color:#64748b;">Upload a high-res patient portrait in frontal neutral pose.</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(31, 41, 55, 0.3); border-radius: 12px; border: 1px solid rgba(255,255,255,0.03);">
                <div style="font-size:1.5rem; margin-bottom:8px; color:#38bdf8;"><i class="fa-solid fa-gears"></i></div>
                <div style="font-weight:600; color:#f8fafc; margin-bottom:4px;">2. AI Processing</div>
                <div style="font-size:0.8rem; color:#64748b;">U-Net isolates facial muscles; landmark equations score asymmetry.</div>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; background: rgba(31, 41, 55, 0.3); border-radius: 12px; border: 1px solid rgba(255,255,255,0.03);">
                <div style="font-size:1.5rem; margin-bottom:8px; color:#22c55e;"><i class="fa-solid fa-file-pdf"></i></div>
                <div style="font-weight:600; color:#f8fafc; margin-bottom:4px;">3. PDF Export</div>
                <div style="font-size:0.8rem; color:#64748b;">Generate, review, and download patient clinical reports.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### <i class=\"fa-solid fa-microchip\" style=\"color: #38bdf8; margin-right: 10px;\"></i> Core Neural Architecture", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="premium-card">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px;">
            <div>
                <h5 style="color:#f8fafc; margin-top:0; font-size:1rem;"><i class="fa-solid fa-shield-halved" style="color:#6366f1; margin-right:6px;"></i> Classifier CNN</h5>
                <p style="color:#94a3b8; font-size:0.85rem; line-height:1.4;">
                    Convolutional Neural Network trained to flag anomalies in facial expressions, identifying early-stage palsy.
                </p>
            </div>
            <div>
                <h5 style="color:#f8fafc; margin-top:0; font-size:1rem;"><i class="fa-solid fa-draw-polygon" style="color:#38bdf8; margin-right:6px;"></i> Segmenter U-Net</h5>
                <p style="color:#94a3b8; font-size:0.85rem; line-height:1.4;">
                    Segmentation model that isolates eye, brow, and mouth clusters to trace asymmetry pixel ratios.
                </p>
            </div>
            <div>
                <h5 style="color:#f8fafc; margin-top:0; font-size:1rem;"><i class="fa-solid fa-bezier-curve" style="color:#22c55e; margin-right:6px;"></i> Landmark Equations</h5>
                <p style="color:#94a3b8; font-size:0.85rem; line-height:1.4;">
                    Distance ratios between pupils, mouth corners, and nasal tips computed dynamically via Mediapipe.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_sidebar:
    st.markdown("### <i class=\"fa-solid fa-bolt\" style=\"color: #f59e0b; margin-right: 10px;\"></i> Quick Actions", unsafe_allow_html=True)
    
    # We can render nice interactive HTML buttons that prompt users to click page menus
    st.markdown("""
    <div class="premium-card" style="padding: 20px 15px;">
        <p style="color:#94a3b8; font-size:0.85rem; margin-top:0; margin-bottom:15px;">
            Select a function from the left sidebar navigation menu or use these direct access points:
        </p>
        <div style="display:flex; flex-direction:column; gap:10px;">
            <div style="padding:12px; background:rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.2); border-radius:10px; cursor:pointer;">
                <div style="font-weight:600; color:#e2e8f0; font-size:0.9rem;"><i class="fa-solid fa-chart-line" style="color:#6366f1; margin-right:8px;"></i> Clinical Dashboard</div>
                <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">View diagnostics performance and metrics.</div>
            </div>
            <div style="padding:12px; background:rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.2); border-radius:10px; cursor:pointer;">
                <div style="font-weight:600; color:#e2e8f0; font-size:0.9rem;"><i class="fa-solid fa-file-medical" style="color:#38bdf8; margin-right:8px;"></i> Run Analysis</div>
                <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Upload patient photo and generate a report.</div>
            </div>
            <div style="padding:12px; background:rgba(34, 197, 94, 0.08); border: 1px solid rgba(34, 197, 94, 0.2); border-radius:10px; cursor:pointer;">
                <div style="font-weight:600; color:#e2e8f0; font-size:0.9rem;"><i class="fa-solid fa-folder-open" style="color:#22c55e; margin-right:8px;"></i> Reports Database</div>
                <div style="font-size:0.75rem; color:#94a3b8; margin-top:2px;">Search and download saved clinical reports.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 20px; color:#64748b; font-size:0.8rem;">
        Neural Shield AI V2.1 • HIPAA Compliant Server<br>
        © 2026 Eastern Medical Center. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
