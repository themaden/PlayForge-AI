from typing import List
from pathlib import Path
from html import escape
from backend.app.schemas import GameConcept, AssetSpec

class AdPackagerEngine:
    """Single-File HTML5 Standalone Ad Packager
    Bundles Phaser 3.80, JS game logic, SVG assets, and network SDK hooks (Meta, TikTok, MRAID).
    """

    def package_ad(self, concept: GameConcept, code: str, assets: List[AssetSpec], target_network: str) -> str:
        svg_declarations = "\n".join([
            f"const {a.asset_id}_svg = `{a.svg_data}`;"
            for a in assets
        ])

        engine = (Path(__file__).resolve().parents[2] / "vendor" / "phaser.min.js").read_text(encoding="utf-8")
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>{escape(concept.title)} - Playable Ad</title>
    <!-- Embedded Phaser 3.80 Engine CDN -->
    <script>{engine}</script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; touch-action: none; }}
        body, html {{ width: 100%; height: 100%; overflow: hidden; background: #0f172a; display: flex; justify-content: center; align-items: center; font-family: sans-serif; }}
        #phaser-game-container {{ width: 100%; height: 100%; max-width: 480px; max-height: 854px; position: relative; }}
    </style>
    <script>
        // Target Ad Network SDK Stub: {target_network}
        window.AdNetwork = "{target_network}";
        if (window.mraid) {{
            window.mraid.addEventListener('ready', function() {{ console.log('MRAID Ready'); }});
        }}
    </script>
</head>
<body>
    <div id="phaser-game-container"></div>
    <script>
        {svg_declarations}

        {code}

        const config = {{
            type: Phaser.AUTO,
            parent: 'phaser-game-container',
            width: 360,
            height: 640,
            scale: {{
                mode: Phaser.Scale.FIT,
                autoCenter: Phaser.Scale.CENTER_BOTH
            }},
            scene: [PlayableScene]
        }};

        const game = new Phaser.Game(config);
    </script>
</body>
</html>
"""
        return html
