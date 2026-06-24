import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

# Application Title
st.title("📊 AI OTC Chart Analyser & Predictor")
st.write("Educational Simulation Tool (Image Upload & Timer Update)")

# 1. Screenshot Upload Box
st.subheader("📸 Upload Chart Screenshot")
uploaded_file = st.file_uploader("Apne Quotex Chart Ka Screenshot Yahan Upload Karein", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chart Screenshot", use_container_width=True)
    st.success("✅ Photo Uploaded Successfully!")

# 2. Timer Settings
st.subheader("⏱️ Target Prediction Time")
col1, col2 = st.columns(2)
with col1:
    current_time = st.text_input("Abhi ka time kya ho rha hai? (e.g., 06:23)", value="06:23")
with col2:
    target_time = st.text_input("Kis time ki candle predict karni hai? (e.g., 06:26)", value="06:26")

# 3. Old ML Indicator Logic (For Background Simulation)
np.random.seed(42)
rows = 1000
data = {
    'RSI': np.random.uniform(10, 90, rows),
    'MACD': np.random.uniform(-1, 1, rows),
    'Prev_Candle_Type': np.random.choice([0, 1], size=rows),
    'Next_Candle': np.random.choice([0, 1], size=rows)
}
df = pd.DataFrame(data)
X = df[['RSI', 'MACD', 'Prev_Candle_Type']]
y = df['Next_Candle']
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

st.markdown("---")
st.subheader("🎯 Run AI Analysis")

# 4. Prediction Button Execution
if st.button("Analyze & Predict Next Candle 🚀"):
    if uploaded_file is None:
        st.error("⚠️ Pehle upar chart ka screenshot upload kijiye!")
    else:
        # Image based pattern simulation
        mock_probabilities = np.random.dirichlet(np.ones(2), size=1)[0]
        put_chance = round(mock_probabilities[0] * 100, 2)
        call_chance = round(mock_probabilities[1] * 100, 2)
        
        st.info(f"Analyzing patterns between {current_time} and target time {target_time}...")
        st.markdown("---")
        st.subheader(f"🔮 AI Result for {target_time} Candle:")
        
        if call_chance > put_chance:
            st.success(f"📈 **TREND DIRECTION: CALL (UP)**")
        else:
            st.error(f"📉 **TREND DIRECTION: PUT (DOWN)**")
            
        st.write(f"🟢 **CALL (UP) Hone Ka Chance:** {call_chance}%")
        st.write(f"🔴 **PUT (DOWN) Hone Ka Chance:** {put_chance}%")
        
        st.warning("⚠️ Disclaimer: Jaisa pehle discuss hua tha, yeh sirf ek experimental simulation hai. Is par real money se trade mat lena kyunki static photo se accuracy nahi aati.")
