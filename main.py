import streamlit as st
import backend

st.title(":blue[_NEWS_]-ANALYSIS", text_alignment="center")
topic = st.text_input("Enter topic")

if topic:
    start = st.date_input("ENTER FROM DATE: ",value=None)
    end = st.date_input("ENTER TO DATE: ",value=None)

    if start and end:

        content = backend.get_api(topic,start,end)
        counter, f_counter, pos_counter,neg_counter, neu_counter, f_elapsed = backend.get_articles(content,topic)

        st.subheader(f"Positive articles: :blue[{pos_counter}]")
        st.subheader(f"Negative articles: :blue[{neg_counter}]")
        st.subheader(f"Neutral articles: :blue[{neu_counter}]")
        st.subheader(f":blue[{counter}] of :green[{len(content["articles"])}] displayed")
        st.subheader(f":red[{f_counter}] articles failed")
        st.subheader(f":red[{f_elapsed}]")
