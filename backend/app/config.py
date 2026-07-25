import os
from pydantic import BaseModel

class Settings(BaseModel):
    PROJECT_NAME: str = "PlayForge AI"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    DEBUG: bool = True
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "demo_key")
    FLUX_API_KEY: str = os.getenv("FLUX_API_KEY", "demo_key")

settings = Settings()
