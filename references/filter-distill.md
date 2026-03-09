# Filter And Distill

Use this reference after the raw cache exists.

## Filter layer

The filter layer decides which cached rows are worth carrying forward.

Score or judge each row on:

- relevance to the objective
- usefulness relative to rows already kept
- source quality

Typical drop reasons:

- duplicate of a stronger row
- off-topic
- low-information summary
- stale or weak source

Write both keep and drop decisions into `artifact_rows.csv`.

## Distill layer

The distill layer converts kept rows into compact findings.

Use one row per kept source or distilled artifact in `artifact_rows.csv`.

## Distillation rules

- Prefer one atomic takeaway per row.
- Group duplicate evidence under one distilled row instead of repeating the same claim.
- Keep the wording concise enough to feed directly into `report.md`.
- Preserve the upstream row IDs and URLs.
- Mark uncertain items as provisional rather than smoothing them into certainty.

## Markdown synthesis

Build `report.md` from the distilled rows in `artifact_rows.csv`, not from raw cache rows.

Recommended flow:

1. kept findings
2. provisional items
3. deferred paths
4. recommended next step
