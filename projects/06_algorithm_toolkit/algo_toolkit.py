"""Project 06 - Algorithm toolkit: classic algorithms and data structures, implemented by hand.

Fill in every function / method marked ``raise NotImplementedError`` and run::

    python -m pytest projects/06_algorithm_toolkit -q
"""
from __future__ import annotations
import heapq
import time
from collections import OrderedDict, deque
from typing import Callable, Hashable, Sequence

def binary_search(items: Sequence[int], target: int) -> int:
    """Index of ``target`` in the sorted sequence ``items`` or ``-1`` if absent. O(log n); do not use ``bisect`` or ``index``.
    If the value occurs several times, return the index of the first occurrence."""
    raise NotImplementedError

def merge_sort(items: Sequence[int]) -> list[int]:
    """Return a new sorted list (stable merge sort, O(n log n)). Do not use ``sorted`` / ``list.sort``; do not mutate the input."""
    raise NotImplementedError

def lis_length(items: Sequence[int]) -> int:
    """Length of the longest *strictly* increasing subsequence. O(n log n) (hint: patience sorting + ``bisect``)."""
    raise NotImplementedError

def edit_distance(a: str, b: str) -> int:
    """Levenshtein distance (insert / delete / substitute, each cost 1) with dynamic programming, O(len(a) * len(b))."""
    raise NotImplementedError

def knapsack_01(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Maximum total value of a subset of items whose total weight is <= ``capacity`` (each item used at most once)."""
    raise NotImplementedError

def dijkstra(graph: dict[Hashable, dict[Hashable, float]], source: Hashable) -> dict[Hashable, float]:
    """Shortest distances from ``source`` in a weighted graph given as ``{node: {neighbour: weight}}`` (weights >= 0).
    Unreachable nodes are absent from the result. Use ``heapq``."""
    raise NotImplementedError

def topological_sort(graph: dict[Hashable, Sequence[Hashable]]) -> list[Hashable]:
    """Topological order of a DAG given as ``{node: [successors]}`` (nodes that only appear as successors count too).
    Raise ``ValueError("cycle")`` if the graph has a cycle. When several orders are valid, pick nodes in the order of
    first appearance (Kahn's algorithm with a FIFO queue)."""
    raise NotImplementedError

class LRUCache:
    """Least-recently-used cache with ``capacity`` entries; ``get`` and ``put`` are O(1).

    * ``get(key)`` returns the value (and marks the key as most recently used) or ``None`` if missing.
    * ``put(key, value)`` inserts / updates; when the cache is full the least recently used key is evicted.
    * ``len(cache)`` is the number of stored keys and ``key in cache`` must NOT change the usage order.
    """

    def __init__(self, capacity: int) -> None:
        """Store the capacity (raise ``ValueError`` if it is not positive) and create the empty storage."""
        raise NotImplementedError

    def get(self, key: Hashable):
        """Value for ``key`` or ``None``; a hit makes the key the most recently used."""
        raise NotImplementedError

    def put(self, key: Hashable, value: object) -> None:
        """Insert or update ``key`` (most recently used); evict the least recently used key if over capacity."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Number of stored keys."""
        raise NotImplementedError

    def __contains__(self, key: Hashable) -> bool:
        """Membership test that does not change the usage order."""
        raise NotImplementedError

def time_function(func: Callable[[int], object], n: int, repeat: int=3) -> float:
    """PROVIDED. Best wall-clock time (seconds, ``time.perf_counter``) of ``repeat`` calls of ``func(n)``."""
    best = float('inf')
    for _ in range(repeat):
        start = time.perf_counter()
        func(n)
        best = min(best, time.perf_counter() - start)
    return best

def estimate_exponent(func: Callable[[int], object], sizes: Sequence[int]=(2000, 4000, 8000, 16000)) -> float:
    """Empirical complexity: time ``func(n)`` for every size in ``sizes`` and return the slope of the straight line fitted
    to ``log(time)`` vs ``log(n)`` (``numpy.polyfit``). ~1 means linear, ~2 quadratic."""
    raise NotImplementedError
