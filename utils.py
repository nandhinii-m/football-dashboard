import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/players_data_light-2025_2026.csv")

    df["Comp"] = (
        df["Comp"]
        .astype(str)
        .str.split(n=1)
        .str[-1]
    )

    return df
