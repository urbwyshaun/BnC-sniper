import streamlit as st
import requests

st.set_page_config(page_title="Boom Crash Sniper", layout="wide", page_icon="🎯")

# --- SIDEBAR WHATSAPP ---
st.sidebar.title("📱 WhatsApp Setup")
phone = st.sidebar.text_input("Phone (with country code)", placeholder="27712345678")
apikey = st.sidebar.text_input("CallMeBot API Key", type="password")
st.sidebar.markdown("[Get API Key Here](https://www.callmebot.com/blog/free-api-whatsapp-messages/)")
st.sidebar.divider()
st.sidebar.success("App: Separate Charts ✅")

def send_wa(msg):
    if phone and apikey:
        try:
            url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={msg}&apikey={apikey}"
            requests.get(url, timeout=5)
            return True
        except: return False
    return False

st.title("🎯 Boom & Crash Sniper - FINAL")

tab_boom, tab_crash = st.tabs(["🔵 BOOM 1000 - SELL SPIKES", "🔴 CRASH 1000 - BUY SPIKES"])

# BOOM TAB - SEPARATE CHART
with tab_boom:
    col_chart, col_info = st.columns([3, 1])
    with col_chart:
        st.components.v1.html("""
        <div id="boom_chart" style="height:550px;"></div>
        <script type="text/javascript" src="https://s.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "container_id": "boom_chart",
          "autosize": true,
          "symbol": "OANDA:BOOM1000USD",
          "interval": "1",
          "timezone": "Africa/Johannesburg",
          "theme": "dark",
          "style": "1",
          "locale": "en",
          "toolbar_bg": "#f1f3f6",
          "hide_side_toolbar": false
        });
        </script>
        """, height=570)
    with col_info:
        st.subheader("🔵 BOOM 1000")
        st.metric("STATUS", "WAITING FOR SPIKE")
        st.write("**Strategy:** Sell The Spike")
        st.write("SL: 2% above spike high")
        st.write("TP: 50% spike retrace")
        st.divider()
        if st.button("🔴 BOOM SPIKE DETECTED - SELL", type="primary", use_container_width=True):
            st.audio("https://www.soundjay.com/buttons/sounds/beep-01a.mp3")
            st.error("### 🔴 SELL NOW ON BOOM!")
            st.write("Enter SELL | SL: Spike High")
            if send_wa("🔴 BOOM 1000 SPIKE - SELL NOW! SL: Spike High"): st.success("WhatsApp Sent ✅")
        st.info("Wait for big red wick > 4.5x average")

# CRASH TAB - SEPARATE CHART
with tab_crash:
    col_chart, col_info = st.columns([3, 1])
    with col_chart:
        st.components.v1.html("""
        <div id="crash_chart" style="height:550px;"></div>
        <script type="text/javascript" src="https://s.tradingview.com/tv.js"></script>
        <script type="text/javascript">
        new TradingView.widget({
          "container_id": "crash_chart",
          "autosize": true,
          "symbol": "OANDA:CRASH1000USD",
          "interval": "1",
          "timezone": "Africa/Johannesburg",
          "theme": "dark",
          "style": "1",
          "locale": "en",
          "toolbar_bg": "#f1f3f6",
          "hide_side_toolbar": false
        });
        </script>
        """, height=570)
    with col_info:
        st.subheader("🔴 CRASH 1000")
        st.metric("STATUS", "WAITING FOR SPIKE")
        st.write("**Strategy:** Buy The Spike")
        st.write("SL: 2% below spike low")
        st.write("TP: 50% spike retrace")
        st.divider()
        if st.button("🟢 CRASH SPIKE DETECTED - BUY", type="primary", use_container_width=True):
            st.audio("https://www.soundjay.com/buttons/sounds/beep-01a.mp3")
            st.success("### 🟢 BUY NOW ON CRASH!")
            st.write("Enter BUY | SL: Spike Low")
            if send_wa("🟢 CRASH 1000 SPIKE - BUY NOW! SL: Spike Low"): st.success("WhatsApp Sent ✅")
        st.info("Wait for big green wick > 4.5x average")

st.divider()
st.caption("Built for Cape Town | 2 separate charts | WhatsApp alerts ready")
