import pandas as pd
import pickle

# Load trained category model
with open("category_model.pkl", "rb") as f:
    category_model = pickle.load(f)

# Load dummy transactions
df = pd.read_csv("dummy_transactions.csv")

# Predict category using ML
df["predicted_category"] = category_model.predict(df["receiver"])

# Save enriched dataset
df.to_csv("enriched_transactions.csv", index=False)

print("✅ Transactions enriched with ML-based categories")
print(df)
