import streamlit as st

st.title("ボイスチェンジャー")

# 1つ目のオーディオファイル
st.header("元の音声")
data1 = "TsubukuVoice.mp3"
st.audio(data1)

# 2つ目のオーディオファイル
st.header("彼方このえの変換音声")
data2 = "audios/tanjiro.mp3"
st.audio(data2)
