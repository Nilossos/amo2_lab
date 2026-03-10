import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(folder):
    dataframes = []
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder, file))
            dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True)


# загрузка данных
train_df = load_data("data/train")
test_df = load_data("data/test")

# заполнение пропусков
train_df = train_df.fillna(train_df.median())
test_df = test_df.fillna(test_df.median())

# признаки
features = ["temperature", "humidity", "pressure"]

scaler = StandardScaler()

train_df[features] = scaler.fit_transform(train_df[features])
test_df[features] = scaler.transform(test_df[features])

# сохраняем
os.makedirs("data/processed", exist_ok=True)

train_df.to_csv("data/processed/train_processed.csv", index=False)
test_df.to_csv("data/processed/test_processed.csv", index=False)

print("Preprocessing completed")