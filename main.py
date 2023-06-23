import streamlit as st

st.title("ボイスチェンジャー")

# 1つ目のオーディオファイル
st.header("元の音声")
data1 = "audios/SnapSave.io - 「鬼滅の刃」竈門炭治郎の名言・台詞まとめ (128 kbps).mp3"
st.audio(data1)

# 2つ目のオーディオファイル
st.header("変換後の音声")
data2 = "audios/tanjiro.mp3"
st.audio(data2)
