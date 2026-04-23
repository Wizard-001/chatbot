import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

# Page configuration
st.set_page_config(
    page_title="Nexus AI | Mistral",
    page_icon="🌌",
    layout="wide",
)

# Advanced CSS for a high-fidelity, futuristic look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');

    :root {
        --primary: #8b5cf6;
        --secondary: #a855f7;
        --accent: #d946ef;
        --bg-dark: #0f0720;
    }

    /* Global Overrides */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1e1033 0%, #0f0720 100%);
        font-family: 'Inter', sans-serif;
        color: #f8fafc;
    }

    /* Animated background effect */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: 
            radial-gradient(circle at 20% 30%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(217, 70, 239, 0.08) 0%, transparent 50%);
        z-index: -1;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(2, 6, 23, 0.8) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Chat Message Styles */
    .stChatMessage {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border-radius: 24px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        margin-bottom: 20px !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        padding: 1.5rem !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .stChatMessage:hover {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 8px 30px rgba(99, 102, 241, 0.1);
        transform: scale(1.01);
    }

    /* Custom Header Design */
    .main-title {
        background: linear-gradient(to right, #a78bfa, #c084fc, #d946ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin-bottom: 0.5rem;
        filter: drop-shadow(0 4px 10px rgba(168, 85, 247, 0.3));
    }

    /* Global cursor pointer for all interactive elements */
    button, 
    [role="button"], 
    [data-testid="stSelectbox"], 
    [data-baseweb="select"], 
    .stSlider,
    .stSelectbox,
    .stButton,
    .stChatInputContainer textarea {
        cursor: pointer !important;
    }

    /* Selectbox Pointer & Fixes */
    [data-testid="stSelectbox"] * {
        cursor: pointer !important;
    }
    [data-testid="stSelectbox"] input {
        cursor: pointer !important;
        caret-color: transparent !important;
        pointer-events: none !important;
    }

    /* Pulse animation for status */
    @keyframes pulse {
        0% { transform: scale(0.95); opacity: 0.5; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.5; }
    }
    .status-dot {
        height: 10px; width: 10px;
        background-color: #22c55e;
        border-radius: 50%;
        display: inline-block;
        margin-right: 8px;
        animation: pulse 2s infinite ease-in-out;
        box-shadow: 0 0 10px #22c55e;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(168, 85, 247, 0.3);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover { background: rgba(168, 85, 247, 0.5); }

    /* Button Styling */
    .stButton>button {
        border-radius: 12px !important;
        background: linear-gradient(135deg, #8b5cf6 0%, #d946ef 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Application Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar Content
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #818cf8;'>Nexus AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.7; font-size: 0.9rem;'>Next-Gen Intelligent Interface</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # System Status
    st.markdown(f"<div><span class='status-dot'></span><span style='font-size: 0.8rem; font-weight: 600;'>System: Operational</span></div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Settings Container
    with st.expander("🛠️ Advanced Settings", expanded=True):
        persona = st.selectbox(
            "Intelligence Persona",
            ["Neutral 🧘", "Happy 😊", "Sad 😔", "Angry 😠", "Funny 🤡"],
            index=0
        )
        
        temperature = st.slider(
            "Creativity Engine",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1
        )

    # Session Stats
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("📊 Session Insights")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", len(st.session_state.messages))
    with col2:
        # Show truncated persona name
        st.metric("Persona", persona.split()[0])

    st.markdown("---")
    if st.button("🗑️ Purge Neural History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Layout
st.markdown("<h1 class='main-title'>Nexus Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6; margin-top: -10px;'>Harnessing Mistral LLM via LangChain Mesh</p>", unsafe_allow_html=True)

# Quick Prompts
if not st.session_state.messages:
    st.markdown("<br><br>", unsafe_allow_html=True)
    cols = st.columns(3)
    with cols[0]:
        if st.button("🚀 Explain Quantum Physics", use_container_width=True):
            st.session_state.messages.append(HumanMessage(content="Explain Quantum Physics in simple terms."))
            st.rerun()
    with cols[1]:
        if st.button("🎨 Write a Cyberpunk Poem", use_container_width=True):
            st.session_state.messages.append(HumanMessage(content="Write a short cyberpunk poem."))
            st.rerun()
    with cols[2]:
        if st.button("💡 Creative Idea for App", use_container_width=True):
            st.session_state.messages.append(HumanMessage(content="Give me a creative idea for a new mobile app."))
            st.rerun()

# Initialize model
@st.cache_resource
def get_model(temp):
    return ChatMistralAI(model='mistral-small-2506', temperature=temp)

try:
    model = get_model(temperature)
except Exception as e:
    st.error("Neural Interface offline. Check API connectivity.")
    st.stop()

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        avatar = "👤" if isinstance(message, HumanMessage) else "🤖"
        role = "user" if isinstance(message, HumanMessage) else "assistant"
        with st.chat_message(role, avatar=avatar):
            st.markdown(message.content)

# Logic to handle both Chat Input and Quick Prompts
persona_map = {
    "Neutral 🧘": "You are a neutral AI assistant.",
    "Happy 😊": "You are a happy and cheerful AI assistant. Use emojis and be very positive!",
    "Sad 😔": "You are a sad and melancholic AI assistant. You sound existential.",
    "Angry 😠": "You are an angry and grumpy AI assistant. You are easily annoyed.",
    "Funny 🤡": "You are a funny AI assistant. Tell jokes and use puns!"
}

# 1. Handle Chat Input
if prompt := st.chat_input("Inject prompt into neural stream..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.rerun()

# 2. Check if the last message needs a response (Handles Quick Prompts)
if st.session_state.messages and isinstance(st.session_state.messages[-1], HumanMessage):
    with chat_container:
        with st.chat_message("assistant", avatar="🤖"):
            response_container = st.empty()
            chat_messages = [SystemMessage(content=persona_map[persona])] + st.session_state.messages
            
            try:
                with st.spinner(" "):
                    response = model.invoke(chat_messages)
                    full_response = response.content
                
                # Streaming Simulation
                displayed_text = ""
                for char in full_response:
                    displayed_text += char
                    response_container.markdown(displayed_text + "▌")
                    time.sleep(0.003)
                
                response_container.markdown(full_response)
                st.session_state.messages.append(AIMessage(content=full_response))
                st.rerun()
            except Exception as e:
                st.error(f"Neural spike detected: {str(e)}")
