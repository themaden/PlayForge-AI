import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.schemas import GeneratePromptRequest, PlayableGenerationResponse
from backend.app.orchestrator import AgentOrchestrator
from backend.app.reviews import save_project, get_project, save_review
from pydantic import BaseModel, Field, model_validator
from typing import Literal

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
        save_project(response)
        return response
    except NotImplementedError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class ReviewRequest(BaseModel):
    decision: Literal['approved', 'changes_requested']
    feedback: str = Field('', max_length=2000)

    @model_validator(mode='after')
    def require_feedback(self):
        self.feedback = self.feedback.strip()
        if self.decision == 'changes_requested' and not self.feedback:
            raise ValueError('Describe the requested changes.')
        return self


@app.get('/api/projects/{project_id}')
def read_project(project_id: str):
    result = get_project(project_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Project not found')
    return result


@app.post('/api/projects/{project_id}/review')
def review_project(project_id: str, review: ReviewRequest):
    project = get_project(project_id)
    if project and review.decision == 'approved' and project.get('runtime_evaluation') and not project['runtime_evaluation']['passed']:
        raise HTTPException(status_code=409, detail='Resolve failed browser checks before approving.')
    try:
        return save_review(project_id, review.decision, review.feedback)
    except KeyError:
        raise HTTPException(status_code=404, detail='Project not found')


class RevisionRequest(BaseModel):
    generation_mode: Literal['local_template', 'local_ai'] = 'local_ai'
    generate_images: bool = False
    evaluate_browser: bool = False


@app.post('/api/projects/{project_id}/revise')
def revise_project(project_id: str, revision: RevisionRequest):
    original = get_project(project_id)
    if original is None:
        raise HTTPException(status_code=404, detail='Project not found')
    if original['review_status'] != 'changes_requested':
        raise HTTPException(status_code=409, detail='Request changes with feedback before creating a revision.')
    feedback = original['reviews'][-1]['feedback']
    prompt = (original['prompt'] + '\nReviewer feedback: ' + feedback)
    if len(prompt) > 2000:
        raise HTTPException(status_code=422, detail='Brief and feedback exceed the 2000-character limit.')
    try:
        request = GeneratePromptRequest(prompt=prompt, duration=original['game_concept']['duration_seconds'],
            generation_mode=revision.generation_mode, generate_images=revision.generate_images,
            evaluate_browser=revision.evaluate_browser, seed=original['provenance'].get('seed', 42))
        result = orchestrator.generate_playable(request)
        result.parent_project_id = project_id
        result.provenance['review_feedback'] = feedback
        save_project(result)
        return result
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error))
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))

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
