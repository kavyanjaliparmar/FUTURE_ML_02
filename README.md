# 🚀 Support Ticket Classifier

An end-to-end Machine Learning web application that classifies support tickets and assigns priority levels in real-time using Natural Language Processing (NLP).

---

## 🔍 Overview

This project takes user-submitted support queries and predicts:

- Ticket Category (e.g., Hardware, Access, Software)
- Priority Level (High / Medium / Low)
- Confidence Score

It combines NLP techniques with a Logistic Regression model and is deployed using a Flask-based web interface.

---

## 🧠 How It Works

1. User enters a support ticket (query)
2. Text is preprocessed:
   - Lowercasing
   - Removing special characters
   - Stopword removal using NLTK
3. Text is converted into numerical features using TF-IDF Vectorization
4. A Logistic Regression model predicts the ticket category
5. Priority is assigned using rule-based logic:
   - High → keywords like "urgent", "error", "failed"
   - Medium → categories like Hardware, Access
   - Low → remaining cases
6. Confidence score is calculated using model probabilities

---

## ⚙️ Tech Stack

- Python
- Flask
- Scikit-learn
- NLTK
- HTML + CSS

---

## 💡 Features

- Real-time ticket classification
- NLP-based preprocessing
- TF-IDF feature extraction
- Logistic Regression model
- Priority prediction system
- Confidence score visualization
- Interactive UI

---

## 🚀 Future Improvements

- Upgrade model using BERT / deep learning
- Add database for ticket history
- Deploy on cloud (Render / AWS)
- Real-time predictions without page reload

---

## ⭐ Acknowledgment

Built as a machine learning + web integration project to demonstrate practical NLP applications.
