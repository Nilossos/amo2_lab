import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

train_df = pd.read_csv("data/processed/train_processed.csv")

# признаки и таргет
X = train_df[["day", "humidity", "pressure"]]
y = train_df["temperature"]

model = LinearRegression()
model.fit(X, y)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")

print("Model trained and saved to models/model.pkl")