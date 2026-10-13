import bisect
import itertools
import random
from collections import deque
from functools import lru_cache

import pytest

from helpers import assert_fast
from practice_04_numbers_search_greedy_dp import (
    abs_distinct,
    chocolates_by_numbers,
    coin_change_min,
    count_factors,
    count_semiprimes,
    count_triangles,
    frog_ways,
    ladder,
    max_nonoverlapping_segments,
    min_max_division,
    min_perimeter_rectangle,
    tie_ropes,
)

rng = random.Random(31337)


# ----------------------------------------------------------------------------- count_factors
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (24, 8),
        (36, 9),
        (49, 3),
        (97, 2),
        (2**20, 21),
        (2_147_483_647, 2),  # prime
        (2_147_483_646, 192),  # 2 * 3**2 * 7 * 11 * 31 * 151 * 331
    ],
)
def test_count_factors_examples(n, expected):
    assert count_factors(n) == expected


def test_count_factors_random():
    for _ in range(300):
        n = rng.randint(1, 5000)
        assert count_factors(n) == sum(1 for d in range(1, n + 1) if n % d == 0)


def test_count_factors_speed():
    assert assert_fast(count_factors, 2_147_483_647) == 2


# ----------------------------------------------------------------------------- min_perimeter_rectangle
def test_min_perimeter_rectangle_examples():
    assert min_perimeter_rectangle(30) == 22
    assert min_perimeter_rectangle(1) == 4
    assert min_perimeter_rectangle(4) == 8
    assert min_perimeter_rectangle(7) == 16


def test_min_perimeter_rectangle_random():
    for _ in range(300):
        n = rng.randint(1, 3000)
        expected = min(2 * (a + n // a) for a in range(1, n + 1) if n % a == 0)
        assert min_perimeter_rectangle(n) == expected


def test_min_perimeter_rectangle_speed():
    n = 999_999_937  # prime near 1e9
    assert assert_fast(min_perimeter_rectangle, n) == 2 * (1 + n)
    assert assert_fast(min_perimeter_rectangle, 1_000_000_000) == 2 * (31_250 + 32_000)  # 31250 * 32000


# ----------------------------------------------------------------------------- chocolates_by_numbers
def _choc_oracle(N, M):
    eaten, pos = set(), 0
    while pos not in eaten:
        eaten.add(pos)
        pos = (pos + M) % N
    return len(eaten)


def test_chocolates_examples():
    assert chocolates_by_numbers(10, 4) == 5
    assert chocolates_by_numbers(1, 1) == 1
    assert chocolates_by_numbers(5, 1) == 5
    assert chocolates_by_numbers(6, 6) == 1
    assert chocolates_by_numbers(7, 3) == 7


def test_chocolates_random():
    for _ in range(300):
        N, M = rng.randint(1, 60), rng.randint(1, 120)
        assert chocolates_by_numbers(N, M) == _choc_oracle(N, M), (N, M)


def test_chocolates_speed():
    assert assert_fast(chocolates_by_numbers, 1_000_000_000, 999_999_999, limit=0.5) == 1_000_000_000
    assert assert_fast(chocolates_by_numbers, 1_000_000_000, 500_000_000, limit=0.5) == 2


# ----------------------------------------------------------------------------- count_semiprimes
def _is_semiprime(n):
    if n < 4:
        return False
    count, d = 0, 2
    while d * d <= n:
        while n % d == 0:
            n //= d
            count += 1
        d += 1
    if n > 1:
        count += 1
    return count == 2


def test_count_semiprimes_examples():
    assert count_semiprimes(26, [1, 4, 16], [26, 10, 20]) == [10, 4, 0]
    assert count_semiprimes(4, [4], [4]) == [1]
    assert count_semiprimes(1, [1], [1]) == [0]
    assert count_semiprimes(30, [1], [30]) == [sum(_is_semiprime(i) for i in range(1, 31))]


def test_count_semiprimes_random():
    N = 300
    flags = [False] + [_is_semiprime(i) for i in range(1, N + 1)]
    for _ in range(100):
        P, Q = [], []
        for _ in range(rng.randint(1, 6)):
            p = rng.randint(1, N)
            P.append(p)
            Q.append(rng.randint(p, N))
        assert count_semiprimes(N, P, Q) == [sum(flags[p : q + 1]) for p, q in zip(P, Q)]


def test_count_semiprimes_big():
    N, M = 50_000, 30_000
    P, Q = [], []
    for _ in range(M):
        p = rng.randint(1, N)
        P.append(p)
        Q.append(rng.randint(p, N))
    result = assert_fast(count_semiprimes, N, P, Q, limit=4.0)
    # reference via smallest-prime-factor sieve
    spf = list(range(N + 1))
    for i in range(2, int(N**0.5) + 1):
        if spf[i] == i:
            for k in range(i * i, N + 1, i):
                if spf[k] == k:
                    spf[k] = i
    pref = [0] * (N + 1)
    for i in range(1, N + 1):
        semi = i > 3 and spf[i] != i and spf[i // spf[i]] == i // spf[i]
        pref[i] = pref[i - 1] + semi
    assert result == [pref[q] - pref[p - 1] for p, q in zip(P, Q)]


# ----------------------------------------------------------------------------- ladder
def test_ladder_examples():
    assert ladder([4, 4, 5, 5, 1], [3, 2, 4, 3, 1]) == [5, 1, 8, 0, 1]
    assert ladder([1], [30]) == [1]
    assert ladder([2], [30]) == [2]
    assert ladder([3], [30]) == [3]


def test_ladder_random():
    @lru_cache(None)
    def ways(n):
        return 1 if n <= 1 else ways(n - 1) + ways(n - 2)

    for _ in range(100):
        A = [rng.randint(1, 60) for _ in range(rng.randint(1, 6))]
        B = [rng.randint(1, 30) for _ in A]
        assert ladder(A, B) == [ways(a) % 2**b for a, b in zip(A, B)]


def test_ladder_big():
    A = [rng.randint(1, 50_000) for _ in range(50_000)]
    B = [rng.randint(1, 30) for _ in A]
    result = assert_fast(ladder, A, B, limit=3.0)
    fib = [1, 1]
    for _ in range(50_000):
        fib.append((fib[-1] + fib[-2]) % 2**30)
    assert result == [fib[a] % 2**b for a, b in zip(A, B)]


# ----------------------------------------------------------------------------- min_max_division
def _division_oracle(K, A):
    n = len(A)
    pre = [0]
    for x in A:
        pre.append(pre[-1] + x)
    INF = float("inf")
    dp = [[INF] * (n + 1) for _ in range(K + 1)]  # dp[k][i]: best large sum splitting A[:i] into k blocks
    dp[0][0] = 0
    for k in range(1, K + 1):
        for i in range(n + 1):
            for j in range(i + 1):
                dp[k][i] = min(dp[k][i], max(dp[k - 1][j], pre[i] - pre[j]))
    return dp[K][n]


def test_min_max_division_examples():
    assert min_max_division(3, 5, [2, 1, 5, 1, 2, 2, 2]) == 6
    assert min_max_division(1, 5, [2, 1, 5]) == 8
    assert min_max_division(3, 5, [2, 1, 5]) == 5
    assert min_max_division(5, 5, [1, 2]) == 2
    assert min_max_division(2, 0, [0, 0, 0]) == 0
    assert min_max_division(4, 10, [10, 10, 10, 10, 10]) == 20


def test_min_max_division_random():
    for _ in range(200):
        K = rng.randint(1, 4)
        A = [rng.randint(0, 9) for _ in range(rng.randint(1, 8))]
        assert min_max_division(K, 9, A) == _division_oracle(K, A), (K, A)


def test_min_max_division_big():
    A = [rng.randint(0, 10_000) for _ in range(100_000)]
    K = 1_000
    result = assert_fast(min_max_division, K, 10_000, A, limit=4.0)

    def feasible(limit):
        blocks, cur = 1, 0
        for x in A:
            if cur + x > limit:
                blocks, cur = blocks + 1, x
            else:
                cur += x
        return blocks <= K

    assert feasible(result) and not feasible(result - 1)


# ----------------------------------------------------------------------------- abs_distinct
def test_abs_distinct_examples():
    assert abs_distinct([-5, -3, -1, 0, 3, 6]) == 5
    assert abs_distinct([]) == 0
    assert abs_distinct([0]) == 1
    assert abs_distinct([-3, -3, 3, 3]) == 1
    assert abs_distinct([-2_147_483_648, 2_147_483_647]) == 2
    assert abs_distinct([-7, -7, -7]) == 1


def test_abs_distinct_random():
    for _ in range(300):
        A = sorted(rng.randint(-8, 8) for _ in range(rng.randint(0, 12)))
        assert abs_distinct(A) == len({abs(x) for x in A})


def test_abs_distinct_big():
    A = sorted(rng.randint(-10**9, 10**9) for _ in range(300_000))
    assert assert_fast(abs_distinct, A) == len({abs(x) for x in A})


# ----------------------------------------------------------------------------- count_triangles
def _tri_oracle(A):
    return sum(1 for a, b, c in itertools.combinations(A, 3) if a + b > c and b + c > a and a + c > b)


def test_count_triangles_examples():
    assert count_triangles([10, 2, 5, 1, 8, 12]) == _tri_oracle([10, 2, 5, 1, 8, 12]) == 4
    assert count_triangles([]) == 0
    assert count_triangles([1, 1]) == 0
    assert count_triangles([2, 2, 2]) == 1
    assert count_triangles([1, 1, 2]) == 0  # degenerate
    assert count_triangles([5, 5, 5, 5]) == 4


def test_count_triangles_random():
    for _ in range(500):
        A = [rng.randint(1, 12) for _ in range(rng.randint(0, 10))]
        assert count_triangles(A) == _tri_oracle(A), A


def test_count_triangles_big():
    A = [rng.randint(1, 10**9) for _ in range(1_000)]
    result = assert_fast(count_triangles, A, limit=6.0)
    s = sorted(A)
    expected = 0
    for i in range(len(s)):  # O(n^2 log n) reference with bisect
        for j in range(i + 1, len(s)):
            expected += max(0, bisect.bisect_left(s, s[i] + s[j]) - j - 1)
    assert result == expected


# ----------------------------------------------------------------------------- tie_ropes
def _ropes_oracle(K, A):
    n = len(A)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(i):
            if sum(A[j:i]) >= K:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]


def test_tie_ropes_examples():
    assert tie_ropes(4, [1, 2, 3, 4, 1, 1, 3]) == 3
    assert tie_ropes(1, [1]) == 1
    assert tie_ropes(5, [1, 1]) == 0
    assert tie_ropes(3, [3, 3, 3]) == 3
    assert tie_ropes(10, [1] * 10) == 1
    assert tie_ropes(10, [1] * 9) == 0


def test_tie_ropes_random():
    for _ in range(500):
        K = rng.randint(1, 12)
        A = [rng.randint(1, 8) for _ in range(rng.randint(1, 11))]
        assert tie_ropes(K, A) == _ropes_oracle(K, A), (K, A)


def test_tie_ropes_big():
    A = [rng.randint(1, 1000) for _ in range(100_000)]
    K = 5_000
    cur, expected = 0, 0
    for x in A:
        cur += x
        if cur >= K:
            expected, cur = expected + 1, 0
    assert assert_fast(tie_ropes, K, A) == expected


# ----------------------------------------------------------------------------- max_nonoverlapping_segments
def _segments_oracle(A, B):
    n, best = len(A), 0
    for r in range(n + 1):
        for combo in itertools.combinations(range(n), r):
            ok = all(B[i] < A[j] or B[j] < A[i] for i, j in itertools.combinations(combo, 2))
            if ok:
                best = max(best, r)
    return best


def test_segments_examples():
    assert max_nonoverlapping_segments([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]) == 3
    assert max_nonoverlapping_segments([], []) == 0
    assert max_nonoverlapping_segments([1], [1]) == 1
    assert max_nonoverlapping_segments([1, 1], [1, 1]) == 1
    assert max_nonoverlapping_segments([1, 2], [1, 2]) == 2
    assert max_nonoverlapping_segments([1, 1, 1], [2, 3, 4]) == 1


def test_segments_random():
    for _ in range(300):
        n = rng.randint(0, 8)
        segs = []
        for _ in range(n):
            a = rng.randint(0, 15)
            segs.append((a, a + rng.randint(0, 5)))
        segs.sort(key=lambda s: s[1])
        A, B = [s[0] for s in segs], [s[1] for s in segs]
        assert max_nonoverlapping_segments(A, B) == _segments_oracle(A, B), (A, B)


def test_segments_big():
    segs = []
    for _ in range(100_000):
        a = rng.randint(0, 10**9)
        segs.append((a, a + rng.randint(0, 5_000)))
    segs.sort(key=lambda s: s[1])
    A, B = [s[0] for s in segs], [s[1] for s in segs]
    last, expected = -1, 0
    for a, b in segs:
        if a > last:
            expected, last = expected + 1, b
    assert assert_fast(max_nonoverlapping_segments, A, B) == expected


# ----------------------------------------------------------------------------- coin_change_min
def _coin_bfs(C, k):
    if k == 0:
        return 0
    seen, queue = {0}, deque([(0, 0)])
    while queue:
        total, steps = queue.popleft()
        for c in C:
            nxt = total + c
            if nxt == k:
                return steps + 1
            if nxt < k and nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))
    return -1


def test_coin_change_examples():
    assert coin_change_min([1, 3, 4], 6) == 2
    assert coin_change_min([5, 10], 3) == -1
    assert coin_change_min([1, 2, 5], 11) == 3
    assert coin_change_min([2], 0) == 0
    assert coin_change_min([2], 3) == -1
    assert coin_change_min([186, 419, 83, 408], 6249) == 20
    assert coin_change_min([1], 5) == 5


def test_coin_change_random():
    for _ in range(300):
        C = rng.sample(range(1, 15), rng.randint(1, 4))
        k = rng.randint(0, 40)
        assert coin_change_min(C, k) == _coin_bfs(C, k), (C, k)


def test_coin_change_big():
    assert assert_fast(coin_change_min, [1, 5, 10, 25, 50, 100], 50_000) == 500
    assert assert_fast(coin_change_min, [7, 13, 29, 101], 20_000, limit=3.0) != 0


# ----------------------------------------------------------------------------- frog_ways
def _frog_oracle(S, k, q):
    @lru_cache(None)
    def ways(pos):
        if pos == 0:
            return 1
        return sum(ways(pos - s) for s in S if s <= pos)

    return ways(k) % q


def test_frog_ways_examples():
    assert frog_ways([1, 2], 4, 1000) == 5
    assert frog_ways([1], 10, 7) == 1
    assert frog_ways([2], 3, 100) == 0
    assert frog_ways([1, 2], 10, 1000) == 89
    assert frog_ways([1, 2], 10, 10) == 9
    assert frog_ways([3, 5], 0 + 1, 100) == 0


def test_frog_ways_random():
    for _ in range(200):
        S = rng.sample(range(1, 8), rng.randint(1, 3))
        k = rng.randint(1, 25)
        q = rng.randint(2, 1000)
        assert frog_ways(S, k, q) == _frog_oracle(tuple(S), k, q), (S, k, q)


def test_frog_ways_big():
    S = list(range(1, 21))
    k, q = 10_000, 1_000_003
    ref = [1] + [0] * k
    for j in range(1, k + 1):
        ref[j] = sum(ref[j - s] for s in S if s <= j) % q
    assert assert_fast(frog_ways, S, k, q, limit=4.0) == ref[k]
