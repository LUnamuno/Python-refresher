# 01 - RectangleBuilderGreaterArea

**Codility:** [RectangleBuilderGreaterArea](https://app.codility.com/programmers/trainings/2/rectangle_builder_greater_area/) - Exercise 2, 2016 Contest

Count the different rectangular pens of area at least X that can be built from pieces of fence.

## Task description

Halfling Woolly Proudhoof is an eminent sheep herder. He wants to build a pen (enclosure) for his new flock of sheep. The pen will be rectangular and built from exactly four pieces of fence (so, the pieces of fence forming the opposite sides of the pen must be of equal length). Woolly can choose these pieces out of `N` pieces of fence that are stored in his barn. To hold the entire flock, the area of the pen must be greater than or equal to a given threshold `X`.

Woolly is interested in the number of different ways in which he can build a pen. Pens are considered different if the sets of lengths of their sides are different. For example, a pen of size `1x4` is different from a pen of size `2x2` (although both have an area of 4), but pens of sizes `1x2` and `2x1` are considered the same.

Write a function:

```python
def solution(A, X)
```

that, given an array `A` of `N` integers (containing the lengths of the available pieces of fence) and an integer `X`, returns the number of different ways of building a rectangular pen satisfying the above conditions. The function should return `-1` if the result exceeds `1,000,000,000`.

### Example

Given `X = 5` and the array `A = [1, 2, 5, 1, 1, 2, 3, 5, 1]` (four pieces of length 1, two of length 2, one of length 3 and two of length 5) the function should return `2`. The pens that can be built are of sizes `1x5` and `2x5`. Pens of sizes `1x1` and `1x2` can be built, but are too small in area. It is not possible to build pens of sizes `2x3` or `3x5`, as there is only one piece of fence of length 3.

### Assumptions

- `N` is an integer within the range `[0..100,000]`;
- `X` is an integer within the range `[1..1,000,000,000]`;
- each element of array `A` is an integer within the range `[1..1,000,000,000]`.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `rectangle_builder_greater_area.ipynb` | Counting solution, official example, brute force and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_2_2016_contest/01_rectangle_builder_greater_area/requirements.txt
jupyter lab codility/exercise_2_2016_contest/01_rectangle_builder_greater_area/rectangle_builder_greater_area.ipynb
```

## Hints

1. A pen is an unordered pair of lengths `{a, b}`: `a != b` needs at least **two** pieces of each length; `a == b` (a square) needs at least **four** pieces of that length.
2. Count the occurrences of every length (`Counter`). Keep the sorted list of distinct lengths that have at least two pieces.
3. Squares are counted separately: lengths with at least four pieces and `a * a >= X`.
4. For each length `a` in the sorted list, the valid partners `b > a` are those with `b >= ceil(X / a)`: they form a suffix of the list, found with `bisect`.
5. The count can reach about `1.25 * 10^9`, so return `-1` when it exceeds `10^9`. Complexity: O(N log N).
