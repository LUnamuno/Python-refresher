"""Practice 4 - number theory, binary search, caterpillar, greedy, dynamic programming.

Companion to notebooks ``14_codility_3_number_theory.ipynb`` and
``15_codility_4_search_greedy_dp.ipynb``.

Run::

    python -m pytest codility/test_practice_04_numbers_search_greedy_dp.py -v
"""

# --------------------------------------------------------------------------- number theory


def count_factors(N: int) -> int:
    """Number of positive divisors of N (1 <= N <= 2_147_483_647).

    >>> count_factors(24)
    8

    Expected: O(sqrt N).
    """
    raise NotImplementedError


def min_perimeter_rectangle(N: int) -> int:
    """Minimal perimeter 2 * (a + b) of a rectangle with integer sides a * b == N.

    1 <= N <= 1_000_000_000.

    >>> min_perimeter_rectangle(30)
    22

    Expected: O(sqrt N).
    """
    raise NotImplementedError


def chocolates_by_numbers(N: int, M: int) -> int:
    """N chocolates are arranged in a circle, numbered 0..N-1. Starting at 0 you eat
    every M-th chocolate (wrapping around) and stop when you reach one you have
    already eaten. Return how many chocolates you eat.

    1 <= N, M <= 1_000_000_000.

    >>> chocolates_by_numbers(10, 4)
    5

    Expected: O(log(N + M)) (Euclid).
    """
    raise NotImplementedError


def count_semiprimes(N: int, P: list[int], Q: list[int]) -> list[int]:
    """A semiprime is a product of exactly two primes, not necessarily different
    (4, 6, 9, 10, 14, 15, ...). For each query k return how many semiprimes lie in
    the closed range [P[k], Q[k]] (1 <= P[k] <= Q[k] <= N).

    >>> count_semiprimes(26, [1, 4, 16], [26, 10, 20])
    [10, 4, 0]

    Expected: O(N log log N + M) (sieve with smallest prime factors + prefix sums).
    """
    raise NotImplementedError


def ladder(A: list[int], B: list[int]) -> list[int]:
    """Ladder i has A[i] rungs. You climb 1 or 2 rungs per step.

    For each i return the number of distinct ways to reach the top, modulo 2**B[i].

    >>> ladder([4, 4, 5, 5, 1], [3, 2, 4, 3, 1])
    [5, 1, 8, 0, 1]

    1 <= A[i] <= 50_000, 1 <= B[i] <= 30. Expected: O(max(A) + len(A)).
    Hint: the answer is a Fibonacci number; compute them once, modulo 2**30.
    """
    raise NotImplementedError


# --------------------------------------------------------------------------- binary search


def min_max_division(K: int, M: int, A: list[int]) -> int:
    """Split A (non-negative integers, each <= M) into K contiguous blocks (blocks
    may be empty). The "large sum" is the biggest block sum. Return the smallest
    large sum achievable.

    >>> min_max_division(3, 5, [2, 1, 5, 1, 2, 2, 2])
    6

    Expected: O(n log(sum A)) - binary search on the answer, like ``boards`` in the lesson.
    """
    raise NotImplementedError


# --------------------------------------------------------------------------- caterpillar


def abs_distinct(A: list[int]) -> int:
    """A is sorted in non-decreasing order. Return the number of distinct absolute
    values in it (A may be empty).

    >>> abs_distinct([-5, -3, -1, 0, 3, 6])
    5

    Expected: O(n) with two indices walking in from both ends.
    """
    raise NotImplementedError


def count_triangles(A: list[int]) -> int:
    """Count the triplets of *indices* x < y < z whose values can be the sides of a
    non-degenerate triangle (each pair of sides sums to more than the third).
    A is NOT sorted and its values are positive.

    >>> count_triangles([10, 2, 5, 1, 8, 12])
    4

    Expected: O(n^2) - sort, then the caterpillar of section 15.2.
    """
    raise NotImplementedError


# --------------------------------------------------------------------------- greedy


def tie_ropes(K: int, A: list[int]) -> int:
    """Ropes of lengths A[i] lie in a row; you may tie two *adjacent* ropes together
    (the result is one longer rope that is adjacent to its former neighbours).

    Return the maximum number of ropes of length >= K you can end up with.

    >>> tie_ropes(4, [1, 2, 3, 4, 1, 1, 3])
    3

    Expected: O(n).
    """
    raise NotImplementedError


def max_nonoverlapping_segments(A: list[int], B: list[int]) -> int:
    """Segments [A[i], B[i]] on a line, given sorted by right end (B non-decreasing)
    with A[i] <= B[i]. Segments that share even one point overlap.

    Return the size of the largest set of pairwise non-overlapping segments.

    >>> max_nonoverlapping_segments([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])
    3

    Expected: O(n) (always take the segment that ends first).
    """
    raise NotImplementedError


# --------------------------------------------------------------------------- dynamic programming


def coin_change_min(C: list[int], k: int) -> int:
    """Minimum number of coins (unlimited supply of each denomination in C) that sum
    to exactly k, or -1 if impossible. k >= 0 (k == 0 needs 0 coins).

    >>> coin_change_min([1, 3, 4], 6)    # greedy would answer 3 (4+1+1)
    2
    >>> coin_change_min([5, 10], 3)
    -1

    Expected: O(len(C) * k).
    """
    raise NotImplementedError


def frog_ways(S: list[int], k: int, q: int) -> int:
    """A frog starts at 0 and wants to land exactly on k. It may jump any of the
    distances in S (repeatedly). Count the different jump sequences, modulo q.

    >>> frog_ways([1, 2], 4, 1000)       # 1111, 112, 121, 211, 22
    5

    Expected: O(len(S) * k).
    """
    raise NotImplementedError
