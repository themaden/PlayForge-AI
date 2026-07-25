# PlayForge AI 🚀
### AI-Powered Playable Game Ad Generation Platform

**PlayForge AI** is an enterprise-grade platform that automates the creation of high-converting interactive HTML5 playable game advertisements (such as those created by Dream Games, Voodoo, and Playtika) using a multi-agent AI framework and the Phaser 3.80 HTML5 game engine.

---

## 🌟 Why PlayForge AI?

Traditional playable ad development involves a **2-4 week pipeline** across game designers, developers, artists, animators, and marketing managers.

With **PlayForge AI**:
1. Enter a natural language prompt (e.g., *"Royal Match style puzzle save-the-king 30s playable ad for Meta"*).
2. 5 Specialized AI Agents collaborate to generate game concept, synthesize Phaser 3 scene code, generate SVG assets, run automated bot QA, and inject high-CTR conversion hooks.
3. Download a single-file standalone HTML5 playable ad ready for instant upload to Meta Ads, TikTok Pangle, Google App Campaigns, or Unity Ads in seconds.

---

## 🤖 5-Agent Architecture

```
                                USER PROMPT
                                     │
                                     ▼
                   +----------------------------------+
                   |       Next.js 14 Studio UI       |
                   +-----------------+----------------+
                                     │
                                     ▼
                   +----------------------------------+
                   |      FastAPI Orchestrator        |
                   +-----------------+----------------+
                                     │
     ┌──────────────────┬────────────┼────────────┬──────────────────┐
     ▼                  ▼            ▼            ▼                  ▼
🎮 Agent 1          👨‍💻 Agent 2   🎨 Agent 3   🧪 Agent 4         📈 Agent 5
Game Design         Code Gen     Asset Gen    Gameplay QA        CTR Optimizer
(Rules, mechanics,  (Phaser 3    (Sprites,    (Time-to-1st-tap,  (Hook tuning,
 duration)          scenes)      effects)     FPS, bot test)     store redirect)
     │                  │            │            │                  │
     └──────────────────┴────────────┼────────────┴──────────────────┘
                                     │
                                     ▼
                   +----------------------------------+
                   |   Single-File HTML5 Packager     |
                   |   (Meta, TikTok, Google, Unity)  |
                   +----------------------------------+
```

---

## 🛠️ Stack & Technologies

- **Frontend**: Next.js 14, React 18, TypeScript, Tailwind CSS, Lucide Icons, Framer Motion.
- **Backend**: Python 3.11, FastAPI, Pydantic v2, Uvicorn.
- **Game Engine**: Phaser.js 3.80.
- **Ad Networks**: Meta Ads (FbPlayable), TikTok Pangle, Google App Campaigns, Unity Ads (MRAID 3.0).

---

## 🚀 Quick Start Guide

### 1. Run Backend Server
```bash
cd backend
pip install -r requirements.txt
python main.py
```
*API will run on `http://localhost:8000` (Swagger UI at `/docs`)*

### 2. Run Frontend Studio
```bash
npm install
npm run dev
```
*Open `http://localhost:3000` in your browser.*

---

## 🧪 Running Tests

```bash
pytest backend/tests
```

---

## 📜 Git Commit History
This project includes **30+ structured atomic commits** detailing backend initialization, agent creation, engine templates, UI components, ad network exporter, and automated test suites.
