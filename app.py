import streamlit as st
import requests

st.set_page_config(page_title="Boom Crash Sniper", layout="wide", page_icon="🎯")
st.title("🎯 Boom & Crash Sniper - PRO")

# --- WHATSAPP SETUP ---
st.sidebar.header("📱 WhatsApp Alert")
phone = st.sidebar.text_input("Your Number", placeholder="27xxxx")
apikey = st.sidebar.text_input("CallMeBot API Key", type="password")
st.sidebar.caption("Get key: callmebot.com -> WhatsApp")

def send_whatsapp(msg):
    if phone and apikey:
        try:
            url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={msg}&apikey={apikey}"
            requests.get(url, timeout=5)
            st.toast("WhatsApp sent!")
        except: st.error("WhatsApp failed")

# --- TABS - SEPARATE CHARTS ---
tab_boom, tab_crash = st.tabs(["🔵 BOOM 1000", "🔴 CRASH 1000"])

with tab_boom:
    c1, c2 = st.columns([3,1])
    with c1:
        st.components.v1.html("""
        <div id="b" style="height:500px"></div>
        <script src="https://s.tradingview.com/tv.js"></script>
        <script>new TradingView.widget({
          "container_id":"b","autosize":true,"symbol":"DERIV:BOOM1000",
          "interval":"1","theme":"dark","style":"1"
        });</script>""", height=520)
    with c2:
        st.subheader("Boom 1000")
        st.metric("Signal", "WAIT")
        st.write("Sell spike reversal")
        if st.button("🔴 Simulate BOOM SPIKE", use_container_width=True):
            send_whatsapp("🔴 BOOM 1000 SPIKE - SELL NOW!")
            st.success("SELL NOW - SL: spike high")

with tab_crash:
    c1, c2 = st.columns([3,1])
    with c1:
        st.components.v1.html("""
        <div id="cr" style="height:500px"></div>
        <script src="https://s.tradingview.com/tv.js"></script>
        <script>new TradingView.widget({
          "container_id":"cr","autosize":true,"symbol":"DERIV:CRASH1000",
          "interval":"1","theme":"dark","style":"1"
        });</script>""", height=520)
    with c2:
        st.subheader("Crash 1000")
        st.metric("Signal", "WAIT")
        st.write("Buy spike reversal")
        if st.button("🟢 Simulate CRASH SPIKE", use_container_width=True):
            send_whatsapp("🟢 CRASH 1000 SPIKE - BUY NOW!")
            st.success("BUY NOW - SL: spike low")
