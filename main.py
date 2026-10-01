import streamlit as st
import backend

st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    content = backend.get_info(topic)
    st.subheader(f"Available :green[{content["totalResults"]}] top headlines for :green[_{topic}_]")
    for article in content["articles"][:5]:
        st.write(article["title"])
        st.write(article["description"])
        st.write("---")
