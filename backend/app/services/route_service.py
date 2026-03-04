import requests
from app.core.config import settings

def get_best_route(data):
    """
    Communicates with ML Engine
    """
    response = requests.post(settings.ML_ENGINE_URL, json=data)
    return response.json()
