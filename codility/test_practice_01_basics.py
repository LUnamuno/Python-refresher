import random
from collections import Counter

import pytest

from helpers import assert_fast
from practice_01_basics import (
    binary_gap,
    cyclic_rotation,
    frog_jmp,
    odd_occurrences,
    perm_missing_elem,
    tape_equilibrium,
)

rng = random.Random(2024)


# ----------------------------------------------------------------------------- binary_gap
def _binary_gap_oracle(n):
    return max(len(g) for g in bin(n)[2:].strip("0").split("1"))


@pytest.mark.parametrize(
    "n, expected",
    [(1, 0), (2, 0), (5, 1), (9, 2), (15, 0), (32, 0), (529, 4), (1041, 5), (20, 1), (2**31 - 1, 0), (2**30 + 1, 29)],
)
def test_binary_gap_examples(n, expected):
    assert binary_gap(n) == expected


def test_binary_gap_random():
    for _ in range(500):
        n = rng.randint(1, 2**31 - 1)
        assert binary_gap(n) == _binary_gap_oracle(n), n


# ----------------------------------------------------------------------------- cyclic_rotation
@pytest.mark.parametrize(
    "A, K, expected",
    [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
        ([], 5, []),
        ([7], 100, [7]),
        ([1, 2, 3], 0, [1, 2, 3]),
        ([1, 2, 3, 4, 5], 12, [4, 5, 1, 2, 3]),
    ],
)
def test_cyclic_rotation_examples(A, K, expected):
    assert cyclic_rotation(A, K) == expected


def test_cyclic_rotation_does_not_mutate():
    A = [1, 2, 3, 4]
    cyclic_rotation(A, 1)
    assert A == [1, 2, 3, 4]


def test_cyclic_rotation_random():
    for _ in range(200):
        A = [rng.randint(-5, 5) for _ in range(rng.randint(0, 12))]
        K = rng.randint(0, 40)
        expected = list(A)
        for _ in range(K):  # literal definition, one rotation at a time
            if expected:
                expected.insert(0, expected.pop())
        assert cyclic_rotation(A, K) == expected


# ----------------------------------------------------------------------------- odd_occurrences
def test_odd_occurrences_examples():
    assert odd_occurrences([9, 3, 9, 3, 9, 7, 9]) == 7
    assert odd_occurrences([42]) == 42
    assert odd_occurrences([1, 1, 2]) == 2
    assert odd_occurrences([5, 4, 5, 4, 3, 3, 8, 3, 3]) == 8


def test_odd_occurrences_random():
    for _ in range(200):
        pairs = [rng.randint(1, 20) for _ in range(rng.randint(0, 15))]
        odd = rng.randint(100, 120)
        A = pairs + pairs + [odd]
        rng.shuffle(A)
        assert odd_occurrences(A) == odd


def test_odd_occurrences_big():
    vals = list(range(1, 500_001))
    A = vals + vals + [10**9]
    rng.shuffle(A)
    assert assert_fast(odd_occurrences, A) == 10**9


# ----------------------------------------------------------------------------- frog_jmp
@pytest.mark.parametrize(
    "X, Y, D, expected",
    [(10, 85, 30, 3), (1, 1, 5, 0), (1, 2, 5, 1), (1, 1_000_000_000, 1, 999_999_999), (5, 25, 5, 4), (5, 26, 5, 5)],
)
def test_frog_jmp(X, Y, D, expected):
    assert frog_jmp(X, Y, D) == expected


def test_frog_jmp_is_constant_time():
    assert assert_fast(frog_jmp, 1, 1_000_000_000, 1, limit=0.5) == 999_999_999


# ----------------------------------------------------------------------------- perm_missing_elem
def test_perm_missing_elem_examples():
    assert perm_missing_elem([2, 3, 1, 5]) == 4
    assert perm_missing_elem([]) == 1
    assert perm_missing_elem([2]) == 1
    assert perm_missing_elem([1]) == 2
    assert perm_missing_elem([1, 2, 3]) == 4


def test_perm_missing_elem_random():
    for _ in range(200):
        n = rng.randint(1, 30)
        full = list(range(1, n + 2))
        missing = rng.choice(full)
        A = [x for x in full if x != missing]
        rng.shuffle(A)
        assert perm_missing_elem(A) == missing


def test_perm_missing_elem_big():
    n = 100_000
    A = list(range(1, n + 2))
    A.remove(54_321)
    rng.shuffle(A)
    assert assert_fast(perm_missing_elem, A) == 54_321


# ----------------------------------------------------------------------------- tape_equilibrium
def _tape_oracle(A):
    return min(abs(sum(A[:p]) - sum(A[p:])) for p in range(1, len(A)))


def test_tape_equilibrium_examples():
    assert tape_equilibrium([3, 1, 2, 4, 3]) == 1
    assert tape_equilibrium([1, 2]) == 1
    assert tape_equilibrium([-1000, 1000]) == 2000
    assert tape_equilibrium([5, 5]) == 0
    assert tape_equilibrium([-1, -2, -3]) == 0  # (-1 -2) vs (-3)


def test_tape_equilibrium_random():
    for _ in range(300):
        A = [rng.randint(-20, 20) for _ in range(rng.randint(2, 12))]
        assert tape_equilibrium(A) == _tape_oracle(A), A


def test_tape_equilibrium_big():
    A = [rng.randint(-1000, 1000) for _ in range(100_000)]
    P = sum(A)
    # O(n) oracle with running sum
    left, best = 0, float("inf")
    for p in range(len(A) - 1):
        left += A[p]
        best = min(best, abs(left - (P - left)))
    assert assert_fast(tape_equilibrium, A) == best


def test_tape_equilibrium_does_not_mutate():
    A = [3, 1, 2, 4, 3]
    tape_equilibrium(A)
    assert A == [3, 1, 2, 4, 3]
