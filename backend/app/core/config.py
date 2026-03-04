from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    BACKEND_HOST = os.getenv("BACKEND_HOST")
    BACKEND_PORT = int(os.getenv("BACKEND_PORT"))
    ML_ENGINE_URL = os.getenv("ML_ENGINE_URL")

settings = Settings()
