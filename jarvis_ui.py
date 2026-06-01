import streamlit as st
import os
from dotenv import load_dotenv
import voice_engine  # Custom voice framework import
import jarvis_agents  # Custom backend agent import

# Load environment credentials securely
load_dotenv(dotenv_path="private.env")
api_key = os.getenv("GROQ_API_KEY")

# Set up Streamlit Page configurations
st.set_page_config(page_title="J.A.R.V.I.S.", page_icon="🤖", layout="centered")

# --- FUTURISTIC SCI-FI DESIGN (CSS) ---
st.markdown(
    """
    <style>
    /* Dark Theme Core */
    .stApp {
        background-color: #03030a;
    }
    
    /* Custom Futuristic Status Typography */
    .status-text {
        color: #00f0ff;
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        text-align: center;
        margin-top: 20px;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
    }
    
    /* Sleek Capsule Input Custom Styling */
    .stTextInput div>div>input {
        background: linear-gradient(135deg, #09091e 0%, #03030a 100%) !important;
        border: 2px solid #1e1e3f !important;
        border-radius: 30px !important;
        color: #ffffff !important;
        padding: 15px 25px !important;
        text-align: center !important;
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.15) !important;
        font-size: 14px !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Neon Focus State for Input Capsule Bar */
    .stTextInput div>div>input:focus {
        border: 2px solid #ec4899 !important;
        box-shadow: 0 0 25px rgba(236, 72, 153, 0.4) !important;
    }

    /* Hide standard Streamlit header and footer clutter */
    header, footer {
        visibility: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Greet operator once upon application initialization
if "greeted" not in st.session_state:
    st.session_state.greeted = True
    voice_engine.speak("Hello badri sir chepandi?")

# Render Center Graphic Capsule Component
st.markdown("<div class='siri-wrapper'>", unsafe_allow_html=True)

# --- CORE BACKEND COORDINATOR WORKFLOW ---
def execute_stark_intelligence(query_string: str):
    if not api_key:
        st.error("CORE FAULT: GROQ_API_KEY CONTEXT UNRESOLVED.")
        return None
    
    # 1. Anchor a dynamic status block inside the webpage layout
    status_msg = st.empty()
    
    try:
        # 2. Render localized loading text string on screen 
        status_msg.markdown("<div class='status-text'>JARVIS IS SEARCHING THE SYSTEM CORE...</div>", unsafe_allow_html=True)
        
        # 3. Call your matching backend agent script execution function 
        output = jarvis_agents.run_autonomous_agent(query_string)
        
        # 4. Clear loading string and render the final verified AI answer on screen
        status_msg.markdown(f"<div class='status-text'>{output}</div>", unsafe_allow_html=True)
        
        # 5. Let your engine speak the response text out loud
        voice_engine.speak(output)
        return output
        
    except Exception as e:
        status_msg.markdown(f"<div class='status-text'>SYSTEM FAULT: {str(e)}</div>", unsafe_allow_html=True)
        return None

# --- THE 2040 MINIMALIST CONTROL INTERFACE ---

# 1. The Single Input Field (Styled perfectly by your neon CSS parameters)
user_typed = st.text_input("Terminal Command Input", placeholder="Type your command macro here, Sir...", label_visibility="collapsed")

# 2. Check for text interactions automatically upon pressing Enter
if user_typed:
    with st.spinner("Processing command matrix..."):
        execute_stark_intelligence(user_typed)

st.markdown("</div>", unsafe_allow_html=True)
