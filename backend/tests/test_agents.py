import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from backend.app.schemas import GeneratePromptRequest
from backend.app.agents.design_agent import GameDesignAgent
from backend.app.agents.code_agent import CodeGenerationAgent
from backend.app.agents.asset_agent import AssetGenerationAgent
from backend.app.agents.test_agent import GameplayTestingAgent
from backend.app.agents.optimize_agent import OptimizationAgent

def test_design_agent_match3():
    agent = GameDesignAgent()
    req = GeneratePromptRequest(prompt="Royal Match puzzle save king", duration=30, target_network="Meta")
    concept = agent.process(req)
    assert concept.mechanic == "Tap Puzzle"
    assert concept.duration_seconds == 30

def test_code_agent_generation():
    design_agent = GameDesignAgent()
    code_agent = CodeGenerationAgent()
    req = GeneratePromptRequest(prompt="Royal Match puzzle save king", duration=30)
    concept = design_agent.process(req)
    code = code_agent.process(concept)
    assert "PlayableScene" in code
    assert "Phaser.Scene" in code

def test_asset_agent_synthesis():
    design_agent = GameDesignAgent()
    asset_agent = AssetGenerationAgent()
    req = GeneratePromptRequest(prompt="Royal Match", duration=30)
    concept = design_agent.process(req)
    assets = asset_agent.process(concept)
    assert len(assets) >= 3
    assert any(a.asset_type == "hand_tutorial" for a in assets)

def test_testing_agent():
    design_agent = GameDesignAgent()
    code_agent = CodeGenerationAgent()
    test_agent = GameplayTestingAgent()
    req = GeneratePromptRequest(prompt="Royal Match", duration=30)
    concept = design_agent.process(req)
    code = code_agent.process(concept)
    res = test_agent.process(concept, code)
    assert res.is_playable is True
    assert res.time_to_first_action_sec is None
    assert all(res.checks.values())
