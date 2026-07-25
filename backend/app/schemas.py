from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class GeneratePromptRequest(BaseModel):
    prompt: str = Field(..., example="Create a 30-second Royal Match puzzle save-the-king playable ad")
    genre: str = Field("Match-3", example="Match-3")
    duration: int = Field(30, example=30)
    target_network: str = Field("Meta", example="Meta")
    theme: Optional[str] = Field("Royal Rescue", example="Royal Rescue")

class GameConcept(BaseModel):
    title: str
    mechanic: str
    duration_seconds: int
    primary_goal: str
    failure_hook: str
    cta_text: str
    color_palette: List[str]

class AssetSpec(BaseModel):
    asset_id: str
    name: str
    asset_type: str  # background, character, object, hand_tutorial, cta_banner
    svg_data: str

class TestResult(BaseModel):
    is_playable: bool
    time_to_first_action_sec: float
    difficulty_score: float
    engagement_rating: str
    fps_estimate: int
    recommendations: List[str]

class OptimizationReport(BaseModel):
    original_hook_delay: float
    optimized_hook_delay: float
    ctr_boost_estimate_percent: float
    applied_enhancements: List[str]

class PlayableGenerationResponse(BaseModel):
    project_id: str
    prompt: str
    game_concept: GameConcept
    generated_code: str
    assets: List[AssetSpec]
    test_result: TestResult
    optimization_report: OptimizationReport
    export_html: str
