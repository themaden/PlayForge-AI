"""Runtime regression checks against the actual packaged HTML."""
import os
import tempfile
import time
import uuid
from pathlib import Path


def evaluate_html(html: str, duration: int) -> dict:
    from playwright.sync_api import sync_playwright
    started = time.perf_counter()
    errors = []
    checks = {}
    root = Path(__file__).resolve().parents[1] / 'data' / 'evaluation'
    root.mkdir(parents=True, exist_ok=True)
    run_id = uuid.uuid4().hex[:12]
    with tempfile.TemporaryDirectory(dir=root) as temp:
        path = Path(temp) / 'playable.html'
        path.write_text(html, encoding='utf-8')
        with sync_playwright() as p:
            browser = p.chromium.launch(channel=os.environ.get('PLAYFORGE_BROWSER_CHANNEL', 'msedge'), headless=True)
            context = browser.new_context(offline=True, viewport={'width': 360, 'height': 640})
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(path.as_uri())
            page.wait_for_function('typeof game !== "undefined" && game.scene.scenes[0].tiles?.length > 0')
            checks['canvas_loaded'] = page.locator('canvas').count() == 1
            page.screenshot(path=str(root / (run_id + '-preview.png')))
            if 'this.load.image("generated_bg"' in html:
                checks['generated_background_loaded'] = page.evaluate('game.scene.scenes[0].textures.exists("generated_bg")')
            tile = page.locator('canvas')
            tile.click(position={'x': 90, 'y': 160})
            page.wait_for_timeout(250)
            checks['tap_scores'] = page.evaluate('game.scene.scenes[0].score === 100')
            tile.click(position={'x': 90, 'y': 160})
            page.wait_for_timeout(250)
            checks['repeated_tap_ignored'] = page.evaluate('game.scene.scenes[0].score === 100')
            for x in [150, 210]:
                tile.click(position={'x': x, 'y': 160})
                page.wait_for_timeout(250)
            checks['win'] = page.evaluate('game.scene.scenes[0].gameEnded && game.scene.scenes[0].score === 300')
            dialogs = []
            def capture(dialog):
                dialogs.append(dialog.message)
                dialog.dismiss()
            page.on('dialog', capture)
            tile.click(position={'x': 180, 'y': 360})
            checks['demo_cta'] = bool(dialogs)
            page.screenshot(path=str(root / (run_id + '-win.png')))
            # Check actual timer expiry on a fresh scene, not a manually toggled flag.
            page.reload()
            page.wait_for_function('typeof game !== "undefined" && game.scene.scenes[0].tiles?.length > 0')
            page.wait_for_function('game.scene.scenes[0].gameEnded', timeout=(duration + 5) * 1000)
            checks['timeout'] = page.evaluate('game.scene.scenes[0].score === 0 && game.scene.scenes[0].timeLeft <= 0')
            checks['no_runtime_errors'] = not errors
            checks['offline_execution'] = checks['canvas_loaded']
            page.screenshot(path=str(root / (run_id + '-timeout.png')))
            browser.close()
    return {'method': 'playwright_chromium', 'checks': checks, 'passed': all(checks.values()),
            'errors': errors, 'screenshots': [f'backend/data/evaluation/{run_id}-preview.png', f'backend/data/evaluation/{run_id}-win.png', f'backend/data/evaluation/{run_id}-timeout.png'],
            'duration_ms': round((time.perf_counter() - started) * 1000, 2)}
