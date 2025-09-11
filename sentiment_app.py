# sentiment_ai_simple.py

import streamlit as st
import re
import emoji
import nltk
from transformers import pipeline
from collections import Counter
import os
import openai

# NLTK Setup
nltk.download('punkt', quiet=True)
from nltk.tokenize import sent_tokenize

# Text Cleaning
def clean_text(text):
    text = emoji.demojize(text)
    text = re.sub(r"http\S+|www.\S+", " ", text)
    text = re.sub(r"[^A-Za-z\s:]", "", text)
    return re.sub(r"\s+", " ", text.lower().strip())

# Load Sentiment Model
@st.cache_resource(show_spinner=True)
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

sentiment_model = load_model()

# Sentiment Analysis
def analyze_sentiment(text):
    label_map = {"LABEL_0": "NEGATIVE", "LABEL_1": "NEUTRAL", "LABEL_2": "POSITIVE"}
    
    results = [
        {**res, "label": label_map.get(res['label'], res['label'])}
        for sentence in sent_tokenize(text)
        for res in [sentiment_model(clean_text(sentence))[0]]
    ]
    
    labels = [r['label'] for r in results]
    overall = Counter(labels).most_common(1)[0][0]
    avg_score = sum(r['score'] for r in results) / len(results)
    
    return overall, avg_score, results

# OpenAI GPT Response
openai.api_key = os.getenv("OPENAI_API_KEY")

def ai_response(prompt):
    if not openai.api_key:
        return None
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=150
        )
        return resp['choices'][0]['message']['content']
    except Exception as e:
        print("OpenAI API error:", e)
        return None

# Streamlit App UI
st.set_page_config(page_title="AI-Enhanced Sentiment Analyzer", layout="wide")
st.title("💬 AI-Enhanced Sentiment Analysis App")

user_input = st.text_area("Enter text here:", height=200)

if st.button("Analyze Sentiment") and user_input.strip():
    overall, avg_score, sentence_results = analyze_sentiment(user_input)
    
    st.subheader("Overall Sentiment")
    st.success(f"{overall} (Confidence: {avg_score:.2f})")
    
    st.subheader("Sentence-level Analysis")
    colors = {"POSITIVE": "green", "NEGATIVE": "red", "NEUTRAL": "gray"}
    for i, r in enumerate(sentence_results, 1):
        st.markdown(
            f"<span style='color:{colors[r['label']]}'>Sentence {i}: {r['label']} (Confidence: {r['score']:.2f})</span>",
            unsafe_allow_html=True
        )
    
    st.subheader("AI Response")
    prompt = f"User wrote: {user_input}\nSentiment: {overall}\nProvide a friendly, helpful AI response:"
    response_text = ai_response(prompt)
    
    if response_text:
        st.info(response_text)
    else:
        st.warning(
            "🤖 AI response is unavailable due to quota limitation error, please chek after some time."
        )
else:
    st.info("Enter some text and click 'Analyze Sentiment'.")
