import uuid
import time
from backend.app.schemas import GeneratePromptRequest, PlayableGenerationResponse
from backend.app.agents.design_agent import GameDesignAgent
from backend.app.agents.code_agent import CodeGenerationAgent
from backend.app.agents.asset_agent import AssetGenerationAgent
from backend.app.agents.test_agent import GameplayTestingAgent
from backend.app.agents.optimize_agent import OptimizationAgent
from backend.app.exporter.ad_packager import AdPackagerEngine
from backend.app.local_models import MODEL_LOCK, generate_brief, generate_background, TEXT_MODEL, IMAGE_MODEL
from backend.app.browser_evaluation import evaluate_html

class AgentOrchestrator:
    def __init__(self):
        self.design_agent = GameDesignAgent()
        self.code_agent = CodeGenerationAgent()
        self.asset_agent = AssetGenerationAgent()
        self.test_agent = GameplayTestingAgent()
        self.optimize_agent = OptimizationAgent()
        self.exporter = AdPackagerEngine()

    def generate_playable(self, request: GeneratePromptRequest) -> PlayableGenerationResponse:
        started = time.perf_counter()
        project_id = f"pf_{uuid.uuid4().hex[:8]}"

        # Step 1: Game Design Agent
        concept = self.design_agent.process(request)
        provenance = {'text_provider': 'template', 'image_provider': 'fixed_svg', 'seed': request.seed}
        background = None
        if request.generate_images and request.generation_mode != 'local_ai':
            raise ValueError('Generated images require local_ai mode.')
        if request.generation_mode == 'local_ai':
            with MODEL_LOCK:
                brief = generate_brief(request.prompt)
                concept.title = brief.title
                concept.primary_goal = brief.instruction
                concept.cta_text = brief.cta
                provenance.update(text_provider='transformers', text_model=TEXT_MODEL,
                                  creative_brief=brief.model_dump(), instruction_source='tested_template')
                if request.generate_images:
                    background = generate_background(brief.image_prompt, request.seed)
                    provenance.update(image_provider='diffusers', image_model=IMAGE_MODEL,
                                      image_prompt=brief.image_prompt)

        # Step 2: Code Generation Agent
        generated_code = self.code_agent.process(concept, background)

        # Step 3: Asset Generation Agent
        assets = self.asset_agent.process(concept)
        if background:
            from backend.app.schemas import AssetSpec
            assets.append(AssetSpec(asset_id='generated_bg', name='Diffusion background',
                                    asset_type='background', svg_data='', image_data=background))

        # Step 4: Gameplay Testing Agent
        test_result = self.test_agent.process(concept, generated_code)

        # Step 5: Optimization Agent
        optimization_report = self.optimize_agent.process(concept, test_result)

        # Build Standalone HTML5 Ad Package
        export_html = self.exporter.package_ad(concept, generated_code, assets, request.target_network)
        runtime = evaluate_html(export_html, request.duration) if request.evaluate_browser else None

        return PlayableGenerationResponse(
            project_id=project_id,
            prompt=request.prompt,
            game_concept=concept,
            generated_code=generated_code,
            assets=assets,
            test_result=test_result,
            optimization_report=optimization_report,
            export_html=export_html,
            generation_duration_ms=round((time.perf_counter() - started) * 1000, 2)
            , generation_mode=request.generation_mode, provenance=provenance,
            runtime_evaluation=runtime
        )
