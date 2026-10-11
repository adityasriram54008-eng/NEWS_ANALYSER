import requests
from newspaper import Article, Config, ArticleException
import streamlit as st

API_KEY = "//API-KEY//"

def get_api(topic):
    url = f"https://newsapi.org/v2/top-headlines?q={topic}&apiKey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content

def get_articles(content,topic):

    st.subheader(f"Available :green[{len(content["articles"])}] top headlines for :green[_{topic}_]")
    counter = 0
    f_counter = 0

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

    for index, news in enumerate(content["articles"], start=1):

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

        if (len(article.text)) < 200:
            f_counter += 1
            continue
        else:
            st.write(article.text)
            st.write('-----')
            counter += 1

    return counter,f_counter

