# State Files

Use these files to keep the simple search loop outside the prompt.

Recommended run layout:

```text
run-name/
  search_nodes.csv
  child_query_cache.csv
  artifact_rows.csv
  report.md
```

## `search_nodes.csv`

Treat this file as the small root-node ledger.

Use it for:

- 3 to 5 root query variants
- short branch labels
- status
- priority

Keep one row per root query.

## `child_query_cache.csv`

Treat this file as the raw retrieval cache.

Use it for:

- the node that produced the query
- the query text
- the tool or route used
- returned titles, URLs, snippets, and ranks
- retrieval timestamp

Append new raw rows rather than rewriting them for presentation.

## `artifact_rows.csv`

Treat this file as the filter and distill ledger.

Use it for:

- which source URL survived filtering
- the canonical URL or deduped source
- keep or drop status
- why it was kept or dropped
- the short distilled summary
- confidence
- the target report section

This file should stay traceable to upstream cache row IDs and node IDs.

## `report.md`

Treat this file as the final Markdown synthesis for the user.

Recommended sections:

```md
# Report Title

## Objective

## Distilled Findings

## Provisional Items

## Deferred Paths

## Recommended Next Step
```

Build this file from `artifact_rows.csv`, not from memory.
