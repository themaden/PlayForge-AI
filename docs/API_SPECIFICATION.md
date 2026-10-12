# REST API

The authoritative request and response schemas are available at `/docs` when the backend runs locally.

| Endpoint | Purpose |
| --- | --- |
| POST /api/generate | Create and persist a local template output; prompt length 3–2000, duration 5–60 seconds |
| GET /api/projects/{project_id} | Retrieve output and review history; unknown IDs return 404 |
| POST /api/projects/{project_id}/review | Save approved or changes_requested; changes require nonblank feedback |
| GET /api/health | Check service availability |
| GET /api/presets | Legacy template suggestions; pull-the-pin and tile blast are not implemented |

Example review body:

```json
{"decision": "changes_requested", "feedback": "Make the instructions clearer"}
```

`validation_method` is `static_code_checks`. Runtime and ad performance metrics are unmeasured. The local API does not implement authentication or ad-network certification.
