import json
import os
import sqlite3
from pathlib import Path
from datetime import datetime, timezone


def connection():
    path = Path(os.environ.get('PLAYFORGE_DB', str(Path(__file__).parents[1] / 'data' / 'projects.sqlite3')))
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute('CREATE TABLE IF NOT EXISTS projects (id TEXT PRIMARY KEY, payload TEXT NOT NULL)')
    db.execute('CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, project_id TEXT NOT NULL, decision TEXT NOT NULL, feedback TEXT NOT NULL, created_at TEXT NOT NULL)')
    return db


def save_project(result):
    with connection() as db:
        db.execute('INSERT INTO projects VALUES (?, ?)', (result.project_id, result.model_dump_json()))


def get_project(project_id):
    with connection() as db:
        row = db.execute('SELECT payload FROM projects WHERE id=?', (project_id,)).fetchone()
        if row is None:
            return None
        payload = json.loads(row['payload'])
        history = db.execute('SELECT decision, feedback, created_at FROM reviews WHERE project_id=? ORDER BY id', (project_id,)).fetchall()
        payload['reviews'] = [dict(item) for item in history]
        payload['review_status'] = history[-1]['decision'] if history else 'pending'
        return payload


def save_review(project_id, decision, feedback):
    with connection() as db:
        if db.execute('SELECT 1 FROM projects WHERE id=?', (project_id,)).fetchone() is None:
            raise KeyError(project_id)
        db.execute('INSERT INTO reviews (project_id, decision, feedback, created_at) VALUES (?, ?, ?, ?)',
                   (project_id, decision, feedback, datetime.now(timezone.utc).isoformat()))
    return get_project(project_id)
