# CSV Schemas

Use stable column names so the search loop can be resumed or post-processed later.

## `search_nodes.csv`

Recommended columns:

- `node_id`
- `question`
- `branch_family`
- `status`
- `priority`

## `child_query_cache.csv`

Recommended columns:

- `cache_row_id`
- `node_id`
- `query_text`
- `provider`
- `rank`
- `url`
- `title`
- `snippet`
- `retrieved_at`

## `artifact_rows.csv`

Recommended columns:

- `artifact_id`
- `node_id`
- `cache_row_id`
- `source_url`
- `canonical_url`
- `title`
- `filter_status`
- `filter_reason`
- `distilled_summary`
- `confidence`
- `report_section`

## Update rules

- Raw cache CSVs should be append-first.
- Derived CSVs may be regenerated, but keep stable IDs when possible.
- Do not rename columns mid-run unless you also migrate the existing files.
- Preserve row IDs so `report.md` can trace back to the pipeline outputs.
