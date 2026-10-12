"""Reproduce a real local-model output and its revision; no mocks."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from backend.app.orchestrator import AgentOrchestrator
from backend.app.schemas import GeneratePromptRequest
from backend.app.reviews import save_project, save_review

root = Path(__file__).resolve().parents[1]
out = root / 'docs' / 'examples'
out.mkdir(parents=True, exist_ok=True)
engine = AgentOrchestrator()
request = GeneratePromptRequest(
    prompt='Create a forest rescue tap puzzle. Use a green enchanted forest background with no text. Keep the CTA short.',
    duration=5, generation_mode='local_ai', generate_images=True, evaluate_browser=True)
result = engine.generate_playable(request)
save_project(result)
save_review(result.project_id, 'changes_requested', 'Change the title to Forest Gems and the CTA to PLAY NOW.')
(out / 'forest_playable.html').write_text(result.export_html, encoding='utf-8')
evidence = result.model_dump(exclude={'export_html', 'generated_code', 'assets'})
(out / 'verification.json').write_text(json.dumps(evidence, indent=2), encoding='utf-8')
print('FIRST_OUTPUT', result.project_id, result.provenance, result.runtime_evaluation, flush=True)
if not result.runtime_evaluation['passed']:
    raise RuntimeError('Generated playable failed browser evaluation')
print('Verified real LLM + diffusion + browser flow.', flush=True)
