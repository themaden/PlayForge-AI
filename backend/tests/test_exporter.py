import pytest
from backend.app.schemas import GeneratePromptRequest
from backend.app.orchestrator import AgentOrchestrator

def test_exporter_bundle_standalone():
    orchestrator = AgentOrchestrator()
    req = GeneratePromptRequest(prompt="Royal Match style match-3 save the king", target_network="Meta")
    res = orchestrator.generate_playable(req)
    
    assert res.export_html.startswith("<!DOCTYPE html>")
    assert "phaser.min.js" in res.export_html
    assert "PlayableScene" in res.export_html
    assert "FbPlayable" in res.export_html or "Meta" in res.export_html
