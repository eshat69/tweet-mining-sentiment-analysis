import streamlit as st
import pickle
import re
from nltk.stem import WordNetLemmatizer

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Twitter Sentiment Analysis",
    page_icon="🐦",
    layout="centered"
)

# -----------------------------
# Load Model & Vectorizer
# -----------------------------
@st.cache_resource
def load_model():
    with open("svm_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("vec_model.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer

model, vectorizer = load_model()
lemmatizer = WordNetLemmatizer()

# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)

# -----------------------------
# Prediction
# -----------------------------
def predict(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return prediction

# -----------------------------
# User Interface
# -----------------------------
st.title("🐦 Twitter Sentiment Analysis")
st.markdown("### Predict Tweet Sentiment using Linear SVM")

tweet = st.text_area(
    "Enter Tweet",
    height=180,
    placeholder="Type a tweet here..."
)

if st.button("Predict"):

    if tweet.strip() == "":
        st.warning("Please enter a tweet.")
    else:

        pred = predict(tweet)
        if pred == 0:
            st.error("😠 Negative")
        elif pred == 1:
            st.success("😊 Positive")
        elif pred == 2:
            st.info("😐 Neutral")
        elif pred == 3:
            st.warning("🤔 Irrelevant")
        else:
            st.write(f"Prediction: {pred}")

        st.markdown("---")
        st.write("**Original Tweet:**")
        st.write(tweet)