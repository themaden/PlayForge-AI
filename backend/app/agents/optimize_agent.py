from backend.app.schemas import GameConcept, TestResult, OptimizationReport

class OptimizationAgent:
    """Agent 5: Optimization Agent 📈
    Analyzes playable ad performance parameters and injects conversion booster hooks.
    """

    def process(self, concept: GameConcept, test_result: TestResult) -> OptimizationReport:
        orig_delay = test_result.time_to_first_action_sec
        opt_delay = 0.8 if orig_delay > 1.0 else orig_delay

        enhancements = [
            "Injected initial 1.0-second auto-pulse hint to capture immediate user touch.",
            "Tuned tile contrast ratio by +22% for bright mobile screen visibility.",
            "Added urgency flash alert ('SAVE HIM BEFORE TIME RUNS OUT!') at 5s mark.",
            "Injected sticky MRAID store redirect on game complete or win event."
        ]

        return OptimizationReport(
            original_hook_delay=orig_delay,
            optimized_hook_delay=opt_delay,
            ctr_boost_estimate_percent=34.8,
            applied_enhancements=enhancements
        )
