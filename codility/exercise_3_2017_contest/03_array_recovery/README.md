# 03 - ArrayRecovery

**Codility:** [ArrayRecovery](https://app.codility.com/programmers/trainings/3/array_recovery/) - Exercise 3, 2017 Contest

Count the arrays that could have produced a given 'previous smaller value' array.

## Task description

Bob once had an array `A` with `N` elements. Each element was a positive integer not exceeding `M`.

Bob wrote a program to find an array `B`, defined as follows. For every index `J`, let's find the biggest index `K` such that `K < J` and `A[K] < A[J]`. Then set `B[J] = A[K]`. If there is no such index `K`, then set `B[J] = 0`. Intuitively, the `J`-th element of `B` contains the last value smaller than `A[J]` that appears before it, or `0` if there is no such element.

For example, let `A = [2, 5, 3, 7, 9, 6]`. Then `B = [0, 2, 2, 3, 7, 3]`. For instance, `B[5] = 3`, as `A[5]` is 6 and the last value before `A[5]` smaller than 6 is 3.

Bob computed an array `B` and then mistakenly deleted `A`. He now intends to find every valid array `A` from which his program would produce `B`. Count the number of such arrays `A`. Since the answer could be very big, return it modulo `10^9 + 7`.

Write a function:

```python
def solution(B, M)
```

that, given an integer `M` and an array `B` with `N` integers, returns the remainder from the division by `10^9 + 7` of the number of valid arrays `A` from which Bob would get `B`. You can assume that there is at least one such array.

### Examples

1. Given `M = 4`, `B = [0, 2, 2]` the function should return `3`. The possible removed arrays `A` were `[2, 3, 3]`, `[2, 4, 3]` and `[2, 4, 4]`.
2. Given `M = 10`, `B = [0, 3, 5, 6]` the function should return `4`, as the possible arrays `A` were `[3, 5, 6, 7]`, `[3, 5, 6, 8]`, `[3, 5, 6, 9]` and `[3, 5, 6, 10]`.
3. Given `M = 10^5`, `B = [0, 0]` there are `5,000,050,000` possible arrays (the first element in array `A` can be anything in the range `1..10^5` and the second element can be either equal or smaller), so the function should return `49965` (as we are taking modulo `10^9 + 7`).

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- `M` is an integer within the range `[1..1,000,000,000]`;
- each element of array `B` is an integer within the range `[0..M]`;
- there exists at least one valid array `A` from which Bob would get array `B`.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `array_recovery.ipynb` | Stack + combinatorics solution, brute-force and DP checks, timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_3_2017_contest/03_array_recovery/requirements.txt
jupyter lab codility/exercise_3_2017_contest/03_array_recovery/array_recovery.ipynb
```

## Hints

1. Simulate the "previous smaller value" with a monotonic stack of strictly increasing values: pop while `top >= A[J]`, then `B[J]` is the new top (or `0` for an empty stack), then push `A[J]`.
2. Every stack element except the top is revealed by `B`: the element pushed right above it has `B` equal to it. Only the **top** element is still unknown.
3. A run of equal values `B[i] = ... = B[j] = c` forms a non-increasing sequence inside `(c, hi]`, where `hi` is the stack element just above `c` (or `M`). Counting those sequences is a "multiset" count: a binomial coefficient.
4. The binomial arguments can exceed the modulus, but `k <= N < p`, so `C(n, k) = n(n-1)...(n-k+1) / k!` evaluated modulo `p` (with the inverse of `k!`) is still correct.
5. Check small cases against a brute force over all arrays `A`. Complexity: O(N log p).
