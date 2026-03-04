from pydantic import BaseModel

class RouteRequest(BaseModel):
    source: str
    destination: str
    travel_mode: str  # car, bike, walk

class RouteResponse(BaseModel):
    best_route: str
    score: float
    explanation: list
