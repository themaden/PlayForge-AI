# PlayForge AI - REST API Specifications

The PlayForge AI backend exposes OpenAPI/Swagger compliant endpoints for programmatic playable ad generation.

## Endpoints

### 1. `POST /api/generate`
Generates a complete standalone HTML5 playable ad from a prompt.

**Request Body:**
```json
{
  "prompt": "Create a 30-second Royal Match style puzzle save-the-king playable ad",
  "genre": "Match-3",
  "duration": 30,
  "target_network": "Meta",
  "theme": "Royal Rescue"
}
```

**Response:**
Returns `PlayableGenerationResponse` containing `project_id`, `game_concept`, `generated_code`, `assets`, `test_result`, `optimization_report`, and `export_html`.

### 2. `GET /api/presets`
Returns predefined high-converting playable ad prompts and configs.

### 3. `GET /api/health`
Health check endpoint returning `{"status": "ok"}`.
