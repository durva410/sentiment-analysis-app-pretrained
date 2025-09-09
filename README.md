# 📝 Sentiment Analysis App

A simple web app built with **Streamlit** and **Hugging Face Transformers** to analyze the sentiment of user input text.

## 🚀 Features
- Predicts **Positive**, **Negative**, or **Neutral** sentiment of user input.
- Displays prediction confidence score.
- Automatically removes links from input text.
- Interactive, user-friendly interface.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/durva410/sentiment-analysis-app-pretrained.git
   cd sentiment-analysis-app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

Run the Streamlit app:
```bash
streamlit run sentiment_app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## 📂 Project Structure
```
.
├── sentiment_app_pretrained.py   # Main app code
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

## 📦 Deployment
- You can deploy this app on **Hugging Face Spaces** (free) or **Streamlit Cloud**.
- Just upload your `sentiment_app_pretrained.py`, `requirements.txt`, and `README.md`.

## ✨ Example
Input:  
```
I love using this app!
```

Output:  
```
Sentiment: POSITIVE 😀 (Confidence: 0.99)
```
