import streamlit as st
from PIL import Image
import google.generativeai as genai
import time

# Premium Dark Dashboard Config
st.set_page_config(page_title="REAL AI VISION CORE v4.0", page_icon="📈", layout="wide")

# CSS matching 1000123790.jpg exactly with high fidelity layout
st.markdown("""
    <style>
    .main { background-color: #111214; color: #e3e4e6; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    
    /* Main Card Container */
    .dashboard-card {
        background-color: #1a1b1e;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #2a2b2f;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    
    /* Time Badge matching 1000123790.jpg layout */
    .time-badge {
        background-color: #262930;
        color: #5383ec;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: bold;
        float: right;
    }
    
    /* Bias Metrics Blocks */
    .bias-container { display: flex; gap: 15px; margin-bottom: 25px; margin-top: 15px; }
    .bias-box {
        flex: 1;
        background-color: #141517;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        border: 1px solid #222326;
    }
    .bullish-title { color: #2ebd85; font-size: 14px; display: flex; justify-content: center; align-items: center; gap: 5px; }
    .bearish-title { color: #df4949; font-size: 14px; display: flex; justify-content: center; align-items: center; gap: 5px; }
    .bullish-val { color: #2ebd85; font-size: 32px; font-weight: bold; margin-top: 5px; }
    .bearish-val { color: #df4949; font-size: 32px; font-weight: bold; margin-top: 5px; }
    
    /* Data Rows Layout */
    .data-row {
        display: flex;
        justify-content: space-between;
        padding: 14px 0;
        border-bottom: 1px solid #222326;
        font-size: 15px;
    }
    .data-label { color: #8a8d93; }
    .data-value { font-weight: 500; color: #ffffff; }
    .trend-green { color: #2ebd85; font-weight: bold; }
    .trend-red { color: #df4949; font-weight: bold; }
    .conf-medium { color: #2ebd85; display: flex; align-items: center; gap: 5px; }
    
    /* Bullet points section */
    .why-section { margin-top: 25px; }
    .why-title { font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
    .custom-bullet { list-style-type: none; padding-left: 0; }
    .custom-bullet li { padding-left: 20px; margin-bottom: 10px; position: relative; color: #c2c4c9; font-size: 14px; }
    .custom-bullet li::before { content: "•"; position: absolute; left: 0; color: #ffffff; font-size: 18px; top: -2px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧙‍♂️ MULTI-CURRENCY REAL AI VISION SCANNER")
st.write("Powered by genuine Gemini 2.5 Multi-Modal Vision Processing Engine.")
st.markdown("---")

# 1. API Key Setup in Control Panel
st.sidebar.subheader("🔑 AI Authentication")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

# 2. Image Upload
uploaded_file = st.file_uploader("📥 Drag and drop or browse chart screenshot:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("📷 Control Panel & Input")
        st.image(image, use_container_width=True)
        
        # Currency Pair Options
        currency_pairs = [
            "EUR/USD (Forex Real)", "EUR/JPY (Forex Real)", "GBP/USD (Forex Real)", 
            "USD/JPY (Forex Real)", "EUR/USD (OTC)", "EUR/JPY (OTC)"
        ]
        selected_pair = st.selectbox("💱 Select Uploaded Currency Pair:", currency_pairs)
        
        # Manual Target Time Input
        current_system_time = time.strftime("%H:%M")
        target_time_input = st.text_input("🎯 Set Target Candle Time (e.g., 12:30):", value=current_system_time)
        
        trigger_analysis = st.button("🚀 EXECUTE REAL AI VISION SCAN")
        
    with col2:
        st.subheader("🖥️ Core System Output")
        
        if trigger_analysis:
            if not api_key:
                st.error("❌ Please enter your Gemini API Key in the sidebar first!")
            else:
                try:
                    # Configuring Google GenAI with user's genuine API key
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    with st.spinner("AI Engine is scanning candlesticks and visual geometry..."):
                        
                        # High fidelity technical prompt explicitly forcing structure validation
                        prompt = f"""
                        You are an expert financial market analyst. Analyze this chart image for the pair {selected_pair}.
                        Perform real analysis on market structure, candlestick patterns (like Engulfing, Doji, Hammer), support/resistance lines, and price action psychology.
                        Do NOT guess or base analysis on random pixel distribution. Give a probabilistic prediction for the upcoming candle at target time {target_time_input}.
                        
                        Return the result STRICTLY as a valid Python dictionary with the exact following keys for processing (do not wrap in markdown blocks, just the raw text):
                        {{
                            "bullish_bias": int (e.g. 68),
                            "bearish_bias": int (e.g. 32),
                            "trend": "Uptrend" or "Downtrend" or "Sideways",
                            "pattern": "Name of pattern detected or 'None'",
                            "support": "Detected price level or approximate decimal string",
                            "resistance": "Detected price level or approximate decimal string",
                            "confidence": "High" or "Medium" or "Low",
                            "reasons": [list of 3-4 specific structural bullet points string explaining why in Hinglish language]
                        }}
                        """
                        
                        # Sending the prompt along with the raw uploaded chart image matrix to Google AI
                        response = model.generate_content([prompt, image])
                        
                        # Parsing response data safely
                        data = eval(response.text.strip().replace("```python", "").replace("```", ""))
                        
                        # --- PREMIUM DASHBOARD LAYOUT INJECTION ---
                        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
                        
                        st.markdown(f"<span class='time-badge'>{target_time_input}</span>", unsafe_allow_html=True)
                        st.markdown(f"<h3 style='margin: 0 0 5px 0; font-size: 20px; color:#ffffff;'>Analysis Result</h3>", unsafe_allow_html=True)
                        st.markdown(f"<span style='color: #8a8d93; font-size: 14px;'>Asset: {selected_pair} (Real AI Analysis)</span><div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)
                        
                        # Twin Blocks for Bias Percentages from AI Model
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
                        
                        # Data Rows mapping
                        trend_class = "trend-green" if "Up" in data['trend'] else "trend-red"
                        st.markdown(f"""
                            <div class='data-row'><span class='data-label'>Trend</span><span class='data-value {trend_class}'> {data['trend']}</span></div>
                            <div class='data-row'><span class='data-label'>Current Pattern</span><span class='data-value'>{data['pattern']}</span></div>
                            <div class='data-row'><span class='data-label'>Support</span><span class='data-value'>{data['support']}</span></div>
                            <div class='data-row'><span class='data-label'>Resistance</span><span class='data-value'>{data['resistance']}</span></div>
                            <div class='data-row'><span class='data-label'>Confidence</span><span class='data-value conf-medium'>{data['confidence']}</span></div>
                        """, unsafe_allow_html=True)
                        
                        # Dynamic Why Section based on actual AI inference
                        bias_direction = "bullish" if data['bullish_bias'] >= data['bearish_bias'] else "bearish"
                        st.markdown(f"""
                            <div class='why-section'>
                                <div class='why-title'>🧠 Why {bias_direction} for {target_time_input}?</div>
                                <ul class='custom-bullet'>
                        """)
                        for r in data['reasons']:
                            st.markdown(f"<li>{r}</li>", unsafe_allow_html=True)
                        st.markdown("</ul></div>", unsafe_allow_html=True)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"⚠️ Connection Error or Invalid Output Format: {str(e)}")
                    st.warning("Make sure your API key is valid and you uploaded a clear chart image.")
        else:
            st.info("💡 API Key daalein, Asset aur Target Time set karein, aur execute button dabayein.")

st.markdown("---")
st.caption("Educational AI Multi-Modal Engine • This module parses visual inputs through external neural network endpoints.")
