import os
import numpy as np
import pandas as pd

np.random.seed(42)

os.makedirs("data/train", exist_ok=True)
os.makedirs("data/test", exist_ok=True)


def generate_weather(days=200, anomaly=False):
    t = np.arange(days)

    # температура (сезонность)
    temperature = 10 + 15 * np.sin(t / 20) + np.random.normal(0, 2, days)

    # влажность
    humidity = 60 + 20 * np.sin(t / 15) + np.random.normal(0, 5, days)

    # давление
    pressure = 1010 + np.random.normal(0, 3, days)

    if anomaly:
        idx = np.random.randint(0, days)
        temperature[idx] += np.random.randint(15, 25)
        humidity[idx] -= np.random.randint(20, 40)

    df = pd.DataFrame({
        "day": t,
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    })

    # пропуски
    for col in ["temperature", "humidity", "pressure"]:
        mask = np.random.rand(days) < 0.05
        df.loc[mask, col] = np.nan

    return df


# train datasets
for i in range(5):
    df = generate_weather(200)
    df.to_csv(f"data/train/train_{i}.csv", index=False)

# test datasets (с аномалиями)
for i in range(3):
    df = generate_weather(200, anomaly=True)
    df.to_csv(f"data/test/test_{i}.csv", index=False)

print("Datasets created successfully")