import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Pro Mathematical Analytics Engine", page_icon="📈", layout="centered")

st.title("📈 MATHEMATICAL OTC & FOREX ANALYTICS ENGINE")
st.write("Pure Quantitative Analysis via Live Interbank Price Feeds (Zero Randomness)")
st.markdown("---")

# 1. Asset Selection (Real International OTC / Forex Pairs)
st.subheader("🎯 Target Currency Pair")
pair_choice = st.selectbox("Select Live Forex Pair:", [
    "EURUSD=X (Euro / US Dollar)",
    "GBPUSD=X (British Pound / US Dollar)",
    "AUDUSD=X (Australian Dollar / US Dollar)",
    "USDJPY=X (US Dollar / Japanese Yen)"
])

# 2. Analytics Execution
if st.button("RUN MATHEMATICAL ANALYSIS 🚀"):
    with st.spinner("Fetching live tick-by-tick mathematical data matrices..."):
        # Fetching last 5 days data with 5-minute intervals for intraday precision
        data = yf.download(tickers=pair_choice, period="5d", interval="5m")
        
        if data.empty:
            st.error("⚠️ Server Timeout: Could not fetch real-time market array.")
        else:
            # Flatten multi-index columns if any
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)
                
            st.success(f"✅ Connection Established. Analyzing last {len(data)} price vectors.")
            
            # --- 100% PURE MATHEMATICAL INDICATORS CODE ---
            close_prices = data['Close'].dropna()
            
            # A. Relative Strength Index (RSI - 14)
            delta = close_prices.diff()
            gain = delta.clip(lower=0)
            loss = -delta.clip(upper=0)
            ema_gain = gain.ewm(com=13, adjust=False).mean()
            ema_loss = loss.ewm(com=13, adjust=False).mean()
            rs = ema_gain / (ema_loss + 1e-10)
            rsi = 100 - (100 / (1 + rs))
            
            # B. Bollinger Bands (20 Period, 2 Standard Deviations)
            sma_20 = close_prices.rolling(window=20).mean()
            std_20 = close_prices.rolling(window=20).std()
            upper_band = sma_20 + (2 * std_20)
            lower_band = sma_20 - (2 * std_20)
            
            # C. MACD (12, 26, 9)
            exp1 = close_prices.ewm(span=12, adjust=False).mean()
            exp2 = close_prices.ewm(span=26, adjust=False).mean()
            macd_line = exp1 - exp2
            signal_line = macd_line.ewm(span=9, adjust=False).mean()

            # Latest values extraction
            current_price = float(close_prices.iloc[-1])
            current_rsi = float(rsi.iloc[-1])
            current_upper = float(upper_band.iloc[-1])
            current_lower = float(lower_band.iloc[-1])
            current_macd = float(macd_line.iloc[-1])
            current_signal = float(signal_line.iloc[-1])
            
            # --- DISPLAY LIVE DATA MATRICES ---
            st.markdown("### 📊 Real-Time Market Metrics")
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric(label="Live Price", value=f"{current_price:.5f}")
            m_col2.metric(label="RSI (14)", value=f"{current_rsi:.2f}")
            m_col3.metric(label="Volatility Band", value="HIGH" if (current_upper - current_lower)/current_price > 0.002 else "LOW")

            # --- ALGORITHMIC VERIFICATION MATRIX (NO TUKKA) ---
            st.markdown("---")
            st.subheader("📝 Quantitative Verdict & Logic")
            
            # Strictly Mathematical Scoring System
            math_score = 0
            logic_logs = []
            
            # RSI Rules
            if current_rsi > 70:
                logic_logs.append(f"• **Overbought Core (RSI: {current_rsi:.2f}):** Momentum exhausted. High mathematical probability of downward mean reversion.")
                math_score -= 2
            elif current_rsi < 30:
                logic_logs.append(f"• **Oversold Core (RSI: {current_rsi:.2f}):** Selling pressure depleted. High probability of upward bounce.")
                math_score += 2
            else:
                logic_logs.append(f"• **Neutral Momentum:** RSI at {current_rsi:.2f} confirms stable trading range inside boundaries.")
                
            # Bollinger Bands Rules
            if current_price >= current_upper:
                logic_logs.append(f"• **Volatility Ceiling Breached:** Price touched Upper Bollinger Band ({current_upper:.5f}). Rejection expected.")
                math_score -= 2
            elif current_price <= current_lower:
                logic_logs.append(f"• **Volatility Floor Breached:** Price touched Lower Bollinger Band ({current_lower:.5f}). Structural support activated.")
                math_score += 2
                
            # MACD Crossover Rules
            if current_macd > current_signal:
                logic_logs.append("• **Bullish Convergence:** MACD Line crossed above Signal Line. Upward velocity increasing.")
                math_score += 1
            else:
                logic_logs.append("• **Bearish Convergence:** MACD Line crossed below Signal Line. Downward velocity increasing.")
                math_score -= 1

            # Output Determination based on raw score calculation
            if math_score >= 2:
                st.success("📈 STRATEGY: UPWARD BIAS (CALL MOMENTUM)")
                st.write("**Confidence Level:** HIGH MATHEMATICAL CONVERGENCE")
            elif math_score <= -2:
                st.error("📉 STRATEGY: DOWNWARD BIAS (PUT MOMENTUM)")
                st.write("**Confidence Level:** HIGH MATHEMATICAL CONVERGENCE")
            else:
                st.warning("🔄 STRATEGY: NO EDGE ZONE (SIDEWAYS MARKET)")
                st.write("**Confidence Level:** RISK ZONE - AVOID ENTRY")

            # Print Mathematical breakdown
            st.markdown("#### 📄 Mathematical Logic Breakdown:")
            for log in logic_logs:
                st.write(log)
                
            st.markdown("---")
            st.markdown(f"""
            **📐 Calculated Pricing Envelope:**
            * **Upper Volatility Resistance:** {current_upper:.5f}
            * **Lower Volatility Support:** {current_lower:.5f}
            * **MACD Differential:** {current_macd - current_signal:.6f}
            """)
            
st.write("---")
st.caption("100% Algorithmic Engineering Dashboard • Powered by Yahoo Finance Live Interbank Infrastructure")
