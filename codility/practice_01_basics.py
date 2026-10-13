"""Practice 1 - iterations, arrays, time complexity.

Companion to notebook ``12_codility_1_foundations.ipynb``.

Replace every ``raise NotImplementedError`` with your own solution, then run::

    python -m pytest codility/test_practice_01_basics.py -v

Tests for functions you have not written yet are *skipped*, not failed.
The tests also check running time, so an O(n^2) answer where O(n) is expected
will fail on the big inputs. All functions must be pure: do not mutate the
arguments you are given (copy first if you need to).
"""


def binary_gap(N: int) -> int:
    """Length of the longest run of zeros surrounded by ones in the binary form of N.

    1 <= N <= 2_147_483_647. Return 0 if there is no such run.

    >>> binary_gap(1041)   # 10000010001
    5
    >>> binary_gap(32)     # 100000 -> the zeros are not closed by a one
    0

    Expected: O(log N).
    """
    raise NotImplementedError


def cyclic_rotation(A: list[int], K: int) -> list[int]:
    """Rotate A to the right K times and return the new list (A may be empty).

    >>> cyclic_rotation([3, 8, 9, 7, 6], 3)
    [9, 7, 6, 3, 8]

    0 <= K <= 100 (but write it so that K can be much larger than len(A)).
    Expected: O(n).
    """
    raise NotImplementedError


def odd_occurrences(A: list[int]) -> int:
    """A has an odd number of elements; every value occurs an even number of times
    except exactly one value. Return that unpaired value.

    >>> odd_occurrences([9, 3, 9, 3, 9, 7, 9])
    7

    Expected: O(n) time. Bonus: O(1) extra memory (think XOR).
    """
    raise NotImplementedError


def frog_jmp(X: int, Y: int, D: int) -> int:
    """A frog at X wants to reach a position >= Y with jumps of fixed length D.

    Return the minimal number of jumps.

    >>> frog_jmp(10, 85, 30)
    3

    1 <= X <= Y <= 1_000_000_000, 1 <= D. Expected: O(1) (no loop!).
    """
    raise NotImplementedError


def perm_missing_elem(A: list[int]) -> int:
    """A holds N *different* integers from the range 1..N+1 (so one is missing).

    Return the missing one. N may be 0.

    >>> perm_missing_elem([2, 3, 1, 5])
    4

    Expected: O(n) time, O(1) extra space (hint: Gauss, section 3.4 of the lesson).
    """
    raise NotImplementedError


def tape_equilibrium(A: list[int]) -> int:
    """Split the non-empty-sided tape at P (1 <= P < N) into A[:P] and A[P:].

    Return the minimal possible value of |sum(A[:P]) - sum(A[P:])|. N >= 2.

    >>> tape_equilibrium([3, 1, 2, 4, 3])
    1

    Expected: O(n) (hint: prefix sums, but you do not need the whole list).
    """
    raise NotImplementedError
