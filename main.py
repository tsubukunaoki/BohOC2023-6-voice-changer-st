import streamlit as st

st.title("タイトルを入力")

# 1つ目のオーディオファイル
st.header("タイトルを入力")
data1 = "audios/tanjiro.mp3"
st.audio(data1)

# 2つ目のオーディオファイル
st.header("タイトルを入力")
data2 = "audios/TsubukuVoice.mp3"
st.audio(data2)
