from flask import Flask, render_template, request
import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def assign_priority(text, category):
    text = text.lower()
    if "urgent" in text or "failed" in text or "error" in text:
        return "High"
    elif category in ["Hardware", "Access"]:
        return "Medium"
    else:
        return "Low"

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    priority = None
    confidence = None
    ticket_text = ""

    if request.method == 'POST':
        ticket = request.form['ticket']
        ticket_text = ticket

        cleaned = clean_text(ticket)
        vector = tfidf.transform([cleaned])

        pred = model.predict(vector)
        probs = model.predict_proba(vector)

        category = le.inverse_transform(pred)[0]
        confidence = round(max(probs[0]) * 100, 2)

        prediction = category
        priority = assign_priority(ticket, category)

    return render_template(
        'index.html',
        prediction=prediction,
        priority=priority,
        confidence=confidence,
        ticket=ticket_text
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001, use_reloader=False)