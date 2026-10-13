"""Practice 2 - counting elements, prefix sums, sorting.

Companion to notebook ``12_codility_1_foundations.ipynb`` (counting, prefix sums)
and ``13_codility_2_sorting_stacks_leader_slices.ipynb`` (sorting).

Run::

    python -m pytest codility/test_practice_02_counting_prefix_sorting.py -v
"""


def perm_check(A: list[int]) -> int:
    """Return 1 if A is a permutation of 1..N (each value exactly once), else 0.

    >>> perm_check([4, 1, 3, 2])
    1
    >>> perm_check([4, 1, 3])
    0

    Expected: O(n).
    """
    raise NotImplementedError


def frog_river_one(X: int, A: list[int]) -> int:
    """A[k] is the position (1..X) where a leaf falls at second k.

    Return the earliest second at which every position 1..X is covered by a leaf,
    or -1 if that never happens.

    >>> frog_river_one(5, [1, 3, 1, 4, 2, 3, 5, 4])
    6

    Expected: O(n).
    """
    raise NotImplementedError


def missing_integer(A: list[int]) -> int:
    """Return the smallest strictly positive integer that does NOT occur in A.

    Values may be negative or huge.

    >>> missing_integer([1, 3, 6, 4, 1, 2])
    5
    >>> missing_integer([-1, -3])
    1

    Expected: O(n).
    """
    raise NotImplementedError


def max_counters(N: int, A: list[int]) -> list[int]:
    """N counters start at 0. For each K = A[i]:

    * if 1 <= K <= N: increase counter K by one;
    * if K == N + 1: set *all* counters to the current maximum value.

    Return the counters after all operations.

    >>> max_counters(5, [3, 4, 4, 6, 1, 4, 4])
    [3, 2, 2, 4, 2]

    Expected: O(N + len(A)); the naive "reset every counter" is O(N * len(A)).
    """
    raise NotImplementedError


def passing_cars(A: list[int]) -> int:
    """A[i] is 0 for a car travelling east, 1 for west.

    Count the pairs (P, Q) with P < Q, A[P] == 0 and A[Q] == 1.
    Return -1 if the answer exceeds 1_000_000_000.

    >>> passing_cars([0, 1, 0, 1, 1])
    5

    Expected: O(n).
    """
    raise NotImplementedError


def count_div(A: int, B: int, K: int) -> int:
    """Number of integers i in the closed range [A, B] that are divisible by K.

    0 <= A <= B <= 2_000_000_000, K >= 1.

    >>> count_div(6, 11, 2)
    3

    Expected: O(1) - no loop over the range.
    """
    raise NotImplementedError


def genomic_range_query(S: str, P: list[int], Q: list[int]) -> list[int]:
    """S is a DNA string of letters A, C, G, T with impact factors 1, 2, 3, 4.

    For each query k return the minimal impact factor inside S[P[k] : Q[k] + 1].

    >>> genomic_range_query("CAGCCTA", [2, 5, 0], [4, 5, 6])
    [2, 4, 1]

    Expected: O(len(S) + len(P)) - hint: one prefix-sum array per letter.
    """
    raise NotImplementedError


def distinct(A: list[int]) -> int:
    """Number of distinct values in A (A may be empty).

    >>> distinct([2, 1, 1, 2, 3, 1])
    3

    Solve it twice if you like: with sorting (as in the lesson) and with a set.
    """
    raise NotImplementedError


def triangle(A: list[int]) -> int:
    """Return 1 if there are three indices P < Q < R such that A[P], A[Q], A[R]
    can be the sides of a non-degenerate triangle:

        A[P] + A[Q] > A[R]  and  A[Q] + A[R] > A[P]  and  A[R] + A[P] > A[Q]

    otherwise 0. Values can be as large as 2**31 - 1 (and negative).

    >>> triangle([10, 2, 5, 1, 8, 20])
    1

    Expected: O(n log n) (hint: sort; only *neighbours* in sorted order matter).
    """
    raise NotImplementedError


def max_product_of_three(A: list[int]) -> int:
    """Maximal product A[P] * A[Q] * A[R] over any three different indices.

    len(A) >= 3, values may be negative.

    >>> max_product_of_three([-3, 1, 2, -2, 5, 6])
    60

    Expected: O(n log n) (or O(n) if you are brave). Mind the two big negatives!
    """
    raise NotImplementedError
