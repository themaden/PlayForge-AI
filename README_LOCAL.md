# PlayForge Studio

Local portfolio prototype for producing and reviewing a template-based HTML5 tap puzzle. It does not call an LLM or image model and requires no paid API account.

## Implemented

- Python FastAPI pipeline with separate design, code, asset and static validation stages.
- One playable tap puzzle: three different tile taps win; the timer triggers a failure screen.
- Embedded Phaser engine so exported HTML opens without internet access.
- Static code checks, with unknown FPS, engagement and CTR represented as unmeasured.
- SQLite project storage and a persistent human review history.
- Approve or request changes, restore saved projects by ID, and download approved output in the UI.
- Actual pipeline duration measured with a monotonic timer. This excludes database writing, HTTP and browser rendering.

## Limits

This is a tap puzzle rather than a complete match-3 game. Brief interpretation uses fixed rules and templates. Pull-the-pin and tile blast requests return an explicit error. SVG assets are fixed examples rather than generated artwork. Human feedback is saved for manual revision; automatic regeneration is not implemented. Review approval gates the UI download button, not access to an authenticated export API. The CTA shows a demo message. Ad network certification, diffusion/video generation, runtime evaluation per generation and model-based orchestration remain future work.

## Run locally on Windows

Install Python 3.11 or newer and Node.js, then extract the source package. In the project folder:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r backend/requirements.txt httpx
npm ci
```

In one terminal:

```powershell
.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

In a second terminal:

```powershell
npm run dev -- --hostname 127.0.0.1
```

Open http://127.0.0.1:3000. Both services are for local use. No cloud deployment or public authentication is included.

## Demo sequence

1. Generate a royal rescue puzzle with a 15-second duration.
2. Tap one tile twice: the second tap must not increase the score.
3. Tap two other tiles to see the win screen.
4. Generate again and let the timer expire to see the failure screen.
5. Write feedback and select Request changes. Approve only after review.
6. Download the HTML and open it with internet access disabled.
7. Copy the saved project ID and restore it to verify the review history.

## Verification

```powershell
.venv\Scripts\python.exe -m pytest backend/tests -q
npm run build
```

Eight backend tests passed, and the frontend production build passed. Browser checks verified canvas loading, distinct tile scoring, win and timeout behavior, saved review history, approved downloads and offline execution. These are development checks, not ad performance measurements.

## Next development steps

1. Improve the playable mechanic and make brief fields affect visible output.
2. Add a local model through Ollama only after checking machine resources.
3. Validate structured model output and record which provider generated each artifact.
4. Add actual image generation and integrate returned images into the game.
5. Run browser evaluation automatically for each output and connect human feedback to revision.

This version was developed with Codex assistance. Be prepared to explain the code and reproduce the demo before describing the new features as your own hands-on experience in an interview.

Phaser is redistributed under its MIT license in backend/vendor/PHASER_LICENSE.md.
