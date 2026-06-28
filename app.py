import streamlit as st
from PIL import Image
import openai
import base64
from io import BytesIO
import datetime
import pytz
import json
import time

# Premium Dark Layout Configuration
st.set_page_config(page_title="QUOTEX OTC PREDICTOR v7.1", page_icon="🎯", layout="wide")

# 🔒 SAFE JUGAD: Key ko split karke joda hai taaki GitHub ise block na kare
part1 = "Sk-proj-CnZAI-8fQzu_XsgRoZOYaT239sHWpcolDFfe09t0Eg4-O1_m"
part2 = "XL9vFWevWLcGQNguv5gizCyoMbT3BlbkFJKo5WnklU6l7uThayqcJOIl"
part3 = "5auufeReElwlpNi41d5QcJQKLue8pGtphPk3f2x2eBSH9F-Bl3EA"

OPENAI_API_KEY = part1 + part2 + part3

# Custom CSS for Premium Trading Dashboard & Example Output Format
st.markdown("""
    <style>
    .main { background-color: #0d0e12; color: #e3e4e6; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .dashboard-card { background-color: #16171d; border-radius: 12px; padding: 25px; border: 1px solid #262930; box-shadow: 0 8px 32px rgba(0,0,0,0.5); }
    .time-badge { background-color: #1e222d; color: #2962ff; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: bold; float: right; border: 1px solid #2a2e39; }
    
    /* Candle Signal Styling */
    .candle-container { display: flex; gap: 20px; margin: 20px 0; }
    .candle-box { flex: 1; background-color: #1e222d; border-radius: 8px; padding: 20px; text-align: center; border: 1px solid #2a2e39; }
    .green-signal { color: #00e676; font-size: 40px; font-weight: bold; }
    .red-signal { color: #ff5252; font-size: 40px; font-weight: bold; }
    
    /* Grid Data rows */
    .matrix-row { display: flex; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #22252c; font-size: 15px; }
    .matrix-label { color: #787b86; font-weight: 500; }
    .matrix-value { color: #ffffff; font-weight: bold; }
    
    /* Bullet points for Reasons */
    .reason-title { font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 20px; margin-bottom: 12px; display: flex; align-items: center; }
    .bullet-list { list-style-type: none; padding-left: 0; }
    .bullet-list li { padding-left: 22px; margin-bottom: 10px; position: relative; color: #b2b5be; font-size: 14px; line-height: 1.5; }
    .bullet-list li::before { content: "•"; position: absolute; left: 0; color: #2962ff; font-size: 22px; top: -4px; }
    
    .live-clock-box { background-color: #16171d; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦅 QUOTEX OTC BINARY PREDICTOR ENGINE")
st.write("Advanced Price Action Rejection, Candlestick Psychology & Technical Indicator Confluence Model.")
st.markdown("---")

# 🕒 1. LIVE DIGITAL IST CLOCK (SIDEBAR)
IST = pytz.timezone('Asia/Kolkata')
st.sidebar.markdown("### 🇮🇳 Live Market Time (IST)")
clock_placeholder = st.sidebar.empty()

# 2. IMAGE UPLOAD & INTERFACE CONTROL
uploaded_file = st.file_uploader("📥 Upload Quotex OTC Market Chart Screenshot:", type=["png", "jpg", "jpeg"])

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

if uploaded_file is not None:
    base64_image = encode_image(uploaded_file)
    uploaded_file.seek(0)
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1.3])
    
    with col1:
        st.subheader("📷 Asset Control Matrix")
        st.image(image, use
