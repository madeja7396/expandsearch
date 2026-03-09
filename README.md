# expand-search

Lightweight Codex skill for shallow, auditable search runs.

This project keeps the search loop intentionally small:

`search_nodes.csv` -> `child_query_cache.csv` -> `artifact_rows.csv` -> `report.md`

## What It Is

`expand-search` is a CSV-first search pipeline for cases where 3 to 5 root queries are enough. It expands a user theme into a small node set, caches raw retrieval rows, filters them into compact artifact rows, and writes a short Markdown report.

## Repository Layout

- `SKILL.md`: main skill instructions
- `references/`: operational references for schemas, routing, expansion, and filtering
- `scripts/init_run.py`: scaffold a new run directory
- `scripts/run_demo.py`: local demo generator
- `demo/simple-demo/`: example output
- `runs/2026-03-10-self-mirror/`: canonical real run for the theme `自己と鏡像`
- `tasks/`: project planning, review, and lessons captured during development

## Quick Start

Initialize a run:

```bash
python3 scripts/init_run.py runs/my-run
```

Then populate:

1. `search_nodes.csv`
2. `child_query_cache.csv`
3. `artifact_rows.csv`
4. `report.md`

## Design Rules

- Keep the loop shallow.
- Prefer 3 to 5 meaningfully different root queries.
- Treat `child_query_cache.csv` as append-first raw evidence.
- Build `report.md` from `artifact_rows.csv`, not from memory.
- Escalate to a deeper research workflow if the shallow loop stops being enough.
