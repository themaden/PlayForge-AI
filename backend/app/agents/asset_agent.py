from typing import List
from backend.app.schemas import GameConcept, AssetSpec

class AssetGenerationAgent:
    """Agent 3: Asset Generation Agent 🎨
    Generates optimized playable SVG & inline raster graphical assets.
    """

    def process(self, concept: GameConcept) -> List[AssetSpec]:
        assets = [
            AssetSpec(
                asset_id="bg_01",
                name="Royal Dungeon Background",
                asset_type="background",
                svg_data="<svg width='360' height='640' viewBox='0 0 360 640' xmlns='http://www.w3.org/2000/svg'><rect width='100%' height='100%' fill='#1e1b4b'/><circle cx='180' cy='200' r='140' fill='#312e81' opacity='0.5'/></svg>"
            ),
            AssetSpec(
                asset_id="hero_king",
                name="King Character Sprite",
                asset_type="character",
                svg_data="<svg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'><circle cx='50' cy='50' r='40' fill='#f59e0b'/><polygon points='35,25 50,10 65,25' fill='#ef4444'/></svg>"
            ),
            AssetSpec(
                asset_id="gem_red",
                name="Royal Ruby Gem",
                asset_type="object",
                svg_data="<svg width='50' height='50' viewBox='0 0 50 50' xmlns='http://www.w3.org/2000/svg'><polygon points='25,5 45,20 35,45 15,45 5,20' fill='#ef4444'/></svg>"
            ),
            AssetSpec(
                asset_id="hand_tutorial",
                name="Animated Tutorial Pointer",
                asset_type="hand_tutorial",
                svg_data="<svg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'><text x='5' y='30' font-size='30'>👆</text></svg>"
            ),
            AssetSpec(
                asset_id="cta_button",
                name="Conversion Call-To-Action Button",
                asset_type="cta_banner",
                svg_data="<svg width='240' height='60' viewBox='0 0 240 60' xmlns='http://www.w3.org/2000/svg'><rect width='240' height='60' rx='12' fill='#2563eb'/><text x='120' y='35' font-size='16' font-weight='bold' fill='#ffffff' text-anchor='middle'>PLAY NOW</text></svg>"
            )
        ]
        return assets
