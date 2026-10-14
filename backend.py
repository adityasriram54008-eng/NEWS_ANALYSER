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

def get_articles(content, topic):
    in_time = time.time()

    st.subheader(f"Available :green[{len(content['articles'])}] top headlines for :green[_{topic}_]")

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
        start_time = None
        end_time = None
        outcome = "unknown"
        error_details = ""

        try:
            article = Article(news['url'], config=config)

            start_time = time.time()
            article.download()
            article.parse()
            end_time = time.time()

            if len(article.text) < 200:
                f_counter += 1
                outcome = "short_text"

            else:
                index = analyzer.polarity_scores(article.text)
                if index['compound'] > 0.05:
                    pos_counter += 1
                elif index['compound'] < -0.05:
                    neg_counter += 1
                else:
                    neu_counter += 1

                st.write(news['url'])
                st.write(f"Compound: {index['compound']}")
                st.write(f"Positivity: {index['pos']}")
                st.write(f"Negativity: {index['neg']}")
                st.write('-----')

                counter += 1
                outcome = "success"

        except Exception as e:
            error_details = f"{type(e).__name__}: {str(e)}"
            outcome = "extraction_error"
            f_counter += 1

        finally:
            end_timef = time.time()

            if start_time is not None:
                if end_time is None:
                    end_time = time.time()
                time_elapsed = end_time - start_time
            else:
                time_elapsed = 0.0

            time_elapsedf = end_timef - start_timef

            with open('article_outcomes.txt', 'a') as file:
                file.write(f"URL: {news['url']}\n")
                file.write(f"Outcome: {outcome}\n")
                file.write(
                    f"Download and parse time: "
                    f"{time_elapsed:.4f} seconds\n")
                file.write(
                    f"Total article time: "
                    f"{time_elapsedf:.4f} seconds\n")

                if error_details:
                    file.write(f"Error: {error_details}\n")

                file.write("-" * 50 + "\n")

    out_time = time.time()
    f_elapsed = out_time - in_time

    return counter,f_counter,pos_counter,neg_counter,neu_counter,f_elapsed

