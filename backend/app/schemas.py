from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class GeneratePromptRequest(BaseModel):
    prompt: str = Field(..., min_length=3, max_length=2000)
    genre: str = Field("Match-3", example="Match-3")
    duration: int = Field(30, ge=5, le=60)
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
    validation_method: str = "static_code_checks"
    checks: Dict[str, bool] = Field(default_factory=dict)
    time_to_first_action_sec: Optional[float] = None
    difficulty_score: Optional[float] = None
    engagement_rating: str
    fps_estimate: Optional[int] = None
    recommendations: List[str]

class OptimizationReport(BaseModel):
    original_hook_delay: Optional[float] = None
    optimized_hook_delay: Optional[float] = None
    ctr_boost_estimate_percent: Optional[float] = None
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
    generation_mode: str = "local_template"
    generation_duration_ms: float = 0
