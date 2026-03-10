import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score

test_df = pd.read_csv("data/processed/test_processed.csv")

X_test = test_df[["day", "humidity", "pressure"]]
y_test = test_df["temperature"]

model = joblib.load("models/model.pkl")
y_pred = model.predict(X_test)

# метрики
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model evaluation:")
print(f"MSE: {mse}")
print(f"R2 score: {r2}")