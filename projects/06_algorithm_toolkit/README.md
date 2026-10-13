# Project 06 - Algorithm toolkit

Classic algorithms and one data structure written by hand: searching, sorting, dynamic programming, graphs and an LRU cache. The last function measures the complexity empirically.

**Skills:** algorithmic thinking, recursion, `heapq`, `collections`, dunder methods, complexity analysis. This is the "Codility style" project: tests compare against brute force and also check the speed.
**Notebooks to review first:** 12-15 (Codility lessons), 04 (iterators), 05 (OOP).

## How to work

1. Open `algo_toolkit.py`; `time_function` is provided.
2. `python -m pytest projects/06_algorithm_toolkit -q` (skipped = not implemented yet).
3. Think about the complexity before coding: slow solutions fail the large tests.

## Milestones

1. `binary_search`, `merge_sort`.
2. Dynamic programming - `lis_length`, `edit_distance`, `knapsack_01`.
3. Graphs - `dijkstra`, `topological_sort`.
4. `LRUCache` - O(1) `get`/`put` (hint: `collections.OrderedDict`; stretch: write it with a dict + doubly linked list).
5. `estimate_exponent` - fit a line in log-log scale and read the exponent.

## Stretch goals

- Add `quick_sort` with a random pivot and compare it with `merge_sort` using `estimate_exponent`.
- Implement A* on a grid and compare the explored nodes with Dijkstra.
- Add type hints everywhere and run `mypy --strict` on the file.
- Add a `lru_cache`-based memoised version of `edit_distance` and compare.
