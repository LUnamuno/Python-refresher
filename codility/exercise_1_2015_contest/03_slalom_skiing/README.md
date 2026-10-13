# 03 - SlalomSkiing

**Codility:** [SlalomSkiing](https://app.codility.com/programmers/trainings/1/slalom_skiing/) - Exercise 1, 2015 Contest

Maximum number of gates passed in a slalom with at most two changes of direction.

## Task description

You are a skier participating in a giant slalom. The slalom track is located on a ski slope, goes downhill and is fenced by barriers on both sides. The barriers are perpendicular to the starting line located at the top of the slope. There are `N` slalom gates on the track. Each gate is placed at a distinct distance from the starting line and from the barrier on the right-hand side (looking downhill).

You start from any place on the starting line, ski down the track passing as many gates as possible, and finish the slalom at the bottom of the slope. Passing a gate means skiing through the position of the gate.

You can ski downhill in either of two directions: to the left or to the right. When you ski to the left, you pass gates of increasing distances from the right barrier, and when you ski to the right, you pass gates of decreasing distances from the right barrier. You want to ski to the left at the beginning.

Unfortunately, changing direction (left to right or vice versa) is exhausting, so you have decided to change direction at most two times during your ride. Because of this, you have allowed yourself to miss some of the gates on the way down the slope. You would like to know the maximum number of gates that you can pass with at most two changes of direction.

The arrangement of the gates is given as an array `A` consisting of `N` integers, whose elements specify the positions of the gates: gate `K` (for `0 <= K < N`) is at a distance of `K + 1` from the starting line, and at a distance of `A[K]` from the right barrier.

For example, consider array `A` such that:

```
A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]      (N = 13)
```

The original statement shows a picture of this track with a course that passes eight gates. After starting, you ski to the left (from your own perspective). You pass gates 2, 3, 5, 6 and then change direction to the right. After that you pass gates 7, 8 and then change direction to the left. Finally, you pass gates 10, 11 and finish the slalom. There is no possible way of passing more gates using at most two changes of direction.

Write a function:

```python
def solution(A)
```

that, given an array `A` consisting of `N` integers, describing the positions of the gates on the track, returns the maximum number of gates that you can pass during one ski run.

For example, given the above data, the function should return `8`, as explained above.

For the array `A = [1, 5]` (`N = 2`) the function should return `2`.

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- each element of array `A` is an integer within the range `[1..1,000,000,000]`;
- the elements of `A` are all distinct.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `slalom_skiing.ipynb` | Fenwick-tree DP solution, brute force and quadratic DP references, timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_1_2015_contest/03_slalom_skiing/requirements.txt
jupyter lab codility/exercise_1_2015_contest/03_slalom_skiing/slalom_skiing.ipynb
```

## Hints

1. The gates passed form a subsequence of `A` that is **increasing**, then **decreasing**, then **increasing** (each phase may be a single gate; the first direction is left, so the first phase is the increasing one).
2. Dynamic programming with three states per gate `i`: `f0[i]` (last gate of phase 1), `f1[i]` (phase 2) and `f2[i]` (phase 3).
3. `f0[i] = 1 + max f0[j]` over `j < i` with `A[j] < A[i]`; `f1[i] = 1 + max(f0[j], f1[j])` over `j < i` with `A[j] > A[i]`; `f2[i] = 1 + max(f1[j], f2[j])` over `j < i` with `A[j] < A[i]`.
4. The quadratic version is too slow for `N = 100,000`. Compress the values and use **Fenwick trees for prefix maxima** (one per state, the second one on reversed ranks). Complexity: O(N log N).
5. Check the DP against a brute force over all subsets for small `N`.
