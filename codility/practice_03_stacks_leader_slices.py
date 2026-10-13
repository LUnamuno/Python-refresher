"""Practice 3 - stacks and queues, leader, maximum slice.

Companion to notebook ``13_codility_2_sorting_stacks_leader_slices.ipynb``.

Run::

    python -m pytest codility/test_practice_03_stacks_leader_slices.py -v
"""


def brackets(S: str) -> int:
    """Return 1 if S is a properly nested string over ()[]{} else 0.

    The empty string is properly nested.

    >>> brackets("{[()()]}")
    1
    >>> brackets("([)()]")
    0

    Expected: O(n) with a stack.
    """
    raise NotImplementedError


def fish(A: list[int], B: list[int]) -> int:
    """Fish i has size A[i] (all sizes distinct) and swims in direction B[i]:
    0 = upstream (towards index 0), 1 = downstream (towards the last index).
    Fish are listed in river order and all move at the same speed.

    When two fish meet, the bigger one eats the smaller one. Return how many
    fish stay alive.

    >>> fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
    2

    Expected: O(n) (stack of downstream fish).
    """
    raise NotImplementedError


def stone_wall(H: list[int]) -> int:
    """H[i] is the height the wall must have at position i. Blocks are rectangles
    of any width but must be exactly as tall as the part of the wall they cover.

    Return the minimum number of blocks.

    >>> stone_wall([8, 8, 5, 7, 9, 8, 7, 4, 8])
    7

    Expected: O(n) with a stack.
    """
    raise NotImplementedError


def dominator(A: list[int]) -> int:
    """Return the index of *any* element whose value occurs in more than half of
    the positions of A, or -1 if there is no such value (also for empty A).

    >>> A = [3, 4, 3, 2, 3, -1, 3, 3]
    >>> A[dominator(A)]
    3

    Expected: O(n) (the Boyer-Moore "golden leader" of the lesson).
    """
    raise NotImplementedError


def equi_leader(A: list[int]) -> int:
    """Count the split positions S (0 <= S < N - 1) such that A[:S+1] and A[S+1:]
    both have a leader (value in more than half of that part) and it is the
    *same* value in both parts.

    >>> equi_leader([4, 3, 4, 4, 4, 2])
    2

    Expected: O(n).
    """
    raise NotImplementedError


def max_profit(A: list[int]) -> int:
    """A[i] is the price of a share on day i. Buy on day p, sell on a later day q.

    Return the maximum possible profit A[q] - A[p], or 0 if no profit can be made
    (also for fewer than two days).

    >>> max_profit([23171, 21011, 21123, 21366, 21013, 21367])
    356

    Expected: O(n).
    """
    raise NotImplementedError


def max_slice_sum(A: list[int]) -> int:
    """Maximum sum of a NON-EMPTY contiguous slice of A.

    Careful: the lesson allows the empty slice (sum 0). Here the slice must contain
    at least one element, so for an all-negative array the answer is the
    largest (least negative) element.

    >>> max_slice_sum([3, 2, -6, 4, 0])
    5
    >>> max_slice_sum([-10, -3, -7])
    -3

    Expected: O(n) (Kadane).
    """
    raise NotImplementedError


def max_double_slice_sum(A: list[int]) -> int:
    """A "double slice" is a triplet (X, Y, Z) with 0 <= X < Y < Z < N; its sum is
    A[X+1] + ... + A[Y-1] + A[Y+1] + ... + A[Z-1]  (Y itself, and the ends, are
    excluded; either part may be empty).

    Return the maximum double-slice sum. N >= 3.

    >>> max_double_slice_sum([3, 2, 6, -1, 4, 5, -1, 2])
    17

    Expected: O(n) (hint: best slice ending before Y, best slice starting after Y).
    """
    raise NotImplementedError
