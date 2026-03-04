from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="UrbanSense ML Engine")

MODEL_PATH = os.getenv("MODEL_PATH")
model = joblib.load(MODEL_PATH)

class RouteInput(BaseModel):
    traffic_score: float
    availability_score: float
    risk_score: float

@app.post("/predict")
def predict_route(data: RouteInput):
    score = model.predict([[data.traffic_score,
                             data.availability_score,
                             data.risk_score]])[0]

    explanation = []
    if data.traffic_score < 2:
        explanation.append("Low traffic")
    if data.availability_score > 0.5:
        explanation.append("Good parking availability")
    if data.risk_score < 5:
        explanation.append("Safe route")

    return {
        "best_route": "Route-A",
        "score": round(float(score), 2),
        "explanation": explanation
    }

@app.get("/")
def health():
    return {"status": "ML Engine running"}
