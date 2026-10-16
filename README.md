# 📰 News Analyzer

A Python-based web application that analyzes news articles on a given topic and evaluates the **sentiment and overall portrayal** of the topic across different news sources.

The project uses the **NewsAPI** to retrieve news articles, extracts article content, and applies **Natural Language Processing (NLP)** techniques to analyze the sentiment of the articles.

---

## 🚀 Features

- 🔎 Search for news articles based on a topic
- 📰 Retrieve articles using the NewsAPI
- 📄 Extract article text using `newspaper3k`
- 🧠 Perform sentiment analysis using NLTK
- 📊 Calculate positive and negative sentiment
- 📈 Determine the overall portrayal of a topic
- 🌐 Interactive interface built with Streamlit
- ⚠️ Handles articles that cannot be successfully extracted

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit** — Web application interface
- **NewsAPI** — News article retrieval
- **Newspaper3k** — Article extraction
- **NLTK** — Natural Language Processing and sentiment analysis
- **Regular Expressions (Regex)** — Text processing and cleaning

---

## 🔄 How It Works

The application follows a simple pipeline:

```text
User enters a topic
        ↓
NewsAPI retrieves relevant articles
        ↓
Article URLs are collected
        ↓
Newspaper3k attempts to extract article text
        ↓
Text is cleaned and processed
        ↓
NLTK performs sentiment analysis
        ↓
Sentiment results are aggregated
        ↓
Overall portrayal of the topic is displayed
```

---

## 📊 Sentiment Analysis

The project uses sentiment analysis to classify the extracted article content into positive and negative sentiment.

The results are aggregated across the successfully processed articles to provide an indication of how positively or negatively the searched topic is being portrayed.

This is **not intended to determine whether a news source is objectively biased**. It is simply an experimental way of using sentiment analysis to examine the language used when reporting on a particular topic.

---

## 🧩 Project Challenges

One of the main challenges with this project was **reliably extracting article content from different news websites**.

Different websites use different page structures, anti-bot systems, paywalls, and access restrictions. As a result, `newspaper3k` cannot successfully extract every article.

The application therefore handles extraction failures instead of assuming that every retrieved article can be processed.

This was also an important part of the project because it demonstrated that working with real-world web data is considerably less predictable than working with clean datasets.

---

## 📁 Project Structure

```text
News-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── ...
```
---

## 🔑 API

This project uses **NewsAPI** to retrieve news articles.

You will need your own API key to run the application.

Do not commit your API key directly to GitHub. Use an environment variable or Streamlit secrets instead.

---

## 📌 Limitations

- Article extraction does not work reliably for every news website.
- Some websites block automated requests.
- Paywalled or restricted articles may not be accessible.
- Sentiment analysis depends on the quality and context of the extracted text.
- Sentiment does not necessarily represent factual bias or political bias.
- The number of successfully analyzed articles can be lower than the number of articles initially retrieved.

---

## 🔮 Future Improvements

Some possible improvements include:

- Add more detailed sentiment visualizations
- Display positive/negative article counts
- Show the most positive and negative articles
- Improve article extraction reliability
- Add support for more news sources
- Compare sentiment across different news outlets
- Add article-level sentiment scores
- Improve text preprocessing
- Explore more advanced NLP models

---

## 🎯 What I Learned

This project helped me work with several concepts together rather than as isolated exercises:

- Working with external APIs
- Processing real-world data
- Web scraping and article extraction
- Regular expressions
- Natural Language Processing
- Sentiment analysis
- Error handling
- Streamlit application development
- Working with third-party libraries
- Dealing with unreliable external data

The biggest takeaway was that **real-world data is messy**. APIs, websites, and third-party services don't always behave consistently, and applications need to account for those failures.
