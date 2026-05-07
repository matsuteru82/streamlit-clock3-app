import streamlit as st
import datetime
from streamlit_autorefresh import st_autorefresh

# 1秒ごとに更新
st_autorefresh(interval=1000, key="clockrefresh")

JST = datetime.timezone(datetime.timedelta(hours=9))

st.title("世界時計")

utc_now = datetime.datetime.now(datetime.timezone.utc)
jst_now = utc_now.astimezone(JST)

# UTC
st.header("UTC")

st.write(utc_now.strftime("%Y-%m-%d %H:%M:%S"))

weekday_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

today_utc = utc_now.weekday()

st.write(f"Today is {weekday_en[today_utc]}")

# JST
st.header("JST")

st.write(jst_now.strftime("%Y-%m-%d %H:%M:%S"))

weekday_jp = ["月", "火", "水", "木", "金", "土", "日"]

today_jst = jst_now.weekday()

st.write(
    f"今日は {jst_now.strftime('%Y年%m月%d日')} "
    f"{weekday_jp[today_jst]}曜日です"
)
#
# streamlit run Clock4_BrowserRefresh.py
#
#
# http://localhost:8501
#
