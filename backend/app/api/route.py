from fastapi import APIRouter
from app.schemas.route import RouteRequest, RouteResponse
from app.services.route_service import get_best_route

router = APIRouter()

@router.post("/route", response_model=RouteResponse)
def calculate_route(request: RouteRequest):
    result = get_best_route(request.dict())
    return result
