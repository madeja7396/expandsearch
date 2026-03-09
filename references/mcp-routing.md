# MCP Routing

Use this reference when the bottleneck is not "what do I think?" but "which tool should gather the next evidence for the simple loop?"

## Root discovery

Use search-oriented tools when you need:

- first-pass coverage
- alternative phrasings
- recent changes

Current local default:

- Prefer `exa` first for the small root query set.

## Page confirmation

Use browser-oriented tools when you need:

- JS-heavy docs or product sites
- deterministic access to a specific result page

Current local default:

- Prefer `playwright` only when a kept result needs page-level confirmation.

## Escalation rule

If the shallow loop is no longer enough, switch to `$deep-research` instead of adding more recursive layers here.
