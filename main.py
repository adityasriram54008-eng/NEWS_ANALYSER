import streamlit as st
import backend
from newspaper import Article, Config


st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    content = backend.get_info(topic)
    st.subheader(f"Available :green[{content["totalResults"]}] top headlines for :green[_{topic}_]")

    i = 1

    for news in content["articles"][:6]:
        config = Config()
        config.proxies = {
            "http": "http://us2512v1ej33:myjx887ixdxds36@193.56.28.63:3129",
            "https": "http://us2512v1ej33:myjx887ixdxds36@209.50.189.27:3129",
        }
        config.browser_user_agent = (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0.0.0 Safari/537.36'
        )
        config.request_timeout = 20

        article = Article(news['url'], config=config)
        article.download()
        article.parse()
        st.write(article.text)
        st.write(i)
        i = i+1