import streamlit as st
import datetime
import time



# Web にタイトルを表示  
st.markdown("<h1 style='text-align: center;'>現在の時刻</h1>", unsafe_allow_html=True)


# 現在時刻取得
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.header(f"ただいまの時刻は {now} です")

# 1秒後に再実行
time.sleep(1)
st.rerun()

#
# streamlit run Clock2_print.py
#
#
# http://localhost:8501
#
