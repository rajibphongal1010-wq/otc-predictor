import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Application Title
st.title("📊 AI OTC Candle Predictor")
st.write("Educational Simulation Tool for Strategy Testing")

# 1. Back-end Machine Learning Logic (AI Training Simulation)
np.random.seed(42)
rows = 1000
data = {
    'RSI': np.random.uniform(10, 90, rows),
    'MACD': np.random.uniform(-1, 1, rows),
    'Prev_Candle_Type': np.random.choice([0, 1], size=rows), # 0 = Red, 1 = Green
    'Next_Candle': np.random.choice([0, 1], size=rows)      # Target
}
df = pd.DataFrame(data)

# AI Features and Target Selection
X = df[['RSI', 'MACD', 'Prev_Candle_Type']]
y = df['Next_Candle']

# Model initialization and training
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# 2. Front-end User Interface (UI)
st.subheader("🔮 Current Market Status")
rsi_input = st.slider("Current RSI Value (Check on Quotex Chart)", 0.0, 100.0, 50.0)
macd_input = st.number_input("Current MACD Value (Check on Quotex Chart)", value=0.00, format="%.4f")
prev_candle = st.selectbox("Pichli Candle Kaunsi Thi?", ["🔴 Red (Bearish)", "🟢 Green (Bullish)"])

# Converting text input to numbers for AI
prev_encoded = 1 if "Green" in prev_candle else 0

# 3. Prediction Execution Button
if st.button("Predict Next Candle 🚀"):
    # Passing user data into the AI model
    user_data = np.array([[rsi_input, macd_input, prev_encoded]])
    probabilities = model.predict_proba(user_data)[0]
    
    put_chance = round(probabilities[0] * 100, 2)
    call_chance = round(probabilities[1] * 100, 2)
    
    st.markdown("---")
    st.subheader("🎯 AI Prediction Result:")
    
    # Displaying results based on higher probability
    if call_chance > put_chance:
        st.success(f"📈 **TREND: CALL (UP)**")
    else:
        st.error(f"📉 **TREND: PUT (DOWN)**")
        
    st.write(f"🟢 **CALL (UP) hone ka chance:** {call_chance}%")
    st.write(f"🔴 **PUT (DOWN) hone ka chance:** {put_chance}%")
    
    st.warning("⚠️ Disclaimer: This is an analytical tool based on historical patterns. Use it only on Demo Accounts.")
