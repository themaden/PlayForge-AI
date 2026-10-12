from backend.app.local_models import CreativeBrief
from backend.app.orchestrator import AgentOrchestrator
from backend.app.schemas import GeneratePromptRequest
from fastapi.testclient import TestClient
from backend.main import app
import pytest


def fake_brief(prompt):
    return CreativeBrief(title='Forest Gems', instruction='Tap three different gems', cta='PLAY NOW', image_prompt='Green forest game background with no text')


def test_ai_provenance_and_safe_text(monkeypatch):
    monkeypatch.setattr('backend.app.orchestrator.generate_brief', fake_brief)
    result = AgentOrchestrator().generate_playable(GeneratePromptRequest(prompt='forest', generation_mode='local_ai'))
    assert result.generation_mode == 'local_ai'
    assert result.provenance['text_provider'] == 'transformers'
    assert result.game_concept.title == 'Forest Gems'
    assert 'Forest Gems' in result.generated_code
    assert result.provenance['image_provider'] == 'fixed_svg'


def test_model_failure_has_no_template_fallback(monkeypatch):
    def fail(prompt):
        raise ValueError('Invalid model JSON')
    monkeypatch.setattr('backend.app.orchestrator.generate_brief', fail)
    with pytest.raises(ValueError, match='Invalid model JSON'):
        AgentOrchestrator().generate_playable(GeneratePromptRequest(prompt='forest', generation_mode='local_ai'))


def test_revision_link_and_feedback(tmp_path, monkeypatch):
    monkeypatch.setenv('PLAYFORGE_DB', str(tmp_path / 'revision.sqlite3'))
    client = TestClient(app)
    original = client.post('/api/generate', json={'prompt': 'royal puzzle'}).json()
    url = '/api/projects/' + original['project_id']
    assert client.post(url + '/revise', json={}).status_code == 409
    client.post(url + '/review', json={'decision': 'changes_requested', 'feedback': 'Change title to Forest Gems'})
    seen = []
    def brief(prompt):
        seen.append(prompt)
        return fake_brief(prompt)
    monkeypatch.setattr('backend.app.orchestrator.generate_brief', brief)
    response = client.post(url + '/revise', json={'generation_mode': 'local_ai'})
    assert response.status_code == 200
    revised = response.json()
    assert revised['parent_project_id'] == original['project_id']
    assert 'Change title to Forest Gems' in seen[0]
    assert client.get('/api/projects/' + revised['project_id']).json()['review_status'] == 'pending'


def test_script_termination_is_escaped():
    from backend.app.agents.code_agent import CodeGenerationAgent
    from backend.app.schemas import GameConcept
    concept = GameConcept(title='</script><script>alert(1)</script>', mechanic='Tap Puzzle',
        duration_seconds=5, primary_goal='Tap gems', failure_hook='Timeout',
        cta_text="It's time", color_palette=['#ffffff'])
    code = CodeGenerationAgent().process(concept)
    assert '</script>' not in code
    assert '\\u003c' in code


def test_failed_browser_evaluation_blocks_approval(tmp_path, monkeypatch):
    monkeypatch.setenv('PLAYFORGE_DB', str(tmp_path / 'failed.sqlite3'))
    monkeypatch.setattr('backend.app.orchestrator.evaluate_html', lambda html, duration: {'passed': False, 'checks': {'win': False}})
    client = TestClient(app)
    project = client.post('/api/generate', json={'prompt': 'royal puzzle', 'evaluate_browser': True}).json()
    response = client.post('/api/projects/' + project['project_id'] + '/review', json={'decision': 'approved'})
    assert response.status_code == 409
