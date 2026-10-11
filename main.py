import streamlit as st
import backend
from newspaper import Article, Config, ArticleException

st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    content = backend.get_info(topic)
    st.subheader(f"Available :green[{len(content["articles"])}] top headlines for :green[_{topic}_]")

    counter = 0
    f_counter = 0

    for index,news in enumerate(content["articles"],start = 1):

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

        try:
            article.download()
            article.parse()
        except ArticleException as e:
            with open('ruledout.txt', 'a') as file:
                file.write(f"URL: {news['url']}\n")
                file.write(f"Exception type: {type(e).__name__}\n")
                file.write(f"Exception message: {str(e)}\n")
                file.write("-" * 50 + "\n")
            f_counter += 1
            continue

        st.write(article.text)
        st.write('-----')
        counter += 1

    st.subheader(f"{counter} of {len(content["articles"])} displayed")
    st.subheader(f"{f_counter} articles failed")