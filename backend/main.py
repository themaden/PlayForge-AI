import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.schemas import GeneratePromptRequest, PlayableGenerationResponse
from backend.app.orchestrator import AgentOrchestrator

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="PlayForge AI Platform Engine"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = AgentOrchestrator()

@app.get("/")
def root():
    return {
        "status": "online",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.post("/api/generate", response_model=PlayableGenerationResponse)
def generate_playable(request: GeneratePromptRequest):
    try:
        response = orchestrator.generate_playable(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/presets")
def get_presets():
    return [
        {
            "id": "royal_match",
            "name": "Royal Rescue Match-3",
            "prompt": "Create a 30-second Royal Match style puzzle save-the-king playable ad",
            "genre": "Match-3",
            "duration": 30,
            "theme": "Royal Rescue"
        },
        {
            "id": "hero_pull_pin",
            "name": "Pull-the-Pin Rescue",
            "prompt": "Create a 15-second Pull the pin hero puzzle save treasure dodging lava playable ad",
            "genre": "Pull-the-Pin",
            "duration": 15,
            "theme": "Dungeon Hero"
        },
        {
            "id": "castle_blast",
            "name": "Castle Defense Tile Blast",
            "prompt": "Create a 30-second color tile tap blast rebuild castle wall playable ad",
            "genre": "Tile Blast",
            "duration": 30,
            "theme": "Kingdom Defense"
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
