from backend.app.schemas import GameConcept, TestResult, OptimizationReport

class OptimizationAgent:
    """No performance claims without measurements."""
    def process(self, concept: GameConcept, test_result: TestResult) -> OptimizationReport:
        return OptimizationReport(applied_enhancements=[])
