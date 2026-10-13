import itertools
import random
from collections import Counter

import pytest

from helpers import assert_fast
from practice_03_stacks_leader_slices import (
    brackets,
    dominator,
    equi_leader,
    fish,
    max_double_slice_sum,
    max_profit,
    max_slice_sum,
    stone_wall,
)

rng = random.Random(99)


# ----------------------------------------------------------------------------- brackets
def _brackets_oracle(s):
    prev = None
    while prev != s:  # repeatedly delete matched neighbours
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return 1 if s == "" else 0


@pytest.mark.parametrize(
    "s, expected",
    [("{[()()]}", 1), ("([)()]", 0), ("", 1), ("(", 0), (")", 0), ("()", 1), (")(", 0), ("((()))", 1), ("([{}])", 1), ("(]", 0), ("{{{{", 0), ("}}}}", 0)],
)
def test_brackets_examples(s, expected):
    assert brackets(s) == expected


def test_brackets_random():
    for _ in range(1000):
        s = "".join(rng.choice("()[]{}") for _ in range(rng.randint(0, 10)))
        assert brackets(s) == _brackets_oracle(s), s
    for _ in range(300):  # also generate valid strings
        s = ""
        for _ in range(rng.randint(0, 6)):
            o, c = rng.choice(["()", "[]", "{}"])
            pos = rng.randint(0, len(s))
            s = s[:pos] + o + c + s[pos:]
        assert brackets(s) == 1, s


def test_brackets_big():
    assert assert_fast(brackets, "(" * 150_000 + ")" * 150_000) == 1
    assert assert_fast(brackets, "(" * 150_000 + ")" * 149_999) == 0
    assert assert_fast(brackets, "([{}])" * 40_000) == 1


# ----------------------------------------------------------------------------- fish
def _fish_oracle(A, B):
    fishes = list(zip(A, B))
    changed = True
    while changed:
        changed = False
        for i in range(len(fishes) - 1):
            (sa, da), (sb, db) = fishes[i], fishes[i + 1]
            if da == 1 and db == 0:  # they meet
                fishes.pop(i + 1 if sa > sb else i)
                changed = True
                break
    return len(fishes)


def test_fish_examples():
    assert fish([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
    assert fish([1], [0]) == 1
    assert fish([1, 2], [1, 0]) == 1
    assert fish([2, 1], [1, 0]) == 1
    assert fish([1, 2, 3], [1, 1, 1]) == 3
    assert fish([1, 2, 3], [0, 0, 0]) == 3
    assert fish([3, 2, 1], [0, 0, 0]) == 3
    assert fish([5, 4, 3, 2, 1], [1, 1, 1, 1, 1]) == 5


def test_fish_random():
    for _ in range(500):
        n = rng.randint(1, 9)
        A = rng.sample(range(1, 30), n)
        B = [rng.randint(0, 1) for _ in range(n)]
        assert fish(A, B) == _fish_oracle(A, B), (A, B)


def test_fish_big():
    n = 100_000
    A = rng.sample(range(1, 10**9), n)
    B = [rng.randint(0, 1) for _ in range(n)]
    # O(n) reference using a stack
    stack, alive_up = [], 0
    for a, b in zip(A, B):
        if b == 1:
            stack.append(a)
        else:
            while stack and stack[-1] < a:
                stack.pop()
            if not stack:
                alive_up += 1
    expected = alive_up + len(stack)
    assert assert_fast(fish, A, B, limit=3.0) == expected


# ----------------------------------------------------------------------------- stone_wall
def _wall_oracle(H):
    """Split at the minimum: one block covers the whole base, recurse on the pieces above it."""
    if not H:
        return 0
    m = min(H)
    count, part = 1, []
    for h in H + [m]:
        if h == m:
            count += _wall_oracle([x - m for x in part]) if part else 0
            part = []
        else:
            part.append(h)
    return count


def test_stone_wall_examples():
    assert stone_wall([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
    assert stone_wall([1]) == 1
    assert stone_wall([5, 5, 5]) == 1
    assert stone_wall([1, 2, 3]) == 3
    assert stone_wall([3, 2, 1]) == 3
    assert stone_wall([1, 2, 1]) == 2
    assert stone_wall([2, 1, 2]) == 3


def test_stone_wall_random():
    for _ in range(500):
        H = [rng.randint(1, 5) for _ in range(rng.randint(1, 10))]
        assert stone_wall(H) == _wall_oracle(H), H


def test_stone_wall_big():
    H = [rng.randint(1, 10**9) for _ in range(100_000)]
    assert assert_fast(stone_wall, H) == _stack_wall(H)


def _stack_wall(H):
    stack, blocks = [], 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] < h:
            stack.append(h)
            blocks += 1
    return blocks


# ----------------------------------------------------------------------------- dominator
def _leader(A):
    if not A:
        return None
    v, c = Counter(A).most_common(1)[0]
    return v if c > len(A) // 2 else None


def test_dominator_examples():
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    assert A[dominator(A)] == 3
    assert dominator([]) == -1
    assert dominator([1, 2]) == -1
    assert dominator([1, 2, 3, 4]) == -1
    assert dominator([7]) == 0
    assert dominator([1, 1, 2, 2]) == -1  # exactly half is NOT more than half


def test_dominator_random():
    for _ in range(500):
        A = [rng.randint(0, 3) for _ in range(rng.randint(0, 11))]
        idx = dominator(A)
        leader = _leader(A)
        if leader is None:
            assert idx == -1, A
        else:
            assert 0 <= idx < len(A) and A[idx] == leader, A


def test_dominator_big():
    A = [rng.randint(0, 10**6) for _ in range(49_999)] + [42] * 50_001
    rng.shuffle(A)
    assert A[assert_fast(dominator, A)] == 42
    B = [42] * 50_000 + list(range(1_000_000, 1_050_000))  # exactly half is not enough
    rng.shuffle(B)
    assert assert_fast(dominator, B) == -1


# ----------------------------------------------------------------------------- equi_leader
def _equi_oracle(A):
    total = 0
    for s in range(len(A) - 1):
        l, r = _leader(A[: s + 1]), _leader(A[s + 1 :])
        if l is not None and l == r:
            total += 1
    return total


def test_equi_leader_examples():
    assert equi_leader([4, 3, 4, 4, 4, 2]) == 2
    assert equi_leader([1]) == 0
    assert equi_leader([1, 1]) == 1
    assert equi_leader([1, 2]) == 0
    assert equi_leader([5, 5, 5, 5]) == 3


def test_equi_leader_random():
    for _ in range(500):
        A = [rng.randint(0, 2) for _ in range(rng.randint(1, 11))]
        assert equi_leader(A) == _equi_oracle(A), A


def test_equi_leader_big():
    A = [7] * 60_000 + [rng.randint(0, 5) for _ in range(40_000)]
    rng.shuffle(A)
    # the oracle is O(n) via counts
    n, c = len(A), A.count(7)
    left, expected = 0, 0
    for s in range(n - 1):
        left += A[s] == 7
        if left > (s + 1) // 2 and (c - left) > (n - s - 1) // 2:
            expected += 1
    assert assert_fast(equi_leader, A) == expected


# ----------------------------------------------------------------------------- max_profit
def _profit_oracle(A):
    return max([0] + [A[q] - A[p] for p, q in itertools.combinations(range(len(A)), 2)])


def test_max_profit_examples():
    assert max_profit([23171, 21011, 21123, 21366, 21013, 21367]) == 356
    assert max_profit([]) == 0
    assert max_profit([5]) == 0
    assert max_profit([5, 4, 3]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([0, 200_000]) == 200_000


def test_max_profit_random():
    for _ in range(500):
        A = [rng.randint(0, 20) for _ in range(rng.randint(0, 10))]
        assert max_profit(A) == _profit_oracle(A), A


def test_max_profit_big():
    A = [rng.randint(0, 200_000) for _ in range(400_000)]
    lo, best = A[0], 0
    for x in A:
        lo = min(lo, x)
        best = max(best, x - lo)
    assert assert_fast(max_profit, A) == best


# ----------------------------------------------------------------------------- max_slice_sum
def _slice_oracle(A):
    return max(sum(A[p : q + 1]) for p in range(len(A)) for q in range(p, len(A)))


def test_max_slice_sum_examples():
    assert max_slice_sum([3, 2, -6, 4, 0]) == 5
    assert max_slice_sum([-10]) == -10
    assert max_slice_sum([-10, -3, -7]) == -3
    assert max_slice_sum([5, -7, 3, 5, -2, 4, -1]) == 10
    assert max_slice_sum([0]) == 0
    assert max_slice_sum([1, 2, 3]) == 6
    assert max_slice_sum([-1, 5, -1]) == 5
    assert max_slice_sum([-2, 1]) == 1


def test_max_slice_sum_random():
    for _ in range(500):
        A = [rng.randint(-10, 10) for _ in range(rng.randint(1, 12))]
        assert max_slice_sum(A) == _slice_oracle(A), A


def test_max_slice_sum_big():
    A = [rng.randint(-1000, 1000) for _ in range(1_000_000)]
    best = cur = A[0]
    for x in A[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    assert assert_fast(max_slice_sum, A, limit=4.0) == best


# ----------------------------------------------------------------------------- max_double_slice_sum
def _double_oracle(A):
    n, best = len(A), 0
    for x, y, z in itertools.combinations(range(n), 3):
        best = max(best, sum(A[x + 1 : y]) + sum(A[y + 1 : z]))
    return best


def test_max_double_slice_sum_examples():
    assert max_double_slice_sum([3, 2, 6, -1, 4, 5, -1, 2]) == 17
    assert max_double_slice_sum([1, 2, 3]) == 0
    assert max_double_slice_sum([-5, -5, -5]) == 0
    assert max_double_slice_sum([0, 10, -5, 10, 0]) == 20  # the negative element is the free "hole" Y
    assert max_double_slice_sum([0, 10, 10, 10, 0]) == 20  # Y must be dropped from a run of positives
    assert max_double_slice_sum([5, 5, 5, 5, 5, 5]) == 15


def test_max_double_slice_sum_random():
    for _ in range(500):
        A = [rng.randint(-8, 8) for _ in range(rng.randint(3, 10))]
        assert max_double_slice_sum(A) == _double_oracle(A), A


def test_max_double_slice_sum_big():
    A = [rng.randint(-10_000, 10_000) for _ in range(100_000)]
    n = len(A)
    left = [0] * n  # best slice sum ending at i (may be empty)
    right = [0] * n
    for i in range(1, n - 1):
        left[i] = max(0, left[i - 1] + A[i])
    for i in range(n - 2, 0, -1):
        right[i] = max(0, right[i + 1] + A[i])
    expected = max(left[y - 1] + right[y + 1] for y in range(1, n - 1))
    assert assert_fast(max_double_slice_sum, A) == expected
