import streamlit as st

st.title("ボイスチェンジャー")

# 1つ目のオーディオファイル
st.header("元の音声")
data1 = "audios/TsubukuVoice.mp3"
st.audio(data1)

# 2つ目のオーディオファイル
st.header("彼方このえの変換音声")
data2 = "audios/tsubuku_voice_raburaibu.mp3"
st.audio(data2)

st.header("竈門炭治郎の変換voice1")
data3 = "audios/tsubuku_voice2.mp3"
st.audio(data3)

st.header("竈門炭治郎の変換voice2")
data3 = "audios/tsubuku_voice1.mp3"
st.audio(data3)
