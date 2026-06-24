import streamlit as st
import numpy as np

# Page configuration for premium dark trading dashboard
st.set_page_config(page_title="AI OTC Predictor Pro", page_icon="📈", layout="centered")

# Premium Custom CSS for Dark UI
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stButton > button:first-child {
        background-color: #00ffcc; color: #000000; font-weight: bold;
        border-radius: 8px; width: 100%; border: none; height: 50px; font-size: 18px;
    }
    div.stButton > button:first-child:hover { background-color: #00cc99; color: #ffffff; }
    .metric-box {
        background-color: #1f2937; padding: 20px; border-radius: 12px;
        border: 1px solid #374151; text-align: center; margin-bottom: 10px;
    }
    .result-box-call {
        background-color: #064e3b; border: 2px solid #10b981; padding: 25px;
        border-radius: 12px; text-align: center; color: #34d399; font-size: 24px; font-weight: bold;
    }
    .result-box-put {
        background-color: #7f1d1d; border: 2px solid #ef4444; padding: 25px;
        border-radius: 12px; text-align: center; color: #f87171; font-size:
