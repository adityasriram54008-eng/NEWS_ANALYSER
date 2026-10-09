import streamlit as st
import backend
from newspaper import Article

st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    content = backend.get_info(topic)
    st.subheader(f"Available :green[{content["totalResults"]}] top headlines for :green[_{topic}_]")
    for news in content["articles"][0]:
        article = Article(news['url'])
        article.download()
        article.parse()
        st.write(article.text)
        st.write("----------------")