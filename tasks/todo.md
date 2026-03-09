# TODO

## 2026-03-10 Release

### Scope Decisions
- [ ] Publish this project as a standalone git repository rooted at `/mnt/d/dev/expandsearch`.
- [ ] Keep the public snapshot focused on the skill, references, demo, scripts, tasks, and the canonical `self-mirror` run.
- [ ] Exclude accidental local-only artifacts from the initial public commit.

### Implementation
- [ ] Add minimal publication files needed for a public repo.
- [ ] Initialize a standalone git repository for this project.
- [ ] Stage the intended files and create a release commit.
- [ ] Configure a public remote if the environment provides a valid target.

### Validation
- [ ] Confirm the repo can be committed cleanly from its own root without depending on the broken parent git tree.
- [ ] Confirm the committed tree includes the canonical run and excludes the auxiliary local-only run.
- [ ] Confirm whether push/publication succeeded or record the exact blocker.

### Review
- Pending.

## 2026-03-10 Run: 自己と鏡像

### Scope Decisions
- [x] Use a shallow `expand-search` run, not `$deep-research`.
- [x] Interpret the theme as a cross-disciplinary exploratory search across philosophy, psychoanalysis, psychology, and literature/art.
- [x] Produce one auditable run directory with `search_nodes.csv`, `child_query_cache.csv`, `artifact_rows.csv`, and `report.md`.

### Implementation
- [x] Initialize a new run directory for the theme.
- [x] Expand the theme into 3 to 5 orthogonal root queries in `search_nodes.csv`.
- [x] Retrieve and cache raw search results in `child_query_cache.csv`.
- [x] Filter and distill the cached rows into `artifact_rows.csv`.
- [x] Build `report.md` from the kept artifact rows.

### Validation
- [x] Confirm the run directory contains the 4 required files with the expected schemas.
- [x] Confirm `report.md` is traceable back to node IDs and cache/artifact rows.
- [x] Check that the final kept rows cover multiple distinct angles on the theme.

### Review
- Primary run directory: [runs/2026-03-10-self-mirror](/mnt/d/dev/expandsearch/runs/2026-03-10-self-mirror)
- Output quality: 5 root nodes, 10 raw cache rows, 10 artifact rows, and a Markdown synthesis spanning philosophy, psychoanalysis, developmental psychology, and literature/aesthetics.
- Validation notes: CSV headers match the skill schema, all artifact rows resolve to valid node IDs and cache row IDs, and `report.md` uses explicit `(node/cache/artifact)` references.

## Scope Decisions
- [x] Replace the previous multi-layer, demo-heavy design with a minimal shallow search loop.
- [x] Keep only the essential runtime artifacts: `search_nodes.csv`, `child_query_cache.csv`, `artifact_rows.csv`, and `report.md`.
- [x] Finish by installing the skill globally.

## Implementation
- [x] Rewrite `SKILL.md` and `agents/openai.yaml` around the simple 3-stage loop.
- [x] Reduce the references to the minimum set needed for the shallow loop.
- [x] Simplify `scripts/init_run.py` and `scripts/run_demo.py` to match the 4-file artifact set.
- [x] Remove grandchild recursion, native subagent orchestration, and extra ledgers from the runtime contract.

## Validation
- [x] Run structural validation against the simplified skill.
- [x] Execute the demo and confirm the 4-file artifact set is produced.
- [x] Validate the globally installed skill.

## Review
- Final runtime contract: `search_nodes.csv` -> `child_query_cache.csv` -> `artifact_rows.csv` -> `report.md`.
- Demo executed with `python3 scripts/run_demo.py` and now lives at [demo/simple-demo](/mnt/d/dev/expandsearch/demo/simple-demo).
- Global skill installed at [/root/.codex/skills/expand-search](/root/.codex/skills/expand-search) with only the essential skill files.
- Validation: `python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py /mnt/d/dev/expandsearch` returned `Skill is valid!`
- Validation: `python3 /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py /root/.codex/skills/expand-search` returned `Skill is valid!`
- Remaining gaps: the demo is static and placeholder-backed, and the simple skill intentionally escalates to `$deep-research` instead of growing new layers.
