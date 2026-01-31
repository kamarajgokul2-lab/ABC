import pandas as pd
import pickle

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. Load dataset
df = pd.read_csv("transactions.csv")

print("Dataset loaded successfully")
print(df.head())

# 2. Features & labels
X = df["receiver"]
y = df["category"]

# 3. ML pipeline (Text → Vector → Classifier)
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

# 4. Train model
pipeline.fit(X, y)

# 5. Save model
with open("category_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Category model trained and saved as category_model.pkl")
