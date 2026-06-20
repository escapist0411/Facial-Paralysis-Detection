import streamlit as st
import time
import os

def load_custom_css():
    # Load fonts
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)
    
    # Read assets/styles.css if it exists
    css_content = ""
    css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css_content = f.read()
            
    # Inject styling
    st.markdown(f"""
    <style>
    {css_content}
    
    /* Premium overrides */
    html, body, [data-testid="stAppViewContainer"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #0b111e;
        background-image: radial-gradient(circle at 10% 20%, rgba(16, 37, 76, 0.4) 0%, rgba(11, 17, 30, 0.1) 90.1%);
        color: #e2e8f0;
    }}
    
    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
    }}
    
    [data-testid="stHeader"] {{
        background: rgba(11, 17, 30, 0.5) !important;
        backdrop-filter: blur(8px);
    }}
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #090d16 0%, #111827 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }}
    
    [data-testid="stSidebar"] * {{
        color: #94a3b8 !important;
    }}
    
    [data-testid="stSidebar"] .active {{
        background-color: rgba(99, 102, 241, 0.1) !important;
        border-left: 3px solid #6366f1;
    }}
    
    /* Card Styles */
    .premium-card {{
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 20px;
    }}
    
    .premium-card:hover {{
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.2);
    }}
    
    /* Custom button styling */
    .stButton > button {{
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 28px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.4) !important;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(99, 102, 241, 0.6) !important;
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%) !important;
    }}
    
    /* Metrics custom container */
    div[data-testid="metric-container"] {{
        background: rgba(31, 41, 55, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 16px;
        box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
    }}
    
    div[data-testid="stMetricValue"] {{
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        color: #38bdf8 !important;
    }}
    
    /* Splash screen styling */
    .splash-container {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 80vh;
        text-align: center;
    }}
    
    .splash-logo {{
        font-size: 80px;
        margin-bottom: 20px;
        animation: pulse 2s infinite ease-in-out;
    }}
    
    @keyframes pulse {{
        0% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.4)); }}
        50% {{ transform: scale(1.05); filter: drop-shadow(0 0 25px rgba(56, 189, 248, 0.8)); }}
        100% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.4)); }}
    }}
    
    .splash-title {{
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }}
    
    .splash-subtitle {{
        font-size: 1.25rem;
        color: #94a3b8;
        max-width: 600px;
        margin-bottom: 40px;
    }}
    
    .loader-bar-container {{
        width: 300px;
        height: 6px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 15px;
    }}
    
    .loader-bar {{
        height: 100%;
        width: 0%;
        background: linear-gradient(90deg, #6366f1, #38bdf8);
        animation: fillProgress 3s forwards ease-in-out;
    }}
    
    @keyframes fillProgress {{
        0% {{ width: 0%; }}
        20% {{ width: 15%; }}
        40% {{ width: 45%; }}
        75% {{ width: 85%; }}
        100% {{ width: 100%; }}
    }}
    
    .loading-status {{
        font-size: 0.85rem;
        color: #64748b;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }}
    
    /* Doctor Card */
    .doctor-card {{
        background: rgba(31, 41, 55, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: all 0.3s ease;
    }}
    
    .doctor-card:hover {{
        border-color: rgba(56, 189, 248, 0.3);
        transform: translateY(-2px);
    }}
    
    .doctor-img {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        margin: 0 auto 15px auto;
        border: 3px solid #6366f1;
    }}
    
    .doctor-name {{
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 1.15rem;
        color: #f8fafc;
        margin-bottom: 4px;
    }}
    
    .doctor-role {{
        font-size: 0.85rem;
        color: #38bdf8;
        font-weight: 500;
        margin-bottom: 10px;
    }}
    
    .doctor-exp {{
        font-size: 0.8rem;
        color: #94a3b8;
    }}
    </style>
    """, unsafe_allow_html=True)

def apply_sidebar_branding():
    st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="font-family: 'Outfit', sans-serif; color: #f8fafc; font-weight: 600; font-size: 1.5rem; letter-spacing: 1px;">
            <i class="fa-solid fa-stethoscope" style="color: #38bdf8; margin-right: 8px;"></i>
            Neural Shield
        </h2>
        <hr style="border-color: #334155; margin-top: 10px; margin-bottom: 0px;">
    </div>
    """, unsafe_allow_html=True)

def show_splash_screen():
    # If already loaded in this session, skip
    if "splash_loaded" in st.session_state and st.session_state.splash_loaded:
        return True
        
    st.session_state.splash_loaded = False
    
    # Render splash container
    splash_placeholder = st.empty()
    
    with splash_placeholder.container():
        st.markdown("""
        <div class="splash-container">
            <div class="splash-logo"><i class="fa-solid fa-brain-circuit" style="color: #6366f1;"></i></div>
            <div class="splash-title">NEURAL SHIELD AI</div>
            <div class="splash-subtitle">Next-Generation Clinical System for Facial Paralysis Diagnostics & Analysis</div>
            <div class="loader-bar-container">
                <div class="loader-bar"></div>
            </div>
            <div id="status-text" class="loading-status">Initializing System...</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate loading steps
        status_updates = [
            "Initializing deep learning frameworks...",
            "Loading CNN classification weights...",
            "Loading U-Net facial segmentation masks...",
            "Setting up clinical interface...",
            "Ready!"
        ]
        
        time_step = 0.5
        for status in status_updates:
            time.sleep(time_step)
            st.markdown(f"""
            <script>
            document.querySelector('.loading-status').innerText = "{status}";
            </script>
            """, unsafe_allow_html=True)
            
    # Mark as loaded and rerun
    st.session_state.splash_loaded = True
    splash_placeholder.empty()
    st.rerun()
