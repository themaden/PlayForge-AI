import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fastapi.testclient import TestClient
from backend.main import app

root = Path(__file__).resolve().parents[1]
out = root / 'docs' / 'examples'
original = json.loads((out / 'verification.json').read_text(encoding='utf-8'))
client = TestClient(app)
response = client.post('/api/projects/' + original['project_id'] + '/revise', json={
    'generation_mode': 'local_ai', 'generate_images': True, 'evaluate_browser': True})
if response.status_code != 200:
    raise RuntimeError(response.text)
revised = response.json()
(out / 'forest_revision.html').write_text(revised['export_html'], encoding='utf-8')
evidence = {key: value for key, value in revised.items() if key not in ['export_html', 'generated_code', 'assets']}
(out / 'revision_verification.json').write_text(json.dumps(evidence, indent=2), encoding='utf-8')
assert revised['parent_project_id'] == original['project_id']
assert revised['runtime_evaluation']['passed']
print('REVISION', revised['game_concept'], revised['runtime_evaluation'], flush=True)
print('Real feedback-conditioned revision verified. Review required on the new version.', flush=True)
