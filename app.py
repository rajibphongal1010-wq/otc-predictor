import streamlit as st
from PIL import Image
import google.generativeai as genai
import time

# Premium Dark Layout Configuration
st.set_page_config(page_title="CORE AI VISION v5.0", page_icon="📉", layout="wide")

# UI styling matching output example exactly
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
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 HIGH-POWER AI VISION CANDLESTICK SCANNER")
st.write("Real AI analysis using genuine Multi-Modal Computer Vision. No pixel hacks.")
st.markdown("---")

# Sidebar for Genuine Google API Authentication
st.sidebar.subheader("🔑 Secure AI Core")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

uploaded_file = st.file_uploader("📥 Drop chart screenshot here:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("📷 Control Matrix")
        st.image(image, use_container_width=True)
        
        # All exact pairs extracted from user screenshots 1000123652.jpg and 1000123653.jpg
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
        
        # Dynamic manual target time
        target_time = st.text_input("🎯 Set Target Candle Time (e.g., 12:45):", value="12:45")
        
        execute_btn = st.button("🚀 RUN GENUINE PRICE ACTION ANALYSIS")
        
    with col2:
        st.subheader("🖥️ True AI Output Matrix")
        
        if execute_btn:
            if not api_key:
                st.error("❌ Please supply a valid Gemini API Key in the sidebar.")
            else:
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    with st.spinner("AI is physically reading candle structures & market psychology..."):
                        
                        # Dynamic prompt ensuring no pixel hacks or guessing
                        prompt = f"""
                        You are an expert price action trader. Analyze this chart image for the asset {selected_pair}.
                        You must read the actual chart geometry, candles (body, wick, ratio), market psychology, and support/resistance lines.
                        Do NOT guess or look at random color distributions. Provide an expert assessment for what the next market movement behavior implies for the target execution time window: {target_time}.
                        
                        Return the output strictly in this exact Python dictionary string format so the script can parse it (Do not wrap in backticks or markdown, just raw text):
                        {{
                            "bullish_bias": int (percentage value),
                            "bearish_bias": int (percentage value),
                            "trend": "Uptrend" or "Downtrend" or "Sideways",
                            "pattern": "Identified pattern name",
                            "support": "Identified support price level",
                            "resistance": "Identified resistance price level",
                            "confidence": "High" or "Medium" or "Low",
                            "reasons": ["Reason 1 in Hinglish based on psychology", "Reason 2 in Hinglish based on S/R block", "Reason 3 based on candle wicks"]
                        }}
                        """
                        
                        response = model.generate_content([prompt, image])
                        
                        # Parsing dictionary safely
                        clean_text = response.text.strip().replace("```python", "").replace("```", "")
                        data = eval(clean_text)
                        
                        # --- PREMIUM DESIGN UI ---
                        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
                        st.markdown(f"<span class='time-badge'>{target_time}</span>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='margin:0 0 5px 0; color:white;'>Analysis Result</h3>", unsafe_allow_html=True)
                        st.markdown(f"<div style='color:#8a8d93; font-size:14px; margin-bottom:15px;'>Asset: {selected_pair}</div>", unsafe_allow_html=True)
                        
                        # Bias Display Bars
                        st.markdown(f"""
                            <div class='bias-container'>
                                <div class='bias-box'>
                                    <div class='bullish-title'>↑ Bullish Bias</div>
                                    <div class='bullish-val'>{data['bullish_bias']}%</div>
                                </div>
                                <div class='bias-box'>
                                    <div class='bearish-title'>↓ Bearish Bias</div>
                                    <div class='bearish-val'>{data['bearish_bias']}%</div>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                        
                        # Technical Info Rows
                        t_color = "trend-green" if "Up" in data['trend'] else "trend-red"
                        st.markdown(f"""
                            <div class='data-row'><span class='data-label'>Trend</span><span class='data-value {t_color}'>{data['trend']}</span></div>
                            <div class='data-row'><span class='data-label'>Current Pattern</span><span class='data-value'>{data['pattern']}</span></div>
                            <div class='data-row'><span class='data-label'>Support</span><span class='data-value'>{data['support']}</span></div>
                            <div class='data-row'><span class='data-label'>Resistance</span><span class='data-value'>{data['resistance']}</span></div>
                            <div class='data-row'><span class='data-label'>Confidence</span><span class='data-value conf-badge'>{data['confidence']}</span></div>
                        """, unsafe_allow_html=True)
                        
                        # Psychological Reasons Breakdown
                        st.markdown(f"<div class='why-title'>🧠 Candlestick Psychology & Reasons ({target_time}):</div>", unsafe_allow_html=True)
                        st.markdown("<ul class='custom-bullet'>", unsafe_allow_html=True)
                        for reason in data['reasons']:
                            st.markdown(f"<li>{reason}</li>", unsafe_allow_html=True)
                        st.markdown("</ul></div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"Format Parsing Error: AI response structural anomaly. Try again. Detail: {str(e)}")
