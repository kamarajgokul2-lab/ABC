import pandas as pd

# Load enriched transactions
df = pd.read_csv("enriched_transactions.csv")

# Calculate total spend per category
summary = df.groupby("predicted_category")["amount"].sum().reset_index()

print("\n💰 Spending Summary:")
print(summary)

# Save summary for UI usage
summary.to_csv("spending_summary.csv", index=False)
