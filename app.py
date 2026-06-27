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
st.set_page_config(page_title="CORE GPT-4o VISION v6.4", page_icon="📉", layout="wide")

# ✅ MAINE AAPKI API KEY YAHAN DIRECT SET KAR DI HAI TAAKI ERROR NA AAYE
OPENAI_API_KEY = "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"

# UI styling matching premium dark trading dashboard
st.markdown("""
    <style>
    .main { background-color: #111214; color: #e3e4e6; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    .dashboard-card { background-color: #1a1b1e; border-radius: 12px; padding: 24px; border: 1px solid #2a2b2f; box-shadow: 0 4px 20px rgba(0,0,0,0.4); }
    .time-badge { background-color: #262930; color: #5383ec; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: bold; float: right; }
    .bias-container { display: flex; gap: 15px; margin-bottom: 25px; margin-top: 15px; }
    .bias-box { flex: 1; background-color: #141517; border-radius: 8px; padding: 15px; text-align: center; border: 1px solid #222326; }
    .bullish-title { color: #2ebd85; font-size: 14px; font-weight: 500; }
    .bearish-title { color: #df4949; font-size: 14px; font-weight: 500; }
    .bullish-val { color: #2ebd85; font-size: 32px; font-weight: bold; margin-top: 5px; }
    .bearish-val { color: #df4949; font-size: 32px; font-weight: bold; margin-top: 5px; }
    .data-row { display: flex; justify-content: space-between; padding: 14px 0; border-bottom: 1px solid #222326; font-size: 15px; }
    .data-label { color: #8a8d93; }
    .data-value { font-weight: 500; color: #ffffff; }
    .trend-green { color: #2ebd85; font-weight: bold; }
    .trend-red { color: #df4949; font-weight: bold; }
    .conf-badge { color: #2ebd85; font-weight: bold; }
    .why-title { font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 20px; margin-bottom: 10px; }
    .custom-bullet { list-style-type: none; padding-left: 0; }
    .custom-bullet li { padding-left: 20px; margin-bottom: 8px; position: relative; color: #c2c4c9; font-size: 14px; }
    .custom-bullet li::before { content: "•"; position: absolute; left: 0; color: #5383ec; font-size: 18px; top: -2px; }
    .live-clock-box { background-color: #1a1b1e; border: 1px solid #ff4b4b; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 ADVANCED CHATGPT VISION MULTI-INDICATOR SCANNER")
st.write("Real-time Price Action + MACD + Stochastic Confluence Analysis with Live IST Clock.")
st.markdown("---")

# 🕒 1. LIVE REAL-TIME DIGITAL CLOCK IN SIDEBAR
IST = pytz.timezone('Asia/Kolkata')
st.sidebar.markdown("### 🇮🇳 Live India Time (IST)")
clock_placeholder = st.sidebar.empty()

# 2. FILE UPLOADER & CONTROLS
uploaded_file = st.file_uploader("📥 Drop chart screenshot here:", type=["png", "jpg", "jpeg"])

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

if uploaded_file is not None:
    base64_image = encode_image(uploaded_file)
    uploaded_file.seek(0)
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("📷 Control Matrix")
        st.image(image, use_container_width=True)
        
        all_pairs = [
            "NZD/CHF (OTC)", "USD/IDR (OTC)", "USD/BDT (OTC)", "USD/DZD (OTC)", 
            "AUD/NZD (OTC)", "USD/EGP (OTC)", "CAD/JPY", "USD/PKR (OTC)", 
            "EUR/USD", "GBP/NZD (OTC)", "USD/MXN (OTC)", "EUR/GBP", 
            "EUR/JPY", "AUD/JPY", "GBP/USD", "USD/PHP (OTC)", "NZD/CAD (OTC)",
            "GBP/CAD", "EUR/AUD", "USD/ARS (OTC)", "USD/ZAR (OTC)",
            "GBP/AUD", "GBP/JPY", "NZD/JPY (OTC)", "NZD/USD (OTC)",
            "AUD/USD", "AUD/CAD", "USD/COP (OTC)", "USD/INR (OTC)",
            "USD/NGN (OTC)", "EUR/CAD", "USD/JPY"
        ]
        selected_pair = st.selectbox("💱 Select Trade Asset:", sorted(all_pairs))
        target_time = st.text_input("🎯 Set Target Candle Time (with AM/PM):", value="01:40 AM")
        execute_btn = st.button("🚀 RUN CHATGPT PRICE ACTION ANALYSIS")
        
    with col2:
        st.subheader("🖥️ ChatGPT AI Output Matrix")
        
        if execute_btn:
            if not OPENAI_API_KEY:
                st.error("❌ API Key missing in code.")
            else:
                try:
                    client = openai.OpenAI(api_key=OPENAI_API_KEY)
                    
                    with st.spinner("ChatGPT is digitally projecting MACD & Stochastic values from candles..."):
                        
                        prompt = f"""
                        You are an expert quantitative trader and multi-modal neural vision network. 
                        Look at this chart image for {selected_pair}. 
                        
                        Even if MACD and Stochastic oscillators are not visually present at the bottom of this screenshot, you must visually look at the price wave peaks, candle sizes, and velocity to CALCULATE and PROJECT what their state would be right now.
                        
                        Analyze for target time window: {target_time}.
                        
                        Your output MUST be a valid JSON object ONLY. Do not wrap in markdown or backticks.
                        Format:
                        {{
                            "bullish_bias": <int_percentage>,
                            "bearish_bias": <int_percentage>,
                            "trend": "<Uptrend/Downtrend/Sideways>",
                            "pattern": "<Exact candlestick pattern name>",
                            "macd_scenario": "<State of MACD - e.g. Bullish Crossover / Bearish Signal Cross>",
                            "stochastic_scenario": "<State of Stochastic - e.g. Oversold K-Line cross / Overbought Reversal>",
                            "support": "<Support level>",
                            "resistance": "<Resistance level>",
                            "confidence": "<High/Medium/Low>",
                            "reasons": [
                                "1. Candle Fact: Describe the structure of the last candle here in Hinglish.",
                                "2. Indicator Math: Explain why the projected MACD/Stochastic scenario aligns with the current price momentum in Hinglish.",
                                "3. Target {target_time} Scenario: Give the exact behavioral reason for Green or Red win percentage at this time in Hinglish."
                            ]
                        }}
                        """
                        
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": prompt},
                                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                                    ]
                                }
                            ],
                            max_tokens=800,
                            temperature=0.15,
                            response_format={"type": "json_object"}
                        )
                        
                        raw_text = response.choices[0].message.content.strip()
                        data = json.loads(raw_text)
                        
                        # Display Results
                        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
                        st.markdown(f"<span class='time-badge'>Target: {target_time}</span>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='margin:0 0 5px 0; color:white;'>ChatGPT Indicator & Price Action Scenario</h3>", unsafe_allow_html=True)
                        
                        st.markdown(f"""
                            <div class='bias-container'>
                                <div class='bias-box'><div class='bullish-title'>↑ GREEN Candle Chance</div><div class='bullish-val'>{data['bullish_bias']}%</div></div>
                                <div class='bias-box'><div class='bearish-title'>↓ RED Candle Chance</div><div class='bearish-val'>{data['bearish_bias']}%</div></div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        t_color = "trend-green" if "Up" in data['trend'] else "trend-red"
                        st.markdown(f"""
                            <div class='data-row'><span class='data-label'>Trend Matrix</span><span class='data-value {t_color}'>{data['trend']}</span></div>
                            <div class='data-row'><span class='data-label'>Candlestick Pattern</span><span class='data-value'>{data['pattern']}</span></div>
                            <div class='data-row'><span class='data-label'>📊 Calculated MACD State</span><span class='data-value' style='color:#5383ec;'>{data['macd_scenario']}</span></div>
                            <div class='data-row'><span class='data-label'>📉 Stochastic Oscillator</span><span class='data-value' style='color:#f1c40f;'>{data['stochastic_scenario']}</span></div>
                            <div class='data-row'><span class='data-label'>Support Zone</span><span class='data-value'>{data['support']}</span></div>
                            <div class='data-row'><span class='data-label'>Resistance Zone</span><span class='data-value'>{data['resistance']}</span></div>
                            <div class='data-row'><span class='data-label'>AI Confidence</span><span class='data-value conf-badge'>{data['confidence']}</span></div>
                        """, unsafe_allow_html=True)
                        
                        st.markdown(f"<div class='why-title'>🧠 Confluence Psychology & Reasons ({target_time}):</div>", unsafe_allow_html=True)
                        st.markdown("<ul class='custom-bullet'>", unsafe_allow_html=True)
                        for reason in data['reasons']:
                            st.markdown(f"<li>{reason}</li>", unsafe_allow_html=True)
                        st.markdown("</ul></div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"ChatGPT Analysis Error: {str(e)}")

# 🕒 BACKGROUND LOOP FOR LIVE CLOCK
while True:
    current_ist = datetime.datetime.now(IST).strftime("%I:%M:%S %p")
    clock_placeholder.markdown(f"""
        <div class='live-clock-box'>
            <h2 style='color:#ff4b4b; margin:0; font-size:28px; font-family:monospace;'>{current_ist}</h2>
            <span style='color:#8a8d93; font-size:12px;'>🔴 LIVE MARKET TIME (IST)</span>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(1)
