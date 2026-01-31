from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle

# ---------------- APP INIT ----------------
app = Flask(__name__)

# ---------------- LOAD FRAUD MODEL ----------------
clf = pickle.load(open("model.pkl", "rb"))

# ---------------- SIMPLE RULE-BASED CHATBOT ----------------
def chatbot_reply(user_message):
    msg = user_message.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return "Hello! 😊 How can I help you with fraud detection or transactions?"

    qa = {
        "why was my transaction flagged":
            "Your transaction was flagged due to high amount, unusual timing, or unknown merchant.",

        "what is fraud":
            "Fraud is an unauthorized or suspicious transaction that deviates from normal behavior.",

        "how does fraud detection work":
            "Fraud detection uses machine learning to analyze transaction patterns.",

        "what is fraud probability":
            "Fraud probability shows how likely a transaction is fraudulent.",

        "how can i avoid fraud":
            "Avoid fraud by not sharing OTPs and monitoring transactions regularly.",

        "why is my card blocked":
            "Your card may be temporarily blocked due to suspicious activity.",

        "what does high risk mean":
            "High risk means the transaction strongly deviates from normal behavior."
    }

    for question in qa:
        if question in msg:
            return qa[question]

    return "I can help with fraud detection, transaction status, and risk explanation."

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template("home.html")

# ---------------- FRAUD INPUT PAGE ----------------
@app.route('/fraud')
def fraud_page():
    return render_template("fraud.html")

# ---------------- FRAUD PREDICTION ----------------
@app.route('/predict', methods=['POST'])
def predict():
    raw = request.form.get('message', '').strip().split()

    if len(raw) != 30:
        return render_template(
            "fraud.html",
            error="Enter exactly 30 numeric values"
        )

    try:
        values = np.array(raw, dtype=float).reshape(1, -1)
    except ValueError:
        return render_template(
            "fraud.html",
            error="Only numeric values are allowed"
        )

    probability = round(clf.predict_proba(values)[0][1] * 100, 2)
    result = "Fraudulent" if probability >= 20 else "Legitimate"

    return render_template(
        "fraud.html",
        result=f"{result} transaction",
        probability=probability
    )

# ---------------- TRANSACTION TABLE ----------------
@app.route('/transactions')
def transactions():
    df = pd.read_csv("transaction_history.csv")
    data = df.to_dict(orient="records")

    return render_template(
        "transactions.html",
        data=data
    )

# ---------------- CHATBOT UI ----------------
@app.route('/assistant')
def assistant():
    return render_template("chat.html")

# ---------------- CHATBOT API ----------------
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get("message", "")
    reply = chatbot_reply(user_message)
    return jsonify({"reply": reply})

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)
