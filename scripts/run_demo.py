#!/usr/bin/env python3

import csv
from pathlib import Path
import shutil

from init_run import CSV_SPECS, TEXT_TEMPLATES, write_csv, write_text


def append_row(path: Path, row: list[str]) -> None:
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(row)


def main() -> None:
    demo_dir = Path("demo/simple-demo").resolve()
    if demo_dir.exists():
        shutil.rmtree(demo_dir)
    demo_dir.mkdir(parents=True, exist_ok=True)

    for name, headers in CSV_SPECS.items():
        write_csv(demo_dir / name, headers, True)

    for name, content in TEXT_TEMPLATES.items():
        write_text(demo_dir / name, content, True)

    append_row(
        demo_dir / "search_nodes.csv",
        ["N00", "Best ramen in Tokyo for late-night travelers", "scope", "active", "high"],
    )
    append_row(
        demo_dir / "search_nodes.csv",
        ["N01", "Shinjuku late-night ramen options", "comparison", "cached", "medium"],
    )
    append_row(
        demo_dir / "search_nodes.csv",
        ["N02", "Late-night ramen near Tokyo Station", "comparison", "open", "medium"],
    )

    append_row(
        demo_dir / "child_query_cache.csv",
        [
            "CQ01",
            "N01",
            "Shinjuku late night ramen best",
            "exa",
            "1",
            "https://example.com/shinjuku-ramen",
            "Late Night Ramen in Shinjuku",
            "Guide to several shops open after midnight.",
            "2026-03-10T00:00:00Z",
        ],
    )
    append_row(
        demo_dir / "child_query_cache.csv",
        [
            "CQ02",
            "N00",
            "Tokyo late night ramen travelers",
            "exa",
            "2",
            "https://example.com/tokyo-ramen",
            "Tokyo Ramen for Night Owls",
            "Overview of several neighborhoods with late-night shops.",
            "2026-03-10T00:05:00Z",
        ],
    )

    append_row(
        demo_dir / "artifact_rows.csv",
        [
            "A01",
            "N01",
            "CQ01",
            "https://example.com/shinjuku-ramen",
            "https://example.com/shinjuku-ramen",
            "Late Night Ramen in Shinjuku",
            "keep",
            "Relevant late-night comparison source",
            "Shinjuku is a promising late-night ramen branch for travelers.",
            "provisional",
            "Distilled Findings",
        ],
    )
    append_row(
        demo_dir / "artifact_rows.csv",
        [
            "A02",
            "N00",
            "CQ02",
            "https://example.com/tokyo-ramen",
            "https://example.com/tokyo-ramen",
            "Tokyo Ramen for Night Owls",
            "keep",
            "Useful city-level overview",
            "Tokyo-wide overview supports Shinjuku as one good late-night area.",
            "provisional",
            "Distilled Findings",
        ],
    )
    append_row(
        demo_dir / "artifact_rows.csv",
        [
            "A03",
            "N02",
            "",
            "",
            "",
            "Tokyo Station branch",
            "defer",
            "Not explored in the simple demo",
            "",
            "open",
            "Deferred Paths",
        ],
    )

    write_text(
        demo_dir / "report.md",
        """# Report

## Objective

Find one simple answer path for a late-night ramen query.

## Distilled Findings

- Shinjuku is a promising late-night ramen branch for travelers.
- A Tokyo-wide overview supports Shinjuku as one good late-night area.

## Provisional Items

- The demo uses placeholder sources and is not verified.

## Deferred Paths

- Tokyo Station was left open in the demo.

## Recommended Next Step

- Add one independent confirming source before treating the result as verified.
""",
        True,
    )

    print(f"Demo written to: {demo_dir}")
    print("Files:")
    for path in sorted(demo_dir.iterdir()):
        print(f"- {path.name}")


if __name__ == "__main__":
    main()
