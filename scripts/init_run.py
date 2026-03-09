#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path


CSV_SPECS = {
    "search_nodes.csv": [
        "node_id",
        "question",
        "branch_family",
        "status",
        "priority",
    ],
    "child_query_cache.csv": [
        "cache_row_id",
        "node_id",
        "query_text",
        "provider",
        "rank",
        "url",
        "title",
        "snippet",
        "retrieved_at",
    ],
    "artifact_rows.csv": [
        "artifact_id",
        "node_id",
        "cache_row_id",
        "source_url",
        "canonical_url",
        "title",
        "filter_status",
        "filter_reason",
        "distilled_summary",
        "confidence",
        "report_section",
    ],
}


TEXT_TEMPLATES = {
    "report.md": """# Report

## Objective

## Distilled Findings

## Provisional Items

## Deferred Paths

## Recommended Next Step
""",
}


def write_csv(path: Path, headers: list[str], force: bool) -> str:
    if path.exists() and not force:
        return "kept"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
    return "created"


def write_text(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return "kept"
    path.write_text(content, encoding="utf-8")
    return "created"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize a simple expand-search run directory."
    )
    parser.add_argument("run_dir", help="Target directory for the run artifacts")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files instead of preserving them",
    )
    args = parser.parse_args()

    run_dir = Path(args.run_dir).expanduser().resolve()
    run_dir.mkdir(parents=True, exist_ok=True)

    created = []
    kept = []

    for name, headers in CSV_SPECS.items():
        result = write_csv(run_dir / name, headers, args.force)
        (created if result == "created" else kept).append(name)

    for name, content in TEXT_TEMPLATES.items():
        result = write_text(run_dir / name, content, args.force)
        (created if result == "created" else kept).append(name)

    print(f"Initialized run directory: {run_dir}")
    print(f"Created: {', '.join(created) if created else 'none'}")
    print(f"Kept: {', '.join(kept) if kept else 'none'}")


if __name__ == "__main__":
    main()
