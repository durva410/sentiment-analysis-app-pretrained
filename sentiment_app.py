# sentiment_app_pretrained.py

import re
import streamlit as st
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def remove_links(text):
    return re.sub(r'http\S+|www.\S+', " ",text)
# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📝 Sentiment Analysis App")
st.write("Type any sentence below to get it's sentiment")

user_input = st.text_area("Enter your text:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        cleaned_input = remove_links(user_input)
        result = sentiment_pipeline(user_input)[0]
        label = result['label']
        score = result['score']

    
        emoji = "😀" if label == "POSITIVE" else "😡" if label == "NEGATIVE" else "😐"

        st.success(f"Sentiment: **{label} {emoji}** (Confidence: {score:.2f})")
    else:
        st.warning("Please enter a sentence before analyzing.")

    
