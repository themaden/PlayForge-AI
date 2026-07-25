from backend.app.schemas import GameConcept, GeneratePromptRequest

class GameDesignAgent:
    """Agent 1: Game Design Agent 🎮
    Formulates core playable game design, duration, win/fail conditions, and CTA specifications based on prompt.
    """

    def process(self, request: GeneratePromptRequest) -> GameConcept:
        prompt_lower = request.prompt.lower()

        if "pull" in prompt_lower or "pin" in prompt_lower:
            mechanic = "Pull-The-Pin"
            primary_goal = "Pull correct pins to drop treasure to hero while dodging lava"
            failure_hook = "Player pulls wrong pin, hero gets burned by lava!"
            title = "Hero Rescue Pin Challenge"
            cta_text = "SAVE THE HERO NOW!"
            colors = ["#f59e0b", "#ef4444", "#3b82f6", "#10b981"]
        elif "blast" in prompt_lower or "tile" in prompt_lower or "tap" in prompt_lower:
            mechanic = "Tile Blast"
            primary_goal = "Tap matching blocks to rebuild castle wall before time runs out"
            failure_hook = "Castle wall crumbles if tiles aren't blasted in 5 seconds!"
            title = "Castle Defense Tile Blast"
            cta_text = "REBUILD YOUR KINGDOM!"
            colors = ["#ec4899", "#8b5cf6", "#06b6d4", "#face15"]
        else:
            mechanic = "Match-3 Rescue"
            primary_goal = "Match 3 royal gems to break the cage and save the King"
            failure_hook = "Water rises in 10 seconds if match-3 fails!"
            title = "Castle Rescue Puzzle"
            cta_text = "PLAY TO SAVE THE KING!"
            colors = ["#e11d48", "#2563eb", "#059669", "#d97706"]

        return GameConcept(
            title=title,
            mechanic=mechanic,
            duration_seconds=request.duration,
            primary_goal=primary_goal,
            failure_hook=failure_hook,
            cta_text=cta_text,
            color_palette=colors
        )
