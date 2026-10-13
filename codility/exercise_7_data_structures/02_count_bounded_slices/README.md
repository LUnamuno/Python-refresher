# 02 - CountBoundedSlices

**Codility:** [CountBoundedSlices](https://app.codility.com/programmers/trainings/7/count_bounded_slices/) - Exercise 7, Data Structures - *medium*

Calculate the number of slices in which `maximum - minimum <= K`.

## Task description

An integer `K` and a non-empty array `A` consisting of `N` integers are given.

A pair of integers `(P, Q)`, such that `0 <= P <= Q < N`, is called a *slice* of array `A`.

A *bounded slice* is a slice in which the difference between the maximum and minimum values in the slice is less than or equal to `K`. More precisely it is a slice such that `max(A[P], A[P+1], ..., A[Q]) - min(A[P], A[P+1], ..., A[Q]) <= K`.

The goal is to calculate the number of bounded slices.

For example, consider `K = 2` and array `A` such that:

```
A[0] = 3
A[1] = 5
A[2] = 7
A[3] = 6
A[4] = 3
```

There are exactly nine bounded slices: `(0,0), (0,1), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3), (4,4)`.

Write a function:

```python
def solution(K, A)
```

that, given an integer `K` and a non-empty array `A` of `N` integers, returns the number of bounded slices of array `A`.

If the number of bounded slices is greater than `1,000,000,000`, the function should return `1,000,000,000`.

For the example above the function should return `9`.

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- `K` is an integer within the range `[0..1,000,000,000]`;
- each element of array `A` is an integer within the range `[-1,000,000,000..1,000,000,000]`.

Write an **efficient** algorithm.

## Files

| File                          | Purpose                                                        |
|-------------------------------|----------------------------------------------------------------|
| `README.md`                   | This description.                                              |
| `requirements.txt`            | Dependencies of this mini-project.                             |
| `count_bounded_slices.ipynb`  | Solution, official example, edge cases, brute-force check and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_7_data_structures/02_count_bounded_slices/requirements.txt
jupyter lab codility/exercise_7_data_structures/02_count_bounded_slices/count_bounded_slices.ipynb
```

## Hints

1. If `(P, Q)` is bounded, every sub-slice of it is bounded too. So for a fixed right end `Q`, the valid left ends form a contiguous range `[P_min(Q), Q]`, and `P_min(Q)` never decreases when `Q` grows: a **two-pointer / sliding window**.
2. For each `Q` add `Q - P + 1` slices ending at `Q`.
3. You need the max and the min of the current window in O(1): keep two **monotonic deques** (`collections.deque`), one decreasing for the max and one increasing for the min, storing indices.
4. Shrink the window from the left while `max - min > K`, popping expired indices from the deque fronts.
5. Cap the answer at `1,000,000,000` (in Python there is no overflow, but the task asks for the cap).
6. Complexity: O(N) time, O(N) space. A brute force is O(N^2) and fails the large tests.
