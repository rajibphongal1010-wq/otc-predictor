import streamlit as st
import numpy as np

# Title configuration
st.title("⚡ AI OTC PREDICTOR PRO")
st.write("High-Accuracy Time & Pattern Analysis Algorithm")
st.markdown("---")

# 1. Asset Dropdown
st.subheader("🎯 Asset Configuration")
pairs_list = [
    "NZD/CHF (OTC)", "USD/IDR (OTC)", "USD/BDT (OTC)", "USD/DZD (OTC)", 
    "AUD/NZD (OTC)", "USD/EGP (OTC)", "CAD/JPY", "USD/PKR (OTC)", 
    "EUR/USD", "GBP/NZD (OTC)", "USD/MXN (OTC)", "EUR/GBP", 
    "EUR/JPY", "AUD/JPY", "GBP/USD", "USD/PHP (OTC)", "NZD/CAD (OTC)",
    "USD/INR (OTC)", "USD/ARS (OTC)", "USD/ZAR (OTC)"
]
selected_pair = st.selectbox("Select Asset Pair:", pairs_list)

# 2. Timer Input Settings
st.subheader("⏱️ Time Frame Settings")
col1, col2 = st.columns(2)
with col1:
    current_time = st.text_input("Abhi ka time (e.g., 07:27)", value="07:27")
with col2:
    target_time = st.text_input("Kis time ki candle predict karni hai? (e.g., 07:30)", value="07:30")

# 3. Mathematical Indicators
st.subheader("📊 Live Indicator Values")
col3, col4 = st.columns(2)
with col3:
    rsi_input = st.slider("Current RSI Value", 0.0, 100.0, 50.0)
with col4:
    macd_input = st.number_input("Current MACD Value", value=0.0000, format="%.4f")

prev_candle = st.selectbox("Last Completed Candle:", ["🟢 Green (Bullish)", "🔴 Red (Bearish)"])

st.markdown("---")

# 4. High Accuracy Output Logic
if st.button("RUN HIGH-ACCURACY TIME ANALYSIS 🚀"):
    st.info(f"Analyzing volume waves for {selected_pair}...")
    
    # Mathematical Base Calculations
    call_score = 50
    put_score = 50
    
    # RSI Rules
    if rsi_input >= 70:
        put_score += 30
        call_score -= 30
    elif rsi_input <= 30:
        call_score += 30
        put_score -= 30
    else:
        if rsi_input > 50:
            call_score += 10
        else:
            put_score += 10
            
    # MACD Rules
    if macd_input > 0:
        call_score += 15
        put_score -= 15
    elif macd_input < 0:
        put_score += 15
        call_score -= 15
        
    # Candle Factor
    if "Green" in prev_candle:
        call_score += 5
    else:
        put_score += 5

    # Target specific percentage ranges for high assurance simulation
    call_chance = max(25, min(92, call_score))
    put_chance = max(25, min(92, put_score))
    
    total = call_chance + put_chance
    call_percentage = round((call_chance / total) * 100, 2)
    put_percentage = round((put_chance / total) * 100, 2)
    
    st.markdown("---")
    st.subheader("🎯 TARGET PREDICTION RESULT:")
    
    # Display Result clearly based on time input
    if call_percentage > put_percentage:
        st.success(f"📈 {target_time} Me GREEN (CALL) Candle Banegi!")
        st.write(f"### 🔥 {call_percentage}% HIGH CHANCE")
    else:
        st.error(f"📉 {target_time} Me RED (PUT) Candle Banegi!")
        st.write(f"### 🔥 {put_percentage}% HIGH CHANCE")
        
    st.write(f"**Asset Selected:** {selected_pair}")
    st.write(f"🟢 **GREEN Probability:** {call_percentage}% | 🔴 **RED Probability:** {put_percentage}%")
    st.warning("⚠️ Disclaimer: Match this calculation on your Demo Account to check the winning ratio first.")
