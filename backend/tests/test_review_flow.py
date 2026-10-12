import pytest
from fastapi.testclient import TestClient
from backend.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv('PLAYFORGE_DB', str(tmp_path / 'review.sqlite3'))
    return TestClient(app)


def test_generation_and_persistent_review(client):
    response = client.post('/api/generate', json={'prompt': 'A royal puzzle', 'duration': 15})
    assert response.status_code == 200
    project = response.json()
    assert project['test_result']['fps_estimate'] is None
    assert project['optimization_report']['ctr_boost_estimate_percent'] is None
    assert project['generation_duration_ms'] > 0
    url = '/api/projects/' + project['project_id']
    assert client.get(url).json()['review_status'] == 'pending'
    assert client.post(url + '/review', json={'decision': 'changes_requested', 'feedback': 'Make the instruction clearer'}).status_code == 200
    assert client.post(url + '/review', json={'decision': 'approved'}).status_code == 200
    saved = client.get(url).json()
    assert saved['review_status'] == 'approved'
    assert len(saved['reviews']) == 2


def test_invalid_and_missing_reviews(client):
    assert client.post('/api/projects/missing/review', json={'decision': 'approved'}).status_code == 404
    assert client.post('/api/projects/missing/review', json={'decision': 'changes_requested', 'feedback': ' '}).status_code == 422


def test_unsupported_mechanic_and_bad_duration(client):
    assert client.post('/api/generate', json={'prompt': 'pull the pin'}).status_code == 422
    assert client.post('/api/generate', json={'prompt': 'A royal puzzle', 'duration': -5}).status_code == 422
