import random
from itertools import combinations

import pytest

from algo_toolkit import (
    LRUCache,
    binary_search,
    dijkstra,
    edit_distance,
    estimate_exponent,
    knapsack_01,
    lis_length,
    merge_sort,
    time_function,
    topological_sort,
)


def test_time_function_is_provided():                   # must pass from the start
    assert time_function(lambda n: sum(range(n)), 1000) > 0


# ---------------------------------------------------------------- searching and sorting
def test_binary_search_examples():
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([], 1) == -1
    assert binary_search([2], 2) == 0
    assert binary_search([1, 2, 2, 2, 3], 2) == 1       # first occurrence


def test_binary_search_random():
    rnd = random.Random(1)
    for _ in range(300):
        items = sorted(rnd.randint(0, 30) for _ in range(rnd.randint(0, 20)))
        t = rnd.randint(-2, 32)
        expected = items.index(t) if t in items else -1
        assert binary_search(items, t) == expected


def test_binary_search_does_not_scan():
    class Counting(list):
        reads = 0

        def __getitem__(self, i):
            Counting.reads += 1
            return super().__getitem__(i)

    data = Counting(range(100_000))
    assert binary_search(data, 77_777) == 77_777
    assert Counting.reads < 100


def test_merge_sort():
    assert merge_sort([]) == []
    assert merge_sort([5]) == [5]
    assert merge_sort([3, 1, 2, 3, -1]) == [-1, 1, 2, 3, 3]
    rnd = random.Random(2)
    for _ in range(100):
        xs = [rnd.randint(-50, 50) for _ in range(rnd.randint(0, 60))]
        before = list(xs)
        assert merge_sort(xs) == sorted(xs)
        assert xs == before                              # input untouched


def test_merge_sort_tuple_input_and_speed():
    assert merge_sort((3, 2, 1)) == [1, 2, 3]
    xs = [random.Random(3).randint(0, 10 ** 6) for _ in range(100_000)]
    assert merge_sort(xs) == sorted(xs)


# ---------------------------------------------------------------- dynamic programming
def test_lis_length():
    assert lis_length([]) == 0
    assert lis_length([7]) == 1
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([2, 2, 2]) == 1                     # strictly increasing
    assert lis_length(list(range(100_000))) == 100_000


def test_lis_length_against_brute_force():
    rnd = random.Random(4)
    for _ in range(100):
        xs = [rnd.randint(0, 8) for _ in range(rnd.randint(0, 10))]
        best = 0
        for r in range(len(xs) + 1):
            for sub in combinations(xs, r):
                if all(a < b for a, b in zip(sub, sub[1:])):
                    best = max(best, r)
        assert lis_length(xs) == best


def test_edit_distance():
    assert edit_distance("", "") == 0
    assert edit_distance("abc", "") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("flaw", "lawn") == 2
    assert edit_distance("same", "same") == 0
    assert edit_distance("intention", "execution") == 5


def test_edit_distance_properties():
    rnd = random.Random(5)
    words = ["".join(rnd.choice("abc") for _ in range(rnd.randint(0, 7))) for _ in range(40)]
    for a in words:
        for b in words[:10]:
            assert edit_distance(a, b) == edit_distance(b, a)
            assert abs(len(a) - len(b)) <= edit_distance(a, b) <= max(len(a), len(b))


def test_knapsack():
    assert knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert knapsack_01([], [], 10) == 0
    assert knapsack_01([5], [10], 4) == 0
    assert knapsack_01([5], [10], 5) == 10
    assert knapsack_01([2, 2, 2], [3, 3, 3], 5) == 6      # each item only once


def test_knapsack_against_brute_force():
    rnd = random.Random(6)
    for _ in range(100):
        n = rnd.randint(0, 8)
        w = [rnd.randint(1, 6) for _ in range(n)]
        v = [rnd.randint(1, 9) for _ in range(n)]
        cap = rnd.randint(0, 15)
        best = max(
            sum(v[i] for i in sub)
            for r in range(n + 1)
            for sub in combinations(range(n), r)
            if sum(w[i] for i in sub) <= cap
        )
        assert knapsack_01(w, v, cap) == best


# ---------------------------------------------------------------- graphs
GRAPH = {
    "A": {"B": 7, "C": 9, "F": 14},
    "B": {"A": 7, "C": 10, "D": 15},
    "C": {"A": 9, "B": 10, "D": 11, "F": 2},
    "D": {"B": 15, "C": 11, "E": 6},
    "E": {"D": 6, "F": 9},
    "F": {"A": 14, "C": 2, "E": 9},
    "Z": {},
}


def test_dijkstra():
    assert dijkstra(GRAPH, "A") == {"A": 0, "B": 7, "C": 9, "D": 20, "E": 20, "F": 11}
    assert dijkstra(GRAPH, "Z") == {"Z": 0}
    assert dijkstra({}, "x") == {"x": 0}


def test_dijkstra_directed_and_unorderable_nodes():
    g = {1: {"a": 1.5}, "a": {(2, 2): 2}, (2, 2): {}}          # mixed types: nodes must never be compared
    assert dijkstra(g, 1) == {1: 0, "a": 1.5, (2, 2): 3.5}


def test_dijkstra_large_grid():
    n = 120
    g = {(i, j): {} for i in range(n) for j in range(n)}
    for i in range(n):
        for j in range(n):
            if i + 1 < n:
                g[(i, j)][(i + 1, j)] = 1
            if j + 1 < n:
                g[(i, j)][(i, j + 1)] = 1
    assert dijkstra(g, (0, 0))[(n - 1, n - 1)] == 2 * (n - 1)


def test_topological_sort():
    g = {"shirt": ["tie", "belt"], "tie": ["jacket"], "pants": ["shoes", "belt"], "belt": ["jacket"], "socks": ["shoes"]}
    order = topological_sort(g)
    assert sorted(order) == sorted({"shirt", "tie", "belt", "jacket", "pants", "shoes", "socks"})
    pos = {n: i for i, n in enumerate(order)}
    for u, succ in g.items():
        for v in succ:
            assert pos[u] < pos[v]


def test_topological_sort_is_deterministic():
    assert topological_sort({1: [2, 3], 2: [4], 3: [4]}) == [1, 2, 3, 4]
    assert topological_sort({}) == []
    assert topological_sort({"x": []}) == ["x"]


def test_topological_sort_cycle():
    with pytest.raises(ValueError, match="cycle"):
        topological_sort({1: [2], 2: [3], 3: [1]})
    with pytest.raises(ValueError, match="cycle"):
        topological_sort({1: [1]})


# ---------------------------------------------------------------- data structure
def test_lru_cache_basic():
    c = LRUCache(2)
    assert c.get("a") is None
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1                                 # 'b' is now the least recently used
    c.put("c", 3)
    assert c.get("b") is None
    assert c.get("a") == 1 and c.get("c") == 3
    assert len(c) == 2


def test_lru_cache_update_and_contains():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 10)                                         # update refreshes 'a'
    c.put("c", 3)                                          # evicts 'b'
    assert "b" not in c and "a" in c and "c" in c
    assert c.get("a") == 10
    c2 = LRUCache(2)
    c2.put(1, 1)
    c2.put(2, 2)
    assert 1 in c2                                         # `in` does not refresh
    c2.put(3, 3)
    assert 1 not in c2


def test_lru_cache_invalid_capacity_and_falsy_values():
    with pytest.raises(ValueError):
        LRUCache(0)
    c = LRUCache(1)
    c.put("zero", 0)
    assert c.get("zero") == 0


def test_lru_cache_is_fast():
    c = LRUCache(1000)
    for i in range(200_000):
        c.put(i, i)
        c.get(i - 500)
    assert len(c) == 1000


# ---------------------------------------------------------------- empirical complexity
def test_estimate_exponent_linear_vs_quadratic():
    linear = estimate_exponent(lambda n: sum(range(n * 20)), sizes=(20_000, 40_000, 80_000, 160_000))
    quadratic = estimate_exponent(lambda n: sum(i * j for i in range(n) for j in range(n)), sizes=(100, 200, 400, 800))
    assert 0.6 < linear < 1.5
    assert 1.5 < quadratic < 2.6
