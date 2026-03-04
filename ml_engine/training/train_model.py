import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
from data_cleaning.clean_data import clean_traffic, clean_parking, clean_safety

# Load datasets
traffic = clean_traffic(pd.read_csv("datasets/raw/traffic.csv"))
parking = clean_parking(pd.read_csv("datasets/raw/parking.csv"))
safety = clean_safety(pd.read_csv("datasets/raw/safety.csv"))

# Merge simplified features
data = traffic.merge(parking, on="area").merge(safety, on="area")

X = data[["traffic_score", "availability_score", "risk_score"]]
y = 1 / (X.sum(axis=1))  # lower cost = better route

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "models/route_model.pkl")
print("✅ Model trained and saved")
