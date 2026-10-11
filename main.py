import streamlit as st
import backend

st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    content = backend.get_api(topic)
    counter, f_counter = backend.get_articles(content,topic)

    st.subheader(f":blue[{counter}] of :green[{len(content["articles"])}] displayed")
    st.subheader(f":red[{f_counter}] articles failed")