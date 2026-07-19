https://tweet-mining-sentiment-analysis.streamlit.app/ 
# 🐦 Tweet Mining Sentiment Analysis

A Machine Learning-based Twitter Sentiment Analysis application that classifies tweets into four sentiment categories using Natural Language Processing (NLP) and a Linear Support Vector Machine (SVM). The project also includes a Streamlit web application for real-time sentiment prediction.

---

## 📌 Project Overview

This project analyzes tweets and predicts their sentiment using NLP preprocessing techniques and machine learning models. It demonstrates the complete workflow from data preprocessing to model deployment.

### Sentiment Classes

- 😊 Positive
- 😠 Negative
- 😐 Neutral
- 🤔 Irrelevant

<img width="1472" height="989" alt="word cloud" src="https://github.com/user-attachments/assets/7dfea4cc-2eb5-4ae6-9ca9-107af1be81a2" />

---

## 🚀 Features

- Tweet text preprocessing
- Text vectorization using CountVectorizer
- Linear SVM classifier
- Interactive Streamlit web application
- Real-time sentiment prediction
- Clean and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Streamlit
- Pickle

---

## 📂 Project Structure

```
tweet-mining-sentiment-analysis/
│
├── app.py
├── tweet_mining.ipynb
├── svm_model.pkl
├── vec_model.pkl
├── requirements.txt
├── README.md
└── assets/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/eshat69/tweet-mining-sentiment-analysis.git
```

Navigate to the project

```bash
cd tweet-mining-sentiment-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Machine Learning Pipeline

1. Load Dataset
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction using CountVectorizer
5. Model Training
6. Model Evaluation
7. Save Model
8. Streamlit Deployment

---


## 📊 Model Performance

The project evaluates multiple machine learning algorithms for tweet sentiment classification. The comparison below shows the training and testing accuracy of each model.

| Model | Training Accuracy | Testing Accuracy |
|-------|------------------:|-----------------:|
| Naive Bayes | **97.17%** | **80.43%** |
| Decision Tree | **78.85%** | **73.31%** |
| Logistic Regression | **88.64%** | **79.73%** |
| **Linear SVM (Best Model)** | **90.72%** | **82.55%** |


**Classifier**

- Linear Support Vector Machine (LinearSVC)

**Feature Extraction**

- CountVectorizer

---

## 🖥️ Demo

Input a tweet such as:

```
I absolutely love this product!
```

Prediction:

```
😊 Positive
```

---

## 📦 Requirements

```
streamlit
scikit-learn
pandas
numpy
nltk
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 📚 Future Improvements

- Deep Learning (LSTM/BERT)
- Twitter API Integration
- Model Comparison Dashboard
- Explainable AI (SHAP/LIME)
- Docker Deployment
- Cloud Deployment

---

## 👨‍💻 Author

**Eshat**

- GitHub: https://github.com/eshat69

