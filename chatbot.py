def chatbot_reply(user_message):
    msg = user_message.lower().strip()

    # greetings
    if msg in ["hi", "hello", "hey"]:
        return "Hello! 😊 You can ask me about fraud detection or transactions."

    qa = {
        "why was my transaction flagged":
            "Your transaction was flagged due to unusual amount, time, or merchant behavior.",

        "what is fraud":
            "Fraud is an unauthorized or suspicious transaction that deviates from normal behavior.",

        "how does fraud detection work":
            "We use machine learning to analyze transaction patterns and assign a fraud probability.",

        "what is fraud probability":
            "Fraud probability shows how likely a transaction is fraudulent.",

        "how can i avoid fraud":
            "Avoid fraud by not sharing OTPs, monitoring transactions, and using secure platforms.",

        "why is my card blocked":
            "Your card may be temporarily blocked due to suspicious activity.",

        "what does high risk mean":
            "High risk means the transaction strongly deviates from normal spending behavior."
    }

    for question in qa:
        if question in msg:
            return qa[question]

    return "I can help with fraud detection, transaction status, and risk explanation."
