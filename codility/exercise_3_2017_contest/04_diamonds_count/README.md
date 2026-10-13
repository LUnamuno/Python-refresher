# 04 - DiamondsCount

**Codility:** [DiamondsCount](https://app.codility.com/programmers/trainings/3/diamonds_count/) - Exercise 3, 2017 Contest

Count the rhombi with axis-parallel diagonals whose four vertices are given points.

## Task description

A diamond is a quadrilateral whose four sides all have the same length and whose diagonals are parallel to the coordinate axes.

You are given `N` distinct points on a plane. Count the number of different diamonds that can be constructed using these points as vertices (two diamonds are different if their sets of vertices are different). Do not count diamonds whose area is empty.

Write a function:

```python
def solution(X, Y)
```

that, given two arrays `X` and `Y`, each containing `N` integers, representing `N` points (where `X[K]`, `Y[K]` are the coordinates of the `K`-th point), returns the number of diamonds on the plane.

### Examples

1. For `N = 7` points whose coordinates are specified in arrays `X = [1, 1, 2, 2, 2, 3, 3]` and `Y = [3, 4, 1, 3, 5, 3, 4]`, the function should return `2`, since we can find two diamonds (the original statement shows a picture): the one with vertices `(1,3), (2,1), (3,3), (2,5)` and the one with vertices `(1,4), (2,3), (3,4), (2,5)`.
2. Given arrays `X = [1, 2, 3, 3, 2, 1]`, `Y = [1, 1, 1, 2, 2, 2]`, the function should return `0`, since there are no diamonds on the plane.

### Assumptions

- `N` is an integer within the range `[4..1,500]`;
- each element of arrays `X` and `Y` is an integer within the range `[0..N-1]`;
- given `N` points are pairwise distinct.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `diamonds_count.ipynb` | Centre-counting solution, brute-force check and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_3_2017_contest/04_diamonds_count/requirements.txt
jupyter lab codility/exercise_3_2017_contest/04_diamonds_count/diamonds_count.ipynb
```

## Hints

1. Four equal sides with axis-parallel diagonals means: a horizontal diagonal and a vertical diagonal that **cross at their common midpoint** (any lengths, both greater than 0).
2. Both midpoints must have integer coordinates, so a diamond is identified by its **centre** `(cx, cy)`.
3. For a centre, let `h` be the number of pairs of points on row `cy` symmetric about `cx`, and `v` the number of pairs on column `cx` symmetric about `cy`. That centre yields `h * v` diamonds.
4. Enumerate the pairs of points that share a row (sum of `k(k-1)/2` over rows is at most `N(N-1)/2`), then the pairs that share a column. Total O(N^2).
5. Compare with a brute force that tests every set of four points on small inputs.
