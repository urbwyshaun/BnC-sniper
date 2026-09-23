import streamlit as st

st.set_page_config(page_title="Boom Crash Sniper", layout="centered")

st.title("🎯 Boom & Crash Sniper")
st.caption("Clean | Fast | No heavy charts")

tab_boom, tab_crash = st.tabs(["🔵 BOOM 1000", "🔴 CRASH 1000"])

# --- BOOM TAB ---
with tab_boom:
    st.subheader("Boom 1000")
    st.markdown("**Strategy: SELL the spike**")
    
    col1, col2 = st.columns(2)
    col1.metric("Status", "WAITING")
    col2.metric("Next Action", "Wait for spike")
    
    st.divider()
    st.write("**Rules:**")
    st.write("1. Watch for big down spike")
    st.write("2. Wait 2 ticks after spike")
    st.write("3. Enter SELL")
    st.write("4. SL: Top of spike | TP: 50% retrace")
    
    st.link_button("📈 Open Boom Chart", "https://app.deriv.com/")

# --- CRASH TAB ---
with tab_crash:
    st.subheader("Crash 1000")
    st.markdown("**Strategy: BUY the spike**")
    
    col1, col2 = st.columns(2)
    col1.metric("Status", "WAITING")
    col2.metric("Next Action", "Wait for spike")
    
    st.divider()
    st.write("**Rules:**")
    st.write("1. Watch for big up spike")
    st.write("2. Wait 2 ticks after spike")
    st.write("3. Enter BUY")
    st.write("4. SL: Bottom of spike | TP: 50% retrace")

st.divider()
st.success("✅ This version loads in 2 seconds")
