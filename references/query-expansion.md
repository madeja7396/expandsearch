# Query Expansion

Expand the user's query into a small root set. Do not jump straight from one query to a big search tree.

## Root query expansion

Write the original query and 3 to 5 orthogonal variants into `search_nodes.csv`.

Useful root families:

1. scope clarification
2. comparison
3. implementation
4. evaluation
5. primary-source

Not every run needs all five. Use only the families that could change the search outcome.

## Query writing rules

- Keep the domain keywords stable while changing the intent.
- Prefer simple, root-level variants before anything recursive.
- Translate into English when the best evidence is likely to be English.
- Reuse terminology found in strong sources.
- Stop at the root layer unless the simple loop clearly fails.

## CSV discipline

- `search_nodes.csv` stores the small root query set.
- `child_query_cache.csv` stores raw retrieval results for those root queries.

Do not hide the query text. Keep it visible in every cache row.
