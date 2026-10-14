import requests
from newspaper import Article, Config, ArticleException
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import time

API_KEY = "9e5609838c2c482491361790dec782ab"

def get_api(topic,start,end):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={start}&to={end}&sortBy=relevancy&language=en&apiKey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content

def get_articles(content,topic):
    in_time = time.time()
    st.subheader(f"Available :green[{len(content["articles"])}] top headlines for :green[_{topic}_]")
    counter = 0
    f_counter = 0
    pos_counter = 0
    neg_counter = 0
    neu_counter = 0

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

    analyzer = SentimentIntensityAnalyzer()

    for news in content["articles"][:20]:
        start_timef = time.time()

        article = Article(news['url'], config=config)

        try:
            start_time = time.time()
            article.download()
            article.parse()
            end_time = time.time()

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
            index = analyzer.polarity_scores(article.text)
            if index['compound']>0.05:
                pos_counter += 1
            elif index['compound']< -0.05:
                neg_counter += 1
            else:
                neu_counter += 1

            st.write(news['url'])
            st.write(f"Compound: {index['compound']}")
            st.write(f"Positivity: {index['pos']}")
            st.write(f"Negativity: {index['neg']}")
            st.write('-----')
            counter += 1

            end_timef = time.time()

            time_elapsed = end_time - start_time
            time_elapsedf = end_timef - start_timef

            with open('complete_time.txt','a') as file:
                file.write(f"{time_elapsedf}\n")
            with open('time_in_dp.txt','a') as file:
                file.write(f"{time_elapsed}\n")
    out_time = time.time()
    f_elapsed = out_time - in_time
    return counter,f_counter,pos_counter,neg_counter, neu_counter, f_elapsed

