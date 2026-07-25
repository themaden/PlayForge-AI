import uuid
from backend.app.schemas import GeneratePromptRequest, PlayableGenerationResponse
from backend.app.agents.design_agent import GameDesignAgent
from backend.app.agents.code_agent import CodeGenerationAgent
from backend.app.agents.asset_agent import AssetGenerationAgent
from backend.app.agents.test_agent import GameplayTestingAgent
from backend.app.agents.optimize_agent import OptimizationAgent
from backend.app.exporter.ad_packager import AdPackager Engine

class AgentOrchestrator:
    def __init__(self):
        self.design_agent = GameDesignAgent()
        self.code_agent = CodeGenerationAgent()
        self.asset_agent = AssetGenerationAgent()
        self.test_agent = GameplayTestingAgent()
        self.optimize_agent = OptimizationAgent()
        self.exporter = AdPackagerEngine()

    def generate_playable(self, request: GeneratePromptRequest) -> PlayableGenerationResponse:
        project_id = f"pf_{uuid.uuid4().hex[:8]}"

        # Step 1: Game Design Agent
        concept = self.design_agent.process(request)

        # Step 2: Code Generation Agent
        generated_code = self.code_agent.process(concept)

        # Step 3: Asset Generation Agent
        assets = self.asset_agent.process(concept)

        # Step 4: Gameplay Testing Agent
        test_result = self.test_agent.process(concept, generated_code)

        # Step 5: Optimization Agent
        optimization_report = self.optimize_agent.process(concept, test_result)

        # Build Standalone HTML5 Ad Package
        export_html = self.exporter.package_ad(concept, generated_code, assets, request.target_network)

        return PlayableGenerationResponse(
            project_id=project_id,
            prompt=request.prompt,
            game_concept=concept,
            generated_code=generated_code,
            assets=assets,
            test_result=test_result,
            optimization_report=optimization_report,
            export_html=export_html
        )
