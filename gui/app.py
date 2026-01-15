import streamlit as st
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    if blob.sentiment.polarity > 0:
        return "Positive 😊"
    elif blob.sentiment.polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

st.title("Sentiment Analysis App")
st.write("Enter text below to analyze sentiment.")

user_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    result = analyze_sentiment(user_input)
    st.success(f"Sentiment: {result}")
