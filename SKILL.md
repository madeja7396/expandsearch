---
name: expand-search
description: Simple search-pipeline skill for agents that expands a user query into a few root search nodes, stores raw retrieval rows in one CSV, filters and distills them into one artifact CSV, and writes a short Markdown report. Use when a task needs a lightweight, repeatable search loop with CSV and Markdown outputs instead of a deep research system.
---

# Expand Search

Use this skill when the task needs a lightweight search loop, not a large research operating system. Keep the pipeline shallow and stop once the answer path is good enough.

Simple Is Best:

- stay local by default
- keep one search depth by default
- keep CSV state minimal
- do not add extra ledgers unless the simple loop fails

## Scope

This skill is for:

- lightweight exploratory retrieval
- tasks where 3 to 5 root query variants are enough
- search runs where raw retrieval should be cached and reused
- filtering and distilling a small result set into auditable outputs

This skill is not for:

- single-pass factual lookups
- recursive search trees by default
- native multi-agent orchestration
- purely local code edits with no search component
- polished visual deliverables such as slides, HTML, or PDFs

## Execute the pipeline

1. Create or normalize `search_nodes.csv`, `child_query_cache.csv`, `artifact_rows.csv`, and `report.md`. Read `references/state-files.md`.
2. If you want a clean scaffold, run `python3 scripts/init_run.py <run-dir>`. Read `references/csv-schemas.md`.
3. Expand the user query into 3 to 5 root queries and store them in `search_nodes.csv`. Read `references/query-expansion.md`.
4. Retrieve against the best root queries and append raw rows to `child_query_cache.csv`. Read `references/mcp-routing.md`.
5. Filter the raw rows for relevance and usefulness. Write keep or drop decisions plus short summaries into `artifact_rows.csv`. Read `references/filter-distill.md`.
6. Build `report.md` from the kept rows in `artifact_rows.csv`, not from memory.
7. Stop when the small root set is exhausted or the report is already good enough.

## Discipline

- Keep root queries meaningfully different. Do not create multiple rows that differ only by wording.
- Prefer 3 to 5 root queries, not a large tree.
- Treat `child_query_cache.csv` as the raw cache. Do not overwrite raw retrieval fields just to make them prettier.
- Treat `artifact_rows.csv` as the filter and distill layer.
- If the shallow loop is not enough, switch to `$deep-research` instead of adding more layers here.

## File roles

- Treat `search_nodes.csv` as the node ledger for the small root set.
- Treat `child_query_cache.csv` as the append-first raw retrieval cache.
- Treat `artifact_rows.csv` as the kept-or-dropped decision layer plus compact synthesis ledger.
- Treat `report.md` as the final Markdown synthesis.

## Stop conditions

Stop the loop when one or more of these are true:

- the root query set is exhausted
- recent retrieval rows are only duplicates
- `artifact_rows.csv` is no longer gaining high-value kept rows
- the kept rows in `artifact_rows.csv` are already enough to answer the user's objective

## Final outputs

- The primary machine-readable outputs are `search_nodes.csv`, `child_query_cache.csv`, and `artifact_rows.csv`.
- The primary human-readable output is `report.md`.
- Keep `report.md` traceable to node IDs and row IDs from the CSV layers.

## Load references as needed

- Read `references/state-files.md` before creating or normalizing state files.
- Read `references/csv-schemas.md` before creating, renaming, or normalizing CSV columns.
- Read `references/query-expansion.md` when creating the small root query set.
- Read `references/filter-distill.md` when scoring, filtering, or distilling cached rows.
- Read `references/mcp-routing.md` when tool choice is part of the bottleneck.
