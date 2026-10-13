import itertools
import random

import pytest

from helpers import assert_fast
from practice_02_counting_prefix_sorting import (
    count_div,
    distinct,
    frog_river_one,
    genomic_range_query,
    max_counters,
    max_product_of_three,
    missing_integer,
    passing_cars,
    perm_check,
    triangle,
)

rng = random.Random(7)


# ----------------------------------------------------------------------------- perm_check
@pytest.mark.parametrize(
    "A, expected",
    [([4, 1, 3, 2], 1), ([4, 1, 3], 0), ([1], 1), ([2], 0), ([1, 1], 0), ([1, 2, 2], 0), ([1_000_000_000], 0), ([2, 3, 4, 5], 0)],
)
def test_perm_check_examples(A, expected):
    assert perm_check(A) == expected


def test_perm_check_random():
    for _ in range(300):
        n = rng.randint(1, 10)
        A = list(range(1, n + 1))
        rng.shuffle(A)
        assert perm_check(A) == 1
        B = list(A)
        B[rng.randrange(n)] = rng.randint(1, n + 1)
        assert perm_check(B) == (1 if sorted(B) == list(range(1, n + 1)) else 0)


def test_perm_check_big():
    A = list(range(1, 100_001))
    rng.shuffle(A)
    assert assert_fast(perm_check, A) == 1
    A[0] = 1_000_000_000
    assert assert_fast(perm_check, A) == 0


# ----------------------------------------------------------------------------- frog_river_one
def _river_oracle(X, A):
    for t in range(len(A)):
        if set(range(1, X + 1)) <= set(A[: t + 1]):
            return t
    return -1


def test_frog_river_one_examples():
    assert frog_river_one(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    assert frog_river_one(1, [1]) == 0
    assert frog_river_one(2, [2, 2, 2, 2, 2]) == -1
    assert frog_river_one(3, [1, 2]) == -1


def test_frog_river_one_random():
    for _ in range(300):
        X = rng.randint(1, 6)
        A = [rng.randint(1, X) for _ in range(rng.randint(1, 15))]
        assert frog_river_one(X, A) == _river_oracle(X, A), (X, A)


def test_frog_river_one_big():
    X = 100_000
    A = list(range(1, X + 1))
    rng.shuffle(A)
    # every value appears exactly once, so the river is only covered by the very last leaf
    assert assert_fast(frog_river_one, X, A) == X - 1
    assert assert_fast(frog_river_one, X, A[:-1]) == -1


# ----------------------------------------------------------------------------- missing_integer
def _missing_oracle(A):
    s = set(A)
    i = 1
    while i in s:
        i += 1
    return i


def test_missing_integer_examples():
    assert missing_integer([1, 3, 6, 4, 1, 2]) == 5
    assert missing_integer([1, 2, 3]) == 4
    assert missing_integer([-1, -3]) == 1
    assert missing_integer([2]) == 1
    assert missing_integer([1]) == 2
    assert missing_integer([0]) == 1
    assert missing_integer([1_000_000, -1_000_000]) == 1


def test_missing_integer_random():
    for _ in range(300):
        A = [rng.randint(-5, 12) for _ in range(rng.randint(1, 12))]
        assert missing_integer(A) == _missing_oracle(A), A


def test_missing_integer_big():
    A = list(range(1, 100_001))
    A.remove(77_777)
    rng.shuffle(A)
    assert assert_fast(missing_integer, A) == 77_777


# ----------------------------------------------------------------------------- max_counters
def _counters_oracle(N, A):
    c = [0] * N
    for k in A:
        if k == N + 1:
            c = [max(c)] * N
        else:
            c[k - 1] += 1
    return c


def test_max_counters_examples():
    assert max_counters(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    assert max_counters(1, [1]) == [1]
    assert max_counters(1, [2, 2]) == [0]
    assert max_counters(3, []) == [0, 0, 0]


def test_max_counters_random():
    for _ in range(300):
        N = rng.randint(1, 6)
        A = [rng.randint(1, N + 1) for _ in range(rng.randint(0, 15))]
        assert max_counters(N, A) == _counters_oracle(N, A), (N, A)


def test_max_counters_big():
    N = M = 100_000
    A = [N + 1 if i % 3 == 0 else rng.randint(1, N) for i in range(M)]
    result = assert_fast(max_counters, N, A, limit=3.0)
    # fast oracle
    base, cur, mx = 0, {}, 0
    for k in A:
        if k == N + 1:
            base, cur = mx, {}
        else:
            cur[k] = max(cur.get(k, base), base) + 1
            mx = max(mx, cur[k])
    expected = [max(cur.get(i, base), base) for i in range(1, N + 1)]
    assert result == expected


# ----------------------------------------------------------------------------- passing_cars
def _cars_oracle(A):
    return sum(1 for p, q in itertools.combinations(range(len(A)), 2) if A[p] == 0 and A[q] == 1)


def test_passing_cars_examples():
    assert passing_cars([0, 1, 0, 1, 1]) == 5
    assert passing_cars([1, 1, 1]) == 0
    assert passing_cars([0, 0, 0]) == 0
    assert passing_cars([0]) == 0
    assert passing_cars([1, 0]) == 0
    assert passing_cars([0, 1]) == 1


def test_passing_cars_random():
    for _ in range(300):
        A = [rng.randint(0, 1) for _ in range(rng.randint(1, 15))]
        assert passing_cars(A) == _cars_oracle(A), A


def test_passing_cars_overflow_and_speed():
    A = [0] * 50_000 + [1] * 50_000  # 2.5e9 pairs > 1e9
    assert assert_fast(passing_cars, A) == -1
    B = [0] * 30_000 + [1] * 30_000  # 9e8 pairs
    assert assert_fast(passing_cars, B) == 900_000_000


# ----------------------------------------------------------------------------- count_div
@pytest.mark.parametrize(
    "A, B, K, expected",
    [(6, 11, 2, 3), (0, 0, 11, 1), (1, 1, 11, 0), (10, 10, 5, 1), (10, 10, 3, 0), (0, 2_000_000_000, 1, 2_000_000_001), (11, 345, 17, 20), (0, 10, 3, 4)],
)
def test_count_div_examples(A, B, K, expected):
    assert count_div(A, B, K) == expected


def test_count_div_random():
    for _ in range(500):
        A = rng.randint(0, 50)
        B = rng.randint(A, 80)
        K = rng.randint(1, 15)
        assert count_div(A, B, K) == sum(1 for i in range(A, B + 1) if i % K == 0)


def test_count_div_is_constant_time():
    assert assert_fast(count_div, 0, 2_000_000_000, 7, limit=0.5) == 2_000_000_000 // 7 + 1


# ----------------------------------------------------------------------------- genomic_range_query
IMPACT = {"A": 1, "C": 2, "G": 3, "T": 4}


def _dna_oracle(S, P, Q):
    return [min(IMPACT[c] for c in S[p : q + 1]) for p, q in zip(P, Q)]


def test_genomic_range_query_examples():
    assert genomic_range_query("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]
    assert genomic_range_query("A", [0], [0]) == [1]
    assert genomic_range_query("T", [0], [0]) == [4]
    assert genomic_range_query("TTTG", [0, 3], [2, 3]) == [4, 3]


def test_genomic_range_query_random():
    for _ in range(200):
        S = "".join(rng.choice("ACGT") for _ in range(rng.randint(1, 15)))
        P, Q = [], []
        for _ in range(rng.randint(1, 8)):
            p = rng.randrange(len(S))
            P.append(p)
            Q.append(rng.randint(p, len(S) - 1))
        assert genomic_range_query(S, P, Q) == _dna_oracle(S, P, Q), (S, P, Q)


def test_genomic_range_query_big():
    n = 100_000
    S = "".join(rng.choice("ACGT") for _ in range(n))
    P, Q = [], []
    for _ in range(50_000):
        p = rng.randrange(n)
        P.append(p)
        Q.append(rng.randint(p, n - 1))
    result = assert_fast(genomic_range_query, S, P, Q, limit=4.0)
    # spot-check a handful against the oracle
    for i in range(0, 50_000, 5_000):
        assert result[i] == min(IMPACT[c] for c in S[P[i] : Q[i] + 1])


# ----------------------------------------------------------------------------- distinct
def test_distinct():
    assert distinct([2, 1, 1, 2, 3, 1]) == 3
    assert distinct([]) == 0
    assert distinct([5]) == 1
    assert distinct([-1_000_000, 1_000_000, -1_000_000]) == 2
    A = [3, 1, 2, 3]
    distinct(A)
    assert A == [3, 1, 2, 3]
    big = [rng.randint(-1_000_000, 1_000_000) for _ in range(100_000)]
    assert assert_fast(distinct, big) == len(set(big))


# ----------------------------------------------------------------------------- triangle
def _triangle_oracle(A):
    for p, q, r in itertools.combinations(range(len(A)), 3):
        a, b, c = A[p], A[q], A[r]
        if a + b > c and b + c > a and c + a > b:
            return 1
    return 0


def test_triangle_examples():
    assert triangle([10, 2, 5, 1, 8, 20]) == 1
    assert triangle([10, 50, 5, 1]) == 0
    assert triangle([]) == 0
    assert triangle([1, 1]) == 0
    assert triangle([2, 2, 2]) == 1
    assert triangle([2**31 - 1, 2**31 - 1, 2**31 - 1]) == 1
    assert triangle([-1, -1, -1]) == 0  # negative "lengths" never form a triangle


def test_triangle_random():
    for _ in range(500):
        A = [rng.randint(-3, 12) for _ in range(rng.randint(0, 8))]
        assert triangle(A) == _triangle_oracle(A), A


def test_triangle_big():
    # zeros never form a triangle; the only one hides at the very end -> brute force needs ~n^3 steps
    A = [0] * 99_997 + [5, 5, 5]
    assert assert_fast(triangle, A) == 1
    assert assert_fast(triangle, [0] * 99_997 + [5, 5, 10]) == 0
    B = [2**i for i in range(31)]  # a+b < c for every triple: no triangle
    assert triangle(B) == 0


# ----------------------------------------------------------------------------- max_product_of_three
def test_max_product_of_three_examples():
    assert max_product_of_three([-3, 1, 2, -2, 5, 6]) == 60
    assert max_product_of_three([-5, -6, 1, 2, 3]) == 90
    assert max_product_of_three([-5, -6, -1, -2]) == -10
    assert max_product_of_three([1, 2, 3]) == 6
    assert max_product_of_three([0, 0, 0, -1]) == 0
    assert max_product_of_three([-1000, -1000, 1000]) == 1_000_000_000


def test_max_product_of_three_random():
    for _ in range(300):
        A = [rng.randint(-10, 10) for _ in range(rng.randint(3, 9))]
        expected = max(A[p] * A[q] * A[r] for p, q, r in itertools.combinations(range(len(A)), 3))
        assert max_product_of_three(A) == expected, A


def test_max_product_of_three_big():
    A = [rng.randint(-1000, 1000) for _ in range(100_000)]
    s = sorted(A)
    expected = max(s[-1] * s[-2] * s[-3], s[0] * s[1] * s[-1])
    assert assert_fast(max_product_of_three, A) == expected
