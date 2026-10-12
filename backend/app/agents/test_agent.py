from backend.app.schemas import GameConcept, TestResult

class GameplayTestingAgent:
    """Static checks; browser playability must be tested separately."""
    def process(self, concept: GameConcept, code: str) -> TestResult:
        checks = {
            "scene_class": "class PlayableScene extends Phaser.Scene" in code,
            "touch_handler": "pointerdown" in code and "setInteractive" in code,
            "win_condition": "checkWin()" in code and "targetScore" in code,
            "timeout_condition": "this.timeLeft <= 0" in code,
            "cta": "triggerCTA" in code,
        }
        return TestResult(is_playable=all(checks.values()), checks=checks,
            engagement_rating="Not measured", recommendations=[
            "Static checks cannot establish runtime playability or ad performance.",
            "Review tap response, timer, end screen and CTA in the preview."])
