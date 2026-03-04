import pandas as pd

def clean_traffic(df):
    df = df.dropna()
    df["traffic_score"] = df["traffic_level"].map({
        "Low": 1,
        "Medium": 2,
        "High": 3
    })
    return df

def clean_parking(df):
    df = df.dropna()
    df["availability_score"] = 1 - df["occupancy"]
    return df

def clean_safety(df):
    df = df.dropna()
    df["risk_score"] = df["crime_rate"]
    return df
