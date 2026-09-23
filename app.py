import streamlit as st

st.set_page_config(page_title="Boom Crash Sniper", layout="wide")
st.title("🎯 Boom & Crash Sniper - Fast Mode")

tab1, tab2 = st.tabs(["🔵 BOOM 1000", "🔴 CRASH 1000"])

with tab1:
    st.subheader("BOOM 1000 - Sell Spike")
    st.metric("Signal", "WAIT 👀")
    st.info("1. Spike happens (big red wick)\n2. Wait 2 ticks\n3. SELL\nSL = 2% above spike")
    st.link_button("Open Boom Chart (Deriv)", "https://app.deriv.com/dtrader?market=boom_1000")

with tab2:
    st.subheader("CRASH 1000 - Buy Spike")
    st.metric("Signal", "WAIT 👀")
    st.info("1. Spike happens (big green wick)\n2. Wait 2 ticks\n3. BUY\nSL = 2% below spike")
    st.link_button("Open Crash Chart (Deriv)", "https://app.deriv.com/dtrader?market=crash_1000")

st.success("This version loads instantly. Use Deriv chart + this for signals.")
