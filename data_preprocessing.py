import pandas as pd
import os

df = pd.read_csv("dataset/synthetic/synthetic_semiconductor_supply_chain_1000_rows.csv")

df = df.drop_duplicates()

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

# Fill missing values instead of deleting rows
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(df[col].median())

os.makedirs("dataset/processed", exist_ok=True)
df.to_csv("dataset/processed/final_pcb_scm_dataset.csv", index=False)

print("✅ Data preprocessing completed")
print("Final shape:", df.shape)
print(df.head())