from fastapi import FastAPI
from app.api.route import router as route_router
from app.core.cors import setup_cors
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

setup_cors(app)

app.include_router(route_router)

@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}
