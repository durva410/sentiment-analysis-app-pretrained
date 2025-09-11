# 📊 Sentiment Analysis Web App

A simple **Sentiment Analysis Web Application** built with [Streamlit](https://streamlit.io/) that analyzes text and classifies it into sentiments (Positive, Negative, Neutral).  
It integrates **Hugging Face Transformers**, **NLTK**, and emoji preprocessing for richer text analysis.  

---

## 🚀 Features
- ✅ Real-time text sentiment classification  
- ✅ Emoji-to-text conversion (😃 → :smile:)  
- ✅ Sentence tokenization with NLTK  
- ✅ Hugging Face Transformers integration  
- ✅ Optional Hugging Face / OpenAI API support  
- ✅ Interactive UI powered by Streamlit  

---

## 📂 Project Structure
```
sentiment-analysis-app/
│-- sentiment_app.py       # Main application script
│-- requirements.txt       # Python dependencies
│-- README.md              # Documentation
```

---

## 🛠 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK tokenizer (first run only)**
   ```python
   import nltk
   nltk.download('punkt')
   ```

---

## 🔑 API Keys (Optional)
If you want to use Hugging Face Inference API or OpenAI models:

1. **Get Hugging Face Token** → [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  
2. **Get OpenAI API Key** → [https://platform.openai.com](https://platform.openai.com)  
3. Set them as environment variables:

Linux/Mac:
```bash
export HF_API_KEY="your_huggingface_api_key"
export OPENAI_API_KEY="your_openai_api_key"
```

Windows (CMD):
```cmd
set HF_API_KEY=your_huggingface_api_key
set OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Running the App
Start the Streamlit server:
```bash
streamlit run sentiment_app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501).  

---

## 📊 Example
**Input:**  
```
I love this app 😍 but the UI could be better.
```

**Output:**  
- Sentiment: *Neutral / Mixed*  
- Positive words: *love, 😍*  
- Negative words: *better*  

---

## 📜 License
This project is licensed under the MIT License.  

---

## 🙌 Acknowledgements
- [Streamlit](https://streamlit.io/)  
- [Hugging Face Transformers](https://huggingface.co/transformers/)  
- [NLTK](https://www.nltk.org/)  
- [Emoji](https://pypi.org/project/emoji/)  
