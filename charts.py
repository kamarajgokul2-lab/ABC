import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("spending_summary.csv")

# PIE CHART
plt.figure()
plt.pie(df["amount"], labels=df["predicted_category"], autopct="%1.1f%%")
plt.title("Spending Distribution by Category")
plt.savefig("static/pie_chart.png")
plt.close()

# BAR CHART
plt.figure()
plt.bar(df["predicted_category"], df["amount"])
plt.xlabel("Category")
plt.ylabel("Amount Spent")
plt.title("Spending by Category")
plt.savefig("static/bar_chart.png")
plt.close()

print("📊 Charts generated successfully")
