import streamlit as st

st.set_page_config(page_title="Boom Crash Sniper", layout="wide", page_icon="🎯")

st.markdown("<h1 style='text-align:center'>🎯 Boom & Crash Sniper</h1>", unsafe_allow_html=True)
st.caption("Fast Mode - Charts load separately")

tab1, tab2 = st.tabs(["🔵 BOOM 1000", "🔴 CRASH 1000"])

with tab1:
    st.subheader("Boom 1000 - Sell The Spike")
    c1, c2 = st.columns([3,1])
    with c1:
        st.components.v1.html("""
        <div style="height:500px" id="b"></div>
        <script src="https://s.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({"container_id":"b","autosize":true,"symbol":"CAPITALCOM:BOOM1000","interval":"1","theme":"dark"});
        </script>""", height=520)
    with c2:
        st.metric("Status","WAIT FOR SPIKE")
        st.write("**Rule:** Spike Wick > 4.5x avg → Wait 2 ticks → SELL")
        if st.button("Simulate SPIKE", key="boom"): st.success("🔴 SELL NOW - SL: Spike High")

with tab2:
    st.subheader("Crash 1000 - Buy The Spike")
    c1, c2 = st.columns([3,1])
    with c1:
        st.components.v1.html("""
        <div style="height:500px" id="c"></div>
        <script src="https://s.tradingview.com/tv.js"></script>
        <script>
        new TradingView.widget({"container_id":"c","autosize":true,"symbol":"CAPITALCOM:CRASH1000","interval":"1","theme":"dark"});
        </script>""", height=520)
    with c2:
        st.metric("Status","WAIT FOR SPIKE")
        st.write("**Rule:** Spike Wick > 4.5x avg → Wait 2 ticks → BUY")
        if st.button("Simulate SPIKE", key="crash"): st.success("🟢 BUY NOW - SL: Spike Low")

# Removed auto-rerun = instant load
